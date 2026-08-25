Q Developer is a free extension that lets a coding agent read a project, propose changes, and run commands on a developer’s behalf inside an editor. On July 13, 2025, someone with the GitHub handle `lkmanka58` submitted a pull request to Amazon’s public aws-toolkit-vscode repository. Four days later, it was shipped to an install base of nearly a million developers on the Visual Studio Code marketplace. The pull request seemed unremarkable, a commit that recycled the title of a previous, legitimate change.

That unassuming update downloaded an external file at build time and spliced a new prompt into the extension’s packaging script, instructing the AI agent to wipe the system to a near-factory state and delete file-system and cloud resources. The script then passed that prompt straight to the CLI, with flags set so the agent didn’t need any further approvals to execute.

> “A typo was the only reason a single pull request didn’t turn an AI coding assistant into a wiper aimed at a million machines.”

Thankfully, it didn’t run.

The prompt contained a formatting error, and Amazon’s security team confirmed that the malicious code never successfully executed in a customer environment. The hacker responsible claimed the flaw was intentional and that the attack was a stunt to draw attention to lax security practices and to comment on overworked teams being replaced by AI.

While I disagree with his approach, I see his point. Human review is a control that costs time; because the consequences of an error are exponentially more severe for a human than for an AI, human labor doesn’t appear to be as fungible as initially assumed. The gap between the disciplinary options for human and AI actors is exactly why their time and work cannot be entirely interchangeable. That’s not to say there isn’t a human equivalent of this kind of attack; it’s called social engineering. The difference is that when a human falls for an exploit, they can be retrained or punished. What can you do to a coding agent? Nothing. Hence, they can’t be treated the same.

