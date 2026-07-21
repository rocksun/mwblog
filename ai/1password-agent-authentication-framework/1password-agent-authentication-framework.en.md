As AI agents tackle more tasks, such as [managing online accounts](https://thenewstack.io/safari-mcp-platform-infrastructure/), authentication has become a practical engineering problem. For example, companies like [Coinbase are already running over a thousand agents in production](https://thenewstack.io/multi-model-ai-infrastructure/). Enter a new 1Password feature for [Claude](https://thenewstack.io/ai-agent-infrastructure-reliability/) that is designed to let a fleet of agents sign in without ever exposing passwords to the LLM.

The company calls this [new browser integration](https://1password.com/blog/1password-for-claude) a “zero-exposure security framework.” Credentials are decrypted only when needed and passed directly to the browser, allowing Claude to complete an action without ever seeing the underlying password or one-time authentication code.

> ## Decryption stays on-device

[Nancy Wang](https://www.linkedin.com/in/wangnancy/), CTO of 1Password, tells *The News Stack* that credential decryption and filling happen locally on the user’s Mac using 1Password’s standard autofill engine.

“When an agent needs to authenticate, 1Password decrypts the credential on-device and injects it directly into the target website through a secure channel,” Wang says. “Claude can ask 1Password to perform that action, but 1Password does not return the plaintext credential to Claude or place it in the model’s context.”

> When an agent needs to authenticate, 1Password decrypts the credential on-device and injects it directly into the target website through a secure channel.

## Task-scoped credential access

When 1Password recognizes that a compatible AI agent is controlling the browser, the extension enters a restricted state called Agentic Mode to enforce least privilege. In this state, the agent cannot browse or search the user’s vault or choose from unrestricted vault contents.

“The moment an AI agent takes control of the browser, 1Password locks down automatically, limiting access to only the credentials explicitly granted for the current task,” Wang says. “Nothing else in the 1Password vault is reachable.”

Claude access is granted per task, and users approve or deny each session with a single biometric prompt via Touch ID or a password. Authorization is scoped to a single task and expires when that task ends, meaning there is no standing access between sessions.

> “The moment an AI agent takes control of the browser, 1Password locks down automatically, limiting access to only the credentials explicitly granted for the current task.”

## Prompt injection remains risky

It is important to separate credential protection from session control. Wang noted that protecting the secret does not, by itself, constrain every action the agent can take after authentication. Once signed in, the agent may be able to interact with the destination service using the user’s authenticated session.

This means [prompt injection remains a real risk](https://thenewstack.io/gpt-red-prompt-injection-testing/). A malicious injection could cause the agent to request access the user did not intend or to take unexpected actions after signing in.

To reduce this, 1Password adds a separate authorization boundary. The approval request appears in a 1Password-controlled UI, where the user can review and reject it. While this reduces the credential exposure risk and limits the available blast radius, users must remain attentive to what the agent actually does during an authenticated session. As a precaution, 1Password also scans the page after every autofill to ensure nothing in form submissions remains exposed before returning control to Claude.

> As a precaution, 1Password also scans the page after every autofill to ensure nothing in form submissions remains exposed before returning control to Claude.

> ## Passkeys and payments ahead

1Password for Claude is now available for Mac users across all plans. It requires the 1Password desktop app and browser extensions as well as the Claude desktop app and browser extensions.

Currently, the system supports usernames, passwords, and TOTP codes. Wang noted that support for social logins, passkeys, payment cards and identity details is on the roadmap.

While this implementation launches exclusively with Claude, Wang expects the underlying principle — that agents should be able to use credentials without receiving or retaining the secrets themselves — to eventually apply across [other agent frameworks](https://thenewstack.io/cloudflare-ai-web-economics/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)