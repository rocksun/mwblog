The past decade of cloud native was about scaling microservices with [Kubernetes](https://thenewstack.io/primer-how-kubernetes-came-to-be-what-it-is-and-why-you-should-care/) and [GitOps](https://thenewstack.io/4-core-principles-of-gitops/). The next will be about how these systems work with AI.

Earlier this year, the Argo Project community received a major contribution: a [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) server for Argo CD, donated by [Akuity](https://akuity.io/) and now maintained as a community project. This shows how open standards like MCP, combined with open source collaboration, are becoming critical as AI and cloud native converge.

## **Why Standards Matter for AI and Infrastructure**

Cloud native technology has advanced through standards. [Containers](https://thenewstack.io/introduction-to-containers/) became practical with the Open Container Initiative (OCI) specification. Service meshes gained adoption with interoperability. GitOps scaled through common practices in projects like [Argo CD and Flux](https://thenewstack.io/gitops-on-kubernetes-deciding-between-argo-cd-and-flux/).

AI is at a similar stage. Models and agents are powerful, but connecting them to infrastructure tools such as deployment platforms, observability stacks or security scanners often requires custom code.

MCP defines a consistent way for AI systems to connect with these tools. It serves as a universal adapter for AI in cloud native environments.

## **A GitOps Example: Argo CD Meets MCP**

GitOps provides a practical example. [Argo CD](https://thenewstack.io/survey-argocd-leaves-flux-and-other-gitops-platforms-behind/), the most widely used GitOps operator, keeps Kubernetes workloads synchronized and reliable for thousands of organizations.

In the past, adding AI to GitOps meant building custom integrations. With the new MCP server for Argo CD, AI agents can work directly with core workflows such as checking status, syncing deployments and pulling logs. This demonstrates how AI-assisted operations can reduce manual effort and simplify troubleshooting.

## **Donating the Argo CD MCP Server to the Community**

For MCP to succeed, projects need to be developed in the open. That is why the Argo CD MCP Server, first built by engineers at Akuity, was donated to the Argo Project community. It now lives under [argoproj-labs/mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd), where anyone can contribute.

The project has already gained traction. Users are testing it, filing feature requests and submitting pull requests. What began as an experiment is now a community-owned effort that connects AI and GitOps in practical ways.

## **Beyond GitOps: A Bigger Movement**

The same idea applies across the cloud native stack. MCP could enable AI agents to:

* Query metrics or traces from observability tools.
* Inspect traffic flows or apply policies in service meshes.
* Run compliance checks in security scanners.

In every case, MCP lowers integration friction and creates a shared foundation for experimentation. Enterprises benefit from faster and safer adoption. The community benefits by avoiding fragmentation and accelerating innovation, just as OCI standardized containers do.

## **Why Open Source is Key**

Cloud native progresses fastest when the community works in the open: sharing code, aligning on standards and solving problems together.

The donation of the Argo CD MCP Server reflects this approach. By moving the project under community ownership, its development will be guided by shared needs rather than individual vendor priorities. In cloud native, open source is more than just a licensing model, it’s how real progress happens.

## **Looking Ahead**

It is still early for MCP, but the trajectory looks familiar:

* Containers became mainstream once standards like OCI emerged.
* GitOps scaled because projects like Argo CD and Flux rallied the community.
* Service mesh adoption accelerated once interoperability was prioritized.

AI in infrastructure will likely follow the same path. Open standards and open source projects will make it safe, consistent, and scalable.

## **A Call to the Community**

MCP’s success depends on community experimentation. Whether you are a contributor, an operator or simply curious about AI in Kubernetes, now is the time to get involved.

The Argo CD MCP Server donation is one example of how open source contributions can accelerate progress. By making projects like this community-owned, the ecosystem can shape the way AI and cloud native come together.

Shared standards changed how we build and run applications. They can now change how we operate them in the age of AI. Community-driven approaches, not proprietary solutions, will make that possible.

*KubeCon + CloudNativeCon North America 2025 is taking place Oct. 10-13 in Atlanta, Georgia.* [*Register now*](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/)*.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/10/a65a1c66-cropped-5104c1c2-alexander_matyushentsev-600x600.jpeg)

Alexander Matyushentsev is the co-founder and chief architect at Akuity. He is the co-creator of Argo, an Argo CD lead and maintainer with over a decade of experience in software development. He is an enthusiast of continuous integration, agile practices...

Read more from Alexander Matyushentsev](https://thenewstack.io/author/alexander-matyushentsev/)