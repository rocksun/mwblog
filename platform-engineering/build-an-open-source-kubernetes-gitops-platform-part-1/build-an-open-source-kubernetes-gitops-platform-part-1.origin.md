# Build an Open Source Kubernetes GitOps Platform, Part 1
![Featued image for: Build an Open Source Kubernetes GitOps Platform, Part 1](https://cdn.thenewstack.io/media/2025/01/69041ce4-gitops-1024x576.jpg)
With Kubernetes recently celebrating its 10th birthday, its landscape of popular [open source](https://thenewstack.io/open-source/) products reached such a maturity that whatever your platform must use, there is a reliable open source product ready to help.

A common cluster typically includes many open source tools since Kubernetes without these tools doesn’t add value to your business. These tools are all part of an intimidatingly large Cloud Native Computing Foundation (CNCF) [landscape](https://l.cncf.io/) that offers a menu of microproducts. There are tools to help do things like [manage access to your services](https://thenewstack.io/postgres-with-kubernetes-self-managed-or-managed-service/), create and renew your Transport Layer Security (TLS) certificates, manage your Domain Name Security (DNS) records and keep your secrets safe and synced. These tools provide pillars for how you build and deliver your apps and infrastructure to preproduction and production software environments for your users.

This walkthrough is a comprehensive example for building a multicluster GitOps platform using popular open source tools in the [Kubernetes](https://thenewstack.io/kubernetes/) space.

**Step 1. Choose Your Cloud**
The first thing you’ll need to do is choose the cloud you’ll call home. Every cloud is a little different, but Kubernetes levels the playing field quite a bit if you focus on cloud native architecture. Hyperscalers boast reliability, while simpler clouds showcase cost savings, speed and simpler Infrastructure as Cloud (IaC) and cloud experiences.

With the right cloud native tool choices, your cloud choice matters far less. In a Kubernetes landscape, it’s easy to find cloud-agnostic products. Argo, [cert-manager](https://thenewstack.io/how-cert-manager-got-to-500-million-downloads-a-month/) , external-dns and CI Runners all work the same way in different clouds.

If [hybrid cloud or multicloud](https://thenewstack.io/kubernetes-applications-for-multicloud-hybrid-cloud-environs/) is an eventual part of your story, do your best to avoid cloud-specific tech when building your platform. Cloud tutorials, blueprints and reference guides might try to guide you to use their proprietary ingress controllers, secrets manager, etc., but there are often more portable open source alternatives on the CNCF landscape to choose from. It helps to do your research first.

**Step 2. Pick Your Git Provider**
It’s hard to find an option more compelling than GitHub or [GitLab](https://about.gitlab.com/?utm_content=inline+mention). Both have reliable SaaS solutions to host your git repositories and container images, and both offer self-hosting. You really can’t go wrong with either provider.

For public-facing open source code, I would lean toward using GitHub. If you’ll be self-hosting your git server, I would lean toward GitLab. If you have neither of these requirements, GitHub generally has the popularity vote. Important questions you should ask yourself before you get started are: What might I ever open source, and why might I want my source code to be [privately hosted and removed from a SaaS](https://thenewstack.io/private-saas-a-new-paradigm/) ecosystem?

**Step 3. Your Platform Domain and DNS Provider**
If you don’t have an opinion on DNS providers yet, Cloudflare is a great provider to bet on, especially for an unclear cloud future. You can purchase and register a domain directly or point your existing domain to Cloudflare nameservers from your current DNS registrar. Cloudflare provides some great services and its configuration user experience is really straightforward.

Most folks who plan to stay centralized in a single cloud use their cloud provider’s DNS service. This is a fine instinct to follow. In the Kubernetes landscape cert-manager and external-dns products have exceptional cloud support across most clouds, and those two products, along with IaC, are usually the only DNS stakeholders.

**Step 4. Define Your Infrastructure as Code**
IaC is the first code that you’ll have to produce for your platform. IaC is the code that defines the cloud resources you need. It helps to configure the “desired state” of any software that you use, like GitHub or [DataDog](https://www.datadoghq.com/?utm_content=inline+mention), but this can compete with what you want out of GitOps. Your instinct should be to let GitOps win that battle when you can. GitOps is simply a better workflow for managing application configuration on Kubernetes.

There are only a few frontrunners in the IaC space. [Hashicorp](https://www.hashicorp.com/?utm_content=inline+mention)’s Terraform has been the darling of IaC for the better part of the past decade. Some licensing decisions loosened their grip on the industry allowing OpenTofu to emerge as a popular fork from the infrastructure giant.

Other popular options include Crossplane, which lets you define your IaC in a Kubernetes native way, and Pulimi, which lets you write your IaC in more popular development languages.

When you write your IaC, avoid the temptation to build an IaC monolith. Keep your state small and break things up into reasonably isolated domains. For example, you can define your cloud, git, secrets and user resources in distinct IaC spaces. This keeps your IaC execution times fast and reduces the blast radius of your IaC changes.

Other considerations in the IaC realm are the automation and governance of your IaC execution. Atlantis, Crossplane, Spacelift, Env0 and Terraform Cloud all do well in this space. Once you have your IaC established, the best thing you can do for your audit trail is to centralize and automate its execution. This arranges things so your human users don’t need their own permissions to these resources as the platform automation takes over the responsibility.

**Step 5. Choose Your GitOps Engine**
GitOps is similar to IaC in many ways. GitOps allows you to define a desired state and then make it the actual state. Where IaC tools often do this by running a command, GitOps does this by automatically binding the desired state of something in a git repository to its actual state in a Kubernetes cluster.

Operationally, this means that to make a change to an app in your cluster, for example a new version of the app, you change the instance in your cluster with a pull request for a change to a `gitops`
repository for housing all of your application configurations. This provides a significant advantage to your platform’s security, disaster recovery, operational transparency and configuration repeatability.

There are two leading GitOps tools, Argo CD and Flux CD. Both have vibrant communities and solve huge problems in the Kubernetes space. They are both dependable choices with good release track records, robust open source governance models and a spirit of coding through the community.

I think Argo CD might be the best piece of software that’s ever been written. I’ve heard the same said of Flux CD. [My GitOps heart beats strong](https://thenewstack.io/i-need-to-talk-to-you-about-kubernetes-gitops/) for both projects, and I love their joint mission.

**Step 6. Define Your Management Pillars**
You’re going to have to define which tools you’re going to use in your initial control plane cluster or your management cluster. There are a ton of ways to do this, but for practical purposes I’m going to provide an example based on the approach at Konstruct.

At Konstruct a typical management cluster would look something like this:

The management cluster establishes your foundational tech to build, manage and deliver apps and additional infrastructure.

For the control plane at Konstruct we choose:

**Argo CD:**a GitOps engine to manage everything in Kubernetes and everything that we extend Kubernetes to manage outside of the cluster.**Atlantis:**automates your Terraform/OpenTofu executions in your pull request to provide IaC governance.**Crossplane:**uses GitOps for IaC operations.**vCluster:**creates low-cost isolated clusters inside of our clusters.
To access cluster services:

**ingress-nginx:**allows outside access to the services that run in your cluster.**external-dns:**automatically points your hostname DNS records to your load balancers.**cert-manager:**generates and renews creates short-lived TLS certificates for your services.**Let’s Encrypt issuer:**provides free browser-trusted TLS certificates for your services.
For CI:

**github-actions-runer-controller****:**a self-hosted GitHub actions runner to run GitHub CI jobs privately.**gitlab-runner****:**a self-hosted runner to run GitLab CI jobs privately.**Argo Workflows:**We have a set templates that build containers, Helm charts and do GitOps delivery and promotion.**ChartMuseum:**a simple interface for hosting Helm charts backed by S3.
For users and secrets:

**Vault/OpenBao:**secrets engine, users, groups and OpenID Connect (OIDC) provider so the platform has instant single sign-on.**External Secrets Operator:**abstracts your secrets engine from Kubernetes and keeps your secrets in sync.**Reloader:**operator that restarts pods when secrets in Kubernetes change.
For a platform portal:

creates physical and virtual Kubernetes clusters using GitOps and manages the application delivery to those clusters.[kubefirst-pro](https://konstruct.io/kubefirst-pro):
A lot of the appeal of Kubernetes comes from its vendor-agnostic architecture, which enables these somewhat-swappable components. You could use these same tools that we use, or you can choose alternatives from the CNCF landscape that cover the same functions.

**Provision Your Cloud Native Platform**
Congratulations, you’ve now selected your cloud, DNS, and git provider. You’ve established the pieces of tech that you want in your management platform; you know what your IaC and GitOps technologies will be; and now you’re ready to begin provisioning your new open source platform for your organization.

In the next post, we’ll continue with the steps to execute starting from platform creation day. We will walk through the creation of the the platform bots, creation of your GitOps file content, the execution of your cluster provisioning IaC, the GitOps cluster bootstrapping process, the establishment of your environments and workload cluster fleets, the modeling and provisioning of your downstream workload clusters and the delivery of your first built app to your new environments. Join me for the continuation of this platform building journey in Part 2.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)