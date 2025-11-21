On Nov. 18, 2025, [Cloudflare](https://www.cloudflare.com/) experienced a [major outage](https://apnews.com/article/cloudflare-outage-x-openai-9335e8e0da2a0027d1fbac5eb97d11ae) lasting several hours that disrupted access to numerous popular websites and online services worldwide. This was only the latest in a wave of major Internet service providers going down. Others have included [Amazon Web Services](https://thenewstack.io/a-cascade-of-failures-a-breakdown-of-the-massive-aws-outage/) and [Azure](https://www.zdnet.com/article/massive-azure-outage-is-over-but-problems-linger-heres-what-happened/), both in October. It’s becoming painfully clear that we rely all too much on a handful of cloud and network services companies.

However, there’s no single flaw here. In [AWS](https://aws.amazon.com/?utm_content=inline+mention)‘s case, it was ultimately — yes, you know this story — a [Domain Name System](https://thenewstack.io/13-years-later-the-bad-bugs-of-dns-linger-on/) (DNS) foul-up, while Azure’s failure was due to a mistaken configuration change. With [Cloudflare, the root cause was a database system’s permissions blunder](https://blog.cloudflare.com/18-november-2025-outage/). This resulted in popular sites and services such as Shopify, Amazon, and Robox failing, and in essentially all AI chatbots, such as ChatGPT, Perplexity, and Anthropic Claude, being knocked out.

## Root Cause: A Database Permissions Blunder

Specifically, the outage was triggered not by a cyberattack, but by a software bug in Cloudflare’s Bot Management system. Specifically, a recent change to the permissions for a database query generated an overlarge “feature file” that was used by the Bot Management module with many duplicate entries.

This file is usually a fixed size and regenerated every few minutes, but the bug caused the file to exceed expected limits, thereby crashing the [Bot Management module](https://www.cloudflare.com/application-services/products/bot-management/) repeatedly. Since this module is integral to Cloudflare’s core proxy pipeline, any traffic relying on it was affected, resulting in widespread 5xx errors.

## Outage Timeline and Resolution

The issues began around 11:20 UTC, with symptoms including elevated latency, access authentication failures, and error codes surfaced throughout Cloudflare’s core networks. Initial confusion led some teams to suspect a large-scale DDoS attack, but this was quickly ruled out once the root cause was identified as the corrupted feature file.

In the meantime, many people on the net at work and play noticed trouble. As [Cisco ThousandEyes](https://www.thousandeyes.com/) reported, while network paths to Cloudflare’s frontend infrastructure appeared clear of any elevated latency or packet loss, [Cisco ThousandEyes observed a number of timeouts and HTTP 5XX server errors](https://www.thousandeyes.com/resources/internet-outages-timeline), which are indicative of a backend services issue. Ironically, even websites that monitor web outages themselves, such as Downdetector, went down due to the Cloudflare failure.

## Outage Timeline and Resolution

Behind the scenes, Cloudflare explained, the feature file was being regenerated every five minutes by a query running on a [ClickHouse database cluster](https://clickhouse.com/docs/architecture/cluster-deployment), which was being gradually updated to improve permissions management. So, “every five minutes, there was a chance of either a good or a bad set of configuration files being generated and rapidly propagated across the network.”

“Eventually,” Cloudflare continued, “every ClickHouse node was generating the bad configuration file and the fluctuation stabilized in the failing state.” This fix was to stop “the generation and propagation of the bad feature file and manually insert a known good file into the feature file distribution queue. And then forcing a restart of our core proxy.”

Fortunately, Cloudflare’s engineers halted the generation and propagation of the bad files relatively quickly. By 14:24 UTC, Cloudflare had rolled back to a previously stable version. Core traffic largely normalized by 14:30 UTC, with full system restoration completed by 17:06 UTC.

## Cascading Effects on Ancillary Systems

As is always the case with such things, one problem cascaded into another. Other impacted ancillary Cloudflare systems were affected. This included the [Workers KV storage](https://developers.cloudflare.com/kv/) and [Cloudflare Access](https://www.cloudflare.com/zero-trust/products/access/), which depend on the core proxy, and suffered increased error rates and login disruptions. The [Cloudflare Dashboard login](https://dash.cloudflare.com/) was severely affected as [Turnstile](https://www.cloudflare.com/application-services/products/turnstile/), Cloudflare’s CAPTCHA service, failed to load correctly. It also didn’t help any that CPU usage surges due to internal debugging systems working overtime to diagnose uncaught errors, and was always slowing the content delivery network (CDN) down.

All together, the main outage lasted about three hours with a period of recovery, then final stabilization following full remediation. Some clients experienced longer disruptions due to backlogs and retry storms as services returned to life.

## Cloudflare’s Commitment to Preventing Future Outages

Looking ahead, Cloudflare has committed to several measures to prevent recurrence. These include:

* Hardening ingestion of configuration files with validation similar to user inputs.
* Implement global kill switches for problematic features to rapidly isolate issues.
* Eliminate scenarios where error reports or core dumps could overwhelm resources.
* Conduct thorough reviews of failure modes across all core proxy modules.

That’s all well and good, but this failure, when considered alongside other recent Internet outages, has underscored just how fragile today’s Internet is. True, external attacks, such as [Terabyte-sized Distributed Denial of Service (DDoS) attacks](https://www.zdnet.com/article/cloudflare-blocks-largest-ddos-attack-heres-how-to-protect-yourself/), which can cascade into global service outages for millions of users, are also a real problem. But, even without such attacks, these system failure incidents are raising important questions about just how safe critical cloud infrastructure systems are anyway.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)