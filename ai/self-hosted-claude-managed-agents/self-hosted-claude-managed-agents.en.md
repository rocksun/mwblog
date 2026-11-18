![A finger on the button, depicting roll-backs and kill-switches.](https://cdn.thenewstack.io/media/2026/11/2876cde1-public-domain-vectors-grxqbf6y-dq-unsplash-1024x646.jpg)

Anthropic has unveiled a self-hosted version of its platform for building and running AI agents.

[Self-hosted Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/self-hosted), as it’s aptly called, is available now in private beta. Customers host both the server that coordinates the agents and the sandboxes where the agents run their tools, either in their own cloud account or in an on-premises data center. Credentials and session histories stay on their infrastructure, while requests to Claude go to the inference provider they configure.

While the benefits of self-hosting are evident, particularly for companies handling sensitive data, the [accompanying license](https://www.anthropic.com/legal/self-hosted-managed-agents-license) comes with a number of notable caveats that may give some customers pause — this includes strict deadlines for responding to safety notices, limits on which models customers can use, and rules against preventing certain types of data from being sent to Anthropic.

## Claude’s road to self-hosting

Back in April, Anthropic [debuted Claude Managed Agents](https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/), a hosted service for building and running AI agents. The following month, the company [launched self-hosted sandboxes](https://thenewstack.io/anthropic-mcp-tunnels-sandboxes/), which let customers run agents’ tools on their own infrastructure while Anthropic continued to run the Claude Managed Agents server.

With self-hosted Claude Managed Agents now in the mix, customers can run that server themselves, too, and store session histories in their own database.

In a [blog post](https://claude.com/resources/articles/self-hosted-claude-managed-agents) marking the launch, Anthropic says agents are taking on more consequential engineering tasks, including repairing failed builds, checking releases and deciding which alerts need attention. That work can require access to sensitive systems, such as private code repositories and internal build and release systems.

> “For agents with that level of access, some teams want the whole service in their own environment, not just the sandbox.”

“They run unattended on your code and need access to your internal systems,” the company writes. “For agents with that level of access, some teams want the whole service in their own environment, not just the sandbox. Until now, that meant building the platform themselves.”

Several companies have done exactly that. Spotify [developed Honk](https://engineering.atspotify.com/2026/6/code-with-claude-coding-is-no-longer-the-constraint), which runs Claude through the Agent SDK inside Spotify’s own harness. The company deploys Honk in Kubernetes pods in its cloud environment, giving it access to its internal CI systems so it can run builds and verify its code changes.

Anthropic’s new offering packages much of that work into a product. Customers run Anthropic’s server and the sandbox workers in their own cloud or data centre, with PostgreSQL if they want to retain session histories across restarts, while their developers use the same core APIs as they do with the hosted service. The local server can send requests to Claude through Anthropic’s API, a cloud provider such as Amazon Bedrock or Microsoft Foundry, or the company’s own gateway.

## The devil in the detail: 8 hours to act

While Anthropic’s formal announcement emphasizes *why* companies might want to host the service themselves, digging into the details of the license reveals how much control Anthropic retains over the software once it’s deployed.

For starters, Anthropic ships the server as a proprietary binary that customers can’t modify, meaning that they can’t patch or customize the server code themselves. They *can* route requests through their own gateway, but only to Claude models. The license also bars models from other developers unless Anthropic expressly permits them, and [the public inference docs](https://platform.claude.com/docs/en/managed-agents/self-hosted/inference-provider) list only Claude models.

Among the most notable terms of the license is how little time customers have to act on Anthropic’s safety notices. If the company flags a safety, security or misuse risk in writing, customers have just eight hours to disable the affected feature or roll back the version across every deployment. They also have one business day from delivery to install a designated safety update.

![§5.3 Eight hours to roll back or disable](https://cdn.thenewstack.io/media/2026/11/a589ff56-safety-rollback-screenshot-with-torn-edges-1024x172.png)

§5.3 Eight hours to roll back or disable

[Patrick Moorhead](https://www.linkedin.com/in/patmoorhead/), founder and chief analyst at [Moor Insights & Strategy](https://moorinsightsstrategy.com/), says the eight-hour deadline is tighter than the time most large enterprises typically allow to make production changes.

“Self-hosted usually means the customer owns the change window,” Moorhead tells *The New Stack*. “This license flips that.”

> “Self-hosted usually means the customer owns the change window. This license flips that.”

Even within the Claude model lineup itself, access can vary. The license says Anthropic can decide, on safety grounds, that some or all of a licensee’s customers should access certain Claude models *only* through Anthropic’s hosted service.

![§5.6 Anthropic can reserve models for hosted access](https://cdn.thenewstack.io/media/2026/11/407f225c-5.6-access-path-original-screenshot-1024x289.png)

*§5.6 Anthropic can reserve models for hosted access*

Moreover, the license bars customers from blocking or altering what it calls “usage signals,” the observability data the software may send to Anthropic. The company can use this data to measure how much the software is used and to monitor compliance with the agreement.

> “The idea is that if you build an agent that is breaking the law or causing harm you cannot stop us [the model lab] from figuring that out and doing anything about it.”

[Jason Andersen](https://www.linkedin.com/in/jasontandersen/), also an analyst at Moor Insights & Strategy, says the telemetry clause and the separate requirement to maintain safeguards Anthropic specifies are broadly in line with how cloud vendors would try to prevent misuse.

“The idea is that if you build an agent that is breaking the law or causing harm you cannot stop us [the model lab] from figuring that out and doing anything about it,” Andersen tells *The New Stack*.

![§5.9 Customers can’t block usage signals](https://cdn.thenewstack.io/media/2026/11/a8419896-5.9-usage-signals-screenshot-1024x270.png)

*§5.9 Customers can’t block usage signals*

## The security backdrop

In July, [Anthropic disclosed](https://thenewstack.io/anthropic-claude-containment-failure/) that Claude models had gained unauthorized access to real computer systems during cybersecurity evaluations. That same month, [OpenAI had disclosed](https://thenewstack.io/openai-huggingface-sandbox-breach/) that models undergoing internal tests had bypassed isolation controls and breached systems at Hugging Face.

While a model provider can address a problem on its side, an agent running on a customer’s servers may keep operating. And so the customer may also need to take action to contain the problem.

“I do think that this is Anthropic putting more teeth around safety to limit their exposure which is effectively what a license does,” Andersen says. “It does not really change the risk of the technology it makes or those who use it to make agents.”

## How enterprise buyers might respond

The long and short of all this is that Managed Agents now comes in three forms: fully-hosted by Anthropic, hosted by Anthropic with customer-run sandboxes, and now fully self-hosted.

Whether that third option works for buyers depends on what they need from self-hosting in the first place. Moorhead expects regulated buyers to push back on both the rollback deadline and the telemetry terms.

“It’s workable for companies already comfortable running Claude as a cloud service, and they’ll treat this as a cloud service that happens to sit in their data center,” he says. “For banks, government and sovereign buyers, expect procurement and legal to push back on sections 5.3 [safety rollback] and 5.9 [usage signals].”

Andersen, for his part, says the terms are “a reasonable ask” for enterprises, and doubts they’ll slow adoption overall, given that buyers who need full control over their agents would likely be looking elsewhere already.

“If you needed that level of control on your agents, you would likely consider a more independent, possibly open-weight solution,” he says.

The post [Anthropic now lets you self-host Claude Managed Agents. The catch? 8 hours to act if it flags a safety risk in the software](https://thenewstack.io/self-hosted-claude-managed-agents/) appeared first on [The New Stack](https://thenewstack.io).