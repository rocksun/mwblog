“I’ve been doing this since the ’90s — decades of building guardrails to prevent humans from breaking production. We’re now removing those guardrails and saying: Hey, come play with us, come create, go build the next experiences of the world,” Netlify CTO [Dana Lawson](https://www.linkedin.com/in/dglawson/) told the packed audience this week at AI Native DevCon in London.

Agentic AI has established the next layer of abstraction, where intent — expressed in conversational language — becomes the next programming language that exponentially more people can create with. There will be a [billion new applications written by 2029](https://www.idc.com/resource-center/blog/agent-adoption-the-it-industrys-next-great-inflection-point/) because AI enables what Lawson calls *the builder*.

Sure, this is great for these citizen developers. But, for many software engineers, this is the first time they’ve faced this level of career uncertainty. The industry — and by extension the world — is changing so fast, and tech layoffs dominate headlines. Even if your company hasn’t taken that aggressive route, it’s normal that you’d question what your role is now that you seldom write code.

So if software development is no longer defined by writing code, what distinguishes an engineer? According to Lawson, they are the ones who understand what agent experience (AX) can and should be.

![](https://cdn.thenewstack.io/media/2026/06/162b569d-dana-lawson-ainativedevcon-1-1024x576.jpg)

Dana Lawson at AI Native DevCon this week in London (Credit: *The New Stack*)

## Has the engineer’s role changed?

In some ways, no. Because writing code was only ever less than a quarter of an engineer’s job, and increasingly the least strategic bit.

“You are the shepherd of production,” Lawson says of the engineer’s experience in the age of AX. “Make sure that what goes in and what goes out is well-understood. If we do agentic experiences right, those agents should be event-driven activities where the signal is pushed to a developer versus pulled.”

Now more than ever, success or failure of agentic adoption comes down to a comprehensive understanding of complex systems, the route to production, and business context.

“Agent experience is thinking about all that new system context and intent in the software delivery lifecycle,” Lawson contends. “It is the practice of designing where humans and agents collaborate seamlessly — and it isn’t just about making API calls agent-friendly.”

Netlify launched in 2014 as a platform for front-end website and application developers. This new onslaught of citizen developers don’t speak developer; they don’t know what git is. In response, the platform has had to be rebuilt, not just to communicate with developers, but with AI agents and these new builders.

In reworking the platform for these two new audiences, Netlify found it was better able to serve its developer audience. Because, as Lawson defines it, agent experience is a combination of developer experience and user experience. And by solving for both, her team was finally able to help users overcome institutional and domain-knowledge boundaries that have always gatekept the industry, limiting it to folks with computer science degrees.

“When we made the agent error messages clearer, structured the build output for machines, and removed unnecessary friction, our developers also benefited from this,” Lawson reflects. “Every human assumption we removed made the platform better for everyone.”

## For both kinds of builders, it’s about what to build.

As [Outcome Engineering](https://o16g.com/) argues, AI removes human bandwidth as a limitation. That means the engineer job becomes even more about deciding what *not* to build.

“The bitter truth is you’re going to be stuck building a whole bunch of stuff that’s going to be obsolete, probably in months, not years. So finding the right paths and putting intent in the right areas is what’s going to be the keeper,” Lawson tells *The New Stack* in a follow-up interview, about this risk of too much too fast. “This is where development and engineering practices are core to this because now anybody in the world can literally build anything.”

It’s up to engineers to make sure what the builders build is right — for your business, your customers, security, and the world.

“We have the burden of responsibility on our shoulders to make sure that we are implementing compaction, we are thinking about compression, that we are building the right resources to make the internet continue to benefit open and democratized for everybody, but also be environmentally friendly,” she continues.

This means that engineering, more than ever, must focus on the internal tech stack, people, and processes.

## Systems rebuilt for your agents and agentic intent

“You really do have to rethink the entire stack along the way, from how we express the intent to how systems communicate, so that we can trust,” Lawson says. After all, enterprise systems were designed for human operators.

“There was an intent that you would be a part of that loop, even if stuff was set to work continuously, agents struggle with this. They can’t see across boundaries. Every API speaks a different dialect,” as Lawson puts it. Critical workflows are known only by word of mouth, “in a Slack thread from 2022, in an undocumented Terraform module.”

Lawson offered architectural evolutions that drive better agent experience:

1. **From APIs to capabilities**: while software architecture has always exposed endpoints via APIs (e.g. POST, GET, PATCH), agent-native systems expose intent-level operations through capabilities that express what you want to accomplish (e.g. create\_a\_site, deploy-repository)
2. **From request-response to event-driven: moving away from request-and-wait**, agents subscribe to events, observe system behavior, and, when permitted, act autonomously
3. **From machine-readable to agent-legible:** Shifting away from individuals’ understanding of certain “mysterious” segments of architecture, an agentic platform creates architectural complexity blueprints—for agents and humans alike—to understand a system before they make changes

“This development cycle becomes a continuous human-agent loop, so no longer is it a handoff” to operations teams, Lawson says. “It is everybody participating at the same time, and the human stays in the loop by providing judgment, taste, direction. This loop moves at machine speed. This isn’t replacing engineers, it’s amplifying everybody’s ability to be a builder.”

## Human-set agentic boundaries

“Agents don’t just write the code; they’re participating in the enterprise infrastructure lifecycle; they’re generating the tests, detecting faults, analyzing build blocks, proposing fixes, opening PRs, CI/CD — it all just becomes a continuous feedback loop,” Lawson remarks. “Some things may not be at that level of sophistication, but this is where you need to start thinking about reinventing those needs.”

At least for now, agent experience should be grounded in the humans driving it. For the Netlify team, that looks like:

* Each agent only executes within its specified sandbox.
* Human-in-the-loop by default, focusing on meaningful, intent-driven part of the engineer’s job.
* Each agent action is logged, making it auditable and instantly rollable back.

> “If you can’t explain what the agent did, why would you trust it in production?”

“If you can’t explain what the agent did, why would you trust it in production?” Lawson says.

“Engineering evolves from implementing every feature to really ensuring that the systems and guardrails architecture is tight and solid.”

The good thing is, at least for now, designing for agents actually was designing for humans all along. “It’s not just agent experience, it’s human experience, and that’s what AX is for,” Lawson puts it.

> “The judgment to build systems that agents can work with, that is the engineering skill of the future…”

“AI forced us to clarify our architecture, our structure, and our signals. It, in fact, made us all better developers. The judgment to build systems that agents can work with, that is the engineering skill of the future, and agent experience ensures agents amplify human creativity rather than replace it.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)