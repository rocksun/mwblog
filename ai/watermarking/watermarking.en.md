[← declaude](/)

# How AI text watermarking works.

A watermark in plain text sounds impossible. Text has no pixels to hide data in, and
no metadata survives copy-and-paste; every character is right there in front of you.
Where could a mark possibly go?

And yet the marks are real. Google has watermarked text from the Gemini app and
web experience since 2024 (its API is, at the time of writing, a
[documented
exception](https://discuss.ai.google.dev/t/does-gemini-api-text-output-carry-synthid-watermarking-gemini-2-5-flash-lite-gemini-3-1-flash-lite-eu-ai-act-art-50-2/177241)), and as of August 2026, new Claude models mark text at the model
level, with earlier models to follow. They're
invisible, they survive copying, and they
work because they don't live in the characters at all. They live in the
*choices between words*.

## 1. Writing is a series of small choices

The one idea in this step: a model writes by rolling weighted dice
between several words that would each be fine.

When a model is mid-sentence, it doesn't know "the next word." It has a shortlist,
like autocomplete, with preferences. Here's a real kind of moment, one word from the
end of a sentence:

the sentence being written

The results of the study were quite

🎲 roll the dice
🎲 roll ×20

Each roll sweeps the shortlist, lands on one word (odds matching the
bars) and drops it into the sentence above. The dots tally where the rolls land: try
×20 and watch the pile take the shape of the odds. Notice what *never* changes:
every landing makes a perfectly good sentence.

A page of text contains hundreds of these little forks, one per word, and at many of
them several options are equally fine. That slack is the raw material. Whoever gets to
lean on how the dice land can hide a pattern in the text without changing what it says.

## 2. A secret key leans on those choices

The one idea in this step: the key secretly colours the shortlist and
gives one colour a gentle nudge. The text still reads normally.

Here is the classic recipe (Kirchenbauer et al. 2023; Google's SynthID reaches the
same end by a subtler, tournament-style route). At each fork, secret-keyed maths splits
the candidate words into
**green** and
**red**, an arbitrary colouring only the
key-holder can reproduce. Then the dice get tilted a little toward green.

the sentence being written

The results of the study were quite

apply the secret key
🎲 roll the dice
🎲 roll ×20

No key applied: these are the model's own preferences.
Dashed outlines will show the old odds once the key is on.

Two things make this sneaky. The nudge is mild: a red word can still win — it's just
a little less likely. And the colouring is not a fixed property of the word: the key
computes it from a short run of the words just before, so the same candidate is green
after one prefix and red after another:

The same four candidate words, coloured by the key after six different
prefixes. The key sees the words just before it; the position in the wider text is invisible to it. Only the
*overall lean* toward green accumulates, and only the key-holder knows which
words were green where.

(Two siblings, same principle.
Google's SynthID — the one in production — replaces the nudge with a tiny secret
*tournament*: a few candidates are drawn from the model's own odds, the key scores them,
and the bracket is arranged so that, averaged over the key's draws, every word's odds
stay exactly what the model intended. Aaronson's scheme, built at OpenAI, skips
even that and derives the dice-rolls themselves from the key. Different maths, same
principle: the mark lives in the choices.)

## 3. Whoever holds the key can count

The one idea in this step: with the key, you can re-colour any text and
simply count. Marked text lands green too often to be luck.

Detection doesn't read the text or judge its style. The detector replays the
key-holder's colouring over the words and counts how many came up green. Without a mark
(or without the right key), green should win about half the time. A coin flip. Here's
an ordinary-looking paragraph; try both keys on it:

count with the right key
count with the wrong key
📖 keep reading: same mark, ×4 the text

greens: – of
55

coin flip

flag bar (this length)

Filled-and-underlined chips are green, dashed outlines are red. The
words read identically either way; the colouring exists only in the key-holder's
maths. With the wrong key the split is meaningless, and the count sits at chance.

(This demo's tilt is drawn strong so you can see it; a production mark leans far
more gently and needs correspondingly more text. In this demo's 50/50 model, a
1,500-word document would flag at only ~55% green: small leans become persuasive
only through length, which is why short texts are genuinely hard to call.)

## 4. What editing does to the mark

The one idea in this step: the mark lives in runs of untouched wording.
Editing erases it exactly where the runs break, and nowhere else.

Each word's colouring is derived from a short run of the words just before it (one
to a handful, depending on the scheme). So a position only counts as evidence if a short
window of the original wording (the word plus its neighbours) survives intact.

Here is the same paragraph from step 3, at five edit depths. **Drag the slider and
watch the highlighted runs shrink.** A highlight means that run of wording still
matches the original exactly, so the detector can count there. Everything faded is new
wording, where there is nothing but coin-flip noise left to count.

fix  
typos
light  
touch
tighten  
sentences
heavy  
edit
full  
rewrite

fix typos ·
surviving windows: –%

The verdict reads the surviving fraction measured *from the
highlights above*, projected to a 1,500-word document. Two things to notice:
how much a "heavy edit" leaves standing, and how far toward a full rewrite you
have to drag before the evidence actually dies.

On real implementations (MarkLLM's KGW and EXP schemes on an open model, washed by
declaude's full-rewrite route): about 0.5% of windows survive, and detector accuracy
falls from essentially certain to a coin flip. The published literature agrees on the
shape of this. Light or one-pass paraphrase *dilutes* the mark rather than
deleting it; in Kirchenbauer et al.'s experiments, the detector recovers given enough
text, with even human paraphrase becoming detectable again after roughly 800 tokens
(about 600 words). What removes
the mark is re-composition that shares no runs of wording with the original.

That is why a tool that rewrites from the meaning (like [declaude](/)'s
full-rewrite route) is what actually erases this family of marks, and why a light
pass that keeps most of the phrasing does not.

One boundary stated plainly: those numbers come from open implementations we can
measure. Anthropic's production scheme is undisclosed, so no one outside Anthropic
can yet run this test against Claude's own mark.

## 5. What this means in practice

The one idea in this step: detection is private, probabilistic, and
about *processing*, not authorship.

* **Only the key-holder can check.** Your teacher, editor, or favourite "AI
  detector" website cannot run this test; a genuine check needs the provider's
  secret key, or a checking service the provider runs. Google runs an early-access
  detector portal for SynthID; Anthropic says detection tooling is forthcoming.
* **A watermark check is not an "AI detector."** Tools like GPTZero guess from
  style and are famously unreliable. A watermark is the opposite: a deliberate,
  key-gated statistical test. Don't let the two blur.
* **A found mark means "processed by", not "written by".** Anthropic's own
  documentation notes that human text merely proofread or translated by Claude picks up
  the mark. And absence proves even less: old models or heavy editing
  yield clean results on genuine AI text.
* **Short and low-choice text carries little mark.** Evidence grows with length,
  and text with only one right continuation (code, quotations, lists of facts) offers
  the dice too little slack to hide anything in.
* **Certain marks outlive a rewrite.** Schemes keyed on the word itself
  rather than its neighbours hold up far better: a same-meaning rewrite keeps
  enough of the words that much of the mark survives.
  (Their weakness is different: a colouring reused everywhere can be reverse-engineered
  from enough output.) Others hide in the meaning, and a same-meaning rewrite partly
  preserves them; the only answer we know there is outline-level regeneration.

Written by [James Padolsey](https://j11y.io) at
[NOPE](https://nope.net) as an
accompaniment to [declaude](/). The interactive figures are a teaching model
with illustrative parameters, not any provider's actual scheme.

**Sources & further reading.**
Kirchenbauer et al., *A Watermark for Large Language Models* (ICML 2023) ·
Dathathri et al., *Scalable watermarking for identifying LLM outputs*
(SynthID-Text, Nature 2024) ·
Aaronson & Kirchner, *Watermarking GPT outputs* (2022) ·
Kirchenbauer et al., *On the Reliability of Watermarks for Large Language Models*
(ICLR 2024) ·
Sadasivan et al., *Can AI-Generated Text be Reliably Detected?* (2023) ·
Zhao et al., *The Mark Fades: Adaptive Evolutionary Paraphrase-based Attack*
(ACL Findings 2026) ·
Anthropic, [*How
Claude marks AI-generated content*](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) (Help Center, Aug 2026) ·
Our own known-key experiments: re-composition collapses KGW/EXP detection to chance
(AUC 0.99 → ≈0.5), context-free unigram marks survive (0.73–0.84); outline-level
regeneration is the only answer we know for meaning-space marks.

For the specialist: the residual-evidence model behind the step-4
verdict is z ≈ f·√N·z₁ (surviving fraction f, document length N, per-token strength
z₁). The figures count words; real detectors count tokens in the model's own
tokenizer. Same shape.