AI is the epitome of moving fast and breaking things. But where has the rigor gone, asks Thoughtworks CTO [Rachel Laycock](https://www.linkedin.com/in/rachellaycock/). Where are the guardrails?

AI may be dubbed the great disruptor, but it’s really just an accelerator of whatever you already have. The 2025 DORA report places [AI’s primary role in software development as that of an amplifier](https://dora.dev/research/2025/) — a funhouse mirror that reflects back the good, bad, and ugly of your whole pipeline. AI is proven to be impactful on the individual developer’s work and on the speed of writing code. But, since [writing code was never the bottleneck](https://leaddev.com/velocity/writing-code-was-never-the-bottleneck), if traditional software delivery best practices aren’t already in place, this velocity multiplier becomes a debt accelerator.

> “AI is proven impactful on the individual developer’s work… but, since writing code was never the bottleneck… this velocity multiplier becomes a debt accelerator.”

“Sure, you can get an agent or a swarm of agents to build lots of software for you, but is that software secure? Is it optimized for cost? Does it do exactly what you expected to? Does it have any unexpected behaviors or consequences?” asks Laycock, worrying that tech workers are overlooking the cross-cutting concerns of AI.

“Building an app is easy. It’s always been easy if you’re a coder. Now it’s easy if you’re not a coder. But an app is not distributed, complex business software.”

A generation ago, a small group of technologists gathered in the mountains of Utah to develop the Agile Manifesto. This February, one of its most famous signatories, Martin Fowler, the team at Thoughtworks, and enterprise engineering leadership returned to that mountain to respond to the next seismic shift of [AI-native development](https://thenewstack.io/ai/).

In a recent interview with *The New Stack*, Laycock reflected on this meeting of technical minds amid a surge in software development. Hint: it was never just about the tech.

## **AI drives an influx of noobs**

The software industry has always been gatekeeping, so it should be a good thing that AI is allowing more people to participate in shaping our future. But if we’re not careful, elitism and protectionism will ignite a ticking time bomb.

“People are leaning into: Oh, I need more senior engineers than I do juniors. That’s a different problem because you have to create engineers over time,” Laycock says, not abiding by some companies’ tactic of using AI to replace [junior engineers](https://thenewstack.io/advice-for-people-still-entering-the-tech-industry-in-2026/).

“Instead of being like: Hey, they don’t know what they’re doing, stop it. We should think about: How can we become good stewards? [How do we have empathy?](https://thenewstack.io/do-you-have-the-empathy-to-make-the-move-to-architect/) How do we help them learn? What can we do to explain to them why and to build better guardrails for these systems?”

As it always has, what distinguishes a high-performing team from a low-performing one is the adoption of DevOps, microservices, and continuous integration and continuous delivery best practices, alongside guardrails, security, testing, automation, version control, observability, progressive delivery and rollbacks, and more.

> “Instead of being like: Hey, they don’t know what they’re doing, stop it. We should think about: How can we become good stewards? How do we have empathy? How do we help them learn?”

“Software that’s well-written, that’s well-architected. This is why modular systems exist: they make it easier for humans to understand and for us to change and adapt. We kept coming back to why the fundamentals of software engineering are so important,” Laycock reflects on the Thoughtworks unconference. “We’re moving up a layer of abstraction where we are not yet trusting that the agents are going to do what we expect them to because we’re seeing that they’re making mistakes that get made when you’re an immature developer.”

It’s not a problem that AI is allowing more people to participate in creating our future, but, she says, guardrails exist for a reason, and especially now cannot be ignored.

“Whether it’s your CI/CD pipeline, whether it’s your fitness functions that tell you that it’s performing as you expect it to, that the costs are as you expect them to be,” Laycock says. “So when software comes at a higher level of abstraction — like with Java — we had a whole new group of people come into the industry who had to learn all the hard lessons of distributed systems.”

More and more people will be entering our industry without the inherent knowledge of what it takes to build complex, distributed systems, which is nothing new, as universities and bootcamps have always leaned too far into Greenfield builds.

“Us as senior technologists in the industry. Instead of complaining about that — ‘Oh, these people don’t know what they’re doing’ — we should be the people’s stewards,” Laycock says. “Because we do know why these things matter.”

This does require senior architects to show empathy and patience to newcomers, including subject matter experts who weren’t raised in the tech industry but can bring significant value to your target users.

“We don’t talk about the why. We just have this assumption: Of course, you have to care about that thing because we’ve learned that,” she warns, “but people who are coming new into the industry and are able to now build software too, they haven’t learned these lessons.”

## **Lost in agentic translation**

Are the current popular programming languages supporting AI and these best practices? The industry is on the cusp of reconsidering programming languages.

Languages currently exist for native English speakers to read, but code must now be optimized for both humans and AI agents, or perhaps for agent-specific languages. We may soon see an increase in languages that support a more structured approach.

“We might see new types of languages, maybe very heavily typed languages, that lean more into having a structured approach to programming,” Laycock says, referring to the unconference participants’ debate. “There was also this concept of, do we even care about the code anymore? Obviously, we care about the rigor and the architectural principles around it, and about testing that it’s built in a certain way. But how much fiddling with the code are we actually going to do in the future?”

As the need for humans to read code fades, programming languages will likely become more efficient, making them easier for AI agents to read than for humans.

“Are things that are good for humans good for agents?” Laycock continues that “If it’s well-explainable, well-tested, that’s good for both sides. I think there’s going to be a divergence, potentially, of some people being like: Let’s do it in the most human-readable way, and then others being like: Let’s start building software in a different way that’s maybe just for agents.”

There’s also an argument that the way we develop will completely change. Simon Wardley and Tudor Girba advocate that [moldable development](https://moldabledevelopment.com/) will bring a contextual approach—think programming via [Wardley maps](https://thenewstack.io/simon-wardley-on-mapping-our-way-to-a-common-language/)—to software decision-making. The signees of the [Outcome Engineering Manifesto](https://o16g.com/) agree with them that it was never about the code. O16g, as it’s abbreviated, prioritizes desired business results and measurable user impact over software delivery.

Thoughtworks has even launched its own product, the [AI/works agentic development platform,](https://www.thoughtworks.com/ai/works) which leverages AI and domain-driven design to map out the business capabilities enterprises need to modernize — a requirement now more than ever, given the modularity and scale of AI.

“There is a lot of software already in the world that we don’t understand,” Laycock remarks, which can only increase with the agents creating software. Laycock adds, “not all software is created equal from a risk and a business value perspective.”

No one came out of the retreat calling for AI agents to replace humans anytime soon. But there are areas that call for more humans in the loop.

With this will guide where enterprises will allow for more code generation and agentic healing, versus, she continues, “there’ll be other software, which is extremely high business value, high-impact, customer facing, where we want more humans in there, where we want the software to be more human-readable, more modularized, well-understood, strong guardrails, strong ability to do incident response.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)