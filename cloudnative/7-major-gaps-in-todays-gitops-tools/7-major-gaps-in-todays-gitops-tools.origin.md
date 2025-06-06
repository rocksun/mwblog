# 7 Major Gaps in Today’s GitOps Tools
![Featued image for: 7 Major Gaps in Today’s GitOps Tools](https://cdn.thenewstack.io/media/2025/05/120318c3-gaps-gitops-tools-1024x576.jpg)
GitOps has revolutionized infrastructure management and the software delivery process forever. With [Git](https://roadmap.sh/git-github) as the single source of truth, [GitOps](https://thenewstack.io/4-core-principles-of-gitops/) replaced traditional, manual and error-prone deployment processes with a faster, automated approach. Tools like Argo CD and Flux CD have dominated the conversations by leveraging GitOps as their core principle in [Kubernetes](https://thenewstack.io/kubernetes/) deployments.

However, as the cloud native landscape evolves and deployments grow more complex, these leading tools face new challenges in maintaining security, scalability and operational best practices. So, what does GitOps need to look like today to meet cloud native organizations’ demands for smarter and more secure Kubernetes deployments?

## Rise of GitOps Tools: Flux and Argo CD
Weaveworks coined the term “GitOps” in 2017. The core idea behind GitOps is to use Git as the single source of truth for declarative infrastructure and application deployments.

Before GitOps, teams relied heavily on custom scripts (Python, Bash, etc.) or manual commands (`kubectl apply`
) to deploy applications. These manual approaches introduced several challenges, like making it hard to track changes or repeat deployments, and a lack of standardization meant processes were often prone to errors.

[GitOps emerged](https://thenewstack.io/extending-cicd-and-gitops-for-better-k8s-app-deployments) to tackle these challenges, and Flux was the first tool to adopt this model. Flux made deployments easier by directly pulling changes from the Git repository instead of pushing changes to the cluster. Then came Argo CD, which addressed Flux’s limitations by providing a visual dashboard and improving usability, which led to broader enterprise adoption.
Together, Flux and Argo CD paved the way for modern, reliable and scalable software delivery powered by GitOps.

## Lingering Gaps in GitOps Tools
While GitOps improved software delivery, these GitOps tools introduced their own set of [challenges](https://thenewstack.io/extending-cicd-and-gitops-for-better-k8s-app-deployments/). Teams started facing issues with rollbacks, approval processes and managing too many tools.

Here are some common gaps in current GitOps tools.

### Multicluster Management Hurdles
Managing multiple Kubernetes clusters with these GitOps tools often introduces significant complexity. Organizations have to pick between deploying separate Argo CD instances per cluster, which results in high operational overhead, or using a single, centralized Argo CD instance for all the Kubernetes clusters, which can become a single point of failure. Such architectural challenges make it difficult to maintain visibility, control and resilience across multiple environments, and multicluster GitOps becomes a real challenge.

### Missing Policy-Based Deployments
GitOps tools like Flux and Argo CD act only as Git-to-Kubernetes syncing tools. While they excel at keeping the cluster state in sync with what’s defined in Git, they lack native support for policy-based deployments that govern how and when deployments should occur.

For example, organizations may want to enforce manual approvals, apply security or compliance checks, or restrict deployments to specific time windows. Such policies are necessary to prevent unverified or unintentional changes from making it to production.

### No Native SLO-Based Rollbacks
Current GitOps tools lack native support for rollbacks driven by service-level objectives (SLOs). SLO-based rollbacks allow teams to quickly revert to the previous stable version when deployments impact key user experience metrics. Without this capability, teams are forced to write custom scripts or rely on an external tool, which increases complexity and tool sprawl.

### Lack of GitOps Promotion Capabilities
In GitOps, “promotion” is the process of moving an application from one environment to another, such as from development to testing, and then to production, by making declarative changes in Git. Current GitOps tools lack native support for GitOps promotion. Teams often have to rely on manual steps, branch management or custom pipelines to promote applications across environments, which goes against the core GitOps principles of automation and consistency.

## The Need for Application-Aware GitOps
To overcome the limitations of current GitOps tools, the next generation of platforms must go beyond basic Git-to-Kubernetes syncing. They need to be application-aware, secure by design and flexible enough to support [complex delivery at scale](https://thenewstack.io/the-ultimate-guide-to-software-distribution). Here’s what a modern GitOps platform should provide:

### Flexible Rollback Capabilities
Rollback should be more than just reverting a Git commit. GitOps platforms need to support intelligent, automated rollbacks based on real-time metrics like SLO violations, error rates or latency spikes. This minimizes user impact without having to rely on manual intervention or custom scripts.

### Support for Advanced Deployment Strategies
[Deployment strategies](https://devtron.ai/blog/kubernetes-deployment-guide/) like canary, blue-green and progressive rollouts shouldn’t require extra setups or third-party tools. Instead of integrating third-party tools like Flagger, teams should be able to configure and execute advanced deployment patterns directly within the GitOps platform.
### Simplified Multicluster Deployments
Handling [deployments across multiple clusters](https://devtron.ai/blog/managing-kubernetes-resources-across-multiple-clusters/) shouldn’t be complicated or fragile. A modern GitOps platform should make it easy to manage applications in different clusters through a single, unified view while still giving teams the flexibility to control each cluster independently.

### GitOps-Powered Application Promotion
[Promoting applications](https://devtron.ai/blog/application-promotion-in-devtron/) from development to staging to production shouldn’t be a manual or complicated process. A good GitOps platform should let teams define clear promotion workflows in Git so apps move through each environment automatically and safely without extra steps or scripts.
### Built-in Approval Policies
[Approval policies](https://devtron.ai/blog/approval-based-deployments-on-kubernetes/) should be part of the GitOps process from the start. Whether it’s a quick sign-off from a teammate or an automatic check for issues, the platform should make sure that approval gates are built right into the GitOps workflow so that only safe, reviewed changes get deployed.
### Advanced Role-Based Access Control
[Role-based access control (RBAC)](https://devtron.ai/blog/sso-and-rbac-a-secure-access-strategy-for-your-kubernetes/) should be built directly into the platform and not be dependent on Kubernetes clusters, which can add unnecessary complexity. Teams should be able to set detailed permissions within the platform across environments, applications and workflows, ensuring security and compliance without unnecessary extra overhead.
### Built-in Observability
Clear visibility into deployments, sync status, app health and historical changes is essential. In 2025, GitOps platforms should provide [built-in observability](https://devtron.ai/blog/kubernetes-observability/), enabling teams to easily troubleshoot issues, track rollbacks and monitor the entire deployment process from a unified dashboard.

## Modernizing App Lifecycle Management
![Devtron dashboard](https://cdn.thenewstack.io/media/2025/05/ed4367e5-devtron-dashboard.png)
Source: Devtron.

[Devtron](https://devtron.ai/product/deployment-with-gitops) is built to simplify GitOps for modern teams. It supports flexible rollbacks, advanced deployment strategies and effortless multicluster management. With built-in approval gates, fine-grained RBAC and robust observability features, Devtron maintains security, compliance and transparency throughout the deployment process. Its unified platform gives teams full control, allowing them to deploy smarter and safer, accelerating software delivery without compromising on quality.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)