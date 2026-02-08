If Kubernetes admins don’t have enough to worry about with the upcoming [Nginx gateway cutoff](https://thenewstack.io/cncf-retires-the-ingress-nginx-controller-for-kubernetes/), they now may need to rifle through their Helm charts to potentially thwart a dangerous setting.

Security researcher [Graham Helton](https://grahamhelton.com/) has [shared a Kubernetes vulnerability](https://grahamhelton.com/blog/nodes-proxy-rce) he unearthed that allows some random user, armed with read-only permission, to run arbitrary and even privileged commands on any pod in a cluster.

His trick is to use a service account with permissions for the Kubernetes `nodes/proxy GET` resource, which is used by dozens of monitoring tools, and provides access for issuing privileged-level pod commands.

In other words, it’s a feature, not a bug.

## Working as intended

Helton initially reported the quirk as a bug in November through the [Kubernetes bug bounty program](https://x.com/GrahamHelton3/status/2015789987799667097). The issue was soon marked closed, marked as “intended behavior.”

The`nodes/proxy GET` call is intended for service accounts, and is used by many monitoring tools.

How a get request gets transformed into a full remote code execution is [due to a mismatch](https://x.com/GrahamHelton3/status/2015789990429487294) between Websockets and the Kublet’s authorization logic.

Helton found Helm charts for 69 tools that used`nodes/proxy GET`. For them, it provides the permissions to reach a node’s internal API to get the data they need.

“Some of the worlds biggest kubernetes vendors rely on it because there is no generally available alternative,” Helton [writes on X](https://x.com/GrahamHelton3/status/2015789990429487294).

So, no [CVE alert](https://thenewstack.io/why-the-value-of-cve-mitigation-outweighs-the-costs/) for `nodes/proxy Get` behavior, because its not a vulnerability.

The official path forward is to use [KEP-2862](https://github.com/kubernetes/enhancements/issues/2862) (“Fine-Grained Kubelet API Authorization”), an extension expected in the upcoming Kubernetes 1.36 release, expected in April.

## How to bring down a Kubernetes cluster

So, if you have a service account that’s subscribed to `nodes/proxy GET`, and can reach a Node’s Kubelet on port 10250, then you are free to issue any command to `/exec` endpoints, including commands for privileged system pods that could destroy the cluster entirely.

Here are some other things you can do, [according to Helton](https://x.com/GrahamHelton3/status/2015789990429487294): steal service account tokens from other pods, or execute code in control plane pods.

Worse yet, no record would be left of such malicious actions, as the “Kubernetes AuditPolicy does not log commands executed through a direct connection to the Kubelet’s API,” Helton explains.

Here is the cluster’s permission set that makes this all possible:

```

 # Vulnerable ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
name: nodes-proxy-reader
rules:
- apiGroups: [""] \
resources: ["nodes/proxy"]
verbs: ["get"]
```

If you want to try it out for yourself, Helton [posted an entire lab](https://labs.iximiuz.com/tutorials/nodes-proxy-rce-c9e436a9).

## Precautions to take?

Hard questions may have to be asked for those with these system settings: Do you value your telemetry more than your security?

Industry observer Alex Ellis [calls the disclosure](https://x.com/alexellisuk/status/2016096083168915636) “worrying.”

Cloud native security company Edera field CTO [Jed Salazar](https://www.linkedin.com/in/jedsalazar/?originalSubdomain=ca) notes the vulnerability points out how Kubernetes workloads are different 2026 than they were in 2016.

They’re no longer just stateless apps. They’re “AI training pipelines with proprietary model weights, financial trading systems, and healthcare applications with patient data,” he writes. “The blast radius of a monitoring stack compromise in 2026 is categorically different from 2016.”

The answer, Salazar writes, is architectural isolation, which is [what Edera offers](https://thenewstack.io/kubecon-eu-2025-edera-protect-offers-a-secure-container/) (the configuration did not leave Edera users vulnerable, Salazar notes).

For everyone else, until KEP-2862 fully trickles down to production, Salazar advised a number of  precautions:

1. *Audit your RBAC policies for nodes/proxy permissions immediately,*
2. *Consider whether monitoring tools truly need direct kubelet access,*
3. *Implement network policies restricting access to kubelet port 10250,*
4. *Plan your migration to KEP-2862 fine-grained permissions when they GA,*
5. *Adopt workload isolation technologies that limit blast radius regardless of upstream decision*s.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)