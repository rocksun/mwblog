Countless companies are capitalizing on the AI boom, building everything from [coding assistants](https://thenewstack.io/what-are-ai-code-assistants-and-how-should-you-use-them/) to customer support bots. But only a handful are building the foundational AI models themselves — the underlying systems that power it all.

That group is dominated largely by OpenAI, Anthropic, and Google, with the likes of [Mistral AI](https://mistral.ai/) sitting just outside that elite circle. Founded out of Paris in 2023, Mistral has raised billions from a who’s who of investors, [including Microsoft](https://techcrunch.com/2024/02/27/microsoft-made-a-16-million-investment-in-mistral-ai/) and [Nvidia](https://mistral.ai/news/mistral-ai-and-nvidia-partner-to-accelerate-open-frontier-models), all while pushing a more open approach — releasing open-weight models and giving developers more control over how they run them.

> On Wednesday, Mistral debuted a new model, Mistral Medium 3.5, alongside a system that lets its coding agents run in the cloud.

Now, the company is edging toward the same territory as some of its larger rivals. On Wednesday, Mistral [debuted](https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5) a new model, [Mistral Medium 3.5](https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04), alongside a system that lets its coding agents run in the cloud, where they can keep working in the background while developers get on with other things.

Additionally, Mistral is adding a “work mode” to [Le Chat](https://chat.mistral.ai/chat), its ChatGPT-style interface, that can take on longer jobs by calling tools in parallel, as it looks to move beyond chat and into doing actual work.

## Teleport to the cloud

Mistral’s coding assistant, [Vibe](https://mistral.ai/products/vibe), has until now mostly lived in the terminal, where developers could ask it to read a repo, edit files, run commands, fix bugs, or write tests from the command line. With this update, Mistral is pushing it into a different mode — one where you can spin up multiple agents in the cloud, let them work through tasks independently in isolated sandboxed environments, and come back to review what they’ve done.

Sessions can be started locally from the CLI or Le Chat and “teleported” to the cloud mid-task, preserving the full context — including the task itself, previous steps, and any changes made so far. From there, the agents continue running remotely, without being tied to the developer’s machine.

![Teleport to the cloud](https://cdn.thenewstack.io/media/2026/05/0036b09b-teleport.gif)

*Teleport to the cloud*

So instead of sitting in a loop, prompting and checking results, developers can hand off chunks of work and allow them to run in the background. Those tasks might include writing new features, updating code, or preparing changes as draft pull requests for later review.

Users can also launch Vibe directly from Le Chat. For example, they could ask it to build a sales dashboard, and it would run the task in a remote setup before returning a finished branch or a draft pull request.

![Launching Vibe from Le Chat](https://cdn.thenewstack.io/media/2026/05/ea4865c7-launchvibefromlechat.gif)

***Launching Vibe from Le Chat***

On top of that, Mistral is adding a “work mode” within Le Chat, where users can set broader tasks — like pulling together a meeting brief or updating documents — and have the system work through them using connected tools.

![Work Mode](https://cdn.thenewstack.io/media/2026/05/d21a7658-workmodegif.gif)

*Work Mode*

[Pini Wietchner](https://www.linkedin.com/in/pini-wietchner-45224513a/), who works on the Mistral product team, says in an [online discussion](https://www.youtube.com/watch?v=KaMbzM9dsTc) that the company has been dogfooding Vibe internally for its latest launch, with most of its pull requests handled remotely.

“We’ve seen internally that Vibe has been really effective,” Wietchner says during that company-produced YouTube video. “Our customers want to use agents both locally and remotely. A local agent is great for a developer working in their IDE or terminal on a coding task. Remote agents let them run multiple agents in parallel, in a secure way using our sandboxing setup.”

> “Our customers want to use agents both locally and remotely. A local agent is great for a developer working in their IDE or terminal on a coding task. Remote agents let them run multiple agents in parallel.”

## Model behavior

Underpinning all this is Mistral Medium 3.5, a 128B parameter model with a 256k context window, designed to handle longer, more involved tasks rather than quick prompts.

Mistral is positioning Medium 3.5 against models already used for similar workloads — including Claude Sonnet, Kimi K2.5, GLM 5.1, and Qwen 3.5, as shown in its reported results. On standard tests like SWE-bench Verified, which measures how well models can resolve real GitHub issues, the company reports competitive scores, alongside results on domain-specific tasks in telecom, retail, and banking. These figures come from Mistral’s own evaluations and may vary under different setups or conditions.

![Agentic benchmarks vs. competing models](https://cdn.thenewstack.io/media/2026/05/8f19cc18-frame-2147228534-1024x750.png)

*Agentic benchmarks vs. competing models*

For those all-in on Mistral’s stack, a more relevant comparison, perhaps, is against its own earlier models. By that measure, Medium 3.5 marks a step up from previous coding-focused releases such as [Devstral 2](https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512), according to the company’s reported Swe-Bench Verified results.

![Agentic benchmarks vs. previous Mistral models](https://cdn.thenewstack.io/media/2026/05/ef08fa34-frame-2147228532-1024x607.png)

*Agentic benchmarks vs. previous Mistral models*

## Building out the pieces

Mistral has been building toward this almost since its inception. In 2024, the company released [Codestral](https://huggingface.co/mistralai/Codestral-22B-v0.1), its [first dedicated coding model](https://mistral.ai/news/codestral), focused on everyday developer tasks like code completion and generation. More recently, it [followed up with Leanstral](https://thenewstack.io/leanstral-formal-verification-code/), which tackled a more difficult problem — using formal verification to check whether code is actually correct.

So rather than jumping straight to fully autonomous agents, Mistral has been building out the pieces: models that can write code, models that can check it, and now a system that tries to run that work in the background.

It’s also where the company starts to overlap more directly with bigger rivals. Anthropic, for example, has been pushing similar ideas with Claude Code, including tools that let developers run longer coding tasks and keep them going across sessions, whether in the [browser, on mobile](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/), or via [remote access to a local environment](https://code.claude.com/docs/en/remote-control).

What sets Mistral apart is how it’s packaging those ideas. Its models are typically released with open weights, and now tools like Vibe can run locally or in the cloud, giving developers more control over their use.

That doesn’t guarantee it will win out — far from it. But it does give Mistral something of a unique angle — especially in Europe, where Mistral has positioned itself as a homegrown alternative to the dominant US labs.

What is seemingly consistent across the board, however, is a growing desire to turn AI from something you have to keep steering into something that can handle chunks of work on its own.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)