Did Kubernetes break up [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) cloud party?

As the co-founder and CTO of cloud native hardware company [Oxide Computer Company](https://oxide.computer/), [Bryan Cantrill](https://www.linkedin.com/in/bryan-cantrill-b6a1/) isn’t one to shy away from speaking his mind. In a recent wide-ranging interview on the  [Pragmatic Engineer](https://www.youtube.com/@pragmaticengineer) podcast, hosted by [Gergely Orosz](https://www.linkedin.com/in/gergelyorosz/),  he offered a perspective on how the release of Kubernetes was essential for fueling the growth of the [Google Cloud Platform](https://cloud.google.com/?utm_content=inline+mention) and other nascent cloud providers, when AWS was relentlessly dominating the market.

“I think that part of that initial attraction to Kubernetes is that people wanted to get some optionality around their cloud and they felt locked into AWS,” he said.

“There was a period of time when I felt like in order to be in the cloud, you had to implement every AWS API. It was thought that Google and Azure could never compete with AWS because they could never be API compatible.”

Cantrill has had a knack at being at the right place at the right time. After graduating from Brown University in 1996, he took a job with [Sun Microsystems](https://thenewstack.io/sun-microsystems-a-look-back-at-a-tech-company-ahead-of-its-time/), which was then the place that companies needed to buy servers from to get on the Internet. There, he helped create [DTrace](https://thenewstack.io/oxide-computings-bryan-cantrill-on-the-importance-of-toolmaking/), a powerful observability tool, originally for Sun’s Solaris operating system, a [Unix variant.](https://thenewstack.io/unix-opensolaris-lives-on-in-this-openindiana-fork/)

When Oracle bought Sun Microsystems, [completing the purchase in 2010](https://www.eweek.com/enterprise-apps/oracle-completes-sun-acquisition/), Cantrill, like many Sun techies, fled shortly after. He became the CTO of [Joyent](https://thenewstack.io/joyent-makes-a-case-for-simplicity-not-openstack-complexity/), a cloud service that was marketed as a engineer-savvy alternative service to the bigger clouds. Cantrill went on to found Oxide, which sells servers to run internal cloud services.

## The AWS Juggernaut

From 2010 to 2014, led by [Andy Jassy](https://thenewstack.io/amazon-web-services-wants-you-to-migrate-off-legacy-databases/), AWS was going through a period of “relentless execution,” Cantrill recalled.

In 2010 the company was still seen as emerging, a “visionary” by Gartner. But by 2014 — the first year Amazon broke out AWS sales in its earnings report —  the company brought in [$4.6 billion](https://www.sec.gov/Archives/edgar/data/1018724/000101872415000006/amzn-20141231x10k.htm) in [revenue](https://www.vox.com/2015/4/23/11561822/amazon-reveals-aws-is-a-nearly-5-billion-business-and-is-profitable), and had about five times the capacity as all the other cloud providers [that Gartner tracked](https://virtualizationreview.com/blogs/the-schwartz-cloud-report/2014/06/gartner-iaas-report.aspx).

It seemed unbeatable. Each year at the [AWS Re:Invent](https://aws.amazon.com/blogs/aws/top-announcements-of-aws-reinvent-2025/) user conference, they company announced price cuts, and a staggering number of new services. Vendors out on the show floor would suddenly find themselves competing with some new service AWS just announced (and, legend has it, even some that packed their booths and left mid-conference).

“If you were a competitor to AWS you were dreading Re:Invent because here comes another price cut. If you are a partner of AWS, you’re dreading Re:Invent because here comes the announcement of a new service that competes with what you’re making,” Cantrill recalled.

Financial reporters will remember that, in its quarterly filings before 2014, Amazon did not break out its earnings specifically for AWS. Typically, companies obfuscate these numbers to hide weak performance. AWS was actually doing the opposite,  Cantril believes. It was hiding its cloud revenue because it was so good, and reinvesting back into the retail side of the business.

Joyent was competing with AWS in offering a public cloud at that time, and so the company saw how lucrative the business could be.

“We ran a public cloud and we knew the economics of a public cloud. The margins were good.”

In fact, several of Joyent’s most prominent customers were retailers in direct competition with Amazon, [such as Walmart](https://www.tritondatacenter.com/blog/nodejs-at-joyent), and presumably not interested in using a competitor’s cloud service.

“Retailers are like, “If you think I’m going to take my dollars and spend them on AWS so Amazon can go to war with me, [then] no thank you,” Cantrill surmised.

## The Power of Running Clouds In-House

The idea of a company, such as a Fortune 500 organization, building its own “private” cloud in-house seemed like an attractive alternative to many, especially as the customers saw their [AWS bills grow](https://thenewstack.io/the-great-aws-outage-the-11-billion-argument-for-kubernetes/).

Joyent had open source software for running a cloud, namely the [SmartOS](https://www.datacenterknowledge.com/open-source-software/joyent-open-sources-smartos-for-the-cloud), a variant of OpenSolaris, that allowed businesses to cobble their own cloud system using commodity hardware. Samsung [purchased](https://news.samsung.com/global/samsung-to-acquire-joyent-a-leading-public-and-private-cloud-provider) the company in 2016, purely to power its own cloud operations, Cantrill said.

It may have been a savvy move for Samsung, though the purchase left other businesses with one fewer option for taking charge of their own clouds.

Other options at the time included [Mesosphere](https://www.datacenterknowledge.com/cloud/mesosphere-kubernetes-to-meld-into-google-s-cloud) and [Docker Swarm](https://www.msn.com/en-us/news/technology/kubernetes-may-be-the-better-choice-but-docker-swarm-makes-more-sense-for-home-labs). Many thought the best way to compete with AWS was to replicate AWS’s own APIs. This was done in an open source project called [Eucalyptus](https://www.eucalyptus.cloud/), which was [purchased by HP in 2014](https://www.datacenterknowledge.com/cloud/hp-buys-aws-compatible-cloud-builder-eucalyptus).

## Enter Kubernetes

In this discussion with Orosz, Cantrill makes the argument that it was actually the [introduction of Kubernetes](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/) container orchestration engine in 2014 that democratized the cloud market, even if it wasn’t that widely used at first (It’s now the second largest opens ource project after Linux).

At the time, Google offered its cloud services, but internally, they were tied to the specific bits of hardware. Kubernetes came about as a project to implement “cluster-based scalable network services,” according to [one of the original papers](https://people.eecs.berkeley.edu/~brewer/cs262b/TACC.pdf) describing the technology. The emergence of [Docker at that time](https://thenewstack.io/docker-at-10-3-things-we-got-right-3-things-we-got-wrong/) allowed of giving each workload its own IP address, thanks to [containers](https://thenewstack.io/containers/).

The promise of Kubernetes is that it [provides the ability to provision basic infrastructure](https://thenewstack.io/docker-versus-kubernetes-start-here/), but not be tied to a specific hardware platform itself. No longer would you need to write to the AWS APIs. Applications could be built to the Kubernetes APIs and, in theory, be able to run on any cloud provider, achieving a form of operational cloud neutrality.

“Multi-cloud didn’t really exist, I’d argue, before Kubernetes,” Cantrill said. Indeed, many of the early contributors to the project were motivated by [this ideal of cloud neutrality](https://thenewstack.io/why-open-platforms-are-the-future-of-kubernetes-deployments/).

## Why Did Kubernetes Open Source Kubernetes?

Why Google open sourced Kubernetes, which was an offshoot of its internal [Borg platform](https://thenewstack.io/10-years-of-kubernetes-past-present-and-future/), in the first place remains a bit of a mystery.

Of course, [there are benefits](https://youtu.be/vBjonut1JMk?t=994) that come with open sourcing any project, such as more contributions to the code base and security.

But releasing an open source project to encourage cloud neutrality also made competitive sense, at least from Google’s P.O.V.

“I think that the argument that people were making internally was about encouraging cloud neutrality because ‘We are the ones that have something to win,'” Cantrill said.

Google even gave the [Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) seed money to launch the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) in 2015 [to independently manage](https://www.cncf.io/announcements/2015/06/21/new-cloud-native-computing-foundation-to-drive-alignment-among-container-technologies) Kubernetes and related open source technologies.

Nonetheless, the Google Cloud Platform has since found its footing in the marketplace. GCP alone now [brings in about $60 billion](https://seekingalpha.com/article/4823341-alphabets-next-growth-cycle) in revenue to Alphabet annually.

AWS is still the top provider, with about a [30% share of the cloud marketplace](https://holori.com/cloud-market-share-2026-top-cloud-vendors-in-2026), though the marketplace itself has ballooned in size to be a [trillion-dollar market today](https://www.visualcapitalist.com/the-worlds-largest-cloud-providers-ranked-by-market-share/), with a wider variety of participants that have gained market share.

“Is Kubernetes to thank solely? No, but I think it’s played an important role for sure,” Cantrill said.

Enjoy the entire talk here:

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)
[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)