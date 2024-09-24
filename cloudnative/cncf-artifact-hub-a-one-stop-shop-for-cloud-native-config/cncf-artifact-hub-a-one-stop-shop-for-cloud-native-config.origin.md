# CNCF Artifact Hub, a One-Stop Shop for Cloud Native Config
![Featued image for: CNCF Artifact Hub, a One-Stop Shop for Cloud Native Config](https://cdn.thenewstack.io/media/2024/09/a52bccac-artifact_hub-1024x684.jpg)
Searching for the latest Argo templates, [Backstage plugins](https://thenewstack.io/demo-self-service-kubernetes-with-rafays-backstage-plugins/), Container images, or CoreDNS plugins? How about Falco rules, Headlamp plugins, or Helm charts?

The newly-launched Artifact Hub has everything you need — and much more! — for building out your own cloud native computing system.

It can even be used to plan out a system you are trying to build, but are unsure if integration tools will support the architecture.

[Artifact Hub](https://artifacthub.io) can be a great resource for cloud native system builders, said [Chris Aniszczyk](https://www.aniszczyk.org/), chief technology officer for the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention), in an interview with TNS.
“For example, let’s say you’re a [MySQL shop](https://thenewstack.io/a-cheat-sheet-to-database-access-control-mysql/). You could immediately go to Artifact Hub and search ‘MySQL’ and get a quick list of MySQL support across the CNCF affiliate ecosystem,” he said.

“It makes it very, very easy for you to search and find these things to help investigate if the project works for you,” Aniszczyk said.

## Where Artifact Hub Came From
The project [grew out](https://www.cncf.io/blog/2024/09/17/artifact-hub-becomes-a-cncf-incubating-project/) of the [Helm Hub](https://helm.sh/blog/intro-helm-hub/) and the mission of indexing all the different Help charts, and now includes 26 types of artifacts covering over 15,000 packages from CNCF and [Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) projects used in the cloud native ecosystem.

“There were other projects in CNCF that had packages or things like plugins that they wanted to list and make searchable,” Aniszczyk explained. “And instead of every project having its own registry, the idea was to have it all in one place.”

Last week, the CNCF accepted the hub, with its newly expanded mission, as an [incubating project](https://github.com/cncf/toc/blob/main/.github/ISSUE_TEMPLATE/template-incubation-application.md), giving the maintainers all the backing of any [CNCF project](https://landscape.cncf.io/?_gl=1*qh8l3w*_gcl_au*MjQyMDg5NDI3LjE3MjMwODU3NDY.*_ga*NTM4NTI4MDkzLjE3MjMwODU3NDU.*_ga_VWZ4V8CGRF*MTcyNzExMzA5NS41LjAuMTcyNzExMzA5NS4wLjAuMA..). It is a group of 41 community volunteers, at latest count, including engineers from CNCF and [SUSE](https://thenewstack.io/suse-combines-stackstate-rancher-for-kubernetes-observability/), keep the project running.

The hub itself has no downloads, but instead just lists and indexes the artifacts, with links back to the project source. They can be searched, with filters, or browsed. Only CNCF maintainers, or verified maintainers working with these projects, can post new content, and the maintainers manage the pages.

## Data the Hub Contains
The web serves as an index for finding cloud native packages and configurations, which would otherwise be difficult to locate with general-purpose search engines or on the originating sites. Each entry includes a description, installation instructions, related projects, a list of maintainers, configuration options with default values and security alerts.

And thanks to [Prometheus](https://thenewstack.io/creating-a-path-for-prometheus-success/) (naturally), the site also features a robust page of [user statistics](https://artifacthub.io/stats). There we learned that about 700,000 visitors have taken a look at packages on the hub each month. It also includes stats on registered users and organizations, registered repositories, totals of packages and package releases.

The code for the site is also [available on GitHub](https://github.com/artifacthub/hub), where it has gathered over 1,600 stars.

Besides those mentioned above. other artifacts you’ll find at the hub:

- Inspektor gadgets
- KCL modules
- KEDA scalers
- Keptn integrations
- Knative client plugins
- Kubectl plugins
- KubeArmor policies
- Kubewarden policies
- Kyverno policies
- Meshery designs
- OLM operators
- OPA and Gatekeeper policies
- OpenCost plugins
- Tekton packages
- Tinkerbell actions
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)