Organizations looking to scale their AI workloads and infrastructure on Kubernetes were largely limited to expensive hyperscaler options. As DevOps and platform engineering teams learn how to properly adopt AI infrastructure for cloud-native deployments, a range of choices is emerging beyond what the major cloud providers offer for deploying heavy AI-inference workloads running on Kubernetes.

Cloud costs have skyrocketed, and remaining locked into a cloud provider for the additional costs associated with running AI inference (the most computationally expensive component of AI infrastructure) is what many organizations understandably seek to avoid.

The recent announcement of SUSE Rancher Prime and SUSE AI joining the Vultr Marketplace is more than just a new partnership — it is a blueprint for the next era of independent, open-source, sovereign AI infrastructure, Vultr’s Chief Marketing Officer Kevin Cochrane told me during CloudNativeCon+KubeCon Europe.

“SUSE Rancher aligns with a whole ethos of open communities, open development, and open stacks,” Cochrane said. “You know, we want to have freedom, choice, and flexibility.”

## Open source, open stacks

Vultr offers organizations B200, H100, and MI300X instances across 32 global regions (as of early 2026) with serverless inference capabilities. Specific to the SUSE agreement, Vultr is pushing further toward open source and cloud-native, especially by offering open-source Rancher through SUSE and by offering organizations flexible access to its GPU infrastructure for AI workloads, while again having more independence from hyperscaler vendor lock-in.

The agreement with SUSE for SUSE Rancher extends Vultr’s global edge cloud infrastructure and Rancher Government Solutions’ (RGS) application infrastructure platform for public-sector Kubernetes edge deployments.

It serves as a platform to meet strict data-security and sovereignty requirements while extending cloud capabilities closer to mission sites. Vultr provides GPU-enabled edge cloud for AI and analytics workloads, while RGS enables consistent orchestration and security across edge deployments and on-premises infrastructure.

In the case of the present agreement between SUSE and Vultr, discussed during KubeCon+CloudNativeCon, the emphasis is on offering organizations the opportunity to rely on Vultr and SUSE Rancher to run AI workloads on cloud-native infrastructure. The option is not purely hyperscaler infrastructure, nor is it a pure do-it-yourself setup running open-source Rancher Kubernetes clusters with SUSE support across a private cloud as an alternative.

It sits somewhere in between: for a CTO looking to take advantage of price differences and, arguably, lower vendor lock-in risk, running SUSE Rancher on Vultr’s infrastructure — leveraging its GPU horsepower and other hardware support — can work.

## A “buyer beware” for neo-clouds

Other alternatives to major hyperscalers exist for AI training and inference, of course. However, Cochrane issued a “buyer beware” warning about the limitations of what he described as “neo-clouds”: startups that have raised massive amounts of capital to offer specialized AI hardware and supporting infrastructure.

While they can offer raw GPU power, Cochrane said they can lack key requirements for organizations, such as adherence to compliance, data-sovereignty needs, security, and other constraints that require very sophisticated infrastructure and management on which organizations can rely. He contrasted this “Wild West” environment with Vultr’s strategy of integrating AI hardware into a mature, 14-year-old public cloud stack that has long served as a much less expensive alternative to the major hyperscalers.

> “Enterprises don’t touch them at the end of the day because the CISO gets involved, SecOps gets involved, the network team gets involved… they come with their checklist and there’s not a lot there.”

“I just get shocked sometimes,” Cochrane said. While noting that these “neo-cloud” platforms might attract AI-native startups, he said they are not up to standard. “Enterprises don’t touch them at the end of the day because the CISO gets involved, SecOps gets involved, the network team gets involved… they come with their checklist, and there’s not a lot there,” Cochrane said.

> “The early AI market was dominated by hyperscalers and well-funded AI-native startups. But true enterprise adoption — especially for mission-critical systems — has yet to fully materialize. That shift is now underway, driven by the rise of enterprise inference.”

Platform engineering teams can choose from bare metal, GPUs, and VMs at a quoted price Vultr says is significantly lower than what the hyperscalers offer. SUSE’s Rancher provides cluster management, SUSE AI provides inference and training, and SUSE’s zero-trust security rounds out the stack.

## Enterprise inference drives adoption

“The early AI market was dominated by hyperscalers and well-funded AI-native startups. But true enterprise adoption — especially for mission-critical systems — has yet to fully materialize. That shift is now underway, driven by the rise of enterprise inference,” Cochrane said. “What we’re focused on is helping platform engineering teams define the right infrastructure and developer productivity strategies — taking the principles they’ve already established for cloud-native applications and extending them to a new generation of AI-native apps.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)