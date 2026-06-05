[Vibe coding](https://thenewstack.io/to-vibe-or-not-to-vibe-when-and-where-to-use-vibe-coding/) has made it easier than ever to build applications. Getting those applications into enterprise production is still the hard part. That’s the gap Microsoft is targeting with [Rayfin](https://github.com/microsoft/awesome-rayfin), its new open-source SDK and CLI announced at [Build 2026](https://news.microsoft.com/build-2026/).

Rayfin lets developers and [coding agents](https://thenewstack.io/ai-coding-agents-level-up-from-helpers-to-team-players/) define application backends entirely in code — data models, business logic, access policies — and deploy them directly to [Microsoft Fabric](https://thenewstack.io/microsoft-fabric-goes-all-in-on-real-time-data-intelligence/). The result, Microsoft says, is an application that arrives in production already secured, compliant, and integrated with the enterprise data estate, without the developer having to manually configure infrastructure.

Vibe-coding platform provider [Replit](https://replit.com/) is the exclusive launch partner. [Michele Catasta](https://www.linkedin.com/in/pirroh/), President and Head of AI at Replit, describes the relationship plainly: [Replit Agent](https://docs.replit.com/references/agent/overview) can use Rayfin to define the backend in code, which then deploys to Fabric so application data resides in the customer’s Fabric data estate. Rayfin will be used internally by Replit for production once it is announced, Catasta tells *The New Stack*, with a broader enterprise rollout to follow.

[Amjad Masad](https://www.linkedin.com/in/amjadmasad/), founder and CEO of Replit, puts the pitch in sharper terms in a statement provided by Microsoft: “Rayfin unlocks a new development model for our users. Agents write the code. Fabric ships it quickly and safely. Together, we’re giving developers something they’ve never had before: a path from idea to enterprise-grade production that’s measured in hours, not months.”

The Replit partnership is not the only signal of enterprise traction. Catasta also pointed to Replit’s recently announced [partnership with Visa](https://thenewstack.io/replit-visa-ai-payments/) — which involves a Trusted Agent Protocol for agentic commerce — as evidence of the kind of enterprise momentum Rayfin is designed to support.

## What Rayfin does

Rayfin works through GitHub-based workflows. Developers — or the agents building on their behalf — describe what to build, and Rayfin generates an enterprise-grade backend, including a database, authentication, and related services, and outputs them directly into application code. Deploying to Fabric turns those components into first-class platform artifacts, governed and discoverable through Fabric’s catalog. Application data lands in [OneLake](https://learn.microsoft.com/en-us/fabric/onelake/onelake-overview) automatically, where it is immediately available to Fabric’s analytics, real-time intelligence, and AI engines.

The security model is architectural rather than bolted on. Data never leaves the customer’s Microsoft Fabric tenant by design. Each service component is an individual artifact in Fabric, subject to the platform’s governance controls. Catasta frames this as the central concern for enterprise buyers: the number one factor as enterprise use cases grow, he says, is security — specifically, how secure are AI-generated applications in a production environment.

## How it compares to Supabase, Neon, and PlanetScale

The obvious comparison is to existing backend-as-a-service platforms — [Supabase](https://thenewstack.io/how-supabase-is-building-its-platform-engineering-strategy/), [Neon](https://thenewstack.io/neon-branching-in-serverless-postgresql/), [PlanetScale](https://thenewstack.io/planetscale-more-monitoring-connections-and-regions-for-the-database-service/) — which also offer managed [PostgreSQL](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/) under the hood and accelerate early-stage development. Catasta draws a distinction in terms of where in the application lifecycle each plays: those platforms accelerate Day 1. Rayfin is designed to ensure applications make it to production.

The bigger difference is scope, he says. Supabase and its counterparts are backend-as-a-service solutions for building applications. Fabric is an end-to-end analytics and data platform that combines data engineering, integration, warehousing, data science, real-time intelligence, and Power BI into a single SaaS offering.

Rayfin’s value proposition rests on that distinction: instead of stitching together services, developers get a backend that is already part of the enterprise data platform, with both operational and analytical workloads supported from day one.

Portability is a legitimate question. Rayfin uses a code-first model and is open source, enabling self-hosting. But it is Fabric-native by default, and Catasta is direct about this: Rayfin is optimized to deploy to Fabric. The enterprise security, governance, and data integration story depends on that deployment target.

## Who it’s for

The target user is enterprise teams, not indie developers. Catasta was explicit: Replit is seeing strong momentum in the enterprise market, and Rayfin is designed to accelerate it. The pitch aligns with a tension that enterprise software buyers know well — the productivity gains from AI coding tools are real, but the CISO’s concerns about unreviewed AI-generated code running in production are equally real. Rayfin positions itself at that intersection.

[Amir Netz](https://www.linkedin.com/in/amirnetz/), CTO of Microsoft Fabric, frames it in similar terms during a Build briefing with *The New Stack*: “You cannot just allow anybody to go build full-stack apps in the enterprise. What we want to make sure is that when people build — and we love the idea that people are building — they can deploy in a way that is secure and compliant and safe for the organization.”

Rayfin is available now as open source. Deployment to Microsoft Fabric is available for customers with a Fabric subscription.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)