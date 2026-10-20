# FIT3179 Data Visualisation 2: Submission draft

Draft answers for the Moodle submission template. Review, edit into your own words, and copy into
the template.

## a. Visualisation URL

https://usofertile.github.io/Australian-libraries/

## b. Sketch PDF URL

https://usofertile.github.io/Australian-libraries/sketch/sketch.pdf

## c. Description

### i. Domain, why and who

- **Domain:** Australian public libraries.
- **Why:** Many people assume libraries are fading in a digital age. The page shows that libraries
  are used equally by every income group, that print lending is holding steady while digital lending
  grows faster, and that libraries are becoming learning and community hubs, especially for young
  children and rural towns.
- **Who:** The average Australian adult. No statistical or library knowledge is assumed; unfamiliar
  terms are explained on the page and in a glossary.

### ii. What: the data

| Dataset | Publisher | Period | Used for |
|---|---|---|---|
| [Cultural and Creative Activities](https://www.abs.gov.au/statistics/people/people-and-communities/cultural-and-creative-activities/2021-22) | Australian Bureau of Statistics | 2021–22 (latest) | Library visits by state, age, sex, income and education (C1–C4) |
| [Public Library Statistics](https://pls.sl.nsw.gov.au/managing-my-library/public-library-statistics) | State Library of NSW | 2024–25 | Loans by council and item type, internet use, programs (C6, C7, C9, C10) |
| [Annual Statistical Survey](https://www.plv.org.au/resources/) | Public Libraries Victoria | 2022–23 to 2024–25 | Three-year borrowing and community trends (C8, C11) |
| [Queensland public libraries statistics](https://www.data.gov.au/data/dataset/slq-qld-public-libraries-annual-statistics1) | State Library of Queensland | 2024–25 | Council-level visits, programs and digital loans (C10, C12) |
| [WA Public Libraries](https://catalogue.data.wa.gov.au/dataset/wa-public-libraries) | State Library of Western Australia | 2021 | Library locations (C5) |
| [Local Government Areas 2025](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/non-abs-structures/local-government-areas) | Australian Bureau of Statistics | 2025 | Map boundaries (C5, C6, C12) |

**Creation process:** Two Python scripts (`scripts/`) turn the source spreadsheets into small
chart-ready CSV files. They read the ABS council shapefile directly, simplify the boundaries for
three states into GeoJSON, and join council names to boundaries. Vision Australia is removed from
the Victorian totals so the three years compare like with like. The page loads 760 KB of data in
total.

### iii. How: idioms and rationale

| # | Chart | Idiom | Marks and channels | Task it supports |
|---|---|---|---|---|
| C1 | Visits by state | Tile grid map | Squares in a grid; colour luminance | Compare states fairly: equal tiles so the ACT and Tasmania are as visible as WA |
| C2 | Visits by age | Line chart | Line and points; position | See the rise and fall across a lifetime |
| C3 | Women vs men | Butterfly chart | Back-to-back bars; length, hue | Compare two groups at each age |
| C4 | Venues by income | Heatmap | Cells; colour luminance, printed values | Spot the one flat row (libraries) among rising rows |
| C5 | WA libraries | Dot map + linked histogram | Points on equal-area projection; brushing | Locate libraries; link distance to location |
| C6 | NSW borrowing | Proportional symbol map + inset | Circle area (total), colour (per resident) | Compare size and intensity by place without large rural areas dominating |
| C7 | What NSW borrows | Treemap (Vega) | Nested rectangles; area, hue by group | Part-to-whole across a two-level hierarchy |
| C8 | Victorian trends | Index line chart | Lines; position, hue | Compare growth of measures with different units |
| C9 | Wi-Fi vs computers | Isotype | Countable icons; hue | Make a 6-to-1 ratio concrete |
| C10 | Program audiences | Waffle charts | 100 squares; hue | "Out of 100" part-to-whole, compared across two states |
| C11 | Community growth | Sorted bar chart | Bars; length, hue vs population reference | Rank changes |
| C12 | Queensland councils | Choropleth + linked scatterplot | Areas ranked into fifths; points (position, hue, size) | Locate councils and see the programs vs digital trade-off |

**Totals:** 12 charts, 9 advanced idioms, 4 map idioms (dot, proportional symbol, choropleth, tile
grid). Maps use the Australian Albers equal-area projection.

**Special features:**
- Every chart shares one colour code: amber for digital, violet for children, teal for print.
- The heatmap has a "top ÷ bottom" ratio column calculated in Vega-Lite.
- The WA map computes each library's distance from Perth in the browser with the haversine
  formula, and brushing the histogram filters the map.
- The Wi-Fi and computer icons are custom SVG paths.
- Clicking a council in the Queensland map highlights it in the linked scatterplot, and the reverse.
- Chart controls (toggles, a checkbox and a dropdown) change what a chart shows; none swap sections.

### Use of generative AI

TODO: describe in your own words. Claude (Anthropic) was used to analyse the data, write the data
scripts, chart specifications and page code, and draft and edit text. Check against Monash's
acknowledgement requirements.

---

## Requirements checklist

- [x] At least 3 different map idioms with appropriate projections
- [x] More than 10 charts; at least 8 advanced idioms
- [x] Data combined from at least 2 sources, using the latest releases
- [x] All charts built with Vega-Lite or Vega; specs readable in `docs/specs/`
- [x] Total downloadable data under a few MB (760 KB)
- [x] Single scrolling page, no buttons that swap sections
- [x] Narrative text, annotations and glossary
- [ ] Replace every `[Your full name]` placeholder (index.html ×2, README)
- [ ] Review the generative AI acknowledgement on the page and here
- [ ] Hand-drawn sketch scanned to `docs/sketch/sketch.pdf`
- [ ] Commit, push, enable GitHub Pages (main → /docs) and test the live URL in a private window
- [ ] Check the page at 1280 px wide with no horizontal scroll
