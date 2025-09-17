[Codex](https://openai.com/codex/), OpenAI’s answer to the likes of GitHub Copilot, Claude Code and similar AI coding agents, is getting a major update today.

At the heart of this launch is GPT-5-Codex, a version of OpenAI’s latest GPT-5 models that the company optimizes specifically for agentic software engineering. And while a new model itself is newsworthy, the team also added a slew of additional features to Codex. These include a rebuilt Codex CLI, which is now centered around agentic workflows, a new IDE extension that brings Codex to tools like VS Code, Cursor and other VS Code forks, an integration with GitHub for code reviews, and workflow updates to the Codex web.

Access to Codex is included for OpenAI users with ChatGPT Plus, Pro, Business, Edu, and Enterprise plans, with usage limits scaling based on which plans a user subscribes to. OpenAI explicitly notes that Plus, Edu and Business plans will cover “a few focused coding sessions each week,” while users on the Pro plan can expect a “full workweek across multiple projects.”

With API access coming soon, Codex CLI users will also be able to use the API to pay for Codex (though that can quickly get expensive).

## GPT-5-Codex

It’s worth noting that while GPT-5 received somewhat of a lukewarm welcome, in part because of its model router, which at times seemed to prioritize saving OpenAI money on inference costs over improved results, GPT-5-Codex does feature a router. It’s a self-contained model designed explicitly for Codex (though it will also become available in the OpenAI API soon).

In a press briefing ahead of today’s launch, OpenAI stressed that to reason over complex problems, GPT-5-Codex uses a dynamic amount of reasoning and that in the company’s own tests, the model was able to work autonomously on a problem for more than seven hours (though that’s not a hard cap).

To help guide the model, GPT-5-Codex now uses an AGENT.md file, which has become the de facto industry standard for providing models with coding guidelines and other instructions.

“The model combines two essential skills for a coding agent: pairing with developers in interactive sessions, and persistent, independent execution on longer tasks,” the company writes in its announcement. “That means Codex will feel snappier on small, well-defined requests or while you are chatting with it, and will work for longer on complex tasks like big refactors.”

[![](https://cdn.thenewstack.io/media/2025/09/2039c006-gpt-5-codex-swe-bench.png)](https://cdn.thenewstack.io/media/2025/09/2039c006-gpt-5-codex-swe-bench.png)

Image credit: OpenAI.

Since the team had a bit of extra time to build this model after the launch of GPT-5, it was able to optimize the model’s coding performance.

OpenAI’s benchmarks do show a relatively slight improvement in the [SWE-bench](https://www.swebench.com/) benchmark, which tests if the model is able to resolve issues from a set of GitHub pull requests. At 74.5%, that’s a very respectable score (there are some discrepancies here with some of the data OpenAI previously reported when it launched GPT-5 because OpenAI’s infrastructure wasn’t able to run the entire suite of tasks).

What’s more important in this context, though, is that GPT-5-Codex scores especially well in refactoring code, easily besting GPT-5 on its high reasoning mode.

## Codex Code Reviews in GitHub

That’s likely also why the team felt now was the right time to launch the GitHub code review agent. “GPT-5-Codex has been trained specifically for conducting code reviews and finding critical flaws,” OpenAI explained. “When reviewing, it navigates your codebase, reasons through dependencies, and runs your code and tests in order to validate correctness.”

While 13.7% of comments left by GPT-5 (high) were incorrect, for example, only 4.4% of GPT-5-Codex comments were simply wrong. Meanwhile, 52% of GPT-5-Codex comments were now considered “high-impact” by the OpenAI team, while only 39% were for GPT-5 (high).

[![](https://cdn.thenewstack.io/media/2025/09/e50cd110-codex-comments-incorrect.png)](https://cdn.thenewstack.io/media/2025/09/e50cd110-codex-comments-incorrect.png)

Image credit: OpenAI.

When it comes to working with GitHub issues directly and working on code approvals, those are the numbers that will make a difference.

Like with similar tools, developers simply mention “@codex review” in their pull requests and tell the agent what to review (think “@codex review for security vulnerabilities”).

“At OpenAI, Codex now reviews the vast majority of our PRs, catching hundreds of issues every day — often before a human review begins. It’s been key to letting the Codex team move fast with greater confidence,” the company says.

## Share More With Your Agent

As for the updates to the rest of the Codex ecosystem, one feature that stands out is that developers can now attach and share images — no matter whether that’s screenshots, wireframes or diagrams — with the coding agent in the CLI and web version to provide additional context.

On the CLI side, Codex now also uses a to-do list to keep track of its progress and the team says it has improved tool calls, as well as the user interface for following along with what the model is doing when it calls these tools and creates diffs. There are now three explicit approval modes: Read-only with explicit approval, auto with full workspace access but requiring approvals outside of that workspace, and full access with Codex being able to read files anywhere and run commands with network access.

For Codex web, the team stresses that it improved the overall cloud infrastructure the service runs on, with improved caching bringing down the median completion time for new tasks and follow-ups by 90%.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)