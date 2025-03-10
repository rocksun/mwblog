# Transferring Trillions of Dollars Daily Using Kubernetes With No Internet
![Featued image for: Transferring Trillions of Dollars Daily Using Kubernetes With No Internet](https://cdn.thenewstack.io/media/2025/03/6aa585bc-disconnected-kubernetes-swift-1024x576.jpg)
There are plenty of [architectural diagrams](https://roadmap.sh/software-design-architecture) out there describing [cloud-based architectures](https://thenewstack.io/3-key-practices-for-perfecting-cloud-native-architecture/) deployed in traditional enterprises. But what if you operate financial market infrastructure that processes transactions that are worth trillions of dollars every day? How do you securely manage and operate an environment at scale with almost no internet access? What if the users inside the cluster can’t access that cluster’s underlying infrastructure in any way, save through the application they’re using? And what if that architecture still has to be completely up to date and patched to keep up with potential security threats?

It’s a complex challenge, especially considering the clusters can’t be connected to the internet. And yet, these are the very constraints that [Swift](https://www.swift.com/) is designed to handle. When one bank transfers funds to another, the transaction is communicated through the Swift network. Banks hold accounts with each other and adjust balances as needed based on transaction requests.

Those requests are SWIFT messages, which remain entirely separate from the internet. So, how do you manage a fleet of clusters in a highly secure offline environment?

## No Touch
Swift’s container platform product owner [Otmane Benali](https://www.linkedin.com/in/obenali/) said that his teams deploy hundreds of Kubernetes clusters around the world, fully disconnected from the internet using GitOps. He described the architecture in his November 2024 [talk](https://www.youtube.com/watch?v=wI6pmgznbd8) at [OpenShift Commons](https://commons.openshift.org/), before KubeCon North America.

“We are operating in a disconnected environment, meaning that users do not have access to the internet. We have only two hosts with internet access: our [Red Hat Enterprise Linux](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) (RHEL) host and the Nexus container registry. On the RHEL host, we run a utility called oc-mirror from Red Hat to download the images. These images are then stored in a local container registry,” explained Benali.

“The list of images” said Benali, “is uploaded into git. [When we have a new OpenShift release or operator], we test them in the lab environment, and once we’re satisfied, we promote it to development, Q/A and then production. Before promoting it, we do use Red Hat Advanced Cluster Security for Kubernetes to scan the image and [Podman](https://thenewstack.io/use-podman-to-create-and-work-with-virtual-machines/)’s signing for authenticity, and then Skopeo to copy the images.”

Swift’s senior enterprise architect [Praveen Siddu](https://www.linkedin.com/in/praveen-siddu-741b9724/) said, “Once the image has been promoted, we don’t stop there. We want to make sure that the images are downloaded and cached in all the geographical locations for that particular environment so that the image is already available in the container registry before it’s used by a pod. The cache image list is uploaded to an object store. The object store is centralized so that we have a clear view of all the environments and we are sure that the images have already been promoted to that environment before we actually start using them.”

## Multicountry, Multicluster
That means there’s a major impetus to keep things secure and up to date, even without internet access. Swift accomplishes this by using git as its source of truth and managing [Kubernetes](https://thenewstack.io/kubernetes/) cluster deployment in a centralized, replicable manner.

“We use a [GitOps model](https://www.redhat.com/en/topics/devops/what-is-gitops), and we use [Red Hat Advanced Cluster Management for Kubernetes](https://www.redhat.com/en/technologies/management/advanced-cluster-management) to have faster cluster builds,” said Benali. “We also introduced fleet management to manage clusters at scale and keep them consistent on the same version. Zero-privilege implementation helped us to meet our regulation requirements, as well as our security requirements. And finally, we have achieved significant cost savings, and we have improved time to market by several factors.”

Siddu expanded on the multicluster architecture used at Swift. He said the teams have Hub and App clusters. “All of them are Red Hat OpenShift clusters. The only difference between Hub cluster and App cluster is App clusters run application workloads; Hub clusters just run Red Hat Advanced Cluster Management and Red Hat GitOps,” said Siddu. “Red Hat Advanced Cluster Management is a very flexible tool. It provides us the ability to build multiple clusters at the same time, because each of those runs in its own namespace, and it’s containerized.”

With git as the source of truth behind all of these cluster builds, Siddu said in the end, only [Argo CD](https://argo-cd.readthedocs.io/en/stable/) can make changes to clusters; no manual updates are made to any cluster.

“If Argo is the only entity making changes to the cluster,” said Siddu, “that means if we have to upgrade one cluster, if we have to upgrade 10 clusters, it’s the same effort, right? Because all we have to do is push the configuration to git. Our work stops as soon as we push the new updates to the git repository; Argo CD does the rest of deploying.”

Swift has been able to cut cluster deploy and test time down to under 90 minutes per cluster.

This includes some built-in safeguards. “One of the safeguards,” said Siddu, “is all of the clusters that are already in this new release must be in a healthy state. If any one of them is not in a healthy state, [the rollout] just stops. And then, if everything is in a healthy state, it moves on to the next cluster, prepares the configuration for it, and Argo CD does the rest of applying it to target clusters. Once that is done, it just gives it some soak period for the cluster to settle and continues with the next.”

All of this work allows Swift to navigate the difficult security and regulatory requirements it faces every day. Having a clear system for tracking who did what, where and when is essential.

“The list of who performed which action on which cluster and when,” said Siddu, “is actually retrieved by another deployment running in the same namespace, and then it’s uploaded to the object store. So, we have clear tracking of who executed which operation on which cluster.”

Benali said this enables the Swift team to deploy hundreds of Kubernetes clusters around the world, quickly and through Swift’s fleet management system. They’re also able to control when upgrades and updates occur so they don’t accidentally spread an unexpected bug. It’s enabled Swift to decrease costs and improve developer velocity while also keeping its customers’ transactions safe and secure.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)