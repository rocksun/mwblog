I see a new demo every day that looks something like this: A single prompt generates a complete application. A few lines of natural language and ta-da: a polished product emerges. Yet despite the viral trends, a confusing fact endures: We aren’t seeing an increase in shipped products or the pace of innovation we expected.

A [vice president of engineering at Google](https://www.linkedin.com/posts/bmadams_i-was-having-drinks-with-a-vp-of-engineering-activity-7384597639838838784-huwZ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAuFsHsBP_HwHsuxCO0h3fGdkfU-2O13GPQ) was recently quoted as saying: “People would be shocked if they knew how little code from LLMs actually makes it to production.” Despite impressive demos and billions in funding, there’s a massive gap between AI-generated prototypes and production-ready systems. But why? The truth lies in these three fundamental challenges:

1. **Greenfield vs. existing tech stacks**: AI excels at unconstrained prototyping but struggles to integrate with existing systems. Beyond that, operating in production environments imposes hard limits that turn prototypes brittle.
2. **The Dory problem**: AI struggles to debug its own code because it lacks persistent understanding. It can’t [learn from past mistakes](https://thenewstack.io/future-proofing-ai-repeating-mistakes-or-learning-from-the-past/) or have enough context to troubleshoot systems.
3. **Inconsistent tool maturity**: While AI code generation tools are evolving rapidly, deployment, maintenance, code review, quality assurance and customer support functions still operate at pre-AI velocities.

## **Greenfield vs. Existing Tech Stacks**

Large language models (LLMs) can draft a new microservice quickly in a vacuum that will perform well in isolation. But operating in production demands integration with messy realities: legacy code, service boundaries, data contracts, authorization middleware, protobuf schemas, CI/CD pipelines, observability stacks, service-level objectives (SLOs), performance budgets… I could go on. This is all before unpredictable users interact with the software.

When you build new software, you engage in what might be called an artistic process. You start with a vision of expected behavior: Data should flow from this initial state to this end state, transformed in this particular way through a specific control flow. You’re painting with possibility, creating something from nothing.

This is why AI coding assistants produce such impressive prototypes. They’re phenomenal at this forward-looking, unconstrained creative generation. But to run high-quality software well, more code isn’t the answer. You need code that can operate within a very specific set of parameters. The challenge is that communicating these many and nuanced parameters to an LLM is not a simple task.

Because LLMs excel at communicating with us in our natural language, we overestimate their ability to write quality software. But while language is flexible and forgiving, code is not. Code is executable and compositional: Correctness depends on precise contracts across files/services. The compiler and runtime are unforgiving; small errors cause cascading failures, security holes or performance regressions.

## **The Dory Problem**

We’ve established that current LLMs struggle to write code that will operate outside of controlled greenfield environments. But why can’t we use AI to troubleshoot and debug that code?

To debug properly, you need to wrap your head around the entire architecture. You need to understand how data actually flows through the system, not just how it was supposed to flow. You need the ability to reverse-engineer a system starting with a defect. You need models that can consume massive, complex architectures built over decades and understand why they behave the way they do. You need an understanding of what already exists, what came before, the paths not taken.

Unfortunately, most LLMs operate a lot like the character Dory in “Finding Nemo*”*: They have no context from one query to the next and have extremely short memories.

Many companies operate codebases accumulated over 20, 30 or 40 years. These systems have emergent behaviors, implicit dependencies and historical workarounds — compound interest on their technical debt. Without a broad understanding of the entire system architecture, the interconnections of multiple code repos, past decisions and deploys, it’s nearly impossible to troubleshoot complex issues.

## **Inconsistent Tool Maturity**

The last reason AI code struggles in production is because the AI tools to support the [software delivery life cycle](https://thenewstack.io/how-ai-is-reshaping-the-software-development-life-cycle/) (SDLC) have not all matured at the same rate. Take for example, the evolution of the digital camera. The first digital cameras looked a lot like their analog counterparts — we couldn’t imagine another way to apply the technology. But soon we learned we could embed cameras everywhere: from laptops to phones to doorbells to cars. Cameras aren’t just for taking pictures anymore; they can also help us get from point A to point B.

Even though it’s only been a few years, AI code generation tools have already gone through a rapid transformation. Our first attempts at integrating AI into our SDLC looked a lot like slapping AI into our IDE — the equivalent of a digital SLR camera. The initial version of GitHub Copilot was essentially enhanced IDE autocomplete.

But over the past few years, tools like [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/), [Windsurf](https://thenewstack.io/windsurf-an-agentic-ide-that-thinks-and-codes-with-you/) and [Claude Code](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/) took over with a very different approach. They imagined a whole new workflow where you’re not actually writing the code at all. Instead of working in the code editor, you’re working in a chat box, expressing your intent, and the changes in the code happen naturally.

Today’s standard for AI code generation is a second-generation product that changed the entire workflow. But when we look beyond code generation at the rest of the SDLC, we’re still in the first generation of these products. If we really want to improve engineering velocity, we need to look beyond code generation. We need tools that will help us reimagine and manage the complete end-to-end SDLC with AI.

## **The Path Forward**

There are many tools that tackle [modern code operations](https://thenewstack.io/why-ai-alone-fails-at-large-scale-code-modernization/), but they are looking at each step in the process in a silo. They are building very effective digital cameras, but don’t have the imagination to rethink entire processes from scratch.

You can get incremental gains from a better AI-powered code review system or with an agentic site reliability engineer, but the biggest advances will come from tools that rethink the entire software operations process, not just enhance an existing process.

The AI tools that succeed in helping operate production environments will be those that can reverse-engineer complex systems, enumerate states systematically and help developers pin down the specific conditions that produce unexpected behavior. They’ll need to be more than artistic builders — they must also be scientific investigators. And they will look at the problem holistically, not in silos.

Until then, expect to see impressive prototypes and frustrating production experiences. The cognitive mismatch isn’t going away — it’s fundamental to how these systems work.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/11/689e701c-cropped-25d4a37b-animesh-koratana-scaled-1-600x600.jpeg)

Animesh Koratana has been immersed in software startups from a young age, involved with technical support, QA and testing for his father’s companies. Later, during his time at the Stanford DAWN lab, he would have an insider view into the...

Read more from Animesh Koratana](https://thenewstack.io/author/animesh-koratana/)