# Meet Kagent, Open Source Framework for AI Agents in Kubernetes
![Featued image for: Meet Kagent, Open Source Framework for AI Agents in Kubernetes](https://cdn.thenewstack.io/media/2025/03/97083fee-kagent-icon-1-copy-2-1024x576.png)
[Solo.io](https://solo.io?utm_content=inline+mention), a cloud native application networking company, today announced kagent, a new open source framework designed to help users build and run [AI agents](https://thenewstack.io/ai-agents/) to speed up Kubernetes workflows.
[Kagent](https://kagent.dev/), aimed at [DevOps](https://thenewstack.io/devops/) and [platform engineers](https://thenewstack.io/platform-engineering/), offers tools, resources and AI agents that can help automate tasks such as configuration, troubleshooting, observability and network security.
The framework integrates with other cloud native tools through an architecture built on the [Model Context Protocol (MCP)](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/). MCP, introduced by Anthropic in November, is intended to standardize how AI models integrate with APIs.

Kagent, built on [Microsoft’s](https://news.microsoft.com/?utm_content=inline+mention) open source framework [AutoGen](https://thenewstack.io/a-developers-guide-to-the-autogen-ai-agent-framework/), holds an [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) open source license.

The project began as an internal solution to a customer problem, according to [Lin Sun](https://thenewstack.io/author/lin-sun/), Solo.io’s senior director of open source.

“We have hundreds of customers who are either running our gateway or mesh solutions,” Sun told The New Stack. “So as we were working with these customers, we have our internal supporting team. They are the face to work with these customers, and they help customers figure out what’s the right solution in the cloud native ecosystem? They help customers solve general problems and also domain-specific problems.”

In the wake of Hurricane Helene’s destructive path last fall through the U.S. Southeast, an insurance company that was a client of Solo.io’s reached out for help, after the insurer’s customers began trying to file online claims on their damaged homes.

“That weekend our team was called in for help, because there was some issue with the production side, and we were jumping to troubleshooting and try to identify where there are, like, 10 network hops. And where is the problem in that network hub?”

Solo.io’s customer-facing engineers wound up tapping its resident experts — who have deeper knowledge of Istio, Envoy, etc. — to help untangle the insurance company’s problems.

“That’s why we started thinking: how can we make ourselves more productive, as we continue to scale out as a company?” Sun said. “We added more customers to our list. So how do we leverage our in-house expertise more efficiently?

“We were thinking, how can we actually clone some of these experts? So we don’t have to pull them [in] for these critical situations, so that they can be either having a peaceful weekend, or they could focus on writing code and make their focus on innovation.”

## A Wish List for the Community
Solo.io, which builds its products on open source projects, intends to donate kagent to the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention), Sun said. If this happens, it would follow the company’s donation in November of Gloo Gateway, a popular open source API gateway, to the CNCF.

The project, now called [kgateway](https://kgateway.dev/), was named an official CNCF Sandbox project this month.

Kagent’s initial launch includes tools for Argo, Helm, Istio, and [Kubernetes](https://thenewstack.io/kubernetes/), along with a Grafana and Prometheus [observability](https://thenewstack.io/observability/) tool. It also includes a cloud native expert knowledge base that can extend with any MCP-compatible tool server.

The framework includes three layers:

**Tools:**AI agents can use pre-defined functions, including a curated knowledge base, availability and performance metrics for services, controls for app deployment and life cycle, utilities for platform administration and debugging, and app security guardrails.**Agents:**Autonomous systems that can plan and implement such tasks as canary deployments for new versions of a user’s applications, establishing a[Zero Trust security](https://thenewstack.io/what-is-zero-trust-security/)policy for every service in a Kubernetes cluster, and debugging service failures.**A declarative API and controller:**This allows the user to build and run agents via their UI, CLI and declarative configuration.
“What we are hoping for is this kagent as an inspiration for the community,” Sun said. “We seeded the project with a few sample agents, a few tools and also a framework integrated with Kubernetes. And then we’re hoping the rest of the community can help us enhance what we build, and also help us [add additional agents](https://kagent.dev/tools) to the catalog to greatly benefit the rest of the ecosystem.

“What I’m envisioning is, for every critical CNCF projects or cloud native projects out there, we have an agent in the catalog, so that when a new user comes to the cloud native landscape, they can have a project-specific agent sitting next to them, and they could even call multiple agents.”

Sun has an extensive wish list. In addition to urging users to try the existing tools and agents and contribute improvements, she offers other ideas.

“We want to have some tracing capability and maybe have some integration with [[OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/)]. We want to have more metrics for kagent. We would also like to have a feedback system.”

And there’s more: ”We also would love to add multi-agent support. Right now, as part of the initial launch, we focus on single agent, but the framework is designed to support multiple agents.”

Sun would also like to add support for multiple [large language models](https://thenewstack.io/llm/). “Right now the support is focused on OpenAI, which we believe is one of the best large language model out there. We do think it will work for other large language models as well. But we’ve only focused on testing.”

Developers interested in contributing to the project can connect via the CNCF Slack’s #kagent channel. Sun also encouraged people to stop by Solo.io’s booth — number S150— at [KubeCon + CloudNativeCon Europe 2025](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/), April 1-4.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)