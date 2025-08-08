If APIs were the connective tissue between different websites and apps during the Web 2.0 era, then AI agents are shaping up to be the same thing in the AI era. In other words, AI agents will increasingly be how you access and use data from various sources around the internet. APIs aren’t going away, but AI agents have stolen their thunder.

Managing AI agents is the new API management — that’s essentially the bet that [Oren Michels](https://www.linkedin.com/in/omichels/), CEO of new AI company Barndoor, is making. Michels was previously founder of Mashery, an API management company he led from 2006 through to its acquisition by Intel in 2013.

Michels doesn’t shy away from the comparison. “If you take APIs and you take the ‘P’ out, it’s a whole lot more interesting,” he joked at the beginning of our conversation.

[![Barndoor homepage](https://cdn.thenewstack.io/media/2025/08/7066d934-barndoor-homepage-aug2025.png)](https://cdn.thenewstack.io/media/2025/08/7066d934-barndoor-homepage-aug2025.png)

Barndoor homepage

[Barndoor](https://barndoor.ai/) describes itself as “the control plane for agentic AI.” Just as Mashery helped companies get APIs under control, the goal of Barndoor is to help enterprise companies tame and put guardrails around agents.

Michels doesn’t think the current solutions for managing AI agents are sufficient. He says the existing IAM (Identity and Access Management) and API management companies haven’t fully solved it. “If those solutions were adequate, we would see a lot more penetration of agentic AI in the enterprise,” he said. “And we don’t see it, because I don’t believe those solutions are adequate.”

He made another parallel to the Mashery days.

“In the same way that you could have said back in the day that, well, Cisco is managing traffic, so they must be doing API Management? Well, of course, they *weren’t* doing API Management. That was why we got to exist; and other companies did as well.”

## Target Users and Use Cases

So who are the people who will be using Barndoor? According to Michels, it’s not necessarily the CIO or security staff. Their job isn’t to use AI (even though it’s hard *not* to use AI, these days). But those people don’t have an “AI problem,” as Michels put it. Once again, it’s similar to the old API days.

“The person that had an API problem was the person at Marriott whose job it was to make hotel room bookings go on a mobile app,” said Michels. In the AI era, the people who have an AI problem “are the people whose job it is to sell stuff and need to do so faster and more efficiently, and use AI to do that.”

Barndoor has already been launched, although because it’s so new there is a waiting list. Since we don’t know Barndoor’s early clients, I asked Michels what are some of the early use cases he’s seeing?

“The use cases really are around agentic workflows that need to interact with various tools,” he replied.

He compared agents to a “robot workforce” and noted that they need the same identity management for tool access as your human workforce.

“They [the human workforce] get access to Salesforce or Notion and a bunch of other things they might do — Gmail, things they use to do their jobs — and they use those tools, do their job, and maybe create some work product. And the customers we’re working with want their agentic tools to be able to do that as well.”

> “If you’re going to let agents have access to [enterprise] tools, you kind of have to start small.”  
> **– Oren Michels, Barndoor CEO**

If it was just about access to tools, that would be a simple solution. But of course there’s more to it.

“If you’re going to let agents have access to these tools, you kind of have to start small,” Michels said. “You have to start and be very deliberate and very modest about limiting the blast radius that these agents have, so that you can sort of see what they’re doing, see what they’re trying to do.”

## MCP: The New REST?

Given that [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) are still very new — albeit very hyped — I wondered what kinds of tools his early enterprise customers want AI agents to be using?

Michels replied that “the first batch of this kind of resembles RPA on steroids.” (I had to look up RPA later: Google’s AI told me that it stands for “Robotic Process Automation” and that it’s “revolutionizing enterprise IT by automating repetitive, rule-based tasks, freeing up IT staff for more strategic work.”)

However, what the Barndoor team has found so far is that the RPA use cases don’t have much value, “because just doing what humans do a little faster isn’t really all that interesting.” But the latest use cases, involving [Model Context Protocol](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP), are more interesting, according to Michels.

He likens MCP to REST (Representational State Transfer) in the API days; REST became the most popular architectural style for APIs in the 2000s.

> “…you get access to an API, you turn it into an MCP server, and then you give your AI access to it.”  
> **– Michels**

“It’s a more effective, faster means of computers to talk to computers, to actually get things done,” he said, about MCP. “And so I think that the parallels [to APIs] are certainly real, especially since part of what you generally do if you want to use MCPs, you get access to an API, you turn it into an MCP server, and then you give your AI access to it.”

In terms of how that actually works, Barndoor acts as a proxy to the MCP server, Michels explained. Once again, there are parallels with API management.

“In the API world, there’s sort of an OAuth workflow that people use to say: I’m here, I have a key to use this API, and I also am allowed to use that data. And in the MCP world, or at least the way we do it, there’s a similar concept, [where] we basically are able to say: okay, we have this agent which has been authorized, we have this human and because the human is tied to an identity that they get from the Identity Access Management system — that we connect to and collaborate with — we are aware of that, and then there’s a flow.”

So Barndoor essentially coordinates the workflow between human workers and agents.

## As Big as SaaS

In one of the [launch posts](https://barndoor.ai/ai-sprawl-competitive-advantage/) for Barndoor in May, Michels wrote: “We expect the agentic AI market to evolve similarly to the SaaS [software as a service] market.” I asked him if he also thinks the agentic AI market will get as big as the SaaS market (which, needless to say, is massive)?

“Oh yeah,” he replied enthusiastically, adding that agentic AI will also probably supplant SaaS products in certain categories. He didn’t specifically mention any by name, but I would think certain customer service SaaS tools are at risk.

But for other categories of SaaS, where human workers still need to be in control, those products will co-exist with agentic AI.

“Remember that we are humans; we use these tools,” Michels said. “The AI supplants [some of] what we do and gives us these superpowers to do a lot more faster. But ultimately, we do need to keep track of our customers, we do need a source of record, we do need one truth that an organization has and everybody has access to.”

In other words, SaaS tools like Salesforce, Notion and Gmail aren’t going to be supplanted by agentic AI. Although they will, as Michels had pointed out earlier in this story, increasingly be used by agents *as well as* humans.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)