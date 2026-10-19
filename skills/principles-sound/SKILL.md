---
name: principles-sound
description: Principles of anything heard (music, production, mixing, voice, sound design, alerts and UI sounds, room acoustics), organized on the six axes. Use when composing, mixing, recording, designing, or critiquing how something sounds.
---

# Sound

A **sound** work is pressure variation in air arranged to reach an ear. The listener hears level and onset first, pitch and rhythm second, and timbre and space last, so every choice is a choice about what they hear in what order, in a room and on a speaker you do not control.

## Tree

```
SOUND
├── Form          pitch, interval, contour, envelope, duration
├── Material      timbre, harmonics, resonance, grain and noise, source
├── Energy        dynamics, loudness, attack and transients, headroom
├── Observer      position, room, playback system, hearing range, masking, attention
├── Composition   arrangement, frequency space, stereo field, voicing, contrast, mix
├── Time          rhythm, tempo, groove, phrase and form, decay, silence
└── Signal        gain staging, noise floor, capture limits
```

## Form

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Pitch | Pitch is perceived as the log of frequency, so equal ratios sound like equal steps | Spacing notes or filters by equal hertz instead of equal ratio | Is every interval, sweep, and tuning step set as a ratio? |
| Interval | An octave is a 2:1 frequency ratio; simple ratios (3:2, 4:3) sound stable and complex ones sound tense | Dissonance or consonance chosen by accident | Name each interval and its tension. Is it the tension you intend? |
| Contour | The rise and fall of a line is remembered before its exact notes | Lines that wander with no shape | Hum the contour with no pitch. Is the shape clear? |
| Envelope | Attack, decay, sustain, and release (ADSR) give a sound its identity as an event | One envelope shape on every sound | Plot the amplitude over time. Does each sound have its own shape? |
| Duration | A note lasts as long as its job; length sets weight and tempo feel | Notes that run past their reason or cut before they land | Does each sound end when its job ends? |

## Material

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Timbre | Timbre is the mix of harmonic levels over time; it separates two sources at the same pitch and level | Two parts with the same timbre fusing into one | Play both at the same note. Can you tell them apart? |
| Harmonics | Overtones sit at whole multiples of the fundamental in most struck and bowed sources; bright sounds hold strong high ones | Brightness added by boosting highs the source never made | Look at the spectrum. Is the energy where the source puts it? |
| Resonance | A body or room amplifies the frequencies it naturally rings at | A single ringing frequency that stands out on some notes | Sweep a tone. Which frequencies jump out? |
| Grain and noise | Noise is energy with no pitch; it gives breath, friction, and air | Clean synthetic tone with no noise, or noise with no purpose | What noise is present, and does it belong? |
| Source | Acoustic, voice, and synthetic sources differ in how they vary from note to note | A synthetic source with identical repeats that reads as mechanical | Play the same note twice. Does it vary the way the source would? |

Honest sources: a sound should behave as the object it implies. A big object rings low and slow; a small one rings high and fast.

## Energy

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Dynamics | Difference in level carries emphasis, as contrast does in every medium | A constant level, so nothing leads | Plot level over time. Where are the peaks and the quiet? |
| Loudness | Sound pressure level in dB is logarithmic: 20 times the log of the pressure ratio to a reference. Perceived loudness depends on frequency and level (equal-loudness contours), and the ear is least sensitive to low frequencies at low levels | Judging a mix at one volume only, or matching level by meter when ears disagree | Compare at low and high volume. Does the balance hold? |
| Attack | The first few milliseconds carry identity and position; a sharp onset reads as near and hard | Onsets blunted by too much compression or too slow an envelope | Solo the first 20 ms. Is the onset still clear? |
| Headroom | Headroom is the space between the loudest peak and the clip point; a peak past it is distorted | Peaks at the limit with no margin, then clipped downstream | How far is the loudest peak below clipping? |
| Compression | A compressor reduces the gap between loud and quiet; it raises sustain and lowers contrast | Compression on everything, flattening the work | Bypass it. What did it add that you want? |

