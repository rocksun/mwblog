GitHub hasn’t had an easy year. The platform has been hit by [repeated outages](https://www.infoq.com/news/2026/04/github-outages-scaling/) affecting core services — including the Actions-based CI/CD pipelines that engineering teams depend on daily — and has had to issue [public apologies as a result](https://www.theregister.com/software/2026/04/29/github-says-sorry-and-says-it-will-do-better-as-uptime-slips/5225752).

The scale of the problem is staggering: Where GitHub handled roughly 1 billion commits across the whole of 2025, it now processes 1.4 billion every *month*, with AI agents alone responsible for more than 17 million pull requests in the same period. GitHub’s COO Kyle Daigle told *The New Stack* in [early June](https://thenewstack.io/github-wants-developers-back/) that the company is now targeting capacity to handle 30 times its current load — a challenge he described as far beyond the normal playbook of adding more machines.

Against that backdrop, Microsoft has chosen this moment to make its most direct push yet to push enterprise customers off [Azure Repos](https://azure.microsoft.com/en-us/products/devops/repos) — its own Git-based source code platform, which has existed in various forms since 2013, predating Microsoft’s [$7.5 billion acquisition of GitHub in 2018](https://news.microsoft.com/source/2018/06/04/microsoft-to-acquire-github-for-7-5-billion/) — and onto GitHub.

## The exit ramp

The tool Microsoft is using to make that case is Enterprise Live Migrations ([ELM](https://learn.microsoft.com/en-gb/azure/devops/repos/enterprise-live-migrations/overview)), currently in limited public preview. The core problem it solves is downtime: previously, moving large repositories from x to x could take days, leaving teams frozen out of active development.

In a [blog post](https://devblogs.microsoft.com/devops/introducing-enterprise-live-migrations-migrate-azure-repos-to-github-with-minimal-downtime-azure-devops-to-github-migration-with-continuous-sync-and-fast-cutover-enterprise-live-migrations-low-downt/) authored by [Soo Stahl](https://www.linkedin.com/in/soostahl/), principal product manager at Azure DevOps, and product manager [Bhuvan Shah](https://www.linkedin.com/in/bhuvan-shah-8a7138171/), the pair explain that ELM works by keeping the source and destination repositories in sync while developers continue working in Azure Repos, with a final switchover window that they say typically takes under 30 minutes.

> “Teams can migrate at their own pace, without coordinating complex, high-risk ‘all-at-once’ migrations.”

“This means no extended freeze periods, no multi-day outages – just a controlled, predictable transition that fits into your operations,” they write. “Teams can migrate at their own pace, without coordinating complex, high-risk ‘all-at-once’ migrations.”

There are real limitations worth acknowledging. ELM carries over the fundamentals — full Git history, branches, tags, pull request metadata, including comments and user history, and branch policies translated into GitHub rulesets — which, for teams whose work is primarily code-focused, may cover most of what they need.

But pipelines, work items, wikis, and test plans all have to be handled separately, and for enterprises deeply embedded in Azure DevOps’s broader project management and CI/CD tooling, ELM is a starting point rather than a complete solution.

For large organizations with hundreds of repositories, this is a multi-stage undertaking regardless.

![Migration to GitHub](https://cdn.thenewstack.io/media/2026/06/546fc57f-azurerepos.webp)

*Migration to GitHub*

For Microsoft, the calculus is all about AI — GitHub is where Copilot, the Copilot Coding Agent, and the broader agentic development suite live, and Azure Repos is not part of that picture.

To demonstrate that this is more than a customer pitch, Microsoft [recently published details](https://devblogs.microsoft.com/devops/how-microsoft-is-migrating-repositories-to-github/) of its own migration — its Copilot, Agents and Platforms (CAP) organization moved over 1,600 repositories and 3,100 developers across in six months, with a team of just two dedicated engineering leads driving the effort.

By consuming its own dog food at scale, Microsoft is making the case that the disruption is manageable and the payoff meaningful. [Poonam Gupta](https://www.linkedin.com/in/poonam-gupta-5155504/), partner director of product management for 1ES and Azure DevOps at Microsoft, cites AI as the primary driver of the migration.

> “Software development is being reshaped by AI, and where code lives now have a direct impact on how much value organizations can capture.”

“Software development is being reshaped by AI, and where code lives now has a direct impact on how much value organizations can capture,” Gupta writes. “For teams that want to take full advantage of AI-native development, repository location is becoming a strategic decision.”

## The elephant in the room

[Rumors](https://www.reddit.com/r/azuredevops/comments/k9cyrl/azure_repos_deprecation/) of Azure Repos’ eventual deprecation have [circulated online for years](https://learn.microsoft.com/en-us/answers/questions/1626498/clarification-on-azure-repos-future-and-deprecatio), and while Microsoft has not confirmed anything on that front, the direction of travel is clear.

The [community response](https://devblogs.microsoft.com/devops/how-microsoft-is-migrating-repositories-to-github/) to Gupta’s June 3 post captured the mood among enterprise customers: several questioned why AI capabilities couldn’t be brought to Azure Repos rather than requiring a platform change, while others raised the cost differential — Azure DevOps Basic costs [$6 per user per month](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/), compared with [GitHub Enterprise’s $21](https://github.com/pricing).

And more than one commenter interpreted the post as a deprecation notice in all but name. “The writing was on the wall since MS [Microsoft] bought GitHub,” wrote one commenter. “[Azure DevOps] is dead and MS wants everyone moving to GitHub… Everybody saw this coming, and only MS denied it.”

Perhaps more important here is the question that Microsoft sidesteps: if GitHub has spent the past year struggling under the weight of agentic development traffic, why is now the right time for enterprises to bet their critical infrastructure on it?

The timing acquired an extra layer of awkwardness on Friday, when 73 Microsoft-owned GitHub repositories — including the Actions used to deploy Azure Functions — [were disabled in a Miasma worm attack](https://www.stepsecurity.io/blog/miasma-worm-hits-microsoft-again-azure-functions-action-and-72-other-repositories-disabled-after-supply-chain-attack-targeting-ai-coding-agents), breaking CI/CD pipelines for developers globally.

None of this necessarily undermines the strategic case for moving to GitHub. The AI development ecosystem is consolidating there, and the migration tooling is getting meaningfully better. But for enterprise teams weighing the decision, reliability and security aren’t footnotes — they are the main criteria. Microsoft is betting that access to Copilot and agentic workflows is compelling enough to tip the balance.

It may well be right, but a 30-minute cutover window is only part of what it will take to make that argument stick.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)