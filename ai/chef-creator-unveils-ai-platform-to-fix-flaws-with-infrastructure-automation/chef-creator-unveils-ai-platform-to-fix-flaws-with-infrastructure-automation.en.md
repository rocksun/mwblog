For the past six years, [Adam Jacob](https://www.linkedin.com/in/adamjacob/), the original author of [Chef](https://www.chef.io?utm_content=inline+mention), has been working on a solution for how Chef and other tools in that generation of infrastructure automation fell short.

“One of the things we saw was that, especially in the large enterprise, the results just weren’t holding up over time, because the complexity of the automation itself was getting in the way,” Jacob told The New Stack.

The key to streamlining that complexity, he felt, lay in natural language: “Our initial hope was that we could find a way to allow a user to express in their own semantics, in their own words, what it was they were trying to do, and then let the system infer, through constraints, what it was that they intended.”

But it wasn’t until the [generative AI (GenAI) boom erupted](https://thenewstack.io/generative-ai-is-just-the-beginning-heres-why-autonomous-ai-is-next/) that that vision could be realized.

Today, [System Initiative](https://www.systeminit.com/), the [startup Jacob co-founded in 2019](https://thenewstack.io/system-initiative-a-devops-makeover-by-ex-chef-adam-jacob/) with [Mahir Lupinacci](https://www.linkedin.com/in/mahirlupinacci/), has announced what it is calling the world’s first AI-native infrastructure automation platform. The platform allows engineers to collaborate directly with AI agents — and with each other — to manage infrastructure using GenAI prompts.

Through natural language prompts, platform users can inventory resources and relationships. The platform pairs AI agents with digital twins of live infrastructure to let users tell the platform which outcomes they want. The platform’s AI then devises a solution and runs a simulation on a digital twin of the system’s real infra. If the solution isn’t right, users can iterate on it if necessary and, ultimately, approve the solution for live deployment.

“People use it to fix all sorts of problems — to do security and compliance analysis, to troubleshoot production outages, performance issues, to deploy their applications using natural language, with all their best practices attached,” said Jacob, System Initiative’s CEO.

The platform can also work as an automated help desk — not just tracking the requests for support, but creating a simulated solution that can be implemented for real within minutes.

As Jacob showed TNS a demo of how the automated help desk works, he observed, “One of the [proofs of concept] that we’re working in with a large enterprise customer has basically this exact workflow, which is, when people need cloud infrastructure built, what they do is go ask for the cloud team to build it by filing a ticket in Jira.”

At the enterprise client, he noted, “The average time to deliver on one of those tickets is 72 days. So it takes 72 days to go from ‘I want some cloud infrastructure’ to ‘cloud infrastructure complete.’”

## Digital Twins of Real Infrastructure

The System Initiative platform integrates with “any workflow or trigger,” the company’s announcement claimed: Terraform, [Pulumi](https://www.pulumi.com?utm_content=inline+mention), GitOps, as well as “Jira tickets, GitHub issues or Slack commands, without any re-architecting of existing processes.”

It can help engineering teams migrate between stacks and providers, said Jacob — for instance, a team might be running containers on EC2 instances, but can use the platform to shift to Kubernetes or the Elastic Container Service. “It’ll sort of do the translation for you,” he said.

This works, he said, because the platform creates one-to-one digital twins of the infrastructure, rather than using abstractions of a service. “The way the system does that is, we basically take in their descriptions of their own service, model it for them, and then stitch it all together, put a little bit of AI against it to, find validations or or policy that they don’t specify in the spec but they do in the docs, and then that generates the the actual models that people use.”

The digital twins “are the things you’re making changes to, inside the simulated change set, and applying policy to, and reviewing,” Jacob said.

“And because those things are one-to-one, what we get is a significant increase, not only in performance, but in your ability to program the system clearly and safely.”

Currently, he added, the platform only allows users to deploy to [AWS](https://aws.amazon.com/?utm_content=inline+mention), though integrations with [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure and [Google](https://cloud.google.com/?utm_content=inline+mention) Cloud Platform are on the roadmap for the near future.

## Easy Collaboration, a Full History of Changes

System Initiative’s dashboard allows users to see their changes update the live deployment in real time, [Nick “Keeb” Stinemates](https://www.linkedin.com/in/nickstinemates/), the company’s vice president of business development and community, told TNS.

And it’s built for collaboration, he added: “The same way that you’d work with Google Docs or Figma, is baked into the system, so that you can collaborate with an AI agent or with your teammates seamlessly.”

The System Initiative platform also allows users to view a comprehensive history of activity, Jacob said. “So we can see: What’s the full history of change that’s happened to this component, both in this change set, and somewhere else? You can see all the raw data.

“This makes it really easy for someone to go through a complex change and be like, ‘Hey, what exactly are we about to do in this particular moment?’”

[![](https://cdn.thenewstack.io/media/2025/08/820bedeb-system-initiative-1024x576.png)](https://cdn.thenewstack.io/media/2025/08/820bedeb-system-initiative-1024x576.png)

A sample of what the System Initiative dashboard looks like — the pieces of infrastructure are listed on the left, activity on the right.

Creating the new platform, Jacob suggested, required a new, “AI-native” approach rather than following in the steps of previous infra automation tools. Doing things the old way, Jacob said, revealed a lot of user experience problems in the middle.

“Every time you tried to build a system that worked this way, what you ran into were technical decisions we made when what we were doing was following the path of traditional infrastructure automation,” he said.

Some of the problems that emerged, he said, included the slowness of the feedback loop and “the fact that security and compliance rules come in at the end. Even though they’re the most critical thing.”

The System Initiative infrastructure automation platform is now available for a free 30-day trial; a free tier is available for managing small production environments of fewer than 100 resources.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Heather Joslyn is editor in chief of The New Stack, with a special interest in management and careers issues that are relevant to software developers and engineers. She previously worked as editor in chief of Container Solutions, a Cloud Native consulting...

Read more from Heather Joslyn](https://thenewstack.io/author/hjoslyn/)