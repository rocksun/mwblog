The current trend is for coding agents to move from the IDE to the command line. There’s Anthropic’s Claude Code, Google’s Gemini CLI, OpenAI’s Codex CLI and Aider, for example. Missing from the group, at least until today, was [Augment Code](https://www.augmentcode.com/), which has been positioning itself as the [AI coding tool for the enterprise](https://thenewstack.io/augment-code-an-ai-coding-tool-for-real-development-work/). As part of its launch week, Augment Code today launched its Auggie CLI coding agent.

That’s in addition to other new features launched this week including an update to its context engine, which can now take information from the last [10,000 commits](https://www.augmentcode.com/blog/announcing-context-lineage) to a branch into account, a [1-click integration](https://www.augmentcode.com/blog/announcing-easy-mcp) that connects Augment Code to tools like CircleCI, [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention), Redis, Sentry and Stripe, and [task lists](https://www.augmentcode.com/blog/how-augment-uses-tasklist) to help guide the coding agents by specifying multistep processes for the agent to follow.

But the highlight of the releases is definitely the CLI agent and Augment Code is putting a different spin on its agent compared to other companies. While the agent can be used in an interactive mode to go back and forth with the developer as it implements features and gets feedback, similar to Claude Code, for example, the team is positioning its CLI agent as a tool for automation, too.

“We were seeing everything that was happening with Claude Code and we were trying to understand if it would it make sense for us to build something like this, given that we already have an IDE feature,” Augment Code co-founder [Guy Gur-Ari](https://www.linkedin.com/in/guy-gur-ari/) told me in an interview ahead of today’s announcement. “For us, this is really about the ability to automate, because we want to go beyond the inner loop. We want to go and let developers automate as much of the software development lifecycle as they can.”

As Augment Code’s CEO [Matt McClernan](https://www.linkedin.com/in/mattmcclernan/) also noted when I talked to him, the team was somewhat surprised to see that its users really wanted to work within the CLI.

McClernan, who joined the company last December, took over from [Scott Dietzen](https://www.linkedin.com/in/scottdietzen/) in the CEO role only a few weeks ago, echoed Gur-Ari’s comments and noted that a lot of customers were looking for ways to bring Augment Code and its context engine into their workflows and into the CI/CD pipeline. The CLI agent, he said, will allow developers to build out temples and scripts for their specific use cases.

As for the interactive experience, the team says it will look and feel quite a bit like existing CLI agents. At this point, that’s a pretty well-trodden path, and it looks like Augment Code isn’t trying to reinvent the wheel there.

It’s the non-interactive mode where things get interesting. “We want you to be able to take the same exact prompts [from the interactive mode] and just run the tool in non-interactive mode and then get some level of control over how much non-interactivity  you want,” he said, hinting that there may be moments where the AI agent still has to prompt the developer for more information. “Do you want to see the full dialog history? Or if you just trust that it works and you really just want the final answer from the model without all the tool calls? Then you can do that as well, because that allows for even more scripting, right? Because then, you can just run the tool inside Unix pipes even, as a part of your workflow.”

The team noted that the CLI agent is essentially the same agent the company uses everywhere, so it uses the same context engine as the rest of Augment Code’s tooling. It’s this context engine, the company has long argued, that sets it apart from the competition (though [GitLab](https://about.gitlab.com/?utm_content=inline+mention), for example, makes similar claims).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)