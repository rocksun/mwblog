Enterprises are experiencing FOMO and rushing to deploy AI-based services and AI agents, but for the teams that are responsible for keeping those systems running in production, the patterns that are forming are starting to feel familiar: Silos are forming between data scientists and operations teams, just as they did years ago between developers and ops. But there is hope.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

“Every service out there — let’s take [AWS](https://aws.amazon.com/?utm_content=inline+mention) Bedrock and SageMaker — they’re supporting OpenTelemetry, which is great,” said [Thanos Matzanas](https://www.linkedin.com/in/thanosmatzanas/), an observability expert at IBM. “For the first time, we all agreed that this is the way to go.”

In this episode of The New Stack Makers, recorded at AWS re:Invent 2025, I sat down with Matzanas and his IBM colleague [Martin Fuentes](https://www.linkedin.com/in/fuentesmartin/) to discuss why AI observability is still an afterthought, what enterprises can learn from past platform shifts, and why breaking down organizational silos may be more important than any new monitoring tool.

## The Silo Problem Returns

The challenge isn’t new technology, it’s old organizational patterns repeating themselves, Matzanas and Fuentes argued. Not too long ago, data teams worked in isolation on models that often only served internal purposes. Now, they are suddenly responsible for customer-facing applications with real revenue implications.

“It’s the first time they come into the mix,” Matzanas explained. “Usually, they were doing their own thing on the side, and now they’re coming into the mix because they’re actually serving real clients, not internal clients, real clients with real revenue. And now they feel the same pressure, I think that all the other teams were feeling in the past.”

Fuentes sees a similar dynamic. The AIOps and site reliability engineering (SRE) community spent years building observability best practices, and many of them are transferable to this current moment, but “we still need to figure out how to measure that business value attached to the models,” he said.

## Don’t Forget the Basics

When asked what advice they’d give to enterprises just starting their AI journey, Matzanas argued that it all comes down to going back to the basics.

“Don’t forget the basics. This is nothing different from any other technology stack,” he said. “What are your metrics? What are your KPIs, what are your [service-level objectives]? How do you monitor the services around your AI applications? How do you monitor your vector databases? How do you monitor your APIs? If you cover all the basics, then when the AI comes in, you have a good bedrock to build on.”

The challenge, though, is that AI models are different because they are not deterministic. Traditional user experience monitoring worked because you could trace a request from the user interface all the way to the infrastructure. With AI, much of the feedback loop depends on humans.

“We rely a lot on user feedback to understand what’s going on,” Matzanas said. “And it’s very difficult to determine the quality of the interaction.”

## Security and Compliance by Design

This means that putting in guardrails is especially important for getting models into production, but Fuentes emphasized that AI workloads require the same governance rigor as traditional applications — and perhaps more. “It’s not only about trusting the result of an inference from a model, but also the concerns about how the data is used to train the models,” he said.

This, too, is about going back to existing tools like role-based access control (RBAC), audit logs, and properly documenting how models and agents have been trained to avoid bias. “There are many things that we learned are important for traditional workloads, and there is no reason why not to apply them in AI.”

## Low-Hanging Fruit: Get People in the Same Room

Asked about where to start, both pointed to the importance of managing organizational change rather than solely focusing on technology adoption.

“Break the silos as soon as possible,” Matzanas said. “We know how, because we’ve done it in the past. Include your data people in the conversation. Show them how it looks in production. Don’t keep them siloed on one side.”

Fuentes offered a complementary perspective: Find the business value first.

“If you want your leadership to buy in and give you the resources to apply generative AI [GenAI] models or agents in your application, it needs to be something that will provide business value eventually,” he said. “Talk with your users about what problems you can resolve where generative AI can be a good solution.”

## Will AI Replace Observability Teams?

Both pushed back against the notion that AI will eliminate human roles in observability — at least for critical systems.

“Because of the criticality of observability in many cases — imagine if you’re monitoring a healthcare application — are you going to ever leave that in the hands of AI?” Matzanas said. “There’s no way. I don’t see any pilots losing their jobs anytime soon.”

Fuentes was similarly optimistic. “AI will very likely not actually replace humans on top. It’s just something else that we can use to increase productivity,” he said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)