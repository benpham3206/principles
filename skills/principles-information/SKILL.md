---
name: principles-information
description: Principles of showing information (charts, diagrams, tables, dashboards, maps, technical drawings, data slides), organized on the six axes plus truth. Use when choosing a chart, encoding data, designing a dashboard or table, labeling a figure, or critiquing whether a display is honest and readable.
---

# Information

An **information display** is data or structure arranged so a reader can answer a question and act on it. The reader first looks for the answer to their own question, so the display succeeds when that answer is the first thing found and the thing found is true. For how marks look (color values, type, spacing), use `principles-visual`; this skill covers what the marks encode. To choose which structure a problem should take before it is drawn, use `principles-represent`.

## Tree

```
INFORMATION
├── Form          encoding (what carries the value), chart type (what question it answers)
├── Material      marks, data ink, color scheme, contrast
├── Energy        salience: the one finding, the gray context
├── Observer      the reader's question, expertise, decision, distance, medium
├── Composition   order, grouping, aligned scales, small multiples, labels, title
├── Time          updates, history, change over time, animation, staleness
└── Truth         scales, units, uncertainty, source, date, precision, the map and the territory
```

## Form

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Encoding rank | Established perceptual ranking, most to least accurate: position on a common scale, length, angle and slope, area, then color intensity and hue. Encode the value that matters most with the highest-ranked channel | Key value on color or area while position carries a minor field | List each variable and its channel. Is the main comparison on position or length? |
| Chart type | The question picks the form: compare (bars or dots), trend (lines), part of whole (stacked bar or a few labeled shares), distribution (histogram or box), relationship (scatter) | A familiar chart type chosen first, question second | State the question in one sentence. Does this form answer it directly? |
| Part of whole | Angle and area are read poorly; shares compare best as aligned lengths | Pie with many slices or similar sizes | Can the reader rank the parts without reading the labels? |
| Dimensionality | Extra dimensions carry no data and distort length and area | Three-dimensional bars, tilted pies | Does any depth or tilt encode a variable? If not, remove it |
| Dual axes | Two vertical scales on one plot let the author pick any apparent correlation | Two series scaled until they appear to track each other | Would the picture change if one scale were rescaled? Then split the plot |
| Diagram form | A diagram shows structure: containment, flow, sequence, hierarchy. Each line type means one relation | Boxes and arrows where arrows mean several things | Name what each arrow, line style, and box shape means |

## Material

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Marks | Points, bars, lines, and cells carry data. Size marks so each is separable and countable | Overplotted points; bars thinner than their gaps | Can you count or isolate individual marks? |
| Data ink | Ink that encodes data stays; gridlines, borders, fills, and ticks that carry nothing are lightened or cut | Heavy frames and grids rivaling the data | Remove an element. Does any reading change? If not, it goes |
| Color scheme | Categorical color for unordered groups (distinct hues, few); sequential for ordered magnitude (one hue, light to dark); diverging for values around a meaningful midpoint (two hues, neutral center) | A rainbow for ordered data; categories in a sequential ramp | Is the data nominal, ordered, or centered? Does the scheme match? |
| Category count | People can match only a handful of hues to a legend | Ten colors in one chart | Count the hues. Past about five (a rule of thumb), group, label directly, or facet |
| Redundant coding | Color alone fails for readers with color-vision differences and for grayscale print | Groups separated by red versus green only | Convert to grayscale and simulate color-vision loss. Do groups still separate? |
| Contrast | Text and marks need enough contrast against the background to read at the real size and in the real light | Light gray labels on white | Measure the contrast ratio of text and of key marks against the background |

## Energy

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Salience | Emphasis is a budget: highlight the one finding in a strong color or weight and gray the context | Every series in a saturated color, so none leads | Name the finding. Is it the most salient mark, and the only one? |
| Annotation | A short note placed at the point of interest tells the reader what to see | The reader must infer the story from the shape | Is the key point labeled where it occurs? |
| Reference marks | A target, average, or threshold line gives a value its meaning | Numbers shown with nothing to compare to | Against what is this value good or bad? Is that mark present? |
| Alarm | Reserve alarm color and motion for states that need action | Red used for decoration, so real alerts vanish | How often is the alarm style on? If often, it signals nothing |
| Density | Detail is available on demand, not forced on every reader at once | All values, labels, and series on one view | What can sit behind a hover, a drill-down, or an appendix? |

## Observer

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Question | Every display answers one question for one reader; build backward from it | A display of everything the data holds | Write the reader's question. Does the answer appear without searching? |
| Expertise | Match the reader's training: a specialist reads a log scale, a general reader needs a plain one with the unit spelled out | Jargon and unexplained encodings for a lay reader | Can a reader outside the field explain how to read it? |
| Decision | Show the quantity the decision turns on, with its threshold | Raw counts when the decision needs a rate or a change | What will the reader do with this? Is that quantity shown directly? |
| Distance and medium | Type, marks, and line weights are set for the real distance and device: a wall screen, a phone, a page, a slide across a room | Dense chart pasted into a slide; tiny tap targets on a dashboard | View at the real size on the real device |
| Attention | A dashboard is glanced at; a report is studied; build for the mode | Study-grade detail on a glance display | How many seconds does the reader have? Does the main answer fit in them? |
| Prior belief | Readers see what they expect; a surprising result needs more evidence on the page | A shocking claim with a bare line | What would a skeptic ask for? Is it on the display? |