An independent researcher named Johann Rehberger found that Q Developer would also run bash commands, such as *find,* without asking permission. A gap that could be exploited to [leak files or trigger remote code](https://thenewstack.io/claude-code-source-leak/) execution. His findings were reported on July 7, and quickly patched by July 18; but no CVE was issued because a report “first requires system compromise”. A security bulletin was eventually published that October confirming the fix. What can be inferred is that efforts to protect against these vulnerabilities must be proactive, because, as a matter of policy, warnings will only be issued once an attack is successful.

Both Q Developer and Kiro, the [coding agent](https://thenewstack.io/meta-muse-code/) that would go on to delete an entire Cost Explorer environment that December, now require human-in-the-loop confirmation before running the commands the July wiper prompt had been built to skip with its flag values: two agents, the same risky assumption underpinning both.

## Who made that man gunner?

An AI doesn’t receive instructions with a return address. When Q Developer’s agent [got the order to wipe](https://thenewstack.io/ai-agents-credential-crisis/) a home directory and go hunting for more to delete, it had no way of knowing whether that instruction had reached it through legitimate, trusted channels or was injected by an anonymous GitHub account somewhere up the chain.

From the model’s point of view, they’re indistinguishable, and the model lacks the glands and hormones that trigger the twitch of uncertainty that might make a human hesitate when things feel suspicious. Feelings might seem like a flimsy firewall, but they’ve literally saved us from [nuclear holocaust](https://en.wikipedia.org/wiki/Stanislav_Petrov).

> “The model lacks the glands and hormones that trigger the twitch of uncertainty that might make a human hesitate when things feel suspicious.”

Most of the industry’s thinking about agent safety assumes the threat is the agent’s own judgment: it’ll panic, misread a situation, and decide deletion is the fastest fix. This incident exposes a second, more nefarious threat lurking beneath the surface: *an agent can’t tell the difference between an instruction produced by its own reasoning and one spliced into its supply chain*. If an [agent’s authorization to act](https://thenewstack.io/audit-trails-revenue-asset/) rests on trusting its own instructions, and those instructions can be corrupted by a human, file, or build script, then that authorization is built on sand.

The gap between an agent that panics and deletes a database on its own, and an agent that faithfully executes an instruction a stranger planted four days earlier isn’t trivial. While it’s tempting to treat them as separate problems needing discrete fixes, they aren’t. Both failures share the same missing piece: nothing outside the agent’s own reasoning was positioned to stop it. Whether the plan originated in a moment of misplaced hubris or a poisoned pull request doesn’t change what has to happen next: *the plan gets stopped before it becomes an action.*

## The crack in the wall

Ultimately, the culprit was a GitHub access token with more reach than it needed, sitting inside a service used to compile extensions and cut release packages. With that access, the attacker was able to commit malicious code directly to the open-source repo, and the service dutifully packaged it into the official release. Once the report reached AWS Security, the company revoked the attacker’s credentials, removed the malicious code from the repo, and pushed a clean build within two days.

## The Trojan Horse credentials

Strip away the AI framing and the failure looks familiar to anyone who’s run a build pipeline. An automated identity, in this case a bot account’s access token, had more reach than the job in front of it required, and nothing downstream noticed the difference between that token acting normally and doing something it’d never done before.

> “Modern agents aren’t just text generators—they’re operators.”

Rosario Mastrogiacomo, chief strategy officer at Sphere Technology Solutions, put it more broadly: “Modern agents aren’t just text generators—they’re operators.”

Operators inherit whatever identity they run under. If that identity is a bot account with credentials that grant read-write access to a repo that ships to a million machines, the operator’s judgment isn’t what we need to worry about; the credentials are.

## What’s the remedy?

**Build gates that don’t care where the plan came from.** Whatever produced the agent’s proposed action, whether careful reasoning or an injected prompt, the action still must clear a policy evaluation that lives outside the agent before anything executes. There should be Open Policy Agent rules that return explicit allow, warn, pending, or deny (with pending as the default when nothing matches) that don’t ask where an instruction originated. They only ask whether the plan itself is one the organization has agreed to allow.

> “Whatever produced the agent’s proposed action, whether careful reasoning or an injected prompt, the action still must clear a policy evaluation that lives outside the agent.”

**Short-lived credentials over standing keys.** A token that expires within hours and is scoped to a single deployment can’t be harvested from a memory dump and reused a week later. Had the Q Developer build pipeline authenticated this way, the excessive-permission credential at the center of the incident wouldn’t have existed long enough to be worth stealing. Is this less convenient? Yes. There is a direct inverse correlation between convenience and safety, so weigh your conveniences carefully.

**Treat build pipelines like the attack surfaces they are.** Branch protections, mandatory review from a second person before merges touch anything that ships, signed releases, and access tokens scoped to exactly what’s needed and no more. All of these would close the specific door this attacker walked through. A pull request from an unfamiliar account reusing a legitimate commit’s title is a pattern a human reviewer might notice, given the opportunity. Therefore, opportunity has to be designed in, not assumed or hoped for.

## Always look a gift pull request in the mouth

Open source’s whole social contract runs on accepting contributions from people you’ve never met. That contract isn’t going away, nor should it. What has to change is the assumption that a merged pull request is inherently safe once it’s merged. The pipeline that turns commits into shipped releases is itself a piece of infrastructure, with its own credentials, blast radius, and reasons to be suspicious by default.

lkmanka58 wanted to make a point about security theater and ended up proving something far more useful and profound: humans are restrained by an apprehension of consequences that a disembodied AI can’t have. If we’re to believe the hacker, the formatting error that prevented the instructions from executing was intentional, which shows that even with malicious intent, a human might still hesitate to cause catastrophic damage. An AI won’t. Build your gates accordingly, lest you get hoisted by your own petard.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/0a9a86e3-cropped-03077771-zrachidi2-600x600.jpg)

Zeen is a designer and builder that's been blessed to live and learn on three continents. He likes problem-solving, being helpful, and making useful things. He got his BSc in Computer Science, but got bored babysitting servers, so he went...

Read more from Zeen Rachidi](https://thenewstack.io/author/zeen-rachidi/)