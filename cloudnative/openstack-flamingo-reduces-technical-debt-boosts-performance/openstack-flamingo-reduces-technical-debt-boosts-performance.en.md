The oldest open source Infrastructure as a Service (IaaS) cloud just celebrated its latest birthday with a new release.

[Flamingo](https://releases.openstack.org/flamingo/index.html), the latest version of [OpenStack](https://www.openstack.org/), comes with significant technical debt reduction and expanded enterprise features.

The release — the 32nd major update — is marked by substantial improvements in concurrency, security, hardware support and a more flexible release cadence, solidifying its role in large-scale deployments, whether you want the latest and greatest features or slower, more stable releases.

Flamingo is the result of the work of 480 contributors representing organizations including BBC R&D, Ericsson, NVIDIA, Rackspace, [Red Hat](https://www.openshift.com/try?utm_content=inline+mention), Samsung SDS, [SAP](https://www.sap.com/index.html?utm_content=inline+mention) and Walmart, integrating almost 8,000 code changes.

Flamingo arrives with OpenStack powering over 55 million compute cores in production environments globally. It’s a long way from how the project began.

## The Origin Story of OpenStack

In 2008, people were still dismissing the cloud as just someone else’s computer. Top tech executives like [Larry Ellison](https://x.com/larryellison), [Oracle’s](https://www.oracle.com/developer?utm_content=inline+mention) CEO, [dismissed cloud computing as simply the latest fashion](https://www.cnet.com/culture/oracles-ellison-nails-cloud-computing/).

Everyone eventually got the message that the cloud was a fundamentally different paradigm, but some people were ahead of the game. One such group included developers at [NASA Ames Research Center](https://www.nasa.gov/ames), [Rackspace](https://www.rackspace.com/) and [Anso Labs](https://ansolabs.com/), who together built the open source IaaS cloud, [OpenStack](https://www.openstack.org/).

It wasn’t the first cloud. Contenders for that honor include the [Amazon Elastic Compute Cloud](https://cc.zdnet.com/v1/otc/00hQi47eqnEWQ6T9d4QLBUc?element=BODY&element_label=Amazon+Elastic+Compute+Cloud&module=LINK&object_type=text-link&object_uuid=55639666-1d6c-4c2f-a8ab-e45d1ac00050&position=1&template=article&track_code=__COM_CLICK_ID__&url=https%3A%2F%2Faws.amazon.com%2Fec2%2F%3Ftag%3Dzd-buy-button-20%26ascsubtag%3D__COM_CLICK_ID__%257C257d03ef-f92f-4d4a-a542-de541967a0d2%257Cdtp&view_instance_uuid=d9ee8763-ebe0-4a07-a14c-02a9b2815eb5), an ancestor of [Amazon Web Services (AWS)](https://aws.amazon.com/?utm_content=inline+mention), and [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure. Although they were built on [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) and other open source programs, they were proprietary platforms.

In 2010, the Ames team wanted NASA to host and manage its own computing and data resources, and created Nebula, an early IaaS cloud. But, as [Brian Gracely](https://www.linkedin.com/in/briangracely), then Red Hat’s senior director of product strategy, [said in a 2020 post on NASA’s blog](https://www.nasa.gov/technology/tech-transfer-spinoffs/in-cloud-computing-open-source-becomes-big-business/), “NASA didn’t have the staff to build the whole thing and maintain it long-term.”

So, the Ames team went the open source route, and in doing so, helped lay the groundwork for OpenStack. The first major building block, [Nova](https://docs.openstack.org/nova/latest/#:~:text=Nova%20is%20the%20OpenStack%20project,limited%20support%20for%20system%20containers.&text=Keystone%3A%20This%20provides%20identity%20and%20authentication%20for%20all%20OpenStack%20services.), is still part of OpenStack today. At the time, though, as one developer put it, “It’s live, it’s buggy, it’s beta. Check it out.”

Simultaneously, [Jonathan Bryce](https://www.linkedin.com/in/jbryce/), co-founder of Rackspace, and his crew were working on their own open source cloud project. Then, Bryce told me, “We met these folks at NASA, and that went really well. So, we flew out to [Ames’ main campus] Moffett Field and spent a whole day with them.

“The whole time, everybody was just sitting there nodding because we were rebuilding our stuff in Python. They were using Python. We picked the Apache 2 license. They picked the Apache 2 license. So, we were, ‘Yes, we have to join forces!'”

## A New Approach To Open Source Collaboration

And they did. The first OpenStack release, Austin, appeared in 2010. Besides creating OpenStack, this would be the first time government-funded software had been released under an open source license.

It was “a bit different than how open source had been approached,” recalled Bryce, who was [named executive director](https://thenewstack.io/linux-foundation-appoints-jonathan-bryce-to-lead-cncf/) of the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention) in June.

“For the most part, open source projects were a collaboration among people who were trying to scratch their own itch or open core projects where a single company built an open source project heart, but all the extras were proprietary, and they owned the entire monetization process.”

With OpenStack, he said, “We wanted open source software to be a key enabler of not just our business, but everyone’s business. So from the beginning, we were really interested in having a big ecosystem of folks coming together to build it all.”

## How OpenStack Became a Cloud Computing Powerhouse

From its very first days, OpenStack had many companies investing in it and sharing the open source wealth. Early members, who are still with it today, include [Dell](https://www.delltechnologies.com/en-us/index.htm?utm_content=inline+mention), [Cisco](http://cisco.com/?utm_content=inline+mention), [Mirantis](https://www.mirantis.com/resources/mirantis-ai-factory-reference-architecture/?utm_source=content-syndication&utm_medium=the-new-stack&utm_campaign=2026q2-whitepaper-building-ai-factories-with-mirantis-k0rdent-ai&utm_content=newsletter&utm_content=inline-mention), and Red Hat. Today, OpenStack has thousands of contributors from more than 500 companies.

Within a few years, OpenStack’s popularity exploded. HP, [IBM](http://www.ibm.com/products/webmethods-hybrid-integration?utm_content=inline+mention), Red Hat, [VMware](https://tanzu.vmware.com?utm_content=inline+mention) and many other tech powers threw their support behind OpenStack.

“A couple of things came together,” said [Jim Curry](https://www.linkedin.com/in/jimncurry/), then Rackspace’s senior vice president of strategy and corporate development. “First, cloud technology and its form factor were hitting an inflection point. After several years, Amazon Web Services was just moving into the mainstream, and people were looking not just for an open source alternative, but for any AWS alternative.”

It was more than that, Bryce said: “We had laid the groundwork, built the community and gotten the software to a point where its market ecosystem really started to go crazy.” It was being used for almost everything you could use a cloud for.

To better manage the growing projects, its corporate backers and developers formed the [OpenStack Foundation](https://www.openstack.org/) in September 2012. This was a nonprofit corporate entity to promote and manage OpenStack software and its community.

Then, Bryce continued, “One of the most interesting and kind of unexpected technology turns happened. The telecom industry really started to engage with OpenStack. When we started OpenStack, we were thinking about data center software for distributed storage.”

However, starting in 2014, [software-defined networks (SDNs)](https://thenewstack.io/defining-software-defined-networking-part-1/) and [network functions virtualization (NFV](https://thenewstack.io/de-ossify-the-network-with-function-virtualization/)) began to run as the backbones of cellular networks.

OpenStack has become the default telecom cloud. Companies such as Verizon, AT&T, China Mobile and Deutsche Telekom have built their 5G infrastructure and SDNs to replace older 4G systems.

At the same time, OpenStack was being used in what its creators had first dreamed up for it. As Bryce put it, “Everything from airlines, automobile manufacturers, financial services, government agencies and private, hybrid and public clouds are using OpenStack.”

For example, in Europe, OpenStack is used as the foundation for public clouds. These include hyperscale clouds from [Deutsche Telekom/T-Systems](https://www.t-systems.com/us/en), [Cleura Public Cloud](https://cleura.com/) and [OVH Public Cloud](https://us.ovhcloud.com/public-cloud/). Then, there are unusual public clouds. One example: [OneQuode](https://www.oneqode.com/), a Pacific Ocean-based cloud provider that specializes in delivering low-latency and high-speed gaming to customers from Korea to San Francisco and the islands in between.

## OpenStack and the Linux Foundation Join Forces

In recent years, OpenStack has also been quietly growing in private clouds. For example, Korean automaker Hyundai uses OpenStack for its private cloud, [hCloud](https://www.hyundai.co.kr/story/CONT0000000000159670).

“[There are several reasons why we are using OpenStack](https://www.zdnet.com/article/why-openstack-and-kata-containers-are-both-seeing-a-resurgence-of-adoption/),” Younghold Han, Hyundai’s vice president of car cloud, told me. “First, there’s data security. We want to control our security.

“And finally, there’s cost. So before Hyundai, I worked in Samsung’s mobile business unit. We launched multiple services for our users that ran on AWS, and you cannot imagine how the costs grew exponentially. So we built out our private cloud.”

Besides this, OpenStack users kept exploring new use cases. For example, Bryce said, “[TensorFlow](https://www.tensorflow.org/?utm_source=the%20new%20stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns%20platform) came along, and now OpenStack is used for AI and machine learning [ML]. And it’s also being used for transcoding video at the edge, so people can watch 4K videos on their phones. Innovation never stops.”

Additionally, other significant projects have emerged from OpenStack. These include [Airship](https://wiki.openstack.org/wiki/Airship), a cloud-provisioning system; [Kata Containers](https://katacontainers.io/), lightweight, container-like virtual machines (VMs); [StarlingX](https://www.starlingx.io/), an edge cloud stack; and [Zuul](https://zuul-ci.org/docs/zuul/), a [CI/CD](https://thenewstack.io/introduction-to-ci-cd/) program. Thanks to these projects, starting in 2021, the [OpenInfra Foundation](https://openinfra.org/) evolved from the OpenStack Foundation to reflect a broader mission beyond just OpenStack.

Recently, however, the OpenStack community took one more step. In March, the [OpenInfra Foundation united](https://thenewstack.io/open-infrastructure-foundation-joins-forces-with-linux-foundation/) with the [Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention). [Jim Zemlin](https://www.linkedin.com/in/zemlin), the Linux Foundation’s executive director, summed up the logic for this move in his keynote at his organization’s member summit that month: “OpenInfra and our cloud projects are kind of like peanut butter and chocolate.”

Bryce, who still heads the OpenInfra Foundation as well as his new role at CNCF, said in his keynote at that March event, “We’re expanding our overall reach, and we’re going to be able to take open source more places.”

The future looks bright for OpenStack and its new friends.

## What’s New in the OpenStack Flamingo Release?

The Flamingo release’s headline achievement is the large-scale removal of [Eventlet](https://pypi.org/project/eventlet/), a Python concurrency library that has been at the foundation of OpenStack for almost 18 years. This migration to modern Python async frameworks was completed in such OpenStack modules as Barbican, Heat, Ironicand Mistral. Progress has also been made in removing it from Nova and Neutron.

These changes will reduce persistent operational problems and technical debt. Eventlet will eventually be entirely removed from OpenStack. The result will be improved performance, scalability and sustainability for this release and the ones that follow.

“This progress in Eventlet migration has strengthened OpenStack for the long run,” said [Goutham Pacha Ravi](https://www.linkedin.com/in/gouthampacha), chair of the OpenStack Technical Committee, in a statement. The transition means faster and more reliable bare-metal provisioning, improved concurrency and lower risk of unexpected side effects from outdated code dependencies.

Moreover, Flamingo continues OpenStack’s move into confidential computing and reinforces access control. [Key Flamingo upgrades](https://tfir.io/openstack-flamingo-release-accelerates-enterprise-cloud-capabilities/) include:

* Nova gains support for one-time-use passthrough devices and AMD SEV-ES secure enclave support.
* Magnum enables credential rotation for Kubernetes clusters — a critical security feature for cloud native deployments.
* Manila supports bring-your-own encryption keys for file servers.
* Horizon introduces QR code onboarding for two-factor authentication, streamlining secure cloud operations.

These enhancements are designed to support modern workloads, such as AI, ML and high-performance computing, while bolstering privacy and data protection for enterprises.

## Introducing OpenStack’s New Release Schedule

With Flamingo, [OpenStack is introducing a “non-Skip Level Upgrade Release Process (SLURP)”](https://docs.openstack.org/project-team-guide/release-cadence-adjustment.html) six-month release. For some time now, there’s been a dispute between OpenStack users who preferred fast, every-six-month releases and others who wanted a year or even longer cadence between releases.

In this compromise, every other release will be considered to be a SLURP release. Upgrades will be supported between SLURP releases, in addition to between adjacent major releases, as they are now.

Companies wanting to stay on the six-month cycle will deploy every SLURP and “not-SLURP” release as always. Businesses wishing to move to a one-year upgrade cycle will synchronize on a SLURP release, and then skip the following “not-SLURP” release, and only upgrade when the subsequent SLURP is released.

Got all that? The next SLURP release, OpenStack 2026.1 “Gazpacho,” is scheduled for April.

In the meantime, we’ll soon see what users make of Flamingo. I suspect that thanks to its modernization of Python async frameworks, it will be the most popular OpenStack release to date.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)