# Codefresh and Octopus: GitOps, K8s and VMs Under One Roof
![Featued image for: Codefresh and Octopus: GitOps, K8s and VMs Under One Roof](https://cdn.thenewstack.io/media/2024/03/4460a067-serena-repice-lentini-igomdftkf-u-unsplash-1-1024x683.jpg)
The recent Codefresh and
[Octopus Deploy](https://octopus.com/?utm_content=inline-mention) [merger](https://octopus.com/blog/octopus-acquires-codefresh) is much more than just about [Kubernetes](https://thenewstack.io/kubernetes/). Yes, the merged entity between Codefresh and Octopus will go a long way in unifying the deployments of cloud native architectures, particularly for large enterprises.
But it also will solve a huge problem: how to manage the heritage architectures that large companies have to accommodate in addition to Kubernetes when deploying and offering services. This is how the merger is intended to solve a significant problem for those organizations that need
[GitOps](https://thenewstack.io/how-enterprises-can-benefit-from-gitops/) ( [Argo CD](https://thenewstack.io/why-argo-cd-is-the-lifeline-of-gitops/)) and Kubernetes and have a lot of existing VMs to manage.
“The ‘greenfield assumption’ has broken and is still breaking a lot of advanced DevOps software implementations by failing to accommodate the complexities of real-life environments,”
[Torsten Volk](https://www.linkedin.com/in/torstenvolk), an analyst for [ Enterprise Management Associates (EMA)](https://www.enterprisemanagement.com/), told The New Stack. “The vast majority of enterprises still have, and will have for many years, messy and heterogeneous environments that somehow need to be made part of CI/CD and GitOps.”
Ironically, this thinking around concerns about existing infrastructure was infrastructure as a service provider
[Puppet](https://thenewstack.io/5-myths-about-puppet/)’s original argument in 2016 when Kubernetes began to see more adoption, and organizations started expressing more concern about the relevance of configuration-management tools, Volk said. Puppet’s thinking then was that CI/CD and GitOps should be independent of the underlying application infrastructure and offer one consistent path to production, Volk said.
“It turns out Puppet was right,” he said.
## Managing Scale
Organizations needing to accommodate mostly VMs and Kubernetes clusters when tasked with managing at scale for 5,000 target and heterogeneous environments, is a key issue that Codefresh and Octopus can solve jointly,
[Dan Garfield,](https://www.linkedin.com/in/dan-garfield/) co-founder and chief open source officer of [ Codefresh,](https://thenewstack.io/codefresh-goes-open-core-with-argo-previews-open-gitops-1-0-release/) an enterprise project built on Argo CD, told The New Stack.
While Codefresh can help solve this problem from a GitOps angle, “it’s actually something that Octopus has worked on from a traditional CD angle, too,” Garfield said.
“Codefresh has been selling Kubernetes to all of these large enterprises and telecoms, gaming, media, defense, banking and healthcare companies,” Garfield said.”But if you look at their workloads, they’re all doing Kubernetes, and they’re doing Kubernetes for 10% of what they run — and 90% of what they run is not that, which they’ve been running for 20 years.”
In an
[article in The New Stack](https://thenewstack.io/how-far-can-you-go-with-argo/), [Nikita Dergilev,](https://nz.linkedin.com/in/ndergilev) senior product manager at Octopus, shared this sentiment. In his view, Argo CD is great for cluster “bootstrapping and it’s easy to configure, and the first deployment will take a little time,” Dergilev said.
“However, he sees an issue with using Argo CD when teams need to deploy apps across many environments or clusters, such as cloud regions,” he said. “The pain comes from the need to manage many
[git](https://thenewstack.io/git-at-15-how-git-changed-the-way-we-code/) repositories, branches or folders and to orchestrate promotions with in-house scripts or manually. It can quickly become a mess.”
## Investing in Argo
Not to say that Octopus has not had a successful Kubernetes product. However, Octopus was seeing more customers adopting Argo.
“For Octopus, the merger was strategic in the sense that they really wanted the technology and the expertise that we had. And so they came in and said, ‘We want to acquire all of you, and we’re not going to bring in and lay a bunch of people off and not going to strip mine the product,” Garfield said.
“Octopus wants Codefresh to keep developing what we’re doing and to keep investing in Argo and they really want to accelerate what we’ve been doing. And what’s interesting is that in this stage of DevOps right now, we’re starting to solve some of the problems that have been in some ways solved in heritage deployments like VMs, where Octopus actually has a lot of expertise.”
Prior to the merger, Codefresh had also developed more than just Kubernetes support as well. The “accepted path” to using Argo CD for heritage infrastructure is via controllers that track state in
[etcd](https://etcd.io/) such as Crossplane, Garfield said. “We’re definitely interested in improving those experiences. To note, GitOps is not a Kubernetes standard, it’s a software delivery standard. It all comes down to how you manage state and desired state.”
Indeed, Volk said he “absolutely believes” that the Argo contributors and the ability to deploy to VMs were a significant draw for Octopus to make the acquisition. “They have every reason to keep the Argo contributors happy, as they are key to sustainably offering one consistent DevOps pipeline and GitOps approach across containers and VMs,” Volk said.
## Build Whatever They Wish
Nevertheless, Codefresh has not focused on VMs, either. “While sometimes people might use us for VMs, they didn’t really show up to us for that, but with Octopus, they were already serving all of those companies using VMs, especially those with heritage applications and VMs,” Garfield said. “So now we can bring them all a solution by building it all into a single experience. We’re going to have an approach where we unify software delivery, for heritage and cloud native applications and we think that’ll be really, really powerful.”
In the realm of software delivery, organizations might typically build “whatever they wish,” by using a
[Jira](https://thenewstack.io/open-source-jira-alternative-plane-lands/) tracker, employing any monitoring tool and looking to develop continuous delivery, Garfield noted. They seek simplicity, reliability, predictability and resilience. The aim is to minimize time expenditure as much as possible, addressing the pain points inherent in the process.
In that sense, an alternative to piecing together different tools and options and developing processes internally is on offer.
“You know who our competition is? It’s shadow DevOps: piles of scripts and people hand rolling deployments,” Garfield said. “That’s our market.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)