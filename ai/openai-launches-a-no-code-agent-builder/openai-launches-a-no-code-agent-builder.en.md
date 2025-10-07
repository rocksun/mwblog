OpenAI is hosting its annual developer conference in San Francisco this week. After a number of consumer and financial announcements in recent days and weeks, including the launch of the Sora video creation app, today’s news is squarely focused on building on top of OpenAI’s platform.

The two highlights here are the beta launch of AgentKit, OpenAI’s [no-code agent builder](https://openai.com/agent-platform/), and apps in ChatGPT, which will allow developers to bring more app-like experiences into the ChatGPT interface.

## OpenAI’s Agent Builder

“AI has moved in the last couple of years from systems that you can ask anything to, to systems that you can ask to do anything for you — and we’re starting to see this through agents, software that can take on tasks with context tools and trust,” OpenAI co-founder and CEO [Sam Altman](https://x.com/sama) said in his keynote. “But for all the excitement around agents and all the potential, very few are actually making it into production. It’s hard to know where to start, what frameworks to use, and there’s a lot of work. There’s orchestration evaluators, connecting tools, building a good UI, and each of these layers adds a lot of complexity before you know what’s really going to work.”

AgentKit is essentially a no-code agent builder on top of the OpenAI platform that is meant to let developers and enterprises create agents — and multiagent systems — and put them into production with just a few clicks.

[![](https://cdn.thenewstack.io/media/2025/10/cf7a2582-visual_-agent-builder-template_assets.png)](https://cdn.thenewstack.io/media/2025/10/cf7a2582-visual_-agent-builder-template_assets.png)

Image credit: OpenAI.

For the most part, this isn’t all that different from other no-code/low-code agent builders. But while OpenAI is positioning this as an enterprise tool — with the ability to bring in data from outside services like Dropbox, Google Drive, Sharepoint and Microsoft Teams, as well as third-party Model Context Protocol (MCP) servers (featuring a registry for these connectors) — a fully enterprise-ready system (something more akin to OutSystems or Mendix) would also have to include in-depth data governance, auditing and security tools.

Agent Builder lets developers set guardrails for the user experience, including, for example, detecting jailbreaks and ensuring that no personally identifiable information leaks into the chat. It also integrates with [Evals](https://platform.openai.com/docs/guides/evals?api-mode=responses), OpenAI’s tool for testing prompts and measuring model behavior.

[![](https://cdn.thenewstack.io/media/2025/10/d81940c0-img_2593-scaled.jpg)](https://cdn.thenewstack.io/media/2025/10/d81940c0-img_2593-scaled.jpg)

Image credit: The New Stack/Frederic Lardinois.

To put these agents into production, OpenAI today also launched ChatKit, a toolkit for embedding these agent experiences into apps. That takes another step out of the process of taking these agents into production. Some of OpenAI’s customers, like HubSpot and others, have already taken this service to power internal and external use cases, like a customer support agent.

[![](https://cdn.thenewstack.io/media/2025/10/cf7a2582-visual_-agent-builder-template_assets.png)](https://cdn.thenewstack.io/media/2025/10/cf7a2582-visual_-agent-builder-template_assets.png)

Image credit: OpenAI.

## Apps in ChatGPT

The other major announcement of the day was the launch of apps in ChatGPT (for all users outside of the European Union). The idea here is to invoke third-party apps in the ChatGPT interface — and for developers to build them using the Apps SDK, which itself builds on Anthropic’s [MCP](https://thenewstack.io/when-is-mcp-actually-worth-it/). Indeed, the Apps SDK, which is open source, is essentially an extension of MCP to allow developers to build both the logic and interface of their apps.

In practice, this will look something like this. Say a user wants to browse homes on Zillow. It can invoke the Zillow apps right from ChatGPT (“Zillow show me homes in Portland, OR under $500,000”). Zillow will then pop up a map and an interactive user interface to see those homes, with the user being able to refine that search or ask more questions about a home in the chat bar.

[![](https://cdn.thenewstack.io/media/2025/10/8cb81f03-img_2596-scaled.jpg)](https://cdn.thenewstack.io/media/2025/10/8cb81f03-img_2596-scaled.jpg)

Image credit: The New Stack/Frederic Lardinois.

The SDK includes affordances to have users sign into apps, which in turn allows developers to offer personalization and access to premium features.

“The magic of this new generation of apps in ChatGPT is how they blend familiar interactive elements — like maps, playlists and presentations — with new ways of interacting through conversation,” the company explains in today’s announcement.

[![](https://cdn.thenewstack.io/media/2025/10/11db30ed-zillow-chatgpt.gif)](https://cdn.thenewstack.io/media/2025/10/11db30ed-zillow-chatgpt.gif)

Image credit: OpenAI.

The first apps available are from Booking.com, Canva, Coursera, Expedia, Figma, Spotify and Zillow. Soon, OpenAI plans to launch a directory of apps that conform to [its guidelines](https://developers.openai.com/apps-sdk/app-developer-guidelines) and open it up to developers.

As of now, some parts of the SDK are still in flux. OpenAI specifically calls out that it will soon offer more granular controls for how data is shared with the developers.

One question that always remains with these marketplaces is discovery. During the earliest days of voice assistants like Google Home and Amazon’s Alexa, those companies put a lot of emphasis on building out a developer platform, but users never materialized because nobody knew what voice commands were actually available. Today’s AI systems are obviously smarter than that, and a number of well-known services will surely have no issues getting usage on a massive platform like ChatGPT. But for new developers, discovery will likely remain a challenge, and if OpenAI starts to proactively suggest services — which the company says it will — there are still questions around how it will handle tools that compete with each other.

Developers may also be a bit hesitant to support this new capability, given that GPTs, OpenAI’s previous attempt at bringing apps into ChatGPT, has mostly lingered in obscurity since its launch.

## Codex GA and More

In addition to the two headline announcements, OpenAI also today launched Codex, its AI coding agent, into general availability, and added a Slack integration and [an SDK](https://developers.openai.com/codex/sdk) that allows developers to embed the tools that power the Codex CLI agent into their CI/CD pipelines and their own tools.

This SDK is now available for TypeScript, with more languages coming soon.

OpenAI also today launched a new real-time voice model — gpt-realtime-mini — which it argues is 70% less expensive than its larger cousins without losing a lot of quality. There is also a new small image model — gpt-image-1-mini — that promises to be 80% less expensive to use than OpenAI’s larger image models.

For developers who want to use OpenAI’s most powerful models in their own applications, GPT-5 Pro is now available in the API.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)