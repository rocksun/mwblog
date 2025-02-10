# Infrastructure as Code: From Imperative to Declarative and Back Again
[Infrastructure as Code](https://thenewstack.io/introduction-to-infrastructure-as-code/) (IaC) has gone through fascinating shifts over the years. The evolution of infrastructure management has been a story of constant iteration, shaped by the needs of scaling systems, velocity and safety metrics a lá [DORA](https://www.env0.com/blog/dora-metrics-an-infrastructure-as-code-perspective), and the demands of developer productivity.
From an imperative approach, where admins wrote detailed scripts to provision and configure infrastructure, the industry moved to declarative [IaC](https://thenewstack.io/infrastructure-as-code-from-imperative-to-declarative-and-back-again), driven by the desire for scalability, repeatability, and reduced human error. Declarative tools like Terraform made it possible to define **what** the infrastructure should look like rather than specifying **how** to create it. This reduced complexity and improved reliability.

In 2025, we’re seeing a subtle but meaningful return to imperative methods — albeit with a twist. Let’s explore how the industry has shifted between imperative and declarative approaches, converging toward today’s hybrid models.

## The Early Days: Imperative Configuration Management
In the early 2000s, tools like Chef and Puppet spearheaded infrastructure configuration automation. Paul Hammond and John Allspaw delivered the influential talk [ 10+ Deploys Per Day: Dev and Ops Cooperation at Flickr](https://www.youtube.com/watch?v=LdOe18KhtT4) at O’Reilly’s Velocity Conference, demonstrating how modern tooling could transform engineering practices. At the time, achieving 10+ deployments a day seemed like science fiction.

[Chef](https://www.chef.io/) and [Puppet](https://www.puppet.com/), the most popular early configuration management platforms, became the backbone of this shift, introducing a fresh approach to configuring systems. However, they operated within an imperative paradigm, where users explicitly outlined the steps to achieve the desired configuration.
For instance, installing software required specifying each command, defining conditions, and meticulously controlling the sequence of operations.

While powerful, the imperative approach struggled with scalability and maintenance. Their reliance on this paradigm made scripts environment-specific and brittle, demanding significant manual effort to adapt to evolving infrastructure needs.

This led to several limitations:

**Increased Complexity:**Scripts grew unwieldy as infrastructure scaled.**Prone to Errors:**Minor mistakes often cause inconsistencies, especially across environments.**Repetitive Logic (No DRY – Don’t Repeat Yourself):**Duplicated code across scripts created a significant maintenance burden.
## The Shift Toward a Hybrid Declarative Configuration
As the industry recognized the drawbacks of purely imperative approaches, tools like [Ansible](https://www.redhat.com/en/ansible-collaborative?intcmp=7015Y000003t7aWQAQ) emerged as a transitional solution, blending imperative and declarative paradigms. It’s no surprise that Red Hat quickly acquired Ansible as it gained momentum. With its YAML-based playbooks, Ansible allowed users to define their infrastructure without specifying the exact steps to achieve it. While still executing tasks sequentially under the hood, Ansible embraced the declarative philosophy of describing outcomes over procedures.

Ansible’s success demonstrated the appetite for more abstraction in infrastructure management, paving the way for fully declarative tools.

## The Declarative Revolution and the IaC Breakthrough
The transformation came with tools like [Terraform](https://www.terraform.io/) and [AWS CloudFormation](https://aws.amazon.com/cloudformation/), which embraced fully declarative models. Instead of focusing on procedural steps, users defined the desired state of their infrastructure in configuration files.

These tools reconciled this state with reality, automating the actions needed to achieve the outcome. Terraform introduced state files to track resources, enabling incremental updates and scalability, while CloudFormation leveraged JSON or YAML templates to manage AWS resources declaratively. Both offered distinct solutions to the challenges posed by imperative models.

This paradigm shift solved many of the issues inherent in imperative approaches:

**Scalability:**Declarative IaC scaled effortlessly across environments.**Consistency:**State tracking ensured uniformity in deployments.**Efficiency:**Teams could manage infrastructure without repeating procedural logic.
## The Imperative Renaissance (Kind of)
Today, tools like [Terraform CDK](https://developer.hashicorp.com/terraform/cdktf) (TFCDK) and [Pulumi](https://www.pulumi.com/) have become popular choices among engineers. These tools allow developers to write IaC using familiar [programming languages](https://thenewstack.io/programming-languages/) like Python, TypeScript, or Go. At first glance, this is a return to imperative IaC. However, under the hood, they still generate declarative configurations — such as Terraform plans or CloudFormation templates — that define the desired state of the infrastructure.

Why the resurgence of imperative-style interfaces?

The answer lies in a broader trend toward improving developer experience (DX), enabling self-service, and enhancing accessibility. Much like the shifts we’re seeing in fields such as platform engineering, these tools are designed to streamline workflows and empower developers to work more effectively.

## Why Now?
The current landscape represents a blending of philosophies. While IaC tools remain fundamentally declarative in managing state and resources, they increasingly incorporate imperative-like interfaces to enhance usability.

The move toward imperative-style interfaces isn’t a step backward. Instead, it highlights a broader movement to prioritize developer accessibility and productivity, aligning with the emphasis on streamlined workflows and self-service capabilities.

**Developer Familiarity:**Many developers are more comfortable with general-purpose programming languages than YAML or domain-specific configuration languages. Using familiar code eliminates a steep learning curve.**Code Reuse:**Developers can incorporate existing application logic into their IaC configurations. For example, code describing the behavior of application agents can be reused to define infrastructure setup.**Productivity Gains:**Tools like TFCDK and Pulumi make IaC more approachable, democratizing infrastructure management. Developers can define infrastructure without switching contexts or learning entirely new languages.**Behind-the-Scenes Declarative Power:**While developers write configurations imperatively, the underlying operations remain declarative. This ensures the preservation of scalability, consistency, and state management benefits.
Even in adjacent domains like CI/CD, we’re seeing this blending. Tools like Dagger and Buildkite let developers use familiar programming languages to define workflows, creating a more accessible experience while maintaining declarative outputs under the hood.

## Full Circle in 2024/5
We’ve come full circle in many ways — but with a modern take on familiar concepts. The push for more developer-friendly interfaces isn’t about reinventing IaC but improving its accessibility and usability. Even after acquiring Red Hat (and, by extension, Ansible), IBM is now set to acquire HashiCorp, highlighting how much the IaC landscape has evolved.

Declarative IaC remains central, but newer tools offer imperative-like interfaces that better align with developer workflows and emphasize flexibility, productivity, and collaboration. These innovations reduce complexity, support collaboration scalability, and improve infrastructure management. They mirror trends in DevOps and [cloud native development](https://thenewstack.io/cloud-native/).

## What’s Next and the Future of IaC
As the lines between imperative and declarative IaC blur, hybrid tools emerge to combine the best of both worlds. Improved state management, tighter integration with application logic, and enhanced multicloud support are [driving the future of IaC toward simplicity and productivity](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/). Different DevOps platforms (like env0) are helping teams embrace these hybrid approaches to achieve more with less.

These models provide the flexibility of imperative-style coding while preserving the scalability and consistency of declarative IaC. The goal isn’t to choose one paradigm over another but to use their strengths together to meet evolving needs. Balancing old and new approaches will remain central to innovation in IaC as tools evolve.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)