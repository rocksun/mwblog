# API Sprawl: Not Just a Tech Problem
![Featued image for: API Sprawl: Not Just a Tech Problem](https://cdn.thenewstack.io/media/2025/04/ce5ba840-api-sprawl-culture-problem-1024x576.jpg)
Everyone is familiar with that uncomfortable feeling you get when you’re a new developer joining a new team, opening the internal API portal and finding… 57 APIs named `user-APIs`
? Uh oh. Some have associated docs. Some don’t. One points to a deprecated staging cluster. Half of them is logged, the other half are hiding in the shadows. Another hasn’t been touched since before the pandemic. (Has it been five years already?) Which ones are you supposed to use?

Or perhaps you’re a tech leader who is asked: “How many APIs are being utilized or in production? How many are being adopted?” And then you sheepishly look over to your engineering managers, hoping someone has that answer ready when the reality is you… Just. Don’t. Know.

Welcome to the hidden human cost of [API sprawl.](https://www.akamai.com/glossary/what-is-api-sprawl) It’s not just about code. It’s about culture.

## Sprawl Is Tribal Knowledge, Weaponized
As development teams grow and ship constantly, [APIs multiply](https://thenewstack.io/heres-how-to-tame-your-api-sprawl-and-why-you-should/). You get a strong team going where everyone is constantly hacking away at their own to-do list, and the pressure to be fast and productive is on. The result is a ton of APIs, not necessarily organized, standardized or even documented across various developer teams.

Without strong governance or tooling, documentation falls out of date, ownership becomes fuzzy and new developers are left playing a frustrating game of API archaeology. This not only slows your developer onboarding time (which in our recent [survey research tends](https://getambassador.io/resources/optimize-development-container-environments) to be a problem for 43% of tech leaders) but also makes for a poor developer experience for all.

And we haven’t even gotten to the worst part… that most of the answers don’t live in some discoverable catalog for visibility but in someone’s head. Usually that honor falls to the engineer who’s been there the longest, or who just happened to write the first version of that billing service three years ago. That’s a lot of risk to take on should that person leave.

This isn’t sustainable. It burns out your developers, slows onboarding and makes cross-team collaboration a nightmare. Plus, it turns what should be a strategic advantage (your so-called reusable APIs, if you can even find them) into a source of technical debt and team friction. Even worse, when you [throw AI into the mix](https://thenewstack.io/ai-operations/), APIs are going to multiply even more because AI will be writing them.

## API Sprawl Is a Drag on Dev Velocity (and Morale)
It starts small: a few duplicated services, some inconsistent naming conventions, a handful of teams rolling their own versions of the same API because they couldn’t find the original (or didn’t trust it).

But over time, the impact becomes clear:

- New engineers take weeks to ramp up.
- Unknown data exposure if sensitive data is unintentionally leaked through forgotten or under-monitored APIs.
- Testing and deployment cycles slow to a crawl, even though 59% of technology leaders report needing to speed up — a ton.
- Changes become risky because no one knows who owns what.
- Burnout creeps in because every fix feels like a fire drill.
In short: API sprawl isn’t just a systems issue. It’s a people problem. And it’s eating your productivity alive and inhibiting the predictability, happiness and velocity of your organization.

In a recent panel of technology leaders [discussing developer productivity metrics](https://www.getambassador.io/blog/what-engineering-teams-measure), panelist [Mary Moore-Simmons](https://www.linkedin.com/in/mmooresimmons/) of Keebo AI shared this important tidbit, driving home that point: “I get that tracking developer happiness and satisfaction may seem intangible, but it’s crucial for long-term success. Teams that are constantly in crisis mode can’t reflect, learn or grow.”

And not handling your API sprawl problem will keep your developers constantly in crisis mode.

## Stop Treating Symptoms. Fix the Root Culture.
You can’t fix API sprawl by emailing the team “please write better docs” or spinning up yet another spreadsheet to track services. You need a [cultural shift](https://thenewstack.io/tech-culture/) — and tooling that supports it. Tools that can streamline that cultural shift include ones that:

**Help you discover and document what’s already there:**Seek[API development](https://www.getambassador.io/blog/api-development-comprehensive-guide)tools that map out your internal API landscape so that you don’t lose track of what you have across your developer environment. Visibility is key, not just for your developers but also for your tech leader who needs to be able to quickly answer questions like, “How many APIs are there and what are they costing us?”**Standardize automatically:**You need to generate consistent, compliant[API specs](https://www.getambassador.io/blog/openapi-specification-structure-best-practices), and this is where you can lean into[AI-assisted spec generation](https://www.getambassador.io/products/blackbird/api-development)to ensure standardization is a top priority.**Enable parallel development easily:**For example, find tools that offer[hosted, production-like environments](https://www.getambassador.io/blog/prod-like-development-environments-improve-api-efficiency)that let frontend and backend teams build and test without stepping on each other.
## Looking Ahead: The Future of Sprawl and MCPs
It’s also worth noting that alongside the rise of AI, teams are beginning to adopt emerging frameworks like the [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) to help enforce consistency, not just in code but in the thinking behind your APIs (the cultural side), and facilitate context-heavy interactions with large language models (LLMs). MCPs will give teams a shared model for how relationships and endpoints are structured and reduce the burden on unique APIs for each service to engage directly with an LLM.

Think of MCPs as shared blueprints for how teams design, define and evolve integration. Instead of everyone winging it with their own take on `user-service`
or `billing-api`
, MCPs enforce reusable, agreed-upon structures. The result as it relates to sprawl? Fewer redundancies, better onboarding and APIs that scale with your organization — not against it.

Eventually, this new technology will also help solve the larger problem of API sprawl, but in the meantime, you can still focus on the cultural change that will help your developer team soar.

## Culture Change Starts With Visibility
Many engineering leaders will argue that API sprawl isn’t a cultural problem; in fact our recent survey showed that leaders consider developer experience as the least of their pressing concerns, with only 15% citing it as an issue. But that’s because they don’t feel the pain developers feel spending countless hours trying to find things.

However, what many fail to realize is that when you don’t get that right, the other 85% of common challenges (security, maintenance and cost overruns) are made even worse. Refusing to tackle API sprawl and the impact it has on your developers’ experience is, through and through, a cultural problem that makes the rest of your challenges even worse, costing you more money, time and head count.

In fact, [48% of organizations struggle with API sprawl](https://www.traceable.ai/blog-post/unveiling-the-2023-state-of-api-security-a-panoramic-industry-view), according to a Traceable report. And I would bet that even more struggle with it without realizing that’s what their problem is.

Look, you can’t fix what you can’t see. And right now, many engineering leaders are flying blind when it comes to API sprawl — paying the price in security risks, missed deadlines and developer churn. The first step isn’t just technical. It’s human.

Give your team the tools and approaches to collaborate, the visibility to avoid duplication and the environment to move fast, without burning out.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)