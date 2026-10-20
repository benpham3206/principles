---
name: principles-language
description: Principles of anything written or spoken (prose, docs, naming, speech, dialogue, prompts for models, UI copy), organized on the six axes plus meaning. Use when writing, editing, naming, scripting, or critiquing words.
---

# Language

A **language** work is a sequence of symbols that rebuilds a meaning in a reader's head. The reader meets it one word at a time, in order, and cannot interrupt, so every choice is a choice about what they know after each word.

## Laws of the medium

- The reader has only the page. What is not written does not exist for them.
- Answer first. Position tells the reader what matters before the words can.
- One concept, one name. Variety in terms reads as variety in meaning.
- Concrete beats abstract. A reader can picture a thing and cannot picture a category.
- Cut until it breaks, then put back the last cut. The sentences that survive carry the load.
- Positive form wins. Say what to do. Name a forbidden thing only when no positive form exists.
- Read it aloud. The ear catches rhythm, length, and clutter that the eye skips.

## Defaults to replace

Stock openers ("In today's world", "It is important to note", "In this section we will", "Let's dive in"), stock closers ("In summary", "In conclusion", "I hope this helps"), hedges (might, perhaps, arguably, it seems, somewhat, a bit) used to avoid a claim, filler transitions (moreover, furthermore, additionally), intensifiers (very, really, extremely), the stock vocabulary (crucial, delve, robust, comprehensive, seamless, leverage as a verb, utilize, ensure, landscape, tapestry, pivotal), triplets by reflex, the rhetorical question that opens a paragraph, the "not X but Y" frame used by habit, and the title that says only the topic.

## Tree

```
LANGUAGE
├── Form          word, sentence length and shape, paragraph, the sentence as one idea
├── Material      diction, register, tone, figurative language
├── Energy        emphasis, verbs, voice, cadence
├── Observer      prior knowledge, the action wanted, attention budget, a model as reader
├── Composition   structure, order, headings, transitions, one idea per paragraph
├── Time          pacing, narrative order, setup and payoff, the reader's journey, aging
└── Meaning       map and territory, definitions, one term per concept, precision, checkable claims
```

## Form

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Word | The shortest word that is exact wins; a word is the smallest unit of choice | A long word where a short one means the same | Replace each long word with a short one. Did meaning change? |
| Sentence length | Length sets load; the reader holds one clause open while reading another | Sentences past about 25 words (a rule of thumb) that nest clauses | Count words. Can you say it in two sentences? |
| Sentence shape | Subject, verb, object in that order is the fastest shape to parse | The subject buried after a long lead-in | Find the verb. How many words come before its subject? |
| Variation | Short sentences land a point; longer ones carry a chain of reasoning; mix them on purpose | Every sentence the same length | Read the lengths down the page. Is there a beat? |
| Paragraph | A paragraph holds one idea and closes it | Two ideas in one block, or one idea split in three | State the paragraph in six words. Is it one idea? |
| One idea per sentence | A sentence that holds two claims hides the weaker one | Claims joined with "and" that need separate proof | Mark each claim. Is there more than one? |

## Material

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Diction | A concrete word shows a thing; an abstract word names a category. Prefer the thing | "Improve outcomes" where "cut load time by half" is meant | Can you picture or measure each noun? |
| Short roots | When two words are equal, the short Old English one (use, help, start) beats the Latin one (utilization, assistance, commencement) | Formal words chosen to sound serious | Swap in the short word. Does anything drop out? |
| Register | Register is the level of formality; it signals who the writer thinks the reader is | Legal tone in a note to a friend, slang in a contract | Read it aloud to the real reader. Does it sound like a person talking to them? |
| Tone | Tone is the attitude a reader infers; it comes from word choice and what is left unsaid | Tone that contradicts the content, such as cheer over bad news | Name the tone in one word. Does the situation call for it? |
| Figurative language | A metaphor moves a known structure onto an unknown one, so it must fit in the parts that matter | Mixed or dead metaphors; a figure where a plain fact serves | Spell out what maps to what. Does it hold at each point? |

## Energy

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Emphasis | The end of a sentence is the stress position; the start is second; the middle is weakest | The key fact placed mid-sentence, a weak phrase placed last | Read the last three words of each sentence. Are they the point? |
| Verbs | A strong verb carries the force; nouns made from verbs (make a decision, perform an analysis) drain it | The action hidden in a noun, with "make", "do", "is" as the verb | Circle the verbs. Do they name the action? |
| Voice | Active voice names the actor; passive fits when the actor is unknown or beside the point | Passive that hides who did what | Ask "who?" of each passive. Is the answer missing on purpose? |
| Cadence | Spoken and written text has a stress pattern the ear checks even in silence | Strings of equal stresses, or a trailing clause that deflates the end | Read it aloud. Where do you stumble? |
| Intensifiers | Force comes from the exact word, not from a modifier on a weak one | "Very important", "extremely significant", "really good" | Delete the intensifier. Pick a stronger word or accept the plain one |

