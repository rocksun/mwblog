[OpenClaw](https://thenewstack.io/openclaw-github-stars-security/) changed everything. The open-source [AI agent](https://thenewstack.io/ai-agents-and-their-life-cycle-what-you-should-know/), which went from zero to 247,000 GitHub stars in 60 days, finally delivered on the universal-agent promise that Google and Apple had been dangling for years but never shipped.

[Sean Blanchfield](https://www.linkedin.com/in/seanblanchfield/?originalSubdomain=ie), CEO and co-founder of Dublin-based startup [Jentic](https://jentic.com/), tells *The New Stack*, “Apple was showing this amazing version of Siri where you just ask it to do anything. That is a wonderful version of Siri that never shipped.

“It took an open-source project to blow the lid off it, and now everyone’s scrambling,” Blanchfield says. “Google or Apple could have more easily done it, but didn’t have the guts to.”

## The security mess OpenClaw left behind

Blanchfield adds, “There wasn’t a huge technical challenge to do this. It’s more of a willingness to do it. What held them back was the risk profile of the thing.”

The result of that risk aversion is a security mess. Blanchfield notes that researchers have found more than 40,000 OpenClaw instances exposed on the public internet. In addition, he notes that Cisco’s AI security team documented data exfiltration and prompt injection in the wild. [One engineer hijacked an agent in under two hours](https://thenewstack.io/openclaw-moltbot-security-concerns/). And the root cause, Blanchfield says, is simple. OpenClaw agents blab credentials, he notes.

“If you say, ‘Can you help me out here,’ it’s like, ‘Yeah, I’ve got a password for that — here it is,'” Blanchfield says. “If someone emails you saying, ‘can I borrow your password for Stripe and you email it back,’ that holds you back from using this stuff for real.”

## A permission firewall for the agentic era

That is the problem Jentic is trying to solve with Jentic Mini, a free, open source, self-hosted offering that launched on Wednesday. Jentic Mini gives developers a lightweight way to run Jentic in their own environment while adding a practical safety and control layer around agent access. Jentic provides a permission firewall for AI agents.

Jentic Mini gives developers a lightweight way to run Jentic in their own environment while adding a practical safety and control layer around agent access.

Built for developers running OpenClaw and other general-purpose agents, Jentic Mini sits between the agent and the APIs it is connecting to. It holds credentials centrally, so the agent never actually sees them, enforces fine-grained permissions, and provides a single kill switch that shuts down all agent data access instantly, the company says.

## Built on 18 months of enterprise work

The product draws on 18 months of enterprise work, Blanchfield tells *The New Stack*. Jentic was founded on the premise that a universal agent would eventually arrive and require this kind of access-control layer.

An access control layer is a self‑hosted, open-source control layer that sits between AI agents (like OpenClaw) and the APIs they call, so you can give agents broad access to services without ever giving them your credentials or unlimited permissions.

So, while waiting for the moment that a universal agent would arrive, the company built out its platform for enterprises rolling out agents — financial institutions, global consultancies, manufacturers — where governance and security are mandatory. Then, when OpenClaw went viral in January, Blanchfield says he was surprised when people started signing up for Jentic’s free tier, looking for a security blanket.

“We realized what was happening, so we jumped all over it,” he says. “We’ve gone into turbo mode trying to rise to the moment.”

At the center of the launch is Jentic’s API catalog, which now spans more than 10,000 APIs. Blanchfield describes it as a [Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) for APIs and workflows. It’s a communal resource primed by agents who have spent 18 months scouring the internet for API definitions, with a built-in feedback loop so agents using it can fix inaccurate documentation and contribute improvements, Blanchfield says.

The first 400 or so APIs are solid, he says, but the quality becomes harder to judge the deeper you go into the long tail, and the agents tend to work around gaps and file fixes.

The credential problem is just the start. Jentic Mini also addresses what Blanchfield calls the permissions gap — the lack of fine-grained access control in most APIs. Gmail, for example, doesn’t let you grant an agent permission to draft emails without also giving it permission to send. That’s an all-or-nothing tradeoff that makes people hesitant to connect their accounts at all, Blanchfield explains. Jentic Mini gets in the middle of that, enforcing targeted permissions so the agent can draft but not send, read but not delete, he notes.

The product is deliberately positioned to complement rather than compete with runtime security tools like [Nvidia’s NemoClaw](https://thenewstack.io/nemoclaw-openclaw-with-guardrails/), which locks down the host machine environment, Blanchfield says.

“There are people securing the thing it runs on, and people securing how it connects to stuff,” he says. “We don’t see anyone else doing this.”

The timing is good for the company. Anthropic announced Monday that [Claude](https://thenewstack.io/claudes-free-plan-can-now-remember-you/) can now control a user’s Mac to complete tasks. This is a move in direct response to OpenClaw’s viral momentum. The [agentic AI](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/) race is on, and the security infrastructure is running behind.

## The SaaS reckoning

Blanchfield, whose background includes building the backend infrastructure for [Call of Duty](https://www.callofduty.com/) at [DemonWare](https://www.demonware.net/) — a company he co-founded that was [acquired by Activision Blizzard](https://investor.activision.com/news-releases/news-release-details/activision-set-acquire-demonware), which is [owned by Microsoft](https://news.microsoft.com/source/2022/01/18/microsoft-to-acquire-activision-blizzard-to-bring-the-joy-and-community-of-gaming-to-everyone-across-every-device/) — says he sees the current moment as more significant than anything he has encountered in decades in tech.

“I wasn’t even as excited when I encountered the web for the first time in ’95-’96,” he tells *The New Stack*. “The next era of software will not be built for humans. It will be built for agents, by agents.”

Blanchfield also says he sees a shift coming that the industry has not fully reckoned with. OpenClaw users, he notes, are already [canceling SaaS subscriptions](https://thenewstack.io/dawn-of-a-saaspocalypse/). This is because when an agent doesn’t have the right tool, it just builds one. “I’ve been canceling SaaS subscriptions everywhere,” he says. “It’s software of a different type. It’s not software we’ll ever buy again.”

Blanchfield also says he believes the more immediate question is whether enough developers trust these agents to connect them to anything that matters. Jentic Mini is Blanchfield’s bet that folks will say yes — if somebody builds the safety net first, he says.

Jentic Mini gives developers a lightweight way to run Jentic in their own environment while adding a practical safety and control layer around agent access.

Jentic Mini is available now at [jentic.com/mini](http://jentic.com/mini) and on GitHub. The enterprise product remains a separate commercial offering.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)