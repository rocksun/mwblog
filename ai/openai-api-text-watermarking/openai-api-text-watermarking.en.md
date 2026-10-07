OpenAI has announced that developers can now opt in to watermarking text generated through its API, as the company extends its existing content provenance efforts to one of the more difficult forms of AI output to reliably identify.

In a [blog post published on Monday](https://openai.com/index/eu-text-provenance/), the company details a new system dubbed textGrain, which embeds a “statistical signal” into generated text by subtly influencing the words a model chooses — for example, favoring one suitable word over another when either would make sense in a sentence. Over a long enough passage, those choices form a pattern that OpenAI’s detector can identify.

API customers worldwide can enable watermarking on supported models from today, and in the coming weeks, OpenAI says it will begin automatically watermarking eligible text produced by ChatGPT and Codex in the European Union (EU). This is in response to new transparency requirements under the [EU AI Act](https://artificialintelligenceact.eu/article/50/).

“Starting today, API customers globally will be able to opt in to text watermarking for select models. Text watermarking will remain off by default in the API,” the company writes. “This lets customers decide how watermarking fits their transparency obligations and the experiences they provide to users.”

> “Text watermarking will remain off by default in the API. This lets customers decide how watermarking fits their transparency obligations and the experiences they provide to users.”

## Differing approaches from OpenAI and Anthropic

It’s worth noting that OpenAI’s approach differs from that Anthropic outlined when it [announced text watermarking for Claude in August](https://thenewstack.io/anthropic-claude-text-watermark/). Anthropic said it would apply watermarking globally to supported Claude models, explaining that it didn’t yet have a reliable way to limit the technology by region. That watermark also extends to developers using Claude through its API, as well as other products such as Claude and Claude Code.

Anthropic doesn’t describe an equivalent opt-out for API developers, giving developers less control over whether their model output carries the watermark.

“Watermarking will be applied at the model level, which means it will be present no matter which Claude product or surface the text comes from,” the company [confirms in its documentation](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content).

For OpenAI API customers that *do* want watermarking, it can be activated at either the project or organization level, with customers able to choose which supported models should use it. The company says no changes to individual API requests are required once it’s enabled.

## OpenAI’s provenance track record

OpenAI already uses several provenance technologies for other types of generated content. Back in 2024, it [began adding](https://openai.com/index/understanding-the-source-of-what-we-see-and-hear-online/) Content Credentials to generated images, using an open standard developed by the Coalition for Content Provenance and Authenticity (C2PA) to record information about a file’s origin and history.

It [later added](https://openai.com/index/advancing-content-provenance/) Google’s SynthID watermarks to supported images in May 2026 and audio in July, and now offers a [Content Provenance API](https://developers.openai.com/api/docs/guides/content-provenance) for checking supported images and audio for those signals.

OpenAI could feasibly have used an existing text watermarking technology such as SynthID, while Meta has developed its own [TextSeal](https://github.com/facebookresearch/textseal) method too. On its [FAQ](https://help.openai.com/en/articles/8912793-provenance-signals-in-openai-generated-content) page, OpenAI says it developed textGrain to give it “more control….over the balance between watermark detectability and the variety of responses generated from the same prompt.” Indeed, it says textGrain matched or exceeded SynthID’s detection performance in its testing, and plans to open-source the technology so “others can build on it and help improve text watermarking.”

## “Code is also harder to watermark”: Where the signal fades

The technique comes with some limitations, however. Because textGrain creates its signal through the choices a model makes between suitable words, detection becomes more difficult when there are fewer choices available.

OpenAI says its detector catches around 80% of watermarked 200-token passages, and 95% of 400-token passages in domains such as psychology, at a target false-positive rate of 1%. And detection is lower for more constrained material such as mathematics.

![Impact of text length and type on detection rate](https://cdn.thenewstack.io/media/2026/10/d4ff8c2c-screenshot-2026-10-05-at-19-06-20-our-approach-to-eu-text-provenance-rules-openai.png)

*Impact of text length and type on detection rate (credit: OpenAI)*

Editing the output can also substantially weaken the signal. In OpenAI’s tests, replacing 10% of the words in a 400-token passage with synonyms reduced its detection rate from around 92% to 66%. Replacing 25% brought it down to just 17%.

![Impact of edits on detection rate](https://cdn.thenewstack.io/media/2026/10/a8071bd2-screenshot-2026-10-05-at-18-56-34-our-approach-to-eu-text-provenance-rules-openai.png)

*Impact of edits on detection rate (credit: OpenAI)*

Notably, OpenAI cautions that shorter passages may simply contain too little material for its detector to reliably identify a watermark.

“Code is also harder to watermark because there are fewer plausible choices for what comes next than in ordinary prose,” the company adds.

> “Code is also harder to watermark because there are fewer plausible choices for what comes next than in ordinary prose.”

This makes the forthcoming Codex rollout worth watching. OpenAI plans to automatically watermark eligible Codex text output in the EU, while acknowledging that source code itself is particularly difficult to watermark. The company hasn’t yet explained exactly what it means by “eligible” Codex output, or whether the watermark will apply to generated code itself.

As *The New Stack* has [previously reported](https://thenewstack.io/fable-5-1-watermark/), Anthropic has encountered similar limitations with Claude. Code gives its watermarking system fewer opportunities to embed a signal without potentially altering how the program behaves, although natural-language text within code, such as comments, is easier to watermark.

And then there’s also the question of whether introducing those token preferences affects the quality of generated code. OpenAI tested its Astra model with and without watermarking against several coding and agent benchmarks, including DeepSWE, AutomationBench and Terminal-Bench, and says it found no meaningful difference in performance. That suggests textGrain can be enabled without significantly hurting coding ability, although it doesn’t tell us how reliably the resulting code can subsequently be identified as watermarked.

Access to the detector is a separate matter altogether. API customers that opt into textGrain don’t automatically gain the ability to detect its watermark, with OpenAI saying that it’s initially limiting detector access to approved research and academic organizations studying areas including text provenance and detection reliability. Such access could, for example, allow researchers to examine how reliably the watermark survives editing and other transformations, or investigate the circumstances in which the detector produces false positives or misses watermarked text.

*The New Stack* asked OpenAI for more detail on what constitutes eligible Codex output and whether it has code-specific detection rates. We will update here if, or when, we hear back.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)