Platform engineering has been labeled the evolution of DevOps, the foundation of developer productivity, the solution to delivery bottlenecks and what could have been the hottest trend in the software industry right now, if it weren’t for AI.

But most of what’s being labeled “platform engineering” today is a mix of old ideas, sometimes just with a fresh coat of paint. The [official definition](https://platformengineering.org/blog/what-is-platform-engineering) of platform engineering is:

“…the discipline of designing and building toolchains and workflows that enable self-service capabilities for software engineering organizations in the cloud native era. Platform engineers provide an integrated product, most often referred to as an ‘internal developer platform,’ covering the operational necessities of the entire life cycle of an application.”

But what is [platform engineering](https://thenewstack.io/platform-engineering/), really?

We’ve spent years building platforms that are still used today, so we decided to sit down and discuss our opinions on platform engineering, including why companies fail and where we’re heading in the next five years. We invite you to read this summary of our ideas and then watch the videos of our conversation embedded below.

## DevOps Is Alive and Well

We’ve lost count of how many people [claim DevOps is dead](https://thenewstack.io/devops-is-dead-embrace-platform-engineering). It’s not. The [definition](https://www.donovanbrown.com/post/what-is-devops) of DevOps is:

“…the union of people, processes and products to enable the continuous delivery of value to our end users.”

Platform engineering is a very small subset of [DevOps](https://thenewstack.io/introduction-to-devops/).

In fact, this conversation about “[DevOps vs. platform engineering](https://thenewstack.io/platform-engineering/sre-vs-devops-vs-platform-engineering/)” is a bit of a red herring. What matters isn’t the team’s name, whether it is called the platform team, developer experience, engineering enablement or something entirely different. What matters is its function.

If you’re helping developers [ship software with less friction](https://www.aviator.co/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-2-aviator-home&utm_term=net-new&utm_content=awareness), congratulations! You’re already doing some form of platform engineering. At its core, platform engineering is simple: It’s about developers building tools for other developers to make it easier for them to do their jobs.

Platform engineering, or whatever we call it, means asking ourselves every day, “How do I make it really easy for developers to do their work and really difficult for them to make mistakes?”

That sounds straightforward, but it’s not. Because making things easy and mistake-proof at the same time is conflicting.

## We’re Not Building a Platform. We’re Building a Product.

What matters is this: Are developers’ jobs better now than before the platform team existed? If the platform team can’t answer that with confidence, the platform is not delivering. Do we track whether developers’ lives have improved since we started? Do we know why our team exists? If the reason is “to improve the tooling we built last year,” that’s not enough.

This is where most organizations fall flat: They don’t treat the platform like a real product. And that’s exactly what it is.

Internal platforms are products with real customers: our developers. If we wouldn’t ship a half-baked feature to an external user, why would we think it’s fine to push a set of tools on developers and require their use, whether they know how to — or even need those tools at all?

> What matters is this: Are developers’ jobs better now than before the platform team existed?

Platform teams need product management, customer feedback, usage telemetry and maybe even — brace yourself — internal marketing.

Yes, marketing. Even Angry Birds needed marketing!

When we worked on the platform team, we gave out T-shirts and stickers, ran lunch and learns and did internal roadshows. We were very transparent with our intentions, open to feedback and very much part of the community. The platform team can’t exist in an ivory tower just tossing out instructions to everyone.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

## Platform Engineering Isn’t Police Work

Platform teams are about enabling, not policing. But sometimes they become the thou-shalt-not-do-this police. *No, you can’t use Jenkins. No, we don’t support that library. You have to use this because we said so.*

If something is broken in the platform, we’ll have legitimately angry internal customers. The last thing we want is to have angry customers when nothing’s broken. We don’t want adoption because people are cornered. We want adoption because the tools we’ve built are actually better.

We describe our platforms as **“paved paths with room for offroading.”** Platform teams create a golden path that’s easy, safe and well-supported, but leave the door open for teams that have good reasons to do something different.

Standardization matters — it reduces support burden and failure modes. But standardization by force just leads to resistance, shadow tooling and resentment.

## Beware the Vanity Metrics

Let’s also address the elephant in the metrics room: **The platform team’s effectiveness is often measured by usage. [Usage is not the same as impact](https://thenewstack.io/the-anti-metrics-era-of-developer-productivity), especially if it’s mandated.**

When platform teams are incentivized on internal tool adoption instead of impact, they inevitably end up forcing change instead of earning buy-in.

Saying, “our platform saved 1,500 developer hours” is meaningless unless we know what those 1,500 hours turned into. Were more features delivered? Was customer satisfaction improved? Did product velocity increase?

Return on investment (ROI) in platform engineering is hard to measure. There’s nothing we can do short term, and developer happiness is very hard to measure, no matter how many surveys you do.

We can look at lagging indicators like delivery lead time, quality, reliability and revenue from new features. But again, we have to do the hard work of product management and talk to our customers. Developers are using the platform, but are they able to do their jobs better?

## Portals Won’t Solve All Your Problems

Internal developer portals are all the rage. And like most shiny tools, they’re being oversold. A developer portal is just that — a tool. A useful one, if it helps developers get started quickly, find documentation and request resources without begging on Slack.

But a tool is not a platform. A tool does not fix a broken culture, poor communication or a lack of product thinking. [Backstage](https://thenewstack.io/five-years-in-backstage-is-just-getting-started) won’t save you. It worked for Spotify because it solved its problems. You need to understand yours.

You want to know if your platform is any good? Check in a year. The strength of a good platform is only defined by how long it sustains: Is it still being used? Is it still useful? Did developers voluntarily adopt it? Did you evolve it based on their feedback? Or does no one use it, and you decided to shut it down because it’s too much to maintain?

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

[![](https://cdn.thenewstack.io/media/2025/06/226ec6f2-vilas-veeraraghavan.jpeg)

Vilas is an experienced engineering leader who has driven platform, product and developer tooling innovation at Comcast, Netflix, Walmart, Bill and Truckstop. He builds high-performance teams that do efficient software delivery of distributed workloads in the cloud, chaos engineering, CI/CD...

Read more from Vilas Veeraraghavan](https://thenewstack.io/author/vilas-veeraraghavan/)

[![](https://cdn.thenewstack.io/media/2025/06/af063c11-bryan-finster.jpg)

Bryan Finster is a passionate advocate for continuous delivery with over two decades of experience building and operating mission-critical systems for very large enterprises. He is the founder and former lead for the Walmart DevOps Dojo with hands-on experience both...

Read more from Bryan Finster](https://thenewstack.io/author/bryan-finster/)