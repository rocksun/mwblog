On Tuesday, Anthropic launched [Claude Science](https://claude.com/product/claude-science), a new application for scientists that can run locally on macOS and Linux or on a remote machine. Anthropic describes it as its AI workbench “where scientists can conduct their research in one place.”

In both design and spirit, it feels a bit like Claude Cowork for scientists.

In its current form, Claude Science, now in beta, primarily targets researchers in the life sciences, but the name suggests the company plans to expand this over time.

## Available across Claude’s paid plans

To use it, you don’t have to be a scientist. It’s available on macOS and Linux for all users on the Claude Pro, Max, Team, and Enterprise plans (though for Team and Enterprise plans, the admin must enable it first). Anthropic is also offering discounted Team plans for research labs.

Anthropic notes that scientists often have to switch among numerous databases and tools such as PubMed, Jupyter, R, and the terminal. The promise of Claude Science is to bring all of these together by connecting Anthropic’s advanced models to the databases, platforms, and tools these researchers already use.

![](https://cdn.thenewstack.io/media/2026/06/341d48c5-claude-science-product-image_01_embargoed-until-tuesday-june-30-2026-10am-pt-1024x629.png)

*Credit: Anthropic*

As in most fields, scientific research involves a lot of repetitive work that doesn’t actually advance the science. The tool, Anthropic writes in its announcement, is meant to help “researchers analyze literature and execute multistep research, and is artifact-first, allowing users to iteratively refine figures and manuscripts until they’re ready for publication. Every output carries an auditable history of how it was made, so scientists can validate and reproduce the results.”

## Not a new model

Anthropic stresses that it isn’t launching a new model for Claude Science. Instead, it is backed by the standard Claude models. When users work with the tool, they first interact with a generalist coordination agent that has access to over 60 databases and a set of relevant skills. The tools also support any other service that they can connect to over MCP.

Anthropic is actually using the skills from Nvidia’s new [BioNeMo Agent Toolkit](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit) to connect to life sciences models and libraries, including Evo 2, Boltz-2, and OpenFold3.

> “The specialized science stays with the partners who built it.”

It’s worth noting that OpenAI is also [integrating](https://nvidianews.nvidia.com/news/nvidia-launches-bionemo-agent-toolkit-giving-ai-agents-the-tools-to-accelerate-scientific-discovery) the BioNeMo Agent Toolkit.

![](https://cdn.thenewstack.io/media/2026/06/7b569cc1-claude-science-product-image_02_embargoed-until-tuesday-june-30-2026-10am-pt-1024x629.png)

*Credit: Anthropic*

As Anthropic also notes, Claude Science is meant to be the reasoning layer and connective tissue. “The specialized science stays with the partners who built it,” the company explains.

Like Jupyter notebooks and similar tools, Claude Science can also generate visuals, including 3D protein structures and genome browser tracks. “Users can chat with the agent about any detail, annotating figures and manuscripts in-line so the agent knows what to address to make them publication-ready,” Anthropic explains.

The code for these visualizations is always available, as is the full message history of their creation.

## Connecting to HPC and Modal

Since Claude can’t exactly run large genomics pipelines or protein folding jobs itself, the tools can also interact with existing high-performance computing clusters via SSH or a [Modal](https://modal.com) account. This, Anthropic argues, ensures that the researchers don’t have to waste time on writing those jobs and troubleshooting them. Instead, Claude will draft a plan, the researchers will review it, and Claude will then submit it to the lab’s existing resources.

An agent then keeps an eye on the job and its outputs, flagging any issues. It’s also possible to fork the session at any point to try different approaches.

## The competition

Large language models do lend themselves to a service like Claude Science, and Google, OpenAI, and others are pushing in the same direction.

At its I/O conference in May, for example, Google launched “Gemini for Science,” which it also explicitly [pitched](https://blog.google/innovation-and-ai/technology/research/gemini-for-science-io-2026/) as “a scientific workbench on your desktop,” bundling science skills across 30-plus life-science databases and its “AI co-scientist” hypothesis engine. Google’s DeepMind, of course, also has a long history in using AI for life sciences research — and a Nobel prize to show for it.

OpenAI also made science and early focus with services like [Prism](https://openai.com/prism/), its tools for scientific writing, and [GPT-Rosalind](https://openai.com/index/introducing-gpt-rosalind/), a frontier model specifically built to accelerate scientific research and drug discovery. With the departure of [Kevin Weil](https://www.wired.com/story/openai-executive-kevin-weil-is-leaving-the-company/) in April of this year, though, OpenAI disbanded its OpenAI for Science and sunset Prism as it shifted its focus towards more of its core services (and Codex).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)