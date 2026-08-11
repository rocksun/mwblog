Cloudflare launched its CloudflareOS open-source AI workspace platform this week, promising every employee a secure workspace equipped with AI tools and access to internal company systems.

Positioned significantly beyond the notion of legacy [virtual desktop infrastructure](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-virtual-desktop-infrastructure-vdi) (VDI) services, which delivered the same fixed applications through a remote screen — and even past the dynamic application delivery, [app masking](https://getnerdio.com/blog/fslogix-application-masking/) and streaming of modern VDI iterations — this is an essentially more dynamic way of working with internal company tools, documents and systems.

Cloudflare’s [CloudflareOS](https://blog.cloudflare.com/cloudflare-os/) makes its apps and services accessible through [secure connection points](https://thenewstack.io/how-devsecops-teams-should-approach-api-security/) that verify every user and every agentic request or connection point before access is granted.

## In AI, every new work session starts from zero

The technology proposition here is built on the fundamental truth that the typical enterprise AI tool knows a great deal about the world, but almost nothing about how a specific company operates, the shape of its internal systems, approval processes, or the ways teams actually get work done.

That means every new work session starts from zero, with employees re-explaining context the AI should already know. But how can new business context-aware agentic access freedoms be granted securely?

[Rita Koslov](https://www.linkedin.com/in/ritakozlov/), VP for developers & AI at Cloudflare, tells *The New Stack* that powering up modern agent use cases means “data is often leaving controlled systems en masse” for the first time.

“It used to be the case that, for example, people asked analytics questions in [the data warehouse](https://thenewstack.io/data-warehouses-are-terrible-application-backends/) where the organization had control,” Koslov says. “Now, employees are asking for API keys for their own tools, agents, etc. This creates a new class of security problems that Cloudflare OS helps to solve.”

## Capability-based access beats handing agents raw API keys

[Cloudflare](https://www.cloudflare.com/) has built what we can call capability-based access, which the company promises beats handing agents raw API keys outright.

“API keys give agents broad access to systems; a capability-access-based approach lets us grant one specific resource, then record exactly what the agent observed, and verify that anyone who sees its work is also allowed to access the source,” underlines Koslov.

Cloudflare OS enables an agent to create documents, slides, spreadsheets, workflows, other agents – or entirely new full-stack applications – all tailored to an employee’s work. What it creates can remain connected to live data sources, be modified and shared safely, and be used directly by both people and agents.

> “API keys give agents broad access to systems; a capability-access-based approach lets us grant one specific resource, record exactly what the agent observed, and verify that anyone who sees its work is also allowed to access the source.”

In terms of how developers and systems operations professionals should react to this offering, Koslov suggests that “the difficult problem is not generating an app” today. Instead, the real challenge is safely running thousands (or millions) of dynamically generated apps, each with persisted state and controlled access.

“Cloudflare OS uses [Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/), which provide lightweight isolated runtimes to load each app’s code on demand, and [Durable Objects Facets](https://developers.cloudflare.com/dynamic-workers/usage/durable-object-facets/) to give it isolated SQLite storage under the platform’s supervision. Outbound networking is disabled by default, and Gatekeepers expose only the resources explicitly granted by the users,” Koslov says. “Dynamic Workers and Durable Objects Facets were invented because doing this was previously not possible.”

For completeness here – and once again a Cloudflare original technology service – [a Gatekeeper is a service-specific Worker](https://github.com/cloudflare/cloudflare-os) that sits between Cloudflare OS and an external service to interpret and understand the service’s API, its resources, and the operations that can be performed on them.

## What happens when it all goes wrong

Koslov confirms that she knows how badly things can skew out of control in unmanaged environments.

“We know this from our own experience talking to other companies on all accounts. They’ve shared instances of internal data copied into AI tools that IT did not know were in use, AI keys embedded into agent-built applications, and even data being shared internally to people who ordinarily wouldn’t have access (or even publicly),” she adds.

Building a tailored alternative is no small project; a platform with proper security and real integration into internal systems can take years to develop and cost millions to maintain. In the meantime, employees find workarounds, IT loses track of which AI tools are running and who is using them, and costs pile up, often with little to show for it.

CloudflareOS starts from a different premise: a company captures its knowledge, processes, and ways of working once in a form AI can actually execute, and that knowledge travels with every employee’s workspace from day one.

## How do we measure business ‘context’?

“Captured business ‘context’ in this case can include company terminology, policies, operating procedures, product documentation, technical standards, sales processes, templates, and established ways of performing recurring work,” confirms Koslov.

CloudflareOS started as the platform Cloudflare built to run its own workforce. Thousands of Cloudflare employees across every team use it daily to perform research, create documents connected to live data, automate repetitive tasks, and build working apps for their day-to-day jobs.

That same platform is now available to any organization as open-source software. Because it’s open source and runs in a company’s own Cloudflare account, organizations own what they build on it.

The platform itself works on any AI model and controls cost. Through Cloudflare AI Gateway, organizations can use any AI model provider, so they’re not locked into one vendor. Administrators see exactly what’s being spent, broken down by person, team, or app. They can set spending budgets, rate limits, or route routine tasks to smaller, more affordable models where a top-tier model isn’t needed.

## Pricing platforms by the token is the wrong meter entirely

Cautiously upbeat about the wider story playing out here, enterprise AI architect and founder of [Besk Tech](https://besk.tech/), [Vladimir Beskorovainyi](https://www.linkedin.com/in/vladimirbesk/), tells *The New Stack* that, traditionally, the industry is pricing these platforms by the token, “and that is the wrong meter entirely” in his view.

“In this example with Cloudflare OS, what a company actually buys here is the obligation to write down how an AI-powered business process really works, and then keep that description true as the business shifts underneath it,” Beskorovainyi says. “The model is the commodity part. What costs real money is the curated context, and nobody budgets for the fact that it starts decaying the day it is written, which is exactly what decides whether any of this survives contact with production.”

> “Cost broken down by person, team and app is the first time I have seen a vendor treat spend as an engineering signal rather than an invoice, and sending routine work to a smaller model is the obvious next step that most enterprises still fail to take.

Beskorovainyi insists that the organizations that win in this game will “not necessarily be the ones running the best model”; they will be the ones that could “already answer in writing what their own approval process is”, way before an agent ever asked.

“Cost broken down by person, team and app is the first time I have seen a vendor treat spend as an engineering signal rather than an invoice, and sending routine work to a smaller model is the obvious next step that most enterprises still fail to take,” advises Beskorovainyi.

## Owning your own context is not the same as your context being any good

He clarifies his point and explains that the qualification here is that “owning your own context is not the same thing as your context being any good”, and so open source tooling and community connections plus an organization’s own account settle who holds the context file.

“Neither tells us whether what is recorded and logged in the context file is still true this quarter. That work stays with the customer permanently, and it is where I expect most of these deployments to come apart, not in anything Cloudflare has built,” Beskorovainyi adds.

[Matthew Prince](https://www.linkedin.com/in/mprince/), co-founder and CEO of Cloudflare has said that his team built Cloudflare OS, “because nothing else did what we needed”, and so now, any company can start from where it took the organization’s internal software engineering function years to get to.

The apparent appeal here must come down to the dynamic nature of Cloudflare OS and its ability to work with and apply AI tools at a custom-engineered business context-aware level with zero trust by default. The platform can turn any output into a working app with its own isolated database, real-time capabilities, and access controls – once agan, that’s not legacy virtual desktop is it?

## No developer required (yet)

The bottom line from Cloudflare is that employees can use any app on Cloudflare OS  directly, or adapt it for their own needs so that it’s a case of “no developer required”, or at least until the next integration task needs to be shouldered, or the big thing comes along, or both.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)