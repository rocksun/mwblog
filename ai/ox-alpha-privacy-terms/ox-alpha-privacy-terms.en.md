**Everybody wants to know who built Ox Alpha**. But developers using the anonymous coding model with their own private code will have a more pressing question: *What happens to that code after they hit send?*

Let’s start with the model’s unusual arrival. An anonymous provider listed Ox Alpha on OpenRouter on August 20, and no company has claimed it yet. [OpenCode](https://opencode.ai/), the open-source terminal agent, debuted it the same day and [announced](https://x.com/opencode/status/2090544355824038300) a capacity of 100 trillion tokens a day.

OpenRouter describes a reasoning model built for long-horizon software engineering. The listing sets the context window to 1,048,576 tokens and prices both input and output at 0 for the preview.

> Which checkpoint is behind the endpoint matters least for this launch. Which legal entity receives the request, and under which route’s terms, has drawn almost no scrutiny at all.

The reaction has been a detective story of tokenizer probes, benchmark screenshots, and a rotating shortlist of suspects.

Which checkpoint is behind the endpoint matters least for this launch. Which legal entity receives the request, and under which route’s terms, has drawn almost no scrutiny at all.

## The identity hunt has been more rigorous than the benchmarking

A developer known as unclecode, who wrote the Crawl4AI crawler, built [modelprint](https://github.com/unclecode/modelprint) to fingerprint anonymous API endpoints. The launch version sent nine infrastructure probes and matched the responses against known models. Ox Alpha lined up with GLM-5.3 on six of the nine.

He is careful about what that proves. Matching fingerprints establish shared infrastructure rather than model identity, he wrote in the project documentation. One lab can serve two different checkpoints from the same stack.

The circumstantial case around Z.ai is strong. The company reportedly previewed GLM-5 on OpenRouter as [Pony Alpha](https://x.com/OpenRouterAI/status/2021639702789730631), and it announced GLM-5.3 six days before Ox Alpha turned up. Xiaomi’s [MiMo](https://x.com/haider1/status/2090725700739477692) team keeps coming up as an alternative, and one reading of the tokenizer behavior points instead at [cl100k\_base](https://wccftech.com/a-mysterious-ai-lab-is-offering-100-trillion-free-tokens-day-for-its-ox-alpha-model-as-evidence-points-to-zhipus-unreleased-glm/), an OpenAI encoding that sits oddly on a Chinese model.

The benchmark story has held up worse. [Ben Davis](https://x.com/davis7/status/2090655207831298095) on X reported a score of 80% across 10 DeepSWE tasks, and he himself flagged the small sample size. A later [113-task run](https://github.com/MatchaOnMuffins/oxalpha) published on GitHub resolved 66 of them (58.4%) over 20 hours of agentic work.

That run is reproducible, whereas the viral screenshot was not. It remains a community benchmark, and the official DeepSWE leaderboard does not list Ox Alpha at all.

## One model, different routes, different privacy expectations

The Ox Alpha model page says the provider retains prompts and completions and does not use them for training. OpenRouter’s broader [Stealth Program terms](https://openrouter.ai/terms/stealth), which govern all other use, grant a license described in the document as irrevocable and perpetual. OpenCode says its Zen providers follow zero-retention and no-training policies. Its published list of exceptions does not include Ox Alpha.

OpenRouter currently publishes conflicting disclosures: Ox Alpha’s page says retained data is not used for training, while the incorporated Stealth EULA licenses state that submitted content is used for training and improvement. They produce materially different privacy expectations depending on how a team reaches the model. A developer cannot infer any of it from the model name.

Scale makes that gap operational rather than academic, because coding agents have pushed billions of tokens through Ox Alpha since Thursday. That traffic can include repository contents, test logs, environment output, and screenshots from private production codebases.

If the Z.ai attribution holds, a second diligence question comes up. The Commerce Department [added](https://www.federalregister.gov/documents/2025/01/16/2025-00704/addition-of-entities-to-and-revision-of-entry-on-the-entity-list) Zhipu AI, the company’s former name, to its Entity List in January 2025. The rule said that the listed entities advance China’s military modernization by developing and integrating advanced AI research. Export controls govern items subject to the EAR, not ordinary API traffic, so nothing here makes the call unlawful. It does put the vendor in a category most enterprise procurement teams screen for.

## The reveals that settled anything came through first-party channels

OpenRouter [named](https://openrouter.ai/announcements/quasar-alpha-and-optimus-alpha-reveal) Quasar Alpha and Optimus Alpha as early GPT-4.1 tests on its own blog. Xiaomi [confirmed](https://www.technology.org/2026/03/19/whos-that-ai-the-mystery-model-everyone-blamed-on-deepseek-turned-out-to-be-xiaomi/) Hunter Alpha as an early MiMo build itself. Community fingerprinting has pointed to the right lab before, but it has never been enough to close the question.

The fair counterargument is that anonymous previews gather unbiased evaluations ahead of a launch, which is a legitimate reason to run one.

> A name will appear on someone’s blog within weeks, long after every team that shipped a private repository through the free preview made that decision without one.

Ox Alpha also carries more restrictive data terms than OpenRouter’s generic Stealth Program terms, which contemplate training on submitted user content.

A name will appear on someone’s blog within weeks, long after every team that shipped a private repository through the free preview made that decision without one.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)