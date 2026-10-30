---
name: principles-visual
description: Shape what people see. Use when designing or reviewing interfaces, layouts, typography, color, icons, images, 3D scenes, renders, video, or product appearance.
---

# Visual

In one line: Show what matters first, and give every color, effect, and container a job the observer can name.

**Visual design** arranges light and shape for an observer. Establish contrast and shape before detail so they see what matters first. In an interface, the content is the subject; controls, chrome, and branding serve it.

## Laws of the medium

- Value structure first. If it works in grayscale at thumbnail size, it can work in color.
- Content first. Controls, navigation, branding, and decoration defer to what the observer came to see.
- Every visual difference carries meaning. A color, weight, effect, border, or container marks one thing; applied everywhere, it marks nothing.
- Use the smallest difference that still reads. Group with space and alignment first, then tone, then lines and shadows.
- Draw each choice from a small system chosen for the content and observer: a type scale, a spacing scale, a corner rule, and a limited palette.
- Fewer, larger shapes beat many small ones. Sharp, high-contrast edges pull the eye; soft edges release it.
- Make light and materials consistent, and reference real ones before inventing them. Shadows, highlights, and reflections agree about the light sources.

## Defaults to replace

In images and scenes: stock gray backgrounds, centered everything, a single front light, an eye-level camera at a 50 mm lens, pure black and pure white, saturated primaries.

In interfaces: a gradient, glow, blur, or shadow on every surface; a card or border around every group; one corner radius at every level of nesting; accents in several hues, or a hue that means nothing; emoji standing in for a drawn icon set; an icon beside every heading; gray text too faint to read; thin weights at small sizes; one size and weight for every level, or many sizes with no scale; default type size and leading; spacing typed by feel; a logo on every screen; placeholder names and round numbers in place of real content; and the most common page template of the moment, such as a centered headline over three equal cards, kept with no reason.

## Tree

```
VISUAL
├── Form          shape, scale, proportion, position, orientation, surface geometry, corners, icons, optical alignment
├── Material      color, accent, effects, texture, roughness, reflectivity, transparency, emission
├── Energy        light: intensity, direction, color, softness, falloff
├── Observer      viewpoint, perspective, focal length, focus, exposure, optical effects, format, appearance, legibility, text size
├── Composition   hierarchy, content and chrome, spacing, grouping, alignment, balance, rhythm, framing, typography, real content
├── Time          motion, timing, transition, deformation
└── Atmosphere    depth cues, haze, scattering, environment
```

## Form

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Shape | Silhouette carries identity; a form should read as a solid black shape | Shapes that only read with detail | Fill it black. Is it still recognizable? |
| Scale | Size relative to known things tells the observer how big it is | No reference, so size is ambiguous | What familiar object sets the scale? |
| Proportion | Ratios between parts read before the parts | Parts sized one by one with no system | Name the ratios. Do they repeat? |
| Position | Placement implies relationship; near means related | Related items far apart, unrelated items touching | Does distance match relationship? |
| Orientation | Horizontal rests, vertical stands, diagonal moves | Tilt with no reason | Does each angle mean something? |
| Surface geometry | Curvature continuity decides how highlights flow | Breaks in curvature that show as kinks in reflections | Run a reflection or a stripe test |
| Corners | For rounded rectangles with circular corners and an even inset, the inner radius equals the outer radius minus the inset, down to zero, so both curves share a center | One radius at every level, so inner corners look pinched against their container | Does the visible gap between the curves stay even at the real size? Where shapes or insets differ, adjust by eye |
| Icons | An icon expresses one concept, simplified until it reads at its smallest size. A set shares one grid, stroke weight, corner style, and family of metaphors, and its weight matches the adjacent text | Icons from mixed sets; emoji standing in for icons; an icon where a word would be clearer | Set every icon in a row at actual size. Do they read as one family? Can a newcomer name each without its label? Label any that fail |
| Optical alignment | Align and size by what the eye sees, not by the bounding box. Round and pointed shapes overshoot a flat edge to look the same size, and a play triangle sits right of its geometric center | Shapes centered by measurement that look off | Blur or squint. Does it look centered and evenly sized? |

## Material

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Color | Value (light or dark) does the work; hue labels; saturation draws the eye. A color reads differently beside different neighbors | Hue doing the job value should do; a color chosen alone on a swatch | Convert to grayscale. Does the hierarchy hold? Judge each color beside its real neighbors |
| Accent | In an interface where the task comes first, reserve one accent for one role, usually what can be acted on, and keep the rest of the palette neutral. Add a color when it carries a distinct meaning or the expression the work intends | Several accents compete, or decoration uses the accent so actions hide | List each hue and the one thing it means or expresses. Is any hue doing two jobs or none? |
| Effects | Each effect says something: shadow shows elevation, blur shows a layer over content, a gradient shows light or depth, and an ornament carries the work's character. Use one where it says something this observer needs or the work intends | An effect on every surface, so it marks nothing and the content sinks behind it | Remove the effect. What did the observer lose? If nothing, leave it off |
| Texture | Texture scale must match object scale | Texture that reveals the true size is wrong | Does the texture belong at this size? |
| Roughness | Roughness decides highlight size and sharpness | Every surface equally glossy | Do surfaces differ the way real materials do? |
| Reflectivity | Reflections show the environment, so the environment is part of the design | Mirror surfaces reflecting nothing | What does it reflect, and is that chosen? |
| Transparency | Transparency shows a layer over something worth seeing. Text on it needs more contrast and weight than on a solid ground | Glass over empty space; faint text over a busy or moving background | What is seen through it? Does text on it read over the busiest content behind? |
| Emission | Emission is a light source; it should light its surroundings | Glowing parts that light nothing | Does the glow spill? |

