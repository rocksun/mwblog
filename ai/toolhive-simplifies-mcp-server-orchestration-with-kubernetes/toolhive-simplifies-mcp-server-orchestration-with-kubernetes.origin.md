# ToolHive Simplifies MCP Server Orchestration with Kubernetes
![Featued image for: ToolHive Simplifies MCP Server Orchestration with Kubernetes](https://cdn.thenewstack.io/media/2025/04/53bedadb-toolhive-1024x683.jpg)
The folks at [StackLok](https://stacklok.com/about) have developed a command line utility, called [ToolHive](https://github.com/StacklokLabs/toolhive), to [securely](https://thenewstack.io/building-with-mcp-mind-the-security-gaps/) manage the [Multiple Context Protocol (MCP)](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) servers you may be running in-house, by using [Kubernetes](https://www.thenewstack.io/Kubernetes) and [containers](https://thenewstack.io/introduction-to-containers/).

These days, everyone is [building MCPs](https://blog.cloudflare.com/remote-model-context-protocol-servers-mcp/), which allow large language model (LLM)-based applications [to access data and services](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/) from applications.

Setting up multiple MCP servers, however, can lead to the usual headaches that always come with managing multiple copies of software.

“Setting up and maintaining MCP servers involves navigating a fast-changing landscape with pretty limited tooling, documentation and support,” wrote [Craig McLuckie](https://www.linkedin.com/in/craigmcluckie), one of the[ co-creators of Kubernetes](https://thenewstack.io/beda-burns-and-mcluckie-the-creators-of-kubernetes-look-back/), and CEO and co-founder of [StackLok](https://stacklok.com/?utm_content=inline+mention) a [developer-centric software supply chain service provider](https://thenewstack.io/stacklok-builds-on-sigstore-to-identify-safe-open-source-libraries/), in a [blog post introducing ToolHive](https://www.linkedin.com/pulse/introducing-toolhive-stacklok-labs-project-simplify-craig-mcluckie-zob8c).

ToolHive is an open source project, under an [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0).

## MCP Deployments
“Developers may encounter complexities in installing and configuring these servers, as well as managing updates and ensuring compatibility across different versions,” McLuckie continued.

Each MCP server relies on external packages, such as those from the [Python](https://thenewstack.io/what-is-python/) or Node.js ecosystems, which much be maintained and present when a new server instance is rolled out.

If you want users to log in, then there must be secrets management going on as well. It’s also a good security idea (if not an organizational mandate) for strong isolation across multiple servers. Users must be limited to only those servers they should have access to.

In short, if MCP servers aren’t uniformly deployed, then the resulting variety will be a headache to manage.

## Enter Kubernetes
Fortunately, McLuckie pointed out, we already have an entire stack of tools for deploying and managing applications at scale. Kubernetes, and its[ associated collection of supporting technologies](https://thenewstack.io/cloud-native/), makes a natural choice for managing [MCP servers](https://thenewstack.io/six-reasons-youll-want-to-use-mcp-for-ai-integration/).

The “containerisation and orchestration capabilities provide a strong foundation for isolating and managing MCP instances,” wrote [Chris Burns](https://www.linkedin.com/in/chris-j-burns/?originalSubdomain=uk), a site reliability engineer for [Stacklok](https://thenewstack.io/stacklok-donates-minder-security-project-to-openssf/), in another [blog post introducing ToolHive](https://dev.to/stacklok/toolhive-secure-mcp-in-a-kubernetes-native-world-3o65).

“Kubernetes’ built-in features, such as role-based access control (RBAC), network policies, and secrets management, address the security concerns that deter enterprises,” he wrote.

“Furthermore, the Kubernetes ecosystem, including tools for monitoring, logging, and automated deployment, enables a comprehensive and secure operational environment for MCP servers.”

ToolHive can be the connective tissue between Kubernetes and the world of AI agents.

Written in [Go](https://thenewstack.io/introduction-to-go-programming-language/), ToolHive is packaged as a single binary and can be run from the command line. The team working on it has already committed 26 releases on GitHub, where the project has earned 192 stars.

To run a collection MCP servers, ToolHive uses Kubernetes’ [StatefulSets](https://thenewstack.io/how-to-better-manage-stateful-applications-in-kubernetes/), a workload API object used to manage stateful applications. Applications are defined in a [YAML manifest](https://github.com/StacklokLabs/toolhive/tree/main/deploy/k8s), and housed in [Open Container Initiative](https://thenewstack.io/open-container-initiative-launches-container-image-format-spec/)-formatted containers for uniformity’s sake. They can be easily provisioned once the StatefulSet and pod are up and running.

## MCP Popularity
AI service provider Anthropic [introduced MCP](https://www.anthropic.com/news/model-context-protocol) as an open standard last November as a way to connect [AI assistants](https://thenewstack.io/agentic-ai-is-coming-but-can-your-data-infrastructure-keep-up/) to external sources of content.

Though the initial release was geared to interfacing its LLM-based service, [Claude](https://thenewstack.io/making-the-fediverse-more-accessible-with-claude-3-7-sonnet/), Anthropic touted MCP as an open standard, and the emerging agentic AI community quickly[ ran with the idea](https://www.google.com/search?q=MCP+site%3Athenewstack.io&rlz=1C1PNKB_enUS1122US1122&oq=MCP+site%3Athenewstack.io&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRiPAtIBCDYzOTdqMGoxqAIAsAIA&).

Earlier this week, Anthropic demonstrated how MCPs could be used in a much larger context. The company introduced for its own users a new feature called Integration that uses MCPs to[ fuse third-party services](https://www.anthropic.com/news/integrations) into its own [Claude Desktop](https://claude.ai/download).

Initially, 10 commercial services have been integrated into the desktop: [Atlassian’s Jira ](https://www.atlassian.com/platform/remote-mcp-server)and[ Confluence](https://www.atlassian.com/platform/remote-mcp-server), [Zapier](https://zapier.com/mcp), [Cloudflare](https://github.com/cloudflare/mcp-server-cloudflare/tree/main), [Intercom](https://www.intercom.com/blog/introducing-model-context-protocol-fin), [Asana](https://developers.asana.com/docs/using-asanas-model-control-protocol-mcp-server), [Square](https://developer.squareup.com/docs/mcp), [Sentry](https://docs.sentry.io/product/sentry-mcp/), [PayPal](https://www.paypal.ai/), [Linear](https://linear.app/changelog/2025-05-01-mcp), and [Plaid](https://api.dashboard.plaid.com/mcp/sse).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)