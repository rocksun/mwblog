Over the last year or so, we’ve seen a proliferation of frameworks and protocols for agentic AI tools.

There is Agent-2-Agent (A2A) for agents to talk to each other, the Agentic Commerce Protocol (ACP) and Agent Payments Protocol (AP2) for agents to talk to commerce systems, and, of course, the Model Context Protocol (MCP) for agents to talk to tools and bring in context. There’s no end to the acronyms.

What’s missing in all of this, however, is a framework that helps agents communicate with humans — or at least that’s what cloud communications company [Twilio](https://www.twilio.com/en-us) argues.

The company on Thursday released the [open-source Agent-2-Human](https://www.twilio.com/en-us/blog/products/introducing-a2h-agent-to-human-communication-protocol) (A2H) protocol, which is designed to help agents manage the handoff from autonomously working on a task to bringing a human into the loop — and do so over the right channel.

> “The agent focuses on what it needs from the human, not how to reach them… and in the process, the system also keeps track of all of these interactions and creates an audit trail.”

“The agent focuses on what it needs from the human, not how to reach them,” as Twilio’s Rikki Singh, the company’s VP of product and engineering for emerging technology, succinctly puts it in the announcement. And in the process, the system also keeps track of all of these interactions and creates an audit trail.

## Keeping humans in the loop

In an exclusive interview with *The New Stack*, Singh says that while agents are becoming increasingly autonomous, you will always need a human in the loop.

“Not because the AI is inefficient, but because there is an element of human judgment that informs a lot of decisions we make, and there is an element of trust that comes with that human judgment,” she says.

The question then becomes about what that escalation route looks like. Twilio has long managed how businesses interact with consumers, whether that’s over text messaging, messaging apps, or voice calls, and Rikki believes that this puts the company in a unique position to address this question.

![](https://cdn.thenewstack.io/media/2026/02/21aeb56d-a2h-diagram-twilio.png)

“I think what we want to solve for is take away the liability — the liability around thinking about, hey, I should have thought about an escalation path. I should have thought about this. It shouldn’t rest on the developer or the consumer, right? It should rest on the tool. It should rest on the technology,” she says.

> “Not because the AI is inefficient, but because there is an element of human judgment that informs a lot of decisions we make, and there is an element of trust that comes with that human judgment.”

The developer should not have to figure out how the agent can reach the human and maintain all the necessary integrations across channels like SMS, WhatsApp, push notifications, or voice.

A2H ideally abstracts all of this away, and the agent just sends its message to an A2H Gateway, which then handles the messaging part of the escalation.

## Intents

Based on the company’s experience in bringing together businesses and consumer, A2H enables five core intents (though it is extensible, of course): inform (for one-way notifications), collect (for gathering structured information like a shipping address), authorize (for approving transactions with authentication), escalate (to hand off to a human) and result (for reporting task completion).

Given the use case, even this first A2H case also focuses on security. Every interaction through the gateway produces a signed artifact. This means that when a human approves a transaction, for example, this is clear evidence that the agent asked for and received consent. As Singh notes, that’s also why a gateway is critical, because there has to be an enforceable set of rules that ensure that the agent asks for approval for certain transactions, for example, and that there is a record of those.

“The lens we took is that anytime you have an agent trying to communicate with a human, the reality is there is an implicit intent,” Singh says. “We realized that’s the best way to help not just developers but also consumers who may eventually be running their own semi-autonomous agents to understand how to frame these conversations. And so that’s why we took the intent approach.”

The default intents are only a baseline, however. The overall framework is extensible.

![](https://cdn.thenewstack.io/media/2026/02/c263073d-a2h-code-twilio.png)

For agents who use MCP, A2H simply becomes another tool, and they can use the same tool-calling patterns (think `humans_inform()`).

## What’s next?

With Thursday’s announcement, Twilio is open sourcing the the first version of the A2H spec, which focuses on the intents, including authentication support, and delivery channel abstraction. Coming soon are integrations with more agent frameworks like LangGraph and CrewAI, additional primitives for creating standing approvals (and cancelling them).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)