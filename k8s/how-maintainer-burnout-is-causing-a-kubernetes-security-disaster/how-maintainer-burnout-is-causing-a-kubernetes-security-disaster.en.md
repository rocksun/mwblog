Like far too many open source projects, we don’t give [Kubernetes External Secrets Operator (ESO)](https://external-secrets.io/) enough attention. We just assume the program will be kept up-to-date and that it will always be there. That’s a big mistake. Recently, one of ESO’s maintainers wrote on Reddit that “the [contributor base hasn’t scaled with the user base](https://www.reddit.com/r/kubernetes/comments/1mp34uk/eso_maintainer_update_we_need_help/). Right now, a very small team of maintainers is responsible for everything.” Indeed, according to [Rasheed Amir](https://www.linkedin.com/in/rasheedwaraich/), CEO of [Stakater](https://www.stakater.com/), a Swedish Kubernetes consulting company, on LinkedIn, “[There’s only one active maintainer left.](https://www.linkedin.com/posts/rasheedwaraich_heads-up-for-kubernetes-users-relying-activity-7361460297049563138-PmqW/)”

In a word, “Ow!”

The result? At the time, the project essentially shut down. There would be no official support: no Slack, no GitHub discussions, and no new versions until at least five active maintainers step up.

This is a big deal. ESO has become a critical utility for securing secrets in Kubernetes environments. ESO is usually one of the very first add-ons deployed to Kubernetes deployments. The [program serves as a bridge to securely sync secrets](https://zesty.co/finops-glossary/external-secrets-operator/) from external providers like [AWS](https://aws.amazon.com/?utm_content=inline+mention) [Secrets Manager](https://aws.amazon.com/secrets-manager/), [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault) and [HashiCorp Vault](https://www.hashicorp.com/en/products/vault) directly into Kubernetes.

[![Diagram](https://cdn.thenewstack.io/media/2025/09/7f55a11f-eso-diagrams-high-level-simple-1.png)](https://cdn.thenewstack.io/media/2025/09/7f55a11f-eso-diagrams-high-level-simple-1.png)

A high-level diagram of how ESO works.

## What Is the Kubernetes External Secrets Operator (ESO)?

When ESO connects to one or more external secret providers, it fetches sensitive data such as credentials, API keys or certificates via secure APIs. It then injects these secrets as native Kubernetes Secret objects so applications can securely access them during runtime. Since Kubernetes’ native secrets are stored in [etcd](https://etcd.io/) and aren’t encrypted, ESO is vital for enabling secrets to live securely in external secret managers with features like audit trails and access controls.

ESO also supports real-time updates and automatic secret rotation. This means if a [secret changes in the external](https://thenewstack.io/securing-kubernetes-with-external-secrets-operator-on-aws/) system, ESO will update it inside Kubernetes automatically.

## The Core Problem: Maintainer Burnout and Lack of Support

How did such an important project end up in such a state? [Gustavo Fernandes de Carvalho](https://github.com/gusfcarvalho), an ESO maintainer, explained on the [ESO GitHub](https://github.com/external-secrets/external-secrets) that the [maintainers “have simply ‘too much to do.’](https://github.com/external-secrets/external-secrets/issues/5084) Our contribution number increases, the support request increases,” while the active community member numbers keep shrinking. Moreover, “our maintaining team is mostly burnt out.” He added, “Our only active maintainer these days is [@Skarlso](https://github.com/Skarlso) (Gergely Brautigam) – which is a bad sign. Last week, when he was on vacation, we had 0 Pull Requests merged, + 20 issues open (most of them support issues).”

This can not continue.

## Project Freeze: The Immediate Consequences for ESO

The remaining team has declared that until they have at least five maintainers, the project is frozen. There will be no new features, bug fixes or security patches. Oh, and as for mentoring “junior people to become maintainers,” they don’t have the [time or the resources to bring them up to speed](https://thenewstack.io/speeding-time-to-value-the-just-in-time-data-analytics-stack/).

Since they first called for help, more than 300 people, de Carvalho reports, have volunteered to help. In addition, “We’ve spoken with the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) , who shared guidance on ensuring long-term project health.”

However, he continued, “While we trust the new maintainers, we can only go back to releasing software when we are confident we have a healthy contribution lifecycle, via this contributor ladder. This means we need to spend time exercising, testing, and adjusting it before we feel confident enough to release it.”

## The Community’s Response and the Path to Recovery

This means there must be six consecutive community meetings with at least five members/reviewers/maintainers in attendance. We have continuous contributors joining our ladder, permanent reviewers elected and permanent maintainers elected.

That’s not going to happen overnight. de Carvalho expects this process could “take at least 6 months. Please, plan accordingly.”

ESO has reached a pivotal moment. Its future depends on the willingness of its user base and the broader Kubernetes community to keep one of the ecosystem’s most critical secrets-management tools alive by addressing this crisis.

## A Warning Sign for the Broader Open Source Ecosystem

It appears they’ll weather this storm. However, ESO is far from the only open source [project facing a lack of support](https://thenewstack.io/12-critical-open-source-projects-losing-security-support-in-2025/). [Maintainer burnout is becoming an all too common problem](https://www.linkedin.com/pulse/when-open-source-breaks-silent-impact-maintainer-burnout-vaughan-xelle/). It must be addressed, or someday soon (and it won’t be long) we’ll see a vital but little-known open source project fall through the support cracks. Businesses will find themselves facing zero-day security problems without any warning or any clue on how to address them.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)