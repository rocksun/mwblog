# Beyond Infrastructure as Code: System Initiative Goes Live
![Featued image for: Beyond Infrastructure as Code: System Initiative Goes Live](https://cdn.thenewstack.io/media/2024/09/f700e053-system_initiative-1024x683.png)
As many [who have met him](https://x.com/adamhjk) know, infrastructure management engineer [Adam Jacob](https://www.linkedin.com/in/adamjacob/) is [not a fan](https://thenewstack.io/adam-jacob-rebuilding-devops-with-system-initiative/) of current [DevOps practices](https://thenewstack.io/DevOps/).

Well, today is Jacob’s big day to “Put Up or Shut Up,” as they say.

For today is the day that his company, [System Initiative](https://www.systeminit.com/), launches a new automation platform, one that makes detailed models of an organization’s IT infrastructure, which can then be used to manage these systems. It is a radical rethink of how infrastructure could be managed, one designed to avoid all the distracting “tiny paper cuts that DevOps is full of,” as Jacob has said.

With a graphical grid-based workspace, an admin can stitch together a system with [small, reactive functions](https://thenewstack.io/system-initiative-could-be-lego-for-deployment/), allowing the system to be managed as “living architecture.” The software checks the requirements for each new containerized component added, alerting the user of any issues around configuration or policy enforcement. It then automates much of the routine work of wiring together different system elements, and provides tools to quickly add in any missing details.

All the problems that typically show up late in a DevOps process can be immediately flagged by the software, according to the company.

“It’s a revolutionary technology that we think is the future of DevOps automation,” Jacob told TNS.

## The Problem With DevOps and IaC
In theory, DevOps practice, often using [Infrastructure as Code](https://thenewstack.io/infrastructure-as-code/) (IaC), uses code to deploy resources in a system in an automated fashion, allowing the system to be updated multiple times in a day, if possible. A common practice has been to store the configuration code in [GitHub](https://thenewstack.io/how-to-use-github-actions-and-apis-to-surface-important-data/) and press the artifacts into production through [Terraform](https://thenewstack.io/is-terraform-dead-revive-your-infrastructure-as-code-strategy/).

In [practice](https://www.amazon.com/stores/author/B0CCGVSJRK), as Jacob [has pointed out](https://thenewstack.io/adam-jacob-rebuilding-devops-with-system-initiative/), this has led to unwieldy, hard-to-update and difficult-to-understand systems built on static definitions. The tools are tightly tied to a version control, making them brittle and difficult to work with. And only elite companies, [such as Google](https://thenewstack.io/despite-the-hype-engineers-not-impressed-with-dora-metrics/), can deploy multiple times in a day with this approach as Jacob (and others) [have argued](https://matthewsanabria.dev/posts/take-the-system-initiative/).

“It’s not a single technology problem, but it is the shape, the foundation, the primitives that we’re being asked to use that cause these [negative] outcomes in the vast majority of cases,” Jacob said.

Managing infrastructure as code may seem like a good idea but it causes “all sorts of downstream problems,” he said.

## How System Initiative Is Different
System Initiative’s approach is different in that all the artifacts are rendered as data and graphed together, so the relations between them can be recalculated on demand. This provides the service’s “digital twins” capability, allowing users to test new configurations and extensions to see if they would actually work.

The graphical interface provides an overview of the entire infrastructure, showing how all the components relate to one another. Changes to the system can be modeled and tested before going live.

This allows teams to test changes and validate configurations. The service allows more than one user to test changes.

Services are rendered as functions. Underneath the visualization, all the entities and relations are captured in [TypeScript](https://thenewstack.io/TypeScript/).

“Let’s say you have a Docker container that you want to use in the load balance service somewhere,” Jacob explained. “So in this condition, there’s a function that takes that Docker container information in the input and its output is the load balancer, and it knows how to configure the right thing, the load balancer on demand. So we change the port container running on then it would automatically change the pool for the load balancer,” he said.

The platform is available as a hosted service with usage-based pricing (including a free tier). The software it runs on is open source.

Initially, System Initiative is built for managing infrastructure on [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) (AWS), but support for other cloud services will be available in the near future.

## About System Initiative
Launched in 2019, System Initiative ([Twitter](https://twitter.com/thesysteminit), [Discord](https://discord.com/invite/system-init)) has raised by $18 million in venture capital from [Amplify Partners](https://www.amplifypartners.com/), [Scale Venture Partners](https://www.scalevp.com/), [Storm Ventures](https://www.stormventures.com/), and [Battery Ventures](https://www.battery.com/).

The open source stack for the service, called [si](https://github.com/systeminit/si), was [open sourced in June 2023](https://thenewstack.io/system-initiative-a-devops-makeover-by-ex-chef-adam-jacob/) ([Apache 2.0](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/)), and has been downloaded by 1,600 times. The project has 29 contributors thus far, and the commercial platform has been given the run-through by at least 120 early users. It is built on [NixOS](https://thenewstack.io/nixos-a-combination-linux-os-and-package-manager/), with [Docker](https://www.docker.com/?utm_content=inline+mention) using [Flakes](https://nixos.wiki/wiki/Flakes) Nix package manager. It has been forked 68 times and has garnered 690 stars.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)