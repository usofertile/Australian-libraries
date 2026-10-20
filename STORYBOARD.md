# Storyboard: "Checked Out?"

Plan for the FIT3179 Data Visualisation 2 page, written against the HD band of the rubric.
**Status: built** (October 2026). The live page in `docs/` follows this plan; corrections found while
building are marked *(corrected)*.
Every number quoted below comes from the files in `docs/data/`. Build each chart from the
processed data listed in [§7](#7-data-preparation), not by typing numbers into specs.

---

## 1. The idea in one page

| | |
|---|---|
| **Title** | **Checked Out?** |
| **Subtitle** | How Australia's public libraries are changing, and who they serve |
| **Domain** | Australian public libraries |
| **Who** | The average Australian adult. No statistics or library jargon assumed. |
| **Why** | Many people assume libraries are fading in a digital age. The data shows the opposite: libraries are used by every income group, print is holding steady while digital grows, and libraries are becoming learning and community hubs, especially for young children and in rural towns. The page helps readers see this and reconsider their local library. |
| **What** | ABS Cultural and Creative Activities 2021–22 (national, by state, age, sex, income, education) **combined with** 2024–25 state library statistics from NSW, Victoria (three years) and Queensland, WA library locations, and ABS 2025 council boundaries. |
| **Thesis** | Libraries haven't checked out. They've changed. |

**Story arc (five acts)**

| # | Section | Question it answers | Key insight |
|---|---|---|---|
| 0 | Hero | Are libraries still used? | 69 million visits in three states in one year |
| 1 | Who walks through the door? | Who uses libraries? | Kids most, young adults least, women more than men |
| 2 | Libraries are for everyone | Is it only well-off people? | The only cultural venue used equally across all incomes |
| 3 | Libraries reach every corner | Where are they, and where is borrowing highest? | From Perth to Kununurra; borrowing varies 10-fold between councils |
| 4 | Print holds steady, digital grows faster | What do people borrow now? | E-book loans up 36% in two years; children's books are the biggest category |
| 5 | More than books | What else do libraries do? | Under-fives fill half of all program seats; rural libraries are town meeting places |
| 6 | Conclusion | So what? | Three takeaways and a nudge to visit |

---

## 2. Rubric map: how this plan meets each HD criterion

| Criterion (weight) | HD requirement | How the plan meets it |
|---|---|---|
| Idioms and complexity (8%) | ≥ 8 advanced idioms across > 10 charts; ≥ 3 map idioms | **12 charts, 9 advanced idioms, 4 map idioms** (dot, proportional symbol, choropleth, tile grid). See [§4](#4-idiom-tally). Every idiom is chosen for a specific task (What/Why/How table in [§4](#4-idiom-tally)). |
| Layout, colour, figure-ground (3%) | Balanced, symmetric, columns/rows, white space, sight lines, clear hierarchy | 12-column grid, three layout patterns only, one left sight line for all text and chart edges, semantic colour system, grey context vs saturated focus. See [§5](#5-design-system). |
| Typography (2%) | Non-standard typeface matching the topic; excellent readability | Fraunces (a bookish old-style serif) for display, Source Sans 3 for reading, 18 px body, 1.65 line height, ≤ 68-character lines, left-aligned, tabular numbers. See [§5.3](#53-typography). |
| Storytelling, annotations, grammar, style (5%) | Clear engaging structure; extensive informative annotations; correct grammar; complete metadata | Claim-style headings, takeaway chart titles, 2–3 annotations on every chart, bridge sentences between sections, "How to read" hints for unfamiliar idioms, glossary, full metadata footer. See [§3](#3-section-by-section-storyboard) and [§6](#6-writing-style-guide). |
| Description (2%) | Domain, who, what, why, how succinctly described | §1 and §4 here feed straight into `SUBMISSION.md`. |
| Interview (3%) | Correct answers | Know the What/Why/How row of every chart ([§4](#4-idiom-tally)) and the data caveats ([§6.4](#64-data-notes-shown-in-the-footer)). |

Format rules from the brief that this plan respects: single scrolling page; no horizontal scroll at
1280 px; toggles only change what a chart shows (allowed), never swap sections; total data loaded
under 1.5 MB; all charts in Vega-Lite except the treemap (Vega, which the brief allows).

---

## 3. Section-by-section storyboard

Layout patterns used throughout (see [§5.1](#51-layout)):
**A** = wide chart (12 columns) · **B** = pair (6 + 6) · **C** = chart (8) + sidebar (4)

### Full-page wireframe

```
┌──────────────────────────────────────────────────────────────┐
│ HERO   kicker · CHECKED OUT? · subtitle · byline              │
│        intro paragraph (7 cols)                               │
│        [69 million visits] [1 in 3 a member] [1 in 4 digital] │
├──────────────────────────────────────────────────────────────┤
│ 01 WHO WALKS THROUGH THE DOOR?                                │
│ [C1 tile grid map ············· 8 ] [sidebar: how to read  4] │  C
│ [C2 lifetime line ········ 6 ] [C3 women vs men butterfly 6 ] │  B
├──────────────────────────────────────────────────────────────┤
│ 02 LIBRARIES ARE FOR EVERYONE                                 │
│ [C4 heatmap: venue × income / education ················ 12 ] │  A
│ ████ pull-quote band: the education gap ████████████████████ │
├──────────────────────────────────────────────────────────────┤
│ 03 LIBRARIES REACH EVERY CORNER                               │
│ [C5 WA dot map ················· 8 ] [distance histogram   4] │  C
│ [C6 NSW proportional symbols + Sydney inset ············ 12 ] │  A
├──────────────────────────────────────────────────────────────┤
│ 04 PRINT HOLDS STEADY, DIGITAL GROWS FASTER                   │
│ [C7 treemap: what NSW borrows ·························· 12 ] │  A
│ [C8 Victoria index lines ·· 6 ] [C9 isotype Wi-Fi vs PCs ·· 6 ] │  B
├──────────────────────────────────────────────────────────────┤
│ 05 MORE THAN BOOKS                                            │
│ [C10 waffles NSW | QLD ············· 8 ] [sidebar: early yrs 4] │  C
│ [C11 Victoria community growth bars ···················· 12 ] │  A
│ [C12 QLD choropleth ········ 6 ] [linked scatter ·········· 6 ] │  B
├──────────────────────────────────────────────────────────────┤
│ CONCLUSION  three takeaways (4 + 4 + 4) · call to action      │
├──────────────────────────────────────────────────────────────┤
│ FOOTER  sources · data notes · glossary · author · AI use     │
└──────────────────────────────────────────────────────────────┘
```

---

### 0 · Hero

**Kicker:** FIT3179 DATA VISUALISATION 2 · AUSTRALIA
**H1:** Checked Out?
**Standfirst:** How Australia's public libraries are changing, and who they serve.
**Byline:** By [full name] · October 2026

**Intro (draft):**
> Ask most Australians when they last borrowed a library book and many will say "at school".
> Yet in 2024–25, people in New South Wales, Victoria and Queensland walked into their public
> libraries 69 million times. Libraries haven't checked out. They've changed.

**Stat tiles** (three equal tiles, 4 + 4 + 4 columns, big Fraunces numerals):

| Number | Label | Basis |
|---|---|---|
| **69 million** | library visits in a year: 3.3 for every resident | NSW 28.2M + Vic 24.2M + Qld 16.9M, 2024–25 |
| **1 in 3** | residents is a library member | 6.86M members ÷ 20.9M people |
| **1 in 4** | loans in Victoria and Queensland is now digital | Vic 26%, Qld 28% |

---

### 1 · Who walks through the door?

**Standfirst:** One in five adults and one in three children visited a library in 2021–22. Who
goes depends on your age, your gender and where you live.

#### C1 · Tile grid map: library visits by state (Pattern C, 8 + 4)
- **Title:** Children are library regulars in every state
- **Subtitle:** % who visited a library or archive in the past 12 months, 2021–22
- **Idiom:** tile grid map (map idiom). Every state and territory is one equal square, so the ACT
  and Tasmania are as visible as WA. That suits rates per person, where land area is irrelevant.
- **Marks/channels:** square `rect` per state at fixed grid positions; colour luminance (teal
  sequential, same 0–45% scale for both groups); state abbreviation and % as text.
- **Interaction:** radio toggle **Adults | Children**. The fixed scale makes the switch visibly
  darker for children. Tooltip shows both values.
- **Annotations:**
  - WA: "43% of children, the highest in Australia"
  - NSW/Vic: "Lowest for adults (19% and 18%). Both states had long COVID lockdowns in 2021."
- **Sidebar (4 cols):** "How to read this map: each square is a state or territory, drawn the
  same size so small states are easy to compare." Plus the national figures: adults 20%, children 33%.
- **Data:** ABS tables 14 and 22.

#### C2 · Line: a lifetime of library visits (Pattern B, left)
- **Title:** Library use peaks at storytime age, dips in our twenties and returns with kids
- **Subtitle:** % who visited a library or archive in the past 12 months, by age, 2021–22
- **Idiom:** line with points (basic). The best idiom for a pattern across ordered age groups.
- **Values:** 5–8: 37 · 9–11: 34 · 12–14: 27 · 15–17: 28 · 18–24: **18** · 25–34: 19 · 35–44: **24** ·
  45–54: 19 · 55–64: **17** · 65–74: **23** · 75+: 20
- **Annotations** (phase labels above the line): "Storytime years", "Drifting away",
  "Back with their own kids", "Retirement".
- **Interaction:** checkbox "Show children's reading for pleasure" adds a dashed amber line for
  ages 5–14 (76%, 78%, 63%), annotated "Reading drops at 12–14 too". Tooltips on points.
- **Data:** ABS tables 16 and 23; table 9 for reading.

#### C3 · Butterfly chart: women and men (Pattern B, right)
- **Title:** Women visit more than men at every age
- **Subtitle:** % who visited a library or archive, people aged 15 and over, 2021–22
- **Idiom:** butterfly (back-to-back) chart. Shared age axis down the centre; men extend left,
  women right, so the gap reads directly at each age.
- **Marks/channels:** bars; length = %; hue = sex (women teal, men slate); age = vertical position.
- **Annotation** *(corrected)*: the gap is widest at 15–17 (34% vs 20%) and 35–44 (30% vs 17%); both rows
  are highlighted and labelled "Teenage years" and "Parenting years".
- **Data:** ABS table 16.

**Bridge:** "Age and gender shape who visits. Income, surprisingly, does not."

---

### 2 · Libraries are for everyone

**Standfirst:** Most cultural outings cost money, and it shows. Libraries are the exception.

#### C4 · Heatmap: cultural venues by income (Pattern A, wide)
- **Title:** Libraries are the only cultural venue used equally by rich and poor
- **Subtitle:** % of adults who attended in the past 12 months, by household income group, 2021–22
- **Idiom:** heatmap. Rows = 7 venue types, columns = 5 income groups (lowest to highest fifth).
  The eye compares whole rows at once: libraries form a flat band while every other row darkens
  to the right.
- **Marks/channels:** `rect`; colour luminance (teal sequential); % printed in each cell (white
  text on dark cells, ink on light cells); rows sorted by the gap between highest and lowest income.
- **Key values:** Libraries 20 → 21 · Art galleries 10.5 → 28.5 · Museums 9.5 → 25.5 ·
  Live music 9.2 → 26.3 · Theatre 4.8 → 13.4 · Musicals/opera 3.0 → 12.3 · Cinemas 26.7 → 54.6
- **Highlight:** Libraries row label bold, cells outlined in ink (2 px).
- **Interaction:** toggle **Income | Education**. Columns switch to 8 education levels.
- **Annotations:**
  - Libraries row: "20–21% in every income group"
  - Art galleries: "2.7 times as likely in the highest income group"
- **How to read:** "Darker = more people attended. Read across a row to see how attendance changes with income."
- **Data:** ABS tables 19 and 20.

**Pull-quote band** (full-bleed, dark teal background, paper-coloured Fraunces text):
> The one gap is education: 31% of people with a postgraduate degree visit a library,
> compared with 16% of those who left school at Year 10.

**Bridge:** "If libraries are for everyone, can everyone reach one?"

---

### 3 · Libraries reach every corner

**Standfirst:** From city branches to outback towns, public libraries stretch across the continent,
but how much people borrow varies hugely.

#### C5 · Dot map: WA's public libraries + linked distance histogram (Pattern C, 8 + 4)
- **Title:** 232 libraries across Australia's largest state
- **Subtitle:** Public libraries in Western Australia, mainland only
- **Idiom:** dot map. One dot per library at its real location over light LGA outlines.
  Linked histogram (basic) of distance from Perth, computed in Vega-Lite with a haversine
  `calculate`.
- **Projection:** Australian Albers equal-area (see [§5.5](#55-maps-projection-and-base-layers)).
- **Interaction:** brush on the histogram highlights those libraries on the map (others fade to
  grey). Tooltip: library name, suburb, distance from Perth.
- **Annotations:**
  - Perth cluster: "69 libraries (30%) within 50 km of Perth"
  - Kununurra: "Kununurra: 2,220 km from Perth"
  - Histogram: "21 libraries are more than 1,000 km from Perth"
- **Data:** `libraries location.csv` (Christmas and Cocos Islands excluded and noted); WA LGA TopoJSON.

#### C6 · Proportional symbol map: NSW borrowing (Pattern A, wide, with inset)
- **Title:** Borrowing per person varies more than ten-fold across NSW
- **Subtitle:** Loans per council in 2024–25. Circle size = total loans; colour = loans per resident
- **Idiom:** proportional symbol map. Circles at council centroids avoid the big-area bias of a
  choropleth, where huge, sparsely populated western councils would dominate.
- **Marks/channels:** `circle`; area = total loans (sqrt scale); colour = loans per resident
  (5 teal bins); white 0.5 px stroke so overlapping circles separate.
- **Layout:** NSW map (left) + **Greater Sydney inset** (right, same scales), signposted by a
  "see the inset" label. Lord Howe Island is dropped so the mainland fills the frame.
- **Annotations:**
  - Lane Cove: "15.6 loans per resident"
  - Fairfield: "1.4 loans per resident"
  - "Sydney, Inner West and The Hills each lend more than 1.5 million items"
- **Note under chart:** "Some councils share libraries, so very small councils can look unusually
  high or low."
- **Data:** NSW table 2e (127 councils) joined to LGA centroids.

**Bridge:** "So what are people borrowing?"

---

### 4 · Print holds steady, digital grows faster

**Standfirst:** E-books are the fastest-growing part of library lending, but they are adding to
print, not replacing it.

#### C7 · Treemap: what NSW borrowed (Pattern A, wide) · *Vega*
- **Title:** Children's books are the biggest thing libraries lend
- **Subtitle:** 35 million loans in NSW public libraries, 2024–25, by type of item (magazines excluded)
- **Idiom:** treemap. Shows part-to-whole across a two-level hierarchy (group → item type) in a
  space-efficient way; area is proportional to loans.
- **Hierarchy and colour:**
  - Children's and teen books (violet): picture books 6.0M, junior fiction 5.9M, junior
    non-fiction 1.6M, young adult 1.0M
  - Adult books (teal): adult fiction 7.7M, adult non-fiction 3.6M
  - Digital (amber): e-audiobooks 3.3M, e-books 2.8M, digital music 0.1M
  - Other physical (warm grey): DVDs 2.2M, CD audiobooks 0.3M, toys and games, kits, music
- **Annotations:**
  - "Children's and teen books: 14.5M loans, more than adult books (11.3M)"
  - "E-audiobooks outnumber CD audiobooks 10 to 1"
- **How to read:** "Each rectangle's size shows how many times that type of item was borrowed."
- **Interaction:** hover tooltip (item type, loans, % of total).
- **Data:** NSW tables 2b and 2c.

#### C8 · Index line chart: two years of change in Victoria (Pattern B, left)
- **Title:** E-book loans grew five times faster than physical loans
- **Subtitle:** Victoria, change since 2022–23 (2022–23 = 100)
- **Idiom:** multi-line (basic). Indexing puts measures with different units on one scale.
- **Lines (2024–25 end values, direct-labelled):** E-book loans **136** (amber) · Members 113 ·
  Physical loans 107 (teal) · Population 105 (dashed grey reference) · Physical collection 95
- **Annotations:** "Above the dashed line = grew faster than the population"; "Physical
  collection shrank 5% while loans rose".
- **How to read:** "100 is the 2022–23 level. 136 means 36% higher."
- **Interaction:** hover a line to highlight it and fade the rest; tooltip with real values.
- **Data:** PLV survey, Vision Australia excluded.

#### C9 · Isotype chart: Wi-Fi vs library computers (Pattern B, right)
- **Title:** Most people now bring their own device
- **Subtitle:** Internet sessions in NSW public libraries, 2024–25. Each icon = 500,000 sessions
- **Idiom:** isotype (pictogram). Countable icons make an abstract 6-to-1 ratio concrete for a
  general audience.
- **Marks/channels:** Wi-Fi icon × 23 (amber) vs desktop-computer icon × 4 (teal), in rows of 10.
- **Annotations:** "11.5 million Wi-Fi sessions" · "1.9 million computer bookings" ·
  "In Victoria, Wi-Fi hours rose 52% in two years."
- **Data:** NSW table 20; PLV survey.

**Bridge:** "Fewer people need a library computer. More need a place to learn and meet."

---

### 5 · More than books

**Standfirst:** Storytime, coding clubs, book groups, job help: libraries now run millions of
sessions a year, and the youngest Australians are their biggest audience.

#### C10 · Waffle charts: who attends library programs (Pattern C, 8 + 4)
- **Title:** Under-fives fill half of all library program seats
- **Subtitle:** Of every 100 people at a library program in 2024–25…
- **Idiom:** waffle chart (unit chart). 10 × 10 grids, one square = 1% of attendees, NSW and
  Queensland side by side. Easier than a pie for "out of 100" thinking.
- **Squares:**
  - NSW: early childhood 48 · children 16 · young adults 2 · adults 16 · seniors 4 · culturally and
    linguistically diverse 3 · Aboriginal and Torres Strait Islander 1 · all ages 10
  - Queensland: 0–5 years 58 · 6–12 years 18 · 13–17 years 1 · other programs 23
- **Colour:** violet family for children (dark = youngest), teal for adults/seniors, grey for other.
- **Annotation:** "Early childhood: 905,000 attendances in NSW, 875,000 in Queensland"
- **Interaction:** hover a category to highlight it in both waffles.
- **Footnote:** "NSW and Queensland group programs differently, so compare the children's
  categories rather than every square."
- **Sidebar (4 cols):** "Every week in 2024–25, about 15,700 Victorian children attended an
  early-years session at their library."
- **Data:** `library_programs_by_state.csv`; PLV survey.

#### C11 · Sorted bars: Victoria's community boom (Pattern A, wide)
- **Title:** Libraries are becoming community meeting places
- **Subtitle:** Victoria, % change from 2022–23 to 2024–25
- **Idiom:** horizontal bar sorted by change (basic). The clearest way to rank % changes.
- **Bars:** Meeting room hours booked **+74%** · Local partnerships +52% · Book clubs +43% ·
  Bookable rooms +28% · Program attendance +25% · Branch visits +20% · *Population +5%
  (reference rule)* · Home library customers −3%
- **Colour:** teal for growth above population, grey for the population reference, warm grey for
  decline.
- **Annotations:** "Meeting rooms: 256,000 hours booked, up from 148,000"; "Population grew 5%:
  everything to the right grew faster".
- **Data:** `vic_library_community_trends.csv`.

#### C12 · Choropleth + linked scatter: Queensland's bush libraries (Pattern B)
- **Title:** In the bush, the library is the town's meeting place
- **Subtitle:** Queensland councils, 2024–25, per resident
- **Idiom:** choropleth (left) linked to a scatterplot (right, basic). The map shows *where*; the
  scatter shows the trade-off: rural councils attend more programs but use fewer digital items.
- **Map:** LGA polygons; councils ranked into fifths on the selected measure ("Lowest fifth" to
  "Highest fifth", teal), which reads more easily than numeric quantile breaks; LGAs without data in grey.
- **Interaction:** dropdown **Program attendance | Visits | Digital loans** (per resident).
  Click a council on either view to highlight it in both. Tooltips with council name and values.
- **Scatter:** x = digital loans per resident (e-books, e-audio, e-video), y = program attendance per
  resident; colour = Rural Libraries Queensland councils (green) vs councils running their own service
  (slate); size = population; diamonds = each group's combined rate.
- **Annotations:**
  - Winton Shire: "4.8 program attendances per resident"
  - Boulia: "most digital loans per resident" (a rural shire: an honest exception)
  - *(corrected)* Rural vs other councils per resident: programs 0.55 vs 0.27 · visits 3.7 vs 3.1 ·
    digital loans 0.8 vs 1.8 (the earlier 3.1 included database use)
- **Note:** "Three outback shires record more than 20 visits per resident, likely boosted by
  visitors to these very small towns."
- **Data:** Queensland council CSV joined to QLD LGA TopoJSON.

---

### 6 · Conclusion: Libraries haven't checked out

Three equal columns (4 + 4 + 4), each a small icon, a bold one-line claim and one sentence:

1. **For everyone.** The only cultural venue used equally by every income group.
2. **Changing, not fading.** E-book loans rose 36% in two years while print lending still grew.
3. **A place to belong.** Half of all program seats go to under-fives, and rural towns use their
   library as a meeting place.

**Closing line** *(corrected: 55–64 year olds, not young adults, visit least)*: "If your last visit was
at school, you're in good company: library visits drop sharply once school ends. Your local library
is probably busier, and more useful, than you remember."

---

## 4. Idiom tally

| # | Chart | Idiom | Advanced? | Map? | What (data) | Why (task) | How (marks → channels) |
|---|---|---|---|---|---|---|---|
| C1 | Visits by state | Tile grid map | ✔ | ✔ | 8 states × 2 groups, rate | Compare states; adults vs children | rect → position (grid), luminance |
| C2 | Lifetime of visits | Line + points | — | | 11 ordered age groups, rate | Find trend and turning points | line/point → x position, y position |
| C3 | Women vs men | Butterfly chart | ✔ | | 8 ages × 2 sexes, rate | Compare two groups across age | bar → length, hue |
| C4 | Venues by income | Heatmap | ✔ | | 7 venues × 5 incomes (or 8 education levels), rate | Compare patterns; find the outlier row | rect → luminance, position |
| C5 | WA libraries | Dot map + linked histogram | ✔ | ✔ | 232 points (lat/lon); derived distance | Locate; see distribution | point → position (geo); bar → length |
| C6 | NSW borrowing | Proportional symbol map | ✔ | ✔ | 127 councils: loans, loans per resident | Compare magnitude by place; find extremes | circle → area, luminance, position (geo) |
| C7 | What NSW borrows | Treemap (Vega) | ✔ | | Hierarchy of 17 item types, loans | Part-to-whole; rank | rect → area, hue (group) |
| C8 | Victorian change | Index multi-line | — | | 5 measures × 3 years, index | Compare trends | line → position, hue |
| C9 | Wi-Fi vs PCs | Isotype | ✔ | | 2 counts | Compare magnitude | icon → count, hue |
| C10 | Program audiences | Waffle | ✔ | | Attendance shares by audience, 2 states | Part-to-whole; compare | square → count, hue |
| C11 | Community growth | Sorted bars | — | | 8 measures, % change | Rank | bar → length |
| C12 | Queensland bush | Choropleth + linked scatter | ✔ | ✔ | 62 councils × 3 per-resident measures | Locate; correlate | area → luminance; point → position, hue, size |

**Totals:** 12 charts · 9 advanced · 4 map idioms (3 geographic + tile grid) · 3 basic idioms.

Backup if a tutor disputes the butterfly or tile map as "advanced": swap C11 for a **slope chart
of rural vs larger Queensland councils** or present C8 as a **connected scatterplot** (physical
vs e-book loans over three years).

---

## 5. Design system

### 5.1 Layout
- **Grid:** 12 columns, 1080 px max content width, 24 px gutters, 24 px side padding.
  Fits a 1280 px laptop with no horizontal scroll; stacks to one column below 820 px.
- **Three patterns only** (A wide, B pair, C chart + sidebar) so the page has a predictable rhythm.
  Each section opens with heading + standfirst + body text on 7 columns, then figures.
- **Sight lines:** headings, body text, chart titles, axis starts and captions all share the left
  edge of the grid. In pairs, chart tops and titles align on one horizontal line; both charts in a
  pair have the same height.
- **White space:** 96 px between sections, 48 px between a text block and its figure, 32 px
  between paired charts. Nothing touches the edges.
- **Navigation:** optional slim sticky bar with section anchors (01–05) and a reading-progress
  line. Anchors scroll; they never swap content.

### 5.2 Colour

| Token | Hex | Used for |
|---|---|---|
| `--paper` | `#faf7f2` | Page background (warm, like book paper) |
| `--paper-alt` | `#f1ece3` | Sidebars, callouts, conclusion band |
| `--ink` | `#1f2328` | Headings, body text, annotation emphasis |
| `--ink-soft` | `#555b63` | Captions, axis labels, secondary text |
| `--rule` | `#ddd5c8` | Dividers, axis domain lines |
| `--print` | `#1d4e5f` | **Print/physical** and the default single-series colour |
| `--digital` | `#d08a2e` | **Digital**: e-books, e-audio, Wi-Fi (always this colour) |
| `--young` | `#7b5ea7` | **Children and early years** (lighter tints for older children) |
| `--rural` | `#5b7f3a` | Rural Libraries Queensland councils (C12 only) |
| `--context` | `#b8b2a7` | Non-focus data, references, "other" categories |
| `--men` | `#8a9bb0` | Men in C3 (women use `--print`); avoids pink/blue stereotypes |
| Sequential | `#e6efef → #0f3440` | One teal ramp for every map and the heatmap: darker = more |

Rules:
- **Same meaning, same colour, everywhere.** Digital is always amber, children always violet.
  The reader learns the code once.
- **Highlight by contrast, not by adding hues.** Focus data is saturated; everything else is
  `--context` grey.
- Teal, amber and violet stay distinguishable with the common forms of colour blindness. Check
  each chart with a simulator (e.g. Coblis) before submitting.
- Never rely on colour alone: every categorical colour also has a direct label or legend.

### 5.3 Typography

| Role | Font | Size / weight / line height |
|---|---|---|
| H1 title | Fraunces | clamp(2.6rem, 6vw, 4.25rem) / 700 / 1.05 |
| H2 section | Fraunces | 2.4rem / 600 / 1.15, preceded by amber section number |
| H3 / chart title | Fraunces | 1.25rem (charts: 18 px) / 600 |
| Standfirst | Source Sans 3 | 1.35rem / 400 / 1.5, `--ink-soft` |
| Body | Source Sans 3 | 1.125rem (18 px) / 400 / 1.65, max 68 characters per line |
| Caption, notes | Source Sans 3 | 0.9rem / 400 / 1.5, `--ink-soft` |
| Kicker | Source Sans 3 | 0.8rem / 600, uppercase, 0.12em letter-spacing, amber |
| Stat tile number | Fraunces | 3rem / 700, `font-variant-numeric: lining-nums tabular-nums` |
| Chart text | Source Sans 3 | axis 12 px, annotations 12.5 px (600 for the key number) |

- **Why Fraunces:** an old-style serif with a literary, printed-book character that matches the
  topic. Source Sans 3 is a highly legible humanist sans for long reading and small chart labels.
- All text left-aligned (no centred paragraphs). No underlines except links. Bold only for key
  numbers.

### 5.4 Chart styling and figure-ground
- No chart borders (`view.stroke: null`); light gridlines (`#e9e3d9`) on the value axis only.
- **Direct labels** instead of legends wherever possible (line ends, waffle categories).
- Axis titles only when units aren't in the subtitle. Remove redundant tick labels.
- Annotations: 12.5 px, ink colour, short leader lines (0.75 px `--ink-soft`), placed in empty
  space and never covering data. Two to three per chart, always containing a number.
- Every chart has: takeaway title (Fraunces) → subtitle with measure, place and year → chart →
  source line ("Source: ABS, Cultural and Creative Activities 2021–22").
- The page's key insight (§2 pull-quote) gets the strongest figure-ground contrast: a full-width
  dark teal band with paper-coloured text, used only once.

### 5.5 Maps: projection and base layers
- **Projection:** Australian Albers equal-area, the standard equal-area projection for national
  Australian maps (EPSG:3577). In Vega-Lite:
  `{"type": "conicEqualArea", "parallels": [-18, -36], "rotate": [-132, 0]}`. Equal-area keeps
  region sizes honest, which matters most for the choropleth.
- State outline (C5, C6 and the Sydney inset): the councils dissolved into one shape, drawn on top
  in ink at 40% opacity, 1 px, so the state stands out from the page. The C1 tiles get the same
  outline.
- Base layer: LGA outlines in `#ece6dc` with 0.4 px white borders. No-data areas use the same
  light fill plus a "No data" legend swatch.
- The tile grid map (C1) is deliberately projection-free and explained in its sidebar.

### 5.6 Interaction (all purposeful, none decorative)

| Chart | Interaction | Purpose |
|---|---|---|
| All | Formatted tooltips | Exact values on demand |
| C1 | Adults / Children toggle | Compare groups on one fixed scale |
| C2 | Show reading-for-pleasure checkbox | Optional second layer without clutter |
| C4 | Income / Education toggle | Reveal the one real gap |
| C5 | Brush histogram → highlight map | Link distance to location |
| C8 | Hover line → highlight | Isolate one trend |
| C10 | Hover category → highlight in both waffles | Compare states |
| C12 | Measure dropdown; click to link map ↔ scatter | Locate and compare councils |

---

## 6. Writing style guide

### 6.1 Voice and grammar
- Plain English for a general Australian reader. Active voice. Sentences under 25 words; paragraphs
  of 2–4 sentences.
- **Australian spelling:** visualisation, colour, centre, organise, program, licence (noun).
- Headings are **claims** in sentence case ("Libraries are for everyone"), not topics
  ("Income analysis").
- Chart titles state the takeaway; subtitles state the measure, place and year.
- No causal claims from correlations: write "rural councils attend more programs", not "being
  rural causes…".
- Proofread with LanguageTool or Grammarly, then read every paragraph aloud.

### 6.2 Numbers and dates
- Financial years with an en dash: **2024–25**. Survey year: **2021–22**.
- One to nine in words in prose; numerals from 10. Millions in prose: "24.2 million"; in charts: "24.2M".
- Percentages with the symbol: "36%". Per-resident figures to one decimal place.
- Round in prose ("about 1 in 4"), give exact values in tooltips.

### 6.3 Glossary (first use explained inline; full list in the footer)

| Term | Plain-English explanation |
|---|---|
| Loan | One item borrowed once, physical or digital |
| E-book / e-audiobook | A book or audiobook borrowed through a library app |
| Program | A library session such as storytime, a coding club or a seniors' tech class |
| Per resident | The total divided by the council's population |
| Index (2022–23 = 100) | 100 is the starting level; 136 means 36% higher |
| Library or archive | The ABS survey's category, which also includes archives |
| Rural Libraries Queensland | A State Library of Queensland program supporting small rural councils' libraries |
| Culturally and linguistically diverse | People from non-English-speaking backgrounds (avoid the acronym "CALD") |

### 6.4 Data notes (shown in the footer)
- ABS figures are from 2021–22, the latest release; NSW and Victoria had long lockdowns in 2021.
- ABS counts children's visits outside school hours only.
- Victorian figures exclude Vision Australia so years compare like with like.
- NSW and Queensland classify programs differently.
- Very small councils' per-resident figures can be inflated by visitors or shared libraries.
- WA map excludes Christmas Island and the Cocos (Keeling) Islands.

### 6.5 Metadata footer checklist
- [ ] Every dataset: title, publisher, year, URL
- [ ] Map boundaries: ABS LGA 2025 (ASGS Edition 3)
- [ ] Icons: source/licence (if not simple emoji)
- [ ] Author full name, date (October 2026), unit and university
- [ ] Generative AI acknowledgement (what was AI-assisted)
- [ ] Link to the GitHub repo and `docs/specs/` folder

---

## 7. Data preparation

Keep everything the page loads under **1.5 MB**. Processed files go in `docs/data/`
(TopoJSON in `docs/data/geo/`); scripts in `scripts/`.

| File | Built from | For | Size |
|---|---|---|---|
| `geo/wa_lga.geojson` | LGA shapefile → WA → simplified | C5 | 161 KB |
| `geo/nsw_lga.geojson` | LGA shapefile → NSW → simplified (finer in Sydney; Lord Howe Island dropped) | C6 | 263 KB |
| `geo/qld_lga.geojson` | LGA shapefile → QLD → simplified | C12 | 186 KB |
| `geo/wa_outline.geojson` | WA councils dissolved into one state outline | C5 | 53 KB |
| `geo/nsw_outline.geojson` | NSW and Greater Sydney councils dissolved into outlines | C6 | 61 KB |
| `abs_library_state.csv` | ABS tables 14, 22 + tile positions | C1 | <1 KB |
| `abs_library_age.csv` | ABS tables 9, 16, 23 | C2, C3 | 1 KB |
| `abs_venue_attendance.csv` | ABS tables 19, 20 | C4 | 3 KB |
| `wa_libraries.csv` | `libraries location.csv`, mainland only | C5 | 13 KB |
| `nsw_council_loans.csv` | NSW table 2e + council centroids | C6 | 7 KB |
| `nsw_loans_treemap.csv` | NSW tables 2b, 2c as an id/parent hierarchy | C7 | 2 KB |
| `vic_borrowing_trends.csv` | PLV survey (Vision Australia excluded) | C8 | 1 KB |
| `nsw_internet_access.csv` | NSW table 20 | C9 | <1 KB |
| `library_programs_by_state.csv` | NSW, PLV and QLD program data | C10 | 2 KB |
| `vic_library_community_trends.csv` | PLV survey (Vision Australia excluded) | C11 | 1 KB |
| `qld_council_measures.csv` | QLD council CSV + LGA name key | C12 | 7 KB |

**Total loaded by the page: 760 KB.** All files are rebuilt by `scripts/build_story_data.py` and
`scripts/build_program_data.py` (Python with pandas and shapely; the shapefile is read directly).

**Mapshaper** (web console at mapshaper.org, or CLI), per state:
```
-i LGA_2025_AUST_GDA2020.shp
-filter 'STE_NAME21 == "Queensland"'
-filter-fields LGA_CODE25,LGA_NAME25,AREASQKM
-simplify 3% keep-shapes
-o format=topojson qld_lga.topojson
```
Centroids for C6: `-points inner` then `-o format=csv`.

---

## 8. Build schedule (due Sunday 25 October, 11:55 pm)

| Date | Work |
|---|---|
| Wed 14 – Thu 15 Oct | Reconcile this plan with your submitted sketch; data prep (§7) |
| Fri 16 – Sun 18 Oct | Maps: C1, C5, C6, C12 |
| Mon 19 – Wed 21 Oct | C2–C4, C7–C11 |
| Thu 22 Oct | All narrative text and annotations |
| Fri 23 Oct | Layout, typography and colour pass; colour-blind check; 1280 px and 1366 px width test; page weight check |
| Sat 24 Oct | Proofread; metadata; AI acknowledgement; complete `SUBMISSION.md`; push; test the live URL in a private window |
| Sun 25 Oct | Buffer; submit on Moodle |
| Week 12 studio | Interview: rehearse the What/Why/How row for every chart (§4) and the data notes (§6.4) |
