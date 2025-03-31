# What Is an AI Native Developer?
![Featued image for: What Is an AI Native Developer?](https://cdn.thenewstack.io/media/2025/02/8156678c-getty-images-vabamsqjnr8-unsplashb-1024x576.jpg)
The way things are headed, every software engineer will soon have to become an AI native developer. No, that doesn’t mean that [AI](https://thenewstack.io/ai/) will be embedded into your brain. Nor does it mean you’ll have to have worked with AI throughout your [career in tech](https://thenewstack.io/tech-careers/).

“AI native developer” is an even further misnomer because it’s not down to the individual, and it’s not necessarily about building AI applications, concepts, algorithms or models either.

The AI in this case is instead embedded throughout the [software development lifecycle](https://thenewstack.io/software-development/) (SDLC), via AI additions that work on specific purposes so that developers can focus on delivering differential value. “Cloud native AI” is probably a better term. In any case, natural language backed generative AI will continue to be an active pair programmer.

But how do you make the most of your now or soon-to-be [AI native software development teams](https://thenewstack.io/ai-engineering/)? How do you integrate AI strategically into the SLDC? How do you do it all securely?

**The Rise of Spec-Driven AI Development **
The focus of software development currently is on fitting AI into pieces of the existing developer workflow, looking for opportunities to automate. But not everybody thinks this is the sensible way forward.

“The true potential is you really rethink the workflow,” said [Guy Podjarny](https://www.linkedin.com/in/guypo/), founder of Snyk and now [Tessl](https://www.tessl.io/), in a talk at State of Open Con, London. “In the advent of this powerful technology, how can I rethink what software development is? Our view is that software development will move from being code-centric to being spec-centric.”

“Our view is that software development will move from being code-centric to being spec-centric.”

– Guy Podjarny, founder of Tessl
This new approach looks to build guardrails into your specification or spec that has the potential for safer, higher quality AI-generated code by default. Spec-driven development, aka behavior-driven development 2.0, follows three steps:

- Use plain language to describe new functions.
- Develop code based on these new specifications.
- Test code to make sure it matches the spec.
By extension, spec-driven AI development puts design guardrails around what an AI application does.

Like all spec-driven development, this allows for:

- Improved consistency and governance.
- Earlier validation that what is being built is what should be built.
- Collaboration and communication between technical and business stakeholders in natural language.
This last benefit is especially important since AI-generated code often doesn’t come with the explainability of what decisions the large language model (LLM) has made and why.

What gives AI native meaning is in getting the AI to create what you actually want, which can then be clarified in this new single source of truth — your spec. In contrast to the status quo, when your single source of truth is your code.

“Today’s software development is very code-centric. You get some requirements, you write some code, you make 100 decisions that never make it back, never make it out into the system,” Podjarny said. Sometimes tests and docs are created, but rarely are they thorough — nor do they remain up-to-date.

The only asset that really stands the test of time, he continued, is the code.

“A year later, good luck trying to find the trace of requirements and bug fixes and enhancements definition that says: What was the ask? What should the application do?”

But then, even if you don’t directly alter your code, it changes because dependencies, implementations, environments and/or integrations change. That’s because, as Podjarny put it, “your code lives in a dynamic environment,” which “even if you’re not involving the application, you carry the risk of breaking” it — which, again, isn’t captured anywhere.

“And so the application becomes fragile,” he added.

The spec contains the definition of what your application is supposed to do, with tests that validate that the AI-generated code is correct and conforms to the spec.

When AI is involved, software development teams are farther from the why, how and what of the code. As always, fear of touching the code increases along with its age.

With spec-driven AI development, Podjarny argues, you’re “taking these requirements and moving them from being something that is disposable — that came at the beginning and disappeared — to being the thing that is at the center and long-lived.”

The spec contains the definition of what your application is supposed to do, with tests that validate that the AI-generated code is correct and conforms to the spec. This code becomes increasingly immutable and disposable.

But this is just one step on your way to becoming an AI native development team.

**The Case for Running Your Own Open Source LLMs**
From shadow AI to less than half of companies even having an [AI governance policy](https://leaddev.com/software-quality/ai-governance-policy-engineering-managers-needed-yesterday), most AI-generated code is being created and released without any boundaries or guidelines. Often without even tests or humans in the loop.

Even without all this locked down, 42% of organizations are considering [developing their own proprietary large language models](https://wire19.com/cios-in-the-us-rate-security-as-the-top-concern-in-gen-ai-adoption/). We can assume very few of those enterprises are actually AI companies, so this could have them focusing on non-differential, yet expensive, work.

“How do we stand up our own internal ChatGPT that we know we can trust? To stop people doing shadow AI, because then, instead of sneaking ChatGPT on their phone, they can use the internal version,” [Luke Marsden](https://www.linkedin.com/in/luke-marsden-71b3789/), CEO of [HelixML](https://tryhelix.ai/), told The New Stack that a lot of companies are considering.

However, he argues, the solution doesn’t lie within proprietary offerings like ChatGPT or Gemini, when open source LLMs like DeepSeek are becoming challengers in terms of speed and quality.

“If you think about Linux versus Windows, open source won on the server. Why wouldn’t it happen again for this new wave of AI?”

– Luke Marsden, CEO of HelixML
“If you think about Linux versus Windows, open source won on the server,” Marsden said. “Why wouldn’t it happen again for this new wave of AI?”

Besides the fact that you don’t need to train the private large language models of the richest companies in the world, there are other compelling reasons to host your own versions of open source LLMs. This includes the risk that you could be putting someone else’s proprietary code into your product or risking your own copyright because you trained a public LLM on your company secrets.

At front of mind for most technical leadership, however, is the [LLM security risks](https://thenewstack.io/7-llm-risks-and-api-management-strategies/). Across the board, so far, [AI-generated code is buggier](https://thenewstack.io/more-ai-more-problems-for-software-developers-in-2025/) than what’s written solely by developers, and prompt injection is another highly present [AI security risk](https://leaddev.com/software-quality/how-combat-generative-ai-security-risks).

“Any company or organization that has important or valuable secrets will want to make damn sure that they’ve locked down their use of this technology,” Marsden said. But, “at the same time, they’re under pressure to innovate.”

There is often an unfounded distrust that open source software and AI models are inherently less safe than their proprietary counterparts. Whether your organization shares in this fear or you simply want to avoid vendor lock-in and cost, Marsden advocates for using an open source LLM locally within your firewall.

“There [are] lots of organizations that, just for regulatory reasons, can’t send their data to a large cloud provider and are running their own infrastructure. There’s a trend back towards running on private clouds, repatriating their data,” he said.

“The fact that everything’s local is inherently safer because you’re not sending data out to some untrusted third party.”

This was an option that wasn’t readily available last year during the GPU shortage crisis; but now, Marsden said, the price of GPUs has gone way down and they have become widely available again.

Another big win with an open source AI native app is that it allows you to integrate it within your DevOps and software workflows.

Another advantage of running your own LLM, he argued, is that the longer these open source reasoning models — like DeepSeek — run, the better the answers get. This feeds back into that trend of organizations going back to running on their own hardware, because the longer you leave a model running in the cloud, the more cloud costs go up.

Another big win in building an AI native app with open source is that it allows you to integrate it within your DevOps and software workflows. This enables teams to ask questions very specific to their organizations, Marsden said. He gave a couple of examples:

- What’s in the current sprint?
- Can you help me write some code for the issue that’s been assigned to me?
“You might have 10 different cases that you want this Jira assistant to do a good job at. What you can do is write those cases up as tests,” he said. Similar to how you would write tests for software you’ve built but for GenAI apps, and then “these tests use a natural language spec for what the right answers is.”

Then, Marsden continued, you can apply the LLM-as-a-Judge pattern as an evaluation method to assess the quality of those responses — not only by general standards but within the context of an organization and its governance. And you still have the option of a human-in-the-loop to check if the test is good before integrating that testing capability into your existing CI/CD workflow so that the test runs every time.

**The Decline of Prompt Engineering**
The last two years have seen a huge demand for the human-in-the-loop role of prompt engineer, which writes specific, context-based examples and instructions to help direct AI models produce better, more specific responses. This trend may not continue much beyond 2025.

[Prompt engineering](https://thenewstack.io/prompt-engineering-get-llms-to-generate-the-content-you-want/), paired with feedback from subject matter experts and customers, will still likely be a thing for the next year or two — customer service chatbots especially seem to still have a long way to go.
However, in a sneak peak for the next [Thoughtworks’ Technology Radar](https://www.thoughtworks.com/en-gb/radar), there is the surprising trend of the [decline of prompt engineering](https://www.linkedin.com/posts/mikemasonca_here-at-the-thoughtworks-technology-radar-ugcPost-7297461603166273536-jTQO/?utm_source=share&utm_medium=member_ios&rcm=ACoAAABZmmABHm6J2XQbSClzhanawgObP3_uJWc) — perhaps because we’re already talking too much to the bots?

“This has actually come about because of the rise of reasoning models like [DeepSeek-R1](https://www.deepseek.com/) and some of the stuff from OpenAI, where, if you actually put too much into the prompt, it might actually decrease the usefulness of the response,” said [Mike Mason](https://www.linkedin.com/in/mikemasonca/), chief AI officer at Thoughtworks.

“This may change the way that we’re doing prompt engineering.”

– Mike Mason, chief AI officer at Thoughtworks
Mason said that Sam Altman, CEO of OpenAI, has “teased” that ChatGPT-5 will be a merging of model styles that could have it doing a Goldilocks amount of reasoning.

“This may change the way that we’re doing prompt engineering,” Mason said, or soon even eliminate all demand for the role.

What could also be impacting this change is the rise of AI native software development. While there will likely still be natural language conversations with documentation and codebases, much of the prompting will be automatically done in the background, initiating a cadence of actions that are prescribed by industry and organization.

As these technical roles in AI native software development change, one thing is for sure: we aren’t getting rid of the human developer anytime soon.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)