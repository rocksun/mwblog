[Gemini CLI](https://cloud.google.com/gemini/docs/codeassist/gemini-cli), [Google](https://cloud.google.com/?utm_content=inline+mention)‘s open source AI agent that developers access from the terminal and that competes with the likes of [Claude Code](https://thenewstack.io/claude-code-user-base-grows-300-as-anthropic-launches-enterprise-analytics-dashboard/), is now moving beyond the command line and into GitHub with the launch of [Gemini CLI GitHub Actions](http://google-github-actions/run-gemini-cli). Developers will be able to tag the agent in their GitHub issues and Gemini will start working on the issue asynchronously, whether that’s a bug fix or adding a new feature to an existing app. The tool uses GitHub Actions, GitHub’s CI/CD platform, as its compute service.

[Ryan J. Salva](https://www.linkedin.com/in/ryanjsalva/), Google’s senior director of product for developer experiences, noted that Google started on this project because it received so many contributions and feature requests after the launch of Gemini CLI that the team started to automate a lot of what it was doing in GitHub.

“The community happened to take notice. They happen to see what we were doing and wanted to use those same tools for themselves,” he said in a press conference ahead of today’s launch at Google Cloud Next Tokyo. “It is an autonomous agent for all the normal kind of routine tasks that you have to perform inside of GitHub, whether that be triaging issues, performing code reviews or, frankly, opening the kind of the limits up and making it just a general on demand collaborator for all sorts of tasks that you might want to delegate.”

The agent will allow developers to set up automations that will invoke the agent when a new issue is filed, a pull request gets submitted or even when an issue gets a new label.

“By automating through these SDLC [software development life cycle] events, you can effectively take all of the labor of managing that SDLC and delegate it out to the CLI,” Salva said.

To get started, users need to install the Gemini CLI tool and run ‘/setup-github.’

Usage of the agent itself will be free, but you need to bring your Google API Studio API key, and once you run out of your free tier there, you will pay for the API usage. GitHub Actions, where the agent will work on the project, also charges by the minute once you run out of the free tier there. Vertex AI users, as well as users on the standard and enterprise tiers of Gemini Code Assist, will also get access to the service.

Individual users on the free version of Code Assist will get access to the new tool soon, as well.

The advantage of using GitHub Actions, Salva noted, is also that whenever an instance of the Gemini CLI is opened, GitHub Actions spins up a new container that isolates the process from everything else that happens on the platform.

On the security side, the service uses Google Cloud’s workload identity federation, which eliminates the need for long-lived API keys and allows for granular access controls so the developer can ensure the agent only has access to specific branches, for example.

“Locking that down and giving it least privilege ensures that when you’re using Gemini CLI in an autonomous fashion, you’re not jeopardizing any slip or automatic destruction of data,” Salva said.

Now, if all of this sounds a bit familiar, that may be because you’ve heard of [GitHub’s own coding agent](https://thenewstack.io/github-launches-its-coding-agent/), which launched in May. The GitHub agent, too, is a software engineering (SWE) agent that works asynchronously right inside the GitHub ecosystem.

Likewise, Anthropic recently demoed how its Claude Code agent can work with GitHub Actions as well. The [Claude Code GitHub Actions tool](https://docs.anthropic.com/en/docs/claude-code/github-actions) is currently in beta. Augment Code, too, recently launched an asynchronous agent (or “[remote agent](https://thenewstack.io/augment-codes-remote-agents-code-in-the-cloud/),” as the company calls it).

GitHub is using Anthropic’s Claude Sonnet model for its agent, while Google obviously uses its own Gemini models.

Like GitHub, Google also notes that its tool focuses on team collaboration, given that GitHub is where software development teams come together. But there’s no reason solo developers wouldn’t want to try it, too.

Since it runs in GitHub, it has the full context of a given project to work with.

In a demo, Google showed how a developer can tag the agent in an issue, with the agent then responding with a plan for how to accomplish that task. Once approved, the agent then works in the background (though the developer always gets full transparency into what the agent does) and checks off the to-do items from that plan as it goes along.

It’s worth noting that this isn’t Google’s first foray into bringing agents into the GitHub ecosystem. [Gemini Code Assist for GitHub](https://blog.google/technology/developers/gemini-code-assist-free/) launched in February, after all. But as Salva noted, that project solely focused on code reviews and didn’t have any other capabilities.

“Developers were looking for a more general-purpose tool that could be used for a wide variety of use cases, not just code review but automation events in the SDLC of all kinds,” he said. “And so Gemini CLI is opening up the number of possible use cases by providing a generalizable agent. It so happens that the team building the existing code review agent and Gemini CLI is the same team. They are both within my organization, and so we’re looking at convergence over the long term.”

> [GitHub Launches Its Coding Agent](https://thenewstack.io/github-launches-its-coding-agent/)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)