# Checked Out? Australia's Public Libraries

A data story about how Australia's public libraries are changing, and who they serve. Built with
[Vega-Lite](https://vega.github.io/vega-lite/) and [Vega](https://vega.github.io/vega/) for FIT3179
Data Visualisation 2 (Monash University, Semester 2 2026).

**Live page:** https://usofertile.github.io/Australian-libraries/
**Sketch (PDF):** https://usofertile.github.io/Australian-libraries/sketch/sketch.pdf

## Repository layout

```
docs/                        ← GitHub Pages serves this folder
├── index.html               single scrolling page: story, 12 charts, metadata
├── css/style.css            layout (12-column grid), colour tokens, typography
├── js/main.js               embeds every chart and applies the shared chart theme
├── specs/                   one human-readable spec per chart (c01–c12; c07 is Vega)
├── data/                    processed CSV files the charts load (646 KB in total)
│   ├── geo/                 simplified council boundaries (GeoJSON) for the three maps
│   └── …                    plus the original source files (shapefiles are git-ignored)
└── sketch/sketch.pdf        scanned hand-drawn sketch (add this)
scripts/
├── build_story_data.py      builds the map boundaries and most chart CSVs from the sources
└── build_program_data.py    builds the library program and Victorian community CSVs
STORYBOARD.md                the design plan: story, idioms, layout, colour, typography, style
SUBMISSION.md                draft of the Moodle description (domain, why, who, what, how)
```

## Charts

| # | Chart | Idiom |
|---|---|---|
| C1 | Library visits by state | Tile grid map |
| C2 | A lifetime of library visits | Line chart |
| C3 | Women vs men | Butterfly chart |
| C4 | Cultural venues by income or education | Heatmap |
| C5 | WA's public libraries | Dot map + linked histogram |
| C6 | NSW borrowing by council | Proportional symbol map + Sydney inset |
| C7 | What NSW borrows | Treemap (Vega) |
| C8 | Victorian borrowing trends | Index line chart |
| C9 | Wi-Fi vs library computers | Isotype chart |
| C10 | Who attends library programs | Waffle charts |
| C11 | Victoria's community growth | Sorted bar chart |
| C12 | Queensland's bush libraries | Choropleth + linked scatterplot |

## Publishing with GitHub Pages

1. Commit and push to `main`.
2. On GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch**,
   then choose **Branch: `main`** and **Folder: `/docs`** and save.
3. After a minute the page is live at the URL above. Every push to `main` redeploys it.

`docs/.nojekyll` tells GitHub to serve the files as they are.

## Previewing locally

The charts load their specs and data with `fetch`, so opening `index.html` straight from disk will
not work. From the repo root run:

```
py -m http.server 8000 -d docs
```

then open http://localhost:8000.

## Rebuilding the data

```
py scripts/build_program_data.py
py scripts/build_story_data.py
```

Both need Python with `pandas`, `openpyxl` and `shapely`. The shapefile is read directly, so no GIS
packages are required. The raw ABS shapefiles (about 55 MB each) are excluded from git; download the
2025 Local Government Areas shapefile from the ABS into
`docs/data/Local Government Areas - 2025 - Shapefile/` to rebuild the map boundaries.

## Author

[Your full name], October 2026
