When [AWS](https://aws.amazon.com/?utm_content=inline+mention) launched Elastic Kubernetes Service in 2018, the target audience was early adopters who wanted a managed control plane and to handle everything else themselves. Over the last eight years, that has changed quite a bit.

“We’re starting to get into more the late majority, even the laggards,” said [Mike Stefaniak](https://www.linkedin.com/in/mike-stefaniak/), senior manager of product management for EKS and ECR at AWS. “People come into Kubernetes. They don’t have massive platform teams. They don’t want to manage every single thing themselves.”

VIDEO

In this episode of The New Stack Makers, I sat down with Stefaniak to discuss how AI workloads are reshaping Kubernetes, why AWS open-sourced a Model Context Protocol (MCP) server for EKS, and what’s actually happening with agentic AI in production environments.

## Tool Names Matter

Earlier this year, AWS Labs released an MCP server for EKS as a Labs project.

“Some of the early feedback that I found interesting is that the actual tool names that you’re putting in your MCP server matter quite a bit, where you don’t just necessarily want to copy every API call that EKS has, because the LLM [large language model] can figure that out itself,” Stefaniak explained. “Troubleshooting, runbooks, how to deploy CloudFormation stacks to actually run a full application — that’s much more interesting that we put in our MCP server than just create cluster, deploy pod. We’ve evolved the tool names we launched with quite a bit, and now we’re working on managing it to make it more enterprise-ready.”

The team has also launched a hosted knowledge base that contains years of support cases and internal logs that it can now feed to an agent that may be trying to solve a similar problem. “We’ve seen every possible way that a node can fail, that a cluster can fail. If we can bundle all that into an agent and our MCP server, customers can solve problems without having to open a support ticket,” Stefaniak said.

## Still Experimental, but Getting Real

While “agentic AI” continues to dominate many conference — and especially keynote — conversations, Stefaniak argues that at least for his customers, it’s still very early on in this game. Those customers are still very much focused on regular LLM inferencing on EKS.

“I would say agentic AI is more the frontier,” he noted. “Most users today still have a human in the loop. Troubleshooting cases, for example — let the agent figure it out, give a suggestion. If you’re going so far as to just let the agent try to fix it itself, that’s further than most people are.” 

That’s especially true for customer-facing applications, he said. “The internal platforms, they’re more willing to be bleeding edge because it’s internal. For customer-facing applications, there’s a lot more caution there.”

## What’s Next?

But Stefaniak does believe that this will change soon. “2026 will be the year of production deployments for agentic workloads, whereas 2025 was more traditional LLM inferencing and experimenting with agentic workloads,” he said.

For teams that want to experiment with agentic workloads, he recommends AWS’s open source Strands SDK for writing agents in Python, starting with an external model endpoint. 

His favorite “Hello world” exercise for getting started with agents? Building a Kubernetes troubleshooting agent and then crashing a pod to see how the agent diagnoses the problem.

“It’s quite fun when the thing just goes and looks at logs and metrics, and it’s like, ‘It looks like this image doesn’t exist. There’s a typo. Go fix it.'”

As for his own AI usage, Stefaniak is also increasingly using these agentic tools, he said. 

“If you had asked me six months ago, I would say not much,” he explained. “In the last six months, I honestly feel like I’m working more efficiently with some of these tools. Some of the really helpful use cases I’ve been using internally: BI. I used to have to go figure out SQL tables and SQL queries to go figure out what’s going on with our customers and understand how they’re using our service to make decisions. We have a BI agent that can now understand our tables and I can ask it questions that I’ve been wondering answers to for years, honestly, and it just goes and figures it out for me based on the data that’s already there. That’s been a real, concrete use case internally that I’ve seen speed up the product development process for us.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)