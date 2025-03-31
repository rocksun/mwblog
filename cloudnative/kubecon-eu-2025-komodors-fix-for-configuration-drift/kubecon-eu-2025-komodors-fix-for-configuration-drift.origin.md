# KubeCon EU 2025: Komodor’s Fix for Configuration Drift
![Featued image for: KubeCon EU 2025: Komodor’s Fix for Configuration Drift](https://cdn.thenewstack.io/media/2025/03/4facffee-komodor-1024x683.png)
Kubernetes networking admins attending [KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) in London next week should stop by Booth N330 to learn how they can prevent [Kubernetes configuration drift](https://thenewstack.io/reddit-no-longer-haunted-by-drifting-kubernetes-configurations/).

The new Komodor service is finely tuned to detecting drift and helping admins undo the damage it can cause. It is one of the first commercial products on the market to tackle this problem, according to the company.

The service automatically flags deviations from expected configurations. It monitors release rollouts and detects anomalies in resource consumption while flagging any breaking changes.

It is offered as a new feature on the company’s self-named platform.

## The Komodor Platform
Offered as a [software service](https://thenewstack.io/komodor-workflows-extend-kubernetes-troubleshooting/), [Komodor](https://www.youtube.com/watch?v=00OowbUvj5Y) is a management platform for [Kubernetes](https://thenewstack.io/kubernetes/) designed to simplify operations and help remedy issues, especially for large-scale fleet deployments and multicloud and hybrid cloud deployments.

The service was built to operate and manage large-scale Kubernetes clusters, monitoring their health and reliability through a GUI where users can view and manage all their integrated Kubernetes clusters and their current status. Users can scope their views to specific environments, clusters, teams, and applications using the workspaces.

To work, Komodor requires the installation of a “very lean agent” on top of each Kubernetes cluster that captures everything that happens inside the clusters, including management actions, changes in configurations, and events like deployments, said [Itiel Shwartz](https://www.linkedin.com/in/itiel-shwartz-18542853/?originalSubdomain=il), co-founder and CTO of [Komodor](https://komodor.com/about-us/), in an interview with The New Stack.

![](https://cdn.thenewstack.io/media/2025/03/f4ab8a69-komodor-drift-management-screenshot.png)
The Komodor management platform for Kubernetes.

This setup also provides a bevy of additional benefits, such as cost optimization and self-service troubleshooting for developers. It provides root-cause analysis of issues, sometimes through the help of its AI agent, [Claudia](https://komodor.com/blog/introducing-klaudiaai-redefining-kubernetes-troubleshooting/).

Komodor was raised in a cloud native environment and integrates with [GitOps](https://thenewstack.io/gitops-git-push-all-the-things/) engines like [Argo](https://thenewstack.io/how-far-can-you-go-with-argo/) and [Flux](https://thenewstack.io/why-flux-isnt-dying-after-weaveworks/), as well as with common Kubernetes operators and custom resources like [cert-manager](https://thenewstack.io/how-cert-manager-got-to-500-million-downloads-a-month/) and [ExternalDNS](https://github.com/kubernetes-sigs/external-dns).

## Challenges of Drift
Increasingly, Komodor’s users — which include admins for large financial services and Fortune 500 companies — have noticed in their Day 2 operations that their Kubernetes deployments may, over time, have drifted from their original configurations, or “desired states.”

This is often called configuration drift.

This may happen due to a number of causes, including:

**Manual changes,**or direct modifications made to the cluster configuration without updating the source of truth (like Git repositories).**Inconsistencies in automation,**such as errors or oversights in automation scripts.**Variations across infrastructure providers**due to differences in underlying hardware.**Misconfigured deployments,**such as incorrect parameters.**Incomplete rollouts,**due perhaps to service interruptions or miscellaneous hardware failures.**Outdated container images or applications**that were inadvertently installed or never updated.
These changes can occur both to manual deployments or even through [Infrastructure-as-Code (IaC) deployments](https://thenewstack.io/introduction-to-infrastructure-as-code/), which are designed to prevent such inadvertent shenanigans.

Even GitOps environments are not immune to drift, Shwartz said. GitOps can become tricky in large-scale, multicluster environments, and multi-environment deployments can be difficult to express and manage purely within a GitOps framework.

## How Komodor Will Help Remediate Configuration Drift
Komodor manages configuration drift by automatically detecting deviations and provides the tools to identify the root causes.

One of the crucial aspects of the service is the timeline view, which shows how a cluster’s behavior has changed over time and offers side-by-side views of how attributes have changed, Shwartz noted. It can show a sequence of events as they occurred, which can help pinpoint the cause of anomalies.

Drift can be detected without fancy services, using tools such as the `Kubectl Diff`
command or even basic log analysis, but they can leave an admin helplessly flailing in a sea of data.

Other commercial drift detection tools include [Quali Torque](https://www.quali.com/torque/) and SUSE’s [StackState](https://www.stackstate.com/).

On April 22, the company will offer [a webinar](https://tracking.us.nylas.com/l/2699a4514c1e402c9bf2a8b051d36150/5/0384502b54f182e6d8f5fbaddf1ff1d15b86d9975ec4309680da339145b65ef3?cache_buster=1742994023) to explain more. Or you can go ahead and [request a demo](https://tracking.us.nylas.com/l/2699a4514c1e402c9bf2a8b051d36150/6/553ae4611df43a3ca74ea977728e99f83cc259b22ed273787ac7a6fbca5ec108?cache_buster=1742994023).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)