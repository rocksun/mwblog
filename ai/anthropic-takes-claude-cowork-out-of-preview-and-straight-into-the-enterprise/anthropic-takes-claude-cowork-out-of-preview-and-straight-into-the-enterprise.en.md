Anthropic on Thursday took [Claude Cowork](https://thenewstack.io/anthropic-accelerates-its-cowork-enterprise-play/), its tool for letting non-developers delegate tasks and workflows to a Claude-based agent, [out of preview](https://claude.com/blog/cowork-for-enterprise) and into general availability.

The service, which only launched a few months ago, is now generally available on all paid Claude plans (Pro, Team, Enterprise).

When Claude Code took off, many developers realized that it wasn’t just an interesting tool for coding in the CLI but also for working on non-coding tasks, especially ones that involved working with a local filesystem. Cowork, at its core, is that capability with a more user-friendly interface as part of the Claude desktop app. It takes the Claude models out of the chat mode of Claude.ai and gives it the ability to handle tasks end-to-end, including working with text documents and spreadsheets.

“The vast majority of Claude Cowork usage comes from outside engineering teams,” Anthropic writes in its announcement. “Importantly, functions like operations, marketing, finance, and legal are not handing Claude their core work, but rather the work that surrounds their most critical tasks — project updates, collaboration decks, research sprints, etc. “

## Making Cowork enterprise-ready

With this launch, Anthropic is stressing that Cowork is ready for the enterprise, and for those users, the company is also adding a number of additional features that enterprises have been asking for.

“What’s been holding Claude Cowork back from full enterprise rollout wasn’t the product — it was the governance layer CIOs need before greenlighting anything at scale. Today’s launch closes that gap,” an Anthropic spokesperson told us in an email.

These include new enterprise features include what is likely the most important feature for enterprises: role-based access controls. With this update, enterprise admins can now organize users into groups, using either a manual approach (which isn’t ideal for large organizations) or through the cross-domain identity management capabilities of their existing identity providers.

In addition, admins can now granularly restrict which actions are available for each MCP tool. This means they could allow the Gmail connector to read emails, for example, but not send them.

Other new features include the ability to set budgets for teams (for those who use the API), as well as usage analytics, including per-user activity, skill usage, and the usual daily/weekly/monthly active user reports.

With this update, Cowork is also now supporting OpenTelemetry, so teams can get granular data about which tools, skills, and connectors are being used, among other data, which enterprises can then pull into their existing analytics pipelines (this feature is only available to users on Team and Enterprise plans).

Since working for an enterprise sadly also means having more meetings than you can handle (or need), it’s nice to see that Cowork now also features a Zoom MCP connector. This brings in meeting summaries and action items, as well as transcripts.

The GA launch comes right as the agentic-desktop category heats up. Microsoft launched Copilot Cowork in March, built on the same Claude engine and agentic harness as Anthropic’s product, but Copilot Cowork runs in the cloud inside a customer’s M365 tenant. This also means that all of Microsoft’s built-in governance featurs will cover Copilot Cowork.

Google’s Gemini Agent Mode and OpenAI’s Operator are also competing for the same non-developer workflow automation space.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)