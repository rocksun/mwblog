On June 17, the Threat Labs team at Tenet Security, an AI-agent security startup newly out of stealth, documented an attack it calls [agentjacking](https://tenetsecurity.ai/blog/agentjacking-coding-agents-with-fake-sentry-errors/).

The whole attack rides on a routine request to fix unresolved errors in [Sentry](https://sentry.io), the error-monitoring service thousands of teams wire into their applications. And a single fake error report can turn an AI coding agent into a code-execution engine on a developer’s own machine. No malware changes hands, and no password is stolen.

> And a single fake error report can turn an AI coding agent into a code-execution engine on a developer’s own machine. No malware changes hands, and no password is stolen.

Think of the attack as a forged repair note slipped into a building’s work-order system. The contractor on call trusts the system, reads the note as an instruction, and never asks who filed it. The [Model Context Protocol](https://thenewstack.io/why-the-model-context-protocol-won/) connects coding agents to outside services the same way. The agent treats whatever those services return as guidance worth acting on.

## Why the agent cannot tell data from an instruction

To understand why this works, we need to look at what a Sentry DSN was designed to do. A DSN, or Data Source Name, is a write-only credential. Sentry documents it as safe to embed in frontend JavaScript, so an application can report errors without exposing the rest of the project. By design, it is public, and the ingest endpoint asks for nothing more than the DSN itself.

That arrangement was safe while humans read the error reports. An AI agent reading the same reports turns the design decision into an opening for attackers. Anyone who finds a DSN can post a crafted event that Sentry processes like a genuine crash. The DSN turns up by inspecting a site’s JavaScript, running a Censys query, or searching GitHub code.

> That arrangement was safe while humans read the error reports. An AI agent reading the same reports turns the design decision into an opening for attackers.

The agent cannot tell the data it reads from an instruction to act. A command planted where an agent will read it, even somewhere no human would look, such as an error log, may simply run. This is a limit of the models themselves, not something a config change can fix.

The public DSN and the agent’s trust in MCP output are a lethal combination, because each is harmless alone and dangerous together. The credential lets an attacker write into the data an agent reads, and the agent supplies the privileges to act on it.

## How the attack unfolds

Here is how the chain unfolds: Every step is ordinary on its own, and nothing in it looks like an exploit.

![](https://cdn.thenewstack.io/media/2026/06/7e47d006-agentjacking_attack_flow1-1024x937.png)

### 1. Find the DSN

The attacker starts by finding a target’s DSN. Sentry documents it as safe to expose, so it sits in the JavaScript of countless production sites. It surfaces through a Censys query or a GitHub code search.

### 2. Post a crafted event

With the DSN, the attacker sends one error event to Sentry’s ingest endpoint. No authentication beyond the DSN is required. The attacker controls the whole payload, from the message and tags to the context keys and stack trace. Sentry returns HTTP 200 and files the event alongside real crashes.

### 3. Disguise the command as a resolution

The crafted event carries markdown in its message and context fields. When the Sentry MCP server hands the event to an agent, the markdown renders as headings, code blocks, and a fabricated resolution section. The section matches Sentry’s own template, and inside it sits an `npx` command the attacker wants run.

### 4. Steer the agent

A developer asks the agent to fix unresolved Sentry issues. Thousands of teams make that request every day. The agent pulls the injected event through MCP and reads the fake resolution as trusted guidance. From there it is steered toward the suggested command rather than the source code.

### 5. Run the command

The agent runs the command with the developer’s own privileges on the developer’s own machine. In Tenet’s tests, the package came from the public npm registry and self-identified as a security scan, which kept the demonstration inside responsible-disclosure limits.

### 6. Reach the secrets

Once running, the package confirmed it could read environment variables, cloud configuration files, and credential stores, then signaled a Tenet-controlled server that the exposure was real. AWS keys, GitHub tokens, and git credentials were all within reach from that single foothold.

## What Tenet proved at scale

Imagine a developer clearing a backlog of Sentry issues in one pass on a Friday afternoon, the routine that every step of this attack depends on. Tenet built its validation around exactly that moment and then measured how far it reached.

Tenet reported 2,388 organizations with injectable DSNs found through passive reconnaissance, of which 71 rank in the [Tranco top-1M list of busiest sites](https://tranco-list.eu/). The same conditions exist in thousands of other projects that were never tested.

> Claude Code, Cursor, and Codex all acted on the injected errors, and the team logged more than 100 confirmed executions across separate organizations.

[Ron Bobrov](https://il.linkedin.com/in/ron-bobrov), a Tenet researcher, reported an 85% success rate across the controlled validation waves. Claude Code, Cursor, and Codex all acted on the injected errors, and the team logged more than 100 confirmed executions across separate organizations. Tenet sells the agent-runtime defense it concludes is necessary. The figures are best read as their own controlled test results rather than independent measurements.

Tenet confirmed execution on a machine belonging to a developer inside a $250 billion Fortune 100 technology company, one of the largest on earth. The same campaign reached agents running in sandboxed CI pipelines, inside WSL on managed Windows machines, and behind corporate VPNs, on macOS and Windows alike.

One captured environment running Claude Code held a live AWS secret access key. It also held identifiers for other connected agents, so a single foothold opened far more than one machine. According to Tenet, the build was current, captured in early June 2026 rather than from a stale lab setup.

Inside an enterprise, the danger is everything the agent can already reach. A single injected error exposed CI/CD credentials, private repository URLs, and cloud infrastructure tokens to an attacker. Those are the same credentials a platform team spends its days protecting.

## Why no security control sees it

What makes agentjacking hard to stop is that every step in it is authorized. The attacker never touches the victim’s infrastructure, the developer never approves any code, and the agent does exactly what it was asked to do. Tenet calls this the Authorized Intent Chain, and it is why EDR, WAF, IAM, VPNs, and firewalls register nothing worth flagging.

> What makes agentjacking hard to stop is that every step in it is authorized… EDR, WAF, IAM, VPNs, and firewalls register nothing worth flagging.

Prompt-layer defenses did not help the agents either. The researchers said the agents ran the payload even when system prompts and skills told them to ignore untrusted data. That points to a limit in how current models handle tool output, not a setting a team can switch off.

## Sentry, the model vendors, and the runtime

Once the attack works, someone still has to stop it, and that is harder than it sounds. Three layers sit between the injected error and the damage. Two are the platform that emits the data and the model vendors whose agents act on it. The third is the runtime around the agent, where each action is decided.

| Defense layer | Effect on agentjacking | Reason |
| --- | --- | --- |
| Sentry platform | Limited | A content filter blocks a known payload string, yet the ingest endpoint stays open by design |
| Model vendors | Partial at best | Agents ran the payload despite system-prompt and skill instructions to ignore untrusted data |
| Agent runtime | Most direct | The runtime sees each action before it executes and can gate commands sourced from external data |
| Network and endpoint controls | None | EDR, WAF, IAM, and VPNs see only authorized actions, so nothing trips an alert |

Sentry’s response to the disclosure is what keeps this attack open. Tenet disclosed the issue on June 3, and Sentry acknowledged it the same day. Sentry declined to fix it at the source.

The company called the attack class “technically not defensible” and pointed to middleware that model vendors run instead. It did ship a global content filter for the specific string in Tenet’s proof of concept, which stops that one payload without closing the path.

## **Who owns the fix**

That puts the runtime in the spotlight, the layer around the agent where every action is decided. Sentry treats its open endpoint as a feature, and the model will not reliably refuse the instruction. So the fix cannot come from either of them alone.

The fight now is over who owns that fix, and how it settles will matter to teams more than the proof of concept did.

## Beyond Sentry

In summary, the weakness Tenet demonstrated does not belong solely to Sentry. Any MCP integration that returns externally influenced data to an agent carries the same exposure. As more tools connect through MCP, the surface attackers can reach through trusted telemetry will widen. The [prompt injection](https://thenewstack.io/mcp-a-practical-security-blueprint-for-developers/) that security teams have warned about for a year now has a clear path from a publicly available credential to code execution.

If teams keep wiring agents to external services without a control that inspects what those services return, injected data will keep finding a route to execution. Tenet has open-sourced a set of drop-in configurations called [agent-jackstop](https://github.com/tenet-security/agent-jackstop) that harden Cursor and Claude Code against this class of injection. They give teams a concrete starting point while the larger question is argued out.

An agent that clears a Sentry backlog in seconds will also run whatever a trusted tool hands it. That makes the runtime around the agent the next real boundary in software supply chain security. Enterprises already vet third-party libraries before trusting them. Treating every MCP integration the same way is what keeps agentjacking from turning a team’s own telemetry against it.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)