Honest materials: a surface should look like what it is made of and behave that way.

## Energy (light)

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Intensity | The brightest point is where the eye goes first | Brightest spot on something unimportant | Where is the brightest area? Is it the subject? |
| Direction | Light from one side reveals form; front light flattens it | Flat front light on everything | Can you tell the form from shading alone? |
| Color | Warm against cool creates depth and separation | One temperature everywhere | Is there a key and fill temperature contrast? |
| Softness | Source size sets shadow edge; large source, soft edge | Hard shadows where the scene implies soft light | Does the shadow edge match the source? |
| Falloff | Light dims with distance; falloff directs attention | Even light that gives no focus | Does light lead the eye inward? |

## Observer

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Viewpoint | Camera height sets the relationship: low looks up, high looks down | Eye level by default | Why this height? |
| Perspective | Converging lines create depth and lead to a point | Lines leading out of the frame | Where do the lines point? |
| Focal length | Long lenses compress and flatter; wide lenses exaggerate | Wide lens on a product or face | Does the lens distort the subject? |
| Focus | Sharpness marks the subject; blur removes the rest | Everything sharp, so nothing is the subject | What is the sharpest thing? |
| Exposure | Keep detail where it matters; clip only on purpose | Lost highlights on the subject | Check the histogram on the subject |
| Optical effects | Flare, bloom, and aberration are realism cues; use sparingly | Effects hiding weak work | Is it better without them? |
| Format | Aspect ratio, resolution, and display gamut set the canvas | Designing for one screen, shown on another | Check at the real size, on the real device |
| Appearance | Define colors by role, such as text, background, separator, and accent, rather than by value. Each role then keeps its meaning in light, dark, and increased-contrast settings | A palette that works in one appearance only; a dark mode made by inverting values | View every screen in each appearance the platform offers. Does each role keep its contrast and meaning? |
| Legibility | Text needs contrast against its actual background and a weight heavy enough for its size. A 4.5:1 contrast ratio for body text is a common accessibility convention | Light gray text, thin weights at small sizes, text over busy images | Measure contrast on the real background. Is any small text set in a thin weight? |
| Text size | People enlarge text. The layout keeps its order and content at the largest size they can choose | Truncated labels, overlapping parts, or a hierarchy that flips at large sizes | Set text to the largest size. Does every label still read, and does the order hold? |

## Composition

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Hierarchy | One element first, then a clear second and third | Several elements competing for first | Squint. What do you see first, second, third? |
| Content and chrome | Content takes the space and the attention; controls sit quietly above or around it. Brand shows through accent, type, and voice more than through a repeated logo | Toolbars, banners, and logos take more of the first view than the content | What share of the first view is the thing the observer came for? |
| Spacing | Space groups; use a scale of spacing values | Spacing chosen per element | Are all spacings drawn from one scale? |
| Grouping | Space and alignment group items first. A container, such as a card, box, or tinted region, is for a group that must read as one object | A card around every group, so containers stop grouping and the page becomes a field of boxes | Remove a container. Do space and alignment still group the items? Then leave it off |
| Alignment | Shared edges create order and calm. Place edges on one grid of columns, gutters, and margins, and break it only on purpose | Near-misses a few pixels off; elements placed by eye | Overlay the grid. Does every edge land on it, and is every break chosen? |
| Balance | Visual weight balances around the center, symmetric or not | All the weight on one side with no reason | Flip it. Does it feel heavier one way? |
| Rhythm | Repetition with variation leads the eye | Monotony, or variation with no pattern | Is there a beat? |
| Framing | The edge of the frame is part of the composition | Tangents, cut limbs, crowded edges | Check each place the subject meets the edge |
| Typography | Type is shape first and words second. Use one or two families and a few sizes on a scale. Distinguish levels with the fewest effective changes in size, weight, or color. Adjust tracking and leading for the typeface, script, size, and line length | Many sizes and families, levels that differ in every property at once, crowded or loose display type, body lines too long | Count families and sizes. Set real text at each size. Is the hierarchy clear, and is anything crowded or broken? Check line length near 45 to 75 characters |
| Real content | Design with real content and its extremes: the longest name, the empty state, the largest number, another language | A layout that works only with placeholder text and round numbers | Replace every placeholder with real and worst-case content. What breaks? |

## Time

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Motion | Motion draws the eye harder than anything still; move only what matters. Keep motion on frequent actions brief or absent, and let people reduce it | Many things moving at once; a flourish on every tap; motion with no way to turn it down | What moves, and why? How often does each animation run, and what remains with reduced motion? |
| Timing | Speed implies mass; heavy things ease slowly | Linear motion that feels mechanical | Does the easing match the weight? |
| Transition | Transitions explain where things came from and went | Cuts or fades that lose the observer | Can you track each object across the change? |
| Deformation | Squash and stretch show material and force | Rigid objects stretching, soft ones not | Does deformation match the material? |

## Atmosphere

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Depth cues | Overlap, size, haze, and focus stack to show distance | One cue only, so depth is weak | How many depth cues agree? |
| Haze and scattering | Distance lowers contrast and shifts color toward the sky | Far objects as sharp and saturated as near ones | Does contrast drop with distance? |
| Environment | The world around the subject sets mood and reflections | Subject floating in a void | What world does this live in? |

## Learn from the best

Study work that has lasted, and name why it works in terms of the axes: Dieter Rams for restraint, Massimo Vignelli for type and grid discipline, Robert Bringhurst for typographic rhythm, Josef Albers for color in context, Susan Kare for icons at their real size, Edward Tufte for the smallest effective difference, and the platform's own human interface guidelines for its conventions. `principles-craft` sets the bar.

Pairs with: before `principles-method`, `principles-craft`; after `principles-verify`.
