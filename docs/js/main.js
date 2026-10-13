// Embeds every chart on the page. Each entry pairs a .chart element id in
// index.html with its specification in docs/specs/ (Vega-Lite, or Vega for C7).

const charts = [
  { id: "#c01", spec: "specs/c01_state_tilemap.vl.json" },
  { id: "#c02", spec: "specs/c02_lifetime_line.vl.json" },
  { id: "#c03", spec: "specs/c03_gender_butterfly.vl.json" },
  { id: "#c04", spec: "specs/c04_venue_heatmap.vl.json" },
  { id: "#c05", spec: "specs/c05_wa_dotmap.vl.json" },
  { id: "#c06", spec: "specs/c06_nsw_symbols.vl.json" },
  { id: "#c07", spec: "specs/c07_nsw_treemap.vg.json" },
  { id: "#c08", spec: "specs/c08_vic_index.vl.json" },
  { id: "#c09", spec: "specs/c09_wifi_isotype.vl.json" },
  { id: "#c10", spec: "specs/c10_program_waffle.vl.json" },
  { id: "#c11", spec: "specs/c11_vic_community_bars.vl.json" },
  { id: "#c12", spec: "specs/c12_qld_choropleth.vl.json" },
];

// Shared chart theme: matches the typography and colour tokens in css/style.css.
const theme = {
  background: null,
  padding: 4,
  font: "Source Sans 3",
  title: {
    font: "Fraunces",
    fontSize: 18,
    fontWeight: 600,
    anchor: "start",
    color: "#1f2328",
    subtitleFont: "Source Sans 3",
    subtitleFontSize: 13,
    subtitleColor: "#555b63",
    subtitlePadding: 6,
    offset: 14,
  },
  axis: {
    labelFont: "Source Sans 3",
    labelFontSize: 12,
    labelColor: "#555b63",
    titleFont: "Source Sans 3",
    titleFontSize: 12,
    titleFontWeight: 600,
    titleColor: "#555b63",
    domainColor: "#ddd5c8",
    tickColor: "#ddd5c8",
    gridColor: "#ebe5db",
  },
  legend: {
    labelFont: "Source Sans 3",
    labelFontSize: 12,
    labelColor: "#555b63",
    titleFont: "Source Sans 3",
    titleFontSize: 12,
    titleFontWeight: 600,
    titleColor: "#555b63",
  },
  header: {
    labelFont: "Fraunces",
    labelFontSize: 15,
    labelFontWeight: 600,
    labelColor: "#1f2328",
  },
  text: { font: "Source Sans 3", fontSize: 12, color: "#1f2328" },
  view: { stroke: null },
  range: { category: ["#1d4e5f", "#d08a2e", "#7b5ea7", "#5b7f3a", "#b8b2a7"] },
};

const embedOptions = { actions: false, renderer: "svg", config: theme };

for (const { id, spec } of charts) {
  const el = document.querySelector(id);
  if (!el) continue;
  vegaEmbed(el, spec, embedOptions).catch((err) => {
    console.error(`Failed to render ${spec}`, err);
    el.classList.add("chart--error");
    el.textContent = `This chart could not be loaded (${spec}).`;
  });
}
