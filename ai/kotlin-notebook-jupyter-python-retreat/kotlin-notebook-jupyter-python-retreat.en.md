[JetBrains](https://www.jetbrains.com/), the Czech developer tools company behind the IntelliJ IDEA IDE, [announced Monday](https://blog.jetbrains.com/idea/2026/06/kotlin-notebook-sunset/) that it’s sunsetting [Kotlin Notebook](https://kotlinlang.org/docs/kotlin-notebook-overview.html), the interactive coding plugin it first launched in July 2023.

Starting with [IntelliJ IDEA 2026.2](https://blog.jetbrains.com/idea/2026/05/intellij-idea-2026-2-eap/), the plugin will be unbundled from the IDE and handed to the open-source community under the Apache 2.0 license — the first time its source code has been made publicly available. JetBrains will publish no compatible version for 2026.3 and beyond, meaning whoever picks this up faces an immediate compatibility cliff.

> “Kotlin Notebook didn’t reach the level of adoption we expected.”

Almost exactly three years [after](https://blog.jetbrains.com/kotlin/2023/07/introducing-kotlin-notebook/) its launch, [Marco Behler](https://www.linkedin.com/in/marco-behler-4b4b8a171/), head of the JVM ecosystem at JetBrains, says the plugin has basically failed to find its audience. “Kotlin Notebook didn’t reach the level of adoption we expected,” Behler writes.

He also points to a broader change in how developers work, with AI a prime protagonist.

“AI tools have changed how developers explore code, prototype, and iterate, and many of the workflows that originally drove notebook adoption have evolved along with that shift,” he says.

> “AI tools have changed how developers explore code, prototype, and iterate.”

Microsoft made a near-identical move in February, when it [quietly announced](https://github.com/dotnet/interactive/issues/4163) it was deprecating Polyglot Notebooks — its VS Code extension for running C# and other languages inside the Jupyter format — with barely a month’s notice. The [extension had drawn more than](https://www.devclass.com/databases/2026/02/14/microsoft-deprecates-polyglot-notebooks-developers-react/4091167) 1.8 million installs and a four-star rating before Microsoft pulled the plug, pointing users toward “the next generation of AI-powered coding experiences” as the path forward.

## The Python problem

While the AI displacement thread may hold some truth, there could be a simpler explanation underneath it: notebooks are a Python-native habit, and always have been.

The [Jupyter](https://jupyter.org/) format — the open standard underpinning both Kotlin Notebook and Polyglot Notebooks — [originated in the Python and data science world](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/). Its kernel protocol, an open spec that defines how a notebook frontend communicates with a language runtime, is language-agnostic by design, making it fairly straightforward for JetBrains and Microsoft to build on top of it. But the working culture that makes notebooks genuinely useful — exploratory analysis, inline visualization, sharing results as a living document — belongs substantively to data scientists working in Python, not to application developers working in Kotlin or C#.

JetBrains was trying to bring that culture into IntelliJ’s Kotlin developer base. Microsoft was attempting the same for its C# and .NET community. Neither community adopted it the way Python developers adopt Jupyter, and both companies have seemingly used AI as the exit ramp.

## Jupyter’s thunder: stolen by no one

Jupyter Notebook usage, it seems, remains in rude health. According to GitHub’s [most recent Octoverse report](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/), the number of repositories containing Jupyter Notebooks grew 75% year-over-year, from 1.4 million to 2.42 million. A further data point: Jupyter Notebook usage nearly doubled specifically within AI-tagged repositories, with over 400,000 such projects active — evidence of its role as the go-to environment for prototyping and running AI experiments.

Google [Colab](https://en.wikipedia.org/wiki/Google_Colab), for its part, tells a different story entirely. Built from the ground up as a Python-first environment for data scientists and ML researchers since 2017, Colab never had the audience problem that sank Kotlin Notebook and Polyglot Notebooks — it was always serving the community for whom notebooks are a daily tool. Google has been adding AI features to Colab [for several years](https://blog.google/innovation-and-ai/technology/developers-tools/google-colab-ai-coding-features/), with a full “[AI-first](https://developers.googleblog.com/new-ai-first-google-colab-now-available-to-everyone/)” version rolled out in June 2025. It was basically all about baking agentic capabilities directly into the notebook, rather than treating AI as a reason to abandon it.

For JetBrains, the Kotlin Notebook sunset is one piece of a larger recalibration. As *The New Stack* has [previously written](https://thenewstack.io/ide-vs-desktop-agent/), the traditional IDE is under real pressure from AI-native coding tools that increasingly handle tasks through conversation and agent orchestration rather than menus and keystrokes. In early June, [JetBrains open-sourced Mellum2](https://thenewstack.io/jetbrains-mellum2-open-source-coding-model/), a 12-billion-parameter coding model built for on-premises deployment — a confident move in the current AI coding tools market. Killing a niche plugin and open-sourcing a frontier model in the same month says something about where JetBrains thinks its future lies — and it isn’t persuading Kotlin developers to work like data scientists.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)