GitHub’s latest move to shake up its Copilot coding assistant is to give it its very own home in a dedicated app.

The Microsoft subsidiary [announced](https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview/) on Thursday a technical preview of the [GitHub Copilot app](https://github.com/features/preview/github-app), a standalone desktop application designed to manage coding agents, issues, pull requests, and development sessions from a single interface.

The app lets developers launch Copilot tasks directly from GitHub issues, prompts, or existing code sessions, while tracking progress across repositories and active agent runs.

> “A standalone desktop application designed to manage coding agents, issues, pull requests and development sessions from a single interface.”

![The Copilot app](https://cdn.thenewstack.io/media/2026/05/f4ecd4ca-cl_githubapppreview_header_07-1024x538.png)

*The Copilot app*

According to GitHub, the app includes a unified inbox for surfacing issues and pull requests, side-by-side diff reviews, session history, repository context, and support for running multiple coding agents simultaneously. Developers can also inspect proposed changes, leave feedback, resume paused sessions, and move completed work into pull requests.

Under the hood, the new app is built on [GitHub Copilot CLI](https://github.com/features/copilot/cli), GitHub’s terminal-based AI coding agent, which reached general availability in February. The desktop client brings those agent capabilities into a dedicated graphical interface, allowing developers to supervise coding sessions, repositories, and tasks without bouncing between terminals, editors, and browser tabs.

![The GitHub Copilot app](https://cdn.thenewstack.io/media/2026/05/3ca28875-giffy.gif)

*The GitHub Copilot app*

Available for macOS, Windows, and Linux, the Copilot app is currently in public preview for Copilot Business and Enterprise subscribers, while Copilot Pro and Pro+ users [can join a waitlist](https://github.com/features/preview/github-app?#form) for early access.

GitHub hasn’t formally announced a full public launch date. However, the announcement’s [accompanying product video](https://github.com/user-attachments/assets/244c19ef-dfdf-446e-b346-101475799f05) references June 2, suggesting the company may be targeting that date for a broader rollout.

## **Beyond the IDE**

Since [launching in 2021](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/), Copilot has primarily existed inside developer tools such as Visual Studio Code, JetBrains IDEs, and Visual Studio itself. GitHub later expanded Copilot into GitHub.com, mobile apps and terminal-based tooling through Copilot CLI.

The original experience revolved around inline suggestions and chat assistance embedded directly inside the editor. Developers would write code locally, while Copilot generated completions, answered questions or suggested edits alongside their existing workflow.

> “The new desktop app pushes Copilot further toward the model emerging across the wider AI coding market.”

The new desktop app pushes Copilot further toward the model emerging across the wider AI coding market: autonomous coding agents operating across repositories, tasks, and cloud environments. That puts GitHub into more direct competition with tools such as [Claude Code](https://thenewstack.io/claude-code-desktop-redesign/) from Anthropic and [OpenAI’s Codex](https://thenewstack.io/openais-codex-desktop-app-is-all-about-managing-agents/), all of which have gained traction by allowing developers to delegate larger chunks of engineering work to AI systems.

GitHub’s advantage, of course, is that much of the surrounding developer infrastructure already lives on its platform. Repositories, issues, pull requests, CI pipelines, and code review systems are already built into GitHub, giving the company a way to tie coding agents directly into the existing software development lifecycle.

[Petter Arnesen](https://www.linkedin.com/in/pettertech/), an Azure MVP and cloud architect who [had early access to the app](https://www.youtube.com/watch?v=5Q5mLNYJ6Hw) for several weeks, described GitHub’s approach as “probably the most interesting implementation” of an AI developer assistant he has tried so far.

In a [LinkedIn post](https://www.linkedin.com/feed/update/urn:li:activity:7460725853962829826/), Arnesen said he had been using the app for everything from side projects to agent-driven pull request review loops where Copilot could wait for feedback, address comments, and update PRs automatically. Still, he said he would not yet “unleash this on production systems without supervision,” pointing to bugs during the preview period and a tendency for AI agents to produce overly complicated solutions without human oversight.

## **Copilot’s commercial model**

The launch follows some major changes to Copilot over recent months, as GitHub adjusts both the product and commercial model.

In April, GitHub [paused new sign-ups](https://thenewstack.io/github-copilot-signups-paused/) for some Copilot individual plans while introducing tighter usage limits for existing subscribers, reflecting growing demand and rising infrastructure costs tied to AI coding tools.

Shortly afterward, [the company announced](https://thenewstack.io/github-copilot-usage-billing/) a broader overhaul of Copilot pricing, moving away from a largely fixed-price subscription model toward usage-based billing tied to tokens consumed by different AI models.

Under the revised structure, pricing factors in input tokens, generated output, and cached context usage, with rates varying depending on which underlying model developers choose to run. The changes bring Copilot closer to how foundation model providers themselves charge for AI inference.

GitHub has also spent recent months expanding the underlying agent infrastructure around Copilot. On Wednesday, the company [introduced a REST API](https://github.blog/changelog/2026-05-13-start-copilot-cloud-agent-tasks-via-the-rest-api/) for launching cloud-based Copilot agent tasks, alongside [unified session views inside JetBrains IDEs](https://github.blog/changelog/2026-05-13-introducing-copilot-cli-agent-and-unified-sessions-view-in-github-copilot-for-jetbrains-ides/).

The desktop app now brings many of those pieces together into a more coherent product surface.

More broadly, the release reflects how quickly AI coding tools are evolving. Early coding assistants focused on helping developers write individual functions or snippets faster. The newer generation revolves around systems capable of handling larger tasks independently across repositories and projects.

GitHub’s new app suggests the company sees that transition as central to Copilot’s future — and does not want that market defined by its big-name rivals.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)