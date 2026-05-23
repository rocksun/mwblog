**Enterprise AI is running into a problem.** But it has more to do with data infrastructure than model quality. The snag is that most businesses still keep data fragmented across databases, SaaS tools, warehouses, and internal platforms, with security controls layered on top to protect each surface area separately.

That works fine in a batch world, but it becomes a serious constraint once agents and AI applications have to reason across live business data, [Sean Falconer](https://www.linkedin.com/in/seanf/), head of AI at data streaming platform Confluent, tells *The New Stack.*

“Most AI projects fail before they even reach a single customer because the data layer breaks down,” Falconer says. “Teams have the models and mandate, but security risks and fragmented data stop them from shipping.”

Confluent’s aim is to make real-time data streaming the secure foundation for AI apps and agents, with controls and developer tooling that high-stakes industries need.

> Confluent’s aim is to make real-time data streaming the secure foundation for AI apps and agents, with controls and developer tooling that high-stakes industries need.

So while teams can build convincing demos, they often can’t go beyond POCs. According to [McKinsey](https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/building-the-foundations-for-agentic-ai-at-scale), eight in ten companies cite data limitations as a roadblock to scaling agentic AI. It’s the gap Confluent wants to close with its new [Confluent Intelligence](https://www.confluent.io/blog/2026-q2-confluent-intelligence-update/) and [Confluent Cloud](https://www.confluent.io/blog/2026-q2-confluent-cloud-launch/) capabilities, launched in London on May 19. The aim is to make real-time data streaming the secure foundation for AI apps and agents, with controls and developer tooling that high-stakes industries need.  
  
Plenty of firms built security controls across systems and carved their data into separate swimlanes decades ago. It made sense then, but now it gets in the way of AI. Leaders are faced with an ugly trade-off: over-provision access to agents, stall the projects, or centralize the data and hope performance and control hold up. None of those options is ideal.

## **Why AI needs live context**

For Falconer, one of the biggest bottlenecks isn’t the models, it’s access to current data. “I see a demo like a movie set, with a fake cityscape, where I’ve paid the extras to be in the background,” he says. “Real cities are going to be a lot more complicated and unpredictable.” The hard part comes when a polished demo has to survive real users and real data.  
  
Take an airline that uses a customer support agent to help passengers rebook flights. “Old data could mean putting a customer on a flight that no longer exists, or into a seat that’s already been taken — all of it is bad news,” says Falconer, adding that the whole point is to create a better user experience and a more streamlined process. Real-time accuracy is no longer a nice-to-have for AI systems; it’s the difference between a convincing demo and something that functions in the wild.

> “I’ve got 10,000 hours under my belt, so I have the historical reference on how to drive… But if my camera feed of the road ahead only updates every two hours, how long is it before I crash?”

To deliver on its promises, AI requires two kinds of intelligence: historical pattern recognition and real-time signals. Falconer likens it to driving. “I’ve got 10,000 hours under my belt, so I have the historical reference on how to drive,” he says. “But if my camera feed of the road ahead only updates every two hours, how long is it before I crash?”

The same logic applies to enterprise AI. Companies have spent decades building up historical data and batch systems, but have underinvested in the ability to process what’s happening now. That’s the leap: AI agents need both memory and live context if they’re to make safe operational decisions.

## **Easier, safer streaming**

Confluent wants to help teams move away from hand-crafted plumbing and towards a more guided way of working with streaming systems. The latest additions, including its managed MCP server, agent skills, and dbt adapter, are designed to reduce friction in configuration and setup while democratizing access for developers who aren’t as familiar with, or don’t live in, that environment day-to-day. In practice, that means people can express what they need in natural language, then use familiar workflows to build, manage, and debug streaming operations.

The point isn’t just ease. Falconer argues that when teams have to work around cumbersome setup or opaque tooling, they often end up working around the security model too. By contrast, if the system is opinionated and easier to use, more people are likely to stay inside the approved path. As he puts it, the skills are really “recipes” that capture Confluent’s own best practices, so developers don’t have to reconstruct all that domain knowledge themselves.

It comes with a warning label, though. Falconer is clear that models remain non-deterministic, so the question is also how to keep them controlled. Confluent’s managed MCP server is read-only and maps back to existing RBAC, roles, and credentials. At the same time, the skills layer is more flexible and better suited to staging or development environments than direct production changes.

An important distinction for enterprise teams, which reflects the reality of modern AI development: experimentation is useful, but production still needs determinism. “With production environments, use tools within a staging or deployment environment, and once you know it’s working correctly, use a system like Terraform to push them into production in a repeatable way,” says Falconer.  
  
The same logic applies to data movement. Confluent’s stream processing layer can link to external databases, pull in context for AI, enrich a datastream, or talk to large language models in a customer’s cloud environment — but those connections shouldn’t need to travel over the public internet. When Confluent Cloud is running alongside a customer’s own Azure-hosted systems, communication between those surfaces stays on Microsoft’s private backbone.

That’s key because the enterprise case for AI is increasingly about securely moving context around, not just moving data quickly. Confluent is also pushing privacy deeper into the stack, with built-in PII detection and redaction in Flink SQL, so sensitive data can be handled in the stream rather than routed out to a warehouse first.

## **Real-world proof**

Financial services already run on streams of events — card transactions, login attempts, wire transfers, and ATM activity. “But historically, it’s been difficult to run advanced AI models directly within livestreams in a secure, governed way,” points out Falconer. The usual fallback has been to batch everything into a warehouse and detect fraud later, which means action can come hours or days after the event.  
  
The launch, which includes support for TimesFM, shifts that work closer to the point of data creation, with more adaptive anomaly detection and less model tuning. That way, teams can spot account takeover patterns or abnormal transaction spikes immediately, rather than after costs have already mounted.

Falconer’s broader philosophy is one he learned as head of developer experience at Google: if the tooling is clunky, adoption stalls. He recalls how an API-first business messaging product was powerful, but hard to get started with. A click-through cut onboarding time and lifted the use of advanced features by 3x, while launches doubled. As he says, “make it easy and fun to use, and developers will be safer and more successful.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/e36dae7b-cropped-6c610b3e-megan-carnegie-square-sizing-600x600.jpg)

Megan is a London-based independent technology journalist with over a decade of experience writing analytical features for publications like WIRED, Fast Company, and the BBC. She specializes in the world of work, covering Big Tech, startups, AI, recruitment trends, and...

Read more from Megan Carnegie](https://thenewstack.io/author/megan-carnegie/)