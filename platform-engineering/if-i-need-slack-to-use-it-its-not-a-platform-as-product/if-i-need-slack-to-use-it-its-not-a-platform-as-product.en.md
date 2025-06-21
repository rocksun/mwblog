I still remember the first time I was told: Just use the internal platform — it’s all self-service now.

So I tried. I opened the documentation. Scrolled. Scrolled some more. Got distracted. Pinged the Slack channel. By the time I had managed to spin up what I needed, I had read three wiki pages, guessed my way through some Terraform variables, and reverse-engineered a naming convention that felt like a puzzle from another team’s backlog.

I wasn’t onboarding — I was decoding.

That’s when I realized something wasn’t right. If I need a Slack thread to figure out your so-called platform, is it even a platform? Or is it a half-baked product pretending to be one?

Let’s zoom out for a moment. Industry-wide, internal platforms are all the rage. Yet I can recall only one from my experience that genuinely felt like a cool breeze. Ironically, it wasn’t built in-house — we had outsourced the heavy lifting to a third party. That came with a cost, and not every organization has the appetite or budget for that kind of investment.

## Same Friction, New Tools

At KubeCon + CloudNativeCon Europe in London this April, the same developer concerns echoed across hallway conversations, lightning talks and informal meetups.

Poor documentation remains a major roadblock. Distributed systems feel overwhelming. Feedback loops are slow and painful. Tool sprawl fragments the workflow. Developers are stuck between unclear platform ownership and brittle CI/CD setups.

Observability is patchy. Local setups rarely match production. And most teams are still debating who owns what.

