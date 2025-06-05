# GitHub Launches Its Coding Agent
![Featued image for: GitHub Launches Its Coding Agent](https://cdn.thenewstack.io/media/2025/05/e323f54e-img_6682-1024x768.jpg)
Earlier this year, GitHub [teased](https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/) Project Padawan, its agent for assisting software engineers and act on their behalf to handle routine tasks like reviewing code, refactoring it, troubleshooting and more. Today, at the annual [Microsoft Build](https://build.microsoft.com/en-US/home) conference, GitHub is launching its first iteration of this coding agent, dubbed the GitHub Copilot Coding Agent. This new software engineering (SWE) agent will be fully integrated into the GitHub experience and able to take GitHub issues and work on them autonomously. It will start rolling out to Copilot Enterprise and Copilot Pro+ users today.

Since the coding agent needs a lot of computational power, it will run in the cloud, using GitHub Actions. Once a developer assigns an issue to the agent, it will spin up a customizable development environment in GitHub Actions to work on the pull requests.

The agent will not, however, be able to run any CI/CD workflows without human approval. It can also only push to branches it has created, never touching the default branch and others that the developer has created. Developers can limit which MCP servers and internet sites the agent can access, and to add another layer of review on top of this, the developer who asked the agent to open the pull request can’t be the one who approves it.

![](https://cdn.thenewstack.io/media/2025/05/d3102053-screenshot-2025-05-18-at-2.06.51%E2%80%AFpm.png)
Image credit: Microsoft.

“The agent, in today’s world, doesn’t have the same level of trust as a human developer,” GitHub CEO [Thomas Dohmke](https://www.linkedin.com/in/ashtom/) told me. “It is almost like you’re letting somebody into your team without an interview loop and without a background check and those things. And so we believe the agent needs to sit in an environment where more controls are applied than we would apply to humans.“

For the time being, it is powered by Anthropic’s Claude Sonnet 3.7, because, as Dohmke told me, the team believes that this model currently has “the best mix of quality of the code and matching developer preference.”

## 👀
Dohmke has recently [talked](https://thenewstack.io/github-copilot-wants-to-become-your-peer-programmer/) about Copilot becoming a developer’s peer. In many ways, that’s what’s happening here.

“What the workflow looks like is that you, as a developer, are still spending most of your day, hopefully in VS Code, building software that you like, doing things you like doing,” he said in an interview ahead of today’s announcement. “And when you have a task, or somebody assigns a GitHub issue to you, or a bug report comes in, you hand that off to the coding agent. Then you have a handful agent sessions running in the cloud, while your local machine is available to you, being in the flow state. Hopefully doing something magical.”

![](https://cdn.thenewstack.io/media/2025/05/71cfb03a-screenshot-2025-05-18-at-2.07.56%E2%80%AFpm.png)
Image credit: Microsoft.

Using either GitHub.com, GitHub Mobile or the GitHub CLI, developers can assign an issue to the agent just like they would with any other coworker. Then, the agent adds the 👀 emoji and gets to work. Developers can monitor the progress by seeing the agent’s reasoning steps and efforts to validate the code in the session logs.

GitHub stresses that all of this works best for well-defined requests that would typically be covered by a single GitHub issue. “The agent excels at low-to-medium complexity tasks in well-tested codebases, from adding features and fixing bugs to extending tests, refactoring code, and improving documentation,” Dohmke said.

## From Code Completion To Coding Agent
![](https://cdn.thenewstack.io/media/2025/05/7b6cd271-screenshot-2025-05-18-at-2.11.03%E2%80%AFpm-300x199.png)
Image credit: Microsoft.

This new agent complements Copilot’s existing agent mode, which runs in the IDE. Agent mode can also write code from scratch, make edits to an existing code base and use tools as needed. This agent mode, by the way, was previously only available in VS Code, but is now also available JetBrains, Eclipse and Xcode.

Dohmke sees the current offering as a continuous spectrum, ranging from code completion and agent mode, which cover the inner loop of coding, to the coding agent — and back, he stressed.

“If you imagine, the coding agent creates a pull request and it has created five commits,” he explained. “It’s almost there and now you have the decision to make, do you want to keep prompting for it to get where you know you want it to be? Or do you just use the GitHub CLI to quickly check out that pull request? Open VS Code — with Agent mode or without — and make the changes and then push back? The pull request offers the ideal spot where the agent can get you almost there, and you can do the rest really quickly and commit another few commits into that same pull request to be ready to merge that.”

## Microsoft’s SRE Agent
On top of the coding agent, Microsoft is also launching a sight reliability engineering (SRE) agent for Azure this week, which can actually use the new GitHub SWE agent to remediate issues autonomously.

“The key here is it can monitor your systems, 24/7 and troubleshoot the issues that come up autonomously,” [Amanda Silver](https://www.linkedin.com/in/amandaksilver/), the corporate VP and Head of Product of Microsoft’s Developer Division, told me. “It works in your workflow with GitHub. So once it finds the root cause of the issue, it can actually either automatically attempt to remediate it, […], but then it can also log those issues to GitHub. And so we also have this really nice interplay where you could have the SRE agent monitoring your production systems. It finds an issue, it logs that issue to GitHub as an issue, and then the SWE agent — the GitHub Copilot coding agent that we’re introducing — can go and pick it up and progress on the remediation and repair item.”

Silver noted that this SRE agent is based on the internal agents that Microsoft itself has developed and is using internally. Its data is based on the same guidance that the company gives to its engineers to help them troubleshoot Azure services.

Microsoft is also partnering with New Relic to bring data from its application performance monitoring (APM) service into this workflow. The agent will also be able to work with ServiceNow, [PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention) and other incident management systems.

## DevOps Joy
All of this, Silver said, is meant to bring the joy back to [DevOps](https://thenewstack.io/devops/).

“We view this whole category as really being ‘agentic DevOps,’ as the next phase of DevOps overall,” Silver said. “In that world, we see AI agents being embedded in every phase of development: from planning to production, from coding to deployment. That will really help make delivery of software faster, higher quality, more joyful.”

## Bonus: The VS Code Copilot Extension Goes Open Source
While the coding agent is definitely the highlight of today’s GitHub announcements, it’s worth noting that GitHub is also open sourcing the VS Code GitHub extension. VS Code is already open source and so are many of the extensions that developers have come to rely on. The Copilot extension, including its system prompt, will now live in the same GitHub repository as VS Code.

“I think the key here is that this is really going to allow the ecosystem to build with us,” Silver told me. “VS Code has always been open source and the extensions are what makes the magic in VS Code. I think, obviously, there’s an incredible amount of innovation that’s happening in AI-assisted coding overall and so we want to make sure that VS Code continues to be the epicenter of where all of that innovation is happening.”

It’s worth noting that the Copilot Extension for Apple’s Xcode IDE is [already open sourced](https://github.com/github/CopilotForXcode).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)