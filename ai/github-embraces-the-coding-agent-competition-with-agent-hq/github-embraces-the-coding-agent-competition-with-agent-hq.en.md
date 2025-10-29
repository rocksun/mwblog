**Disclosure:** GitHub paid the author’s air and lodging expenses for GitHub Universe.

SAN FRANCISCO — At its [Universe 2025 conference here](https://githubuniverse.com/), [GitHub](https://github.com/) today [launched](https://github.blog/news-insights/company-news/welcome-home-agents/) a slew of updates that will bring third-party coding agents directly into GitHub.

Thanks to this, developers will be able to see their agents work and see their chain of thought, steer them as needed and approve the code they generated from a single place. Later this year, this new feature will support [Anthropic’s Claude Code](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/), [Google’s](https://cloud.google.com/?utm_content=inline+mention) [Jules](https://thenewstack.io/agentic-coding-how-googles-jules-compares-to-claude-code/) and [OpenAI’s Codex](https://thenewstack.io/openai-launches-a-new-gpt-5-model-for-its-codex-coding-agent/), as well as coding agents from [Cognition](https://cognition.ai/) and [xAI](https://x.ai/), and, of course, GitHub’s own Copilot agent — all as part of GitHub’s paid subscription.

Copilot Pro+ users will also now be able to work with OpenAI’s Codex in the Insider version of VS Code (powered by OpenAI’s [recently launched Codex SDK](https://thenewstack.io/openai-launches-a-new-gpt-5-model-for-its-codex-coding-agent/)), making it the first of these partners to bring their agent right into the editor (and VS Code itself is getting an update that is meant to make it “all about working alongside agents.”)

For those who want more control over these agents, GitHub will now also let developers create custom agents in VS Code. This means they can create AGENTS.md files with custom instructions and guardrails.

This new agent tooling, which the company is branding as Agent HQ, will give these coding agents access to the same tools and APIs that GitHub’s own Copilot agent uses. The idea here, GitHub said, is to make agents native to the GitHub flow and to give developers the tools to manage a fleet of specialized agents to perform tasks in parallel.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

## GitHub’s Agent HQ

Agent HQ will also extend to VS Code, where GitHub will first integrate OpenAI’s Codex directly in the editor, with other agents to follow soon.

As GitHub COO [Kyle Daigle](https://www.linkedin.com/in/kyledaigle/) told me [in an interview](https://youtu.be/5oZAm5fHziA?si=7IO6yYXoC9afY5AO) ahead of today’s announcement, GitHub wants to give developers choice — even if that means they may choose a coding agent that isn’t Copilot, an issue tracker that isn’t GitHub, or an IDE that isn’t VS Code.

[![](https://cdn.thenewstack.io/media/2025/10/527549ea-c7f5cae8-11c9-44f3-842a-a5fde3f4d5b7-scaled.jpg)](https://cdn.thenewstack.io/media/2025/10/527549ea-c7f5cae8-11c9-44f3-842a-a5fde3f4d5b7-scaled.jpg)

GitHub announces support for third-party coding agents in Agent HQ (Credit: The New Stack).

With Copilot, GitHub offered one of the first AI coding tools. But today, developers are spoiled for choice. Coding agents like Anthropic’s Claude Code, Google’s Jules and Gemini CLI, OpenAI’s Codex and Copilot itself, of course, [have become part of the standard toolbox for most developers](https://thenewstack.io/ai-has-won-googles-dora-study-shows-universal-dev-adoption/).

[![](https://cdn.thenewstack.io/media/2025/10/077324cd-3rd-party-agent-ui-1-1024x560.jpg)](https://cdn.thenewstack.io/media/2025/10/077324cd-3rd-party-agent-ui-1-1024x560.jpg)

GitHub’s Agent HQ lets developers select their preferred coding assistant. (Source: GitHub)

“Our goal with Agent HQ,” Daigle said, “is that we have a single place where you can use basically any coding agent that wants to integrate, and have a single pane of glass — a mission control interface, where I can see all the tasks, what they’re doing, what state of code they’re in — think creation, code review, etc, and offer up the underlying primitives that have let us build GitHub’s Copilot coding agent to all of those other coding agents.”

Virtually all coding agents already integrate with GitHub, and developers often kick off their background agent tasks by tagging their favorite coding agent in GitHub. But as Daigle noted, until now, you could not see them actually work on these tasks in GitHub or steer them.

‘We’re partnering with GitHub to bring Claude even closer to how teams build software,” said Anthropic CPO [Mike Krieger](https://www.linkedin.com/in/mikekrieger/). “With Agent HQ, Claude can pick up issues, create branches, commit code, and respond to pull requests, working alongside your team like any other collaborator. This is how we think the future of development works: agents and developers building together, on the infrastructure you already trust.”

## Mission Control

Central to Agent HQ is Mission Control, which will become what GitHub calls the “central command center” for working with these agents. It will be available in the GitHub web interface, VS Code, GitHub’s mobile app and in the CLI.

A common workflow GitHub envisions is that a developer starts by assigning work to an agent in the GitHub web interface and then monitors the progress in Mission Control. Then, if they want to make a change to that code, they’ll move to their IDE and once done, check in the code and work on something else.

[![](https://cdn.thenewstack.io/media/2025/10/bc83de4d-ezgif-504f7f231e73af.gif)](https://cdn.thenewstack.io/media/2025/10/bc83de4d-ezgif-504f7f231e73af.gif)

An example of work being assigned and monitored in Mission Control. (Source: GitHub)

Because these agents will have native access to these primitives, GitHub is also able to extend its support for a number of features that many enterprises have been asking for. A new control plane for these agents, for example, will let organizations set up audit logging, create security policies, and manage which agents and models the developers will have access to.

Specifically, this means adding branch controls to give organizations control over when to run continuous integration workflows and other checks, as well as access controls for agents, one-click merge conflict resolution and better file navigation capabilities.

## Slack and Linear Integrations

GitHub is also launching new integrations with Slack and Linear.

“Everywhere you are coming up with a problem that needs to be solved in code, we should be there,” Daigle told me. “And so we’re we recently launched a Teams integration to do this. We’re adding the Slack integration to do this, where you’re in a conversation with a co-worker and just say ‘@GitHub, let’s go,’ and basically implement this thing. And it’s just going to show you that it started, and I can look at that in Agent, HQ to continue that work.”

The integration with Linear will work similarly. As Daigle stressed, GitHub wants to be wherever “the moment of inspiration” happens and give developers the ability to send a note to the agent and have it build a plan and implement this new idea in code.

## GitHub Code Quality

With this release, GitHub is also launching the public preview of GitHub Code Quality. As the company notes, code — whether written by an agent or human — may pass the necessary tests to be merged, but it can still degrade the overall quality of the codebase.

The new Code Quality feature, the company stated, is meant to provide “org-wide visibility, governance, and reporting to systematically improve code maintainability, reliability, and test coverage across every repository.”

For agents specifically, GitHub has added a code review step now does a first-line review of the code and checks it for any problems.

[![](https://cdn.thenewstack.io/media/2025/10/69d4e408-code-quality.png)](https://cdn.thenewstack.io/media/2025/10/69d4e408-code-quality.png)

The new GitHub Code Quality feature, now in public preview. (Source: GitHub)

## Embracing All Agents

All of this means that GitHub is inviting its competition directly onto its platform — but, Daigle argued, that’s the right move for developers.

“All this technology has not stopped a core truth, which is developers are going to choose the tools they want to choose, and they’re rarely working 100% alone,” he told me. “It’s a team sport, and so we need to bring the ability for them to play as part of a team, not feel like, well, because I’ve chosen this tool, or because I’ve chosen this coding agent, I need to go spend eight hours a day on an island, and then we’ll bring it back to GitHub, where we do work.

[![](https://cdn.thenewstack.io/media/2025/10/38377782-914a8511-b234-474d-92b4-255935e13dab-scaled.jpg)](https://cdn.thenewstack.io/media/2025/10/38377782-914a8511-b234-474d-92b4-255935e13dab-scaled.jpg)

GitHub’s COO Kyle Daigle introduces the new vision for GitHub as the home for all developers and agents (Credit: The New Stack).

“And so next year, next month, next week, we’re going to continue to find these moments where we go: Oh, we can let developers choose this, and you can be a part of GitHub rather than making that be an either/or.”

The company is also launching new integrations with [Slack](https://api.slack.com/?utm_content=inline+mention) and [Linear](https://linear.app/), the popular issue tracking and project management tool that is often used in concert with GitHub.

Every second in 2025, a new developer joined GitHub, the company says. There are now more than 180 developers on the [Microsoft](https://news.microsoft.com/?utm_content=inline+mention)-owned developer platform. As AI coding agents become increasingly popular, the amount of code generated — and the number of people who will be able to write code — will only increase.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)