RALEIGH, N.C. — While most companies are still figuring out how to get their developers to use AI coding tools effectively, [fintech](https://thenewstack.io/the-staging-bottleneck-microservices-testing-in-fintech/) company [Block](https://block.xyz/) just deployed [AI agents](https://thenewstack.io/ai-agents-and-their-life-cycle-what-you-should-know/) to its entire 12,000-person workforce in eight weeks.

At the [All Things Open 2025](https://2025.allthingsopen.org/) conference here last week, [Angie Jones](https://www.linkedin.com/in/angiejones/), Block’s vice president of engineering, explained how the company did it.

[![](https://cdn.thenewstack.io/media/2025/10/f8a79e6a-pxl_20251014_143224926-1-1.jpg)](https://cdn.thenewstack.io/media/2025/10/f8a79e6a-pxl_20251014_143224926-1-1.jpg)

## It Started Small

Like so many tech success stories, this one began with a single frustrated engineer. “Bradley,” a principal [machine learning (ML)](https://thenewstack.io/use-these-tools-to-build-accurate-machine-learning-models/) engineer at Block, said he was tired of AI tools that could only generate code snippets, Jones said in her presentation. He wanted something that could actually do things — automate complex development tasks, not just suggest the next line of code, she said.

When [OpenAI](https://openai.com/) introduced [function calling](https://thenewstack.io/getting-started-with-function-calling-in-llms/), Bradley and a small team started experimenting with automating parts of their development workflow. The experiments worked, but they hit a scaling problem fast. Without any standards, building integrations for different APIs became a headache. Each new tool meant custom code and maintenance issues.

Then [Anthropic](https://www.anthropic.com/) reached out to Block about something called the [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) — an open standard for connecting AI agents to tools and data sources. Block loved the idea, became a launch partner, and rewrote their internal agent (“[Goose](https://github.com/block/goose)“) to work with MCP.

## The Accidental Discovery

Yet, while building Goose for engineers, the team realized they could make it work for everyone at the company.

“We started thinking, what if we could make this work for all 12,000 employees?” Jones said. It sounded ambitious. Most of the workforce had never seen a command line, let alone managed [API keys](https://thenewstack.io/why-your-api-keys-are-leaving-you-vulnerable-to-attack/).

The first attempts were misses. Nontechnical employees couldn’t figure out how to install the software. Those who managed that part got stuck on authentication flows. The whole experience was built for developers, Jones stated.

## Making It Work for Real People

However, the team stopped thinking like engineers and started thinking like their users.

First, they made the software easy to install. The whole process of downloading a file, unzipping and dragging it to the Applications folder was unfamiliar to many employees. So, they added Goose to the internal software center. Now it autoinstalls and autoupdates on every company laptop.

“So, if you have a Block laptop, you have Goose. It just works,” Jones said.

Next, they tackled the “which model should I use” problem. Instead of forcing everyone to use one AI model, they let employees choose. Marketing folks tend to prefer [ChatGPT](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/) for writing. Engineers stick with [Claude](https://thenewstack.io/claude-code-user-base-grows-300-as-anthropic-launches-enterprise-analytics-dashboard/) for technical tasks. The flexibility made adoption much easier across different teams.

“We allow employees to choose from OpenAI, from Anthropic, from [Google](https://cloud.google.com/?utm_content=inline+mention), from Meta providers,” Jones said. “And this gives people that power to choose which makes adoption much easier across the various disciplines.”

Perhaps the biggest challenge was around security. As [Jones noted](https://thenewstack.io/whos-afraid-of-the-queen-of-devrel-angie-jones-of-block/), “Block is a fintech company, meaning Square and Cash App, right? And so, we deal with a lot of regulations. We have to be very secure.” Instead of letting people install random tools, “We spun up a small task team to build internal servers that people needed.”

The team got busy.

“By the end of that week, we had over 60 internal MCP servers ready to go, and today, we’re over 100.”

These internal MCP servers include connections to tools like Slack, Google Calendar, their data warehouse and internal systems. All preapproved, all automatically available.

## The Problems Nobody Talks About

Yet, even with better software, new problems emerged. Employees started enabling every available tool “just in case they needed it,” Jones said. With dozens of tools active, the AI agent became slow and sometimes unusable.

Block’s solution was to implement automatic tool management. If a user asks about calendar scheduling and Asana tasks, the system automatically enables Google Calendar and Asana while turning everything else off. Users don’t have to think about it, Jones said.

They also built conversation summarization. When chats get too long, the system automatically summarizes what’s happened and continues with a fresh context.

## Building a Support System

Moreover, Block invested heavily in helping people use these tools.

They created two Slack channels: one for getting help, another for sharing things people built. The inspiration channel became one of their best adoption drivers. Employees would see a colleague automate something they struggled with and immediately want to try it themselves.

“One [Slack channel] is a place where people can ask questions, they can [report bugs](https://thenewstack.io/curl-fights-a-flood-of-ai-generated-bug-reports-from-hackerone/), they can request features or just get unstuck in real time and everyone just kind of pitches in here,” Jones said. “I can’t overemphasize how critical this has been to adoption, especially for our nontech users.”

The second channel became Block’s secret weapon.

“It’s a space where employees can drop their success stories or cool workflows or clever prompts that they come up with, or wild things that the agent was able to pull off,” Jones said. “So, this channel quickly became one of the best organic drivers of adoption. People scroll through, they see what others are doing, they immediately want to try it out themselves.”

Block also runs weekly workshops, office hours and training sessions about Goose. Not just “here’s how to use AI” sessions, but targeted workshops for specific teams. Sales operations got different training than customer support.

## What People Actually Built

The results were surprising, Jones noted. Employees across the company started automating tasks that would have been unthinkable before, she detailed:

* A security analyst now detects fraud by asking their data warehouse questions in plain English instead of writing complex [SQL queries](https://thenewstack.io/how-to-write-sql-queries/).
* Someone in sales operations analyzed 80,000 sales records and figured out how to redistribute them across different programs. What used to take days of spreadsheet work took an hour.
* An engineer used their incident management integration to spot patterns in system outages, leading to fixes that made their infrastructure more reliable.

Jones shared her own experience: When she needed to sponsor an event but didn’t have time for their usual procurement process, she asked Goose for help. “It felt like Goose was whispering in my ear, ‘Let me tell you who to talk to. Want me to just handle this for you?'”

Jones said the most telling story is one regarding an employee who built her own [MCP server](https://thenewstack.io/10-mcp-servers-for-frontend-developers/), then asked where to submit it. When they gave her a GitHub link, she said, “Oh, I don’t have a [GitHub account](https://thenewstack.io/git-push-how-to-use-the-cli-to-interact-with-github/). I’m not a developer.” A nonengineer had built a tool that solved her specific problem, Jones explained.

## The Bigger Picture

Block’s experience reveals something important about enterprise AI adoption: the technology exists. What’s missing is everything around it — installation, authentication, security, training and community, Jones indicated.

“This isn’t a side project anymore,” she concluded. “We’re putting AI into practice at scale and figuring out what this looks like for a real company.”

Other companies trying to scale AI can learn from Block’s approach. Start with standards (MCP helped them avoid integration chaos). Make things easy to use, not just technically possible. Build security and compliance in from the beginning. And invest in education and community support, Jones explained.

Most importantly: Let users drive innovation. Some of the most creative applications came from departments that had nothing to do with technology, she stated.

Block proved that enterprise AI adoption does not have to be slow, limited to developers or focused on replacing workers. When you make AI tools genuinely accessible, employees find ways to work smarter, faster and more autonomously.

The future of work might not be about AI replacing humans. It may be more about giving every human their own AI-powered capabilities. Block has shown what that looks like at scale.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)