"""Build the small, chart-ready data files used by the web page.

Run from the repo root:  py scripts/build_story_data.py
Requires: pandas, openpyxl, shapely (no GIS packages needed; the shapefile is read directly).

Outputs in docs/data/ (see STORYBOARD.md §7):
  geo/wa_lga.geojson, geo/nsw_lga.geojson, geo/qld_lga.geojson   simplified council boundaries
  abs_library_state.csv      ABS library attendance by state (adults, children) + tile positions
  abs_library_age.csv        ABS library attendance by age and sex; children's reading for pleasure
  abs_venue_attendance.csv   ABS attendance at cultural venues by income and by education
  wa_libraries.csv           WA public library locations (mainland)
  nsw_council_loans.csv      NSW loans per council with map coordinates
  nsw_loans_treemap.csv      NSW loans by item type as an id/parent hierarchy
  nsw_internet_access.csv    NSW Wi-Fi and computer sessions
  qld_council_measures.csv   Queensland per-resident measures by council
  vic_borrowing_trends.csv   Victorian borrowing measures, 2022-23 to 2024-25 (indexed)
"""
import json
import re
import struct
from pathlib import Path

import pandas as pd
from shapely.geometry import LinearRing, MultiPolygon, Polygon, mapping
from shapely.geometry.polygon import orient

DATA = Path(__file__).resolve().parent.parent / "docs" / "data"
GEO = DATA / "geo"
SHP = DATA / "Local Government Areas - 2025 - Shapefile" / "LGA_2025_AUST_GDA2020"
NSW_FILE = DATA / "public_library_statistics_2024-25_v3.xlsx"
VIC_FILE = DATA / "06.-2024-25-PLV-Annual-Statistical-Survey-Final-Datasets-2022-23-to-2024-25.xlsx"
QLD_FILE = DATA / "Queensland public libraries council data 2024-2025.csv"
WA_FILE = DATA / "libraries location.csv"
ABS_ADULT = DATA / "cultural_and_creative_activities_202122_tables_14_to_21.xlsx"
ABS_CHILD = DATA / "cultural_and_creative_activities_202122_tables_22_to_24.xlsx"
ABS_CHILD_PART = DATA / "cultural_and_creative_activities_202122_tables_8_to_13.xlsx"

# Councils in the Sydney inset map (Greater Sydney minus its large outer bushland councils).
SYDNEY = {
    "Bayside", "Blacktown", "Burwood", "Camden", "Campbelltown", "Canada Bay", "Canterbury-Bankstown",
    "Cumberland", "Fairfield", "Georges River", "Hornsby", "Hunters Hill", "Inner West", "Ku-ring-gai",
    "Lane Cove", "Liverpool", "Mosman", "North Sydney", "Northern Beaches", "Parramatta", "Penrith",
    "Randwick", "Ryde", "Strathfield", "Sutherland", "Sydney", "The Hills", "Waverley", "Willoughby",
    "Woollahra",
}


def norm(name):
    """Normalise a council name so library data joins to ABS LGA names."""
    name = re.sub(r"\s*\((NSW|Qld|Vic\.|WA|SA|Tas\.|NT|ACT)\)", "", name)
    name = re.sub(r"\b(City|Regional|Shire|Aboriginal|Town|Council|Municipal|of)\b", "", name, flags=re.I)
    return re.sub(r"[^a-z]", "", name.lower())


# ---------------------------------------------------------------- shapefile

def read_dbf(path):
    with open(path, "rb") as f:
        _, _, _, _, n, header_len, record_len = struct.unpack("<BBBBIHH20x", f.read(32))
        fields = []
        while (d := f.read(32))[0] != 0x0D:
            fields.append((d[:11].split(b"\0")[0].decode(), d[16]))
        f.seek(header_len)
        rows = []
        for _ in range(n):
            rec, pos, row = f.read(record_len), 1, {}
            for name, size in fields:
                row[name] = rec[pos:pos + size].decode("latin-1").strip()
                pos += size
            rows.append(row)
    return pd.DataFrame(rows)


