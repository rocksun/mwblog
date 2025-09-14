Application availability and downtime are concerns no organization can afford to overlook.

While the hard numbers vary by use case, the big picture is clear: Application downtime almost always translates to lost money. According to research from [Oxford Economics](https://www.oxfordeconomics.com/resource/the-hidden-costs-of-downtime-the-400b-problem-facing-the-global-2000/), unplanned downtime costs the Global 2000 $400 billion a year, for an average annual loss of $200 million per company.

And that’s just the start. Per a new [survey](https://www.pgedge.com/press-releases/new-survey-shows-strong-demand-for-high-availability-as-businesses-increasingly-use-postgresql-in-mission-critical-applications-and-to-alleviate-cloud-outage-concerns) conducted by pgEdge on [PostgreSQL](https://roadmap.sh/postgresql-dba) in mission-critical applications, when businesses exceed maximum downtime goals, 56% experience delayed business operations, 49% see increased support volume or customer complaints, 47% require emergency technical remediation and 33% lose revenue or see delayed transactions.

The risk is even [greater for high-stakes organizations](https://thenewstack.io/distributed-postgres-high-availability-for-mission-critical-apps), like those providing healthcare, government or financial services, such as investment management, explained [Phillip Merrick](https://www.linkedin.com/in/phillipmerrick/), co-founder and CEO at [pgEdge](https://thenewstack.io/startup-pgedge-tackles-the-distributed-edge-with-postgres/), in an interview.

“If the trading platform you use to manage your stock positions goes down even for five minutes, that could result in millions of dollars of loss,” said Merrick.

Of course, not every outage is necessarily a reason to panic.

“Some applications, some businesses … can maybe tolerate a half hour or an hour of downtime,” Merrick noted. “But then you have to ask yourself: ‘Given how I’ve architected my applications, and given where they’re running, what is my likely risk of downtime?’”

And that’s where a lot of businesses are running into trouble.

## Why Open Source Needs a High-Availability Strategy

Over the last two decades, Merrick has noticed a developing sea change in enterprise software.

First has been the steady move from on premises to cloud infrastructure. At the same time, businesses increasingly rely on open source software, which Merrick attributed to the opportunity for greater innovation and lower costs when opting for open source instead of legacy vendors.

The move to cloud infrastructure and open source software represents a stark change in the industry, but it’s been a gradual, almost imperceptible transition.

“Early cloud usage was literally developers putting cloud subscriptions on their credit card,” he recalled. “And then before you know it, you’ve actually got some critical applications that are running in the cloud.”

A similar trend played out with open source software. And as companies began using more open source components, they eventually realized they were relying on open source software for many critical applications, but they didn’t have a strategy for high availability.

## The Downtime Risks of a Single Cloud Region

“If you think about companies that are relying on the cloud providers,” Merrick pointed out, “your application typically is going to be resident in just one region.”

That might not sound troublesome, but when you consider that cloud providers are no strangers to major, multihour outages, it’s a frightening — or at least, worrying — prospect.

In surveying 212 IT decision-makers in organizations with 500+ employees across financial services, software, computing and manufacturing, pgEdge found that 21% of respondents have experienced a cloud region failure in the last year.

They’ve certainly made the headlines. The [2021 AWS Tokyo outage](https://thenewstack.io/what-you-can-learn-from-the-aws-tokyo-outage/), the [2023 Google Cloud outage](https://thenewstack.io/google-cloud-services-hit-by-outage-in-paris/) and the [2023 AWS US-East-1 outage](https://www.sdxcentral.com/news/aws-us-east-1-region-outage-downed-many-websites-now-resolved/) are just a few that come to mind. Yet again, [Google Cloud saw an outage in June of this year](https://techcrunch.com/2025/06/12/google-cloud-outage-brings-down-a-lot-of-the-internet/), shuttering services for several hours with ripple effects to downstream providers, including Cloudflare and OpenAI.

It’s no wonder, then, that one in four IT leaders [told Splunk](https://www.splunk.com/en_us/form/digital-resilience-pays-off.html) they believe infrastructure outages are their organization’s most likely source of disruption.

Unfortunately, organizations can expect further outages, simply “because of the way that the cloud providers have architected their clouds. The default is to put your application in just one region,” according to Merrick.

Therein lies the danger. When organizations tie applications to a single region, they introduce a single point of failure, mar availability and create risks for outages and costly downtime.

“A lot of businesses maybe haven’t fully thought this through or really haven’t quantified what those risks to their business actually are,” Merrick said. “High availability is an issue for any business that has a significant cost to their critical applications being down. Every business needs to understand and quantify what downtime will mean for them, and then act accordingly.”

## High Availability: A Growing Concern

Of course, the woes of downtime and availability aren’t anything new, ”but it is something that everyone has become increasingly more focused upon,” Merrick stressed.

That’s largely the result of consumer users, who now decry even the slightest delay when scrolling Instagram or other general applications. That demand for speed has evolved into a near-zero tolerance for delays or downtime across domains: “We want the applications we use to be always on and always available,” emphasized Merrick.

While end-user expectations have risen in recent years, many industries were already tuned into the importance of high availability.

“In some industries — healthcare, financial services, some government services — they simply can’t be down,” Merrick added. “And that’s always been the case.”

Still, that doesn’t mean these industries had an effective strategy to minimize downtime and ensure high availability.

Many organizations — banks, for example — continue to rely on scheduled maintenance, taking systems offline for several hours at supposedly inconvenient times, such as between 2 and 5 a.m. EST.

But Merrick argued that “scheduled maintenance should be a thing of the past.”

For one thing, increasingly global communities mean “off times” no longer truly exist. Whether they provide mission-critical or more commercial services, businesses are expected to be up and running around the clock.

“You ought to be able to do maintenance — upgrading the software, applying the latest security patches — without the application having to be taken down to support the maintenance,” Merrick said.

The reality is, a lot of businesses just aren’t there, even though 79% of respondents in pgEdge’s recent survey say they are evaluating or considering distributed or purpose-built high-availability products for PostgreSQL environments.

## The Challenge of Keeping Data in Sync Across Regions

Whether organizations are dealing with a physical data center they control or a cloud region owned by a cloud provider, it’s been a persistent challenge to keep data in sync across regions — especially with Postgres, the widely adopted relational database for transactional workloads, which wasn’t originally designed for distributed deployments.

As Merrick explained, “You can’t do an instant failover from one region to another unless the database in both places is continually kept in sync.”

That is, unless you opt for a distributed [multimaster](https://www.pgedge.com/solutions/benefit/multi-master) architecture, which allows multiple nodes, each capable of both reading and writing, to stay continuously in sync across regions. This way, if one node or even an entire region goes offline, the application can continue operating with minimal disruption.

If that’s the case, what’s behind the continued reliance on traditional, single-region approaches?

One hesitation has been the perceived complexity of multimaster architecture. “The misconception is that it’s just going to be too hard,” Merrick said.

The same goes for a multiregion strategy, where he acknowledged that “to be able to architect for multiregion is actually difficult unless you’ve got a distributed database.”

Still, despite reservations about complexity, that doesn’t mean it hasn’t been on companies’ radars. For example, in the recent pgEdge survey, almost half (47%) of organizations that deploy applications across multiple cloud regions said they are interested in multimaster replication.

“I know of several CTOs that have multiregion failover as an item in the product roadmap, but they just figured that that was going to be so hard,” Merrick recalled, “so it languished as an item that was very important but always lower down on the roadmap.”

Merrick believes that doesn’t have to be the case — at least not anymore.

## How pgEdge Makes Multimaster Postgres Feasible

Postgres is a powerful database widely lauded for its reliability and flexibility, but it doesn’t come with a distributed option for high availability out of the box.

That’s what pgEdge aims to solve with its fully open source, fully Postgres software.

pgEdge delivers a [distributed Postgres architecture](https://www.pgedge.com/solutions/benefit/postgresql-high-availability), enabling multimaster, multiregion deployments to ensure high availability and low latency and eliminate the costly risks of single-region cloud outages.

Merrick said it’s made possible in part due to pgEdge’s ability to replicate between the nodes, where changes made in one location automatically sync to others in real time.

Notably, this replication requires no manual intervention, which Merrick cited as a frequent concern among engineering teams.

“Some of the folks we work with have tried to use Postgres’s own logical replication in the past, and it needed quite a lot of manual intervention.”

That’s not the case with pgEdge, he said.

But what about the possibility of two writers in two different locations trying to update the same data at the same time?

That’s when conflict resolution comes into play, where pgEdge resolves conflicts via a set of predefined rules — in short, the second write wins. For instances where this rule of thumb can’t apply, pgEdge uses “conflict avoidance” to prevent operations most likely to result in conflict.

“Between conflict resolution and the conflict avoidance, no manual intervention is necessary,” he explained, a win for teams curious about [distributed multimaster Postgres architecture](https://www.pgedge.com/solutions/benefit/multi-master) but dubious about the labor required to make the switch.

## The Future of Distributed Multimaster Architecture

With support for multimaster, multiregion deployments and built-in conflict resolution and avoidance, pgEdge aims to empower organizations with consistent, high availability for more seamless user experiences and less disruptive downtime.

One [global investment management firm](https://www.google.com/url?q=https://a.storyblok.com/f/187930/x/d55b4b196d/financial_services_usecase.pdf&sa=D&source=docs&ust=1757014017919370&usg=AOvVaw3bX8TxPf6c1PBH3oAUI0HG) is already seeing the benefits.

Straddling multiple geographies, asset classes and time frames with more than 1,000 employees and $20 billion assets under management, the firm needed high availability to underpin its high-volume trading platform. With pgEdge, it gets an open source solution fully based on standard Postgres that delivers high-availability features and logical replication capabilities for near-zero downtime upgrades, improved performance and elimination of a single point of failure — an increasingly thorny issue as cloud outages continue to threaten service continuity.

Looking beyond finance, Merrick sees an expanding need for distributed multimaster architecture across industries.

After several years of experimentation with AI applications, “companies are in the process of actually rolling them out and making them available to employees and customers, sometimes on a global basis,” he observed. Realizing this shift will require new strategies to ensure always-on, always-available data access, low latency and minimal downtime.

“And it turns out that pgEdge is a really great fit for AI applications that need to be globally available,” he added.

[Learn more](https://www.pgedge.com/PostgresHAsurvey) about how multimaster [distributed Postgres](https://www.pgedge.com/products/what-is-pgedge) solves high availability and low latency challenges to power global applications.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.