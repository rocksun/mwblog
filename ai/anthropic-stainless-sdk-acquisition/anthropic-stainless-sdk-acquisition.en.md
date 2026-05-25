Earlier this week, Anthropic acquired Stainless, the New York startup whose software generated SDKs for major AI companies, including Anthropic, OpenAI, and Google, as well as infrastructure firms like Cloudflare.

The headline reads as a routine developer-tools deal. But the structural reality is sharper: A company that quietly sat beneath a large slice of the industry’s API layer now belongs to one of the labs competing on that layer.

To understand why this matters, think of the AI industry as a city and SDKs as the driveways connecting buildings to the street. Every lab ships an API, but developers do not touch raw HTTP endpoints. They reach for a TypeScript or Python library that wraps the API in something native and pleasant. Stainless built those driveways for a large share of the city. When one resident buys the driveway-paving company and announces it will stop paving for everyone else, the city’s map changes.

## What Stainless actually did

Stainless turned an API specification into production SDKs. Feed it an OpenAPI spec, and it generates typed, idiomatic client libraries in TypeScript, Python, Go, Java, Kotlin, and more, and keeps them updated as the underlying API changes. It also generated command-line tools and [MCP](https://modelcontextprotocol.io) servers, the connectors that let AI agents reach external APIs through a standard interface.

> Stainless was a factory that took a blueprint and stamped out the same product in a dozen materials, each one finished to look handmade.

The analogy here is straightforward. Stainless was a factory that took a blueprint and stamped out the same product in a dozen materials, each one finished to look handmade. Just as a contract manufacturer lets a hardware company ship a polished product without running its own assembly line, Stainless let an AI lab ship a polished developer experience without staffing a team to hand-write and maintain SDKs in six languages.

That arrangement was invisible and load-bearing. By Stainless’s own [estimate](https://www.stainless.com/blog/stainless-is-joining-anthropic/), roughly a quarter of the world’s professional software developers have used an SDK or visited a docs site it generated. That figure is the company’s claim rather than an independent measurement, but the customer list is public, and it extended well beyond Frontier Labs to companies like Cloudflare, Replicate, and Runway. For most of those teams, the SDK was simply a thing that worked, not a vendor relationship anyone thought about.

## What the deal removes

Anthropic disclosed the acquisition but not the terms. *The Information* [reported](https://techcrunch.com/2026/05/18/anthropic-has-acquired-the-dev-tools-startup-used-by-openai-google-and-cloudflare/) ahead of the announcement that the company was in talks to buy Stainless, backed by Sequoia Capital and Andreessen Horowitz, for more than $300 million. The number matters less than what Anthropic said it would do next.

> The substrate that OpenAI, Google, Cloudflare, and others leaned on is being switched off for everyone except the team that now owns it.

Stainless will wind down all hosted products, including the SDK generator itself. New signups, new projects, and new SDK generation stopped on the day of the announcement. The distinction worth holding onto is between the hosted service and the code. Existing customers retain full rights to the SDKs they’ve already generated, so no one’s current libraries will vanish. What closes is the shared factory, the ongoing ability to regenerate and update SDKs as an API changes. The substrate that OpenAI, Google, Cloudflare, and others leaned on is being switched off for everyone except the team that now owns it.

Consider what that means for a competing lab. An AI company that relied on Stainless for its TypeScript and Python clients now has three options. It can rebuild SDK generation in-house, which means hiring and funding a tooling team that generates no direct revenue. It can migrate to a competing generator and absorb the switching cost. Or it can freeze its SDKs at the last generated version and maintain them by hand, which is the slow erosion every API team dreads. None of these is a crisis. All of them are friction at a layer that most engineering leaders were not watching.

> The strategic weight of the deal is not the Stainless technology landing inside Anthropic. It is the effect on everyone else.

This is the part worth naming clearly. I would argue the strategic weight of the deal is not the Stainless technology landing inside Anthropic. It is the effect on everyone else. Whatever Anthropic’s motive, winding down the hosted generator removes a shared supplier from the market. Anthropic bought a capability, and the same transaction took a shared dependency off the board for rival labs.

## The pattern behind the deal

The Stainless deal is the third move in a sequence, and the sequence is the actual story. In December 2025, [Anthropic acquired Bun](https://thenewstack.io/bun-developers-complaints-anthropic/), the JavaScript runtime that Claude Code ships as a compiled executable. As Bun’s founder put it at the time, if Bun breaks, Claude Code breaks, so Anthropic bought the infrastructure its billion-dollar product depended on. In March 2026, OpenAI [announced](https://thenewstack.io/openai-astral-acquisition/) it would acquire Astral, the startup behind the Python tools uv, Ruff, and ty, and fold the team into Codex.

Three acquisitions, two labs, one direction. Anthropic and OpenAI are the two clearest cases, and each is moving from the model layer down into the developer tooling layer, buying the runtimes, package managers, and SDK generators that sit beneath the software development process. Whether every frontier lab follows is unproven, but the two labs setting the pace for AI coding are both doing it, which is enough to call it a pattern. The frontier labs spent the last two years competing on model benchmarks. The leaders are now competing on who owns the developer’s toolchain.

> The frontier labs spent the last two years competing on model benchmarks. The leaders are now competing on who owns the developer’s toolchain.

Think of it as the difference between selling engines and owning the road network. For years, the labs sold the most powerful engine and let developers bolt it into whatever chassis they liked. Buying Bun, Astral, and Stainless is a bet that the chassis, the fuel system, and the road matter as much as the engine, and that whoever controls them controls where developers can drive.

Model leads are temporary. A lab can hold the top benchmark spot for a quarter and lose it the next. Toolchain position is stickier. Once a developer’s package manager, runtime, and SDKs are wired into a daily workflow, switching costs rise with every project. Owning the tooling converts a fleeting model advantage into a durable distribution advantage.

### Why is this defensive and offensive at once

Buying a critical dependency protects the acquirer’s own product from breakage and roadmap drift. That is the defensive read. The offensive read is that the same purchase can deny the dependency to rivals or put them on a clock. The Stainless deal carries both effects in a single transaction, which is what makes it sharper than the Bun acquisition. Bun stayed open source and broadly available to everyone, so no rival lost access. Stainless is winding down its hosted generator, so they do.

### Why developers should care now

The tools a developer treats as neutral infrastructure are quietly being acquired by owners with competitive interests. A runtime, a linter, or an SDK generator that felt vendor-agnostic in 2025 may sit inside a frontier lab in 2026. That does not make the tools worse. It does mean that the question of who maintains your toolchain and what their incentives are is no longer one you can skip.

The labs are not buying these companies for revenue. They are buying a position in the layer where developer habits form.

The merger of frontier labs and developer-tooling companies follows a recognizable sequence, and each step tightens the link between the model and the workflow around it.

### Partnership

A lab and a tooling company work closely for months before any deal. Anthropic used Bun internally and shaped its roadmap well before the acquisition. Stainless generated every official Anthropic SDK from the earliest days of the Claude API. The partnership phase establishes the dependency that the acquisition later formalizes.

### Acquisition

The lab buys the company outright. The stated reason is always product quality and developer experience. The unstated reason is control, both over the lab’s own roadmap and over a rival’s access. Terms are frequently undisclosed, keeping the strategic weight of the deal out of the headlines.

### Consolidation

The acquired product is absorbed into the lab’s platform. Hosted services for outside customers wind down as Stainless winds down now, or the product stays open, but its roadmap bends toward the acquirer’s needs, as critics worry could happen with Bun. Either way, the tooling layer stops being neutral ground.

The endpoint of this sequence is an industry in which the major model providers also own major parts of the developer toolchain. That is a different competitive map than the one drawn when the contest was purely about model capability.

## What the choice looks like for an API company

Any company that ships a public API and once relied on a shared SDK generator now faces a real decision. Think of it the way you would weigh a managed service against self-hosting after the managed service announces it is shutting down.

| Scenario | Likely path | Rationale |
| --- | --- | --- |
| Small API team, few languages | Hand-maintain existing SDKs | Generated SDKs still owned; manual upkeep is tolerable at small scope |
| Large API surface, many languages | Migrate to a competing generator | Manual maintenance does not scale; switching cost is the lesser pain |
| Reassess the connector tooling strategy | Build SDK generation in-house | Reduces reliance on a rival-owned layer; funds a non-revenue team |
| Agent-heavy product needing MCP servers | Reassess connector tooling strategy | MCP server generation was part of the same wound-down stack |

In practice, most teams will combine these paths, hand-maintaining some clients while migrating others, and the largest players will treat in-house tooling as a strategic line item rather than a cost to avoid. The deal does not break anyone’s product. It moves a quiet operational task back onto roadmaps that had happily forgotten about it.

## What’s next

For developers tracking the tool landscape, the pattern is now visible enough to plan around. The frontier labs are no longer only model companies. They are becoming developer platform companies, and they are getting there by acquisition. Bun gave Anthropic a runtime. Astral gave OpenAI a Python toolchain. Stainless gives Anthropic the SDK and MCP generation layer, and because the hosted generator is closing, rival labs lose a shared supplier in the same move.

The open question is where the consolidation stops, and the answer is not uniform. Some key layers now sit inside model labs, but with different openness models. Bun remains open source and MIT licensed. Astral’s tools are expected to stay open source. Stainless is the outlier, because its hosted generator is shutting down rather than continuing in the open.

The IDE, the linter, the build system, and the agent harness are still partly independent, and each is a plausible next target. Anthropic crossed a reported $30 billion annualized revenue run rate in early April, and OpenAI was reported at more than $25 billion annualized around the same period, which means both have the balance sheet to keep buying.

The next acquisition in this sequence will tell developers how much of their toolchain will belong to the companies whose models they call.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)