def read_shp(path):
    """Return a list of polygon ring lists (None for empty shapes)."""
    shapes = []
    with open(path, "rb") as f:
        f.seek(100)
        while len(header := f.read(8)) == 8:
            _, length = struct.unpack(">ii", header)
            content = f.read(length * 2)
            if struct.unpack("<i", content[:4])[0] == 0:
                shapes.append(None)
                continue
            n_parts, n_points = struct.unpack("<ii", content[36:44])
            parts = struct.unpack(f"<{n_parts}i", content[44:44 + 4 * n_parts])
            start = 44 + 4 * n_parts
            pts = struct.unpack(f"<{2 * n_points}d", content[start:start + 16 * n_points])
            coords = list(zip(pts[0::2], pts[1::2]))
            shapes.append([coords[a:b] for a, b in zip(parts, list(parts[1:]) + [n_points])])
    return shapes


def rings_to_geometry(rings):
    # Shapefiles store outer rings clockwise and holes anticlockwise.
    outers = [r for r in rings if len(r) >= 4 and not LinearRing(r).is_ccw]
    holes = [r for r in rings if len(r) >= 4 and LinearRing(r).is_ccw]
    owned = [[] for _ in outers]
    for h in holes:
        point = Polygon(h).representative_point()
        for i, o in enumerate(outers):
            if Polygon(o).contains(point):
                owned[i].append(h)
                break
    geom = MultiPolygon([Polygon(o, hs) for o, hs in zip(outers, owned)])
    return geom if geom.is_valid else geom.buffer(0)


def simplify(geom, tolerance, min_area, max_lon=180):
    geom = geom.simplify(tolerance, preserve_topology=True)
    parts = list(geom.geoms) if geom.geom_type == "MultiPolygon" else [geom]
    parts = [p for p in parts if p.centroid.x <= max_lon] or parts
    largest = max(parts, key=lambda p: p.area)
    kept = [p for p in parts if p.area >= min_area or p is largest]
    # d3-geo (used by Vega) expects clockwise outer rings, the reverse of RFC 7946.
    kept = [orient(p, sign=-1.0) for p in kept]
    return kept[0] if len(kept) == 1 else MultiPolygon(kept)


def rounded(obj, digits):
    if isinstance(obj, (list, tuple)):
        return [rounded(o, digits) for o in obj]
    return round(obj, digits)


def write_geojson(lga, shapes, state, path, tolerance, min_area, extra=None, max_lon=180):
    features = []
    for idx, row in lga[lga.STE_NAME21 == state].iterrows():
        if shapes[idx] is None:
            continue
        full = rings_to_geometry(shapes[idx])
        tol = tolerance(row) if callable(tolerance) else tolerance
        geom = mapping(simplify(full, tol, min_area, max_lon))
        geom = {"type": geom["type"], "coordinates": rounded(geom["coordinates"], 3)}
        props = {"name": row.LGA_NAME25, "code": row.LGA_CODE25}
        if extra:
            props.update(extra(row, full))
        features.append({"type": "Feature", "properties": props, "geometry": geom})
    path.write_text(json.dumps({"type": "FeatureCollection", "features": features}, separators=(",", ":")))
    return features


def build_geo():
    GEO.mkdir(exist_ok=True)
    lga = read_dbf(SHP.with_suffix(".dbf"))
    shapes = read_shp(SHP.with_suffix(".shp"))
    lga["key"] = lga.LGA_NAME25.map(norm)

    write_geojson(lga, shapes, "Western Australia", GEO / "wa_lga.geojson", 0.01, 0.002)
    write_geojson(lga, shapes, "Queensland", GEO / "qld_lga.geojson", 0.008, 0.001)

    sydney_keys = {norm(n) for n in SYDNEY}
    centroids = {}

    def nsw_extra(row, full):
        point = full.representative_point()
        centroids[row.key] = (round(point.x, 4), round(point.y, 4))
        return {"sydney": row.key in sydney_keys}

    write_geojson(
        lga, shapes, "New South Wales", GEO / "nsw_lga.geojson",
        lambda row: 0.0012 if row.key in sydney_keys else 0.007, 0.0004, nsw_extra,
        max_lon=154,  # drops Lord Howe Island, 600 km offshore, so the mainland fills the map
    )
    return lga, centroids, sydney_keys


# ---------------------------------------------------------------- ABS tables

