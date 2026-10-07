Technical documentation is increasingly being read by AI agents, creating a new set of demands around how that information is published and structured. [Docsy](https://www.cncf.io/blog/2025/01/07/docsy-2024-review-adoptions-and-enhancements/), the Google-created documentation project used by major cloud native projects, is now moving to the Linux Foundation as it adds features aimed specifically at that machine audience.

[Erin McKean](https://www.linkedin.com/in/emckean/), senior developer relations engineer at Google and a member of the Docsy steering committee, announced the move in a keynote on Wednesday at the Linux Foundation’s [Open Source Summit Europe](https://events.linuxfoundation.org/open-source-summit-europe/) in Prague.

First [announced by Google in 2019](https://opensource.googleblog.com/2019/07/announcing-docsy-website-theme-for.html), Docsy is an open source theme for the [Hugo static site generator](https://thenewstack.io/tutorial-use-hugo-to-generate-a-static-website/) designed for technical documentation. It can be used for documentation generally, including proprietary projects, though it has become particularly widely used in the open source sphere. By the [end of 2024](https://www.cncf.io/blog/2025/01/07/docsy-2024-review-adoptions-and-enhancements/), some 2,200 projects were using Docsy, with adopters across the Cloud Native Computing Foundation (CNCF) including Kubernetes, OpenTelemetry, gRPC and Jaeger.

That existing footprint inside Linux Foundation communities is part of the rationale behind the move. Speaking to *The New Stack* after the keynote, McKean says bringing Docsy into the foundation puts it closer to many of the projects already using it.

“Open source projects work best when they are close to the users,” she says.

> “Open source projects work best when they are close to the users.”

## AI needs good documentation, too

In her keynote, McKean focused heavily on the arrival of AI as a new consumer of technical documentation. Some technical writers, she acknowledges, are “a little bit salty” that it took AI to bring more resources to documentation. But the important part, she argues, is whether the information ultimately reaches and helps developers, regardless of the route it takes.

> “When we’re making technical documentation, it really doesn’t matter how the information becomes useful to humans, as long as it does it.”

“When we’re making technical documentation, it really doesn’t matter how the information becomes useful to humans, as long as it does it,” McKean says. “If someone told me that there was evidence that said opera is the best way to reach your project users, I’d be writing operas.”

Docsy has already begun adapting its output for AI tools. Since [version 0.15.0](https://www.docsy.dev/blog/2026/0.15.0/) in May, it can generate a Markdown copy of each page alongside the regular HTML, as well as an llms.txt file that gives AI tools an index of a site’s content. Both features are opt-in and remain experimental.

The broader idea is to give AI systems a more direct route to the information projects want them to use.

> “You can redirect your LLMs and agents to the text that tells them how to use the project.”

“You can redirect your LLMs and agents to the text that tells them how to use the project,” McKean says.

Docsy has continued adding features around that basic concept. Version [0.16.0](https://www.docsy.dev/blog/2026/0.16.0/), released in July, included an upgrade guide written so that it could also be followed by an AI assistant, with conditions, steps and checks built into the instructions. And with version [0.17.0](https://www.docsy.dev/blog/2026/0.17.0/), released in August, Docsy went further on helping agents consume the documentation itself. Sites that enable llms.txt now automatically include a hidden directive at the top of each page pointing visiting agents toward the site’s llms.txt index. That feature is also experimental.

## Scoring docs for agents

Next on the roadmap are “AF,” or agent-friendly, “documentation scores,” designed to give maintainers a way to assess how easily AI tools can find, navigate and consume their documentation. McKean says that should give projects a benchmark to work toward.

“You won’t have to guess,” she says. “You can measure how agent friendly your docs are.”

There is a more conventional payoff to better documentation too: fewer routine questions landing on maintainers. McKean says good docs can answer those questions before someone has to step in manually.

“When you have good docs, it reduces the number of questions that can be easily answered by documentation, reducing the burden on maintainers,” she says.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)