Platform engineering’s goal has always been to make engineers more self-sufficient without sacrificing standards.

The best way to accomplish this was through self-service in a platform you controlled. When a developer needed a new service, they clicked a button and got a repo, a CI pipeline, monitoring, and a Dockerfile. You could let them do this because you built in engineering standards. That combination of self-service and standards was a win-win for you and your developers. They got velocity, you got control.

With AI, developers became builders of [agentic workflows](https://thenewstack.io/what-agentic-workflows-mean-to-microservices-developers/). By building agents, they can automate large parts of their jobs. They’re building SRE agents, release agents, skills, etc. They already had permission to use all these AI tools, so they started stitching stuff together.

> “With AI, developers became builders of agentic workflows. By building agents, they can automate large parts of their jobs.”

This results in a lack of governance & visibility into agents performing destructive operations without human oversight.

We call this agent sprawl.

![Diagrammatic web of interactions between developers, managers, agents, and engineers](https://cdn.thenewstack.io/media/2026/04/e4486b87-1-1024x464.png)

So what does that mean for you as a platform engineer?

## How should you think about the relationship between you and developers?

As platform engineers in an AI world, of course, you want developers to use AI more. But every time adoption of technology goes up, so does the demand for everything you’re responsible for, like costs and governance.

There’s also something uncomfortable about being bypassed by the people you were supposed to enable. You take pride in making developers more capable with your help, but now they’re building agents themselves.

AI has given developers the power to build anything that automates their work, such as an SRE agent, a deployment agent, or even a basic catalog that helps their agents work.

To make their agents powerful, they want to feed them real actions & access to real data. To do that, they still have to go through you. **But even without the actions and context lake you provide, they can still create things powerful enough to be dangerous.**

Let’s say an engineering team builds itself an SRE agent without going through you. We can even go a step further and say that it works really well at triaging issues, saving the team hours per incident.

* But what does the agent probably not do?
* It probably didn’t leave an audit trail.
* It probably isn’t being respectful of PII.
* It probably didn’t use the appropriate credentials.

And the list goes on.

What the team definitely didn’t do was build the agent with the standards their company expects from the start.

And why would they? They have a real, immediate need, and AI makes it easy to solve. They’re also feeling pressure from engineering leadership to produce more results.

## Developers shouldn’t have to wait. (And they’re not going to.)

With this new tool and the new urgency, they’re just doing their jobs in a new way, primarily doing two things:

1. They’re using MCP to query data and get insights that help them or their agents work.
2. They’re building agents like SRE agents that are becoming more capable and taking on more responsibilities across the SDLC.

Developers (and agents) getting the data they need can be solved in a scalable way by providing a rich context lake.

But when all engineers start building agents, how do you facilitate that in a scalable way?

## The product management side of platform engineering

Given the new reality we’re all living in, platform teams have three options.

You can do nothing and let developers build agents however they want. The agent sprawl is already here anyway, so why fight it? The problem is you end up with no visibility, no standards, and no way to intervene when [something goes wrong](https://thenewstack.io/automation-all-fun-and-games-until-something-goes-wrong/) (and it will).

You can mandate that all AI development flows through the platform team. You can probably expect a revolt if you choose this route because the tools are already in developers’ hands. Cursor runs locally. Claude Code runs locally. This is a good way to slow down engineering, not speed it up.

Finally, this is the only option that will work: make the platform compelling enough that developers actively choose to build agents with it.

![Matrix of development and platform engineering a year ago vs. today](https://cdn.thenewstack.io/media/2026/04/c7fd97f2-2-1024x441.png)

So how do you make it more compelling?

This is what I like to call the product management side of platform engineering. You first need to understand what developers are actually trying to do, then remove the hardest parts.

I’ll let you do the work in your org of talking to developers and finding out what they find difficult when building agents.

But I’ll also give you a look at what I see as some common denominators, because developers building agents hit the same walls every time. Scattered data, wild integration connections, lack of approval gates (or too many), or too much access to critical systems, to name a few.

I see those issues repeat themselves across all agents at the “kicking the tires” stage. But if you succeed in removing some of that friction or at least minimizing it, you’ll have a much higher chance that developers will create agents that don’t end up hitting those walls.

There’s also something else here. Developers who build something useful want others to benefit from it, just as in open-source. If there’s a place to share the incident triage skill their team built, they’ll put it there. If there’s a registry where others can find it and extend it, it gets better over time. The platform becomes the place where good work accumulates.

That’s what makes a platform compelling. When developers feel they are using an experience that was designed for them (and their agents).

## How do you create a compelling agent-building experience for your engineering team?

Now that your developers are agent builders, one of your jobs is to make that experience as seamless and enjoyable as possible. They’re coming to make something new. That’s a creator experience, and it requires a different kind of thinking. This is DevEx 2.0.

Here’s what I think matters most when you’re designing for builders:

1. **They need to know what’s available to them before they start**. A developer sitting down to build a release management agent shouldn’t have to ask around to find out what data they can access, which integrations exist, or what actions are possible. That discovery has to be seamless.
2. **They need early wins**. The fastest way to get a developer invested in your platform is to get them to something working quickly. Starter templates, example workflows, and pre-built skills are all great places for them to start forking. A developer who gets something running in an hour is far more likely to build the real thing on your platform than one who spent the first day figuring out how to authenticate.

> “A developer who gets something running in an hour is far more likely to build the real thing on your platform than one who spent the first day figuring out how to authenticate.”

**They need to see what others have built**. This is the open source side of things that developers love. Developers who build something useful want to share it, and developers starting from scratch want to see what already exists. A skill registry or agent catalog will make the platform feel alive. When a developer can browse what their colleagues built and extend it, the platform stops feeling like infrastructure and starts feeling like a community.

![Screenshot of Port's skill catalog page.](https://cdn.thenewstack.io/media/2026/04/45c02668-3-1024x643.png)

Let’s expand on how to help your team discover what’s available before they start building agents.

What [building blocks](https://thenewstack.io/vercel-marketplace-offers-agentic-ai-building-blocks/) should you give them that their agents will need?

![Diagram of the 7 blocks of tech debt that every demo agent creates.](https://cdn.thenewstack.io/media/2026/04/c61036a4-4.png)

*I wrote previously about the “*[*Hidden tech debt of agentic engineering*](https://newsletter.port.io/p/the-hidden-technical-debt-of-agentic)*,” where I expanded on the 7 blocks of tech debt every demo agent creates*

**A reliable context lake.** Agents need to know things in real time, and that information needs to be accurate: who owns this service, what changed in the last deploy, what this service depends on, and who’s on call right now.

Without this, a team building their own agent spends more time on data plumbing than on the actual logic, and gains access to data they wouldn’t otherwise have. The platform team consolidates it in one place, keeps it up to date, and exposes it via an API or MCP that any agent can query.

![Preview of Port's fraud detection interface, viewed graphically](https://cdn.thenewstack.io/media/2026/04/580adb86-5-1024x737.png)

**Pre-cleared integrations.** Agents need to talk to systems: GitHub, PagerDuty, Datadog, Jira, and your cloud provider. Getting access to each of those is a process. Developers building agents on their own may go through that process independently. By centralizing it, the platform team clears the integrations once, and every agent gets them.

![View of pre-approved systems that Agents are able to talk to via Port.](https://cdn.thenewstack.io/media/2026/04/8abf42b7-6-1024x665.png)

**A menu of approved, governed actions.** Agents don’t just read. They do things: trigger rollbacks, open PRs, restart pods, close incidents. Teams building agents on their own either avoid actions entirely (so the agent just tells you what to do) or wire them up without guardrails. The platform team defines which actions are available as tools, so the question is never “can this agent do this?” but “did we explicitly allow it to?”

![Snapshot of Port's Day-2 Operations interface](https://cdn.thenewstack.io/media/2026/04/8beac8f8-7-1024x661.png)

**Deterministic policies.** An agent that suggests a production rollback is fine. An agent that triggers one at 2 a.m. without waking anyone up is not. You can’t handle that with a prompt or skill like “Please ask before doing anything in production”. Policies must be encoded as gates: staging auto-approves, production requires human sign-off outside business hours. They either pass or they don’t, and they need to be deterministic.

![Chart of agentic workflows](https://cdn.thenewstack.io/media/2026/04/fb407f4e-8-1024x207.png)

**An audit trail.** When something goes wrong at 3 a.m., you need to know what the agent did, what data it accessed, what triggered it, and what the outcome was. Teams building their own agents almost never add logging upfront. It feels like overhead at first. The platform team needs to build audit logging into the workflow engine, so it’s automatic. Every action is on the record, whether anyone thought to ask for it or not. The added benefit of the audit trail is that it also serves as the decision trace that will help agents improve over time.

![Screenshot of Port's Audit Log interface](https://cdn.thenewstack.io/media/2026/04/d3d0038c-9-1024x665.png)

**A review process.** Taking an agent from demo to production requires someone from the platform to check permissions, test edge cases, and define what production-ready actually means. The platform team must own that lifecycle: from experiment, to reviewed, to trusted, to fully autonomous.

![Snapshot of Port's Agent Registry interface](https://cdn.thenewstack.io/media/2026/04/82b2212e-10-1024x643.png)

**An approval or human-in-the-loop layer.** At some point, every agent needs to stop and ask a human. Teams building their own approval logic get this wrong in different ways. Some hardcode a Slack message, some skip it entirely. None of them shares a model, so when agents need to work across teams, the approval logic breaks at the seam. The platform provides one: these actions auto-approve, these require a human, and this is who gets notified. A team that builds on it doesn’t have to think about any of that.

![Snapshot of Port's agentic configuration, including the option to enforce manual human-in-the-loop approval.](https://cdn.thenewstack.io/media/2026/04/cab021a9-11-1024x850.png)

None of these is complicated on its own. But when every engineer is building their own agents, the problem compounds quickly.

## The surface area grew

The ground is shifting, and your old job didn’t go away. The service catalog still needs to be maintained. The golden paths still need updating. The CI/CD integrations still break.

And now on top of all of that, there are agents running in the org that you didn’t build, accessing systems you provisioned, doing things you can’t fully see. Developers who never wrote infrastructure code are building internal tools from scratch. The surface area of what you’re responsible for grew, but nobody took anything off your plate to make room.

Some platform teams are watching this unfold and feeling like they’re losing control of something they spent years carefully building. And in a way, they are. The era where every infrastructure decision flowed through the platform team is over.

> “The era where every infrastructure decision flowed through the platform team is over.”

Just because you don’t have a monopoly anymore doesn’t mean you’re not relevant. **You’re actually about to become more relevant than ever before.** Because developers aren’t waiting and the number of agents is exploding. And the window where the number of agents in your org is still small enough to get ahead.

We discussed a win-win for platform engineers and developers. Both teams can still achieve a win-win while using AI.

Port is built for platform engineers stepping into this new role who want to build a win-win experience. It gives your team the foundation to give developers the building blocks they need in their new builder role: governed data, pre-cleared integrations, approved actions, approval gates, and more.Every engineer is a builder now. It’s time to build a platform for them while staying in control.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/05/24f5579b-cropped-bff51576-zohar.png)

Zohar Einy is the CEO of Port, the agentic engineering platform that is helping customers like GitHub, Visa, and PwC move from manual to autonomous engineering. Zohar began his career in the Israel Defense Forces' 8200 unit as an engineer,...

Read more from Zohar Einy](https://thenewstack.io/author/zohar-einy/)