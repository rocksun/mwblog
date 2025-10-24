[Lightning AI](https://lightning.ai/), the company behind the [PyTorch Lightning project](https://thenewstack.io/pytorch-lightning-and-the-future-of-open-source-ai/) that strives to remove the complexities of using [PyTorch](https://thenewstack.io/why-pytorch-gets-all-the-love/), today announced several new tools and features in its commercial offering. These should make it easier for AI teams to build on top of its end-to-end PyTorch platform.

## PyTorch Lightning

The open source [PyTorch Lightning project](https://github.com/Lightning-AI/pytorch-lightning) is a lightweight framework that eliminates much of the boilerplate of working with PyTorch while also making it easier to create PyTorch projects in a structured way.

And while Lightning is at the core of what Lightning AI does, the company’s platform is far broader and includes, among other things, the cloud-based Lightning Studio development environment for training and deploying models, a Jupyter-based notebook environment,  a GPU marketplace, and an infrastructure service for hosting and building AI and machine learning  applications.

## Updates to Lightning AI

These updates include a new AI code editor for its Lightning Studios and Notebooks environments, as well as Lightning Environments, which are essentially sandboxed but scalable environments for exploring, training and scaling distributed AI workloads. The updates also include support for both [Meta’s](https://about.meta.com/?utm_content=inline+mention) Monarch distributed programming framework for PyTorch and Forge, Meta’s new reinforcement-learning framework that leverages Monarch’s distributed infrastructure.

“Our goal is to make every developer in the world a PyTorch developer,” added [William Falcon](https://www.linkedin.com/in/wfalcon/), the CEO of Lightning AI and creator of PyTorch Lightning. “Whether you’re training a model on one GPU or hundreds, Lightning gives you the same tight, interactive loop now supercharged by AI and instantly connected to the compute you need.”

[![](https://cdn.thenewstack.io/media/2025/10/f1669819-lightning-ai-studio-1024x578.png)](https://cdn.thenewstack.io/media/2025/10/f1669819-lightning-ai-studio-1024x578.png)

(Source: Lightning AI)

The marquee feature of the new release is the AI code editor. You can think of it as Lightning’s version of a copilot-style agent that is now built into Lightning Studios (its IDE) and Notebooks (think Jupyter). It features AI agents backed by a model that was specifically trained to be a PyTorch expert for helping developers complete training, inference and reinforcement learning tasks.

These agents can also use the [Lightning Model API](https://lightning.ai/models?section=allmodels) that provides access to a wide variety of proprietary and open weight models.

## Sharable Environments

Another core feature of Lightning AI is its environments, which the company describes as “self-contained, interactive spaces where developers can explore, train, and scale reinforcement learning and distributed AI workloads.”

What’s new now is that developers can share these setups through what the company calls its Environments Hub. That should make it much easier for new developers on the platform to get started with a project.

[![](https://cdn.thenewstack.io/media/2025/10/cb11d360-environment-gallery-1024x655.png)](https://cdn.thenewstack.io/media/2025/10/cb11d360-environment-gallery-1024x655.png)

(Source: Lightning AI)

## Meta’s Monarch Comes to Lightning AI

Also now in this release is support for [Monarch](https://pytorch.org/blog/introducing-pytorch-monarch/), Meta’s new distributed programming framework that aims to make working with PyTorch clusters as easy as working with a single machine.

PyTorch Monarch makes cluster-scale training interactive and persistent. Developers can iterate on experiments, debug issues and modify code in real time, all without having to restart or re-allocate their compute resources.

When integrated with Lightning’s Multi-Machine Training service, this allows developers to scale from a single notebook in Lightning Studio, for example, to hundreds of GPUs across multiple cloud providers while staying within their familiar PyTorch workflows.

[![](https://cdn.thenewstack.io/media/2025/10/eaa0ca2b-5-1.png-1024x634.avif)](https://cdn.thenewstack.io/media/2025/10/eaa0ca2b-5-1.png-1024x634.avif)

(Source: Meta)

“Monarch redefines what distributed training feels like,” said [Luca Antiga](https://www.linkedin.com/in/lantiga), the CTO of Lightning and chair of the PyTorch Foundation’s Technical Advisory Council. “Together with Meta’s PyTorch team, we’re making large-scale development as interactive and flexible as local experimentation. This empowers the next generation of AI builders to move faster than ever.”

Meta also recently launched [TorchForge](https://github.com/meta-pytorch/torchforge), a PyTorch-native reinforcement learning (RL) framework that sits on top of Monarch. It lets developers write their RL algorithms in pseudocode, with Monarch handling the execution.

Lightning AI now supports TorchForge, as well as Meta’s new OpenEnv open standard for packaging and sharing RL environments.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)