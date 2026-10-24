---
name: principles-language
description: Shape meaning and experience with words. Use when writing or editing prose, poetry, lyrics, dialogue, speeches, scripts, social posts, instructions, names, or UI copy.
---

# Language

**Language** shapes what an audience understands, feels, imagines, remembers, or does through words and other symbols.

## Laws of the medium

- Write for an audience and a purpose.
- Supply needed context and choose what to reveal when.
- Choose exact words and revealing details.
- Give the work a voice suited to its speaker and situation.
- Make rhythm, stress, and sound serve the meaning and form.
- Keep what earns its place through meaning, sound, character, atmosphere, or emphasis.
- Keep trust. Support factual claims; distinguish invention, uncertainty, and persuasion where mistaking them would matter.

### Write and revise

1. Name the audience and intended effect. Choose the form below; forms can mix.
2. Draft or read the whole piece. Fix the order, missing context, and passages that miss the purpose before polishing sentences.
3. Use the relevant checks in the reference tables. For a small edit, go straight to the affected part. Read a revision in context and preserve exact terms, necessary conditions, and chosen voice.
4. Remove a passage or try plainer wording. Keep the change only if no needed meaning or effect is lost. Use `principles-simplify` for a larger cut.
5. Check the result against the intent. Read it cold, perform spoken or sung work, and verify factual claims and instructions. Stop when the piece meets its purpose and quality bar.

