# Production specification

Read this specification before every image generation or correction.

## Source-image contract

The source photograph locks all scene-level decisions:

- vessel identity, material, proportions, rim, base, and handle;
- vessel position and scale;
- camera position, focal length impression, and viewing angle;
- aspect ratio, framing, crop, and negative space;
- background colour and surface;
- lighting direction, softness, intensity, highlights, and reflections;
- contact shadow, cast shadow, and ambient shadow.

Only replace:

1. the beverage inside the vessel;
2. an explicitly requested top treatment;
3. explicitly requested external garnish objects.

Remove the source photograph's original ingredient props unless the new brief requests the same objects.

## Prompt contract

Every image-editing instruction should identify:

1. the exact source asset;
2. the requested drink colour, opacity, texture, temperature cues, ice, foam, layers, and viscosity;
3. the requested top treatment;
4. each garnish object and its left, right, or back zone;
5. all locked scene features that must remain unchanged;
6. the requirement for maximum source fidelity and realistic commercial beverage photography;
7. excluded objects.

Use concrete visual language. Replace `make it creamy` with observable details such as `opaque pale-beige liquid with moderate viscosity and a thin natural foam ring`.

## Format cues

### Hot

- Use plausible steam only when the product is served hot.
- Keep crema, microfoam, or whipped topping consistent with the drink.
- Avoid dense artificial steam clouds.

### Iced

- Use physically plausible ice size, refraction, and partial submersion.
- Preserve natural condensation without covering the vessel.
- Keep intentional layers distinct but not perfectly geometric.

### Frappe or milkshake

- Show blended viscosity without making the drink look solid.
- Whipped topping must have irregular folds and peaks.
- Avoid identical topping lobes or synthetic symmetry.

### Protein drink

- Show natural thickness and complete powder integration.
- Avoid dry powder clumps unless explicitly requested.
- Keep foam restrained unless the brief requires otherwise.

### Slush

- Show fine, densely packed ice crystals with plausible translucency.
- Avoid large crushed-ice chunks that read as an iced drink.
- Use natural colour variation rather than a flat neon fill.

## Garnish rules

- Keep external garnishes outside the vessel unless the brief defines a topping.
- Match the requested identity, quantity, zone, depth, scale, and container.
- Use natural asymmetry in cut, rotation, spacing, and size.
- Do not repeat one cloned ingredient shape.
- An empty zone must remain empty.

## Exclusions

Unless explicitly requested, include no:

- text or labels;
- logos;
- hands or people;
- straws, spoons, or napkins;
- unrelated ingredients;
- packaging;
- additional vessels.

## Verification checklist

Compare the result with both the source asset and approved brief.

- Source vessel is unchanged.
- Placement, angle, crop, and negative space match.
- Background, lighting, reflections, and shadows match.
- Drink colour, opacity, temperature cues, ice, foam, layers, and viscosity are plausible.
- Top treatment matches the brief.
- Every garnish is correct and in the correct zone.
- Empty zones remain empty.
- No excluded or unrequested object appears.
- Filename follows the approved rule.

If a material check fails, make one targeted correction from the original source asset. Do not correct by repeatedly editing the failed result.