def abs_values(path, sheet, label, section, block=None):
    """Numbers on the row `label` inside the `section` block (e.g. 'ATTENDANCE RATE')."""
    df = pd.read_excel(path, sheet_name=sheet, header=None)
    text = df.apply(lambda r: " ".join(str(v) for v in r if pd.notna(v)), axis=1).tolist()
    first = df.iloc[:, 0].astype(str).str.strip().tolist()
    start = next(i for i, t in enumerate(text) if t.startswith(section))
    if block:
        start = next(i for i in range(start, len(df)) if first[i] == block)
    row = next(i for i in range(start, len(df)) if first[i] == label)
    return [float(v) for v in df.iloc[row, 1:] if pd.notna(v)]


STATES = [  # abbreviation, name, tile column, tile row
    ("NSW", "New South Wales", 2, 1), ("Vic.", "Victoria", 2, 2), ("Qld", "Queensland", 2, 0),
    ("SA", "South Australia", 1, 1), ("WA", "Western Australia", 0, 1), ("Tas.", "Tasmania", 2, 3),
    ("NT", "Northern Territory", 1, 0), ("ACT", "Australian Capital Territory", 3, 1),
]
VENUES = {
    "Libraries or archives": "Libraries", "Art galleries": "Art galleries", "Museums": "Museums",
    "Cinemas": "Cinemas", "Live music concerts or performances": "Live music",
    "Theatre performances": "Theatre", "Musicals or operas": "Musicals & opera",
}
INCOME = ["Lowest", "Second", "Third", "Fourth", "Highest"]
EDUCATION = ["Postgraduate", "Graduate diploma", "Bachelor", "Diploma", "Certificate",
             "Year 12", "Year 11", "Year 10 or below"]  # ABS column order
EDUCATION_ORDER = list(reversed(EDUCATION))  # chart order: least to most formal education
ADULT_AGES = ["15–17", "18–24", "25–34", "35–44", "45–54", "55–64", "65–74", "75+"]
CHILD_AGES = ["5–8", "9–11", "12–14"]


def build_abs():
    adults = abs_values(ABS_ADULT, "Table 14", "Libraries or archives", "ATTENDANCE RATE")
    children = abs_values(ABS_CHILD, "Table 22", "Libraries or archives", "ATTENDANCE RATE")
    pd.DataFrame([
        {"state": a, "state_name": n, "tile_col": c, "tile_row": r, "adults": adults[i], "children": children[i]}
        for i, (a, n, c, r) in enumerate(STATES)
    ]).to_csv(DATA / "abs_library_state.csv", index=False)

    rows = []
    kids = abs_values(ABS_CHILD, "Table 23", "Libraries or archives", "ATTENDANCE RATE")
    reading = abs_values(ABS_CHILD_PART, "Table 9", "Reading for pleasure", "PARTICIPATION RATE")
    for i, age in enumerate(CHILD_AGES):
        rows.append({"age": age, "order": i, "group": "Persons", "measure": "Visited a library", "rate": kids[i]})
        rows.append({"age": age, "order": i, "group": "Persons", "measure": "Reads for pleasure", "rate": reading[i]})
    for group in ["Persons", "Males", "Females"]:
        values = abs_values(ABS_ADULT, "Table 16", "Libraries or archives", "ATTENDANCE RATE", block=group)
        for i, age in enumerate(ADULT_AGES):
            rows.append({"age": age, "order": i + 3, "group": group, "measure": "Visited a library", "rate": values[i]})
    pd.DataFrame(rows).to_csv(DATA / "abs_library_age.csv", index=False)

    rows = []
    for label, short in VENUES.items():
        income = abs_values(ABS_ADULT, "Table 20", label, "ATTENDANCE RATE")
        for i, g in enumerate(INCOME):
            rows.append({"venue": short, "breakdown": "Income", "group": g, "order": i, "rate": income[i]})
        education = abs_values(ABS_ADULT, "Table 19", label, "ATTENDANCE RATE")
        for i, g in enumerate(EDUCATION):
            rows.append({"venue": short, "breakdown": "Education", "group": g,
                         "order": EDUCATION_ORDER.index(g), "rate": education[i]})
    pd.DataFrame(rows).to_csv(DATA / "abs_venue_attendance.csv", index=False)


