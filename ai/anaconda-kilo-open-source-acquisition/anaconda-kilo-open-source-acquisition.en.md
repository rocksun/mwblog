[Anaconda](https://www.anaconda.com/), a company that provides governed, open-source packages and environments for enterprises, has acquired popular open-source coding agent [Kilo](https://kilo.ai/).

The deal lands at a moment when companies across the industrial spectrum have grown wary of platforms locking them into a single AI provider. In the past 10 days alone we’ve seen [Palantir’s Alex Karp and Mistral’s Arthur Mensch](https://thenewstack.io/karp-mensch-ai-lockin/) warn that closed model providers gain outsized leverage over enterprise data and workflows, while Microsoft’s Satya Nadella [argued](https://thenewstack.io/nadella-reverse-information-paradox/) somethign similar.

And it’s against that backdrop that Anaconda is now taking Kilo under its wing.

Founded out of Austin, Texas in 2012, Anaconda is the company behind the widely used eponymous Python distribution and package manager — a tool that, over more than a decade, helped data scientists and enterprises manage Python environments without dependency headaches. It built its business on convincing companies to trust open-source tooling inside their walls, and in May 2025, [it pushed that ethos into AI](https://thenewstack.io/pythons-open-source-dna-powers-anacondas-new-ai-platform/), launching a platform aimed at giving enterprises the same governed, secure approach to models and AI development.

That launch also coincided with a [$150 million-plus funding round](https://www.anaconda.com/press/anaconda-raises-150m-series-c-funding-ai-enterprise), valuing the company at around $1.5 billion.

> “Right now, most enterprises pick one of two false options: lock down to a single tool and model provider, or let developers use whatever they want with zero visibility. Neither is a real strategy.”

[David DeSanto](https://www.linkedin.com/in/ddesanto/), who [joined Anaconda as CEO](https://www.anaconda.com/press/anaconda-names-new-chief-executive-officer) in October 2025 after six years as GitLab’s chief product officer, tells *The New Stack* that enterprises are ultimately stuck between two extremes — total lockdown, or a total free-for-all.

“Right now, most enterprises pick one of two false options: lock down to a single tool and model provider, or let developers use whatever they want with zero visibility,” DeSanto says. “Neither is a real strategy.”

## Every kilo counts

Kilo, for its part, launched in [March 2025](https://blog.kilo.ai/p/kilo-code-speedrunning-open-source-coding-ai), founded by GitLab co-founder and ex-CEO [Sid Sijbrandij](https://www.linkedin.com/in/sijbrandij/), with Jan Paul Posma as founding CEO. Posma stepped back for personal reasons in September, handing the role to [Scott Breitenother](https://www.linkedin.com/in/scottbreitenother/), who leads the company today. Kilo’s [core sell is neutrality](https://www.forkable.io/p/kilo-an-open-source-coding-agent): rather than tying developers to one AI lab’s models, Kilo lets them plug in whichever provider they want — OpenAI, Anthropic, Google, Mistral, self-hosted models — and switch freely as pricing or performance shifts. The project has built a sizeable presence on GitHub, with more than [26,000 stars and 3,000 forks](https://github.com/kilo-org/kilocode).

Kilo isn’t alone with this pitch. Tools like [OpenCode, Cline, and Aider](https://thenewstack.io/open-source-coding-agents-like-opencode-cline-and-aider-are-solving-a-huge-headache-for-developers/) have found traction by sitting a layer above the models themselves, giving developers a way to dodge unpredictable token bills and vendor lock-in. It’s worth noting that Kilo itself is a fork of [Roo Code](https://github.com/RooCodeInc/Roo-Code), an open source AI coding agent for VS Code. When [Roo Code sunset its IDE extension in favor of a cloud-only agent](https://thenewstack.io/roo-code-cloud-ides-ai-coding/), it sent a wave of its user base looking for alternatives, with Kilo positioning itself as a landing spot. And the appetite cuts both ways: in June, Cursor [acquired Continue](https://thenewstack.io/cursor-acquires-continue-coding/), another open source, model-agnostic assistant, folding one of the category’s earlier standard-bearers into a closed, commercial IDE.

Collectively, this illustrates how contested this layer of the stack has become. And Anaconda is jostling for its seat at the table.

## The trillion-token problem

Kilo’s numbers go some way toward explaining why Anaconda wanted it: more than 3 million developers routing close to 10 trillion tokens a month through the platform, across 500-plus models from over 60 providers.

> “Scale isn’t the problem here — governing it is.”

For DeSanto, that volume is proof that developers want the freedom to pick their own models. However, that proof comes with a governance gap that companies are eager to close.

“Scale isn’t the problem here — governing it is,” DeSanto explains. “Enterprise AI spend is growing faster than anyone’s ability to account for it, piling up invisibly across dozens of tools, work accounts, and personal accounts.”

DeSanto points to what’s become known as “[tokenmaxxing](https://thenewstack.io/lanai-token-tuner-tokenmaxxing/)” — treating AI token usage as a proxy for productivity, without any real link back to what that usage is achieving. Left unchecked, DeSanto suggests, that habit leaves companies flying blind: burning through budget with no way to tell what’s working, where the exposure sits, or whether any of it is paying off.

“Most are also entirely dependent on a single model provider, a bet no enterprise would make on anything else this critical to its business,” DeSanto adds.

> “Most are […] entirely dependent on a single model provider, a bet no enterprise would make on anything else this critical to its business.”

## What comes next for Kilo

Looking to the future, plans are afoot to fold Kilo into Anaconda’s existing AI workspaces, while keeping the developer experience that made Kilo popular intact.

Developers will keep working in VS Code, JetBrains, and the CLI as before, but with default access to Anaconda’s vetted packages, governed models, and AI orchestration layered in behind them. Over the next 12 months, that integration is set to deepen further, connecting Kilo to Anaconda’s orchestration and governance tools so that a project can move from a developer writing code to that code running in production without switching platforms, with the same organizational policies applying at every stage.

“Our vision is a single, unified platform where builders don’t have to choose between speed and governance,” DeSanto says.

> “Enterprises don’t want to be locked into a single model provider, and developers certainly don’t.”

DeSanto calls Kilo’s open-source, no-lock-in model “fundamental” to Anaconda’s strategy going forward, and as part of the deal, Anaconda takes over stewardship of Kilo’s GitHub organization and developer community.

“Enterprises don’t want to be locked into a single model provider, and developers certainly don’t,” he says. “We intend to continue supporting Kilo as an open-source project while investing in its integration with the Anaconda Platform.”

Kilo isn’t the only open source piece Anaconda has been assembling. Back in April, [it acquired Outerbounds](https://thenewstack.io/anaconda-ai-outerbounds-python-metaflow/), the company behind Metaflow, an orchestration framework that originated inside Netflix. Where Kilo handles the moment code gets written, Outerbounds governs what happens once that code needs to run reliably in production — and the two now sit inside the same Anaconda offering.

“It’s huge that these capabilities exist under one platform, but more importantly, they’re all connected as a seamless, continuous experience,” DeSanto says. “Instead of stitching together disparate AI tools, enterprises now have a continuous path to production. Developers can move quickly while providing the governance, visibility, and control required to operate at scale.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)