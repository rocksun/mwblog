# Anthropic Launches Its Most Powerful Models for Coding Yet
![Featued image for: Anthropic Launches Its Most Powerful Models for Coding Yet](https://cdn.thenewstack.io/media/2025/05/45c94973-img_0980-1024x768.jpg)
SAN FRANCISCO — At its first developers conference, [Code with Claude](https://www.anthropic.com/news/Introducing-code-with-claude), AI company Anthropic today [launched](https://www.anthropic.com/news/claude-4) the latest versions of its large language models (LLMs): Claude Opus 4 and Claude Sonnet 4.

These updates promise significant advancements for developers and engineering teams, particularly in coding and long-context reasoning. In all coding-related benchmarks, both models easily outperform their predecessors, though in some other areas like visual reasoning, the old Sonnet model actually outperformed the new one.

While Sonnet 3.7 already offered a hybrid approach, with both a rapid response and an extended thinking mode for deeper reasoning, Opus 4 previously lacked this adjustable capability. This update brings the same dual-mode functionality to Opus 4.

![](https://cdn.thenewstack.io/media/2025/05/12f6fe38-anthropic-amodei.jpeg)
Anthropic CEO Dario Amodei at the company’s Code with Claude conference. Image credit: The New Stack.

These new models are immediately available, on platforms like Anthropic’s own API, Amazon Bedrock and Google’s Vertex AI. Claude Sonnet 4 is available for free on Claude.ai, while Opus 4 is available for paying users.

“Claude 4 marks a new era in AI collaboration,” the company says. We’re building Claude to be your trusted partner — operating with full context, sustaining focus on longer projects, and driving transformational impact at every step.”

![Anthropic benchmarks for Opus 4 and Sonnet 4](https://cdn.thenewstack.io/media/2025/05/ec51a21a-claude-4-benchmarks.png)
Image credit: Anthropic.

## Opus 4
Opus is the name for Anthropic’s flagship models. When Opus 3 [launched](https://www.anthropic.com/news/claude-3-family) just over a year ago, it cemented Anthropic’s reputation as offering some of the best models for coding use cases. The company describes Opus 4 as its most powerful model yet and “the best coding model in the world.” The company says it also excels at problem-solving and powering agent products.

Meanwhile, GitHub, which uses Claude as the basis for its new Software Engineering (SWE) agent, says that it achieved 9% better results using 30% fewer tokens with Opus 4.

![](https://cdn.thenewstack.io/media/2025/05/87caa1cc-claude-plays-pokemon.gif)
Claude plays Pokemon. Image credit: Anthropic.

In part, what makes Opus 4 stand out is that it can handle long-running tasks and maintain its context across what Anthropic describes as “thousands of steps.” Some of the model’s testers have already been able to

this new capability.“Opus 4 offers truly advanced reasoning for coding,” said Yusuke Kaji, General Manager, AI, Rakuten. “When our team deployed Opus 4 on a complex open source project, it coded autonomously for nearly seven hours — a huge leap in AI capabilities that left the team amazed.”

Anthropic kept the price for using Opus 4 the same as for its predecessor, with API usage coming $15 per million tokens of input and $75 per million tokens of output from the model.

![](https://cdn.thenewstack.io/media/2025/05/c1332f04-4_swe-bench.png)
Image credit: Anthropic.

## Sonnet 4
Like most other LLM companies, including OpenAI and Google,

offers a variety of models at different price points (Haiku, which is not getting an update today, is the company’s fastest and least expensive model, but also its least intelligent.)For Sonnet 4, Anthropic says this new version improves upon Sonnet 3.7, which has long led the [SWE-bench](https://www.swebench.com/) benchmark for evaluating models on software engineering tasks. It now scores 72.7% compared to 62.3% for the previous version.

“The model balances performance with practicality for both internal and external use cases, while offering enhanced steerability that gives you greater control over how it implements changes,” Anthropic claims.

At the company’s launch event in San Francisco today, Anthropic CEO Dario Amodei also noted that Sonnet 4 is not as overeager as its predecessor, a common complaint among developers who used the previous version and often saw it as a bit of a disappointment compared to Sonnet 3.5.

It’s not just the models themselves, though, that Anthropic improved. It also added a few new capabilities to how users will be able to work with these models. Both Opus 4 and Sonnet 4 can now use tools, including web search, while thinking through a problem. What’s maybe most interesting here is that they can switch back and forth between tool usage and reasoning as they try to improve their responses. They can even use multiple tools in parallel.

Additionally, when permitted, the models can now access local files. This enables them to “demonstrate significantly improved memory capabilities, extracting and saving key facts to maintain continuity and build tacit knowledge over time,” Anthropic states.

Anthropic also kept the price for Sonnet 4 steady. It remains at $3/$15 (input/output) per million tokens.

## Claude Code
In addition to the new models, Anthropic is also making Claude Code, its agentic coding tool, generally available today. Claude Code can live in the terminal and, now, the developer’s IDE. Anthropic is making extensions available for VS Code and JetBrains. That puts it directly into competition with tools like GitHub Copilot, as well as Cursor and Windsurf (which, to make this more interesting, make Anthropic’s models available to developers in their tools, too).

Anthropic is also releasing a new Claude Code SDK so that developers can build their own agents and applications with the Claude Code agent at their core.

The sample code for the SDK is quite interesting: it’s Claude Code on GitHub. With this, developers can now tag Claude on pull requests to “respond to reviewer feedback, fix CI errors, or modify code.” Anthropic and GitHub have long been close partners.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)