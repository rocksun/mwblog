After a [short public preview](https://aws.amazon.com/blogs/aws/modernize-your-workflows-amazon-workspaces-now-gives-ai-agents-their-own-desktop-preview/), AWS on Tuesday made its [Amazon WorkSpaces for Agents](https://aws.amazon.com/workspaces/ai-agents/) — which you should definitely not confuse with [Amazon Connect Agent Workspace](https://aws.amazon.com/products/connect/customer/agent-workspace/) — generally available. Amazon WorkSpaces are AWS’s persistent cloud-based desktops for enterprises that want to provision virtual desktops to their employees. WorkSpaces for Agents are also virtual desktops, but meant for agents that need to operate desktop applications in the cloud.

## Agents get their own desktops

Ideally, this means an agent could now, for example, interact with a company’s legacy desktop apps without the need for building custom integrations or modernizing those tools.

AWS’s reference customer for this launch is Dutch multinational Wolters Kluwer.

“Our teams manage complex tax, legal, and compliance workflows for customers around the world. Amazon WorkSpaces now lets us put AI agents directly into those workflows — they can access and operate the same business applications our people use, without us having to rebuild anything,” notes André Akkerman, the director of Workplace Technology at Wolters Kluwer, in today’s announcement. “It’s a meaningful step forward for how we think about automation.”

Once enabled, agents can connect to these desktops with the help of the Model Context Protocol (MCP). From there, they can stream their sessions and interact with the desktop apps as needed. Access is managed by AWS’s Identity and Access Management service and auditability is handled by AWS CloudTrail and Amazon CloudWatch.

## MCP + computer vision

AWS argues that MCP and computer use agents, which are still rather slow (since they have to constantly loop through analyzing screenshots and then taking action), are complementary approaches.

The way AWS is currently doing this is by having users install a filesystem MCP server on their WorkSpace when they create the main OS image for the service. With this, the agent can then read and write files through tool calls and doesn’t have to go through the screenshot loop.

“The right design pattern routes each subtask to the most efficient interface available—calling an MCP tool when one exists, and falling back to vision-driven action only when no API covers the task or when interacting with the GUI is itself the goal,” the company explains in its announcement. “There is a compounding benefit: when most of a workflow routes through MCP, the remaining visual subtasks shrink to focused operations — fewer steps, shorter sequences, fewer failures. MCP tool forwarding makes this pattern work inside a WorkSpaces Application instance.”

## Humans in control

With the launch into general availability, AWS is also adding the ability for humans to watch the agents and take control when needed.

“If you observe the agent performing an unexpected action, the stop button gives you direct intervention without restarting the session or rolling back state. As you move from development to production, you can decide which mode fits each workflow based on how much human oversight the task requires,” the company explains.

Given how slow computer use agents still are at this point, no human will want to babysit these agents for long and that’s not a good use of anybody’s salary either. So if a lot of oversight is needed for a given task right now, chances are this is not a great way forward for that workflow.

## Giving agents an identity

With this launch, AWS is also allowing enterprises to use Active Directory to give agents an identity — with the corresponding policies, access controls, and audit logs — that these companies already use for regular users.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)