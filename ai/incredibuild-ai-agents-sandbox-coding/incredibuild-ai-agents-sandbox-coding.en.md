Somewhere out there, a developer is walking around with their laptop half-open, so their AI coding agent doesn’t die.

That’s the state of enterprise AI development in 2026 — and the problem [Incredibuild](https://www.incredibuild.com/) is trying to fix with Islo, a sandbox that gives every agent its own persistent, isolated cloud environment.

The company, best known for its [build acceleration platform](https://www.incredibuild.com/glossary/build-acceleration) used by Microsoft, Take-Two, and Nintendo, has announced Islo, a sandbox purpose-built for [AI coding agents](https://thenewstack.io/ai-coding-agents-level-up-from-helpers-to-team-players/).

The goal is to give every agent its own dedicated, isolated cloud environment, governed by explicit policies, so engineering teams can run agents continuously without the security and governance headaches that come with letting them loose on developer machines or unmanaged infrastructure.

## Agents don’t fit the one developer, one machine model

“Coding agents are capable of doing real work now, but they all run on the developer’s laptop,” [Adam Gold](https://www.linkedin.com/in/adamgold7/), Director of Product Engineering at Incredibuild, says in a press release. “That means they die when the lid closes, and they have access to everything on the machine.

“We built Islo because we believe that every AI agent needs its own computer — not an ephemeral container, but a long-running dev environment with its own running services, scoped credentials, and a lifecycle that doesn’t depend on human supervision.”

> “We built Islo because we believe that every AI agent needs its own computer”

The “every agent needs its own computer” statement is more than a tagline. The current industry model is one developer, one machine — which works because a developer is a single, supervised actor who sits down, does the work, and comes back the next day.

However, agents break that model in three specific ways, according to the company. Their lifecycles don’t match human ones — people are reportedly walking around with laptops half-open so agents keep running, which the company flatly describes as “not a workflow.” They carry a large blast radius, inheriting all the credentials a developer has accumulated — SSH keys, AWS profiles, browser cookies — with none of the judgment about when not to use them. And they need warm, persistent environments with running services, databases, and build caches that ephemeral containers throw away on every run.

## Not Codespaces, not a container

What Incredibuild is building toward is a persistent, addressable machine per agent — with its own scoped credentials and a lifecycle that doesn’t end when a human goes to dinner.

That distinction also separates Islo from the closest existing alternatives, the company says. Cloud dev environments like [GitHub Codespaces](https://thenewstack.io/codeanywhere-founders-take-on-github-codespaces-with-daytona/), [Daytona](https://thenewstack.io/codeanywhere-founders-take-on-github-codespaces-with-daytona/), and [Coder](https://thenewstack.io/self-hosted-cdes-preferred-to-saas-in-large-orgs-says-coder/) were built for humans — they assume an IDE is attached, idle out, and operate on the security premise that the developer is trusted.

Ephemeral sandboxes are optimized for sub-second cold starts and designed to be torn down, the company says. Islo is built around the opposite assumption: the agent is the principal user, sessions are persistent with no session ceiling, and there’s a policy layer between the agent and everything outside the sandbox.

## Choke points, not policy languages

That policy layer is worth understanding in some detail, because “granular policy control” could mean almost anything, Incredibuild says. In Islo’s case, it doesn’t mean a policy language like [Open Policy Agent](https://www.openpolicyagent.org/) or [Cedar](https://thenewstack.io/all-about-cedar-an-open-source-solution-for-fine-tuning-kubernetes-authorization/) — it means enforcement at specific, well-defined choke points.

The network gateway sits outside the [VM](https://thenewstack.io/the-future-of-vms-on-kubernetes-building-on-kubevirt/) and handles every outbound call the agent makes. Enterprises configure an allowlist of hosts, ports, and methods, and the agent has no way around it because the gateway is outside its control. The filesystem boundary enforces read and write rules per path — an agent might be permitted to write to /workspace, but blocked from reading `~/.ssh` or `~/.aws`. An audit log records every shell command, file change, network call, and credential use.

The choke points are independent, so teams can run a wide-open network policy alongside a tight filesystem policy depending on what a given agent is doing.

## Credential-blind by design

Credential handling follows a similar logic of keeping enforcement outside the agent’s reach. Credentials never live in the sandbox — not in the VM image, not in environment variables, not in the agent’s filesystem.

The sandbox is what Incredibuild calls “credential-blind.” Instead, a host-side proxy sits outside the VM and injects credentials at the network boundary based on the agent’s identity and per-sandbox policy. The agent makes API calls without credentials; the Islo gateway attaches them per request.

“We’ve spent years helping teams ship quickly,” [Shimon Hason](https://www.linkedin.com/in/shimon-hason/), CEO of Incredibuild, says in a press release. “Islo is making sure AI can ship safely. We’re introducing a missing layer in the stack: a super-powered sandbox that provides the infrastructure necessary for organizations to safely run AI agents as part of real production workflows.”

## Pricing and availability

While Islo can run independently, Incredibuild is positioning it alongside its existing acceleration technology to speed up compute-heavy steps in build, test, and [CI/CD](https://thenewstack.io/ci-cd/) workflows. The company is also targeting AI research workflows through a partnership with the [Harbor Framework](https://www.harborframework.com/) community — an open-source infrastructure project for authoring and executing agent benchmarks and evaluations.

Islo launches with three tiers: a free plan supporting up to five concurrent sandboxes; a Team plan at $0.07 per CPU-hour and $0.04 per GB-hour supporting up to 50 concurrent sandboxes; and an Enterprise tier with custom packages. The company says it is working with a small group of design partners through a private beta.

Islo is available now at islo.dev. Incredibuild serves more than 600 customers across its platform. Whether the market is ready for that missing layer in the stack is a question the private beta will start to answer.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)