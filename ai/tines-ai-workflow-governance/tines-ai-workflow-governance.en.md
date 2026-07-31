**After eight years of building a no-code automation platform**, Tines launched 3B Tuesday, a new platform that uses AI to author enterprise workflows but still uses conventional code to execute them.

The idea here is for [Tines 3B](https://www.tines.com/wildcode/) to enable employees to describe a workflow, application, or agent in natural language. The service then writes the code and deploys it in an environment where IT and security teams remain in control.

[Tines](https://www.tines.com) co-founder and CEO [Eoin Hinchy](https://www.linkedin.com/in/eoinhinchy/) tells *The New Stack* that the company rebuilt its front end, middle layer, and back end for 3B from the ground up, even while its existing business was still growing. The company raised a $125 million Series C funding round at a $1.125 billion valuation last year, and Hinchy says its original platform now executes 1.5 billion automated actions every week.

“Yes, things are going great, but no code, low code, at least to us, was clearly not the future,” Hinchy says about the decision to build a new platform.

> “There is a sell-by date on low-code, no-code as a category.” —Eoin Hinchy, CEO, Tines.

For Tines, the problem wasn’t that low code had failed. Large language models were getting good enough at writing code to reduce the need for a visual builder.

“There is a sell-by date on low-code, no-code as a category,” Hinchy says. “It was the right solution for a particular moment in time.”

![](https://cdn.thenewstack.io/media/2026/07/0df5cb69-tines_eoin_hinchy_2025_00003-1024x683.jpg)

Tines CTO Eoin Hineys. Credit: Tines.

## Low code’s AI problem

Hinchy founded Tines in 2018 in Dublin with [Thomas Kinsella](https://www.linkedin.com/in/thomas-kinsella/) after spending much of his career in security and IT. The [original Tines Storyboard] gave security and IT staff a visual builder for automating work across otherwise disconnected tools without having to become software engineers.

As large language models improved, Tines added copilots, AI-centric data-transformation features, and [agentic actions] to that platform. Hinchy says the company nevertheless remained skeptical of using autonomous agents for every step of a production workflow.

In [a set of predictions published in late 2023], Hinchy argued that natural-language chat would replace no-code interfaces. About a year ago, he says, the team began asking whether a visual builder still made sense when models could generate code.

![](https://cdn.thenewstack.io/media/2026/07/8b232e91-workflow-1024x655.jpg)

*Credit: Tines*

“Building is now commoditized,” he says, and argues that this means that for a company like Tines, the job shifts from helping users assemble workflows to managing the code they produce, including credentials, integrations, and permissions — and handling the runtime.

While Tines started out with a focus on security, Hinchy says about 40% of Tines customers already use its original product outside of security, but those users still need some technical ability to create a workflow. With 3B, the company wants to reach employees in teams such as finance and human resources who can describe the application or automation they need but don’t know how to deploy and operate it.

Tines typically ships a minimal product and iterates with customers, Hinchy says. This time, it built a complete product in stealth without customer feedback and only brought early customers into 3B over the past few months.

## AI writes the workflow

The 3B builder starts with a natural-language prompt. The model can ask follow-up questions before generating a workflow and breaking it into individual steps. In the process, users can ask 3B to revise the whole application, if necessary, or just one generated step.

Once generated, each workflow step becomes code that runs in its own [ephemeral Docker container](https://thenewstack.io/kubernetes-ai-agent-runtime/). Tines destroys and recreates those isolated environments for every execution, Hinchy says. The code and workflow diagram remain visible for when users want to inspect them (though he also argues that, in most cases, this shouldn’t be necessary).

Once deployed, 3B generates a shareable URL that users can share internally.

For admins, there is a dashboard that shows, for example, which workflows are running, which are failing, which have public internet access, and which depended on a given system or integration. The system will also try to fix any broken workflows automatically and suggest improvements, which admins can then accept in this same view, too.

![](https://cdn.thenewstack.io/media/2026/07/5d3b5b07-monitoring_access_map-1024x655.jpg)

*Credit: Tines*

“’I don’t know anything about Git. I don’t know anything about Vercel. I don’t know anything about pipelines,’” Hinchy says, describing the users Tines is targeting. “We take care of all that for them.”

Customers can bring their own models in 3B, Hinchy says. Developers can also build with an external coding assistant and deploy the result to the platform. Tines’ existing connectors let administrators preconfigure access to services such as Snowflake, AWS, and Workday instead of handing production credentials to every employee who wants to create an internal tool.

## AI builds, code runs

“We’re using AI in the creation of these workflows, but that’s it,” Hinchy says. The generated code executes as a deterministic workflow or application rather than asking a model to reason through every step at runtime.

Hinchy says that should make common workflows faster, cheaper, more predictable, and easier to test. The promise here is that customers won’t need to pay the cost and extra latency of inference for steps that conventional code could easily handle. When needed, however, 3B can still call a model at runtime when a task depends on it, Hinchy says.

## From shadow AI to “shady AI”

As with similar platforms, Tines argues that by offering an easy platform to build with, employees won’t feel the need to go around IT and build with unapproved — and unmanaged — AI tools.  
Hinchy argues that what is happening now is somewhat different from the shadow IT issues that have been a staple of enterprise security discussions for a long time. Today’s employees aren’t simply bringing unauthorized tools into the workplace, he says.

Many are responding to mandates from executives who want them to use AI, with that pressure pushing them to build internal dashboards with coding assistants without considering security features, or to deploy applications through personal hosting accounts on Vercel or elsewhere.

“It’s more like shady AI than shadow AI,” Hinchy says.

![](https://cdn.thenewstack.io/media/2026/07/7e1385d3-monitoring_workflows-1024x655.jpg)

*Credit: Tines*

When using 3B, IT teams can decide which systems and data an employee can use before that employee starts building. An access map shows which users and workspaces can connect to a given service and what they can do there. Tines says each workflow also gets isolated execution, credential protection, and full logging.

The same features put 3B in competition with enterprise software vendors and startups building agent platforms. Hinchy points to major enterprise software companies working on similar products and says “half of YC” is building some version of the same idea.

> Hinchy points to major enterprise software companies working on similar products and says “half of YC” is building some version of the same idea.

Tines’ advantage, he argues, is the experience it has gained running critical automations and the data generated by years of workflow executions. That history, he believes, helps the company recognize what a healthy workflow looks like, where one is likely to fail, and which controls large enterprises expect.

## The old Tines isn’t going away

Existing customers won’t be forced to move their workflows into 3B. Hinchy says Tines has no migration deadline or sunset date for its original Tines Stories platform and will continue investing in it.

Security and IT teams may also prefer the visual builder when they want precise control over a workflow’s implementation. Hinchy expects customers to start new projects in 3B and move existing automations only when they are ready. Over time, though, he believes more customers will let AI own the implementation.

Tines isn’t shutting down the existing visual builder, but Hinchy no longer sees it as the company’s long-term interface. He assumes prompting will replace much of that work.

The visual builder made Tines useful to people who couldn’t code. Now, thanks to coding agents, code is no longer the scarce (and scary) part. Instead, it is now figuring out how to deploy, secure, and govern what AI writes, which is where Tines believes it can take its existing knowledge of how companies operate in the real world and expand its platform to serve them, all while staying true to its workflow automation promises.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)