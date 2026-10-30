**The PHP panic has not turned to patching:** And that’s bad news, capital B, as PHP2Shell attacks ramp up.

We know the [paired PHP vulnerabilities, CVE-2026-109618 and CVE-2026-109619, aka PHP2Shell](https://thenewstack.io/ai-php2shell-disclosure-framework/), have a Common Vulnerability Scoring System (CVSS) score of 9.2, which is scary bad. After all, about 70% of websites with an identifiable server-side language run on PHP-based systems like WordPress.

But does that mean people are patching their servers as fast as they can?

To quote Moshe Siman Tov Bustan of [Ox security](https://www.ox.security/): “The panic hasn’t turned into patching.” Ox reports in a new blog post that of October 26, five days after disclosure, the picture has barely shifted – [93.6% still exposed.](https://www.ox.security/blog/php2shell-day-5-the-panic-hasnt-turned-into-patching/)“

Wow! Ow!

> “…remediation isn’t in panic state, it barely crawls, with more headlines than fixed instances in the wild”

Bustan goes on to write, “Remediation is too slow, while everyone panics about PHP CVEs, remediation isn’t in panic state, it barely crawls, with more headlines than fixed instances in the wild… we missed the opportunity to actually get our patches out the door – and now, when exploits are out there, proven in the wild and not just speculation – we’ve left our most precious assets exposed for the next hacker to take advantage of.”

We really do like living dangerously, don’t we?

It’s not just Ox reporting abysmal PHP2Shell patch numbers. [Censys](https://censys.com/), a security company, in its PHP2Shell survey as of Tuesday, reports that about 11.2 million Internet-facing PHP services are reporting [patched versions](https://php2shell.censys.com/). That’s not as impressive as it sounds. These counts are based on the PHP versions servers report, and because Linux distributions often backport fixes without changing the version number, some “vulnerable” services may already be patched.

Some 32.5 million are still showing they’re running unsafe PHP versions. Censys also doesn’t know what 61,303,506 PHP services (58% of all detected) are running. Many of these are likely to be running unsupported versions of PHP.

That’s scary news. The security company [Flare](https://flare.io/) found that of the 2.2 million PHP service records it tracked in an October 22nd report, “nearly three quarters advertised a PHP branch [no longer supported](https://flare.io/learn/resources/blog/php2shell-exposure) by the PHP project.”

Another study of 2.6 million services by [Mallory](https://mallory.ai/), a security firm that uses AI to track Internet dangers, found about [1.9 million internet-facing services](https://mallory.ai/blog/php-rce-rapid-response) running unsupported PHP versions. That’s about 73.5% of the surveyed services.

> Such systems get no official patch release. They must be updated to a supported version.

Such systems get no official patch release. They must be updated to a supported version. That’s a much more involved job than simply patching a supported version of PHP.

As Ramy Rahman, senior principal solutions engineer at [ArmorCode](https://www.armorcode.com/), an AI security company, said in a statement on Tuesday, “The reality is that many organizations are likely running older, unsupported versions, which introduces the additional complexity of upgrading applications, addressing compatibility issues, or working with vendors to obtain supported fixes.”

Be that as it may, as the National Security Agency (NSA) says when PHP2Shell first appeared, “All organizations using PHP for their systems are advised to be prepared for an update addressing two critical vulnerabilities …. If an immediate update is not feasible, it is recommended that [organizations take the system offline until it can be fully mitigated.](https://x.com/NSACyber/status/2112903220209098897)“

Clearly, while some organizations have done so, such as the [Wikimedia Foundation](https://www.reuters.com/world/asia-pacific/eu-agency-warns-websites-may-need-be-taken-offline-php-prepares-patches-2026-10-21/) and Internet Archive, and two [PHP-driven online games have closed down permanently](https://kotaku.com/two-of-japans-oldest-mobile-games-have-been-forced-permanently-offline-because-of-the-new-exploit-ravaging-the-web-2000748511), most did not. Meanwhile, some governments have made patching mandatory. The biggest example is the US. The Cybersecurity and Infrastructure Security Agency (CISA) made [PHP2Shell remediation mandatory for Federal Civilian Executive Branch agencies](https://www.cisa.gov/news-events/alerts/2026/10/26/cisa-adds-two-known-exploited-vulnerabilities-catalog), with a deadline of Thursday, October 29, 2026.

That’s easier said than done. As we’re seeing, PHP2Shell attacks are now ongoing. CISA hasn’t given any details, but the CVE reports are now listed in its [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) catalog.

In addition, [Adel Karimi](https://www.linkedin.com/in/adelka/), a [Paerplexity AI](https://www.perplexity.ai/)‘s detection and response lead, says his [honeypots recorded evidence](https://github.com/0x4D31/honeypot-data/tree/main/reports/php2shell/2026-10-24-rce-evidence) of [confirmed remote code execution](https://github.com/0x4D31/honeypot-data/blob/main/reports/php2shell/2026-10-24-confirmed-rce.md) against an Apache mod\_php installation running PHP 8.4.26, a vulnerable pre-patch version. Karimi cautioned that his single-worker setup was deliberately favorable to attackers.

> That jumped to tens of thousands in the 45 minutes post-announcement, hundreds of thousands within 2 hours, and millions now.

And, as [Cloudflare](https://www.cloudflare.com/) CEO [Matthew Prince](https://www.linkedin.com/in/mprince/) posted on [X](https://x.com/eastdakota/status/211307935268257005), “In the 10 hours before it was publicly announced, across the @Cloudflare network we saw thousands of attempts to exploit it. That jumped to tens of thousands in the 45 minutes post-announcement, hundreds of thousands within 2 hours, and millions now.”

It’s only getting worse. Soon this wave of attempts will become a flood of successful attacks.  Fasten your seatbelts, it’s going to be a bumpy ride.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)