## Composition

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Order | Sort by value unless the order has meaning (time, geography, a natural sequence) | Alphabetical bars with no reason | Is the order doing work? If it is alphabetical, why? |
| Grouping | Proximity, shared background, and alignment group items; related series sit together | Related items scattered; unrelated ones adjacent | Does distance match relationship? |
| Aligned scales | Compare across panels on the same axis, with the same range and baseline | Panels with different scales that look alike | Do comparable plots share axis ranges? |
| Small multiples | Repeat one design across categories so the reader learns it once and compares by position | Many series tangled in one plot | If lines cross past a handful, split into panels |
| Direct labels | Label marks and lines where they end; a legend forces the eye to travel and a memory to hold | Legend with many colors far from the data | Can the reader name each series without looking away? |
| Title | The title states the finding, in words; the subtitle states what is measured and where | A title naming the topic only | Read the title alone. Does it tell the finding? |
| Table design | Numbers align on the decimal point or right edge; units sit in the header; rows group with space, not lines; whole-row reading is supported | Centered numbers, mixed decimals, a grid on every cell | Do digits line up by place? Can you scan a column? |
| Ordering of detail | Overview first, then zoom, then detail on demand | Detail first, so the whole is never seen | Does the first view show the whole pattern? |

## Time

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Time axis | Time runs left to right at an even scale, with gaps shown as gaps | Uneven intervals plotted as even; missing periods bridged by a line | Are the time steps equal? Are gaps visible? |
| History and change | Show the change the reader cares about: level, rate, or comparison to a baseline, over a span long enough to show the pattern | A short window that hides the trend or the season | Does the window cover a full cycle? |
| Updates | Live displays say how often they refresh and when they last did | A frozen number that looks live | Is the refresh rate and last-updated time shown? |
| Staleness | Old data is marked old; a missing feed is shown as missing, not as zero | A stale value shown at the same weight as fresh ones | What happens on the display when data stops arriving? |
| Animation | Animate only when change over time is the message; otherwise show the states side by side | Motion for effect; transitions that hide values | If you replace the animation with a static before-and-after, is anything lost? |
| Versioned meaning | Definitions of a measure change; a series that crosses a change is marked | A series spliced across a redefinition with no mark | Did the definition, unit, or method change inside the span? |

## Truth

This branch exists because a display can be perfectly readable and false. The reader trusts the display, so the maker answers for it.

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Baseline | Length encodes value only from a true zero, so bars start at zero. Where a non-zero baseline is the point, use position encoding (dots or lines) and mark the axis break | A truncated bar axis that turns a 3 percent gap into a tall one | Do bars start at zero? If an axis is cut, is the cut marked? |
| Scale | A scale is chosen for the data's meaning: linear for differences, log for ratios, stated plainly | A log axis unmarked; a range stretched to dramatize a small change | Is the scale type labeled? Does the visual change match the real change in size? |
| Units | Every axis and number carries its unit, and its denominator for rates | Values with no unit; per-capita mixed with totals | Read each axis. Can you say what one unit is? |
| Uncertainty | Show the range: error bars, bands, intervals, sample size, and what they mean | A single line as if exact | Is spread or error shown? Could two values overlap within it? |
| Source and date | State where the data came from, who produced it, and when it was current | An unsourced figure | Can a reader trace the figure to its origin and date? |
| Precision | Show no more digits than the data supports | Four decimals on a survey of fifty | Does each digit survive the measurement error? |
| Selection | State what was left out and why: filtered rows, a chosen window, an excluded outlier | A start date chosen to produce a trend | Would a different window or filter change the story? |
| Cause | A pattern shown is a pattern, not a cause; imply no more than the data shows | A trend line captioned as a mechanism | Does the wording claim more than correlation, if only correlation was tested? |
| Map and territory | A display is a model with a projection, a boundary, and a grain; each can distort | Area on a map read as quantity; a map projection distorting size | What does the chosen map or diagram leave out, stretch, or merge? Is that stated? |

## Laws of the medium

- The reader's question comes first. Choose the encoding that answers it with the least effort.
- Position beats everything. When a comparison matters, put it on a common aligned scale.
- Emphasis is finite. One finding in color, the rest in gray.
- Remove ink until reading changes, then restore the last piece.
- Label directly and state the finding in the title. A reader should not decode a legend or guess a point.
- Truth outranks effect. A display that misleads has failed, however clear.
- Test with a stranger. Ask what they conclude, and compare it to what you meant.

## Defaults to replace

Pie charts with many slices, three-dimensional bars, rainbow color ramps, legends far from the data, alphabetical order, topic-only titles, a bar axis that starts above zero, dual axes, gridlines and borders at full weight, a frame chosen by the tool, unit-free axes, an unsourced number, a dashboard of every available metric, and an animation that adds nothing.