If this feels familiar, you’re not alone. [Platform engineering](https://thenewstack.io/platform-engineering/) promises to fix these challenges. But in practice, it often introduces new layers of complexity — and more friction for the developers and their workflow.

## Platform First, Product Later

As a developer, every time I hear the term “Platform as a Product,” I pause. What does it really mean — and does it matter to roles like mine?

“Platform” has become a catch-all label.

A script wrapped in a UI? *Platform.*

A Jenkins pipeline with a dropdown menu? *Platform.*

A shared repo of automation templates? *That too.*

But as developers, we know better. A real platform isn’t a tool. It’s an experience — one that helps us move faster, build better and reduce friction, not stack it.

The problem is that every team defines it differently. I’ve explored this in-depth [in my book on platforms and related topics](https://mybook.to/shwetavohra). In our industry, some refer to it as a portal, others as a product — and for developers, it often becomes something else entirely. This leads to persistent confusion and multiple hops just to get intended work done, leaving teams stuck, frustrated  and unable to move forward efficiently.

In my experience working across teams, domains and delivery environments, I’ve seen a consistent pattern of developer friction — particularly in today’s fast-paced, cloud native world. It’s nothing new, but it’s been accelerated by the burden of handling infra, ops and [everything in between](https://thenewstack.io/shifting-left-is-now-mainstream-for-developers-or-is-it/). We’ve made the developer responsible for it all.

## The 4 Recurring Challenges Developers Face

It is easy to blame evolving technology for developer frustrations — but tools alone aren’t the full story. Many of the same issues keep resurfacing across teams and organizations, regardless of stack or scale.

Based on my experience, here are four recurring challenges that go beyond the technical layer. These aren’t exhaustive — so feel free to share your own in the comments. Let’s take a closer look:

### 1. Context Switching Is the Enemy of Flow

One of the most common challenges developers face is managing time and focus — keeping aside all of life’s digital distractions to make it simple. Between writing code, reviewing pull requests, fixing bugs and attending meetings, most developers are stretched thin.

Deep work becomes rare. [Context switching becomes the norm.](https://thenewstack.io/the-interrupt-tax-why-developer-productivity-is-measured-in-silences/) Productivity takes a hit.

### 2. Too Many Tools, too Little Time

Then there’s the pace of technological change. The ecosystem moves fast. New frameworks, [tools](https://thenewstack.io/developers-unhappy-with-tool-sprawl-lagging-data-long-waits/), best practices — they emerge almost weekly. Even the most seasoned developers struggle to stay current without putting in serious effort beyond working hours.

For Instance: Kubernetes offers immense flexibility but brings with it a steep learning curve. YAML sprawl, complex cluster configurations and inconsistent environments become barriers rather than enablers.

### 3. Interoperability Is a Mess

Teams are stitching together pipelines and platforms using a mix of services that were never meant to work together. Fragile systems emerge. Debugging gets harder. Everyone’s waiting on someone else’s platform bug fix to move.

### 4. Security Feels Like a Silo

Security and compliance requirements continue to grow, but the tooling rarely meets developers where they are. Security becomes a reactive checklist, not an integrated guardrail. And it’s the developer who gets caught in the middle.

These are not isolated complaints. They’re recurring themes that impact morale, velocity, and quality — across teams, tools and time zones.

## When Tools Pose as Platforms

Take Terraform. In theory, it enables infrastructure automation. In practice, when every service needs its own template, when no abstraction layer exists, and when standards like encryption and tagging are left to tribal knowledge, it quickly becomes another burden.

Internal portals, marketed as self-service, are often just forms sitting on top of brittle, opaque processes. You fill them out and wait. If something breaks? You’re back to Slack.

And APIs? Some claim that their platform is API-first — until you try to use one and end up needing four separate Slack pings just to make sense of it.

This isn’t developer enablement. It’s entropy wrapped in a friendly interface.

## What a Platform Should Feel Like

We’re not asking for perfection, product or platform. We’re asking for flow.

A good platform should meet developers where they already work: the CLI, the codebase or the API layer. It should offer configuration flexibility through toggles, not templates. Secure defaults — like encryption and logging — should be built-in, not optional.

> If your platform team never talks to its users, you’re not building a product — you’re shipping a guessing game.

Provisioning a full-stack environment shouldn’t require tribal knowledge or multiple Jira tickets. Ideally, the platform should ask a few intelligent questions and handle the rest — like an agent. It should run compliance and vulnerability checks in the background. Pre-load the required libraries. Keep them up to date quietly.

Let developers build — not babysit infrastructure.

## Platform as a Product? Sounds Nice. Prove It.

“Platform as a Product” sounds compelling in slides and charters. But in practice, most internal workflows, self-serves, portals — unless built with intention and user input — fall short.

Here’s the part many overlook: if your platform team never talks to its users, you’re not building a product — you’re shipping a guessing game.

Want developers to adopt your platform? Involve them. Co-design with them. Measure onboarding friction. Treat feedback like bugs. Track adoption and impact like uptime. And most of all, stop assuming that “shift left” is the same as “listen left.”

> Every workaround is a symptom that your platform doesn’t work.

A real platform disappears into the developer’s (or user’s) flow. A bad one interrupts it — daily.

Thinking like a product forces an important question: how much standardization is just enough for developers in your organization? Where are the defined users? The product roadmap? The metrics that tie platform adoption to business impact? The support model? The feedback loops?

If your internal platform doesn’t have these, it’s not a product. And it may not even be a platform.

## Beyond Branded Tools

As a developer, I don’t need another tool with a fancy name. I need a system that removes blockers — quietly. One that doesn’t require a ticket queue, a Slack ping or a multi-tab investigation just to get started.

If you’re calling your internal platform a product, prove it — in how it’s designed, supported and experienced. And if you’re not ready to do that, maybe stop calling it one.

Because the next time I hit a wall with your so-called platform, I’m not raising a ticket. I’m writing a workaround. And every workaround is a symptom that your platform doesn’t work.

But workarounds don’t scale. Platforms with product culture, when built right, do.

## Let’s Go Deeper

We’ve only scratched the surface here. In the coming weeks, we’ll dive deeper into what it really takes to move beyond broken workflows and reactive engineering — offering not just critique, but solution patterns, field notes, and hard-won lessons from platform journeys that worked (and those that didn’t).

> A real platform disappears into the developer’s (or user’s) flow. A bad one interrupts it — daily.

We’ll explore how to reduce cognitive load, accelerate feedback and [bring product thinking into the internal developer experience](https://thenewstack.io/to-fix-platform-engineering-build-what-users-actually-want/).

And we’ll also challenge the notion that [platform engineering](https://thenewstack.io/ebooks/platform-engineering/platform-engineering-what-you-need-to-know-now/) is just glue work. Because real glue — the kind that holds teams, tools and trust together — doesn’t live in documentation. It lives in thoughtful design, clear ownership and the daily rituals that help developers build momentum.

Let’s build platforms that earn the title.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/05/18c0922f-shweta-vohra-2-600x600.jpg)

Shweta Vohra is an architect, author, and inventor with over two decades of experience in the software industry. She has collaborated with more than 50 customers across more than 10 domains, leading international teams and specializing in digital transformation, enterprise...

Read more from Shweta Vohra](https://thenewstack.io/author/shweta-vohra/)