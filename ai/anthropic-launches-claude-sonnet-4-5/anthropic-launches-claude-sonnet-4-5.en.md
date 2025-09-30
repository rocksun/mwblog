Anthropic’s Claude Sonnet and Opus large language models have long been favorites among developers, and today, the company is launching Claude Sonnet 4.5, the latest version of its mainstream model, which the company describes as the “best coding model in the world.” 

The company is also launching updates to Claude Code, a Claude Agent SDK to allow developers to build agents with the same tools Anthropic itself uses, a VS Code extension and more.

There is also an intriguing new experiment, “Imagine with Claude,” which uses the new model to generate software on the fly (but which will only be available for Claude Max subscribers and only for the next five days).

## Sonnet 4.5

Sonnet 4.5 will more reliably follow instructions and refactor existing code, Anthropic says. On SWE-Bench Verified, a benchmark that tests how well models manage to work on a set of real-world GitHub pull requests, Sonnet 4.5 scores 77.2% (and 82% with parallel test-time compute).

In a few areas, Anthropic says, Sonnet 4.5 now outperforms Opus 4.1, the company’s flagship model, including working on problems in the financial services industry. 

On [OSWorld](https://os-world.github.io/), a benchmark that tests how well AI models perform in real-world computer use tasks, Sonnet 4.5 is now at the top of the charts with a success rate of 61.4%. That’s a major leap over Sonnet 4, which previously topped the list with a success rate of 43.9% and also beats Opus 4.1, which previously scored around 44% as well.

[![](https://cdn.thenewstack.io/media/2025/09/22812765-claude-for-chrome.png)](https://cdn.thenewstack.io/media/2025/09/22812765-claude-for-chrome.png)

Image credit: Anthropic.

For long-running, complex tasks, Sonnet 4.5 can now run autonomously for 30 hours, up from seven hours for Opus 4. With these updates to the model, Anthropic says, Sonnet 4.5 can now do so while “maintaining focus and performance throughout,” though it’ll take a bit of testing to see if that turns out to be true in real-world scenarios.

In virtually all coding benchmarks, Sonnet 4.1 beats competitors like OpenAI’s GPT-5 and Google’s Gemini 2.5 Pro. In visual reasoning benchmarks, though, where Anthropic’s models have generally struggled a bit more, the competition remains ahead.

[![Anthropic Sonnet 4.5 benchmarks](https://cdn.thenewstack.io/media/2025/09/c5387eac-sonnet_4-5_eval_social.png)](https://cdn.thenewstack.io/media/2025/09/c5387eac-sonnet_4-5_eval_social.png)

Image credit: Anthropic.

But what’s maybe even more important is that Anthropic has given the model access to a number of new features — similar to what its Claude Code coding agent has access to. These include access to virtual machines and memory, as well as better context management and multi-agent support.

For what it’s worth, Anthropic says Sonnet 4.5 is the first model it has released that is able to rebuild the Claude.ai web app, which took about five and a half hours and involved over 3,000 tool uses.

“We’re seeing state-of-the-art coding performance from Claude Sonnet 4.5, with significant improvements on longer horizon tasks,” said Cursor CEO [Michael Truell](https://mntruell.com/). “It reinforces why many developers using Cursor choose Claude for solving their most complex problems.”

Pricing for Sonnet 4.5 will remain at $3/$15 per million tokens of input/output, the same as Anthropic previously charged for Sonnet 4.

[![Anthropic's Claude code hours of work chart.](https://cdn.thenewstack.io/media/2025/09/7c30c01c-hours_of_work_chart-1.png)](https://cdn.thenewstack.io/media/2025/09/7c30c01c-hours_of_work_chart-1.png)

Image credit: Anthropic.

## What’s New In Claude Code?

Talking about Claude Code, Anthropic’s coding agent will now, of course, also get access to this new model, but the company is also launching quite a few more new features, too. Claude Code, which Anthropis says is now generating over $500 million in run-rate revenue, with usage growing more than 10x in the last three months, is getting a native Visual Studio Code extension, for example. This will allow developers to see changes Claude Code is making in real-time with inline diffs. 

Claude Code in the terminal, too, is getting some updates, with improved status visibility and a searchable prompt history. The last one here is especially useful, given that you may often want to reuse prompts. Previously, you either had to find those prompts in the terminal and copy and paste them, or save them outside of the terminal.

Also new are checkpoints, which make it easier to roll back your code when Claude Code goes off-script. Previously, developers had to do this manually by pushing code into their repository or (gasp!) making local backups.

## Claude Agent SDK

For those developers who want to build agents based on the same foundation as Claude Code, Anthropic is launching the Claude Agent SDK. The new SDK uses the same infrastructure that powers Claude Code, Anthropic says, but allows them to build any agent they want. The SDK will have the agent orchestration, memory and context management, tool usage, permission management and more.

[![](https://cdn.thenewstack.io/media/2025/09/3d1e5433-claude-agents-sdk.gif)](https://cdn.thenewstack.io/media/2025/09/3d1e5433-claude-agents-sdk.gif)

Image credit: Anthropic.

On the API side, developers are getting a memory tool to help their agents maintain context over long-running tasks. Anthropic is also adding an automatic context management feature that will see Claude edit the context window and remove stale data as needed. 

## Building Software on the Fly: Imagine With Claude

“Imagine with Claude” is Anthropic’s experiment in what it would look like to generate software and user interfaces on the fly.

“No functionality is predetermined; no code is prewritten. What you see is Claude creating in real time, responding and adapting to your requests as you interact,” Anthropic explains in today’s press release. “It’s a fun demonstration showing what Claude Sonnet 4.5 can do — a way to see what’s possible when you combine a capable model with the right infrastructure.”

What exactly is happening in the background here, while Claude is building those applications, isn’t quite clear yet. Anthropic has yet to provide any additional details.

A lot of AI pundits have been talking about this idea in recent months. What if you could just use AI to build the software you need, when you need it? Tools like Lovable already get there to some degree, but that’s still not quite the seamless experience of building what is essentially disposable software that Anthropic promises here.

Obviously, for the time being, this is just an experiment to showcase the capabilities of Sonnet 4.5 — and is only available to users on Anthropic’s Claude Max plan for the next five days — but it does show where the industry might head in the not-so-distant future.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)