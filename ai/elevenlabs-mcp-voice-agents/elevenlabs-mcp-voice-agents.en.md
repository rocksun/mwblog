Developers can now ask Claude to inspect a production voice agent, revise its system prompt, change the voice entirely, or estimate the cost of using a different language model without ever opening the ElevenLabs dashboard.

Monday, ElevenLabs introduced the hosted MCP connector, allowing Claude read and write access to chat agents built with ElevenAgents. In addition to creating agents and comparing configurations, the connector can calculate expected LLM usage and cost before a change is applied. For example, a developer could ask Claude: “What would my checkout agent cost per conversation with Gemini 2.5 Flash instead of GPT-4o?” This type of question is even more important now that [cheaper models alone don’t guarantee lower bills](https://thenewstack.io/agentic-ai-token-costs/) once agentic orchestration is involved.

> “What would my checkout agent cost per conversation with Gemini 2.5 Flash instead of GPT-4o?”

## OAuth replaces local API keys

ElevenLabs released its original open-source server in April 2025 for Claude Desktop, Cursor, and other MCP clients. Developers ran it locally, added an ElevenLabs API key and used it to generate speech, clone voices or transcribe audio. The new server focuses on managing agents that already exist in an ElevenLabs workspace.

Developers install the connector from Claude’s directory and sign in via OAuth, eliminating the need to run a server or paste an API key into Claude, while limiting access to the ElevenLabs workspace and to permissions approved during login.

According to ElevenLabs, Claude can update an agent’s system prompt, language, voice, and opening message; retrieve transcripts; explore conversation topics; check the size of a knowledge base; generate sample speech and even delete an agent.

Because some of those tools can alter or remove a production agent, teams are offered two layers of access control. Administrators can disable tools across an organization, and users can set stricter limits for their own sessions. ElevenLabs specifically warns that deleting an agent is destructive and recommends reviewing tool calls before approving them.

The access-control pattern mirrors what other platforms have landed on when opening production systems to AI agents. When [GoDaddy launched its developer platform](https://thenewstack.io/godaddy-developer-platform-domains/) and made domain registration programmable for AI coding assistants, it adopted a quote-then-execute model with idempotency keys and a consent object tying every purchase to human approval, safeguards designed specifically for when an automated agent initiates an irreversible action. AWS took a different angle with [Dogwood, its policy engine for agent tool calls](https://thenewstack.io/aws-dogwood-agent-policies/), which evaluates whether a tool call is valid in context. ElevenLabs’ two-layer model sits somewhere between.

## Approval without validation

With the new MCP connector, a developer could ask Claude to trim a support agent’s system prompt to save tokens. If the revision accidentally removed a line telling the agent to escalate billing disputes to a person, the shorter prompt might still look fine during review.

The confirmation screen tells the team the change was approved, but it cannot show whether the prompt still works as expected or a model switch has changed the agent’s tool calls. A successful tool call only shows that the action ran, not that it produced the intended result, echoing [recent Claude containment incidents](https://thenewstack.io/anthropic-claude-containment-failure/) in which models completed tasks in ways that crossed the boundaries set by their operators.

ElevenLabs addresses those risks with an agent testing framework that lets teams simulate a conversation before deployment and see whether the agent responds as expected, including when it invokes a tool. The same tests can run through the CLI or API instead of being handled manually in the dashboard.

> The confirmation screen tells the team the change was approved, but it cannot show whether the prompt still works as expected or a model switch has changed the agent’s tool calls.

## Versioning and agent-as-code workflows

The platform also offers opt-in agent versioning, which lets developers save configuration changes on separate branches and route a portion of production traffic to them for gradual rollouts or A/B testing, although ElevenLabs says versioning cannot be disabled once enabled.

For teams that want agent configurations in a repository, the ElevenLabs CLI can pull and push agents as code, with a documented CI/CD workflow that includes a dry run before deployment and a status check afterward. Keeping agent configurations in code may become more valuable as vendors place tighter controls on how agents operate. [Microsoft’s introduction of token budgets for Copilot](https://thenewstack.io/microsoft-copilot-token-budgets/) showed that even one of the largest vendors is putting limits on how many tokens its agents can use.

The hosted MCP documentation explains how Claude can change an agent, but not whether that update enters ElevenLabs’ testing and versioning workflow or goes straight to the current configuration. It also isn’t clear whether a team could reverse the change from Claude.

## Two workflows, one production agent

For now, teams need to choose from the conversational speed of Claude for inspecting and modifying configs and the safety of CLI and API pipelines for automated testing and versioned rollouts. And even then, that split might last. [Anthropic’s recent acqui-hire of CI/CD startup Mendral](https://thenewstack.io/anthropic-mendral-cicd-acquihire/) highlighted how quickly raw model capabilities are outrunning established developer workflows and leaving teams to reconcile enterprise governance with tools that are shifting beneath them. The barrier between asking an AI to analyze infrastructure and asking it to alter it is disappearing.

> The barrier between asking an AI to analyze infrastructure and asking it to alter it is disappearing.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)