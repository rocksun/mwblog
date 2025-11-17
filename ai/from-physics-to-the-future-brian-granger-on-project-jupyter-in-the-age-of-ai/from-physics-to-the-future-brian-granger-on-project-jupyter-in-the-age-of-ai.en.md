What if you could rewrite a beloved open source, battle-tested server from scratch, complete with a new test suite, in just 30 minutes? For [Brian Granger](https://www.linkedin.com/in/brian-granger-b9998662/), co-creator of Project Jupyter and senior principal technologist at [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention), this is no longer a thought experiment but a reality that’s fundamentally changing how we think about open source sustainability.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

In this On the Road episode of The New Stack Makers, Granger sat down with TNS Editor in Chief [Heather Joslyn](https://thenewstack.io/author/hjoslyn/) at JupyterCon in San Diego to discuss Jupyter’s origins, the project’s ACM Software System Award and how AI is transforming what’s possible for large open source projects.

## The Physics of Flexible Architecture

Granger first encountered computational notebooks while working on a Ph.D. at the University of Colorado, where he also became friends with fellow grad student and [iPython interactive shell](https://ipython.org/ipython-doc/3/interactive/index.html) creator [Fernando Pérez](https://www.linkedin.com/in/fperezorg/).

“We both grew up in physics using Mathematica and, when [Python](https://thenewstack.io/what-is-python/) came on the scene, we really wanted that same notebook experience, only in Python,” Granger recalled.

A few years and one late-night conversation later, Granger and Pérez came up with a vision to build iPython Notebook, a web-based notebook in Python form that eventually evolved into Jupyter Notebooks.

Their shared physics training shaped Jupyter’s architecture. “Newton’s equations are very modular and extensible. You can model pretty much any classical system in the universe using Newton’s laws. The same is true of quantum mechanics or special general relativity,” Granger said. “We wanted a very small number of building blocks that solved a large number of problems. And I think we got it right.”

That modular, flexible, extensible building blocks — the notebook format, the kernel message protocol and higher-level APIs for Jupyter Server and JupyterLab extensions — have proven remarkably durable, even as the [ecosystem around them](https://thenewstack.io/jupyter-ai-v3-could-it-generate-an-ecosystem-of-ai-personas) has [evolved significantly](https://thenewstack.io/deepnote-a-successor-to-jupyter-notebook-goes-open-source/).

## Rewriting the Rules on Technical Debt

Jupyter was built in a world where data science, AI and machine learning (ML) were just starting to emerge — but that may just be its secret to longevity.

“Jupyter wasn’t designed for software engineering or building applications. It’s for solving hard problems that require human reasoning and thinking through really complex, messy scenarios,” Granger said. “For the era we’re in now, where all of us — literally everyone — is trying to figure out, ‘What do we do with AI?,’ that original use case only gets stronger.”

The team is using AI to build Jupyter now, leading to “even more fun and a significant change in velocity.”

Granger described a recent experiment rewriting Jupyter Servers from Python to Go with the help of an AI coding agent.

“It took about a half an hour until I had a completely new implementation that was following this open API specification and had a test suite with 70% coverage,” he said. “Previously, thinking about rewriting Jupyter Server from scratch, we would have dismissed it immediately as absolute insanity. We have way more important things to do, it’s battle-tested, don’t touch it. But now, all of a sudden, it’s an option.”

This velocity shift is fundamentally changing how the team approaches [technical debt](https://thenewstack.io/technical-debt-continues-to-mount-heres-how-to-solve-it/), sunk costs and prioritization, Granger said. “In terms of technical sustainability for large open source projects like Jupyter, AI is going to play a really important role.”

## Recognition Brings Responsibility

In 2017, Granger won an Association for Computing Machinery Software System Award — placing Jupyter in the same company as Unix, Java and the World Wide Web. It came with a sobering reality check.

“Part of this is an acknowledgement that Project Jupyter, while many of us enjoy it like we would a hobby, is no longer a hobby,” Granger noted. “We have entire industries in academic research and education depending on Jupyter on a daily basis.”

That recognition brings questions about sustainability and competition that laser-hone his focus on the community’s future. “If there’s anything that keeps us up at night, it’s that Jupyter dies a long, slow death of people just starting to use other things,” he said. “We’re highly motivated to understand what users need and serve them and build things that they love.”

Check out the full episode to hear more Jupyter origin lore, why governance challenges caught the team off guard and how the project is navigating the AI era while staying true to its mission of enabling thinking, collaboration and knowledge sharing.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/05/5bc05c60-cropped-bb29d761-michelle_gienow.jpeg)

Michelle Gienow is a former journalist turned software developer. She draws from both professions to write about in-depth technical topics ranging from K8s to Kotlin. Michelle is co-author of "Cloud Native Transformation: Practical Patterns for Innovation" from O'Reilly Media and...

Read more from Michelle Gienow](https://thenewstack.io/author/michelle_gienow/)