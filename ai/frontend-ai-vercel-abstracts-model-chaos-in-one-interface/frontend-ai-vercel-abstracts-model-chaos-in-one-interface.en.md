A new offering by Vercel allows developers to experiment with different AI models through a single interface, without managing multiple API keys, provider accounts or rate limits.

The frontend web hosting platform introduced [Vercel AI Gateway](https://vercel.com/blog/ai-gateway) in public beta Wednesday at its annual user conference, Vercel Ship, held in New York City this year.

The gateway gives developers access to approximately 100 models, abstracting away the complexity of working with multiple AI model providers, Vercel CTO [Malte Ubl](https://www.linkedin.com/in/malteubl/) explained to The New Stack.

“If you’ve ever built any applications, it’s so tedious to go to all these vendors, get API keys,” he said.

The new offering mimics how developers have used databases for the past 25 years, he explained. It works with the company’s AI SDK, released in 2023.

“Rather than saying I’m going to use Oracle SQL and I’m going to use [PostgreSQL](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/), I’m really using these, like, access systems that abstract away the underlying database,” he said. “You can think about the [AI SDK](https://thenewstack.io/vercels-next-big-thing-ai-sdk-and-accelerator-for-devs/) as basically being the same thing, where you have one API, and whether you talk to [Gemini](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/) or you talk to [OpenAI](https://thenewstack.io/openais-sam-altman-ai-is-now-ready-for-the-enterprise/) doesn’t matter.”

It also solves a major headache for developers: It simplifies the process of switching models during development. With AI Gateway, developers can use their Vercel account to gain access to approximately 100 models without additional work, he added.

It’s common for developers to start with a frontier or large, generative AI model, which is easy to make work but expensive, and then find a smaller model that more precisely fits the application’s needs for less cost, he said. AI Gateway gives developers an easy way to experiment with different models to find the right fit for their applications.

“It completely takes away the friction of [trying different models](https://thenewstack.io/should-you-try-small-language-models-for-ai-app-development/) during development,” he said. “You basically just change the name of the model and then it works.”

Once the application deploys to production, developers can then just purchase the chosen model or models through Vercel, he said.

The AI Gateway also helps manage usage, so if one source is down, it will get the same service from another cloud provider, he added.

“All of these vendors are horrible in terms of stability compared to what you might be used to from traditional computing,” he said. “So you’re definitely, you’re definitely not talking 99.9% — you’re talking about like 99% availability.”

Basically, it’s acting as an AI model load balancer proxy server for production, he explained. Developers can also bring their own API keys and Vercel can just bill you through the AI gateway.

It is transparent about the cost, as well, and Vercel is selling everything at the market rate — there is not a markup, he added.

## Vercel’s Sandbox for AI Deployments

In another AI-play, the frontend web hosting company also launched [Vercel Sandbox](https://vercel.com/docs/vercel-sandbox), which lets users run untrusted code safely, such as that created by AI on Vercel’s infrastructure. It’s in beta.

It’s basically Vercel’s “infrastructure as a service” play, allowing developers to run unverified code created by AI in a safe way.

This is not for situations where the developer is committing the code for code review, but rather in situations where there is an application that’s generating code in production, he explained.

Vercel took its own sandbox infrastructure and made it available as a service, he said.

“You’re building this app for your customers, and your customer prompts, generates code — you want to run it,” he said. “It basically turns our built infrastructure into a platform. We’re doing over 1 million builds a day, so it’s ultra rock solid, a production ready infrastructure, packaged up to be easy to use in this AI context.”

Essentially, developers get a secure virtual machine that’s optimized for running code that might be insecure. It’s not optimized for scale but to run once to ensure the code is safe, or identify where the problem is if there’s an error. The sandbox has essentially zero access privileges except what the developer gives it, he added.

In other news at Ship this week, Vercel announced [**Rolling releases**](https://vercel.com/changelog/rolling-releases-are-now-generally-available), a new platform feature that gradually rolls out new deployments to a subset of users. Unlike custom rollout logic, it’s integrated into the platform and monitors deployment health in real time, the company said.

Deployments start with 20% of traffic by default and then that shifts over time, either automatically or manually.

It also reduces the risk of bad deployments reaching 100% of users and gives teams a window to catch regressions — like broken checkouts, backend errors, or performance degradation — before they impact all traffic.

It also announced **[Active CPU pricing for Fluid Compute](https://vercel.com/blog/introducing-active-cpu-pricing-for-fluid-compute),** which will no longer charge compute rates for idle times, he said.

Fluid Compute is [Vercel’s compute model](https://thenewstack.io/vercel-rolls-out-more-cost-effective-infrastructure-model/) designed to handle modern, dynamic workloads like AI and streaming, by combining serverless and traditional server architectures.

“Every request is going to use a certain amount of CPU, and you pay for it, and but there are certain extreme cases which actually become important,” Ubl explained.

For instance, if a developer has an application that can’t even fill up the CPU because there aren’t enough users. Instead of charging for the whole CPU, the developer is charged only for the three users, he explained.

“That’s why our active CPU is so nice, because you only pay for the CPU, and if you only have three users, then you pay for three users,” he said. “You don’t pay for the entire box.”

Finally, Vercel announced **first-class support for [microfrontends](https://thenewstack.io/4-lessons-learned-from-building-microfrontends/)**. Vercel allowed microfrontends previously, but it required a lot of hardcoding support from organizations that wanted to deploy the architecture, Ubl said. Now, [Vercel has built out features](https://vercel.com/docs/microfrontends) that make it easy for developers to deploy microfrontends with less custom work.

These moves better position Vercel to support agentic AI, Ubl noted.

“The goal overall is to turn Vercel into the premier platform for hosting AI applications, in particular agentic applications,” Ubl said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)