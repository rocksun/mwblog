# FediForum Showcases New Fediverse Apps and Developer Network
![Featued image for: FediForum Showcases New Fediverse Apps and Developer Network](https://cdn.thenewstack.io/media/2024/03/823e38fd-agnieszka-ziomek-ucyx_xn8y1i-unsplash-1024x768.jpg)
This week I attended
[FediForum](https://fediforum.org/), a two-day virtual event about fediverse technologies. The [fediverse](https://thenewstack.io/the-fediverse-points-to-our-social-media-future-post-musk/) is a decentralized network of apps that connect together via the W3C [ActivityPub protocol](https://thenewstack.io/devs-are-excited-by-activitypub-open-protocol-for-mastodon/). Its biggest and most well-known app is Mastodon, the microblogging platform that Meta’s Threads is currently in the process of [interconnecting with](https://thenewstack.io/threads-adopting-activitypub-makes-sense-but-wont-be-easy/) (via ActivityPub).
What FediForum showed this year, though, was that the fediverse encompasses many more applications than just Mastodon (and soon, Threads). I’ll discuss a few of the more promising apps/services in this article.
We’ll also look at the Fediverse Developer Network, a new network of enthusiastic “fedidevs” being organized by Andy Piper and several other active fediverse developers.
## Promising Fediverse Apps
Other than Mastodon, you may have already heard of Lemmy (a Reddit-type app), Pixelfed (photo-sharing) and PeerTube (a YouTube clone). But in the 5-minute speed demo sessions that opened each of the two days at FediForum, I discovered a bunch of other very promising apps.
The demos on day one were rather overshadowed by Meta employee
[Peter Cottle’s demo](https://www.youtube.com/watch?v=XGEVy-CjBBg&t=1s) of how Threads is connecting to Mastodon. He noted that Threads users will have an option to turn on “fediverse sharing” in their settings, which includes a pop-up explaining what the fediverse is.
But I found it more interesting to check out the new applications being built. An example from day one was
[Newsmast](https://newsmast.org/), a topic-based news aggregator based on a fork of the Mastodon software. The team behind it is a non-profit organization whose goal is “harnessing the power of social media for good.”
In addition to Newsmast, the team is also building Patchwork, which presenter Michael Foster described as “an easy-to-use customizable onramp to the fediverse for organizations.” Using this technology, which is again based on Mastodon software, organizations can create a “community server” for their own topics.
Your mileage may vary on how well Newsmast curates various topics, but it’s good to see an attempt to create topic feeds for the fediverse.
While Newsmast is basically an extension of Mastodon, some of the new fediverse apps I saw at FediForum are building something brand new and untried before. An example is
[Emissary](https://emissary.social/), demonstrated on day two by Ben Pate from Colorado. Emissary isn’t yet publicly launched, but it’s described as “a standalone Fediverse server designed for end users, app creators, and hosting admins — that gives everyone powerful new ways to join the social web.”
In the demo, Pate showed how you could follow feeds from various open web protocols — ActivityPub, RSS, and IndieWeb formats like microformats and webmentions. What intrigued me was that it seemed to easily interconnect all these diverse, but open standard, protocols. It was like a feed reader that allowed you to follow people from Mastodon, Threads, Bluesky, blogs, etc.
Emissary has
[developer](https://emissary.dev/developers) appeal too. According to the [documentation](https://github.com/EmissarySocial/emissary?tab=readme-ov-file), developers can “create full-featured social apps that are easy to deploy and easy to maintain,” using a low-code environment based on “HTML templates and a JSON config file.” The open source tech stack is pretty interesting: Go, MongoDB, HTMX/Hyperscript.
Another project that caught my eye at FediForum was IFTAS FediCheck, a “Moderation-as-a-Service” tool demoed by
[Emelia Smith](https://hachyderm.io/@thisismissem). The service, which is still in development, will allow Mastodon server administrators to subscribe to “CARIADs” — Consensus Aggregated Retractable IFTAS Allowlist Denylist — and have them automatically maintained by IFTAS FediCheck. This promises to be a much-needed moderation service for [Mastodon administrators](https://thenewstack.io/what-its-like-to-run-a-mastodon-server-in-the-musk-twitter-era/), many of whom run instances on a part-time (and largely unpaid) basis.
“Being in-development, IFTAS FediCheck is Mastodon-only, but there are huge benefits to the broader fediverse network of applications, NodeBB included,” commented
[Julian Lam](https://mastodon.social/@julian@community.nodebb.org/112129270034316415), a co-founder of NodeBB (open source forum software).
## Fediverse Developer Network
Andy Piper, a UK developer, hosted a session on day two about the nascent Fediverse Developer Network. He began by comparing it to the Mozilla Developer Network (MDN).
“It’s kind of a one-stop shop for web standards, web APIs, things like that,” Piper said, regarding MDN. “And wouldn’t it be great if developers had a resource for building new services to integrate with the fediverse?” He noted that the fediverse is more than just ActivityPub, and mentioned ActivityStreams, HTTP signatures and Webfinger as other relevant technologies.
The Fediverse Developer Network aims to provide a resource library and offer guidance to developers. Aside from the technical aspects, another “core concept” of the group is simply to have other people to bounce ideas off.
The group has a
[website](https://fedidevs.org/), [GitHub project](https://github.com/fediverse-devnet), [Mastodon instance](https://mastodon.social/@fedidevs), and [a Matrix forum](https://matrix.to/#/#fediverse-developer-network:matrix.org) (similar to a Discord group).
## Mostly Positive Vibes at FediForum
Overall, the two-day FediForum showcased the enthusiasm of the growing fediverse community. I did sense a bit of unease amongst the community about Meta’s pending entry into the fediverse, but that aside there is a lot of excitement about the new applications and services being developed.
FediForum was organized by fediverse entrepreneur Johannes Ernst, unconference expert Kaliya Young, and event producer Jennifer Holmes. This was the team’s third event, following similar unconferences in March and September last year.
The pace of innovation is so fast, it’ll be fascinating to see what apps get built before the next FediForum event. As
[Ernst commented](https://mastodon.social/@J12t@social.coop/112124112942357119) on Mastodon, “Apparently FediForum is now a measure of time in the Fediverse.” [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)