ATLANTA — Let’s just say that [Okta’s Auth0](https://thenewstack.io/with-auth0-purchase-okta-will-boost-access-apis-for-developers/) platform customers for private cloud weren’t getting what they likely wanted. [Okta](https://thenewstack.io/okta-wants-to-secure-your-ai-agents-too/)’s support was problematic at best, especially for those customers at scale.

This led to a decision to take a huge bet on open source for [GitOps](https://thenewstack.io/4-core-principles-of-gitops/), specifically the [CNCF](https://cncf.io/?utm_content=inline+mention)-graduated project [Argo CD](https://thenewstack.io/survey-argocd-leaves-flux-and-other-gitops-platforms-behind/) (previously called Argo Workflows). It wasn’t just a simple lift and shift; instituting it across such a wide scale of operations required over five years. During [KubeCon + CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) here, Okta engineers [Jérémy Albuixech](https://github.com/jeremy-albuixech) and [Kahou Lei](https://www.linkedin.com/in/kahoulei/) detailed their trials and tribulations during their talk, [“One Dozen To One Thousand Clusters: How Argo Kept up as We Scaled.”](https://kccncna2025.sched.com/event/27FcE/one-dozen-to-one-thousand-clusters-how-argo-kept-up-as-we-scaled-jeremy-albuixech-kahou-lei-okta)

The end result: “We can safely say that the results now show they can scale over a thousand clusters, up from just a dozen or so a few years ago,” Albuixech said during the talk.

## Credit Due

Before diving into Argo CD and how this came about, it’s worth saying what Argo CD is and what GitOps entails. Argo CD is not just a software tool or platform for scaling [Kubernetes](https://thenewstack.io/kubernetes/) clusters, but it is a well-received project with growing community support. It would also be amiss not to mention the parallel CNCF-graduated project [Flux](https://thenewstack.io/why-flux-isnt-dying-after-weaveworks/).

GitOps operators like Argo CD and Flux monitor git as the immutable source of truth for the desired state and apply that desired state to the actual state. The immutable structure of Git also automates changes to applications and code in clusters when vulnerabilities are discovered — as they invariably will be — during runtime. Likewise, if someone were to modify runtimes directly (such as would happen during a security breach), GitOps operators will automatically detect these changes and overwrite them with the desired state in Git.

Flux and Argo CD continuously monitor application definitions and configurations defined in a git repository and compare the specified state of these configurations with their live state on the cluster. Argo CD reports any configurations that deviate from their specified state. These reports allow administrators to automatically or manually resync configurations to the defined state. Again, git always serves as the single source of truth.

## Open Source Truth

Flash back to over five years ago. In its first iteration, Albuixech and Lei described how Okta’s Auth0 platform was mainly a way to host services for customers who wanted their infrastructure and configuration stored in a private cloud account. It was targeted for a very small subset of customers and, as a result, it was not built with high scale and automation as priorities. It had [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) configurations and infrastructure. Updates were done manually by an operator, access was not as secure as it could be and it relied on early days cloud infrastructure — basically code running in virtual machines (VMs).

“As demand increased, we needed a new platform design,” Albuixech said. “After research and proofs of concepts, we ended up with a cloud native architecture using the Argo project heavily.” Argo CD handles service provisioning, Argo Workflows handles deployments, Terraform (with a custom provider) handles Infrastructure as Code (IaC), and all of this is orchestrated by control plane services so we can manage all customer environments, Albuixech said.

## Hard Work

One of the beautiful things about open source projects is how the community users are constantly proposing changes as news and the project itself grows. That said, open source Argo CD exhibits several “significant” challenges, as Albuixech and Lei detailed during their talk.

These include how the auto-sync feature cannot be used in their deployment pipeline because it cannot handle Terraform dependencies or respect customer-specific deployment windows, requiring a custom “auto-sync” using Argo Workflows and the control plane.

As Lei described, Argo CD’s auto-sync ensures the state in the Kubernetes cluster always matches Git. “However, we cannot use auto-sync in our deployment pipeline because of our release model. Each release candidate is a bundle containing service image versions, [Terraform](https://thenewstack.io/terraform-isnt-dead/) code, Kubernetes manifests, plugins and custom logic,” Lei said.

“The homegrown application-X plugin initially caused refresh operations to take minutes because customize spawns a subprocess for each plugin, necessitating a forked binary. Running different plugin versions per customer required a [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)-in-Docker approach, adding further operational complexity,” Lei said.

One release manifest corresponds to one Argo application, and one Argo application represents an entire customer cluster, Lei said. Because infrastructure generated by Terraform affects the configuration and secrets needed by services, Terraform must run before the Argo CD sync. Auto-sync cannot accommodate this dependency, nor can it respect customer-specific deployment windows. The workaround: “So we implement our own ‘auto-sync’ using Argo Workflows plus the control plane,” Lei said.

Other challenges included how transient deployment failures — including crash loops, sync conflicts, plugin failures and stuck syncs — were common. To manage these, the team built a command line interface (CLI) wrapper that classifies failures, enforces timeouts and controls retries, Albuixech and Lei described. “At scale, the application controller often crashes under load, the UI becomes very slow and application statuses can be misleading, requiring controller scaling, infrastructure improvements, CLI tooling and ignore-resource settings,” Lei said. Upstream bugs, such as a race condition in the application controller and performance issues from untracked resources, had to be addressed internally.

Workflows with 50 or more steps, maintained by multiple teams, risk conflicts and require dynamic sub-workflow management. Large workflows for Kubernetes upgrades, [Postgres](https://thenewstack.io/how-distributed-postgres-solves-clouds-high-availability-problem/) blue-green updates, load tests, chaos tests and CI validation can overwhelm the Argo UI, prompting workarounds like launching labeled child workflows. Some UI limitations forced unusual solutions, such as a Chrome plugin to remove the “Terminate” button, which bypassed exit hooks and broke automation. Despite these challenges, the platform continues to scale through extensive custom tooling, workflow orchestration and careful operational management, Lei said.

## Amazing, Really

![](https://cdn.thenewstack.io/media/2025/12/949975ff-img_7790-2.heic)Given a scan of the pull requests issued and feedback on GitHub for this wildly successful open source project, these are very common problems they faced, and the collaborative fixes are on offer. It’s also good to keep in mind that this is a huge success for a major open source project in terms of its implementation. This is not just a very cool GitOps platform technology, but as it continues, Argo CD continues to demonstrate its merit for Kubernetes, especially in GitOps at scale. And not to forget Flux, as it has very proven adoption as well.

Albuixech and Lei are obviously not marketers, but here is how Lei described success: “Despite these challenges, the platform continues to scale through extensive custom tooling, workflow orchestration and careful operational management.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)