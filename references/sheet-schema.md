# Batch sheet schema

Use this schema for `.csv` files and spreadsheet exports.

## Columns

| Column | Required | Accepted values or meaning |
| --- | --- | --- |
| `sku_name` | Yes | Exact customer-facing beverage name |
| `description` | Yes | Short product description |
| `format` | Yes | `hot`, `iced`, `frappe`, `protein`, or `slush` |
| `drink_appearance` | No | Visible colour, opacity, texture, layers, ice, or foam |
| `top_treatment` | No | Topping inside or on the drink; blank means none |
| `garnish_left` | No | External object on the left; blank means none |
| `garnish_right` | No | External object on the right; blank means none |
| `garnish_back` | No | External object behind the vessel; blank means none |
| `garnish_notes` | No | Count, containment, placement, and scale notes |
| `special_instructions` | No | Other visible requirements or exclusions |
| `output_filename` | No | Explicit `.png` filename; otherwise derived from `sku_name` |

## Validation rules

- Every required column must exist.
- Every row needs a unique, non-empty `sku_name`.
- `format` must use one accepted value.
- A garnish cannot occupy more than one zone unless `garnish_notes` explicitly asks for repetition.
- An explicit `output_filename` must end in `.png` and must not contain a directory path.
- Duplicate output filenames are blocking errors.
- Blank garnish fields normalize to `none`.
- Blank `output_filename` values normalize to lowercase kebab-case names derived from `sku_name`.

Validate the complete sheet before generating any image. Report all blocking errors together, grouped by row number or SKU name.

