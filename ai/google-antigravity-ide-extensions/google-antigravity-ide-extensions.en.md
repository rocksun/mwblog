When Google launched Antigravity in November 2025, it was on the premise that developers could hand an entire coding task to an AI agent and let it run. But developers still need to work directly in their code editor.

Google announced Thursday that it is expanding Antigravity into developers’ existing workflows through new extensions for Visual Studio Code, Visual Studio, JetBrains IDEs and Zed. The company is also making Antigravity available through eligible Gemini Enterprise subscriptions.

The extensions let developers open agent conversations in a side panel, review inline diffs, inspect plans and delegate multi-step engineering tasks without moving a project into the Antigravity 2.0 desktop application. The same Antigravity account works across each environment, so users don’t have to sign in or manage licenses separately.

## Agents inside every IDE

The VS Code extension is available now via Microsoft’s extension marketplace on macOS, Linux, and Windows, while the extension for Visual Studio 2026 and .NET solutions is currently in preview. Google is also supporting the JetBrains suite (including IntelliJ IDEA, PyCharm, WebStorm, GoLand, CLion, and Rider) starting with version 2026.2.1, alongside Zed.

Meeting developers in their editor of choice makes it far easier for Google to land inside enterprise engineering teams, where people rarely use the exact same setup.

## Enterprise budgets and guardrails

Admins can turn on Google’s developer tools for employees on Gemini Enterprise Standard, Plus or Standard Emerging Market plans. They can also cap monthly spending for each Google Cloud project. When the included quota runs out, Antigravity either shuts off or switches to pay-as-you-go pricing. Google says controls for individual users and teams are coming later this year.

Until then, everyone in the same edition, project, and region draws from a single pool of credits. Google explains the allowance as monthly but meters it using a rolling seven-day pool. Anything left disappears when the pool resets.

> A nontrivial engineering task can consume 150,000 to 200,000 tokens, while multi-agent handoffs add more input tokens each time work passes between agents.

## Token spending spirals quickly

That quota can go quickly. A nontrivial engineering task can consume [150,000 to 200,000 tokens](https://thenewstack.io/agentic-ai-token-costs/), while multi-agent handoffs add more input tokens each time work passes between agents. One built-in Claude Code skill was recently found to be [loading more than 200,000 tokens before answering a question](https://thenewstack.io/claude-code-token-reduction/). Without a default allocation for each developer, an agent-heavy workflow could burn through the team’s entire pool within hours.

Google is not the first vendor to confront this problem. Microsoft recently introduced [AI token budgets for its engineering divisions](https://thenewstack.io/microsoft-copilot-token-budgets/) after discovering that many of its engineers were spending hundreds to thousands of dollars per month on tokens. Uber reportedly [exhausted its entire 2026 AI coding budget in the first four months of the year](https://thenewstack.io/microsoft-copilot-token-budgets/). An internal Amazon project meant to match author records with product listings exceeded its planned budget by 860%.

## Security policies follow authentication

Enterprise developers sign in with their company credentials, then choose the Google Cloud project and region Antigravity should use. Organizations can connect to their existing identity provider via Workforce Identity Federation, while developers can also authenticate using Application Default Credentials.

Once authenticated, agent sessions inherit the organization’s IAM policies, VPC Service Controls and regional data boundaries. Google says data from enterprise Antigravity sessions is not used to train its foundation models.

> Once one of those connections reaches a production system, a bad setting can have serious consequences.

Admins can limit an agent’s workspace, block browser access, and decide which MCP servers it can use. Once one of those connections reaches a production system, a bad setting can have serious consequences. ElevenLabs’ MCP server, for example, let Claude [delete production voice agents from a chat window](https://thenewstack.io/elevenlabs-mcp-voice-agents/). A connection with that kind of power needs to be treated like any other privileged access.

Putting Antigravity inside existing editors lets Google get its agents onto developers’ machines without requiring a company-wide tooling change, while Gemini Enterprise keeps every session tied to the same policies and project budget regardless of whether it starts in VS Code or JetBrains. Developers can switch editors without changing what the agent can reach or how its usage is billed.

> The extension gets Antigravity through the door; the control plane determines what it can do once it is inside.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)