# ---------------------------------------------------------------- NSW

def nsw_sheet(name):
    xl = pd.ExcelFile(NSW_FILE)
    return pd.read_excel(xl, next(s for s in xl.sheet_names if s.strip() == name), header=None)


def nsw_total(name):
    """{column header: NSW Total value} for a NSW sheet with one header row of column names."""
    df = nsw_sheet(name)
    header_row = next(i for i in range(8) if df.iloc[i, 1:].map(lambda v: isinstance(v, str)).sum() >= 2)
    headers = [" ".join(str(v).split()) for v in df.iloc[header_row, 1:]]
    total = df[df.iloc[:, 0].astype(str).str.strip() == "NSW Total"].iloc[0, 1:]
    return {h: float(v) for h, v in zip(headers, total) if pd.notna(v) and h != "nan"}


def build_nsw(centroids, sydney_keys):
    df = nsw_sheet("Circulation by Council").iloc[4:131, :4].dropna()
    df.columns = ["council", "population", "loans", "loans_per_resident"]
    df["council"] = df.council.astype(str).str.strip().replace({"Hills, The": "The Hills"})
    df["key"] = df.council.map(norm)
    df[["lon", "lat"]] = df.key.map(centroids).apply(pd.Series)
    df["sydney"] = df.key.isin(sydney_keys).map({True: "true", False: "false"})  # Vega reads lowercase booleans
    df["population"] = df.population.astype(int)
    df["loans"] = df.loans.astype(int)
    df["loans_per_resident"] = df.loans_per_resident.astype(float).round(2)
    missing = df[df.lon.isna()].council.tolist()
    assert not missing, f"NSW councils without a boundary: {missing}"
    df.drop(columns="key").to_csv(DATA / "nsw_council_loans.csv", index=False)

    books = nsw_total("Circulation by Books Category")
    other = nsw_total("Circulation of Non-Book")
    leaves = [
        ("Children's & teen books", "Picture books", books["Picture Easy Fiction"] + books["Picture Easy Non Fiction"]),
        ("Children's & teen books", "Junior fiction", books["Junior Fiction"]),
        ("Children's & teen books", "Junior non-fiction", books["Junior Non Fiction"]),
        ("Children's & teen books", "Young adult", books["Young Adult Fiction"] + books["Young Adult Non Fiction"]),
        ("Adult books", "Adult fiction", books["Adult Fiction"]),
        ("Adult books", "Adult non-fiction", books["Adult Non Fiction"]),
        ("Digital", "E-audiobooks", other["E Audio Book Downloads"]),
        ("Digital", "E-books", books["E Books"]),
        ("Digital", "Digital music", other["Digital Music Downloads"]),
        ("Other items", "DVDs and film", other["DVDs, Video & Film"]),
        ("Other items", "CD audiobooks", other["Audio Books: Spoken Word CD's, mp3 and Cassettes"]),
        ("Other items", "Music CDs", other["Music Recordings"]),
        ("Other items", "Toys and games", other["Toys and Games"]),
        ("Other items", "Language kits", other["Language Learning Kits"]),
        ("Other items", "Other", other["Other Non Book"]),
    ]
    total = sum(v for *_, v in leaves)
    rows = [{"id": "root", "parent": "", "name": "All loans", "group": "", "loans": None, "total": int(total), "share": 1}]
    for group in dict.fromkeys(g for g, *_ in leaves):
        group_total = sum(v for g, _, v in leaves if g == group)
        rows.append({"id": group, "parent": "root", "name": group, "group": group,
                     "loans": None, "total": int(group_total), "share": round(group_total / total, 4)})
    for group, name, value in leaves:
        rows.append({"id": name, "parent": group, "name": name, "group": group,
                     "loans": int(value), "total": int(value), "share": round(value / total, 4)})
    pd.DataFrame(rows).to_csv(DATA / "nsw_loans_treemap.csv", index=False)

    net = nsw_total("Internet Public Access")
    pd.DataFrame([
        {"type": "Wi-Fi sessions", "sessions": int(net["No. of Wireless Access Bookings"])},
        {"type": "Library computer bookings", "sessions": int(net["No. of Internet Access Bookings"])},
    ]).to_csv(DATA / "nsw_internet_access.csv", index=False)


