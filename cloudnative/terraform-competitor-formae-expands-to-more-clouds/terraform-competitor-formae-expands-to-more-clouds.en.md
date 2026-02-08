Late last year, startup Platform Engineering Labs [made waves](https://thenewstack.io/kubecon-a-terraform-killer-built-on-apples-pkl/) in the world of [Infrastructure as Code](https://thenewstack.io/infrastructure-as-code/) (IaC) by introducing a new IaC platform, called [Formae](https://platform.engineering/formae), available initially on [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention).

This week, [Platform Engineering Labs](https://platform.engineering/)‘ platform gets (beta) support from additional cloud platforms, including [Google](https://cloud.google.com/?utm_content=inline+mention) [Cloud Platform](https://thenewstack.io/paris-is-drowning-gcps-region-failure-in-age-of-operational-resilience/), [Microsoft](https://aka.ms/modelmondays?utm_content=inline+mention) [Azure](https://thenewstack.io/microsoft-linux-is-the-top-operating-system-on-azure-today/), [Oracle Cloud Infrastructure](https://www.oracle.com/developer?utm_content=inline+mention), and [OVHcloud](https://thenewstack.io/how-ovhcloud-made-its-800-databases-more-efficient/).

The company has also released new AI-enhanced software for managing infrastructure tooling, called the Platform for Infrastructure Builders.

“This release is for and about infrastructure builders,” says [Pavlo Baron](https://www.linkedin.com/in/pavlobaron/), co-founder and CEO of Platform Engineering Labs, in a statement. “From here forward, you don’t need to wait on us or anyone else. Build for your own infrastructure. Launch fast. Iterate fast. Extend fast. Do it hands-on or with help from your Al agents.”

The company is pitching the platform for organizations that may have some components managed by IaC but want to expand operations to older, legacy resources that may have been previously thought too ornery to be managed under IaC.

## Schema-safe change management

The new platform, with the accompanying software development kit (SDK), will allow users to extend their infrastructure with new components, offering schema safety and an easy-to-understand plug-in interface.

“Engineers can now use AI agents to quickly produce and modify plugins that are reliable by design,” says [Zachary Schneider](https://www.linkedin.com/in/zacharyschneider/), co-founder and CTO of Platform Engineering Labs, in a statement.

The Formae software was built to automatically discover and codify system resources and system changes into a single unified source of truth.

The founders claim that this approach offers superior state management and easier migration paths than the industry-leading IaC solution, [HashiCorp’s Terraform](https://thenewstack.io/ibm-hashicorp-sunsets-terraforms-external-language-support/).

## Infrastructure as Code

[Infrastructure as Code](https://thenewstack.io/introduction-to-infrastructure-as-code/) is the practice of saving your system’s configuration in a file, usually using [YAML](https://thenewstack.io/yall-against-my-lingo-why-everyone-hates-on-yaml/) or [JSON](https://thenewstack.io/an-introduction-to-json/), which IaC orchestrators then use as an instruction set to roll out infrastructure.

The advantages IaC promises are automated deployments — a real time saver — and a guard against system drift, which is when systems fall out of alignment from their desired state (usually due to manual intervention).

Yet after everything is set up once, Day 2 operations with IaC can be a headache, Baron contended in an earlier interview with *The New Stack*. IaC files are brittle things. They quickly get complex and difficult to understand, are easy to corrupt with shadow IT work, and are easy to make mistakes with. They offer no guidance as to whether the values they hold are even correct.

Within the Formae environ, an individual IT resource [is extracted](https://docs.formae.io/) into a versioned, declarative code artifact called a “forma” (which is the Latin singular for “form”) that can then be programmed against.

Unlike [Terraform](https://thenewstack.io/how-to-use-terraform-for-automation-at-the-edge/) or [Pulumi](https://thenewstack.io/pulumis-new-internal-developer-platform-accelerates-cloud-infrastructure-delivery/), state management in Formae is handled not by the clients themselves, but by [agents](https://www.youtube.com/watch?v=QHWCdTAKTgM), to guard against system drift. Changes are made in the same way security patches are rolled out, minimizing the blast radius of each update.

The code is written in an unusual language, Apple’s [Pkl](https://github.com/apple/pkl), which that company developed in-house [to manage](https://pkl-lang.org/blog/introducing-pkl.html) its own system deployments.

Pkl is different from JSON and YAML in that it forces users to develop a schema for each type of resource, along with a type annotation. With type annotation, the type values — and sometimes even a range of permissible values themselves — are already established for the variable itself. So fewer typos can sneak in and disrupt the operations.

The open source version of [Formae is available today on GitHub](https://github.com/platform-engineering-labs/formae).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)