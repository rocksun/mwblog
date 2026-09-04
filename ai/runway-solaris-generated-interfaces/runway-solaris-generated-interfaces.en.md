[Runway](https://runway.com/) introduced [Solaris](https://runway.com/news/research/introducing-solaris) on Monday, the first model of a new class of AI systems it calls Interface World Models, which aims to do away with the traditional process of translating designs into code and make the visual interface the application itself.

Solaris is a real-time interactive model that generates an interface frame by frame, learning from users’ clicks, drags, and other interactions to determine what to render next. In it, Runway sees an early step towards a new kind of operating layer in which interfaces are generated in real time.

## The image is the application now

Runway argues that conventional visual interfaces require designers and developers to translate designs into code and define interactions in advance. With Solaris, Runway promises to bypass this step entirely.

The Interface World Model handles both rendering and interactions, generating every frame and every response to user input so, as Runway describes it, “the entire frame becomes the interface.” In this way, the interface is no longer a sequence of pages but a continuously generated, interactive experience in which “users interact directly with the scene itself.”

To illustrate its vision, Runway offers several examples of what becomes possible with a generative interface: dragging and dropping a shirt from a rack onto an image of yourself; moving furniture around a room; watching a salad bowl change as you drag and drop ingredients from a pile.

## Learning, reasoning, and rendering in real time

Solaris is built on Runway’s Gen-4.5 video generation model and follows the path of GWM-1, its general world model. It observes a user’s clicks, drags, and other interactions as signals to generate the next frame. In doing so, it learns what should happen visually each time a user takes an action so it can respond without requiring each interaction to be explicitly programmed.

Runway says it cut the number of denoising steps, taught the model to generate frames autoregressively, and trained it on its own outputs to maintain visual quality over long sessions.

> By doing away with the implementation step where visual designs are translated into code, the image users see quite literally is the application.

It also pairs Solaris with a language model to separate reasoning and rendering. Working together, the language model interprets user requests, decides what the application should do next, and creates prompts to guide rendering. Solaris, meanwhile, generates that behavior in real time.

> Runway argues that agents trained on conventional, coded interfaces can struggle to generalize when layouts change. It says that Solaris can eanble agents can train on ever-changing interfaces and never-before-seen layouts.

Altogether, Runway’s approach boils down to three new software capabilities: interfaces can be visual, “alive,” and open-ended, continuously responding to user actions. By doing away with the implementation step in which visual designs are translated into code, the image users see is literally the application.

## What you stand to gain when you lose the translation step

Runway conducted two evaluations examining coded and generated interfaces.

First, several state-of-the-art multimodal language models, including Claude Fable 5, were tasked with recreating website interfaces from a single screenshot.

Across 30 interfaces, as visuals became more complex, reconstruction quality consistently fell, which Runway points to as evidence that translating an interface through an intermediate representation loses information. But because Solaris operates directly on the visual interface, the company claims it can preserve the interface’s complete visual and semantic state from the first frame onward.

Next, it tested whether a coded interface can recreate “the same sense of a living, responsive environment” as an Interface World Model can.

Runway stacked Solaris against the state-of-the-art language model Claude Opus 5, giving both models the same starting image and interaction requests. Per Runway, across almost 7,500 pairwise judgments and 30 interaction examples, the 250 participants in its user study preferred Solaris for better adherence to the given instructions and for behaving more naturally within the scene in 61% and 71% of comparisons, respectively.

Runway says the evaluation results point to a fundamental difference between coded interfaces and Interface World Models: the former treats each user interaction as an isolated update to the environment, whereas the latter generates interactions that remain coherent within the scene.

## The advent of a new operating layer?

Runway says it expects interface generation to follow the development of image and video generation, with successive models improving speed, coherence, and controllability.

For starters, it says that keeping text stable and legible is a top challenge, along with maintaining coherence over long sessions, grounding generation in richer, verified context, and integrating generated interfaces with the rest of the software stack.

Looking ahead, it envisions a new operating layer that can generate useful interfaces to suit nearly any user need. Personalized storefronts and tutorials are just some of the possibilities Runway puts forth, even going so far as to question whether apps will remain the basic unit of interaction.

Runway says it’s working with partners to launch Solaris publicly and is accepting requests for early access.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)