Repetition, ambiguity, and a delayed reveal can serve the work. Judge them by their effect. Use the [quality checks](#judge-the-result) to set the bar.

| Form | Start with this check |
|---|---|
| Explanation, instructions, report | Can the reader find the point and follow it with the context supplied? For documentation, use [the four modes](#documentation) |
| Prose and essays | Does each passage develop the observation, argument, or experience? |
| Fiction and dialogue | Do events fit the world's rules? Do choices and distinct voices belong to the characters? |
| Poetry | What do images, line breaks, rhythm, and chosen ambiguity make possible? Read it aloud and on the page |
| Lyrics | Sing to the melody. Check stress, breath, vowels, rhyme, and repetition. Use `principles-sound` for musical choices |
| Scripts, speeches, and video | Perform at the intended pace. Can a listener follow on first hearing? Do words, performance, and any visuals work together? |
| Social posts and promotional copy | Does the piece fulfill its opening's promise? Check [requests](#requests) for an ask |
| Names, labels, and UI copy | Test the words among nearby choices. Can the intended person recognize, distinguish, and act? Use `principles-interaction` for the flow |

For usage claims, translations, or comparisons of word choices, use [meaning](#meaning) and [corpus evidence](#corpus-evidence-and-language-metrics).

## Defaults to replace

These are editing prompts. Change a pattern when it weakens this piece.

- Stock openings and endings: "In today's world", "It is important to note", "Let's dive in", "In conclusion", "I hope this helps". Give the passage a job or cut it.
- Hedges used to evade a claim, filler transitions, and intensifiers used instead of an exact word. Keep uncertainty the evidence requires.
- Formal or fashionable words chosen for status. Try "use", "help", or "start" and keep the wording that is equally exact and fits the voice.
- Habitual triplets, rhetorical questions, "not X but Y", stock imagery, forced rhyme, and unexplained changes of voice. Keep a device that creates a needed effect.

## Tree

```
LANGUAGE
├── Form          words, sentences, paragraphs, lines and stanzas
├── Material      diction, connotation, register, tone, imagery
├── Energy        emphasis, verbs, voice, cadence, modifiers
├── Observer      knowledge, attention, point of view, instructions
├── Composition   structure, headings, transitions, lists, links
├── Time          pacing, reveals, setup and payoff, aging
└── Meaning       linguistic structure, context, terms, claims
```

## Form

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Word | Prefer a shorter word when meaning, sound, and voice are equal | Extra weight with no added effect | Try the shorter word. What is lost? |
| Sentence length | Length affects load and pace. In explanatory prose, inspect sentences over about 25 words for nested clauses | The reader loses the thread | Try splitting it. Compare meaning, rhythm, and voice |
| Sentence shape | In plain English prose, subject, verb, object is a useful default | A buried subject delays understanding without purpose | Find the subject and verb. Does their order help? |
| Variation | Vary sentence lengths to shape pace and emphasis | Uniform lengths flatten the passage | Read aloud. Where does the pace need to change? |
| Focus | Develop one main idea per explanatory paragraph. Join clauses when their relation is clearer together | Unrelated claims compete, or a thought is split before it is clear | Name the focus. Does each sentence or clause contribute? |
| Line and stanza | Breaks shape breath, rhythm, emphasis, and expectation | Arbitrary breaks obscure a relation | Read across each break, then pause at it. What changes? |

## Material

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Diction | Use specific words. Keep an abstract or technical term when it is exact | "Improve outcomes" hides the intended change | Can the reader identify the thing or change? Add an example where needed |
| Connotation | Associations vary with community, history, and context | A near-synonym changes the attitude or social relation | Substitute it in the passage. What associations change for this audience? |
| Register | Situation shapes vocabulary, grammar, and directness. Formality is one part | A spoken script reads like a contract; friendliness erases precision | Compare examples for this purpose, participants, activity, and medium |
| Tone | Readers infer attitude from word choice and omission | Cheer contradicts bad news | Name the intended attitude. Does the wording convey it? |
| Figurative language | An image or metaphor earns its place by what it lets the audience perceive | Stock or mixed imagery distracts | What does the image make felt or understood? Does it hold where needed? |
| Dialogue | Give each speaker an intent and distinct voice. Fit evasion and interruption to the scene | Characters explain themselves only for the reader's benefit | Cover the names. Who speaks, and what do they want? |

## Energy

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Emphasis | In English explanatory prose, sentence openings and endings often draw attention | An empty ending displaces the important point | Read the opening and ending. Do they emphasize what matters here? |
| Verbs | In operational prose, name the action or property directly. Try an action verb, "is", or "has" | "Perform an analysis" or an inflated metaphor hides a simple action | Try "analyze" or the literal mechanism. Keep exact terms and purposeful images |
| Voice | Active voice names the actor; passive fits an unknown or unimportant actor | Passive hides responsibility | Ask who acted. Is the omission justified? |
| Cadence | Shape rhythm and sound for the intended reading or performance | Stress clashes with the intended emphasis | Read or perform it. Where do breath, stress, or sound work against the piece? |
| Modifiers | Keep modifiers that change meaning or create a needed effect | "Very important" props up a vague claim | Remove the modifier. Is anything lost? Try an exact word or supported measure |

## Observer

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Prior knowledge | Supply what this audience needs to follow the next idea | Unexplained jargon or needless explanation | Identify unfamiliar terms and missing context |
| Attention | Give the main point enough space and prominence for this audience | A footnote crowds out the finding | Can the reader locate what matters and give it the attention it needs? |
| Point of view | Address the reader in instructions and direct asks. Elsewhere, choose the actor or perspective the piece needs | "You" hides responsibility or breaks a story's perspective | Who acts, who is responsible, and whom does the text address? |
| Instructions | Give the reader or model explicit actions and essential context | Success depends on unstated knowledge | Can a fresh reader act? Pair a necessary prohibition with a usable alternative where one exists |
| Examples | Distinguish required features from incidental wording or format | A model or learner copies details as requirements | Vary examples or state what can differ |
| Listener | Make spoken meaning followable on first hearing | Nested clauses, long lists, or "see above" require rereading | Perform at the intended pace. Can a listener follow the important turns? |

## Composition

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Structure | Match form to content: steps in a list, comparisons in a table, an argument in paragraphs | Layout hides the relation among ideas | Can the reader see how the parts relate? |
| Order | Lead answers and reports with the finding. Put prerequisites before procedural steps | The answer is buried or needed context arrives late | Read in order. Can the reader understand and act at each point? |
| Headings and titles | Headings guide navigation; levels show hierarchy. Titles can identify or evoke | A heading hides content, or a title promises the wrong experience | Read headings alone. Do they give a usable outline and the right expectation? |
| Connections | Show how sentences and paragraphs build on each other | A jump requires hidden context; "moreover" supplies no relation | Name the relation. Use a transition that expresses it, or remove the filler |
| Lists | Number sequences and use bullets for comparable items. Keep items parallel | The reader cannot tell whether order matters | Does numbering express an order, and does each item share a role? |
| Links and literals | Give links descriptive text and context. Reproduce commands and interface labels exactly | "Click here" hides the destination; a label cannot be found | Predict each destination and match each literal name to the thing it names |
| Formatting | Make punctuation and emphasis carry structure, voice, or a needed effect | Repeated dashes, colons, or bold labels add empty emphasis | Check each pause and highlighted span. What does it do? |

## Time

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Pacing | Give difficult ideas room and vary density for the intended pace | The work rushes a hard passage or stalls a simple one | Read at the intended pace. Where must the audience pause? |
| Narrative order | Choose chronology or a reveal for its effect | The audience must reconstruct a sequence unintentionally | Can they place events when needed? What does withholding or revealing change? |
| Setup and payoff | Prepare what a later turn needs. Resolve expectations the work promises to resolve | An unsupported payoff or a forgotten setup | Trace each setup. Is its resolution or deliberate openness earned? |
| Reader's journey | Track what the audience knows, expects, and feels at each turn | A reveal needs missing context | Read in sequence. What is held, questioned, or newly understood? |
| Aging | Date or version claims that a later reader must place in time | "Recently" or "the latest" loses its reference | Can a later reader tell when the claim applies? |

## Meaning

Linguistics describes patterns; writing choices also need a purpose. Check patterns in the relevant language and community. Read an image in context before treating it as a literal claim.

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Sound and word formation | Sounds and meaningful word parts shape recognition, rhythm, and possible readings | Coinage or translation loses a distinction or adds an unwanted echo | Speak it in context and check with users of the language or variety |
| Syntax | Grammar expresses relations. Languages differ in how word order carries them | Compression obscures actors, modifiers, or negation | Restore needed articles and verbs; expand noun strings. Paraphrase plausible readings |
| Context and inference | Semantics concerns linguistic meaning; pragmatics concerns use and inference in context | Literal truth misleads, or an implied request lacks needed context | What must the audience assume, identify, or infer? Test with the context they will have |
| Collocation | Words favor particular neighbors and constructions | A near-synonym sounds misplaced or changes associations | Read matching uses in the relevant register |
| Terms and names | Explain needed terms before use. Keep labels stable where they distinguish concepts; choose titles for their role | A definition drops a condition, a synonym implies a new concept, or a name ages with implementation | Can the reader follow each use? Check pronoun references and whether the name still fits |
| Precision | Match exactness to evidence. A factual range needs a meaningful relation between its endpoints | False precision or an unsupported claim of coverage | Check numbers, conditions, and endpoints. Use a list if a span misleads; preserve purposeful breadth or contrast |
| Evidence | Support factual claims with a source, test, measurement, or observation. A description is not proof | "Experts say" hides a source; "highlighting its value" adds unsupported praise | Name the support and what it establishes. What would show the claim wrong? Use `principles-ground` |
| Ambiguity | Remove unintended readings that change understanding or action. Keep multiple meanings that enrich the work | A modifier changes an instruction, or an edit erases a poem's double meaning | Place "only" and "not" by what they modify. Make grouping and the meaning of "and", "or", or slashes explicit where action depends on it |

## Documentation

Choose the reader's main need for each page or section. Split and link material when a change of purpose interrupts the task. A README can offer several clear routes.

| Mode | Principle | Failure | Check |
|---|---|---|---|
| Tutorial | Teach through something the learner makes, with early results and visible checkpoints | The learner cannot recognize success | Can a newcomer reach and recognize the result from the stated prerequisites? |
| How-to | Solve a named task with direct commands. Put conditions and warnings before actions; give the common path first | Background hides a step, or a warning arrives late | Walk every branch. Does the reader know when and how to take it? |
| Reference | Organize lookup facts around the thing described. Declare scope, options, defaults, limits, and errors | Readers hunt through a lesson or rely on stale facts | Can they find the fact where expected, and does it match the actual version? |
| Explanation | Answer a bounded why question through mechanisms, context, alternatives, and trade-offs | Facts leave the reason unexplained | Can the reader explain the choice and when another would fit? |

For procedures:

1. Give each instruction one action. Inspect instructions over about 20 words; keep necessary conditions.
2. Use exact command, symbol, file, flag, and interface-label names.
3. Run examples from the stated starting conditions and show expected results. Treat unchecked commands and counts as provisional.
4. Generate changing facts from their source where practical; otherwise check against it.

For PR descriptions and commit messages, lead with the problem and resulting behavior, name the evidence, and link long logs. Choose the structure for a brief account of the change.

## Requests

A **call to action** lets the reader make an informed choice. Use `principles-counsel` and `principles-interaction` for decision ownership and consent.

Do authorized work yourself; ask for what needs this reader's authority, knowledge, or judgment. Prioritize multiple asks by what they unblock and the consequences.

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Action and means | Name one concrete action per ask and supply the link, command, or choice | The reader must decode a task or search for how to start | Can they act from the ask alone? |
| Reason | Explain what the action gains, prevents, or unblocks for the reader | The ask serves only the asker's process | Is the reason relevant and supported? |
| Cost and timing | State effort, irreversible effects, consequences of waiting, and real deadlines | A small-sounding ask hides cost or invents urgency | Can the reader judge the cost of acting or waiting? |
| Choice | Make declining as easy as accepting, with real consequences stated plainly | Guilt, hidden defaults, or an obstructed refusal | Can the reader freely say no? |

## Corpus evidence and language metrics

A **corpus** is a selected collection of language used as evidence. Use it to test a usage claim or compare choices. Record population, period, medium, genre, and selection method; size alone does not establish representativeness. Use `principles-measure` for the measurement procedure.

| Measure or method | Principle | Failure | Check |
|---|---|---|---|
| Frequency | Count a defined unit, normalize by relevant opportunities, and keep raw counts and denominators | More text alone produces a higher count | Compare tokenization, case, word forms, denominators, and contributing documents or speakers |
| Dispersion and burstiness | Dispersion describes spread; burstiness describes clustering relative to a stated baseline | A total hides one speaker or topic; sentence-length variation is called burstiness | State the unit, window, and baseline. Inspect positions and contributing texts |
| Collocation analysis | Compare co-occurrence with a baseline accounting for word frequencies. Define span or grammatical relation | Common words dominate counts, or rare pairs dominate a score | Inspect counts, association measures, and passages. Does the pattern persist in relevant texts? |
| Connotation in use | Recurring contexts can support an association, sometimes called semantic prosody | One corpus's association is imposed on every speaker or passage | Read positive, negative, and exceptional contexts in the intended situation |
| Perplexity | Exponential of a language model's mean negative log probability per token, using natural logs; measures prediction on the evaluated text | Incompatible scores are compared, or taken as proof of quality or authorship | Record model, tokenization, context, and text. Compare models on the same held-out data and protocol, or texts under the same fixed model and protocol |

Metrics answer the stated question. Commonness and predictability do not determine which words best serve a poem, character, instruction, or song. Judge the writing's effect separately.

## Judge the result

Use `principles-craft` to choose the bar and `principles-verify` to check the work.

| Level | Check |
|---|---|
| Good | Does the piece deliver its intended meaning, experience, or action for this audience and setting? |
| Great | What would a competent generic version lose? Compare insight, voice, detail, and form with excellent work serving a similar purpose |
| Timeless | Has its force, pleasure, clarity, or usefulness survived a loss of original context? Time supplies that evidence; until then, timelessness is an aim |

A timely notice can succeed through accuracy and usefulness during its brief life.

Pairs with: before `principles-method`, `principles-qualities`, `principles-counsel`; after `principles-verify`, `principles-simplify`.
