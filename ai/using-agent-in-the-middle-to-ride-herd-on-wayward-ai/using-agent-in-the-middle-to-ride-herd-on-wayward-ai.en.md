Development teams are under increasing pressure to adopt AI agents at the same time agents have been known to go rogue, [leaking sensitive data](https://www.pomerium.com/blog/when-ai-has-root-lessons-from-the-supabase-mcp-data-leak) and in one case [deleting a production database](https://x.com/amasad/status/1946986468586721478?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1946986468586721478%7Ctwgr%5E0b243406d50a289d0a25f3478ed7ff3f55bf7bd6%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.notion.so%2Fosohq%2F2389f1471f2b80c3b076e6bfcaac749b&utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform).

[Ilya Sutskever](https://www.linkedin.com/in/ilya-sutskever), former chief scientist and co-founder of OpenAI, has said that AI agents’ autonomous behavior will [become more unpredictable over time](https://www.reuters.com/technology/artificial-intelligence/ai-with-reasoning-power-will-be-less-predictable-ilya-sutskever-says-2024-12-14), leading to warnings that [they are “ticking time bombs”](https://thenewstack.io/ai-agents-are-a-security-ticking-time-bomb/) and calls for [new types of security and governance](https://thenewstack.io/ai-agents-are-creating-a-new-security-nightmare-for-enterprises-and-startups/).

Austin, Texas-based startup [Eve Security](https://www.eve.security/) is coming out of stealth to address the challenge with agent-in-the-loop technology that detects and acts on suspicious agent behavior while cutting out the noise from too many alerts for human intervention.

“What we’re hearing from our customers … is a lot of departments are pushing now for agentic activities, agentic capabilities, because they feel that they’re behind. So there’s a mandate from upper management, there’s a mandate for department leaders, and there’s even a push from grassroots up from employees,” said [Nadav Cornberg](https://www.linkedin.com/in/nadav-cornberg/), co-founder and CEO of Eve Security.

“The CISO department is being kind of pushed into a corner. [They’re saying] ‘You’re impacting the business. We need a solution here.’ On the other hand … I’m OK if we connect an AI agent to Grubhub and [it] accidentally orders 20 Subways. I don’t care. But if you start connecting it to Salesforce or to GitHub or to NetSuite, and suddenly it messes up those systems, guess who the CEO is going to come and chop his head off? Right? I’m going to be the one at fault.”

## Reining in Roaming Agents

With the agent-in-the-loop approach, humans still supervise, but agents are embedded in workflows to parse which actions are truly questionable.

When cofounders Cornberg, [Amit Eliav](https://www.linkedin.com/in/amiteliav/overlay/about-this-profile/) and [Sharon Eilon](https://www.linkedin.com/in/sharoneilon/overlay/about-this-profile/) set out to form the company they wanted to understand CISOs’ pain points. They found them concerned about connecting AI agents to systems containing their companies’ “crown jewel” data. How would they govern it? At the same time, they were worried about being overwhelmed with so many alerts they’d have to have dedicated staff to sift through it all to find what was truly critical.

With its EveGuard platform, its agent in the loop can observe agents and the interactions between agents and business systems to take necessary actions or to escalate the issue to a human. It’s designed to understand the intent behind an action, to address the challenges in English-language-based policies that create blind spots such as translation and cultural nuances and to estimate the risk associated with it.

AI agents are creating vulnerabilities that today’s security tools cannot see, according to [Creighton Hicks](https://liveoak.vc/team/creighton-hicks/), partner at LiveOak Ventures, which, along with Tau Ventures, funded a $3 million seed round for the company.

“Right now, most security leaders are flying blind. Eve Security enables security teams to gain visibility and control over the known and unknown agentic AI running in their enterprise,” he said.

The technology looks at what each agent typically does and whether it does anything else.

## What is the Risk?

“When you look at protocols like MCP … it’s no longer a traditional request and response. It could just be a parameter that says, ‘Please generate a report for all the financial information in Q1 and Q2. Send that report to [these people and cc someone else]. Then please take all of that information, PDF that, and then save it to this directory,’’ he explained.

If the agent does what it historically has done, it’s no problem. But if there’s an anomaly, it might have the right permissions, but this has never been seen before. Or is this something outside policy and being repeated multiple times?

Eve clusters behavior to do risk analysis.

If an agent is gathering information about the weather in Austin, for example, that behavior might not have been seen before, but it’s not that risky for the business, Cornberg explained. If it’s asking for the salary of the CEO or other sensitive company information, however, that should be a red flag. The technology can then interrogate the agent to understand the reasoning behind the request.

“So I can look at the history of reasoning to understand. I can see why it’s asking for it,” Cornberg explained. “You know, actually, the CEO was logged in here. He was asking for it. So I did a challenge in response. Now, as part of interrogation to the CEO, the CEO said, ‘Yeah, it’s me. I’m asking for that information.’ OK, I’m gonna allow it just one time, so I don’t need to bubble it up versus, you know what? No, there’s no real justification here. I’m not gonna allow this, but I’m gonna bubble it up to my manager, because I can’t approve this.”

An Eve component is installed on the customer side that integrates with security information and event management (SIEM) and other tools in which companies define policies such as role-based access control, protecting personally identifiable information (PII) and other data. It supports [Model Context Protocol (MCP)](https://thenewstack.io/mcp-a-practical-security-blueprint-for-developers/) and [Agent-to-Agent (A2A)](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/) protocols, which provide [insights into AI agent interactions](https://thenewstack.io/why-are-agent-protocols-like-mcp-and-a2a-needed/) and agent-to-agent coordination and delegation chains.

The integrations with network tools, endpoint tools and framework the agents were built with are necessary to provide a comprehensive view of what’s going on.

From there, companies can identify and allow only approved agents to operate, eliminating the risk from “shadow” agents; sanitize agentic AI  
outputs in real time to prevent [prompt-injection attacks](https://thenewstack.io/7-llm-risks-and-api-management-strategies/); protect sensitive information and enforce access policies.

## Detection and Response

Cornberg said Eve Security is more narrowly focused than its closest competitors — he pointed to [Lasso Security](https://www.lasso.security/) and [Aim Security](https://www.aim.security/post/aim-to-join-cato-network) (now part of Cato Networks. Rather than going broadly, including the posture side, which involves setting up permissions and policy, it’s drilling down into detection and response. What is the agent allowed to do? Should it be doing this?

[Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk/), Eve Security advisor and CTO at the Cloud Native Computing Foundation, called the new startup “Kind of like the security seatbelt for AI’s self-driving era.”

Co-founder Eilon pointed out that not all risks come from the outside.

“This is anything regulatory, right? It’s sharing information. It’s doing things with this information. Maybe it’s sending an email outwards. Is it supposed to send an email outside of the organization with my name and address? I don’t know,” he said.

“We look at that communication and we see, what’s the intent and what’s there that it’s authorized to do it. If there’s no authorization problem, it can do that activity. No one told it not to do it. But is it right that it should be doing this activity? Someone needs to check. … The world is walking into a very a non-deterministic problem area that we are here to solve.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/01/cabe83e0-susan-mug.jpg)

Susan Hall is the Sponsor Editor for The New Stack. Her job is to help sponsors attain the widest readership possible for their contributed content. She has written for The New Stack since its early days, as well as sites...

Read more from Susan Hall](https://thenewstack.io/author/susanhall/)