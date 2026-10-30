**Google DeepMind introduced Genie 4 on Tuesday**, a world model that renders interactive environments in real time with simulated physics, human motion, and native audio. The photorealistic demos are seriously impressive, but arguably the real draw for anyone [building AI agents](https://thenewstack.io/ramp-laminar-agent-harness/) is that Genie 4 gives them somewhere to run multi-step tasks before it counts.

[Tejas Kulkarni](https://www.linkedin.com/in/tejas-kulkarni-56042214/), a research director at Google DeepMind, describes the approach at a [press briefing](https://techcrunch.com/2026/10/27/googles-genie-4-world-model-adds-audio-more-realistic-worlds-and-real-time-steering/) as a move toward “these hybrid world models,” with Gemini writing the code and text and Genie turning it into a running scene. It gives developers a way to generate test environments on demand, although how closely those simulations reflect real-world conditions remains an open question about [reliability](https://thenewstack.io/liquid-ai-reward-hacking/).

> It gives developers a way to generate test environments on demand.

## How Gemini steers Genie 4

[Genie 4](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) uses several Gemini models to keep its simulations running. [Gemini Omni](https://deepmind.google/models/gemini-omni/) helps shape the environment, while Gemini 3.8 Flash follows what’s happening, plans the next steps and adjusts when something changes.

Instead of producing a finished video, Genie 4 lets users interact with the world as it’s generated. They can move through it with a keyboard, change the camera angle or use text prompts to alter the environment without restarting the simulation.

> Instead of producing a finished video, Genie 4 lets users interact with the world as it’s generated.

## Rehearsing robots in simulation

Google’s clearest example puts Apptronik’s Apollo humanoid through a [game of checkers](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/), with Gemini 4 Argon planning each move and Genie 4 rendering the results as captions steer the scene.

The company is also exploring how the technology could support its [Gemini Robotics](https://deepmind.google/models/gemini-robotics/) research, which gives developers the ability to test agents in changing environments without having to rebuild each simulation from scratch.

## Where the physics breaks down

The catch is that Genie 4 can’t always keep those environments consistent. Objects can shift position or behave unpredictably during longer sessions, and Google acknowledges that the physics isn’t always accurate.

That complicates agent evaluations, particularly when tasks involve [remembering locations or returning to earlier states](https://thenewstack.io/letta-frontiermemory-agent-harness-benchmark/). A failed run could reflect a problem with the agent or the simulation itself, and Google hasn’t demonstrated that Genie 4 can replace traditional physics engines in high-stakes testing.

Game developers are using Genie 4 to explore prototypes and test game mechanics before writing engine code, while enterprise partners are looking at ways to generate their own testing scenarios.

> The company hasn’t published benchmarks showing how Genie 4 performs across repeated agent tests.

The company hasn’t published benchmarks showing how Genie 4 performs across repeated agent tests. This includes whether the same prompt produces consistent results, leaving leaves developers with little to go on when deciding whether to use it in automated testing.

## Who gets Genie 4 access

For now, only trusted testers have access. Google plans to expand availability to Google AI Ultra subscribers through Project Genie and select partners through the Gemini API and Google AI Studio. There’s no word yet on pricing, a wider release or performance guarantees.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)