![The New Stack’s Frederic Lardinois sat down with Jonathan Bryce, executive director of the Cloud Native Computing Foundation (CNCF), to discuss how AI is reshaping cloud native infrastructure, open source innovation, and the developer community.](https://cdn.thenewstack.io/media/2026/11/81c5d979-thumbnail-24-1024x576.png)

AI agents are testing systems that were originally built for people, and Jonathan Bryce thinks the cloud-native community has a lot of work to do to help those systems keep up in this new era.

The New Stack sat down with Bryce, the executive director of the Cloud Native Computing Foundation (CNCF), at KubeCon + CloudNativeCon North America in Salt Lake City to talk about the projects joining the foundation and how AI is changing its work.

VIDEO

Bryce tells *The New Stack*, “A lot of the existing systems in our world were built for human speed, and agent speed is a completely different type of usage pattern and scenario, and so these systems are just not scalable and resilient enough to handle the kind of workloads that agents are generating.”

Running training and inference workloads on Kubernetes is already a familiar job for this community, and Bryce argues that the financial services, healthcare, and transportation systems that agents interact with will also need the elasticity and observability that cloud-native technologies provide.

### OpenShell and Agent Substrate

At KubeCon, Nvidia announced that it was [contributing OpenShell to the CNCF](https://thenewstack.io/nvidia-donates-openshell-cncf/). Google had also [announced the donation of Agent Substrate](https://cloud.google.com/blog/products/containers-kubernetes/open-infrastructure-for-autonomous-agents-comes-to-cncf/) ahead of the show. Both joined the CNCF as Sandbox projects, the foundation’s entry-level tier.

At its core, OpenShell enforces policies, including which files, networks, credentials, and model endpoints an agent can access. Agent Substrate tackles a related but different issue by providing isolated environments for agents on Kubernetes, with features like support for suspending idle sessions and resuming them when needed.

“We can make AI systems that have security and control architected into them from the infrastructure side,” Bryce says.

He sees this as a responsibility for the community, given the questions AI has raised about security and resource consumption. Moving a project like OpenShell into neutral governance also lets more companies contribute to it, he says.

### Doing more with existing hardware

Agent workloads also aren’t as evenly distributed as those of more traditional enterprise applications.

“Your agent, even if it’s always waiting around to be at your beck and call, it’s not necessarily doing work 24/7,” Bryce says. “How do you spin it down and spin it up where it feels like it’s ready for you at any time? That’s going to be the user experience that people demand. How do you do that without just having it sit there and burn CPU cycles on nothing?”

[Agent Substrate](https://thenewstack.io/kubernetes-ai-agent-runtime/) saves the agent’s state and frees up the compute it was using, then restores the session onto an available worker.

Bryce also highlighted [llm-d](https://thenewstack.io/llm-d-cncf-kubernetes-inference/), the distributed inference framework, as an example of software getting more out of existing hardware. While hardware is expensive, expensive to run, and (at least currently) in limited supply, software gives developers something they can work on now.

### A flood of vulnerability reports

Zero-days and security also came up more at this KubeCon than in previous years.

As more people use AI tools to find and report vulnerabilities, Bryce says, open source maintainers have been flooded with duplicate and unverified reports that they still have to take seriously.

He thinks the pace may no longer be accelerating the way it was early this year, but he isn’t sure what 2027 will bring as the models keep getting better.

“Y2K didn’t end up being that big of a deal,” he says. “This is really a moment that could be a big deal if we don’t actually just all get together and work as quickly as we can.”

### Agent adoption is still early

For all the talk about agents at the show, though, Bryce’s assessment of adoption is measured.

“Beyond software development, adoption is still quite low,” he says.

He sees production use in customer service and other areas with a well-defined, historical base of knowledge.

“We’re very, very, very early in the path to billions of agents that are taking action on our behalf on a constant basis,” Bryce says.

Companies remain cautious about what happens when they give an agent access and something goes wrong, which won’t come as a surprise if you’ve recently spent any time talking to big enterprises and their customers.

For now, Bryce sees this as a positive, because it may just allow the community enough time to harden projects like OpenShell and Agent Substrate before enterprises put agents to work more broadly.

The post [AI agents were all over KubeCon. Production is another story](https://thenewstack.io/cncf-bryce-ai-agents/) appeared first on [The New Stack](https://thenewstack.io).