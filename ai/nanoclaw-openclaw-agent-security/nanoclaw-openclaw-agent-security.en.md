**When Gavriel Cohen first saw OpenClaw**, he knew he wanted it. At the time, Cohen (soon to be the founder of [NanoClaw](https://nanoclaw.dev/) and [NanoCo AI](https://nanoco.ai/)) had stopped developing to work on a marketing project.

[Cohen](https://www.linkedin.com/in/gavrielco/) tells *The New Stack* he was deep into Anthropic’s Claude Code, reviving his coding instincts, when he found what was then Clawd Bot (OpenClaw’s original name).

“I had my first little go,” he says. “I installed it, connected it to my WhatsApp, sent a few messages back and forth. So I came to it really from a need as we were building an AI native marketing agency.”

Before this, it was Claude Code with its terminal-based LLM that first stirred him. “I immediately tried it, and that was a big mental unlock, so around March of 2025 I knew I needed to start building again.” Cohen had previously been a developer at [Wix](http://wix.com), the no-code website development platform also based in Tel Aviv.

He knew there was a missing piece from his workflow. “I was mapping out what I needed, and I actually bought a [Mac mini just to run Claude Code in the background](https://thenewstack.io/mac-mini-agent-infrastructure/) and set up scheduled recurring jobs.” So the relationship with OpenClaw blossomed, at first.

## A self-built package surprise

How long did it take to spot potential issues?

“It was pretty immediate,” Cohen remembers. “I was going through the setup that gives you all these options for different packages to install — and one of them was a package that I had built a few months before called NanoPDF. I saw that and thought, ‘Why did they include that tiny package?’”

You might think Cohen would be flattered to see his own package recommended, but tool users expect only to be presented with well-worn, highly reviewed third-party packages. He knew his package was neither of those. It only had a few stars and hadn’t seen an update in months.

But that wasn’t all: “Then in the first day or two I was debugging, after a scheduled job didn’t fire, and I saw the logs of all the WhatsApp messages — not just the one group that I connected it to, but all of them.”

![](https://cdn.thenewstack.io/media/2026/05/108b6252-screenshot-2026-05-30-at-10.22.57-1024x692.png)

Gavriel Cohen

## The fatal half-million lines

A mixture of sloppiness and poor security is more than enough of a red flag for most developers.

Cohen mentions this observation in his interview with *The New Stack* a number of times, and here is why: You can change policies or enforce sharper coding standards, but once a project’s code base grows out of control into an unmaintainable mess, the project is over. Even an open source project can only have so many eyes on it. By February, OpenClaw had over 3,000 pull requests waiting to be resolved.

“But most importantly, I looked at the code base, and it’s like a half a million lines of code.”

Cohen’s marketing business only had three employees. “We had customers, so I wanted to have an agent for each customer, but I couldn’t connect this thing to my customer data, and I couldn’t build a business on top of it,” he says.

So Cohen did the one thing he knew he could do. “I sat down to build NanoClaw. I had to make this super small because in order for anybody who cares about security to use it, they’re going to have to be able to look over the code and actually see what’s going on and be OK with it.”

> “But most importantly, I looked at the code base, and it’s like a half a million lines of code.”

So Cohen began to address the issues. One question at this point is worth thinking about. Architecturally, what is OpenClaw?

“So at the core,” Cohen answers, “you have a coding agent. It can write code and run Bash commands, so you need a persistent environment session. And then you have to connect to a messaging app. And then the fourth thing is connection to the internet.”

Cohen continues. “From those 4 fundamental capabilities you can build out everything else. And it is proactive because once you start scheduling jobs, it’s no longer just reacting to what you’re saying. You can write a claw agent in as little as 25 lines.”

While OpenClaw was clearly not ready for mass exposure, Cohen sticks to his conclusion about the main problem. “I think it was fundamentally flawed from the beginning, and the fatal flaw is half a million lines of code.” (A quick check confirms that OpenClaw now has over 800,000 lines of code). Even after [OpenAI acquired OpenClaw](https://x.com/sama/status/2023150230905159801?lang=en), the usability problems continued, and the community has dwindled.

So has NanoClaw eased setup? Cohen paused before answering this. “I still think of NanoClaw, for the most part, as suited to technical people — not necessarily developers, but those comfortable with the terminal and GitHub. NanoClaw is not shipped as a binary. Everybody runs it from source.”

The new version now has a terminal-based setup script that walks the user through step by step. Any installation problems are passed off to Claude for fixing. Cohen isn’t entirely happy with this; having Claude in the loop has security implications. “If you don’t understand the security model and you’re just running Claude, it can break the security model or remove the sandboxing.”

Talking of which, why did NanoClaw opt to use containers? And did that decision now form a market position?

## Why containers won

“When I actually sat down to write NanoClaw, I just started from an empty project, and I didn’t tell Claude Code to go look at OpenClaw,” answers Cohen. “I just described the capabilities. I said I want a messaging app; a coding agent; I want it in a loop and I want memory and I built it from scratch.”

> “I can’t just have it running on my machine with an autonomous agent able to do everything, so I put it in an isolated container.”

As Cohen got started, new considerations arose. “I thought: which tools should I give it? I don’t want it to be limited and unable to run bash commands, but if I want to let it run any command, it’s got to be in an isolated environment. I can’t just have it running on my machine with an autonomous agent able to do everything, so I put it in an isolated container.” At that point, the use of containers gave NanoClaw a unique selling point.

There was one genuine surprise from Cohen here: “We started with Apple containers.”

Really? “I was running it on a Mac mini, and I was vaguely aware that Apple had added this new native container capability. That worked really well initially, but when thousands of people started using it, everybody wondered, ‘What are you doing with Apple containers? Docker is the default; it’s a standard that works everywhere.’ So I supported both and then within a few weeks I just changed the default to Docker containers.”

NanoClaw partnered with OneCLI to use their credential and proxying layer for added security. But it adds a bit of a paradigm shift. “The user base and the community gets it,” Cohen says. “Before we had that partnership, there was a major issue with credentials entering the agent environment that we were trying to prevent — but, for example, you need to get the Anthropic token in place so that the agent can connect.”

At first NanoClaw created their own proxying solution, but it got complex. “OneCLI was a very natural partnership, and the user base was happy to have a proper solution. We also have human-in-the-loop approvals, and set policies around — for example — how your agent can use Gmail.”

Speaking of collaborations, Vercel comes up a lot in NanoClaw conversations. What’s the actual integration, and where does it sit on the roadmap?

“Vercel created this great open-source package called [Chat SDK](https://github.com/vercel/chat), which gives you standardized connections to about 15 or 20 different messaging apps. One of the core philosophies I came to NanoClaw with is don’t reinvent the wheel. Why should everybody be re-implementing the same integrations with messaging apps — let’s have one library that we all congregate around.”

We can see that OpenClaw is now its own software tool category. So what does NanoClaw need to do over the next twelve months to not just inherit the mantle, but redefine it?

“What we’ve been doing with credential proxies, human-in-the-loop approvals, and building with isolation of agents is tackling head-on the big hairy problems and challenges that stand between using autonomous agents with their full power, while doing it in a way that’s safe.

## Building for the enterprise

“In the next few months, we are looking at large business enterprises that have strict security requirements, compliance requirements, regulatory requirements, etc. So we’ve already gotten to the point where we have the offering where you can connect to your email, you can connect to your calendar and do that safely where any sensitive action has approval.”

Obviously, entry to enterprise space will be a challenge for any small operation. But NanoClaw knows what it is reaching for, so they could be the right crustacean to back as the competitors fight for OpenClaw’s dropped crown.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)