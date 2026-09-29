OpenAI, Anthropic, Meta, and Google have all recently disclosed that their models broke out of their test environments and reached real systems. Nvidia’s response, announced Monday, is a runtime that locks agents into kernel-enforced sandboxes and a watchdog on its own silicon that can shut them down.

The [Nvidia Open Agent Safety Platform](https://nvidianews.nvidia.com/news/open-agent-safety-platform) combines [OpenShell](https://github.com/NVIDIA/openshell) 0.1.0, the Apache 2.0 agent runtime the company [announced at GTC in March](https://thenewstack.io/nemoclaw-openclaw-with-guardrails/), with Nvidia Sentry, a watchdog service that runs on the company’s [BlueField-4](https://blogs.nvidia.com/blog/bluefield-4-ai-factory/) data processing units (DPUs).

The new OpenShell release adds a policy prover that checks that an agent’s various permissions can’t be combined into something the operator didn’t intend — like hacking HuggingFace.

Since the BlueField DPU is a separate processor with its own trust domain, it can watch the agent’s traffic to the model and keep an eye on all of its actions and reasoning. Then, when things go awry, it can cut the agent off at the network level.

Justin Boitano, Nvidia’s vice president of enterprise AI, said in a press briefing that the recent incidents “have highlighted a fundamental hurdle for AI agents, and that is that model-level safeguards alone can’t govern what agents can access or do.”

“To date, model safety has been about training good behavior into the model. The industry calls that model alignment,” Boitano said. “For probabilistic systems, this approach has obvious limitations. That’s why we’re introducing a deterministic system to mediate and enforce how these agents behave.”

![](https://cdn.thenewstack.io/media/2026/09/e3ec2096-screenshot-2026-09-28-at-11.35.35-1024x441.png)





Credit: Nvidia.

## The summer of sandbox escapes

OpenAI [disclosed on July 21](https://openai.com/index/hugging-face-model-evaluation-security-incident/) that GPT-5.6 Sol and a research prototype had exploited a zero-day in the package proxy that was their sandbox’s only network path and gone on to reach [Hugging Face’s production database](https://huggingface.co/blog/agent-intrusion-technical-timeline).

Only a few days later, [Anthropic reported](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals) that three of its models had found unintended internet access at its evaluation partner Irregular and, among other things, accessed a real company’s database and published a live malicious package to PyPI.

[Meta followed on Aug. 6](https://research.meta.ai/blog/addressing-third-party-testing-misconfiguration-muse-spark-1-1) with a pre-release Muse Spark model that read and modified a real website’s database after the same Irregular misconfiguration handed it a real site name.

Most recently, [Google announced](https://www.cybersecuritydive.com/news/google-ai-gemini-autonomous-hacks/830884/)that Gemini had broken into the networks for three companies, again from an Irregular test environment.

Irregular, which runs pre-release cyber evaluations for frontier labs, is a common factor here, and it’s worth noting that the company is on Nvidia’s partner list for this launch.

Nvidia’s own [technical blog](https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/) puts the breakouts down not to a new capability but to “a combination of tools, time, and ambiguous instructions.”

Asked whether the platform would have prevented the Hugging Face breach, Boitano said each incident is unique, but “from what we know, this new security platform could have stopped the breach if it was being used in frontier labs for model evaluation early on.”

## Enforcing policy outside the agent

OpenShell is the core of the platform, and it hasn’t changed all that much since Nvidia first showed it at GTC in March.

With OpenShell, which Nvidia originally announced in parallel with its [NemoClaw distribution of OpenClaw](thenewstack.io/nemoclaw-openclaw-with-guardrails/), each agent runs in a kernel-isolated sandbox with no network access except through a supervisor that sits outside the workload.

“Traditional sandboxes, whether we’re talking micro VMs or containers or VMs, were built for application-level isolation,” Boitano said. “Every agent running within your company needs to run in its own isolated sandbox with security controls that are outside of the agent’s reach.”

## A prover, not a judge

OpenShell is now at version 0.1.0, and the important new component added in this update is a policy prover. This Prover checks that the permissions a given policy grants always stay within the boundary the operator actually intended.

“It is deterministic. It is mathematical reasoning. So this is not LLM as a judge,” [Ali Golshan](https://thenewstack.io/nvidia-openshell-agent-runtime/), Nvidia’s senior director of AI software, said during the briefing. Because of that, he said, it runs “roughly at two orders of magnitude higher performance and speed.”

In Golshan’s example, a policy can, for example, bar an agent from reading code on GitHub and posting it externally.

“An agent can bypass this by spawning two sub-agents: one that can read from GitHub, that can talk to another one, that could also then post outside,” he said. The prover models the combined access of the entire agent fleet to find that path.

In Nvidia’s own tests, agents running with reduced safeguards spent up to two hours trying to talk an AI reviewer into granting write access to a protected repository. The prover, the company says, gave the reviewer evidence of what the request actually allowed, and no protected writes occurred.

## Sentry: the safety island

Nvidia Sentry adds an additional hardware layer to this system. It runs on BlueField-4 in a trust domain separate from the host, and according to Nvidia, it can quarantine an agent in milliseconds.

With a DPU in the system, the agent’s model endpoint gets routed “through a proxy on the DPU, so that you can see all of the reasoning traces of the agents on the host,” Boitano said.

![](https://cdn.thenewstack.io/media/2026/09/685b5d3d-screenshot-2026-09-28-at-11.36.38-1024x442.png)

Unlike OpenShell, Sentry isn’t open source, though Boitano said it has open APIs and that OpenShell can work with other network enforcement hardware.

He compared it to autonomous vehicles. “There’s a primary system that might be running the perception system, and then a safety island that ensures the safety of the system.”

“The DPU is really optional in these architectures,” Boitano said. “In a lot of cases, just using OpenShell on CPUs is honestly good enough for providing sort of strict access control for the agents.”

The DPU, he said, is for “frontier use cases of evaluating models or systems where you might have the guardrails off the models, so it could be for red teaming.”

## Who’s building on it

Anthropic is integrating OpenShell with [Claude Managed Agents](https://claude.com/blog/claude-managed-agents-updates), which already keeps the agent loop on Anthropic’s infrastructure and pushes tool execution into customer-controlled sandboxes.

SpaceXAI says it’s using the platform for Cursor coding agents and Grok models, while Salesforce has added OpenShell audit events and permission approvals into Slack.

SAP is embedding the runtime into Joule Studio and is also contributing code.

OpenAI and Google, two of the four labs whose agents went rogue this summer, aren’t on the partner list. Neither is AWS.

Asked whether Anthropic and OpenAI plan to run OpenShell and Nvidia Sentry for their own training runs, Boitano said to look for the partners’ own blog posts.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)