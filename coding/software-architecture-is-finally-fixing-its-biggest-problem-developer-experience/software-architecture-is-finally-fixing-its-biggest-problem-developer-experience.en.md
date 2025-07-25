Architecture discussions often get lost in abstraction — whiteboard sketches that never survive contact with reality, dense documentation that gathers digital dust, and theoretical purity that crumbles under the pressure of practical application. After years of building and rebuilding systems across different scales and industries, I’ve learned that the most successful architectures share one crucial trait: they’re designed like products, not monuments.

My path to this realization started in research. I earned a Ph.D. in Electrical and Computer Engineering from Aristotle University of Thessaloniki, with a focus on optimization and collaborative robotics. My later work explored AI applications in urban traffic management. Since then, I’ve led software efforts across academic and industrial settings, including roles in the automotive industry at Continental, ZF, and Aptiv, and I currently serve as a Software Engineering Manager at Meta, where I work on Integrity systems. Previously, I managed teams at Backbase, a fintech company in Amsterdam, where I built core banking platforms for retail and business customers.

This shift in perspective changes everything. When you treat architecture as a product, you start asking different questions. Instead of “Is this elegant?” you ask, “Does this help people get their work done?” Instead of optimizing for theoretical perfection, you optimize for real-world outcomes.

## Your Architecture Users Extend Far Beyond Engineering Teams

