**Problem**
A café can shoot one SKU beautifully, but reshooting that quality across 20-100 menu items is slow and expensive. Uncontrolled AI generation is fast, but each generation tends to drift — a different glass, angle, crop, lighting or reflection than the last, so the menu stops looking like one brand.

**Who it's for**
Whoever owns menu/listing photography at scale — needs new SKU images fast without a photoshoot, without a designer manually correcting every AI output for consistency.

**Options considered**
Started with straight prompt-per-SKU generation from zero. It was inconsistent and hard to control — different backgrounds, odd garnish placement, shifting camera angles from one output to the next. Switching to reference-image editing instead of generation-from-scratch was the actual unlock: give the model an approved source photo and ask for one specific, narrow change (e.g. "change the drink from an iced americano to an iced toffee latte, keep the glass, framing, background and angle exactly the same," insisting on hyper-realism) rather than asking it to compose a new image each time. Garnish handling was added later, once the base approach was already working.

The real baseline being replaced: a professional shoot was quoted at AED 4,000 for the first 40 SKUs alone. Since then, 100+ additional SKUs have shipped through this system, plus a full rework of every existing image to add garnish — work a reshoot-based process would have re-quoted from scratch each time.

**Decision & trade-off**
Every new SKU generates from the original approved source photo, never from a previous generation. This wasn't a fix for observed drift — chaining generations was never the working approach in the first place; generating from a fixed reference was what made the output controllable at all, from the earliest tests.

Locked: vessel, camera angle, framing, background, lighting, shadows, crop. Allowed to change: only the beverage, ice/foam/layers, top treatment, and approved props. This constraint came directly from observed failure, not a general design instinct: without this exact instruction, outputs came back with genuinely different-looking photos — garnish placed inconsistently, backgrounds and camera angles shifting SKU to SKU. Locking those specific variables is what made the results consistent enough to hold a brand look across a menu.

**Outcome**
Cut image creation and processing time by ~75%, replacing a process that would have cost AED 4,000+ per 40-SKU batch in professional reshoots — and this system has now covered 140+ SKUs including a full garnish rework, across all five drink formats (hot, iced, frappe, protein, slush).

**What I would build next**
An evals agent to automatically QA each output against the fixed spec — white background, correct garnish structure, same glass as the reference, same camera angle — since some generations still come back not meeting the brief at all and currently need a human to catch that.
