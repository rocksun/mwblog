AI agents increasingly act on people’s behalf, opening pull requests, reviewing code, creating deployments, querying internal systems, or updating business applications. However, today they typically do it wearing the same ID badge as the person deploying them — every service an agent touches sees the person, not the agent, and there’s no clean way to limit what one agent can do or shut it down without cutting off everyone else too.

And that’s why [Vercel](https://vercel.com/), the company behind the [Next.js](https://nextjs.org/) web framework and its associated deployment platform, is acquiring [Better Auth](https://better-auth.com/), whose [open source TypeScript authentication framework](https://github.com/better-auth) sees some 4.7 million weekly npm downloads.

As a result of the transaction, Better Auth creator [Bereket Engida](https://www.linkedin.com/in/bekacru/) and the core team are joining Vercel to continue their work on the framework and on agent identity more broadly.

## Agents under borrowed logins

Better Auth is best known as an open source TypeScript authentication framework, used by developers to add login, sessions, user management and permissions to web applications across multiple frameworks. By the time Vercel came calling, though, the startup had already begun looking beyond authenticating people.

Indeed, Better Auth had started developing [Agent Auth](https://agentauthprotocol.com/), an open protocol designed to give AI agents identities of their own, with scoped, delegated and revocable permissions that remain separate from those of the person deploying them.

Better Auth isn’t alone in its embrace of agent identity. Anthropic [recently introduced Claude Tag](https://thenewstack.io/anthropic-claude-tag-slack/), which gives Claude its own presence in Slack under its own connected accounts, rather than having it act through the identity of whoever tagged it. The implementation is different, but the underlying idea is similar: treating AI agents as distinct actors with their own identity, rather than extensions of the user who invoked them.

> “We’re a small team; the agent identity problem is big and moving fast.”

Explaining the decision to join Vercel in a [Tuesday blog post](https://better-auth.com/blog/better-auth-joins-vercel), Engida writes that solving that problem had grown beyond what a small startup could realistically tackle alone.

“We’re a small team; the agent identity problem is big and moving fast,” Engida notes. “With Vercel’s infrastructure, distribution, community, and product surface area, we can bring these ideas to developers at a much larger scale than we could alone.”

In a separate [blog post](https://vercel.com/blog/vercel-acquires-better-auth) published on Tuesday, Vercel CEO [Guillermo Rauch](https://www.linkedin.com/in/rauchg/) makes a similar case, arguing that existing identity systems were built for people rather than autonomous software.

“When an agent acts on your behalf, it runs under your identity and access, so every service it touches sees you, not the agent,” Rauch writes. “There’s no clean way to limit what any one agent or subagent can do, or to shut down just one without cutting off the rest.”

That work will now feed into [Vercel Connect](https://vercel.com/blog/introducing-vercel-connect) and [Eve,](https://thenewstack.io/vercel-launches-eve-an-open-source-framework-that-treats-agents-as-directories/) the company’s products for connecting AI agents with external services.

> “When an agent acts on your behalf, it runs under your identity and access, so every service it touches sees you, not the agent. There’s no clean way to limit what any one agent or subagent can do, or to shut down just one without cutting off the rest.”

## The road to Vercel

![Vercel CEO Guillermo Rauch with Better Auth CEO Bereket Engida](https://cdn.thenewstack.io/media/2026/07/3f5b2397-phb_2919-edit-2-1024x683.avif)

*Vercel CEO Guillermo Rauch with Better Auth CEO Bereket Engida*

Better Auth began with a problem Engida encountered while building an unrelated open source analytics project. Wanting support for team accounts with different permission levels, he found existing authentication libraries didn’t fit his needs and spent around seven months building his own framework-agnostic alternative before releasing the first version in September 2024.

The project grew quickly, with Better Auth going through the Y Combinator (YC) acclerator program before [raising a $5 million seed](https://better-auth.com/blog/seed-round) in the summer of 2025. Later that year, [it took over stewardship of Auth.js](https://better-auth.com/blog/authjs-joins-better-auth) (formerly NextAuth.js) after the maintainers concluded the two projects were heading in the same direction.

Rauch stresses that the acquisition doesn’t change the framework’s open source status moving forward, with Better Auth remaining freely available under a MIT licence.

“The team continues to lead development with the same open contribution model, community governance, and framework support across the ecosystem,” he writes.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)