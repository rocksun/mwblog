[OpenAI](https://openai.com/) on Thursday [launched GPT-5.4](https://openai.com/index/introducing-gpt-5-4/), the next version of its frontier model. The company calls it its “most capable and efficient frontier model for professional work” and notes that it combines the coding capabilities of its recently launched [GPT-5.3-Codex](https://thenewstack.io/openais-gpt-5-3-codex-helped-build-itself/) model with improved support for spreadsheets, documents, and presentations.

The company argues that the new model is better at searching the web and maintaining context for queries that need longer thinking times. In addition, OpenAI improved the model’s computer-use capabilities and now allows it to more efficiently pick the right tools when it operates in an ecosystem with quite a few available.

It’s also the company’s most factual model yet, OpenAI claims, “with responses 18% less likely to contain errors, and individual claims 33% less likely to be false compared to GPT-5.2.”

With GPT-5.4, the company is removing the beta label from its one-million-token window for API users as well. Codex will now also support this extended token window, but requests for more than 272,000 tokens will count against the usage limits at a 2x rate.

One new feature that is especially interesting is that GPT-5.4 Thinking can now show an upfront plan of its thinking, allowing users to steer the model mid-response while it’s working, ensuring it doesn’t take any wrong turns without burning through thousands of tokens in between turns.

You may wonder: didn’t OpenAI only launch [GPT-5.3-Instant](https://thenewstack.io/openai-gpt-5-1-instant/) earlier this week? Yes. OpenAI’s versioning has always been a bit weird, but it looks like for the mainstream model, we’re skipping a number here again. 5.3-Instant will remain the workhorse model in ChatGPT.

![OpenAI GPT-5.4 benchmarks.](https://cdn.thenewstack.io/media/2026/03/a714095d-screenshot-2026-03-05-at-9.07.12-am.png)

OpenAI GPT-5.4 benchmarks (credit: OpenAI).

## More expensive models, but less token usage

The new model will come in Thinking and Pro versions. GPT-5.4 Thinking will be available in ChatGPT, the API, and the Codex agentic coding app.

The significantly more expensive GPT-5.4 Pro will only be available in ChatGPT and the API, but not in Codex. That may be for the better. At $30/$180 per million input/output tokens (GPT-5.2 Pro was priced at $21/$168), 5.4 Pro is OpenAI’s most expensive model yet, and you don’t want to be surprised by those bills.

The same price increase applies to the standard Thinking mode, which will cost $2.50/$15 per million input/output tokens, up from $1.75/$14.

![](https://cdn.thenewstack.io/media/2026/03/54ffb405-screenshot-2026-03-05-at-9.35.28-am.png)

OpenAI GPT-5.4 pricing (credit: OpenAI).

OpenAI, however, argues that the updated models are far more efficient with their token usage. “GPT-5.4 is our most token-efficient reasoning model yet, using significantly fewer tokens to solve problems when compared to GPT-5.2—translating to reduced token usage and faster speeds,” OpenAI notes in its announcement.

“In the API, GPT-5.4 is priced higher per token than GPT-5.2 to reflect its improved capabilities, while its greater token efficiency helps reduce the total number of tokens required for many tasks,” OpenAI writes. “Batch and Flex pricing are available at half the standard API rate, while Priority processing is available at twice the standard API rate.”

## Benchmarks

On the standard benchmarks, the new model unsurprisingly surpasses its predecessors by a healthy margin. That’s true even across coding tasks, where the new model even beats OpenAI’s own recent Codex release (and Google’s [Gemini 3.1 Pro](https://thenewstack.io/googles-gemini-3-1-pro-is-mostly-great/)) on the SWE-Bench Pro benchmark.

When it comes to agentic use cases and computer use, GPT-5.4 Thinking is also doing quite well, mostly scoring ahead of Anthropic’s Opus 4.6 and Google’s Gemini 3.1 Pro.

For most of these tasks, OpenAI stresses that the new model can achieve these results while still using fewer tokens than its predecessor.

## Better at knowledge work

GPT 5.4 Pro, given its high price, doesn’t always rank significantly better than the Thinking version on the benchmarks OpenAI provided. It does better on the BrowseComp agentic browsing test, but few users would use Pro for that. It does, however, excel at solving advanced math problems, scoring 38% on solving the most advanced problems in the FrontierMath benchmark compared to 27.1% for the Thinking version.

The one area, and maybe the one that most knowledge workers should look at, is its score on the GDPval benchmark, which tests the models’ ability to handle real-world tasks across 44 occupations. There, the new model scores 83%, meaning it matched or exceeded industry professionals in 83% of comparisons. Anthropic’s Opus 4.6 scores 79.5% there.

OpenAI also ran some internal benchmarks. “On a set of presentation evaluation prompts, human raters preferred presentations from GPT-5.4 68.0% of the time over those from GPT-5.2 due to stronger aesthetics, greater visual variety, and more effective use of image generation,” OpenAI writes.

On another internal benchmark, the model also scored 87.5% on a spreadsheet task modeled on what a junior investment banker would do.

Box saw similar improvements in its early testing. “In Box’s evaluations comparing GPT-5.2 and GPT-5.4, we saw an overall performance improvement across our complex extraction tasks dataset from 72% to 78%. These gains demonstrate an increased ability to extract multiple pieces of information from a document in a single pass, including tasks requiring multi-step reasoning — a critical capability to drive and inform enterprise workflows,” said Yashodha Bhavnani, Head of AI at Box, in a statement.

## Availability

The new models are now rolling out across ChatGPT and Codex.  The Thinking version will be available to Plus, Team, and Pro users (Enterprise and Edu users will need their admin to enable it), while the Pro model is only available to users on the Pro and Enterprise plans.

The new models will be available in the API as *gpt-5.4* and *gpt-5.3-pro.*

![](https://cdn.thenewstack.io/media/2026/03/8d829e62-gpt-5.4-in-chatgpt-scaled.png)

Credit: OpenAI.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)