The most [transformative realization in my architectural journey](https://thenewstack.io/counting-on-developers-to-lead-vodafones-transformation-journey/) was understanding who actually interacts with the systems we design. Engineers are obvious users — they need clarity, maintainability, and the confidence to make changes without breaking everything. But they’re just one constituency in a much larger ecosystem.

Product managers rely on architecture to enable rapid iteration and feature deployment without incurring excessive coordination overhead. When they cannot deploy due to three teams that need to coordinate for a trivial update, that’s an architectural problem. Designers and QA engineers require stable, predictable interfaces with clear boundaries and predictable impacts. When a minor UI adjustment becomes backend chaos, the architecture has failed them.

Business stakeholders are interested in speed, price, and scalability. They may never learn the technicalities, but they instantly feel the effect when architecture makes it easier or harder to grow. Customer support teams navigate architectural decisions through the reliability and debuggability of systems by which they shepherd users along.

Recognizing that a larger user base alters the way you make design decisions. Every [design decision is now a question of user experience:](https://thenewstack.io/the-power-of-prototyping-in-user-experience-design/) “Who will this affect, and how will it change their day-to-day work?

## Treating Software Architecture as a Product, Not a Monument

The search for “clean architecture” can be a trap. I’ve seen beautiful systems — perfectly layered, wonderfully abstracted, with pretty class hierarchies — that nobody wanted to maintain. They complied with all the best practices in the book, but somehow made the inconsequential, obscure and simple changes perilous.

Conversely, I’ve worked with so-called “messy” systems that the teams loved because they were able to ship features with confidence, handle edge cases gracefully, and knew what was happening when things went wrong. They traded architectural purity for developer productivity, and it was worth it.

This is not an invitation to discard good design practices. Structure, separation of concerns, and clean interfaces remain essential. However, they should be used for the benefit of the people working with the system, not for their own sake. If architectural choices make work harder instead of easier, something has been wrong, even if the methodology is theoretically sound.

Good architectures tend to be out of sight for those who use them. They provide clear solutions for normal things, reasonable alternatives for abnormal needs, and enough flexibility to expand without requiring total overhauls.

## Measuring Architectural Success Through Developer Productivity Metrics

Most solutions’ dashboards are filled with metrics quantifying user behavior, performance, and business outcomes. Architecture also deserves the same attention to measurement but is instead measured through subjective argument over design aesthetics rather than objective evaluation of effectiveness.

I started tracking architectural health in terms of questions directly related to team productivity: How long does it take to deploy and release a regular feature? How many teams need to coordinate for cross-cutting changes? How often do seemingly unrelated parts of the system affect each other in unknown ways? How confident are engineers when they change essential pieces?

These figures say more than words. When deployment lead time shortens from days to hours, when cross-team dependencies reduce, when production failures occur less frequently and are simpler to debug — these outcomes speak more eloquently of architectural decisions than any design document.

There are times when direct measurement is not possible but the signals are there nonetheless. [Regular discussions with the development teams](https://thenewstack.io/the-impact-of-regular-training-and-timely-security-policy-changes-on-dev-teams/) reveal pain points, bottlenecks, and areas where the architecture is enabling or hindering progress. It is this feedback that forms a critical input in architectural improvement prioritization.

## Building Architecture Roadmaps That Align With Business Goals

Architecture isn’t a one-time decision that gets carved in stone. It’s a living system that either evolves intentionally or degrades accidentally. Like any product, it benefits from deliberate planning and strategic thinking about future needs.

Breaking down architectural planning into three horizons works. “Now” addresses near-term blockers — the architectural debt that currently actively hinders teams. These are typically rapid wins that provide quick relief and build momentum for more significant changes.

“Next” issues are not time-sensitive, but they will hurt if they are not addressed. That might be scaling bottlenecks that will arise as traffic increases, or structural problems that will become more expensive to resolve as the codebase expands.

“Later” is all about placing bets on the future needs wisely. This is where you’re betting on flexibility for subsequent changes in size, scope, or direction of business. These are riskier bets, but they can reap huge rewards when you get it right.

The wise choice would be to align architectural roadmaps with product and business roadmaps. When architectural improvements have a high degree of correlation with business objectives — such as faster feature delivery, improved reliability, and reduced operational costs — they’re easier to prioritize and justify.

## Measuring Architectural Success Through Developer Productivity Metrics

The most stunning architecture is nothing if teams don’t adopt it. I’ve seen too many handsomely built systems gather dust as teams develop workarounds or replicate implementations because the “official” solution didn’t fit for them.

Successful adoption of architecture is about treating internal teams like external customers. That means sending out early drafts to obtain feedback rather than final conclusions, intentionally soliciting ideas on pain points and areas for improvement, and maintaining records that reflect reality rather than expressing wishes.

Tracking adoption metrics — which teams are using new patterns, where old approaches persist, what workarounds are being created — provides crucial feedback about whether architectural changes are actually solving problems or just making new ones.

Adoption metrics monitoring — which groups are adopting new patterns, where they still employ older approaches, what workarounds they’re applying — provides valuable feedback on whether architectural changes are actually solving problems or merely creating new ones.

## The Human Factor: How Good Architecture Reduces Cognitive Load

Last but not least, architecture is about working together to build software. Technical soundness is necessary, but so too are communication, understanding, and trust. Excellent architectures minimize cognitive load, eliminate coordination overhead, and enable practical reasoning about complex systems using simple, yet understandable, mental models.

This human factor influences everything, from naming schemes to service boundaries and deployment procedures. When architecture conflicts with the way teams want to work, friction is inevitable. When it augments and accelerates natural flows, productivity takes off.

Good architecture does not simply organize code — it organizes teams, reduces stress, and creates an environment in which people can focus on solving business problems rather than fighting technical obstacles.

## Building Architecture Roadmaps That Align With Business Goals

Architecture is only valuable when it stops being a constraint and becomes an empowerment. That happens when you apply the same discipline and user-focused approach that you would to any good product to architectural decisions.

Start with knowing your users — all of them, not just the engineers. Track the outcomes that matter most to your business. Create changes strategically, tying technical alterations to business value. Focus on adoption and real-world use rather than theoretical perfection.

When the architecture is good, it’s just about invisible. [Teams ship features faster](https://thenewstack.io/think-like-a-developer-to-help-dev-teams-ship-faster/), systems scale more beautifully, and problems are easier to understand and fix. That’s when architecture stops being a piece of work around which teams flex and becomes something that multiplies the effectiveness of teams.

The most lavish praise an architect can get isn’t for beautiful design, but instead, it’s teams complimenting them by saying the system simply works the way they expect it to. That’s product architecture, and that’s architecture that counts.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/07/c8582754-a8bf0096c796-converted_image__1_-2-600x600.jpeg)

Avraam Tolmidis is a Software Engineering Manager at Meta, where he leads teams working on Integrity systems. He holds a Ph.D. in Electrical and Computer Engineering from Aristotle University of Thessaloniki, with research focused on optimization and collaborative robotics, and...

Read more from Avraam Tolmidis](https://thenewstack.io/author/avraam-tolmidis/)