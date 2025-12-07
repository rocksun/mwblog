Most of the conversation around AI agents today revolves around bots writing code. This didn’t come out of nowhere; Software engineering is [the most common use case](https://www.anthropic.com/news/the-anthropic-economic-index) for AI systems, and code-writing tools are [reaching eye-popping valuations](https://www.reuters.com/business/ai-vibe-coding-startups-burst-onto-scene-with-sky-high-valuations-2025-06-03/). But inside companies, something more fundamental is shifting: [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) are becoming internal “operating systems” that connect and orchestrate data flows between software tools, changing the way we all work, not just the engineers.

At Block, our engineers built an AI agent framework called goose and released it as an open source tool for anyone to use with any large language model. Initially designed for writing code, we quickly realized that for goose to reach its full potential, it needed a standard way to communicate with the dozens of tools that people use daily. Recognizing this same challenge, Anthropic was developing what would become the [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/). We began collaborating early in MCP’s development to help shape this open standard that bridges AI agents with real-world tools and data.

Today, 60% of our workforce — around 6,000 employees — use goose weekly. It serves as a central conductor, reading and synthesising data across dozens of MCP-powered extensions including Slack, Google Drive, [Snowflake](https://www.snowflake.com/?utm_content=inline+mention), Databricks, Jira and others. Just months ago, it would take days of manual labor to read Snowflake dashboards, pull context from recent Slack chatter and generate a weekly Google Doc with insights and flagged anomalies. Now humans orchestrate this process in minutes, directing goose to the relevant data while applying judgment about what matters most.

Unlike the headlines, this isn’t a story about AI replacing jobs. At Block, we believe the shift is about redistributing access to problem-solving.

## **The Compression Effect: Becoming More Self-Sufficient**

Most companies rely on handoffs. A product manager submits a ticket. An engineer builds it. A support team flags a recurring issue. A developer scripts a fix. These workflows protect quality, but they slow things down. AI agents like goose are collapsing that distance by helping people take action on their own instead of waiting on others.

Take customer support escalations. In the past, when a support agent noticed an unusual spike in refunds, they would file an escalation ticket and wait three to five days for the data team to pull transaction analysis, receive raw spreadsheets, manually create a summary and post findings to Zendesk. Now that same agent asks goose to “analyse the last 30 days of refund spikes” and within 30 seconds receives a complete analysis with patterns identified and an automatically generated Zendesk-ready summary.

By allowing users to choose a preferred model and by connecting to internal tools, goose enables teams to move from idea to prototype without waiting in a queue. A support [agent can surface a dashboard](https://thenewstack.io/goodbye-dashboards-agents-deliver-answers-not-just-reports/). A security analyst can write a detection rule. A designer can test live functionality based on user feedback. None of this requires code expertise.

This kind of access was previously off-limits to most employees. That’s starting to change.

## **What’s Next: Building Guardrails and Resilience**

Goose is part of a wider shift within Block and at other forward-thinking companies: recognising that AI’s most valuable role may not just be in what it builds for users, but in what it unlocks for teams. By lowering the barrier to experimentation, internal AI tools are giving people the confidence to test, iterate and solve problems themselves.

This doesn’t remove the need for engineers. If anything, it strengthens their impact. It clears the backlog. It reduces bottlenecks. And it makes the space for more complex, strategic work to get done.

As with any new expansion of capabilities like this, this type of transformation requires careful design. At Block, we’ve implemented specific policies that govern how these AI connections work across our company. Any tool that handles sensitive information requires legal approval before it can be deployed. We maintain curated lists of approved extensions, so employees can only install tools that have passed our security review. And we’ve built smart boundaries directly into the tools themselves. Some automatically avoid accessing confidential databases, while others separate what users can read versus what they can modify. These aren’t bureaucratic barriers; they’re design choices that let teams move fast while keeping important information secure.

The long-term opportunity isn’t just speed or cost savings. It’s resilience. [Companies that embrace](https://thenewstack.io/companies-must-embrace-bespoke-ai-designed-for-it-workflows/) this shift will be less dependent on rigid workflows and more responsive to the people closest to the problem. They’ll be able to move faster without compromising safety, and solve at the edge without losing control at the core.

That’s what we’re learning with goose. And that’s the direction we believe enterprise AI is headed. It may not make headlines, but it’s changing the way organizations function at their core.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/12/fa126603-cropped-d76d88fe-angie-jones-scaled-1-600x600.jpeg)

Angie Jones is vice president of Engineering, AI Tools & Enablement at Block. She is an award-winning teacher and international keynote speaker who shares her knowledge at software companies and conferences all over the world. As a Master Inventor, Angie...

Read more from Angie Jones](https://thenewstack.io/author/angie-jones/)