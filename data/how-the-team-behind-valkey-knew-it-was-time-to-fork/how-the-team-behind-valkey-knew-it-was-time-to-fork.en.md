TOKYO — Forking an open source project is never a first choice. It is divisive, dangerous, and politically risky. But sometimes, as [Valkey](https://valkey.io/) leaders [Roberto Luna Rojas](https://www.linkedin.com/in/robertolunarojas) and [Madelyn Olson](https://www.linkedin.com/in/madelyn-olson-valkey/) said during their talk here Monday at [Open Source Summit Japan,](https://events.linuxfoundation.org/open-source-summit-japan/) you don’t have a choice. It’s the only viable path forward to protect an open source project.

For those who don’t know the story, a recap: In 2024, [Redis](https://redis.com/?utm_content=inline+mention), producers of the widely used in-memory key-value NoSQL database, [decided to dump its three-clause Berkeley Software Distribution (BSD) license](https://lwn.net/Articles/966133) and replace it with the read-only [Redis Source Available License (RSALv2)](https://redis.com/legal/rsalv2-agreement/) and [Server Side Public License (SSPLv1)](https://redis.com/legal/server-side-public-license-sspl/). That went over like a lead balloon with members of its core developer team.

So, they quickly decided to [fork the code into the program we now know as Valkey](https://thenewstack.io/valkey-will-not-just-be-a-redis-retread/). Valkey is proving to be [a very successful fork](https://thenewstack.io/valkey-8-1s-performance-gains-disrupt-in-memory-databases/). With [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention), [Google](https://cloud.google.com/?utm_content=inline+mention),  [Microsoft](https://news.microsoft.com/?utm_content=inline+mention), [Oracle](https://www.oracle.com/developer?utm_content=inline+mention) and other tech powers all backing [Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/ "Valkey"), this open source fork is doing great. Perhaps most telling of all, Redis decided this past May [to reopen the program’s codebase under the GNU Affero General Public License (AGPL)](https://thenewstack.io/redis-is-open-source-again/).

Back in 2024, however, the Valkey fork team members didn’t know that. They just knew they had to move. This is their story.

Speaking before a full room at Open Source Summit Japan, Olson and Luna Rojas, both longtime Redis contributors, detailed the warning signs that preceded the Valkey fork from Redis, the steps the community took to prepare, and the hard-won lessons they believe every open source maintainer should understand.

## Spotting Red Flags

Olson, now a principal engineer at AWS, said the biggest issues emerged from governance that slowly centralized control inside Redis, the company.

In retrospect, she said, Redis open source maintainers like herself saw three main warning signs they should have heeded.

The first was closed governance: Redis-appointed maintainers “had special permissions within the project,” while external maintainers like Olson “were basically just normal members,” leaving core decisions in the hands of company employees.

Then all power was in the hands of the company, not the community. “Redis also had explicit veto permissions … [and] the ability to veto anything they wanted,” she added. This allowed the company to force features into the project — even when maintainers disagreed.

Olson cited [Redis Functions](https://redis.io/docs/latest/develop/programmability/functions-intro/) as one example of a feature “forced into the project by Redis … because they thought that’s what they wanted,” despite pushback from community maintainers.

The community also saw features rejected for non-technical reasons, which Olson called “a very important warning sign.” One widely requested feature from AWS, Google and others, [cluster slot statistics](https://valkey.io/commands/cluster-slot-stats/), was denied simply because Redis did not want it.

Beyond governance, Redis’s project infrastructure was opaque, according to Olson. Builds, performance testing and even the hosts from which open source artifacts were released were private or proprietary. “Only Redis people could do the actual releases,” she noted, which became a severe obstacle later when the fork occurred.

Redis declined to comment on the Valkey maintainers’ claims.

In March 2024, Redis changed its license. Olson said the open source maintainers knew something was up and change might be imminent. That shift triggered the creation of Valkey, a fully open, Linux Foundation-stewarded fork designed to preserve community governance and continuity for users.

## Breaking Away

The Valkey team immediately set its priorities:

* Preserve core processes and behaviors so users would experience continuity.
* Build a strong, neutral governance structure.
* Keep the community together.
* Move everything possible into the open

The Valkey crew adopted the [Linux Foundation’s](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) [Technical Steering Committee model](https://www.linuxfoundation.org/blog/blog/introducing-the-open-governance-network-model) because it was “very similar to what we had before” and engineering-driven from the start. But this time, the team vowed, decisions would be public, transparent and accountable.

One of the first changes was eliminating private meetings. “All the meetings are public,” Olson said. “If we ever see people trying to host private meetings, we will force them to cancel them and make them public.”

She emphasized a universal principle: “Default everything to open,” a change that “has worked really well for the project.”

Because Redis’s internal infrastructure had been invisible, the Valkey maintainers quickly discovered they lacked basic information. For example, they didn’t know how the binaries were built, where downstream distributions sourced Redis, and who maintained critical packages.

They were “very lucky,” Olson said, to meet a Fedora packager at an event, because without that connection, “we wouldn’t have really known … where to even start” in rebuilding downstream support.

To prevent repeating Redis’s opacity, the new team also made documentation and automation a priority. The alternative, Olson said, “was basically trying to document everything either explicitly or have automation around it that’s publicly available. Anyone can go look at the code … and get a relatively good answer pretty quickly”.

Automation allowed anyone, not just AWS engineers, to produce official releases. “Two releases happened from people, not from AWS,” she said proudly. “It’s all one-click mechanisms” now, with fixes visible and repairable through GitHub Actions and CI.

One of the major complaints about Redis pre-fork was its unpredictable release cadence. Olson described Redis 7.0.2, where the code cutoff happened in May but the release didn’t ship until August.

Valkey chose a six-month release cadence to start; the team members surprised themselves by exceeding expectations.  “Having predictability for your community is really important,” Oloson said. A regular cadence, she noted, helps users decide when and how to contribute fixes and features.

## Bumps in the Road

Not everything went smoothly. With openness came growing pains.

Because anyone could trigger releases, mistakes happened. One engineer “retagged” a release after forgetting a commit — breaking downstream systems like [Homebrew](https://brew.sh/). “Don’t let your community do that,” Olson said, with a laugh. The simple, correct fix would have been to create a new version and tag it properly.

Branch protections also proved vital. Several contributors accidentally pushed commits directly to production branches. “It’s not because we don’t trust people,” Olson said. “Everyone makes mistakes,” and protections exist to prevent accidents, not police intentions.

Communication tooling created its own challenges. The community had been using Slack, but many people disliked it, including Olson: “I hate it.”

So the maintainers tried Matrix and Discord. All those attempts to move failed. “Nobody moved,” Olson admitted. Despite Slack’s limitations, including message expiration and broken invite links, “we ended up slowly moving all back to Slack,” she said, because that’s where contributors already were.

## A Pre-Fork Checklist

If you see these warning signs coming in your corporate-driven open source project (opaque management, executives ignoring developers and customer requests), Olson and Luna Rojas suggested you should start considering a fork, so you won’t be caught flat-footed if your company tries to close down your open-source project.

Luna Rojas closed the session with a metaphor: “When you see the fork monster jumping out of your code base, you don’t want to face it alone. You have the Linux Foundation to be there with you to help you build a community-owned project.”

He emphasized a clear checklist for any project considering a fork:

* “Start drafting a charter now.”
* “Source control hygiene — try to be safe while protecting branches and tags.”
* “Keep your community together … doesn’t matter where they are.”
* “Document everything.”
* And always support downstream maintainers — the “unsung heroes” who make software usable across the world’s distributions.

Forking may be a last resort, but as the Valkey team showed, when the warning storm clouds gather and the governance no longer serves the community, a fork can be the healthiest and most sustainable path forward.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)