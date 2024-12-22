# What Do You Lose When You Abandon the Cloud?
![Featued image for: What Do You Lose When You Abandon the Cloud?](https://cdn.thenewstack.io/media/2024/12/ec61c850-what-do-you-lose-when-you-abandon-the-cloud-1024x576.jpg)
High-profile moves from [37signals](https://www.linkedin.com/posts/david-heinemeier-hansson-374b18221_our-cloud-exit-savings-will-now-top-ten-million-activity-7252755548859727874-k5V2/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) (the company behind [Basecamp](https://basecamp.com/) and [HEY](https://www.hey.com/)) and [GEICO](https://www.thestack.technology/warren-buffetts-geico-repatriates-work-from-the-cloud-continues-ambitious-infrastructure-overhaul/) have sparked a [renewed interest in](https://thenewstack.io/why-companies-are-ditching-the-cloud-the-rise-of-cloud-repatriation/) cloud repatriation — moving workloads off the public clouds. They’re not the first, of course. [Dropbox](https://www.dropbox.com/enterprise) famously [undertook a similar journey](https://techcrunch.com/2017/09/15/why-dropbox-decided-to-drop-aws-and-build-its-own-infrastructure-and-network/) back in 2016 because they found it more cost-effective. But[ is cloud repatriation a growing trend](https://thenewstack.io/cloud-migration-regrets-should-you-repatriate/)?

[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) would certainly like the Competition and Markets Authority (CMA), the U.K.’s principal competition regulator, to think that it is. At a July hearing, AWS [cited repatriation as a threat to its business](https://assets.publishing.service.gov.uk/media/66e7fa6910f8726dc23aa16a/240702-aws-hearing-summary.pdf) while giving evidence to the CMA’s investigation into whether the big cloud providers like AWS, Microsoft and Google, engage in anti-competitive practices that limit customer choice.
It is easy to be cynical, but [Daniel Saroff](https://www.linkedin.com/in/daniel-saroff-9301991/), group vice president of consulting and research at [IDC](https://www.idc.com/), a market research company, wrote in a company blog post that he [believes there are several factors driving the repatriation process](https://blogs.idc.com/2024/10/28/storm-clouds-ahead-missed-expectations-in-cloud-computing/): cost overruns; performance and latency issues, with technical and AI-related workloads hitting bottlenecks in public cloud environments; and security and compliance concerns, particularly for sectors where data privacy is paramount, such as finance and health care.

While it is easy to imagine repatriation as all or nothing, as was the case for 37signals and Dropbox, the truth is rather more nuanced. In a 2021 report about cloud costs, published by [Andreessen Horowitz](https://a16z.com/), the Silicon Valley venture capital firm, [the authors stated that](https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/), “Of the many companies we spoke with, even the most aggressive take-back-their-workloads ones still retained 10 to 30% or more in the cloud.”

In other words, a lot of what we’re seeing may just be a sign of growing maturity, with organizations making informed decisions about where particular workloads are best placed. But since everything in architecture is a set of trade-offs, which ones should we be weighing before making such a move?

## Does the Cloud Save You Money?
One sometimes overlooked advantage of moving to the cloud is that it allows you to pay for resources when they are needed, for example, as new customers come online. Spending moves from upfront CAPEX (buying new machines in anticipation of success) to OPEX (paying for additional servers on demand).

Moving back to a data center implies the opposite — purchasing machines ahead of time, based on growth projections.

This distinction sometimes gets conflated with the idea that moving to the cloud saves you money, but that isn’t always true. “A lot of the repatriation examples I’ve seen are firms who have lifted and shifted and found it is more expensive, and are now totally disillusioned,” [Anne Currie](https://thenewstack.io/author/annecurrie/), [co-author of “Building Green Software,”](https://thenewstack.io/want-to-create-software-sustainably-anne-curries-got-ideas/) told The New Stack.

As it turns out, it is very easy to spend money in the cloud. Even at a small scale, many of us have received a bill from a public cloud provider for something we’d forgotten was still running; imagine the magnitude with a scale-up. And while many start-ups rely on the ease of acquiring more compute resources by reaching for a credit card, eventually, it is natural to want to [stop giving a large chunk of your profits to a public cloud provider](https://thenewstack.io/finops/).

The thing you need to weigh here, however, is whether you can drive your costs down while keeping the workloads where they are, or if it will be cheaper to run your own infrastructure. Typically, the latter is more likely if you are operating at a considerable scale — there is a reason why firms like eBay, [Google](https://cloud.google.com/?utm_content=inline+mention) and Amazon do so.

For the rest of us, it makes more sense to look at better cost management. A side effect of being in the cloud is that ownership of technological and financial decision-making shifts from procurement to engineering, architecture and product teams. This is part of what allows faster innovation, but as engineers, it also means that the cost of running our systems becomes yet another thing that has [shifted left](https://thenewstack.io/2023-will-be-the-year-finops-shifts-left-toward-engineering/) and become part of our purview.

To manage it effectively, engineers need accurate, ideally real-time information in order to see where the money goes and be able to make informed choices. It’s another example of a tight feedback loop that enables you to adjust work more rapidly.

A recognized way to manage this is to have a centralized [FinOps](https://thenewstack.io/finops-what-is-it-and-why-should-developers-sign-on/) practice that can bring financial accountability to the variable spend model of cloud. This can help individual product teams take advantage of offers from cloud vendors, such as deep discounts for reservations, flat-rate pricing, and volume and contract discounting. Workloads like 37signals’, which have predictable resource needs, may be able to take advantage of [committed use discounts](https://cloud.google.com/docs/cuds) to drive their costs down.

Most cloud providers also provide mechanisms for capping API usage, quotas and budgets:

- Capping API usage makes sense in cases where this has minimal or no business impact.
- Quotas can be used to set hard limits that throttle resource deployment.
- Budgets and alerts can be set for projects where absolute usage limits are necessary.
Taking this approach may end up being more cost-effective than having an expensive repatriation initiative.

## Case Study: Innovation vs. Costs at Zynga
Another thing to weigh up is pace of innovation — both from the cloud provider and from the consumer.

“Cloud gives you the opportunity to quickly search a space for possibilities — in other words innovate,” [Ian Miell](https://www.linkedin.com/in/ian-miell-694496/?originalSubdomain=uk), a partner at [Container Solutions](https://thenewstack.io/container-solutions-cloud-migration-with-the-best-tools-and-the-right-culture/), a cloud native consultancy, told The New Stack. “When you reach the end of the innovation cycle you look at optimizing, then you think about rebalancing cost, efficiencies and hiring fewer people. That’s why we are seeing 37signals doing it.”

It is also key to understanding one notable repatriation reversal, that of mobile gaming company [Zynga](https://www.zynga.com), which built its own zCloud infrastructure back in 2011.

The firm went through explosive growth. “I started at Zynga in July of 2009,” [Dorion Carroll](https://www.linkedin.com/in/dorioncarroll/), an adviser and former CTO and CIO, told The New Stack. “FarmVille had launched in AWS a month before. Within three months we were at 33 million daily active users.

“Had we launched it on our own servers, we simply could not have grown. We didn’t have enough physical hardware or data center space, and we could not have acquired it fast enough.”

However, 18 months later, Zynga started hitting problems. Some were caused by appropriately mandated security updates. “We had thousands of instances and very limited staff,” Carroll said. “Rebooting everything was daunting, and we didn’t have particularly good software development hygiene, so we didn’t know if the games would come back up if we restarted instances.”

The company also started hitting insufficient capacity events. “Of course, we weren’t AWS’s only customer, so we couldn’t have every instance they launched, but it was causing us problems,” Carroll said.

[Mark Pincus](https://www.linkedin.com/in/markpincus/), Zynga’s CEO and founder, decided the company needed to build its own environment. It was a mammoth undertaking. Zynga hired 100 data center specialists, came up with a specific hardware configuration it could run its own cloud on, and built several new, bespoke data centers in different locations to give resilience and redundancy.
By doing so, the company cut its costs by two-thirds, which seemed like a huge success. However, “Fast forward about three or four years, and all of our equipment is fully depreciated from a CAPEX point of view and worthless,” Carroll said. “We have over 40,000 instances and we’re looking at how we renew all of the equipment.”

On top of this, the business was also doing less well, and because the company was shrinking, all its top data center specialists had moved on. “We were stuck with neither expertise nor budget and with games that had been architected to handle explosive growth but no real plans as to how to shrink them,” Carroll said.

Zynga decided to shift back to AWS, shutting down some games as it transitioned back to the cloud, and closing data centers as the leases expired. It was tough. “About 75% of our games software engineers were focused on shutting things down and moving them,” Carroll said. “It wasn’t great but it ultimately saved us between $250 million to $350 million of capital investment.”

This likely saved the company, but even so, Carroll suggested, “The cost savings were really the least interesting part of the migration. What it really helped us do was accelerate innovation.”

Zynga’s games used a classic three-tiered architecture: web servers in the front, [Memcaching](https://thenewstack.io/how-pinterest-tuned-memcached-for-big-performance-gains/) for the caching layer, then either a [NoSQL](https://thenewstack.io/sql-nosql-and-vectors-oh-my/) or [MySQL](https://thenewstack.io/oracle-support-for-mysql-5-7-ends-soon-key-upgrades-in-8-0/) at the backend for persistence. “It’s a dumb example,” Carroll acknowledged, “but we had thousands of caching servers and we had a feature we wanted to implement that required a new version of Memcached. That turned out to require a new version of [libevent](https://libevent.org/), which in turn required a new version of [Linux](https://thenewstack.io/linux/).”

Zynga’s engineers weren’t sure their stack would even tolerate the change, but “in AWS we could spin up a few Memcached instances very quickly, rotate them into a pool of servers and see if everything worked in a matter of days,” Carroll told TNS.

Once the change was confirmed as successful, Zynga’s engineers could launch new instances and swap them in. Each step also gave a huge efficiency gain that kept compounding.

“We went from 100 servers to 12, but if we’d wanted to do this in our data center we’d have had to acquire all that new hardware in order to do the A/B tests and blue/green swap,” Carroll told us. “That ability to experiment is key, and it’s something we never could have done in our facilities.

“As we moved to new games and features, we could move very quickly, spinning things up and trying them out. If you or the players like them you keep them, if you don’t go back to what you had before.”

## The Impact on Hiring, Capacity Planning
The Zynga example highlights several other trade-offs. One to consider is that if you are running your own data centers, you need to be able to hire the right people and retain them. “That human expertise is almost impossible to replicate,” Carroll said.

Running on your own data centers requires ongoing capacity planning. If you’ve never had to do this, or have not done it for some time, it can be surprisingly fraught. Can you realistically project how many servers you will need ahead of time?

Those of us who can remember what this used to be like will be familiar with the very long procurement cycles we had to work around. Buying a new server, racking it, installing all the necessary software onto it, and adding it to a cluster could take weeks or months; it certainly wasn’t something you could do at the flip of a switch.

A consequence was that we tended to significantly over-provision as a risk management strategy and ended up with a large number of machines sitting idle. That still costs you money — you have to purchase them and pay for the electricity to run them and keep them cool, even if they are not running a workload.

This scenario has sustainability implications, too, because the static power draw of a server is still high; it will be using electricity and, assuming that power is being generated by fossil fuels, releasing carbon even if it is idle.

## Post-Cloud Sustainability Challenges
This doesn’t mean that the only way to build green software is on a public cloud (I’ve [given conference talks arguing this isn’t the case](https://www.conissaunce.com/presentations.html#writing-greener-software)), but the foundation processes are undoubtedly easier to manage on public clouds than on your own infrastructure.

These include techniques such as autoscaling and multitenancy to keep CPU utilization around 50% to 80%; locating workloads in places where the electricity is coming primarily from renewable sources and/or nuclear; and using [demand shifting and shaping techniques](https://www.conissaunce.com/demand-shifting-and-shaping.html) to run computationally expensive workloads when the electricity is greenest.

You don’t get this for free, though. “It is a shared responsibility model,” Currie said. “If you’ve simply [lifted and shifted](https://thenewstack.io/app-modernization-why-lift-and-shift-isnt-good-enough/), it may be a bit greener, but it isn’t very green. If you modernize and go fully cloud native, you can get a system that is more efficient than you can likely achieve on prem.”

AWS, [Microsoft Azure](https://news.microsoft.com/?utm_content=inline+mention) and Google Cloud all have strong sustainability goals and provide tools to assess your carbon footprint on their platforms ([Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/), [Azure Emissions Impact Dashboard](https://www.google.com/search?client=safari&rls=en&q=Azure+Emissions+Impact+Dashboard&ie=UTF-8&oe=UTF-8), and [Carbon Footprint](https://cloud.google.com/carbon-footprint), respectively). [Cloud Carbon Footprint ](https://www.cloudcarbonfootprint.org)is an open source alternative sponsored by [Thoughtworks](https://www.thoughtworks.com/) that can measure, monitor and reduce your carbon emissions on public clouds.

The public cloud gives you a wider range of possible locations for your workloads, meaning that you can use a tool such as [Electricity Maps](https://app.electricitymaps.com/map/24h) to identify locations that have a greener energy mix and just put your workloads there; it’s much easier than building a new data center. You can also consider using more advanced techniques, such as [demand shifting](https://www.conissaunce.com/demand-shifting-and-shaping.html) to perform more computationally intensive workloads at times or locations where energy is greenest.

By taking advantage of certain services offered by various clouds—in particular, burstable instances, spot instances (called “preemptible instances” on Google Cloud) and serverless services, such as Google Cloud Run, AWS Lambda and Azure Functions—you can typically engineer applications in a way that is greener and would be difficult to accomplish in your own data centers.

The wider point is that you typically get the best out of public clouds by taking advantage of the services they offer, but that implies lock-in, which is an anathema to many of us.

“What you want to do is adopt a platform that will take you all the way to 24/7 carbon-free electricity, without you having to do anything more than use that platform as it was intended,” Currie said. “And you are not going to be able to do that yourself.”

## Post-Cloud Security Challenges
There is another set of trade-offs around [security](https://thenewstack.io/security/). Keeping servers up to date, and guarding against intrusions, is time-consuming work that big cloud providers are very experienced in. Just [hiring and retaining good people to do this is difficult](https://thenewstack.io/how-to-get-started-filling-3-4-million-cybersecurity-jobs/).

Cloud service providers very rarely report security breaches and justifiably pride themselves on having high standards around data security. A related question is, as a private company, how are you going to handle the multitude of data sovereignty rules?

In industries such as finance and health care, regulators may be more comfortable with private data center use. “When I worked at Tier 1 banks, the concern was not objectively that cloud is less safe than on-prem,” Miell said. “It was more that the regulators were fine with on-prem. It isn’t about objective risk, it’s about the perception of risk to the regulator.”

A number of companies have suffered from the misconfiguration of cloud infrastructure. [Capital One’s loss of 100 million user records](https://thenewstack.io/capital-ones-cloud-misconfiguration-woes-have-been-an-industry-wide-fear/) back in 2019 is one such example. “The problem is you get these big red buttons you can push in the cloud, like ‘open up my S3 buckets to the world,’” Miell said. “The cloud providers have done mitigation work, but there is still a lingering fear of that kind of event happening and really embarrassing you.”.

There are also specific workloads that the cloud is not really designed for. If you need full control of your network, for example, the cloud isn’t ideal for this.

## What Is This Cloud Native Thing, Anyway?
As you’ve probably realized, this is quite subtle work; many of these trade-offs overlap and intersect. Another thing to consider is that it’s possible to get all the advantages of public cloud, to be “cloud native,” and still be running in your own data center.

“If you use open source tooling and build an appropriate platform, you can have cloud native software on-premises,” Miell told TNS. “You don’t have to be on the cloud to be cloud native.”

To some extent, this is what start-ups like [SoftIron](https://softiron.com) and [Oxide](https://oxide.computer) are looking to exploit.

However, Carroll is skeptical. “Unless you are a cloud provider, there is no excuse for you to be investing in the personal, hardware, networking and storage you need. You are investing in the wrong place.”

For Zynga, he added, the decision to abandon the cloud turned out to be the wrong choice. “because of the cost, impact on innovation and how much it hurt. It only seemed like the right decision at the time because no one was thinking far enough ahead.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)