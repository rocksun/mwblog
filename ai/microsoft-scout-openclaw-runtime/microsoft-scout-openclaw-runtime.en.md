Microsoft has the engineers to build its own agent runtime. At Build 2026 last week, it chose not to, [shipping](https://thenewstack.io/microsoft-build-scout/) Scout, its first always-on work agent, on [OpenClaw](https://github.com/openclaw/openclaw), the open-source project an Austrian developer hacked together over a weekend in late 2025. Microsoft is also contributing its enterprise policy controls back upstream to that project.

The decision reads as a concession *only* if you still think the runtime is the valuable part of an agent.

[Agent runtimes](https://thenewstack.io/managed-ai-agent-runtimes/) are starting to behave the way mobile operating systems did once Android arrived. Google released the Android Open Source Project as a free common base, and the money moved to the layers around it: The Play services, the managed identity, the device-management consoles enterprises pay for, and the silicon underneath. Android made handset makers ubiquitous without ever making the base itself a business. OpenClaw is on the same path, and Build showed Microsoft positioning for every layer except the one it just made free.

> OpenClaw is on the same path as Android, and at Build, Microsoft staked out every layer except the runtime it had just made free.

## What Microsoft shipped at Build

Autopilots are Microsoft’s name for always-on agents that act on a user’s behalf with their own governed identity, rather than waiting to be prompted. Scout is the first in that category. It connects to Microsoft 365 data, runs continuously in the background, and can reach a user’s browser and external apps through the Model Context Protocol. Underneath, it runs on the OpenClaw runtime.

OpenClaw plays the role the Android base plays for a phone. A handset maker takes that base and ships a device without rebuilding the kernel, and Microsoft took the OpenClaw runtime and shipped a governed enterprise agent without rebuilding the agent loop. A weekend project became the common base under a product from a company worth more than three trillion dollars.

Build made the layering explicit. OpenClaw now runs natively on Windows inside Microsoft Execution Containers, the kernel-level sandbox Microsoft built for agents. Nvidia is bringing its own [OpenShell](https://thenewstack.io/nvidia-openshell-agent-runtime/) runtime to Windows on the same containment layer, and Nous Research said its Hermes Agent will integrate both. Roughly five months after launch, OpenClaw is the base that Microsoft, Nvidia and a row of agent startups are building on at once.

## The control plane is the product

If the runtime is the free common base, the business is the control plane above it, and that is where Microsoft put almost all of its engineering at Build.

Consider a finance team that wants an agent to reconcile invoices overnight. The loop that reads an invoice and updates the ledger is the easy part; OpenClaw already does it. What the company needs before it lets that agent near the books is a named identity for the agent, a policy that stops it touching anything outside accounts payable, and a log its auditors can read in the morning. None of that lives in the runtime.

On a phone, the layer enterprises pay for sits above the open base: The managed identity, the policy engine, the device-management console. Microsoft built the agent equivalent, wrapped Scout in it, and then made the same wrapper available for agents it did not build.

### Identity

Every Scout agent operates under its own [governed Entra identity](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/), not a shared service account, so each action traces back to an actor the corporate directory already understands. This is the problem the field has been circling for months: the agentic identity crisis, in which autonomous agents act on borrowed or anonymous credentials that nobody can audit. Microsoft’s answer is to issue the agent a directory entry, the way it would for a new hire.

### Governance and policy

Scout ships with a policy-conformance system that continuously checks whether the agent is operating within set guidelines, and each check leaves an audit trail. Microsoft is contributing that conformance work upstream to OpenClaw so organizations running the open project can validate their own deployments. Agent 365 sits atop the control plane, discovering and managing local agents on a managed device, starting with OpenClaw and extending to GitHub Copilot CLI and Claude Code, so even agents Microsoft did not build surface in its console.

### Grounding

Scout runs on Work IQ, the proprietary layer that lets it learn who you work with, which projects are live, and when a decision has stalled, from the signals already inside Microsoft 365. The runtime executes the loop, while Work IQ and Microsoft 365 make the loop useful within a specific company and put the agent where the work already happens.

Across identity, governance, grounding, and distribution, Microsoft kept the layers that a regulated buyer pays for regulated and left the runtime open.

## How Microsoft domesticated OpenClaw

The obvious objection is that OpenClaw makes an odd foundation for an enterprise product. It grew explosively, carries the supply-chain risk that comes with any fast-moving open ecosystem, and was alarming enough on security that Microsoft once [advised](https://thenewstack.io/persistent-ai-agents-compared/) against running it on standard work machines. That history is the reason the move matters.

Rather than hand raw OpenClaw to corporate users, Microsoft wraps the runtime in the things enterprises already trust: directory identity, device policy, compliance logs, security review, and Microsoft 365 context. OpenClaw enables Scout to act. What lets it act inside a bank or a hospital is the identity, policy and isolation a CIO can sign off on, and that wrapper is Microsoft’s, not the runtime’s. A runtime can make an agent capable, but only identity, policy, auditability and isolation make it acceptable, and those are Microsoft businesses.

## Containment and silicon are the new floor

The other place value collected is beneath the runtime, in containment and silicon. On a phone, the layer below the operating system is the chipset and the secure enclave, the hardware that decides what software is allowed to do at all. The agent stack now has the same floor.

### Containment as an operating-system primitive

[Microsoft Execution Containers](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/) push agent sandboxing into the Windows kernel, letting IT declare what an agent can touch across files, network, and applications, and enforcing it at runtime rather than trusting a prompt to behave. I would argue this matters more than Scout itself, because it makes Windows the place where agent permissions get enforced for any runtime, not only Microsoft’s. OpenClaw, OpenShell, Manus and Hermes all plug into the same boundary.

### Silicon and the on-device floor

Nvidia’s [OpenShell](https://developer.nvidia.com/blog/build-personal-ai-agents-on-windows-pcs-with-new-tools-from-microsoft-and-nvidia/) runs inside the same containers and uses MXC for policy management and inference routing, aimed at always-on agents on Windows hardware. Microsoft is also shipping a Surface developer box built around Nvidia’s RTX Spark silicon. Together, the chips and the sandbox determine how safely an always-on agent can run on a laptop, a question the runtime by itself cannot answer.

Containment has moved into the operating system as a runtime primitive, which makes the OS and the silicon the enforcement floor for every agent, regardless of the runtime that sits on top.

## Where not to build a company

For a team deciding where to spend its own effort, the phone era is the cautionary tale. You would not fork Android to ship an app, and you would not try to out-build the Play store. You would build on the base and invest where you can differentiate or where compliance forces your hand. The same map now applies to agent runtimes.

| Scenario | Recommended focus | Rationale |
| --- | --- | --- |
| Shipping an enterprise agent | Adopt an open runtime, invest in identity and policy | Buyers pay for auditability, not the agent loop |
| Building a consumer or local agent | Adopt a runtime, focus on grounding and experience | Differentiation usually sits in context, not the loop |
| Selling into regulated industries | Prioritise containment and attestation | OS-level enforcement is becoming table stakes |
| Trying to own the runtime layer itself | Reconsider, or contribute upstream instead | Margin and lock-in have largely left this layer |

Real teams will combine these, and a startup might still keep a thin runtime fork for a real technical edge, the way [NanoClaw](https://thenewstack.io/nanoclaw-minimalist-ai-agents/) trimmed OpenClaw to roughly 2,000 lines for auditability. Even so, a company whose whole product is the agent loop now looks like Android without the Play store, widely adopted and hard to bill for on its own.

## Why a weekend project became the shared base

The reason OpenClaw became the common base says something about how this market treats whoever wins a layer. Steinberger built one of the fastest-growing open-source agent projects of the year, [joined](https://decrypt.co/369781/microsoft-scout-openclaw-enterprise-ai-agent) OpenAI in February and moved the project to an independent foundation to keep it open, with OpenAI sponsoring the work. So Microsoft now ships its flagship agent on a runtime within OpenAI’s orbit, at the same moment it trains its own in-house MAI models to rely less on OpenAI. Nvidia, Manus and Nous Research are on the same base.

The license makes it possible. OpenClaw ships under MIT, which lets Microsoft embed it, govern it and sell around it without asking permission. Steinberger has been candid about wanting to change the world rather than build a large company. He got the first half. The platforms wrapped the meter, the directory and the policy engine around his runtime and kept the second.

## What’s next

For developers tracking the agent stack, the shape is now familiar from the phone era: an open common base in OpenClaw, the way Android sits under every handset; a paid control plane of identity, governance, grounding and distribution above it; and an enforced floor of containment and silicon below. Scout is the first big product to make all four layers visible at once.

The harder question is whether winning the runtime is enough to build a business, and Build suggests it is not. Microsoft has not said whether Scout belongs in a Copilot subscription or is billed separately, and the move to consumption pricing for agent work, the same [token tax](https://thenewstack.io/managed-openclaw-serverless-agents/) developers have complained about all year, will decide how much the control plane is worth. Open-infrastructure economics are pulling the runtime down faster than most vendors planned for. The layer that pays is the one Microsoft spent Build building, and I will be watching whether anyone can still charge for the runtime once Autopilots reach general release.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)