**While most AI coding tools default to cloud-hosted models**, local model runtimes [have become a viable alternative](https://thenewstack.io/how-to-run-a-local-llm-via-localai-an-open-source-project/) for developers who want to keep code on their own machines, avoid per-request API costs, or have to work without an internet connection.

[Tools such as Cline](https://thenewstack.io/open-source-coding-agents-like-opencode-cline-and-aider-are-solving-a-huge-headache-for-developers/), [Continue](https://thenewstack.io/cursor-acquires-continue-coding/), and [Aider](https://thenewstack.io/developer-walk-through-of-aider-an-open-source-agentic-cli/) can already be pointed at runtimes like [Ollama](https://ollama.com/) or [LM Studio](https://lmstudio.ai/). At the same time, GitHub added local-model support to Copilot CLI [in April](https://github.blog/changelog/2026-04-07-copilot-cli-now-supports-byok-and-local-models/), including an offline mode for fully air-gapped setups.

The catch is that “local” generally still leaves much of the assembly to the developer. You have to choose a model and a suitable quantization for your hardware, configure the runtime and context settings, and work out which combination performs well with the agent.

And that last part really does matter: models small enough to run comfortably on a laptop can still struggle with the tool use, reasoning, and longer-running tasks that coding agents demand.

This is why JetBrains has now built [Junie Local](https://junie.jetbrains.com/local), a free version of its coding agent designed to run entirely on the developer’s own machine.

## Local market

By way of a brief recap, [JetBrains](https://www.jetbrains.com/) — the developer tools company behind [IntelliJ IDEA](https://www.jetbrains.com/idea/), [PyCharm](https://www.jetbrains.com/pycharm/) and [WebStorm](https://www.jetbrains.com/webstorm/) — launched Junie [in January 2025](https://blog.jetbrains.com/junie/2025/01/meet-junie-your-coding-agent-by-jetbrains/) as an AI coding agent embedded in its IDEs, capable of planning tasks, modifying code, running tests and inspections, and working with the context of a developer’s project. It has since [expanded into a standalone CLI](https://thenewstack.io/jetbrains-names-the-debt-ai-agents-leave-behind/).

Junie itself isn’t exactly new to local models. In a [blog post](https://blog.jetbrains.com/junie/2026/08/junie-local-launch/) published on Monday, JetBrains’ head of marketing [Dmitry Savelev](https://www.linkedin.com/in/dsaveliev/) notes that developers have been able to connect the agent to runtimes such as Ollama and LM Studio for some time, load whichever model they want, and have Junie run against it locally.

However, with Junie Local, JetBrains has picked the model, quantized it, and tuned its inference engine and agent harness around that specific combination. Setup is handled from inside Junie itself: running */local* downloads the model and inference engine, starts a local server, and switches the agent over automatically. There is no separate Ollama or LM Studio installation, endpoint to configure, or model profile to write.

The first step is simply choosing Junie Local from the model selector, where it appears alongside the usual array of cloud-hosted models.

![Junie’s model selector offers Junie Local alongside its cloud-hosted models](https://cdn.thenewstack.io/media/2026/08/d6db6ef4-gif1.gif)

*Junie’s model selector offers Junie Local alongside its cloud-hosted models*

Once the download and setup are complete, Junie switches to the local Qwen model, which then appears in the CLI like any other model option.

![Junie running with Qwen3.6 locally](https://cdn.thenewstack.io/media/2026/08/684ace87-gif2.gif)

*Junie running with Qwen3.6 locally*

From that point on, inference happens entirely on the developer’s machine.

## Under the hood: Why Qwen3.6 — and why an M5 Mac

It’s worth noting that JetBrains has been very specific about its model choice and hasn’t opted for the latest, shiniest open-weight version. Junie Local uses Qwen3.6-27B, a 27-billion-parameter open-weight model [released in April](https://qwen.ai/blog?id=qwen3.6-27b), even though the newer [Qwen3.8-](https://thenewstack.io/alibaba-qwen3-8-max-reactions/)[2](https://thenewstack.io/qwen38-27b-local-inference/)[7B](https://thenewstack.io/alibaba-qwen3-8-max-reactions/) arrived earlier in August with improvements.

> “On today’s Macs, [Qwen] 3.6 wins.”

Savelev notes that the choice came down to *how* the two models behaved inside Junie on current Macs, with Qwen3.8 requiring its reasoning mode to be enabled to work reliably with the agent; with reasoning switched on, tasks took roughly four times longer. For Junie Local right now, Qwen 3.6 offers the better balance of reliability and speed.

“On today’s Macs, 3.6 wins,” Savelev writes.

JetBrains runs Qwen3.6-27B at 4-bit using an inference engine based on mlx-vlm, which in turn uses [MLX](https://opensource.apple.com/projects/mlx/), Apple’s machine-learning framework for Apple Silicon. It’s a similar underlying approach to the one [Ollama adopted in March](https://thenewstack.io/ollama-taps-apples-mlx/), when it moved its Apple Silicon engine onto MLX to take advantage of the chips’ unified-memory architecture.

There is a fairly substantial hardware floor, though: JetBrains confirms that Junie Local involves about 20 GB of downloads, and requires macOS 26, at least 64 GB of unified memory, and an Apple M5 chip or newer. In real terms, that 64 GB requirement puts MacBook Pro users into M5 Pro or M5 Max territory — in other words, this is firmly a high-end Mac proposition.

JetBrains acknowledges that those requirements will put Junie Local beyond the reach of plenty of developers who might otherwise be interested in running it.

“We know that an M5 Mac with 64 GB of RAM is a big ask,” Savelev writes. “We are not going to pretend otherwise. That is simply what it costs to run a 27B model well today, and it is the number we are working hardest to bring down.”

> “We know that an M5 Mac with 64 GB of RAM is a big ask. We are not going to pretend otherwise.”

The intention is to reduce memory requirements, support a wider range of hardware, and continue optimizing the underlying stack.

“If the lofty requirements are the reason you cannot try Junie Local, rest assured that we are working to bring them down,” Savelev adds.

## Where local pays off

Ultimately, the hardware requirement is closely tied to where JetBrains identifies the real performance bottleneck for a local coding agent. The tokens-per-second metric measures how quickly a model generates output, but an agent can spend much of its time first ingesting source files, prompts and other context — the prefill stage — before it starts producing an answer.

“Everyone benchmarks generation speed,” Savelev writes. “For a coding agent, that turns out to be the wrong number to chase because most of the time is spent on prefill, while the model reads files to work out what is going on. Optimizing for prefill is where the real gains were.”

Being free and unmetered also changes the kinds of jobs developers might be willing to hand over. JetBrains positions Junie Local as particularly well-suited to long, repetitive, and mechanical work — multi-file refactors and renames, filling test-coverage gaps, dependency upgrades, and framework migrations — where the agent can keep working and iterating without the developer having to think about how many tokens it’s burning through.

“Long, repetitive, mechanical work is exactly what an agent is for, and exactly what you stop asking for when you are keeping an eye on your balance,” Savelev writes.

> “Long, repetitive, mechanical work is exactly what an agent is for, and exactly what you stop asking for when you are keeping an eye on your balance.”

For everyday development work, Savelev reckons users are unlikely to notice much of a gap compared with stronger cloud models. However, he does concede that more complex architectural reasoning remains better suited to those models.

And then, of course, there is arguably the biggest reason developers have been interested in local models in the first place: privacy. Running the entire agent locally means that no external model provider sits between the developer and their code, and that no source, prompts, or generated changes need to leave the machine. For developers working on proprietary code, under client NDAs, or in environments where sending source to a third party is simply off the table, that is a substantial part of the appeal.

“Everything after the download happens on your hardware, so your prompts, source, and diffs stay put,” Savelev writes.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)