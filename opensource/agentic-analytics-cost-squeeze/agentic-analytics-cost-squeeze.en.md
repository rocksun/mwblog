An AI agent let loose on a data warehouse can run ten or a hundred times more queries than a human-era analytics workflow ever did. The problem for any closed data ecosystem is that those queries tend to route through the same expensive compute path.

[Anjan Kundavaram](https://www.linkedin.com/in/anjan-kundavaram/), Chief Product Officer at [Fivetran](https://www.fivetran.com/), says in a new episode of *The New Stack* podcast, “It’s kind of like using a Lamborghini to mow the lawn all the time.”

> “It’s kind of like using a Lamborghini to mow the lawn all the time.”

Kundavaram made the case in a conversation we had at Google Cloud Next. Fivetran was using the event to push a framing the company calls “Open Data Infrastructure” and to roll out an [Open Data Infrastructure Data Access Benchmark](https://www.businesswire.com/news/home/20260422406594/en/Fivetran-Launches-Industry-Benchmark-Exposing-How-Vendors-Limit-Data-Access-for-AI-Workloads) aimed at making it harder for vendors to quietly tax their customers’ AI workloads. The argument has timing on its side. TNS [reported earlier this year](https://thenewstack.io/agentic-ai-is-coming-but-can-your-data-infrastructure-keep-up/) that most enterprise data systems were never built with agent swarms.

VIDEO

The economics shift Kundavaram describes starts with a counterintuitive fact about agents. They are not humans. They do not need their answers in seconds.

“An agent could go spend more time if the agent thinks you’re going to save 10x the cost,” he says.

In a stack with multiple compute engines available, the agent can route an expensive analytical question to one engine and a cheap one to a lighter, lower-cost option. In a closed stack, every question goes through the same expensive door.

That is one source of the AI cost squeeze. The other is what happens when the data and the context the AI needs are not consolidated in the first place.

> “It’s going to be like a triple whammy.”

If a customer’s information lives in a lot of different systems and its context is not in one place, Kundavaram says, the consequences stack up: poor AI answers, sharply higher costs because agents run far more queries, and waste from feeding those queries with weak context.

“So it’s going to be like a triple whammy,” Kundavaram says.

The reflex inside most data organizations is to clamp down. Kundavaram says that is exactly the wrong move: “One of the data leaders told me at a very large company, hey, our analytics budgets, just queries, have gone up a lot,” he says. “In fact, our own internal analytics leader [at Fivetran] was like, hold on, I got to put control. So we’re like, ‘No, no, don’t put controls. Let’s innovate.'”

His broader prescription is that the productivity unlock from agentic analytics only materializes if customers refuse the lockdown instinct and invest in open infrastructure and semantic discipline instead.

Fivetran has the obvious commercial interest in making this argument, and the company has been busy turning it into a product. TNS [covered](https://thenewstack.io/fivetran-brings-data-lake-interoperability-to-google-cloud/) Fivetran’s data lake interoperability work on Google Cloud, and the company [donated SQLMesh to the Linux Foundation](https://thenewstack.io/fivetran-donates-sqlmesh-lf/) in March.

The harder question is whether enterprise buyers will read the cost curve the same way Kundavaram does, fast enough to act on it before the bills start arriving. That part is still up to them.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)