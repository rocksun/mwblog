Like the idea of OpenClaw-style agents, but their insecurity makes you sweat? The combo of NanoClaw and Docker Sandboxes may be just what you need.

[OpenClaw gets all the hype](https://thenewstack.io/openclaw-github-stars-security/), but people who haven’t drunk the OpenClaw Kool-Aid know its security is abysmal. That’s where [NanoClaw](https://github.com/qwibitai/nanoclaw), the open‑source, security‑focused AI agent runtime designed to run inside isolated containers rather than directly on your host machine, comes in.

[NanoClaw is positioned as a minimalist, production-ready alternative to OpenClaw](https://thenewstack.io/nanoclaw-minimalist-ai-agents/), with a much smaller, more auditable codebase and an architecture built around per-agent isolation. Now locking it down further, its developers have partnered with [Docker](https://www.docker.com/) to run with Docker’s emerging microVM-based [Docker Sandboxes](https://docs.docker.com/ai/sandboxes/).

Docker has spent the past year casting Docker Sandboxes, an experimental Docker Desktop feature, as a secure execution substrate for AI coding and task agents. This is a [shift from simple container isolation to dedicated MicroVMs](https://www.ajeetraina.com/docker-sandboxes-containers-vs-microvms-when-to-use-what/) with private Docker daemons. Sandboxes are currently supported on macOS (Apple Silicon) and Windows, with Linux support rolling out in the coming weeks.

Each sandbox now runs in its own lightweight MicroVM, with its own kernel and Docker engine. This enables your agents to install packages, build images, and run containers without touching the host Docker daemon or the host filesystem. The company pitches this as “defense in depth” for autonomous agents.

Thus, even if an agent pulls off a container escape or exploits a zero-day in its environment, the damage is confined to the MicroVM boundary rather than the developer’s laptop or CI runner. Is it a heck of a lot safer than OpenClaw’s “Security? What security approach?”

This integration enables you to deploy NanoClaw-based agents into isolated sandbox environments with a single command. NanoClaw targets a fast-growing class of AI agents that don’t just answer questions but connect to live data, execute code, and take actions on behalf of users and teams.

That expanded scope raises the stakes for isolation and blast-radius control, as a single compromised agent can potentially access credentials, session histories, or data owned by other agents when they share a host. NanoClaw plus Docker Sandboxes is designed explicitly to address that risk.

According to [Gavriel Cohen](https://www.linkedin.com/in/gavrielco/), NanoClaw’s creator, in a blog post:

*When you’re building with [AI agents, they should be treated as untrusted and potentially malicious.](https://nanoclaw.dev/blog/nanoclaw-docker-sandboxes) … The right approach is an architecture that assumes agents will misbehave and contains the damage when they do. That principle drives every design decision in NanoClaw. Don’t put secrets or credentials inside the agent’s environment. Give the agent access to exactly the data and tools it needs for its job, nothing more. Keep everything else on the other side of a hard boundary. With Docker Sandboxes, that boundary is now two layers deep. Each agent runs in its own container (can’t see other agents’ data), and all containers run inside a micro VM (can’t touch your host machine). If a hallucination or a misbehaving agent can cause a security issue, the security model is broken. Security has to be enforced outside the agentic surface, not depend on the agent behaving correctly.*

[Mark Cavage](https://www.linkedin.com/in/mcavage/), Docker’s President and COO, says in a press release that, “Every organization wants to put AI agents to work, but the barrier is control: what those agents can access, where they can connect, and what they can change. “Docker Sandboxes provide the secure execution layer for running agents safely, and NanoClaw shows what’s possible when that foundation is in place.”

Cohen adds in the press release that “We are at the beginning of a shift where every team, in every organization, will have their own team of AI agents doing real work on its behalf. NanoClaw was built to make that a reality today, and Docker Sandboxes is what makes it a reality that organizations can actually trust.”

Companies are growing increasingly wary of running agents that can execute arbitrary code, install packages, or invoke cloud APIs without strong containment. [MicroVM-based isolation using such programs as Firecracker, Sandboxes, or Kata Containers is emerging as a de facto standard](https://northflank.com/blog/how-to-sandbox-ai-agents) for protecting hosts from AI-generated code. In this approach, containers alone are reserved for trusted internal automation.

By combining Docker’s MicroVM sandboxes with NanoClaw’s minimal attack surface and an auditable open-source codebase, the two companies are pitching their integration as ready for enterprise security reviews. The stack is designed so that if an agent attempts a container escape or triggers an unknown exploit, it still runs within a disposable, MicroVM-backed sandbox that can be reset without affecting other workloads or leaking host secrets. Critics have noted that sandboxing alone is insufficient for “agent safety.”

They emphasize the need for fine-grained authentication and authorization on top of it. Neither Docker nor NanoClaw would argue with that, but they maintain that strong isolation is the necessary foundation for any higher-level security controls. They’re not wrong.

To get started with NanoClaw on Docker Sandboxes, developers can visit [NanoClaw’s GitHub repository](https://github.com/qwibitai/nanoclaw) and the official [Docker Sandboxes documentation](https://docs.docker.com/ai/sandboxes/get-started/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)