## Observer

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Prior knowledge | Write at the edge of what the reader already knows; one step past it, with the step supplied | Jargon the reader lacks, or explanation of what they know | Name the reader. List the three terms they might not have |
| Action wanted | A reader should finish knowing what to do, decide, or believe | Text that informs and leaves the next step unnamed | Write "after reading, the reader will ___". Does the text say it? |
| Attention budget | Attention falls fast; spend it on what matters and cut the rest | Equal space for the key point and the footnote | Weigh words by importance. Does space follow weight? |
| Second person | Address the reader, who is the one acting; "you" beats "the user" | A thing written about the reader instead of to them | Who is the subject of most sentences? |
| A model as reader | A model reads literally and completely, and has only the page | Instructions that rely on unstated context | Hand the text to a fresh reader with no history. Can it act? |
| Positive form | Tell a model what to do; a forbidden thing named in the prompt still primes the thing | "Do not mention X" with no replacement action | Rewrite each prohibition as an instruction. Does one exist? |
| Examples are copied | A model reproduces the shape, length, and wording of an example | One example given, and every output matches it | Vary the examples, or state what may differ |
| Listener | Speech is heard once, in order, with no page to look back at | Written structure read aloud: long lists, nested clauses, references to "the above" | Say it to one person. Can they repeat the point? |

## Composition

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Structure | The shape of the text should match the shape of the content: steps in a list, comparisons in a table, an argument in paragraphs | Prose for a procedure, bullets for an argument | Name the content's shape. Does the form match? |
| Order | Answer first, then support; the reader who stops early still has the point | The conclusion saved for the end | Read only the first sentence of each section. Is the point there? |
| Headings | A heading is a label the reader scans; it should say what the section answers | Clever or vague headings that hide the content | Read the headings alone. Do they outline the argument? |
| Transitions | A transition states the logical link (because, so, but, then); without a link it is filler | "Moreover", "Additionally", "That said" with no logic behind them | Name the relation between the two sentences. Does the word say it? |
| One idea per paragraph | Each paragraph carries one idea and the next one builds on it | A paragraph that opens one idea and ends on another | Do the paragraph's first and last sentences agree? |
| Lists | A list is for items that are parallel and independent | A list of items that depend on each other, or that differ in kind | Can the items be reordered without loss? |
| Cut | Every sentence must change what the reader knows or does | Restating the heading or the sentence before | Delete each sentence in turn. Does anything break? |

## Time

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Pacing | Density sets speed; dense text slows the reader, light text speeds them | Dense and light at the wrong places | Mark the hardest passage. Does the text give it room? |
| Narrative order | Cause before effect, in the order events happened, unless a reason says otherwise | Events in the order the writer learned them | Lay out the events by time. Does the text follow it? |
| Setup and payoff | A reader who holds a question open expects an answer; plant what the end needs | A payoff with no setup, or a setup never paid | List each setup. Where does it close? |
| Reader's journey | The reader moves from not knowing to knowing; each step starts from what they now hold | A term used before it is defined | Read in order. At each sentence, what does the reader hold? |
| Dialogue | Speech in a script shows what a character wants and hides what they feel; people interrupt, dodge, and answer a different question | Characters who state their feelings in full sentences | Cover the names. Can you tell who speaks? |
| Aging | Text outlives its moment; "now", "recently", "the latest" lose their anchor | Relative time words and named versions with no date | Replace relative words with dates, or remove them |
| Revision | A first draft records the thinking; the second serves the reader | Shipping the draft that matches the writer's order of thought | Reorder for the reader. Does the structure change? |

## Meaning

This branch exists only in language. A word is not the thing it names; it is a lossy map of it. The reader builds the territory from the map, so a gap in the map is a gap in what they build.

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Map and territory | A word points at a thing and carries its own habits; the thing does not change when the word does | Treating a name or a label as proof the thing exists or works | Point to the thing outside the text. What is it? |
| Define before use | A term is defined where it first appears, in one line | A term used for pages and defined late, or never | Find each term's first use. Is the definition there? |
| One term per concept | Once a concept has a name, every use of it takes that name | Synonyms for variety, so the reader suspects a second concept | List the terms for each concept. Is there one? |
| Precision | A claim is as exact as the evidence allows: a number, a range, a condition | "Fast", "many", "often", "significant" with nothing under them | Replace each vague word with a number or a bound |
| Checkable claims | Each factual claim names how to test it: a source, a measurement, a date | Claims that cannot fail because they say nothing | Ask "what would show this wrong?" Is there an answer? |
| Ambiguity | A sentence that parses two ways will be read the wrong way by someone | Pronouns with two possible referents; modifiers in the wrong place | For each pronoun, name its noun. Is it one? |
| Names | A name is the shortest label that stays unambiguous in its context and lasts as long as the thing | A name that describes an implementation, so it breaks when that changes | Does the name still fit if the internals change? |
| Grounding | Language cannot verify itself; ground truth sits outside it | A confident description taken as evidence | Measure, run, or look at the thing. Does it match the text? |

Is language your reality? The answer in this skill is no. Language is a map. A fluent sentence can be false, and a true fact can be told badly. Write the map well, then check it against the territory.

Pairs with: before `principles-method`, `principles-qualities`, `principles-counsel`; after `principles-verify`.
