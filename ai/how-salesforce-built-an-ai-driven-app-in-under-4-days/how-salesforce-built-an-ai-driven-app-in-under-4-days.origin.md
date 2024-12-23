# How Salesforce Built an AI-Driven App in Under 4 Days
![Featued image for: How Salesforce Built an AI-Driven App in Under 4 Days](https://cdn.thenewstack.io/media/2024/10/a9f262c8-salesforce-dogfoods-its-ai-agent-platform-2-1024x631.jpg)
Word got out that the Salesforce events team planned to build a custom AI for the Dreamforce conference app. This surprised the online CRM’s AI team, which had already created and was using a new AI enterprise technology stack called Agentforce to build AI agents for customers.

The [Agentforce platform](https://www.salesforce.com/form/agentforce/demo/) became generally available Tuesday, but at the time, the AI team was focused on using it to help external customers develop AI agents for their own use, said [Jayesh Govindarajan](https://www.linkedin.com/in/jayeshg/), the executive vice president for Salesforce AI.

“Four days before Dreamforce, we got a call saying, ‘Hey, we have this events app that’s being built by the events team, and they’re doing it all by themselves — they’re setting up a [vector database](https://thenewstack.io/ai-needs-more-than-a-vector-database/), they are bringing in data,’” Govindarajan told The New Stack. “That’s a lot of work trying to put all these things together. And we were like, ‘Hey, wait a minute, that’s exactly what the stack does. You don’t have to do your own AI by yourself.’”

Building a demo is one thing, but launching at the world’s biggest SaaS event with only four days did raise trepidations, particularly about scale. But it was actually straightforward because the technology stack had been built to support scaling, he said.

“You can just come in, plug in your data, plug in actions, and let the planner do its magic, and be able to get to v1 of an agent really, really quickly.”

– Jayvesh Govindarajan, executive at Salesforce AI
But it did serve as a good test for the Agentforce stack.

“Is it possible to bring all the data in one place to be used for context and grounding?” he said. “Is it possible to, with a few clicks, be able to build a [RAG system](https://thenewstack.io/advanced-retrieval-augmented-generation-rag-techniques/) that can be used to then guide an agentic system? Is it possible to configure with simple actions and descriptions all of the tasks that the agent is supposed to do and can actually do on your behalf? And then, is it possible to configure a full agentic system and the reasoning engine with a few instructions and some guardrails, and then that’s the build process.”

But it took only 2-3 days to build the whole [agentic AI](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) using AgentForce, which Govindarajan said “blew everyone’s mind internally.”

The app, called AskAstro, debuted at the conference, allowing conference goers to query the AI to find sessions of interest and other information. It deployed more than 10,000 instances of the AI agent at Dreamforce, according to a Salesforce’s press release.

Salesforce now plans to use AskAstro for all of its events, Govindarajan said.

## The AI Stack Behind AskAstro
Though the app took only a few days to develop, the technology stack that supports it would take six to eight months if an organization were starting from scratch, Govindarajan said.

The heart of any agentic system is basically three big things, he added:

- A planning and reasoning engine;
- Privacy engines that provide data masking and ensure privacy and intellectual property are protected, and
- Retrieval Augmentation Generation.
“Retrieval augmented generation is all about generating the right context. Think of it like a context engine,” he said.

Data is also a key key element underlying Agentforce, Govindarajan said. Without the right data, large language models will hallucinate so it’s important to provide the right context and the right data, he added.

![An image showing two people and the Agentforce technology stack.](https://cdn.thenewstack.io/media/2024/10/f80d9131-salesforceagentforce-tech-stack.jpg)
The Agentforce technology stack. Image courtesy Salesforce.

When [large language models (LLMs)](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) and [generative AI](https://thenewstack.io/whats-wrong-with-generative-ai-driven-development-right-now/) first came on the scene, it was all about language capabilities, he said. But that has changed quickly.

“In the last eight months or so, what we realized is LLMs are not just great at language, but also phenomenal at orchestrating task, at orchestrating API calls, at […] talking to the customer on one side, and then breaking that task down into smaller sub-tasks, and then mapping those sub-tasks to specific actions that they can take on the behalf of the customer,” he said. “This is a total game changer.”

“Agentforce relies on a family of LLMs for reasoning, planning and production systems. Some of those are their own models that are used for privacy, PII removal and data masking. It’s a family of models that we’ve built and shipped, some of which basically mixes both internal models that we’ve developed along with external models for things like listening, for things like language generation,” he said.

He compared it to the shift required a decade ago when cloud-based SaaS models upended the traditional software development path of build and buy your own infrastructure.

“This was sort of the *deja vu* moment where you don’t need to set up your own vector store. You don’t need to set up your own data cloud. You don’t need to go to data engines. You don’t need to go set up your planner prompting mechanism,” he said. “You can just come in, plug in your data, plug-in actions, and let the planner do its magic, and be able to get to v1 of an agent really, really quickly.”

## The Headaches of AI Testing
AI agent testing can be a real challenge. Govindarajan ran through a list of issues that have to be considered when testing an agentic AI:

- What testing tools can you use to test an agentic system?
- Can you create synthetic data that simulates a user?
- What happens if the right answer doesn’t show up?
- Do you have tools to debug if it does give incorrect answers?
- Can you identify where the incorrect output is coming from?
“Basically, the moment you hit the first issue, debugging is a problem, testing is the problem, but in four days, we were able to dog food all of these sorts of things, really, really fast,” he said. “It was a real test to whether our story is real or not. Are you able to build a production-grade agent in four days by bringing in data, by bringing in context, by bringing in actions, and just launch it in four days after testing it at scale? That’s what we did.”

AskAstro can also remember previous conversations with a user. While it’s one agent, it’s built on a multitenant system, so if a user is logged in, it can remember conversations and provide a more personalized experience, he said.

## How Agentic AI Will Change Frontend Development
Agentic AI will drive the apps of the future, and it will necessitate a shift in how frontend and web application developers approach their end products, Govindarajan added.

“A lot of what we see as two-dimensional applications laid out on a screen with buttons and widgets that encode how the work needs to be done in the enterprise,…that’s going to change to become significantly more agentic,” he said. “Everyone will have an agent. Everyone will have an assistant that can be linked to them and getting work done.”

In many ways, the interface is much simpler, he added, because you’re just talking to the system and it understands enough of the context that you don’t have to overly prompt it.

“It understands enough of [the] context that you don’t have to prompt it exactly the same way,” he said. “Humans, when they’re trying to get a task done, prompt the engine in a variety of ways. They don’t always articulate the request the same way. And what’s cool about these agentic systems is that they’re able to understand that sort of spectrum of articulation, and they’re able to map that to something very specific that you want done on the user’s behalf.”

“Everyone will have an agent. Everyone will have an assistant that can be linked to them and getting work done.”

– Govindarajan
That’s the key experience AI offers that simplifies everything else in the interface, he said.

One additional feature they added is that it can recommend questions a conference user could ask. For example, if an attendee asked what’s happening at Dreamforce today, the AI will provide a few answers, and then will provide the attendee with additional question suggestions based on any previous conversations or context. It might prompt whether the attendee wants to know events in the evening or if the attendee wants to figure out where to have lunch in the neighborhood.

Where does that leave web application developers and frontend developers? It’s probably time to evolve your skillset with an eye toward AI. Salesforce has trained nearly 8,000 web developers from its ecosystems on how to build agents from scratch, which, again, is largely about bringing the right set of data to the user, he said.

“Once you’ve built it, you’ve tested it, you’re ready to launch it,” he said. “Putting it in your mobile app is simply a matter of just an API call.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)