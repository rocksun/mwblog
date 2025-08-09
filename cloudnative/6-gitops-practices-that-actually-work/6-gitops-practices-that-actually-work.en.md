GitOps was pitched as a transformative approach to software delivery and infrastructure management, promising better outcomes across multiple dimensions of organizational performance. But, not all GitOps implementations are created equal.

Research from the [State of GitOps report](https://octopus.com/publications/state-of-gitops-report) reveals six crucial practices statistically related to several meaningful outcomes, including improved software delivery, enhanced reliability, eliminating configuration drift, and easier compliance and audit.

These practices form the foundation of successful GitOps adoption, moving beyond superficial implementation to achieve meaningful business outcomes. Organizations missing one or more of these practices were less likely to gain the benefits of [GitOps](https://thenewstack.io/4-core-principles-of-gitops/).

## **1. Declarative Desired State**

Unlike imperative approaches that require step-by-step instructions, [declarative configuration describes the end state](https://thenewstack.io/gitops-gap-few-use-declarative-configuration-to-manage-state/) you want to achieve, leaving the “how” to automated reconciliation tools. This represents a shift from crafting scripts that call a sequence of APIs and commands to drive state.

This shift from imperative to declarative thinking [addresses one of the most common sources of operational](https://thenewstack.io/address-common-machine-learning-challenges-with-managed-mlflow/) complexity: the mental overhead of understanding how a series of changes will affect system state. This is difficult enough if you assume you know the baseline state and have tight controls to prevent drift, but these assumptions are often incorrect.

Declarative desired state eliminates this complexity by providing a clear, verifiable target. Instead of worrying about the sequence of operations, teams can focus on defining what they want the system to look like.

What you get from declarative desired state:

* A readable change history and audit trail.
* Transfer of reconciliation burden to tools.
* A self-documenting target state.

## 2. Human Readable Format Is Critical

The power of version [control for change management](https://thenewstack.io/data-control-management-three-planes-different-altitudes/) only materializes when the configuration files are human-readable. This practice might seem obvious, but many organizations undermine their GitOps effectiveness by obscuring meaning with binary formats, encoded configurations, or overly complex and verbose markup.

Human-readable formats prioritize readability and comprehension, making it easier to make a change, review changes, or understand the target state. When files aren’t human-readable, making changes is harder, code reviews take longer, and nobody can understand the intended system state. You get a second wave of pain when you need to review an audit trail or determine what change introduced a problem.

What you get from human-readable formats:

* Easier changes that follow the developer-style workflow.
* Faster and easier code reviews.
* Change history and audit trails from version control.

## 3. Responsive Code Review

The speed of code review in GitOps implementations directly impacts the practice’s effectiveness and the likelihood of its consistent adoption. Slow reviews create a cascade of adverse effects that can undermine the entire GitOps approach.

When reviews are sluggish, teams naturally batch changes to [reduce the frequency of the review bottleneck](https://thenewstack.io/2-ways-to-reduce-bottlenecks-with-the-theory-of-constraints/). These larger batches increase complexity, making reviews more difficult and time-consuming, perpetuating the cycle. More critically, large batches increase the risk of each deployment and make it harder to isolate issues when problems occur.

Slow reviews also create pressure to bypass the GitOps process. Teams may resort to direct modifications that circumvent version control when they face urgent issues or tight deadlines. These “emergency” changes break the audit trail and create configuration drift, eroding the benefits of GitOps adoption.

What you get from responsive code reviews:

* Smaller batches have less risk.
* The ability to make version control the primary interface for system changes.
* Better throughput as people are no longer blocked waiting for a review.

## 4. Version Control

While everyone understands version control is a fundamental component of GitOps, its effectiveness depends heavily on the preceding practices. Version control becomes a [powerful platform for change management](https://thenewstack.io/inside-docusigns-ai-powered-agreement-management-platform/) only when you use human-readable declarative files and review changes quickly.

The selection of version control as the foundation for GitOps allows the reuse of existing organizational practices for access control, backup, and disaster recovery. Organizations typically have mature processes for protecting and [managing their source code](https://thenewstack.io/amid-licensing-uncertainty-how-should-iac-management-adapt/) repositories, and you can easily apply these same protections to configuration repositories.

What you get from version control:

* A source of truth for the desired state of the system.
* Familiar tools, controls, and audit trails.
* A complete history of changes and mechanisms to roll back changes.

## 5. Automatic Pull

With automatic pull, both words are equally important. The automation is crucial because you want to keep the system in the desired state. Pull is similarly essential as GitOps shifts from a central orchestrator pushing out changes to a distributed set of agents. This makes it easier to scale as you add more infrastructure, as you don’t need to maintain a central list.

The pull model also aligns with cloud-native architecture patterns, where services are expected to be self-contained and resilient to external dependencies. This architectural alignment makes GitOps a natural fit for modern application platforms and container orchestration systems, though it’s also used beyond Kubernetes.

What you get from automatic pull:

* Increased security as you don’t need to expose endpoints.
* Simpler fleet management, as you don’t need to manage the list of destinations centrally.

## 6. Continuous Reconciliation

Continuous reconciliation involves automatically detecting and correcting deviations from the desired state. The reconciliation loop is core to GitOps, but many organizations haven’t implemented it.

If you’re serious about eliminating configuration drift, you must implement continuous reconciliation. Even with the best will in the world, your chances of preventing drift are low unless you automatically and frequently return the system to the target state.

What you get from continuous reconciliation:

* Confidence that the system remains intended.
* Motivation for all changes to be made through version control.

## It’s Not Gatekeeping, It’s Data

The research backing these practices provides quantitative evidence that GitOps delivers measurable business value if you adopt the proper practices. Organizations considering.

Success in GitOps comes not from a perfect initial implementation but from continuous improvement guided by these research-backed practices. Teams that start with basic implementations of all six practices achieve better outcomes than those that perfect one or two practices without adopting the rest.

Automation is the best way to manage [complexity in software systems](https://thenewstack.io/how-to-hire-and-keep-software-devs-for-complex-systems/). The six practices of GitOps provide a model for this that has been proven to work.

You can find more about the research in the [State of GitOps report](https://octopus.com/publications/state-of-gitops-report), complete the [quick GitOps assessment](https://octopus.com/devops/gitops-maturity-assessment/), and watch on demand [The New Stack’s webinar from July 17, 2025](https://thenewstack.io/webinar/the-state-of-gitops-2025-key-findings-and-what-they-mean-to-you/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/10/e54f7c3f-cropped-fc6cbbe0-steve-fenton-600x600.jpg)

Steve Fenton is an Octonaut at Octopus Deploy, a DORA community guide and a six-time Microsoft MVP with more than two decades of experience in software delivery. He has written books on TypeScript (Apress, InfoQ), Octopus Deploy, and web operations....

Read more from Steve Fenton](https://thenewstack.io/author/steve-fenton/)