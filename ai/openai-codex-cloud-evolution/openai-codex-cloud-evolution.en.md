Thibault Sottiaux, who leads core products at OpenAI, believes that today’s version of Codex will seem outdated before the year ends.

[Sottiaux](https://www.linkedin.com/in/thibault-sottiaux-27195366/) posted on X late Monday, “Given some of the results I’m seeing recently, it’s pretty clear Codex is a good harness.” He continued, “But it will seem primitive in 2-3 months and we’re about to go through another major evolution in how we use AI at the frontier.” He also said, “The next generation of models need more than your laptop.”

> “It will seem primitive in 2-3 months and we’re about to go through another major evolution in how we use AI at the frontier.”

Sottiaux did not share details about OpenAI’s plans for the coming months. However, his comments are timely since the company is already working to move Codex beyond tasks limited to a developer’s computer. Since [launching a new GPT-5 model for Codex](https://thenewstack.io/openai-launches-a-new-gpt-5-model-for-its-codex-coding-agent/) in early July and [surpassing 8 million users](https://thenewstack.io/gpt-5-6-codex-user-surge/) shortly after, the product has been evolving quickly.

## Ona fills the infrastructure gap

In June, OpenAI [said it plans to buy Ona](https://openai.com/index/openai-to-acquire-ona/), a company that creates secure cloud development environments. OpenAI called this deal part of the “next phase of Codex,” where agents can keep working in a customer’s cloud even after the laptop that started the job is closed.

> “The next generation of models need more than your laptop.”

Codex currently uses cloud infrastructure, but it might still need the developer’s laptop to access projects and run tools. If the laptop goes offline, the agent may lose what it needs to keep working.

OpenAI has already tested this approach. In [an experiment published in February](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex), Codex worked for about 25 hours straight, used around 13 million tokens, and generated about 30,000 lines of code while building a design tool from scratch. Alibaba has pushed even further — its Qwen3.8-Max agent recently [coded autonomously for 16 days](https://thenewstack.io/qwen-autonomous-coding-audit/), producing 265 commits with zero human help. Ona could help solve this problem.

The company, which used to be called Gitpod, creates cloud environments that can be set up with the tools and dependencies needed for each project. OpenAI said Ona has helped 2 million developers use these environments.

## Agents need persistent workspaces

If the acquisition goes through, Ona’s technology would let Codex have a permanent workspace in a customer’s cloud. Agents could get the context and tools they need for a task without relying on an active session on a local machine.

OpenAI says companies will still decide how Codex works in their cloud environments, including what sensitive systems it can access. The deal is not final yet, so OpenAI and Ona are still separate companies.

It is not clear if Sottiaux’s prediction is truly related to Ona. Although the acquisition shows OpenAI is looking beyond just the model, because for Codex to work on its own, it needs an environment that stays online even when the developer’s laptop is off.

Unfortunately, moving the execution environment to the cloud solves one problem but creates many new ones.

## Security risks grow with access

Letting a coding agent have full access to a company’s network or a developer’s credentials is undoubtedly risky. OpenAI said Ona’s customer-controlled model will let agents work inside an organization’s own cloud, while OpenAI provides the model and orchestration. Even if the model gets stronger and can handle more complex tasks, it still needs a secure place to run commands, save its progress, and interact with other systems.

Developers can assign tasks like refactoring, upgrading dependencies, or investigating bugs to the agent and let it work remotely. They can track its progress, check terminal output, and step in if a human decision is needed. When the agent finishes, users can review the pull request and see which tests were run.

OpenAI is already heading this way. Codex [has been folded into the ChatGPT desktop app](https://thenewstack.io/openai-codex-work-atlas/) and can handle parallel tasks. Its [desktop app is increasingly built around managing agents](https://thenewstack.io/openais-codex-desktop-app-is-all-about-managing-agents/), and its mobile features let developers monitor and guide tasks running on laptops, devboxes, or remote environments. It has also expanded with [new plugins](https://thenewstack.io/openais-codex-gets-plugins/) and [tools aimed at knowledge workers](https://thenewstack.io/openai-codex-knowledge-workers/) beyond just developers.

> Agent environments will use computing resources along with CI/CD systems.

## Managing a new agent layer

This change means there is a new type of infrastructure to manage. Anthropic is already moving on this front — its [acqui-hire of Mendral](https://thenewstack.io/anthropic-mendral-cicd-acquihire/) is aimed at automating CI/CD tasks like flaky tests and dependency reviews directly inside its platform. Agents will need their own identities and access rules, and their actions will need to be logged, reviewed, and linked back to them, just like with human developers and current automation.

Sottiaux’s prediction certainly has provoked curiosity. Two or three months is a very short time for a product to become “primitive.”

​

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)