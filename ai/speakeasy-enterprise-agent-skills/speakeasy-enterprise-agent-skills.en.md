“**It’s unrealistic to expect an admin** to have context over how every skill in a company should be optimally performing,” [Sagar Batchu](https://www.linkedin.com/in/sagarbatchu/), founder and CEO of [Speakeasy](https://www.speakeasy.com/), tells *The New Stack*.

That problem becomes harder as enterprises adopt AI agents and developers assemble sprawling libraries of skills that contain deployment runbooks, code review checklists, style guides, incident procedures, and internal workflows.

These myriad skills often begin as personal experiments before spreading across repositories, local machines, Slack threads and plugins. To make matters more confusing, they frequently are without clear ownership or a reliable way to know if the skill you’re using is the current version.

Speakeasy on Friday released [Skills Management](https://www.speakeasy.com/blog/release-skills-management), a system designed to treat skills as centrally registered enterprise artifacts, with immutable versions, scoped access and observability into how they are used.

Earlier this year, we started seeing developers create collections of prompts combined with configuration for agents to use. Over a short time, the Agent Skill [specification](https://agentskills.io/specification) for a skill file was forged; written in [Markdown](https://thenewstack.io/obsidian-and-the-case-for-using-more-markdown/) with some YAML frontmatter. And a skill remains the best way to impart specific enterprise knowledge to any agent.

## **Agent skill libraries multiply**

Speakeasy has a simple message about skills in the enterprise. As organizations adopt AI agents, they’re rapidly building libraries of skills — as deployment runbooks, code review checklists, style guides, incident procedures, internal workflows, and other company-specific knowledge.

The problem is that these skills libraries are growing faster than companies can manage. Skills end up scattered across repositories, local machines, Slack threads, and plugins, leaving teams without a clear view of what exists, which version is current, and who owns a given skill.

Speakeasy claims “one mid-sized fintech customer recently discovered more than 500 unique AI skills in use across the company.” This is because AI experimentation has always been a personal endeavor first and foremost. Using a chatbot feels private; even Claude Code still talks to you like a chatbot. So sharing your prompts with the team may not happen immediately. And this fuels a lot of reinventing the wheel as employees create similar skills without knowing what the other is doing.

## **Centralizing skill management**

To solve for this, Speakeasy starts by treating a skill as a new enterprise artifact that needs some kind of centralized registration — what the company has branded Skills Management.

Skills Management treats skills similarly to how git treats code — a registry of immutable versions, and a shared view of what exists. So if you edit an existing skill, you get a new version. But Speakeasy also adds a degree of observability, so the enterprise knows which skills get used most, and how many times different departments are writing similar things. Better still, if a skill underperforms (that is, the agent that uses it notes problems while executing), an LLM judge can analyze it and suggest improvements.

Skills Management forces the user to abide by the aforementioned Agent Skills specification when creating a skill file so that it can use the frontmatter name as canonical. Attempting to enter the same content under a different name is ignored.

## **Immutable versions and access**

Scoped access allows roles to be formed around who can create and curate skills, and who can consume them.

This combination of skills being monitored by Speakeasy’s control plane as agents use them is clearly better than just herding skill files into a git repository.

Validating skills against the Agent Skills specification is a very good idea. Markdown is, after all, basically English with some symbols. But some optional entries in the frontmatter like “license” could use an enterprise template to keep the process simple.

Sagar tells *The New Stack* that he hasn’t seen this come up with customers yet.

“We don’t currently have a first-party concept of a company-specific template,” he says. “However, companies could create a skill for validating skills that could be introduced into our LLM-as-judge process.”

> “We track metadata for each skill so admins can quickly see which skills are maintained (last updated) as well as frequency of use (and spread amongst team members).”

So, would it be easy for a human (or process) to stop the latest bad change spreading?

“Yes,” says Sagar. “We track metadata for each skill so admins can quickly see which skills are maintained (last updated) as well as frequency of use (and spread amongst team members). And we’re actively developing some auto-categorization features.”

That term “admin” leads to another issue for larger enterprises. A lot of different roles may need to come together to work across company skills. You may want a security expert to suggest a new version of a skill but, more crucially, *invalidate existing skill* versions. However, you wouldn’t want them to be able to edit the content of an existing skill. Can that be represented?

Sagar explains that skill versions are immutable: “It isn’t possible to update a skill version.”

However, “When you publish a new skill version, existing versions are ‘unpublished’ by an automation. This addresses both points in this scenario: A security expert would draft a new version of the skill, publishing it would yank the old versions from employees’ machines, and our observability stack surfaces any discrepancies — for example, lagging plugin versions or deliberate local copies. Old versions can be rolled back where appropriate.

“However, for security reasons, there is no concept of version pinning a skill at the moment.”

What seems genuinely smart about this Speakeasy system is that it understands how a skill starts on a dev’s laptop, and needs promotion through the enterprise to become fully adopted, which exposes more issues about roles.

There will be a lot of UI needed for the manager who needs to identify how quickly the promotion is working — but who has no interest in any other aspect of the skills themselves.

> “Because skills follow the Agent skills open format, there is nothing proprietary in terms of how we store skills.”

## **Enterprise skill portability**

With any system that builds knowledge, the user has to know how to leave it. Sagar says Speakeasy has this covered: “Because skills follow the Agent skills open format, there is nothing proprietary in terms of how we store skills. Users are free to export their skills corpus and move them to another platform. We also offer a path that allows users to clone all their MCP servers and skills to a GitHub repo, so they’re free to leave when they want.”

Enterprises are in the middle of containing the explosion of internal AI agents, as well as asking whether the increased token costs are truly worth it. This type of management and observability platform will play an increasing part in judging the true value in the Agent Era.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)