AWS today launched [Kiro](https://kiro.dev), its take on agentic IDEs like Cursor and Windsurf. Like its most direct competitors, AWS used the open source VS Code project as the basis for Kiro, meaning developers can keep all of their VS Code settings and plugins. Kiro also supports the Model Context Protocol (MCP) to connect additional tools.

As for the underlying large language models, an Amazon spokesperson told me that it will use Clause Sonnet 4 as the default, with Sonnet 3.7 as an additional option. Support for more models is coming soon.

Kiro is [available](https://kiro.dev/blog/introducing-kiro/) for Linux, Mac and Windows and supports most popular programming languages. During the preview period, Kiro will be available for free, with pro plans later starting at $19 per month for up to 1,000 interactions per month with the agent. There will also be a Pro+ plan at $39 per month that will allow for up to 3,000 interactions.

Thankfully, AWS isn’t simply replicating the existing developer experience from similar tools but adding its own twists. Specifically, those are Kiro specs and hooks.

## Kiro Specs

Specs are almost self-explanatory. This allows developers to guide the tool by writing out the requirements for their project.

At first, this may not sound like such a novel idea. If you’ve used Anthropic’s Claude Code, you may have done something similar by using that tool’s Claude.md file, for example, but AWS is among the first to make this a code part of the overall experience — and one that more closely aligns with how code is written in an enterprise environment.

[![](https://cdn.thenewstack.io/media/2025/07/2c687f79-kiro-specs-3.png)](https://cdn.thenewstack.io/media/2025/07/2c687f79-kiro-specs-3.png)

Image Credit: Amazon.

But AWS goes a step further here. When you start a project with Kiro, it will automatically generate user stories, using the Easy Approach to Requirements Syntax (EARS) structure to describe them.

In the next step, Kiro then builds a design document by analyzing the code base you may already have and/or the spec requirements it created (and which the developer can obviously modify). What’s interesting here is that it uses this to create data flow diagrams, for example, as it lays out the TypeScript interfaces, database schemas and API endpoints it needs to build the application.

From there, Kiro generates a list of tasks and subtasks to work through step-by-step, including testing and accessibility requirements. Developers can then trigger each task and watch Kiro go to work.

[![](https://cdn.thenewstack.io/media/2025/07/9fea1913-kiro-specs-1.png)](https://cdn.thenewstack.io/media/2025/07/9fea1913-kiro-specs-1.png)

Image Credit: Amazon.

## Kiro Hooks

This is also where Kiro hooks come in. AWS describes them as event-driven automation triggers that can start up an agent to execute specific tasks in the background whenever a file is saved, created or deleted (or when you trigger it manually).

**“**Kiro hooks act like an experienced developer catching things you miss or completing boilerplate tasks in the background as you work,” AWS’s Nikhil Swaminathan and Deepak Singh, Amazon’s VP of developer agents and experiences, explain in today’s announcement.

[![](https://cdn.thenewstack.io/media/2025/07/b9b73ac3-kiro-agent-hooks-1.png)](https://cdn.thenewstack.io/media/2025/07/b9b73ac3-kiro-agent-hooks-1.png)

Image Credit: Amazon.

This means that when an API endpoint is modified, you could trigger a hook to update the Readme file for the project, for example, or run a scan for leaked credentials before committing the code.

“Hooks enforce consistency across your entire team. Everyone benefits from the same quality checks, code standards, and security validation fixes,” Swaminathan and Singh write.

[![](https://cdn.thenewstack.io/media/2025/07/9fbdc436-kiro-agent-hooks-2.png)](https://cdn.thenewstack.io/media/2025/07/9fbdc436-kiro-agent-hooks-2.png)

Image Credit: Amazon.

As Singh and Swaminathan rightly note, [vibe coding](https://thenewstack.io/from-vibe-coding-to-vibe-engineering-its-time-to-stop-riffing-with-ai/) isn’t going away anytime soon, but at this point, it is also clear that while it’s easy enough now to write a new application with just a few prompts, the real work is often in [getting that code ready](https://thenewstack.io/after-vibe-coding-comes-vibe-testing-almost/) for an actual production environment.

Today’s announcement comes at the end of a long string of news for AI code editors. Most of this has been business news, with, for example, Windsurf last week announcing that it was not going to be acquired by OpenAI, but that its execs were going to Google and that the search giant was licensing some of the Windsurf technology for $2.4 billion.

Meanwhile, we’ve also seen the rise of command-line-based coding agents like Claude Code, which seems to be getting the majority of mindshare right now in the agentic coding space, as well as Google’s Gemini CLI and Amazon’s own [Q Developer CLI](https://thenewstack.io/code-in-your-native-tongue-amazon-q-developer-goes-global/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)