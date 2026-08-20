---
name: cafe-picture-generator
description: Create or revise consistent commercial pictures of fresh café beverages from locked source photographs. Use for hot, iced, frappe, protein-drink, and slush SKUs; single-drink intake; CSV batches; or targeted picture corrections. Do not use for packaged drinks, food, logos, posters, or full scene redesigns.
---

# Cafe Picture Generator

Treat each request as a controlled edit of an approved source photograph. Do not create a new composition when a matching source format exists.

## Required references

- Read [references/production-spec.md](references/production-spec.md) before generating or correcting an image.
- Read [references/sheet-schema.md](references/sheet-schema.md) for CSV or spreadsheet work.

## Select the source format

Use the original matching asset:

| Format | Source asset |
| --- | --- |
| Hot | `assets/source-hot.png` |
| Iced | `assets/source-iced.png` |
| Frappe or milkshake | `assets/source-frappe.png` |
| Protein drink | `assets/source-protein.png` |
| Slush or frozen cooler | `assets/source-slush.png` |

If the required asset is missing, ask the user to supply an approved source photograph. Do not substitute an unrelated generated image.

Never use a generated SKU as the source for another SKU.

## Single-SKU workflow

Capture the following visible decisions:

1. SKU name and short description.
2. Format.
3. Left garnish.
4. Right garnish.
5. Back garnish.
6. Drink appearance and top treatment.
7. Garnish placement notes and special instructions.

Preserve fields the user already supplied. Ask only for missing decisions, one concise question at a time. Use native selection controls when available.

Offer garnish options only when they can be photographed as external objects. Use precise phrases such as `ripe mango slices`, `small clear bowl of matcha powder`, or `clear pitcher of milk`. Do not ask about sweetness, quantities, recipe steps, or invisible dissolved ingredients.

Treat `none` as an intentionally empty garnish zone.

## Batch workflow

1. Validate the sheet against [references/sheet-schema.md](references/sheet-schema.md).
2. Treat blank garnish cells as `none`.
3. Collect all blocking ambiguities in one consolidated question.
4. Generate each row independently from its original matching source asset.
5. Keep a completed and remaining checklist for large batches.
6. Put only the latest approved output for each SKU in the final folder.

Use `scripts/validate_sheet.py` for CSV validation and normalization before generation.

## Filenames

Unless the user supplies `output_filename`, derive it from the exact SKU name:

- lowercase the name;
- replace punctuation and whitespace runs with one hyphen;
- remove leading and trailing hyphens;
- retain meaningful numerals;
- add `.png` once.

Examples:

- `Iced Americano` becomes `iced-americano.png`.
- `Cocoa Protein 30` becomes `cocoa-protein-30.png`.
- `Watermelon Lime Slush` becomes `watermelon-lime-slush.png`.

## Correction workflow

Change only the named element. Rebuild the corrected image from the original source asset plus the full approved brief. Do not edit a failed render unless the user explicitly asks to preserve a unique feature that exists only in that render.

