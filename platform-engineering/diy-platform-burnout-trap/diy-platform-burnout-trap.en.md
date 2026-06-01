Platform engineers are some of the most resourceful people in IT. Give them a problem, and they’ll automate their way toward a solution. But what happens when the automation itself becomes the problem?

This is the quiet crisis hiding inside many organizations today. In the race to reduce toil, teams have built what amounts to a mountain of automation. Scripts, layered on blueprints, layered on orchestration workflows, layered on tooling, APIs, GitOps, and infrastructure and label it a “platform.” This isn’t a platform; it’s complexity dressed up in a better outfit.

## Trading one problem for another

Here’s the dirty secret about using automation to [build your own platform](https://images.sw.broadcom.com/Web/CAInc2/%7B68c6ad82-a684-4e39-8feb-12803e4b1f0e%7D_The_Upside_Down_Economics_of_DIY_PaaS.pdf) stack: you don’t actually eliminate complexity; you just become responsible for it in a new way.

It starts well enough. You automate a painful workflow, ship it, and you move on to the next fire. But automation doesn’t maintain itself. Over time, the team that wrote it moves on. As they do, the context behind why it was built fades.

Nobody quite remembers what the edge cases were, why that snowflake script was written that way, or the original problem it solved. And when it breaks–and it will break–you’re not debugging an application. You’ll be performing an archaeological excavation of your own infrastructure, to decipher the intent of the team that originally constructed the automation.

## When scripts outlive their authors

So you do what engineers do: you automate around it. You add new automation on top of old to address the gaps. Now you’re managing two mountains of automation instead of one. And here’s the impact that rarely makes it into the original business case – the platform team doesn’t get to walk away when it’s “done” because it’s never done.

These engineers can’t be reassigned without your platform decaying beneath the applications and services that make up the business’s backbone. You need a robust team to manage this indefinitely just to keep the lights on. We’re simply trading software costs for people costs. And often, you end up spending more to produce something less scalable and capable than what you had from day one.

> “Automation may mask complexity but does not eliminate it, and mountains of automation makes diagnosis and repair exponentially harder when things go sideways.”

This is the real trap. Automation, at its best, is a productivity multiplier. At its worst, it’s lipstick on a pig; all the ceremonies of agility without the true benefits. Automation may mask complexity but does not eliminate it, and mountains of automation makes diagnosis and repair exponentially harder when things go sideways.

## What a pre-engineered PaaS actually does

A true Platform as a Service (PaaS) isn’t a collection of automation. It’s a pre-engineered system where the underlying plumbing, services, security, and resilience are already integrated before you ever install and consume it. This is the ‘batteries included’ model where the platform is ready to use on Day 1 based on best practices and proven architectures. This kind of integration out-of-the-box is one of the things that makes a platform trustworthy and predictable at scale.

For example, an integrated platform includes ‘how’ applications are built and deployed is pre-wired out of the box and works consistently across application types. One of the more unique things Tanzu Platform does is build deployment packages, including the base image for developers. This means that when a security problem comes out–like [Copy Fail](https://hackread.com/linux-kernel-vulnerability-copy-fail-full-root-access/) or the flood of [AI-discovered vulnerabilities](https://www.anthropic.com/research/glasswing-initial-update)–[the platform engineer can rebuild and redeploy apps](https://blogs.vmware.com/tanzu/smarter-patching-at-scale-vulnerability-assessment-and-remediation-with-vmware-tanzu-platform/) very quickly without reaching back into the software delivery lifecycle (SDLC). They simply “restage’ the application using a single command.

The consistency of deployment packages and base images also [enables developer velocity](https://thenewstack.io/unlock-velocity-enable-parallel-frontend-backend-development/) in the every day. When every application is built, packaged, and deployed the same way, developers stop re-solving the same infrastructure problems, and start focusing on the code that actually matters. This is a distinction worth drawing clearly–assembling capable open source tooling like Terraform, ArgoCD, Kubernetes, cert-manager, OpenBao, and Istio gives you powerful building blocks, but it doesn’t give you a platform.

You still own the integration, automation, the opinions, lifecycle management, and the operational model that ties them together. A pre-engineered PaaS handles the myriad of decisions for you. With a PaaS, onboarding a new team or new application isn’t a one-off integration project; it’s a repeatable, predictable process. Standardization is a core outcome of a pre-engineered PaaS, not a side effect, and it’s precisely what makes it possible to push changes faster and with more confidence, regardless of the team, language, or application type.

## Security built into the platform

Security works the same way. When your team makes the decision to pull from open-source components and stitch them together, you now own every security gap between them – data at rest, data in flight, and its running state. This seems like a worthwhile investment at first, but as recent research suggests, [AI-assisted attacks are on the rise](https://blogs.vmware.com/tanzu/how-to-prepare-for-the-world-of-ai-driven-exploits/), and platform teams won’t be able to keep up with surging security vulnerabilities in the build-it-yourself model.

A pre-engineered PaaS standardizes the [governance and compliance](https://thenewstack.io/3-steps-cloud-governance-steps-to-avoid-the-next-hack/) posture across the board. Updates, patches, and fixes from a trusted, first-party vendor mean you’re not reinventing governance from scratch each time you add a new component. The PaaS can help you uniformly and at scale apply the changes in a cascading fashion rather than relying on custom automation.

The calculus starts to shift when you see deployment, security, and onboarding issues in aggregate. Achieving all of this with custom automation means spanning organizational silos, coordinating teams, sustaining headcount, and continuously funding work that never actually finishes.

And worse yet, this work has no meaningful competitive advantage for your organization. Your competitors are working to solve the same problem, but you’re just burning more resources to accomplish the same end result. You own the problem entirely rather than leaning on a trusted, proven vendor. Embracing a PaaS allows you to focus on higher-value, differentiating initiatives for the business.

## AI is the forcing function

The conversation around PaaS is urgent again, and AI is why. Code generation can speed up your development cycles, building and pushing features faster, but production delays will persist if you’re still deploying at the same speed as before.

To avoid eroding the benefits of code generation, you need to deploy applications nearly as fast as they can be coded with AI. This requires streamlining each step of the path to production. In an era where more organizations are exploring the use of autonomous agents, they need a platform that doesn’t take weeks to rotate credentials, days to provision a database, or require access to JIRA’s MCP Server to accomplish their goals.

> “To avoid eroding the benefits of code generation, you need to deploy applications nearly as fast as they can be coded with AI.”

The [pace of AI innovation itself compounds the problem](https://thenewstack.io/diy-kubernetes-agentic-ai/). Whether it’s shadow AI use, MCP servers, agentic harnesses, this week’s new foundation models, or whatever emerges next, the landscape is evolving fast enough that what’s bleeding-edge today may be table stakes in six months. When you build your own platform, you’re on the hook to evaluate each layer of these new technologies, determine how they fit into your stack, and then integrate them yourself, on top of everything else your platform team is already managing to keep the business going.

Organizations running VMware Tanzu Platform receive those innovations. With Tanzu Platform 10.4, for example, customers gained MCP Gateway, an expanded service marketplace where developers can publish their own MCP servers and services for cross-organization consumption, as well as an agent buildpack to streamline and secure the deployment of agentic AI applications.

These are capabilities that would have taken a DIY team months to evaluate, build, and harden. And this isn’t unique to AI. Every release brings new capabilities across the platform that customers simply inherit, without the integration tax. That’s the compounding return on your investment in a pre-engineered PaaS. The platform keeps moving forward, and so do you.

## VMware customers: You’re closer than you think

Platform engineers are uniquely equipped for this moment. They have the pattern recognition, they have seen the technology waves before, they bring their hard-won operational instincts, and the critical thinking skills to know when a system is genuinely resilient versus cleverly disguised complexity.

That’s exactly why their role in curating and operating this next generation of PaaS matters more than ever. Platform Engineers applying these battle-tested experiences using a PaaS will shortcut the tedious automation pitfalls, jumping straight to safely delivering Agentic AI and GenAI application services.

If you’ve already built your stack on [VMware Cloud Foundation](https://thenewstack.io/vmware-cloud-foundation-is-now-an-ai-native-platform/) you’re already in a position to add the value of a true PaaS. VMware Tanzu Platform layers a pre-engineered PaaS on top of your existing infrastructure APIs, running alongside your VMs and containerized workloads, without ripping out what you’ve built and budgeting for alternatives.

With an incremental step, you can leverage what you know and trust, and layer on the only private cloud PaaS for agents that offers direct integration with Private AI services.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/0615be98-darin-zook.png)

Darin Zook is the Product Marketing Engineer for VMware Tanzu Platform. Before joining Tanzu in 2022, he was a solutions engineer and architect who used the knowledge and skills he gained as a customer to help guide operations teams through...

Read more from Darin Zook](https://thenewstack.io/author/darin-zook/)