![Neon arcade scene](https://cdn.thenewstack.io/media/2026/11/0fa0b84a-risky-ming-6qywiwfpzmu-unsplash-1024x698.jpg)

**An Anthropic engineer gave Claude Fable 5.2 one prompt to build** a first-person shooter and let it run for eight hours without human feedback. By the end, the model had processed 445 million input tokens, generated 2.7 million output tokens, and produced a playable browser game at an estimated API cost of $550.

The result was *[Saltline](https://claude.ai/artifact/BGY1SztrAYcJQHSsnHHGmp),* a shooter set in a rain-soaked shipping port where players battle drones and robotic dogs while disabling communications relays. Anthropic engineer [Felix Rieseberg](https://www.linkedin.com/in/felixrieseberg/) shared the game when Fable 5.2 launched on Monday, describing it as an experiment in how much the model could accomplish from one instruction.

The engineer says Fable generated the game’s visuals procedurally rather than relying on imported assets. A [public mirror](https://github.com/realcodebear/saltline-fable-5.2) packages the game into a roughly 1.4MB HTML file containing bundled Three.js code.

According to a note on the game’s title screen, Rieseberg spent about two hours improving the weapon models, sounds, and gameplay, while preserving a link to the original one-shot version.

## The real price tag

YouTuber [Matthew Berman](https://www.linkedin.com/in/matthewberman/) took the experiment further, asking Fable to recreate a level from *Gears of War: E-Day* in Unreal Engine 5 using just three lines of instructions. The result was a playable shooter where players could take cover, fight enemies alongside AI teammates, and reload their weapons using the game’s signature active reload mechanic.

Berman reports that the project consumed approximately 8.5 billion tokens over several days, with an estimated API-equivalent cost approaching $15,000.

His [browser-based Excel clone](https://claude.ai/artifact/NPxoR5gnxVVsXnyPAkKpYS), complete with ribbon tabs, formulas, and pivot tables, required nearly 50 hours and an estimated $11,700.

Berman had early access to the model, so the figure does not necessarily reflect what he paid, but it is a good indication of the computational resources involved in [running agents for extended periods](https://thenewstack.io/ai-coding-tools-in-2025-welcome-to-the-agentic-cli-era/).

## Not Fable alone

Not every game credited to Fable was built with Fable alone. Creative developer [Kevin Ngo](https://kevintngo.com/) writes, “Claude Fable 5.2 made this game demo, playable in the browser. It’s a boat ride through 8 dreamlike worlds,” about his project *[What the Water Keeps](https://x.com/kevin_t_ngo/status/2119868968307695818)*.

Ngo used Tripo to generate 3D assets and Suno v6 for the game’s soundtrack, while Fable composed the trailer music using royalty-free instrument samples.

[Matt Shumer](https://www.linkedin.com/in/mattshumer/), co-founder of HyperWrite, spent considerably more time [experimenting with the model](https://somethingbig.ai/fable-5-2-review). He used Fable to build a browser-based voxel destruction engine with physics-based damage before moving on to a much larger project of an unfinished simulation of Earth with real locations, weather, and transportation systems.

> “It nailed the voxel engine I’ve been trying to get out of almost every model for a year,”

“It nailed the voxel engine I’ve been trying to get out of almost every model for a year,” Shumer writes on his blog, adding that Fable built it from scratch and that it ran on his MacBook.

His Hogwarts-meets-Fortnite battle royale reportedly took roughly two weeks to develop. Shumer initially experimented with multiple agents but found that a single agent produced better results with little intervention.

“It works best as one agent that owns a whole project,” he says, although he acknowledges that the approach could be frustratingly slow.

Shumer says Fable still needs direction, particularly when it makes projects more complicated than necessary. “You still have to steer it. Framing the problem and keeping it on track with your goals is on you.”

> “You still have to steer it. Framing the problem and keeping it on track with your goals is on you.”

Shumer hosts his demos on [Spawn](https://www.spawn.co/@mattshumer/earth), a platform he also lists among his investments. He doesn’t mention that connection in his review, and it’s unclear whether Spawn provided anything beyond hosting the finished projects.

## The token math

Fable 5.2 costs $8 per million input tokens and $40 per million output tokens, but those prices don’t tell the whole story when an agent runs for hours.

Rieseberg says much of *Saltline*‘s 445 million input tokens came from cached context, which Anthropic charges less to process. Without caching, those input tokens alone would have cost approximately $3,560, compared with his estimated $550 for the entire run.

There’s also the developer’s time to consider. Someone still has to decide what to build, review the code, and fix whatever doesn’t work. Shumer, for example, had to rethink his approach when running multiple agents produced disappointing results, while Ngo used separate tools to create assets for his game.

## From demo to product

The demos leave plenty of questions about [what happens after the first working build](https://thenewstack.io/the-hidden-engineering-cost-of-ai-everywhere-product-roadmaps/). Another developer still needs to understand the code, modify features without breaking existing functionality, and track down performance problems. Berman’s spreadsheet faces its own challenges, since working formulas in a demo don’t guarantee accurate results across larger datasets or more complicated calculations.

The demos also raise the question of what they’re based on. The most striking builds recreate games that already exist, with Berman cloning a level of *Gears of War: E-Day*, a current entry in Microsoft’s shooter franchise, and Shumer borrowing from both the Wizarding World and *Fortnite* for his battle royale.

> “It’s a great model, a LOT of things got better but not every single thing,”

[Peter Gostev](https://www.linkedin.com/in/peter-gostev/), who works on AI evaluation at Arena, has tested dozens of prompts and come away impressed, though he isn’t ready to abandon Opus. “It’s a great model, a LOT of things got better but not every single thing,” he [writes on X](https://x.com/petergostev/status/2119873616170881192), noting that one experiment cost $2,618.

*Saltline* and Berman’s projects show that developers can now [hand off substantial implementation work](https://thenewstack.io/agentic-ides-next-frontier-in-intelligent-coding/) and return hours later to something playable or functional. The cost of that work is becoming easier to measure, but the quality of what comes back still needs human judgment.

The post [Anthropic’s Claude Fable 5.2 built a shooter in 1 prompt — and it only took 8 hours and $550](https://thenewstack.io/claude-fable-game-demos/) appeared first on [The New Stack](https://thenewstack.io).