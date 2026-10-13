"""Build tidy CSVs of public library program and community-activity data by state.

Run from the repo root:  py scripts/build_program_data.py

Inputs (docs/data/):
  public_library_statistics_2024-25_v3.xlsx                   State Library of NSW, 2024-25
  06.-2024-25-PLV-Annual-Statistical-Survey-...xlsx           Public Libraries Victoria, 2022-23 to 2024-25
  Queensland public libraries council data 2024-2025.csv      State Library of Queensland, 2024-25

Outputs (docs/data/):
  library_programs_by_state.csv       program sessions + attendance, one row per state/year/category
  vic_library_community_trends.csv    Victorian community-use measures across three years

Notes on comparability:
  - NSW classifies every program twice: by audience (sums to the NSW total) and by
    purpose (only ~90% of programs are classified, so it sums to less than the total).
  - QLD classifies each program once: either by age group (0-5, 6-12, 13-17) or by
    purpose. The two groups together sum to the QLD total. Children's storytime is
    therefore under "audience" in QLD but also under "Literacy & lifelong learning"
    in NSW, so purpose figures are not directly comparable between the two states.
  - Victoria reports total program/event attendance only (no sessions, no breakdown).
  - Vision Australia (a statewide library for people with print disability) is listed
    in every Victorian survey year, but its figures swing widely and some are only
    reported in some years. It is subtracted from every Victorian figure so the three
    years compare like with like across the 50 public library services.
"""
from pathlib import Path
import re

import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "docs" / "data"
NSW_FILE = DATA / "public_library_statistics_2024-25_v3.xlsx"
VIC_FILE = DATA / "06.-2024-25-PLV-Annual-Statistical-Survey-Final-Datasets-2022-23-to-2024-25.xlsx"
QLD_FILE = DATA / "Queensland public libraries council data 2024-2025.csv"

# Shared purpose categories (NSW and QLD both use these six).
PURPOSES = {
    "literacy": "Literacy & lifelong learning",
    "informed": "Informed & connected citizens",
    "digital": "Digital inclusion",
    "personal": "Personal development & wellbeing",
    "creative": "Stronger & creative communities",
    "economic": "Economic & workforce development",
}


def purpose_name(label):
    label = label.lower()
    return next(name for key, name in PURPOSES.items() if key in label)


def row(state, abbr, year, breakdown, category, sessions, attendance, population):
    return {
        "state": state, "state_abbr": abbr, "year": year, "breakdown": breakdown,
        "category": category, "sessions": sessions, "attendance": attendance,
        "population": population,
    }


# ---------- NSW ----------

def nsw_sheet(xl, name):
    """Return (header labels, NSW Total values) for a NSW sheet with paired columns."""
    sheet = next(s for s in xl.sheet_names if s.strip() == name)
    df = pd.read_excel(xl, sheet, header=None)
    # The "NSW Total" label sits in column 0, or column 1 on sheets with a rank column.
    for label_col in (0, 1):
        match = df[df.iloc[:, label_col].astype(str).str.strip() == "NSW Total"]
        if not match.empty:
            break
    header = [" ".join(str(v).split()) for v in df.iloc[3, label_col + 1:]]
    total = match.iloc[0, label_col + 1:]
    return header, [float(v) if pd.notna(v) else None for v in total]


def build_nsw():
    xl = pd.ExcelFile(NSW_FILE)
    S, A, Y = "New South Wales", "NSW", "2024-25"

    _, pop = nsw_sheet(xl, "Population")
    population = int(pop[-1])  # ERP at 30 June 2024, from table 9

    rows = []
    _, (sessions, attendance) = nsw_sheet(xl, "Library Programs")
    rows.append(row(S, A, Y, "total", "All programs", sessions, attendance, population))

    _, (online, views) = nsw_sheet(xl, "Online Library Programs")
    rows.append(row(S, A, Y, "online", "Online programs (views)", online, views, population))

    audience_names = {
        "Early Childhood": "Early childhood", "Children": "Children", "Young Adult": "Young adults",
        "Adults": "Adults", "Seniors": "Seniors", "Indigenous": "Aboriginal & Torres Strait Islander",
        "CALD Communities": "Culturally & linguistically diverse", "All Ages": "All ages",
    }
    header, values = nsw_sheet(xl, "Lib Program Audience")
    for i in range(0, len(header), 2):
        if header[i] in audience_names:
            rows.append(row(S, A, Y, "audience", audience_names[header[i]], values[i], values[i + 1], population))

    header, values = nsw_sheet(xl, "Lib Program Types & Attendance")
    for i in range(0, len(header), 2):
        if header[i] != "nan":
            rows.append(row(S, A, Y, "purpose", purpose_name(header[i]), values[i], values[i + 1], population))
    return rows


