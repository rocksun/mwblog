**Alibaba has launched Qwen3.8-Max**, a multimodal model with 2.4 trillion parameters and built for complicated tasks that may take several days to complete. Now available through QwenCloud and Alibaba Cloud Model Studio, it’s priced at $2 per million input tokens and $6 per million output tokens.

[Qwen3.8-Max](https://qwen.ai/blog?id=qwen3.8&utm_content=list_content_0_alibaba_says_its_latest_qwen_ai_model_beats_moonshots_kimi_k3&j=157227&sfmc_sub=30697404&l=1227_HTML&u=11189807&mid=546014653&jb=72&utm_source=sfmc&utm_medium=email&utm_campaign=NL_fortune-tech_2026-8-3_157227&utm_term=fortune-tech&sfmc_id=30697404) builds on the Qwen3.5 architecture and uses a sparse mixture-of-experts design with hybrid attention. Although the model contains 2.4 trillion parameters in total, it activates approximately 95 billion for each token.

The mixture-of-experts architecture draws on the parts of the model needed for each task — instead of running all 2.4 trillion parameters every time. According to the company, the model weights will be published on Hugging Face and ModelScope next week, making it the first Qwen-Max model released with downloadable weights.

> The model’s mixture-of-experts architecture draws on the parts of the model needed for each task, which still leaves developers with an enormous model to host.

## How the harness works

Even with only 95 billion parameters active at once, the full weights must be stored and distributed across multiple high-memory GPU nodes. In practice, that puts self-hosting beyond the reach of most developers and makes Qwen3.8-Max a more realistic option for large organizations and inference providers with the infrastructure to run it.

> Qwen3.8-Max is a realistic option for large organizations and inference providers with the infrastructure to run it.

This brings Alibaba close to Moonshot AI’s new Kimi K3, which has [2.8 trillion parameters](https://thenewstack.io/kimi-k3-open-weight-coding/). Alibaba holds a [36% stake in Moonshot AI](https://www.euronews.com/next/2026/08/03/alibabas-new-qwen-ai-claims-to-match-unsupervised-working-skills-touted-by-claude), so these are not fully independent rivals. Kimi K3 topped Arena’s frontend coding leaderboard within hours of its debut, and demand overwhelmed Moonshot’s GPU capacity so fast that the company had to pause new subscriptions. Kimi K3’s open-weight release ran into exactly this problem: Demand blew past GPU capacity within 48 hours, and the model’s 2.8T parameters made self-hosting impractical for all but the largest shops. Qwen3.8-Max now enters the same race.

## Other long-running demos

According to Alibaba’s tests, Qwen3.8-Max spent [16 days building a command-line app](https://pulse2.com/alibaba-introduces-2-4-trillion-parameter-qwen3-8-max-ai-model-with-1-million-token-context-window/), took [five days to reproduce a research paper’s results](https://the-decoder.com/alibabas-open-weight-qwen3-8-max-takes-on-long-horizon-ai-tasks-with-2-4-trillion-parameters/), and improved a [chip design after about 500 iterations](https://technofuzn.com/blog/qwen-3.8-max). Alibaba has not released enough information for outside researchers to verify these results.

Alibaba’s most ambitious software demo had Qwen3.8-Max spend 16 days building [“oh-my-cli”](https://github.com/qwen-code-dev-bot/oh-my-cli) on its own. During that time, it made [265 commits and opened 127 pull requests](https://pulse2.com/alibaba-introduces-2-4-trillion-parameter-qwen3-8-max-ai-model-with-1-million-token-context-window/) as it worked through [151 GitHub issues](https://pulse2.com/alibaba-introduces-2-4-trillion-parameter-qwen3-8-max-ai-model-with-1-million-token-context-window/). The repository and its audit trail are public under [qwen-code-dev-bot/oh-my-cli](https://github.com/qwen-code-dev-bot/oh-my-cli), so developers do not have to rely solely on Alibaba’s account of what happened.

> The difference between the model and its harness is key for long-running jobs.

The difference between the model and its harness is key for long-running jobs. The model decides what to do next, but the system around it handles everything else. These parts can decide if an agent runs for 16 days or fails after just 16 minutes.

That infrastructure layer is what [Anthropic acquired the CI/CD startup Mendral to build out](https://thenewstack.io/anthropic-mendral-cicd-acquihire/), and it’s the same lesson [GoDaddy learned when it opened its registrar to AI agents](https://thenewstack.io/godaddy-developer-platform-domains/); the guardrails had to come first.

Alibaba says it trained Qwen3.8-Max on complicated projects that an agent might actually encounter. The model performed similarly when tested with QwenWork, Claude Code, Codex, OpenClaw and Hermes.

The company has [published guides](https://www.trendingtopics.eu/qwen3-8-max-is-the-next-chinese-open-weights-assault-on-the-ai-frontier/) showing developers how to connect it to those tools. Developers should soon be able to put that claim to the test. Model Studio works with the OpenAI and Anthropic API formats, so teams can bring Qwen3.8-Max into coding tools they already use without rebuilding their setup from scratch.

## Context window limits

In one experiment, the model was given the paper “Unified Data Selection for LLM Reasoning” without any code. Alibaba says the agent wrote about 7,600 lines of code, started 33 GPU training jobs, and reproduced the paper’s six main results. It also tested 18 more ideas and improved the reported AIME24 result by 2.7 points.

In another test, Qwen3.8-Max optimized a cryptographic circuit over about 500 iterations. Alibaba says the model cut the design from [8,298 logic gates to 678](https://technofuzn.com/blog/qwen-3.8-max). After running it through OpenROAD, an open-source chip design tool, the physical area dropped by 81%.

This was not a one-shot coding test. The agent had to inspect each result and use it to decide what to try next. But even a million-token context window can only take an agent so far. Developers will want to see whether Qwen3.8-Max can remember earlier decisions and instructions as a project grows.

Sending nearly one million tokens at every step would cause other problems — and as [the economics of agentic AI have shown](https://thenewstack.io/agentic-ai-token-costs/), cheaper per-token pricing does not automatically translate to cheaper projects when autonomous agents are consuming tokens at rates that dwarf human-supervised sessions.

> But even a million-token context window can only take an agent so far. Developers will want to see whether Qwen3.8-Max can remember earlier decisions and instructions as a project grows.

## Benchmarks need outside verification

Alibaba’s internal benchmarks show Qwen3.8-Max performing close to models from Anthropic and OpenAI. According to Alibaba, it scored 86.6 on Terminal-Bench 2.1, compared to 88.8 for OpenAI’s GPT-5.6 Sol (max). Independent runs of the same benchmark produce somewhat different scores for both models, so these figures may shift once outside labs repeat the tests. It also placed [fifth in Text Arena and second in Vision Arena](https://www.trendingtopics.eu/qwen3-8-max-is-the-next-chinese-open-weights-assault-on-the-ai-frontier/). In [Alibaba’s own comparison table covering 31 tests](https://www.trendingtopics.eu/qwen3-8-max-is-the-next-chinese-open-weights-assault-on-the-ai-frontier/), the model leads in six; Claude Fable 5 or GPT-5.6 Sol comes out ahead in most of the rest.

These results make Qwen3.8-Max a strong contender, but they do not yet prove the model can maintain production software on its own for weeks. Once Alibaba releases the weights, developers can find out how well Qwen3.8-Max works outside the company’s own setup. If its performance drops when it is moved to different infrastructure or connected to other coding tools, that will tell us far more than its place on a leaderboard.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)