[Perplexity](https://www.perplexity.ai/hub), in partnership with Nvidia, has taken [Computer](https://www.perplexity.ai/products/computer), its agentic AI assistant, and brought it to the desktop as Portable Computer.

While there is a lot of interest in local AI right now, getting started can still be difficult — and expensive. Portable Computer definitely makes it easier to get started, but to run it, you need the right kind of machine.

## Local AI’s hardware bill

As of now, there are two main options. The easiest way is to get a DGX Spark desktop from Nvidia running DGX OS. But if you have a more traditional PC that’s running Ubuntu on ARM or x64 hardware, and you have an Nvidia RTX card with at least 24GB of GPU VRAM, you’re also in business.

A DGX Spark will set you back $4,800, and even an older RTX 3090 card with 24GB of VRAM currently costs well over $1,500.

Thanks to [RAMmageddon](https://en.wikipedia.org/wiki/2025%E2%80%93present_global_memory_supply_shortage), this won’t likely get cheaper anytime soon.

Bringing Computer to the desktop took more than replacing a cloud model with a smaller one. It needs to be able to read and edit files, run shell commands, and process PDFs locally — but it also needs to connect to external services. All of this, too, needs a local sandbox for the agent to run in.

To account for these smaller models, Nate Kupp, Perplexity’s vice president of Computer Enterprise and Infrastructure, tells *The New Stack* that the team had to “revisit almost everything throughout the stack.” The company reused many of Computer’s capabilities, he says, but changed the harness and model configuration for local hardware.

Indeed, the harness accounted for most of the engineering work, says Kupp. The model still has to plan tasks, call tools, manage files, and execute multi-step tasks, all with fewer parameters than the much larger models that Perplexity typically uses in its cloud service.

Perplexity says the orchestrator that maintains the agent loop is deterministic code and not yet another AI model. In this system, the local model proposes an action, while the orchestrator assembles the context, enforces policy, and runs approved tool calls in an OS-level sandbox.

## Inside the local harness

According to the company, that sandbox restricts processes, filesystem paths, and network access. If the sandbox isn’t available, the harness disables itself before making any tool calls instead of running them outside the sandbox.

The harness is also designed around the model’s practical context limit. Perplexity says Qwen3.8-27B supports a 260,000-token context window but begins to struggle beyond 100,000 tokens. Because of this, portable Computer keeps the core prompt and tool set small and only loads additional skills as needed.

In addition, Perplexity also turned commonly used connectors into command-line tools rather than exposing their larger Model Context Protocol (MCP) definitions directly to the model.

In recent weeks, it has become increasingly clear how important the harness is for agentic performance, something Kupp also noted in the briefing.

With the same Qwen3.8-27B base model and DGX Spark hardware, Computer scored 82.6% on Perplexity’s internal 53-task Local Knowledge Work Bench, compared with 77.6% for Pi and 74% for Hermes. On ParseBench-100, a 100-task subset covering charts, layouts, tables, text, and formatting, Computer scored 65.1%, while Hermes scored only 34.6% and Pi 13.9%.

Perplexity says it plans to open-source the internal benchmark.

## When a local task leaves the machine

With Portable Computer, each task starts on the local device. If the local model can’t complete a step, it can ask a cloud model for advice. Perplexity says the harness selects the relevant context, flags potentially sensitive information, shows the user what would be sent from the machine, and asks for approval before making that call.

The cloud model returns text guidance but does not get direct access to the device’s files or tools. The local orchestrator retains control of execution and incorporates the advice into the same local run.

In one demo, Portable Computer reviewed a folder of tax documents on an [Nvidia DGX Spark](https://thenewstack.io/nvidia-dgx-spark-the-new-stack-developers-guide/), while in a second demo, the local agent analyzed a CSV file and then posted its findings to Slack — demonstrating the agent’s ability to reach beyond the local machine.

Portable Computer includes connectors for Google Drive, Gmail, Slack, and GitHub. When used, web searches and connector calls leave the device, while Perplexity says model inference and private-document processing remain local.

Perplexity’s argument centers on convenience and privacy. Developers who want to go through all of the necessary steps can already combine a local model server with tools and an execution environment. Still, Kupp argues that Portable Computer comes ready to run. “You don’t have to fiddle around with inference,” he says.

Despite the similar name, Portable Computer isn’t [Personal Computer](https://thenewstack.io/mac-mini-agent-infrastructure/), Perplexity’s Mac and Windows application for working with local files and native apps. Portable Computer runs the model and harness locally, but “we’re not doing computer use at this point,” Kupp says.

## Starting with Nvidia

At launch, users can choose between [Qwen3.8-27B](https://thenewstack.io/qwen38-27b-local-inference/) and PPLX 27B, Perplexity’s post-trained version of that model.

Nvidia’s [Nemotron 3.5 Lightning](https://thenewstack.io/nvidia-nemotron-lightning-switchyard/) is coming later. Users can also bring their own models and inference servers.

Sadly, even if you have a very powerful Mac (or are pre-ordering one of the new ones), Portable Computer isn’t available for you yet. Windows support, however, is scheduled to follow in September.

“For now,” Kupp says, Perplexity is “very focused on Nvidia across DGX and RTX,” though he also says that the company is considering other hardware.

Portable Computer will be available to subscribers of Perplexity Pro, Max, Enterprise Pro, and Enterprise Max. Tasks completed locally don’t consume usage-based credits unless the system has to reach out to Perplexity’s cloud models.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)