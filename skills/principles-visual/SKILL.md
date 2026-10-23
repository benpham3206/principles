---
name: principles-visual
description: Shape what people see. Use when designing or reviewing images, layouts, interfaces, 3D scenes, renders, video, or product appearance.
---

# Visual

**Visual design** arranges light and shape for an observer. Establish contrast and shape before detail so they see what matters first.

## Laws of the medium

- Value structure first. If it works in grayscale at thumbnail size, it can work in color.
- Make the lighting consistent. Shadows, highlights, and reflections should agree about the light sources.
- Edges direct attention. Sharp, high-contrast edges pull the eye; soft edges release it.
- Fewer, larger shapes beat many small ones.
- Reference real light and real materials before inventing them.

## Defaults to replace

Stock gray backgrounds, centered everything, a single front light, an eye-level camera at a 50 mm lens, default type size and leading, spacing typed by feel, pure black and pure white, saturated primaries.

## Tree

```
VISUAL
├── Form          shape, scale, proportion, position, orientation, surface geometry
├── Material      color, texture, roughness, reflectivity, transparency, emission
├── Energy        light: intensity, direction, color, softness, falloff
├── Observer      viewpoint, perspective, focal length, focus, exposure, optical effects, format
├── Composition   hierarchy, spacing, alignment, balance, rhythm, framing, typography
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

## Material

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Color | Value (light or dark) does the work; hue labels; saturation draws the eye | Hue doing the job value should do | Convert to grayscale. Does the hierarchy hold? |
| Texture | Texture scale must match object scale | Texture that reveals the true size is wrong | Does the texture belong at this size? |
| Roughness | Roughness decides highlight size and sharpness | Every surface equally glossy | Do surfaces differ the way real materials do? |
| Reflectivity | Reflections show the environment, so the environment is part of the design | Mirror surfaces reflecting nothing | What does it reflect, and is that chosen? |
| Transparency | Transparency shows layers; it needs something behind it worth seeing | Glass over empty space | What is seen through it? |
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

## Composition

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Hierarchy | One element first, then a clear second and third | Several elements competing for first | Squint. What do you see first, second, third? |
| Spacing | Space groups; use a scale of spacing values | Spacing chosen per element | Are all spacings drawn from one scale? |
| Alignment | Shared edges create order and calm | Near-misses, a few pixels off | Draw the edges. Do they line up? |
| Balance | Visual weight balances around the center, symmetric or not | All the weight on one side with no reason | Flip it. Does it feel heavier one way? |
| Rhythm | Repetition with variation leads the eye | Monotony, or variation with no pattern | Is there a beat? |
| Framing | The edge of the frame is part of the composition | Tangents, cut limbs, crowded edges | Check each place the subject meets the edge |
| Typography | Type is shape first and words second; a few sizes on a scale, set by measure and leading | Too many sizes, long lines, tight leading | Count sizes; check line length near 45 to 75 characters |

## Time

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Motion | Motion draws the eye harder than anything still; move only what matters | Many things moving at once | What moves, and why? |
| Timing | Speed implies mass; heavy things ease slowly | Linear motion that feels mechanical | Does the easing match the weight? |
| Transition | Transitions explain where things came from and went | Cuts or fades that lose the observer | Can you track each object across the change? |
| Deformation | Squash and stretch show material and force | Rigid objects stretching, soft ones not | Does deformation match the material? |

## Atmosphere

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Depth cues | Overlap, size, haze, and focus stack to show distance | One cue only, so depth is weak | How many depth cues agree? |
| Haze and scattering | Distance lowers contrast and shifts color toward the sky | Far objects as sharp and saturated as near ones | Does contrast drop with distance? |
| Environment | The world around the subject sets mood and reflections | Subject floating in a void | What world does this live in? |

Pairs with: before `principles-method`, `principles-qualities`; after `principles-verify`.
