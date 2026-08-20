const formats = { hot: "Hot", iced: "Iced", frappe: "Frappe", protein: "Protein", slush: "Slush" };
const samples = {
  hot: { skuName: "Cardamom Cloud Latte", description: "A hot milk coffee infused with cardamom.", appearance: "Opaque warm beige with fine microfoam and subtle steam", topTreatment: "Light cardamom dust", left: "Small natural cluster of green cardamom pods", right: "None", back: "None", notes: "Keep the steam restrained and realistic." },
  iced: { skuName: "Mango Matcha Iced Latte", description: "A layered mango, milk and matcha drink over clear ice.", appearance: "Golden mango base, white milk centre and green matcha top", topTreatment: "None", left: "Ripe mango slices", right: "Small clear bowl of matcha powder", back: "None", notes: "Keep the layers naturally uneven with light condensation." },
  frappe: { skuName: "Salted Caramel Frappe", description: "A blended coffee frappe with salted caramel.", appearance: "Thick pale caramel-brown blend", topTreatment: "Fresh whipped cream with irregular folds and caramel drizzle", left: "Caramel cubes", right: "Small clear jug of cream", back: "None", notes: "No straw. Avoid perfect topping symmetry." },
  protein: { skuName: "Cocoa Almond Protein Shake", description: "A chocolate almond protein drink.", appearance: "Opaque cocoa-brown shake with moderate natural thickness", topTreatment: "Light cocoa dust", left: "Whole almonds", right: "Small clear bowl of cocoa powder", back: "None", notes: "Show full powder integration and restrained foam." },
  slush: { skuName: "Watermelon Lime Slush", description: "A watermelon and lime frozen cooler.", appearance: "Translucent coral-red slush with fine, dense ice crystals", topTreatment: "None", left: "Fresh watermelon wedges", right: "Halved fresh limes", back: "None", notes: "No straw or mint. Keep the colour naturally varied." }
};

let selectedFormat = "iced";
let currentBrief = {};
const byId = (id) => document.getElementById(id);
const fields = { skuName: "sku-name", description: "description", appearance: "appearance", topTreatment: "top-treatment", left: "garnish-left", right: "garnish-right", back: "garnish-back", notes: "notes" };

function readBrief() {
  const brief = { format: selectedFormat };
  Object.entries(fields).forEach(([key, id]) => { brief[key] = byId(id).value.trim(); });
  return brief;
}

function setDraft() {
  byId("status").textContent = "Draft changed";
  byId("status").style.background = "#bcb7ad";
  byId("ready-output").hidden = true;
  byId("draft-output").hidden = false;
}

function loadSample(format) {
  selectedFormat = format;
  document.querySelectorAll("[data-format]").forEach((button) => button.classList.toggle("active", button.dataset.format === format));
  Object.entries(fields).forEach(([key, id]) => { byId(id).value = samples[format][key] || ""; });
  setDraft();
}

function productionPrompt(brief) {
  const value = (text) => text || "None";
  return [
    `Edit assets/source-${brief.format}.png to create “${brief.skuName}”, ${brief.description}`,
    "Replace only the beverage inside the locked vessel, its requested top treatment, and the approved external garnishes.",
    `Drink appearance: ${value(brief.appearance)}.`,
    `Top treatment: ${value(brief.topTreatment)}.`,
    `External garnishes — left: ${value(brief.left)}; right: ${value(brief.right)}; back: ${value(brief.back)}.`,
    brief.notes ? `Additional visible instructions: ${brief.notes}` : "",
    "Keep the source vessel, proportions, placement, camera angle, framing, white space, background, lighting, reflections, shadows and crop exactly unchanged.",
    "Use maximum input fidelity and hyper-realistic commercial beverage photography. Add no logos, text, hands, straws, spoons, napkins or unrequested objects."
  ].filter(Boolean).join("\n\n");
}

function renderOutput() {
  currentBrief = readBrief();
  byId("output-format").textContent = formats[currentBrief.format];
  byId("output-name").textContent = currentBrief.skuName;
  byId("prompt-output").textContent = productionPrompt(currentBrief);
  byId("ready-output").hidden = false;
  byId("draft-output").hidden = true;
  byId("status").textContent = "Ready";
  byId("status").style.background = "#d8ff45";
}

document.querySelectorAll("[data-format]").forEach((button) => button.addEventListener("click", () => loadSample(button.dataset.format)));
document.querySelectorAll("[data-sample]").forEach((button) => button.addEventListener("click", () => loadSample(button.dataset.sample)));
Object.values(fields).forEach((id) => byId(id).addEventListener("input", setDraft));
byId("brief-form").addEventListener("submit", (event) => { event.preventDefault(); renderOutput(); });
byId("clear-button").addEventListener("click", () => { byId("brief-form").reset(); selectedFormat = "iced"; document.querySelectorAll("[data-format]").forEach((button) => button.classList.toggle("active", button.dataset.format === "iced")); setDraft(); });
byId("copy-button").addEventListener("click", async () => { await navigator.clipboard.writeText(byId("prompt-output").textContent); byId("copy-button").textContent = "Copied ✓"; setTimeout(() => { byId("copy-button").textContent = "Copy prompt"; }, 1500); });
byId("download-button").addEventListener("click", () => { const blob = new Blob([JSON.stringify(currentBrief, null, 2)], { type: "application/json" }); const url = URL.createObjectURL(blob); const link = document.createElement("a"); link.href = url; link.download = `${currentBrief.skuName.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "drink-brief"}.json`; link.click(); URL.revokeObjectURL(url); });

loadSample("iced");
renderOutput();
