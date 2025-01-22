# Build an Open Source Kubernetes GitOps Platform, Part 2
![Featued image for: Build an Open Source Kubernetes GitOps Platform, Part 2](https://cdn.thenewstack.io/media/2025/01/42e59b96-platform-1024x595.jpg)
Your company’s internal developer platform (IDP) is one of your greatest assets. This complex fabric of infrastructure and software is how you will build, host, deliver and run the software your company writes. In [Part 1 of this walkthrough](https://thenewstack.io/build-an-open-source-kubernetes-gitops-platform-part-1/), we described the components of a common IDP and how to fast-track the platform-building process. Now let’s walk through creating your new platform.

**Step 7. Prepare Your Platform Robots**
Your platform will need some bot accounts to manage your cloud resources, git settings and (Domain Name Service) DNS records. You’ll need to create the new accounts for each function and generate API keys for each bot. These keys support your app configurations when you start bootstrapping your cluster in the next step. We recommend using email distributions (for example platformteam@domain.com) for your bots to help manage the teams that receive the system notifications.

**Step 8. Build Your Management Cluster**
Your management cluster is the centralized cluster that you’ll find in most Kubernetes-centered cloud architectures. Tools that manage your GitOps, [Infrastructure as Code (IaC)](https://thenewstack.io/infrastructure-as-code-in-2024-why-its-still-so-terrible/), CI/CD, secrets, users and security are usually good candidates for the management cluster.

No matter which cloud or IaC tool, the goal is the same. Using the IaC you already created (Step 4), create a state store, a network, a firewall and a [Kubernetes](https://thenewstack.io/kubernetes/) cluster. The result of this step is a successful connection to your new empty management cluster.

**Step 9. Add Your Instant GitOps Magic ✨**
It’s your moment to shine, my platform engineering head chef, just add that secret dash of your Instant GitOps Magic and wait for the Kubernetes oven to ding with your new platform.

**What Is Instant GitOps Magic?**
Remember that `gitops`
repository we asked you to build? (Step 5 in our first post). Regardless of the tool or service you choose, your management cluster uses a dedicated directory all its own. The cluster directory contains a set of files to represent every app that goes into the new cluster and specifies the order of installation.

If you choose to install Argo or Flux to the new cluster, just point either tool to that magic directory. Your GitOps engine automatically installs all your apps in the exact order needed so all of the chicken and egg dependencies are seamlessly sorted out.

Within a few minutes every app is installed with new DNS records propagating for your new set of platform services. Single sign-on is preconfigured through all of your app configurations. Your [infrastructure is now driven from your IaC and GitOps](https://thenewstack.io/bridging-the-gap-between-infrastructure-as-code-and-gitops/) desired state. Every last secret on the platform is in a single definitive source of truth, all continuously synced throughout the platform on a permanent loop. 🎉

**But How Do I Create GitOps Files?**
It takes most companies a decent amount of time and investment to come up with the right set of files. This is where a lot of the platform engineering discipline happens in a GitOps shop. You can choose to design, write, test and build all of this yourself. Or, you can take advantage of some of the amazing open source work that’s already out there.

At Konstruct, we think you should try out our [GitOps files](https://thenewstack.io/i-need-to-talk-to-you-about-kubernetes-gitops/) and start from there. [Kubefirst](https://konstruct.io/kubefirst) generates a fully hydrated `gitops`
repository that automatically gives you the popular open source tech stack that we described in our last article.

You keep the `gitops`
repo, and you can change any of our opinions into yours. Pull request changes to your new `gitops`
repo, and it’ll update in the management cluster that was just created for you. If you break something, just revert the git commit and try again, no big deal. If you choose to go it alone, we invite you to at least cheat off of our answers — we keep them in the back of the book in [our upstream gitops-template repository](https://github.com/konstructio/gitops-template). In exchange we’d love your feedback if there’s a reason our free lunch was not quite right for you.

**Step 10. Establish Your Workload Fleets**
Now that you’ve established your management cluster, you have a place to keep your users, groups, and secrets, and you have an automated way to run your IaC and GitOps. That’s really all you need to start creating your first fleet of workload clusters.

A workload cluster is just a cluster designed to run your software workloads. A common project might need a `development`
, `staging`
and `production`
workload cluster to run prerelease and released versions of the software that they’re building, for example.

Workload clusters are different from the management cluster in a few ways:

- They can easily depend on the management cluster tools (no chicken and egg).
- They don’t need all the same tools as the management cluster (you don’t need CI tools in your workload clusters for example).
- Versions of tools need to be kept consistent across clusters (so that production-east and production-west are identical, or so that staging truly represents a production-like experience).
In much the same way that you can create a `gitops`
repo from the upstream `gitops-template`
repository, you can also create workload clusters from workload cluster templates. If you decide to test out the Kubefirst Platform, you’ll get examples of these fleet templates directly in your new `gitops`
repository.

A workload cluster template directory is nothing more than a GitOps directory that has YAML defined for the cluster and its applications, but allows variables for details that you want to be different.

For example, if production-east and production-west are two workload clusters for your ideal infrastructure, you want them to use the same IaC modules and have the same versions of your platform tools, like external-dns, cert-manager, reloader, etc. But you also want them in different cloud regions with different cluster names and may need their services bound to different DNS hostnames. Parameterize what’s different so you can prompt your users for values at cluster provision time.

**Step 11. Establish Environments In Your GitOps Repo**
It is helpful to designate a different directory space in the `gitops`
repository to separate the platform tools from the apps that are being developed.

Keeping the apps you build in a different environment-driven directory structure allows you to build the cluster from a bleeding-edge workload cluster template, so you get all new versions of all of your platform tools, but you can late-bind your development environment applications into the new cluster by simply adding the environment link to your cluster in your gitops repo.

Keeping your environment details in a static space that doesn’t fluctuate as clusters come in and out of your infrastructure helps your developers and your continuous integration (CI) engineering. Using GitOps to deliver software requires that you update the app version in a specific location, and it’s helpful when this location doesn’t move as your infrastructure shifts.

**Step 12. Create Your Workload Clusters **
Now it’s time to create a workload cluster, bootstrap it with your template tools and copy your environment apps onto it.

A workload cluster can be a virtual cluster or a physical cluster. Virtual clusters don’t need any new physical infrastructure to be created for them. Instead, with the power of vcluster, you can create new Kubernetes clusters so they live inside of your existing clusters. A vcluster behaves like a fully isolated cluster but without the costs of the additional control plane in your cloud.

On Kubefirst, you can add a completely new, fully hydrated vcluster to your existing cluster with our default templates and they only use ~1GB memory and ~1 CPU core from their host cluster. That’s a very lightweight and inexpensive layer of full cluster isolation.

**Step 13. Deliver Your First Built Application**
Since you’re managing your git repositories using automated IaC, pull request a new git repository to your `gitops`
repo. Your pull request will show you a new plan that adds your repo and applies it once approved.

With a new repository in place, add your source code, a chart, a Dockerfile and some CI to build and deliver the application to your environments.

This is where religions are formed, and everyone has a different CI religion. I don’t want to tell you the “right way” to do CI because there are a great many right ways to do this.

Regardless of the tools you choose, the tasks that the CI needs to accomplish are:

- Building a container, preferably without using root or privileged pods
- Publishing a container to your container hosting provider
- Setting the container image tag as the default image for your helm chart
- publishing the Helm chart
- Setting the desired version of the Helm chart for your app instance in each of your application’s environments using your CI’s progressive pipeline stages
- Add testing to prevent/promote your releases to the next environment
In the Kubefirst Platform, we generate the gitops repo with all of your platform configurations, along with a sample application (metaphor) repo to serve as a demonstration of how to build and deliver a microservice repo using GitOps.

With your CI now in place, you can kick off a job to build your app container and chart, and set the desired state of your app instances to the new version of your app, one environment at a time.

**Step 14. Establish Your Day 2 Components**
Now it’s time to establish the components for your Day 2 operations, or the tasks that never end: more apps, more tech, more considerations, more monitoring.

Some of the tools we like include:

For Kubernetes policy enforcement we like Kyverno a lot for its Kubernetes native configurations and easy onboarding experience.

For logging, [monitoring and observability](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/), we like Datadog for its instant Kubernetes observability features, reliability and customer support. This deviates from our self-hosted free tools mentality quite a bit, but we find this SaaS offering is deeply rich, most projects rely heavily on observability. Self-hosted alternatives for what Datadog provides often include a combination of Prometheus, Grafana, Elasticsearch, Fluentbit, Kibana and Jaeger with OpenTelemetry.

For container scanning, we like open source Trivy, but there are many products in the security space that allow you to defend at different layers of depth, and choosing the security model that’s right for your company is a strategic part of your company’s platform-building initiative. The [platform engineering maturity model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) can help guide you through your in-depth considerations across many different verticals.

**Your Most Important Build: Healthy Platform Culture**
For the most successful companies, the final stage of your platform building never ends. When a company embraces change, speed and delivery but must comply with the quality, reliability and security demands of the mission, the desire to reduce friction will always be present.

Create an environment where this is absolutely expected, where you have to interview your platform users about their experience because of that expectation. When a need from your users surfaces, prioritize it on your platform’s roadmap and celebrate its use.

With a healthy culture of feedback, transparency and shared ownership, you’re on your way to surviving whatever the software industry throws at you next. I hope this walkthrough helps you create the [perfect cloud native platform](https://konstruct.io/) for your needs.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)