## Observer

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Position | Level from a point source in free field falls 6 dB per doubling of distance (inverse square); nearer sounds are louder, drier, and brighter | Distance implied by level alone with no change in reverb or tone | Does a far sound lose level, highs, and dry-to-reverb ratio together? |
| Room | Walls return energy as reflections; reverberation time (RT60) is the time for the level to fall 60 dB | One reverb on everything, or a room with no tail | Does every source sit in one room, or in rooms chosen to differ? |
| Playback system | Small speakers cannot move enough air for low frequencies; headphones place sound inside the head | Mix judged on one system only | Play it on the smallest and the largest system the work will meet |
| Hearing range | The young human ear spans about 20 Hz to 20 kHz; sensitivity peaks near 2 to 4 kHz; the top falls with age and exposure | Detail placed where few listeners hear it, or energy past the speaker's range | Is the key content inside the band the listener hears? |
| Masking | A loud sound hides quieter sounds at nearby frequencies and just after it | Two parts competing in the same band, so one disappears | Mute one part. Does the other appear? |
| Attention | The ear locks onto speech, change, and the unexpected; a steady sound fades from notice | Alerts that fade into the background, or a constant tone that tires | Does the listener notice the sound the first time, and not tire of it? |

## Composition

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Arrangement | Each part has a role: lead, support, rhythm, or space | Every part playing all the time | Name the role of each part. Is there overlap? |
| Frequency space | Parts that share a band mask each other; give each its own region | Many parts packed into the low mids | Split the spectrum into bands. Which parts own each band? |
| Stereo field | Level and time differences between the ears place a source left to right; a centered source sits in front | Everything panned center or everything wide | Check in mono. Does anything vanish? |
| Depth | Distance is built from level, brightness, and dry-to-reverb ratio together | Depth from reverb alone | How many depth cues agree for each source? |
| Voicing | Notes in a chord spaced wide at the bottom and close at the top are clear; close low notes blur | Thirds and seconds stacked in the low octaves | Play the chord low. Do the notes stay distinct? |
| Contrast | Sections differ in density, register, and level so each change is heard | Sections that differ only in label | Compare two sections. What changed? |
| Mix | The mix sets one thing first, then a clear second and third | Several elements competing for first | At low volume, what do you hear first, second, third? |

## Time

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Rhythm | A pattern of accents against a steady pulse gives the ear something to predict | A grid with no accent, or accents with no pulse | Tap the pulse. Do the accents fall where you meant? |
| Tempo | Tempo sets energy and room: a faster pulse needs shorter decays | A tempo left at the default | Why this tempo? What does the decay do at this speed? |
| Groove | Small shifts from the grid, often a few to tens of milliseconds, give feel; a part ahead of the beat pushes, behind it relaxes | Every note on the exact grid, or random offsets with no pattern | Shift one part earlier and later. Which feel serves the work? |
| Phrase and form | Phrases breathe in lengths the ear can hold, and repeat so the form can be learned | Phrases that never resolve, or repeat with no change | Mark the phrase ends. Does each have a landing? |
| Decay | The tail of a note or room tells the listener the size of the space and how soft the source is | Tails that run into the next note and blur it | Do tails clear before the next onset that matters? |
| Silence | Silence is contrast; a gap makes the next sound louder | Sound filling every moment | Where is the longest gap? Is it placed on purpose? |

## Signal

| Leaf | Principle | Failure | Check |
|---|---|---|---|
| Gain staging | Each stage in a chain has a noise floor and a clip point; set level so the signal sits well above one and below the other | Low level early, then noise lifted late; or clipping early | At each stage, how far is the signal from noise and from clip? |
| Noise floor | Every capture holds noise; dynamic range is the gap from the floor to the clip point, and each added bit of a digital word adds about 6 dB | Recording quiet sources so close to the floor that fixing them lifts the noise | What is the signal-to-noise ratio at the quietest part? |
| Capture limit | A sampled signal holds only frequencies below half the sample rate (Nyquist); anything above folds back as a false lower tone | Content above the limit entering the capture | Is the highest frequency present below half the sample rate? |

## Laws of the medium

- Level is a log scale. Sound pressure level in dB is 20 log10 of the pressure ratio to a reference, so +6 dB doubles pressure and +10 dB is heard as roughly twice as loud (a rule of thumb that varies with frequency and level). Think in ratios.
- Two equal, uncorrelated sources add 3 dB, not 6. Two identical in-phase signals add 6 dB; opposite phase cancels.
- Each part owns a band, a position, and a moment. When two share all three, one is lost.
- The first milliseconds, the loudest part, and the lowest frequency tell the listener most. Set them first.
- The room and the speaker are part of the work. A wavelength is the speed of sound (about 343 m/s in air at 20 degrees Celsius) divided by frequency, so low notes are meters long and meet the room as modes, not rays.
- Judge at the three distances: low volume, a cheap speaker, the next room.
- Silence and quiet are material. Contrast needs both.

## Defaults to replace

A single reverb on the whole mix, a tempo of 120 beats per minute, every note on the grid, everything centered, every part in the same octave, a compressor on every channel, the loudest level for every section, a stock envelope, a sound that starts on beat one of every bar, and an alert tone at one pitch and one volume everywhere.
