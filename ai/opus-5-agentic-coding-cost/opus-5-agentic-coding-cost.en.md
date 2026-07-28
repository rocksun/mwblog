On Friday, [Anthropic launched Opus 5](https://thenewstack.io/anthropics-opus-5-almost-fable-5/), the latest iteration of its heavyweight model. Arriving just two months after Opus 4.8 and following the June releases of Mythos 5, [Fable 5](https://thenewstack.io/fable-5-permanent-subscription-access/), and Sonnet 5, Opus 5 rounds out the new generation — only the lightweight Haiku waits for an upgrade.

While smaller than the flagship Fable 5, Opus 5 is significantly cheaper and noticeably less restrictive. Opus 5 is designed to work on programming tasks for much longer without constant human input.

> Opus 5 is designed to work on programming tasks for much longer without constant human input.

## Benchmarks at bargain prices

Priced at $5 per million input tokens and $25 per million output tokens, Opus 5 upends the cost-to-performance ratio for agentic tasks. On coding and knowledge work evaluations like Frontier-Bench and GDPval-AA, Opus 5 establishes a new state of the art.

In the OSWorld 2.0 computer use benchmark, it outperforms every other model at any given cost, surpassing Fable 5’s best result at just over a third of the price. On ARC-AGI 3, an evaluation where the model has to solve novel problems, its score is three times as high as the next best model.

> Because Opus 5 is less expensive to run, teams can afford to let it work through larger coding tasks. That also means thinking differently about security.

Anthropic [writes](https://www.anthropic.com/news/claude-opus-5) in the company announcement that Opus 5 is “much stronger at verifying its work and iterating carefully until it succeeds.” During benchmark testing, the model was given an incomplete prompt and intentionally prevented from viewing a drawing of a machine part. Instead of giving up, it wrote its own computer vision pipeline to reconstruct the part from the image data.

Because Opus 5 is less expensive to run, teams can afford to let it work through larger coding tasks. That also means thinking differently about security, which is one reason microVMs are getting more attention. Unlike long-running containers, they give platform teams an isolated environment they can tear down as soon as a task is finished.

## Security for unsupervised agents

When a model is working across multiple systems without constant human oversight, access has to be temporary and easy to revoke. That’s why more attention is shifting to short-lived, just-in-time credentials, similar to the [delegated authentication model 1Password is developing for Claude](https://thenewstack.io/1password-agent-authentication-framework/).

There’s a catch to giving an AI relentless persistence: it doesn’t know when to quit. Your standard API logs won’t flag that behavior in time. Teams will have to build smarter telemetry that actually understands the context of the workflow. You need a semantic circuit breaker to pull the plug before the model burns through your compute budget.

## Controlling runaway token spend

Opus 5 drops the per-token price tag compared to Fable 5, but [autonomous coding can still get expensive fast](https://thenewstack.io/agentic-ai-token-costs/). An agent working through background loops for hours will churn through millions of tokens before handing off a PR. For platform teams, managing spend by the session becomes the new operational requirement.

To keep those background jobs from crashing on edge cases, Anthropic is launching Automatic Fallbacks in beta. If a prompt trips a safety classifier on Opus 5, the API silently reroutes the task to Opus 4.8 instead of throwing a hard error and killing the entire pipeline.

Opus 5 also inherits its predecessor’s zero-retention posture, bypassing the 30-day data logging mandatory for Fable and Mythos.

To understand where Anthropic expects these environment harnesses to operate, it helps to look at how they are artificially restricting the model. The company is threading a careful needle between short-horizon capability and long-horizon safety.

> If a prompt trips a safety classifier on Opus 5, the API silently reroutes the task to Opus 4.8 instead of throwing a hard error and killing the entire pipeline.

## Biological capability, careful limits

Anthropic spokesperson tells *The New Stack*, Opus 5 is a “meaningful improvement over Opus 4.8 on biology tasks, making it our most capable generally available model for scientific research.” It scores 10.2 percentage points higher than Opus 4.8 on internal organic chemistry benchmarks (like inferring molecular structures from spectroscopy data) and 7.7 percentage points higher in predicting how protein sequence variations determine function.

However, Anthropic’s testing revealed “significant limitations on long-running autonomous research tasks,” which they view as carrying the highest potential risk. As a result, Opus 5 retains a similar portfolio of biological safeguards to Opus 4.8. While biology-related requests blocked on Fable 5 will now route to Opus 5 instead of 4.8, the uncapped Mythos 5 remains the stronger model for long-horizon, open-ended work like autonomous drug design campaigns.

Opus 5 can review source code for defensive security work. Anthropic says those [safeguards should activate far less often than they do with Fable 5](https://thenewstack.io/fable-5-honeycomb-opus/) — about 85% less, according to the company.

Clearly, the models are improving quickly, but the bigger challenge now is making sure the platforms they’re running on can keep up.

## Major AI model releases: a timeline

| Release date | AI model | Company | *The New Stack* report |
| --- | --- | --- | --- |
| July 24, 2026 | Opus 5 | Anthropic | [Anthropic’s Opus 5 is almost Fable 5](https://thenewstack.io/anthropics-opus-5-almost-fable-5/) |
| July 21, 2026 | Gemini 3.6 Flash, 3.5 Flash-Lite and 3.5 Flash Cyber | Google | [Google ships 3 new Gemini models. Just not the one everyone’s waiting for.](https://thenewstack.io/google-ships-3-new-gemini-models-just-not-the-one-everyones-waiting-for/) |
| July 16, 2026 | Kimi K3 | Moonshot AI | [Kimi K3 tops Arena’s coding leaderboard — and it’s open-weight](https://thenewstack.io/kimi-k3-open-weight-coding/) |
| July 9, 2026 | GPT-5.6 Sol, Terra and Luna | OpenAI | [OpenAI’s GPT-5.6 is now live](https://thenewstack.io/openai-gpt-56-live/) |
| July 9, 2026 | Muse Spark 1.1 | Meta | [Meta debuts Muse Spark 1.1 — its first paid AI model](https://thenewstack.io/meta-muse-spark-api/) |
| July 8, 2026 | Grok 4.5 | SpaceXAI | [“Opus-class, but faster”: What Elon Musk says about beating Anthropic](https://thenewstack.io/grok-45-opus-killer-launch/) |
| June 30, 2026 | Claude Sonnet 5 | Anthropic | [Anthropic Sonnet 5: It closes the gap with Opus 4.8, and is cheap until August](https://thenewstack.io/claude-sonnet-5-launch/) |
| June 9, 2026 | Claude Fable 5 and Claude Mythos 5 — Mythos restricted | Anthropic | [Anthropic launches Claude Mythos/Fable 5, but you better try it soon](https://thenewstack.io/anthropic-claude-mythos-fable-5/) |
| May 28, 2026 | Claude Opus 4.8 | Anthropic | [Claude Opus 4.8 is here: effort controls, dynamic workflows, cheaper fast mode, better honesty, less deception](https://thenewstack.io/claude-opus-48-release/) |
| May 19, 2026 | Gemini 3.5 Flash | Google | [Google’s Gemini 3.5 Flash beats the frontier models](https://thenewstack.io/googles-gemini-3-5-flash-beats-the-frontier-models/) |
| April 23, 2026 | GPT-5.5 and GPT-5.5 Pro | OpenAI | [OpenAI launches GPT-5.5, calling it “a new class of intelligence”](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/) |
| April 16, 2026 | Claude Opus 4.7 | Anthropic | [Claude Opus 4.7 arrives with better vision, memory, and instruction-following](https://thenewstack.io/claude-opus-47-launch/) |
| April 7, 2026 | Claude Mythos Preview — restricted release | Anthropic | [Anthropic’s Claude Mythos is now available, but not for you](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/) |
| March 5, 2026 | GPT-5.4 Thinking and GPT-5.4 Pro | OpenAI | [OpenAI launches GPT-5.4 Thinking and Pro](https://thenewstack.io/openai-launches-gpt-5-4/) |
| Feb. 19, 2026 | Gemini 3.1 Pro | Google | [Google’s Gemini 3.1 Pro is mostly great](https://thenewstack.io/googles-gemini-3-1-pro-is-mostly-great/) |
| Feb. 17, 2026 | Claude Sonnet 4.6 | Anthropic | [Anthropic’s new Claude Sonnet 4.6 promises Opus-level coding at Sonnet pricing](https://thenewstack.io/claude-sonnet-46-launch/) |
| Feb. 5, 2026 | GPT-5.3-Codex | OpenAI | [OpenAI’s GPT-5.3-Codex helped build itself](https://thenewstack.io/openais-gpt-5-3-codex-helped-build-itself/) |
| Feb. 5, 2026 | Claude Opus 4.6 | Anthropic | [Anthropic debuts Opus 4.6 with standout scores for solving hard problems that other AIs miss](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/) |
| Dec. 17, 2025 | Gemini 3 Flash | Google | [Google’s New Gemini 3 Flash Rivals Frontier Models at a Fraction of the Cost](https://thenewstack.io/googles-new-gemini-3-flash-rivals-frontier-models-at-a-fraction-of-the-cost/) |
| Nov. 24, 2025 | Claude Opus 4.5 | Anthropic | [Anthropic’s New Claude Opus 4.5 Reclaims the Coding Crown](https://thenewstack.io/anthropics-new-claude-opus-4-5-reclaims-the-coding-crown-from-gemini-3/) |
| Nov. 19, 2025 | GPT-5.1-Codex-Max | OpenAI | [OpenAI Says Its New Codex-Max Model Is Better, Faster and Cheaper](https://thenewstack.io/openai-says-its-new-codex-max-model-is-better-faster-and-cheaper/) |
| Nov. 18, 2025 | Gemini 3 Pro | Google | [Google Launches Gemini 3 Pro](https://thenewstack.io/google-launches-gemini-3-pro/) |
| Sept. 29, 2025 | Claude Sonnet 4.5 | Anthropic | [Anthropic Launches Claude Sonnet 4.5](https://thenewstack.io/anthropic-launches-claude-sonnet-4-5/) |
| Sept. 15, 2025 | GPT-5-Codex | OpenAI | [OpenAI Launches a New GPT-5 Model for Its Codex Coding Agent](https://thenewstack.io/openai-launches-a-new-gpt-5-model-for-its-codex-coding-agent/) |
| Aug. 7, 2025 | GPT-5 | OpenAI | [GPT-5: A Choose Your Own Adventure for Frontend Developers](https://thenewstack.io/gpt-5-a-choose-your-own-adventure-for-frontend-developers/) |
| May 22, 2025 | Claude Opus 4 and Claude Sonnet 4 | Anthropic | [Anthropic Launches Its Most Powerful Models for Coding Yet](https://thenewstack.io/anthropic-launches-claude-opus-4-and-sonnet-4/) |
| April 16, 2025 | o3 and o4-mini | OpenAI | [OpenAI Releases New Models Trained for Developers](https://thenewstack.io/openai-releases-new-models-trained-for-developers/) |
| April 14, 2025 | GPT-4.1, GPT-4.1 mini and GPT-4.1 nano | OpenAI | [OpenAI Releases New Models Trained for Developers](https://thenewstack.io/openai-releases-new-models-trained-for-developers/) |

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)