# ---------------------------------------------------------------- Queensland

def build_qld(lga):
    df = pd.read_csv(QLD_FILE)
    df.columns = [" ".join(c.split()) for c in df.columns]
    df["council_name"] = df.COUNCIL.str.replace("Regioinal", "Regional")  # typo in source
    keys = dict(zip(lga[lga.STE_NAME21 == "Queensland"].key, lga[lga.STE_NAME21 == "Queensland"].LGA_NAME25))
    digital = df[["USAGE EBOOK", "USAGE EAUDIO", "USAGE EVIDEO", "USAGE OTHER DIGITAL ITEMS"]].sum(axis=1)
    out = pd.DataFrame({
        "council": df.council_name.str.replace(r"\s+Council$", "", regex=True),
        "lga_name": df.council_name.map(norm).map(keys),
        "group": df.SERVICE.map({"RLQ": "Rural Libraries Queensland", "IND": "Runs its own library service"}),
        "population": df.POPULATION,
        "visits": df["USAGE PHYSICAL VISITS"],
        "program_attendance": df["PROGRAMS TOTAL SESSIONS ATTENDANCE"],
        "digital_loans": digital,
        "physical_loans": df["USAGE TOTAL PHYSICAL ITEMS"],
    })
    for col, new in [("visits", "visits_pr"), ("program_attendance", "programs_pr"),
                     ("digital_loans", "digital_pr"), ("physical_loans", "physical_pr")]:
        out[new] = (out[col] / out.population).round(2)
    out.to_csv(DATA / "qld_council_measures.csv", index=False)
    return out


# ---------------------------------------------------------------- WA, Victoria

def build_wa():
    df = pd.read_csv(WA_FILE)
    df = df.rename(columns={"Name": "name", "Street Suburb": "suburb",
                            "Latitude (Decimal)": "lat", "Longitude (Decimal)": "lon"})
    df[["lat", "lon"]] = df[["lat", "lon"]].apply(pd.to_numeric, errors="coerce")
    df = df[df.lon.between(112, 130)]  # mainland: drops Christmas and Cocos (Keeling) Islands
    df[["name", "suburb", "lat", "lon"]].to_csv(DATA / "wa_libraries.csv", index=False)


VIC_MEASURES = {
    "Population": "Municipal population",
    "E-book loans": "loans of ebooks",
    "Physical loans": "loans of physical items",
    "Members": "Total number of members",
    "Physical collection": "Total number of physical items",
}


def build_vic():
    rows = []
    for year in ["2022-23", "2023-24", "2024-25"]:
        df = pd.read_excel(VIC_FILE, sheet_name=year, header=3)
        df.columns = [" ".join(str(c).split()) for c in df.columns]
        names = df["Name"].astype(str).str.strip()
        total = df[names == "Victoria (Total)"].iloc[0]
        va = df[names == "Vision Australia"]  # excluded so years compare like with like
        for measure, key in VIC_MEASURES.items():
            col = next(c for c in df.columns if key.lower() in c.lower() and "for loan" not in c.lower())
            value = float(total[col])
            if not va.empty and pd.notna(pd.to_numeric(va.iloc[0][col], errors="coerce")):
                value -= float(va.iloc[0][col])
            rows.append({"year": year, "measure": measure, "value": int(round(value))})
    out = pd.DataFrame(rows)
    base = out[out.year == "2022-23"].set_index("measure").value
    out["index"] = (out.value / out.measure.map(base) * 100).round(1)
    out.to_csv(DATA / "vic_borrowing_trends.csv", index=False)


if __name__ == "__main__":
    lga, centroids, sydney_keys = build_geo()
    build_abs()
    build_nsw(centroids, sydney_keys)
    qld = build_qld(lga)
    build_wa()
    build_vic()

    print("Queensland councils without a boundary:", qld[qld.lga_name.isna()].council.tolist())
    for f in sorted(list(DATA.glob("*.csv")) + list(GEO.glob("*.geojson"))):
        if f.name[0].islower() and f.stat().st_size < 2_000_000:
            print(f"{f.stat().st_size / 1024:8.1f} KB  {f.relative_to(DATA)}")
