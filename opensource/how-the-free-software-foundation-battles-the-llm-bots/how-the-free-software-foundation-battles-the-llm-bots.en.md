A [July 2 blog post](https://www.fsf.org/blogs/sysadmin/our-small-team-vs-millions-of-bots) by senior systems administrator [Ian Kelling](https://www.fsf.org/about/staff-and-board#iank) points out that the infrastructure for the Free Software Foundation “has been under attack since August 2024.”

“Nothing has changed since the article,” FSF sysadmin [Michael McMahon](https://www.fsf.org/about/staff-and-board#michael) told The New Stack on Tuesday. “We are still dealing with all of these issues.”

The organization has with has just two full-time tech team employees plus a handful of “dedicated volunteers” to deal with the issue.

And the FSF’s July post links to [a report from LibreNews](https://thelibre.news/foss-infrastructure-is-under-attack-by-ai-companies/) noting similar issues at high-profile FOSS sites including the Fedora project, KDE GitLab infrastructure, the GNOME GitLab instance, Diaspora, and even the FOSS news site Linux Weekly News. (And “[GNOME](https://thenewstack.io/what-makes-gnome-so-appealing/) has been experiencing issues since a last November…”)

Articles like the FSF’s are a way of sharing “techniques and tools”, McMahon said Tuesday. Though he adds that some system administrators also have a private mailing list “where we can coordinate and share effective strategies. The specific mitigations often cannot be published because that would give our attackers an advantage.”

There’s a lot to learn from the FSF’s battle against the bots — about the tactics of sysadmins, but also about the new challenges that they’re facing today from those “hyper-aggressive LLM crawlers” ? As the FSF puts it in its blog post… “It seems that the health of the web has some serious problems right now.”

## Maintaining 70 Sites

It’s a bigger challenge than it seems. The FSF tech team maintains more than 70 different web sites, services and platforms — not just for FSF and GNU projects but also for “the wider free software community” (including popular web frameworks like [Drupal](https://www.fsf.org/working-together/gang/drupal) and [MediaWiki](https://directory.fsf.org/wiki/MediaWiki), the [KDE desktop environment and software collection](https://directory.fsf.org/wiki/Kde), and even the classic game [NetHack](https://directory.fsf.org/wiki/Nethack)). “We recently counted seventy different services,” Kelling writes, “and have a dozen physical servers across two Boston-area data centers.”

Yet “We don’t use any of the so-called ‘cloud’ services,” [explains another web page](https://www.fsf.org/blogs/sysadmin/join-the-fsf-and-support-the-tech-team), “since the ‘cloud’ they typically refer to [is just someone else’s computer](https://www.gnu.org/philosophy/who-does-that-server-really-serve.html). We do not abstract away problems with frameworks on top of Docker containers running in Kubernetes assembled by someone who tells you to directly pipe curl output into bash and install the software as root without looking at it…”

The FSF holds its stack to a higher standard, the post explains, and “We assemble our software stacks in a way that we can understand and keep track of by configuring services orchestrated by [Ansible](https://thenewstack.io/red-hat-ansible-and-hashicorp-terraform-will-be-coming-together/) in virtual machines with libvirt on Trisquel GNU/Linux, running on bare-metal ASUS KGPE-D16 servers that we own, operate, and trust… “we self-host everything we possibly can so that the software we use can be trusted…”

The admin team even verifies that there’s no nonfree dependencies being run by their software. “We only run code that we can run, modify, copy, and share, right down to running a fully free BIOS on our servers.”

## Repelling an Ongoing Attack

Maintaining all these sites is a “huge task,” July’s blog post explains — especially in the face of those aggressive LLM web crawlers that “have been a significant source of the attacks.”

McMahon explained Tuesday that “These likely LLM companies are not leaving contact details so there is no individual companies to report to other than the owners of the IP addresses.”

So like other sites, their first line of defense is “identifying which IP addresses are sending requests as part of the [[Distributed Denial of Service](https://thenewstack.io/how-a-popular-combo-provides-ddos-protection/)], and then having the server ignore requests from those IP addresses,” the blog post explains.

But that’s not as simple as it sounds. Last December a [blog post](https://www.fsf.org/bulletin/2024/fall/fsf-sysops-cleaning-up-the-internet) remembered that “one of the recent attacks from the last few months, required blocking more than 40,000 IP addresses from a DDoS attack.” And this month Kelling wrote “That attack continues, but we have mitigated it.” (Although in this case, “Judging from the pattern and scope, the goal was likely to take the site down and it was not an LLM crawler.”)

The bad news? “Since then, we have had more attacks with even higher severity.” And there’s multiple attacks from a variety of sources…

* “GNU Savannah, the FSF’s collaborative software development system, was [hit by a massive botnet controlling about five million IPs](https://www.fsf.org/bulletin/2025/spring/defending-savannah-from-ddos-attacks) starting in January.” On July 2, it was “still ongoing, but the botnet’s current iteration is mitigated.” The admin team speculates it’s intended to build an LLM training dataset.
* gnu.org and ftp.gnu.org experienced a new DDoS attack starting May 27. (Also currently mitigated, “Its goal seems to be to take the site down… It has had several iterations, and each has caused some hours of downtime while we figured out how to defend ourselves…”)
* directory.fsf.org, the server behind the Free Software Directory, came under attack on June 18. Two weeks later, that attack was still “very active,” though “partially mitigated.” They believe that attack “likely is an LLM scraper designed to specifically target Media Wiki sites with a botnet.”
* There’s also the usual high-impact traffic from vulnerability scanners and web crawlers, as well as crawlers that pretend to be regular users — or other crawlers.

“We have to figure out a specific defense approach for each attack…” the blog post explained.

There’s another kind of problem. [Automated CI/CD pipelines](https://thenewstack.io/ci-cd/) “often send far more requests than is necessary, which looks and acts like a DDoS attack even though it is not intended to be”. One example is checking — and re-checking — on possibler new code updates for software rebuilds. And “they tend to not provide contact details,” McMahon said Tuesday. “Our methods of contacting them are to send abuse reports to the owners of the IP addresses or to run a ‘scream test’ where we block the address and see if they complain.

“Scream tests are often effective and lead to constructive conversations about better ways to use our resources.”

But the blog post notes that the address-blocking doesn’t always work, and instead “often prompts them to search for better ways to accomplish the same goals.”

## Fighting Back

First, free-software monitoring tools like [Prometheus](https://thenewstack.io/creating-a-path-for-prometheus-success/) and [Uptime Kuma](https://uptime.kuma.pet/) alert them to outages or slowing response times, and “the logs of the service affected usually tell a story.” (Suspicious requests include things like searching for WordPress-specific pages on a site which isn’t even using WordPress or making multiple page requests per second — and they’re cross-checked against tables of the IP address-prefixing ASNs using a tool called IPtoASN).

Then addresses are blocked with “a variety of firewalls,” and there’s also behavior-based blocking with tools [fail2ban](https://github.com/fail2ban/fail2ban) and agent-based rules with [Modsecurity](https://modsecurity.org/). Sometimes they’ll even make abuse reports to ISPs and hosting companies (though “that page may use nonfree JavaScript. We can usually get around using nonfree JavaScript in cases like these by sending an email with a description of the abuse, a snippet of the log, and expected behavior…”)

It’s part of a longer-term strategy. “Hopefully, Internet Service Providers, cloud providers, and mobile carriers will start taking notice of abuse coming from their networks,” McMahon said Tuesday, “and help us out by getting to the root of the greater problem.”

But in the meantime, FSF firewalls can block most of the vulnerability scanners, according to the blog post, and “We may need to block individual addresses, CIDR addresses, VPS providers, or even entire ASNs.”

## A Larger Problem

The FSF finds its sites facing website crawlers that “ignore the robots.txt files, scan too fast, and take down sites” — and here the blog post calls out “especially” those crawlers “written by large language model companies.”

The crawlers are a problem for other sites too, judging by [a March blog post from SourceHut’s CEO/founder Drew DeVault](https://drewdevault.com/2025/03/17/2025-03-17-Stop-externalizing-your-costs-on-me.html). DeVault said these hyper-aggressive LLM crawlers “do so using random User-Agents that overlap with end-users and come from tens of thousands of IP addresses — mostly residential, in unrelated subnets, each one making no more than one HTTP request over any time period we tried to measure — actively and maliciously adapting and blending in with end-user traffic and avoiding attempts to characterize their behavior or block their traffic.”

And it’s taking a toll, DeVault wrote. “We are experiencing dozens of brief outages per week, and I have to review our mitigations several times per day to keep that number from getting any higher… Several high-priority tasks at SourceHut have been delayed weeks or even months because we keep being interrupted to deal with these bots, and many users have been negatively affected because our mitigations can’t always reliably distinguish users from bots. All of my sysadmin friends are dealing with the same problems.”

Some websites use [Anubis](https://github.com/TecharoHQ/anubis), which sends out a JavaScript program requiring computation before allowing site access. But though it matches the FSF’s definition of free software, “we do not support this scheme because it conflicts with the principles of software freedom… a program which does calculations that a user does not want done is a form of malware,” DeVault said.

The blog post ends on a hopeful note. “Even though we are under active attack, gnu.org, ftp.gnu.org, and savannah.gnu.org are up with normal response times at the moment, and have been for the majority of this week… We’ve shielded these sites for almost a full year of intense attacks now, and we’ll keep on fighting these attacks for as long as they continue.”

Volunteers are always welcome to help them continue in this mission, of course. There’s a dedicated page suggesting [multiple ways to help](https://libreplanet.org/wiki/Group:FSF:Tech_Team_Volunteers), McMahon said Tuesday, and “We onboard new volunteers on an ongoing basis.”

But even if you’re not a sysadmin, they [pointed out in December](https://www.fsf.org/bulletin/2024/fall/fsf-sysops-cleaning-up-the-internet), “The best way to signal long-term support with the FSF SysOps team, and the FSF as a whole, is to become an FSF associate member.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/82081813-7zddypfe_400x400.jpg)

David Cassel is a proud resident of the San Francisco Bay Area, where he's been covering technology news for more than two decades. Over the years his articles have appeared everywhere from CNN, MSNBC, and the Wall Street Journal Interactive...

Read more from David Cassel](https://thenewstack.io/author/destiny/)