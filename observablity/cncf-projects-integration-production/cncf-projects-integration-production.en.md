I still remember the first time we lost sleep over something that wasn’t a bug.

It was a Tuesday. Grafana dashboards showed blank panels for Cilium network metrics. Hubble was working fine — DNS visibility, TCP flows, and HTTP latency were all there in the Hubble UI. But the on-call engineer staring at Grafana at 2 AM couldn’t see any of it. The reason? Prometheus had no ServiceMonitors wired to Cilium’s agent and operator pods. Two [Cloud Native Computing Foundation](https://www.cncf.io/) (CNCF) projects, both installed correctly, were completely invisible to each other.

This is what’s known as the integration tax. It’s the [hidden cost of running multiple](https://thenewstack.io/the-hidden-costs-of-multiple-service-catalogs-in-development/) CNCF projects together in production, and it’s where most platform teams spend 80% of their time — not installing projects and not tuning them individually, but wiring them together. Hence, they actually talk to each other.

> “This is what’s known as the integration tax. It’s the hidden cost of running multiple CNCF projects together in production.”

## Every team builds the same stack. Every team breaks it differently.

The CNCF [landscape](https://landscape.cncf.io/?group=projects-and-products&view-mode=grid) has about 250 projects. In practice, most production [Kubernetes](https://kubernetes.io/) platforms settle on the same core stack of 20–30 cloud native tools. [Prometheus](https://prometheus.io/) for monitoring. [ArgoCD](https://argoproj.github.io/cd/) for GitOps. [Cilium](https://cilium.io/) for networking. [cert-manager](https://cert-manager.io/) for TLS. [Velero](https://velero.io/) for backups. [Sealed Secrets](https://fluxcd.io/flux/guides/sealed-secrets/) for credentials. [Kyverno](https://kyverno.io/) for policy. You install them. You write values files.

Wiring happens. Then the failures begin, and they’re never in any single project’s issue tracker.

## Where CNCF projects collide

**cert-manager versus ingress controllers.** We ran into this issue across three cloud providers. cert-manager’s HTTP-01 ACME challenge expects to serve a token over plain HTTP. But if your ingress controller enforces a global HTTP-to-HTTPS redirect —which it should for security —  every ACME validation request gets 301’d before reaching cert-manager’s solver pod. Certificate renewals fail silently. You find out when customers see expired TLS warnings in their browsers. The fix? DNS-01 challenges via Route53, Cloud DNS, or Azure DNS.  But that’s cloud-specific IAM scoping that no Helm chart configures by default. You discover these limitations only after the incident.

**Prometheus versus kubelet.** Here’s one that took us weeks to diagnose. kubelet exposes metrics on four scrape paths. Two of them — `/metrics` and `/metrics/probes`  — both emit `process_start_time_seconds` with identical timestamps because they’re the same process. Prometheus dutifully scrapes both, sees duplicate samples, and fires `PrometheusDuplicateTimestamps`. The alert is noisy. The root cause is invisible without reading the kubelet source.  But the fix is a Jsonnet relabeling rule that drops an entire scrape endpoint. None of these are bugs. Every project works exactly as documented. The failures live in the gaps.

> “None of these are bugs. Every project works exactly as documented. The failures live in the gaps.”

## Cluster API gave us one workflow for four clouds

Before [Cluster API](https://github.com/kubernetes-sigs/cluster-api) (CAPI), provisioning clusters meant choosing a cloud vendor’s CLI. `eksctl` for AWS. `gcloud container clusters create` for GCP. `az aks create` for Azure. Each had its own lifecycle model, upgrade path, and disaster recovery story. You weren’t just locked into a cloud; you were locked into its opinions about managing Kubernetes.

CAPI changed the game. Your cluster is now a set of Kubernetes-native resources —  Cluster, MachineDeployment, MachinePool — and a cloud-specific provider translates them into infrastructure. We run CAPA on AWS, CAPG on GCP, CAPZ on Azure, and CAPH on Hetzner bare metal. The bootstrap sequence is identical everywhere: K3D management cluster → deploy provider → create workload cluster → `clusterctl` move to make it self-managing.

But here’s where the real value emerges: Day-2 operations. A Kubernetes version upgrade becomes a one-line change to a `MachineDeployment`. CAPI handles cordon, drain, and rolling replacement. A `MachineHealthCheck` automatically removes unhealthy nodes. Disaster recovery means recreating a management cluster, restoring Velero [backups from cloud storage](https://thenewstack.io/a-practical-guide-to-kubernetes-stateful-backup-and-recovery/), and letting CAPI resources reconcile. The entire cluster rebuilds itself from the Git state. This is where Cluster API—like the rest of the CNCF stack—reveals whether your integration work actually holds together under pressure.

## The architecture that finally stopped the bleeding

After years of firefighting integration failures across clouds, we landed on a pattern that finally made things sustainable: a two-repo GitOps split. This approach applies whether you’re using commercial platforms or assembling your own stack from open source projects.

**Platform repo:** 100+ Helm charts with production-tested defaults. Cilium NetworkPolicies baked into each chart. Prometheus ServiceMonitors pre-wired. cert-manager annotations are configured for the right challenge type. This configuration is shared across all clusters in all clouds.

**Config repo:** One per customer or environment. Only values that genuinely vary between clusters: domain names, node counts, GCP project IDs, AWS account roles, and Hetzner server types.

ArgoCD watches both. When we fix the Prometheus duplicate timestamps issue in the platform repo, that fix propagates to every cluster (AWS, GCP, Azure, bare metal) via a version bump. One pull request. No per-cluster tickets. No human memory of, “Oh, we need to update the relabeling rule on three different systems”; the integration logic lives in code.

## Hard-won lessons from production

**Generate your monitoring, don’t assemble it.** We use Jsonnet to produce the entire kube-prometheus stack from a single per-cluster vars file. Custom alerting mixins — Velero backup age, [CloudNativePG](https://cloudnative-pg.io/) replication lag, kubelet certificate expiry — live as Jsonnet libraries alongside upstream rules. A single build.sh produces everything. Reproducible. Diffable. Version-controlled. When Prometheus upgrades break your custom rules, the diff is immediate, and the fix is testable before it reaches production.

**Embed NetworkPolicies in charts, not in post-deployment runbooks.** We ship Cilium NetworkPolicy templates inside 20+ Helm charts. Each chart declares its own egress requirements: what external APIs it calls and what internal services it needs. Reverse-engineering network rules from Hubble flow logs after deployment is like writing tests after shipping. Your policies drift. Security becomes guesswork. Embedding them in charts means the policy lives where it’s maintained.

**Automate disaster recovery at bootstrap.** Our provisioning creates cloud storage buckets (S3, GCS, Azure Blob) for Velero backups during initial cluster setup — not as a follow-up task that lives in a Jira ticket for six months. If you can run the bootstrap, you can recover from total cluster loss. Disaster recovery stops being a hope and becomes a testable reality.

**Encrypt secrets, then commit them.** Every credential — deploy keys, cloud IAM, and TLS certs — gets encrypted with Sealed Secrets before it touches Git. The decryption key gets backed up to cloud storage. Your Git repository becomes a complete, auditable record of every cluster’s state, including secrets. Drift detection works. Recovery is one pull request and one clusterctl move away.

**Let machines enforce policy.** Kyverno blocks deployments that are missing resource limits. Kubescape continuously scans CIS benchmarks and feeds violations into Prometheus alerts. Combined with Cilium network segmentation, your security posture becomes something auditors verify from Git history and live cluster state — not from a spreadsheet last updated two quarters ago.

## The compounding cost

The [integration tax](https://thenewstack.io/virtual-clusters-kubernetes-cost-isolation/) isn’t a one-time fee. Every Kubernetes version bump, every Helm chart upgrade, and every new CNCF project introduces new integration surfaces. If your monitoring is hand-crafted YAML, upgrading kube-prometheus from v0.13 to v0.17 means manually diffing hundreds of generated files. If it’s Jsonnet, it’s one line — the debt compounds.

The CNCF ecosystem is extraordinarily powerful. But power without integration is just a list of Helm installs. The work that actually matters—drift detection, coordinated updates, and disaster recovery automation—happens in the wiring. That’s where your platform either survives its second year or just becomes a collection of tools you stop trusting.

*Readers interested in exploring the framework discussed in this article further can find the project’s source code and detailed documentation on the [KubeAid repository](https://github.com/Obmondo/kubeaid) and the [KubeAid website](https://kubeaid.io/).*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/7f9b0407-cropped-83cd7737-rishi_mondal_new111-rishi-mondal-600x600.jpg)

Rishi Mondal is an SRE at Obmondo, where he builds and maintains KubeAid an open-source Kubernetes management platform integrating 25+ CNCF projects. He's a CNCF KubeStellar Maintainer, Docker Captain, Linux Foundation Mentor, and GSoC Mentor at CNCF. He was featured...

Read more from Rishi Mondal](https://thenewstack.io/author/rishi-mondal/)