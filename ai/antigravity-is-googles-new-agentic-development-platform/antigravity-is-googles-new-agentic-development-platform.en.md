[Google](https://cloud.google.com/?utm_content=inline+mention) today [launched](https://antigravity.google/blog/introducing-google-antigravity) [Antigravity](https://antigravity.google), its latest experiment in building an agentic development platform. Powered by [the new Gemini 3 model](https://blog.google/products/gemini/gemini-3/), Antigravity combines what has become a pretty standard AI-centric IDE with a few innovations that, according to Google, evolve the IDE “towards an agent-first future.”

Antigravity will be available for free in public preview for Mac, Windows and Linux starting today, with what Google calls “generous rate limits” for Gemini 3 Pro usage.

[![A demo of Google's Antigravity developer tool.](https://cdn.thenewstack.io/media/2025/11/fe306be4-google-antigracity-demo.gif)](https://cdn.thenewstack.io/media/2025/11/fe306be4-google-antigracity-demo.gif)

A demo of Google’s new Antigravity agentic developer tool. (Image credit: Google)

## Model Choice: Gemini, Claude and GPT-OSS

One interesting aspect here is that Gemini 3 isn’t the only model that developers can choose. They will also be able to use Anthropic’s Claude Sonnet 4.5 and OpenAI’s open-weight GPT-OSS models to power the agents.

“We will provide access to models to the degree we have capacity, with rate limits to prevent abuse and that are refreshed every five hours,” Google explains.

Google and Anthropic recently announced [a major cloud partnership](https://www.cnbc.com/2025/10/23/anthropic-google-cloud-deal-tpu.html) worth billions of dollars. Maybe this was part of the deal.

## Next-Gen Agentic Coding

The IDE itself will give developers access to the code in its editor view and all of the usual trappings of any modern development environment, including tab completions and in-line commands.

“We realized that LLMs — language models — have really fundamentally changed how people code and how we build software, how we bring ideas to life,” [Koray Kavukcuoglu](https://www.linkedin.com/in/koray-kavukcuoglu-0439a720/), the CTO of DeepMind and Google’s chief AI architect, said in a press briefing ahead of today’s announcement. “So today, to push the frontiers of how the model and the IDE can work together, we are introducing Google Antigravity. It is our new agentic development platform. I think it is an important concept to think about how we develop software with a dedicated agent interface that enables developers to operate at these higher, task-oriented levels.”

Agentic coding is obviously neither new anymore nor anywhere near the peak of its hype cycle. But what we are seeing right now is a constant stream of innovations around this concept, and while it’s impossible to judge how well Google’s new models perform in this environment, Google is pushing the envelope around the overall developer experience.

[![The logo for Google's Antigravity agentic coding tool (Credit: Google).](https://cdn.thenewstack.io/media/2025/11/9fa23e7d-googleantigravitylogo-whitebackground.png)](https://cdn.thenewstack.io/media/2025/11/9fa23e7d-googleantigravitylogo-whitebackground.png)

Image credit: Google.

## Trust but Verify

The company argues, for example, that similar tools in this category tend to either show the user every action and tool call the coding agent makes, or only show the final code without context. “Neither engenders user trust in the work that the agent undertook,” the Antigravity team writes in today’s announcement.

In Antigravity, the agents produce what Google calls “artifacts,” which it defines as “deliverables in formats that are easier for users to validate than raw tool calls,” including task lists, implementation plans, screenshots and browser recordings. The idea here, the company says, is to ensure the user can trust that the agent has verified its work.

“You can look at how the agent has been executing, which states have been completed along the way. The agent will verify its work through running the application inside the Chrome browser, and will, when it is finished, present a walkthrough of how the final product is working,” Kavukcuoglu explained.

## Agent Manager

Another example of how Antigravity is trying to bridge existing agentic coding paradigms and new ideas is its focus on what it calls an “agent-first Manager surface,” which the team describes as a kind of Mission Control for spawning, orchestrating and observing agents as they work asynchronously on a task.

Users who prefer a more traditional model, with the editor view and an agent panel on the side, can choose to do so, but the Antigravity team argues that “we are transitioning to an era, with models like Gemini 3, when agents can operate across all of these surfaces simultaneously and autonomously.

“In addition to the IDE-like Editor surface, we are introducing an agent-first Manager surface, which flips the paradigm of agents being embedded within surfaces to one where the surfaces are embedded into the agent,” the team writes.

## Steering the Agent

To steer the agent, developers can write Google Docs-style comments on the artifacts the agent creates or give feedback on the screenshots it presents. Over time, the agent will learn from this feedback by keeping an internal knowledge base based on previous work. This may include snippets of code or task lists of how it previously completed a task successfully.

## What About Gemini CLI and Jules?

This new tool joins existing agentic coding tools on Google’s platform, like [Gemini CLI](https://thenewstack.io/expectations-for-agentic-coding-tools-testing-gemini-cli/), the [Jules coding agent](https://jules.google/) and the [recently launched](https://blog.google/technology/developers/introducing-vibe-coding-in-google-ai-studio/) vibe coding mode in Google’s AI Studio. They all approach this technology from a different point of view, and some, like Jules and now Antigravity, are explicitly meant to be experiments. As of now, it seems Gemini CLI is the service with the most traction. Whether any of these other tools survive in the long run remains to be seen.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)