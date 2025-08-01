The rapid adoption of generative AI tools, AI agents and AI coding tools is creating a [new threat vector](https://thenewstack.io/navigating-the-turbulent-waters-of-ai-security/) that security teams have to grapple with. [Pangea](https://pangea.cloud/), which started out in 2021 as a more traditional service for securing cloud apps, today launched its AI Detection and Response (AIDR) service in preview, which aims to tackle exactly these problems that many enterprises now face. It allows security teams to detect, monitor and secure generative AI applications across the enterprise, no matter whether that’s employee AI use (authorized or shadow AI), internal AI applications and more.

“When viruses and malware first came out in the 80s and 90s, that was a new threat, and we had to create new detection technology to detect that threat, because it didn’t exist before,” said Pangea CEO [Oliver Friedrichs](https://www.linkedin.com/in/oliverfriedrichs/). “I think in this case, it’s very similar. Now words are weapons instead of the bytes that we used to detect with antivirus products — and now we have to create new detection logic and policy frameworks to enforce AI governance and detect AI threats.”

[![](https://cdn.thenewstack.io/media/2025/07/273ecc76-screenshot-2025-06-25-at-6.24.00%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/07/273ecc76-screenshot-2025-06-25-at-6.24.00%E2%80%AFpm.png)

Image credit: Pangea.

Friedrichs is the right person to draw these comparisons. He founded and co-founded four security companies and has a deep background in antivirus and anti-malware software (and exits to McAfee, Symantec, Sourcefire and Splunk). He argues — and many would surely agree — that as enterprises race to adopt this new technology, security is often an afterthought.

## The AI Security Threats Security Teams Face Today

The threat is different, too, and quite different from what most security teams are familiar with. Friedrichs noted that most of Pangea’s client are mostly worried about two different issues. The first is prompt injection attacks, which can trick the model into providing data it shouldn’t or execute malicious actions, being top of mind for most security teams. But, and this is more familiar to most security teams, the other main threat is employees using third-party AI tools and feeding confidential data into these services.

“The security team, they’re concerned about employees and the workforce accessing third-party AI models. Prompt injection is definitely a concern there, but they’re more concerned about their employees leaking personally identifiable information, confidential information, or getting malicious content back and bringing that back into the enterprise,” Friedrichs said. “There’s two very different aspects of AI security — and sometimes they’re combined.”

Having the models respond with malicious content isn’t yet a widespread issue, but Friedrichs noted that a malicious actor could potentially poison a dataset and feed a malicious link into the model’s training data or, as is maybe more likely, a third-party tool or malicious Model Context Protocol (MCP) server that the model or agent accesses.

[![](https://cdn.thenewstack.io/media/2025/07/a6605bde-screenshot-2025-06-25-at-6.40.55%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/07/a6605bde-screenshot-2025-06-25-at-6.40.55%E2%80%AFpm.png)

Image credit: Pangea.

What Pangea has built is a set of tools that sit on top of its [AI Guard](https://pangea.cloud/services/ai-guard/) service. This service is essentially a proxy that developers can call over an API, sitting between the application and the LLM or agent. To detect this malicious — or simply undesirable — content and stop confidential data from leaking into the models, Pangea itself uses smaller LLMs that keep the latency low but are still smart enough to detect potential issues.

The company also partners with the likes of Crowdstrike to gather additional threat intelligence so that it can filter out malicious URLs and IP addresses in the prompt.

## Pangea AIDR

Now, with the AIDR platform, Pangea wants to give enterprises a more end-t0-end solution for monitoring and securing how AI is used in their workflows. To do this, the company has to deploy sensors across a wider range of endpoints. Among other things, this means that today, it is also launching a Chrome extension to guard against shadow AI usage, as well as sensors for gaining visibility into agentic frameworks and SDKs, and an MCP proxy for internally built agents. The team also built integrations with existing AI gateways from [Kong](https://konghq.com/?utm_content=inline+mention), LiteLLM, Portkey and others, which allows it to add its security services at this point as well. There’s also an SDK for developers who want to build Pangea directly into their applications and in the near future, the team plans to support additional browsers like Microsoft Edge and additional AI touchpoints.

“It does require different knowledge and experience to detect those types of threats,” Friedrichs said. “But then, the other half is just everything we’ve done before. It’s just another thing to monitor. We always used to say at the network, we want to apply visibility and control of network traffic, and now we are saying we want to do the same thing for Gen AI traffic.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)