# ---------- Queensland ----------

def build_qld():
    df = pd.read_csv(QLD_FILE)
    df.columns = [" ".join(c.split()) for c in df.columns]
    t = df.select_dtypes("number").sum()
    S, A, Y = "Queensland", "QLD", "2024-25"
    population = int(t["POPULATION"])

    # Attendance headers are truncated (one ends "...COMMUNITIES AT") and spelled
    # differently from the session headers ("ANDLIFE LONG" vs "AND LIFELONG"). The
    # session columns always come before "PROGRAMS TOTAL SESSIONS" and attendance
    # columns after it, so split by position and pair by age group or purpose.
    cols = list(t.index)
    split = cols.index("PROGRAMS TOTAL SESSIONS")
    sessions = [c for c in cols[:split] if c.startswith("PROGRAMS")]
    attendance = [c for c in cols[split + 1:] if c.startswith("PROGRAMS") and "TOTAL" not in c]

    rows = [row(S, A, Y, "total", "All programs", t["PROGRAMS TOTAL SESSIONS"],
                t["PROGRAMS TOTAL SESSIONS ATTENDANCE"], population)]
    ages = {"0 TO 5": "Children 0–5", "6 TO 12": "Children 6–12", "13 TO 17": "Young adults 13–17"}
    for key, name in ages.items():
        s = next(c for c in sessions if key in c)
        a = next(c for c in attendance if key in c)
        rows.append(row(S, A, Y, "audience", name, t[s], t[a], population))
    for s in [c for c in sessions if "SUPPORT" in c]:
        name = purpose_name(s)
        a = next(c for c in attendance if "SUPPORT" in c and purpose_name(c) == name)
        rows.append(row(S, A, Y, "purpose", name, t[s], t[a], population))
    return rows


# ---------- Victoria ----------

VIC_METRICS = {
    "Municipal population": "Population",
    "branch library visits": "Branch library visits",
    "outreach program visits": "Outreach program visits",
    "Program/event attendance": "Program and event attendance",
    "book clubs": "Library book clubs",
    "local partnerships": "Local partnerships",
    "bookable meeting rooms": "Bookable meeting rooms",
    "hours booked": "Meeting room hours booked",
    "home library customers": "Home library service customers",
    "EY children per week": "Early years: children per week",
    "EY adults per week": "Early years: adults per week",
}


def vic_totals(year):
    df = pd.read_excel(VIC_FILE, sheet_name=year, header=3)
    df.columns = [" ".join(str(c).split()) for c in df.columns]
    names = df["Name"].astype(str).str.strip()
    total = df[names == "Victoria (Total)"].iloc[0]
    va = df[names == "Vision Australia"]
    out = {}
    for key, label in VIC_METRICS.items():
        cols = [c for c in df.columns if key.lower() in c.lower()]
        if not cols:
            continue  # measure not collected that year
        value = pd.to_numeric(total[cols[0]], errors="coerce")
        if not va.empty:
            value -= pd.to_numeric(va.iloc[0][cols[0]], errors="coerce") if pd.notna(va.iloc[0][cols[0]]) else 0
        out[label] = value
    return out


def build_vic():
    years = ["2022-23", "2023-24", "2024-25"]
    totals = {y: vic_totals(y) for y in years}
    program_rows = [
        row("Victoria", "VIC", y, "total", "All programs", None,
            totals[y]["Program and event attendance"], int(totals[y]["Population"]))
        for y in years
    ]
    trend_rows = [
        {"year": y, "metric": m, "value": int(round(v))}
        for y in years for m, v in totals[y].items() if pd.notna(v)
    ]
    return program_rows, trend_rows


if __name__ == "__main__":
    vic_programs, vic_trends = build_vic()
    programs = pd.DataFrame(build_nsw() + vic_programs + build_qld())
    programs["sessions"] = programs["sessions"].round().astype("Int64")
    programs["attendance"] = programs["attendance"].round().astype("Int64")

    programs.to_csv(DATA / "library_programs_by_state.csv", index=False)
    pd.DataFrame(vic_trends).to_csv(DATA / "vic_library_community_trends.csv", index=False)
    print(programs.to_string(index=False))
    print()
    print(pd.DataFrame(vic_trends).pivot(index="metric", columns="year", values="value").to_string())
