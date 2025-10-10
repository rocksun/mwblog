It’s now almost three years since Elon Musk [acquired Twitter](https://thenewstack.io/twitter-turmoil-we-need-an-open-protocol-for-public-discourse/). Since then the fediverse — a collection of decentralized web products [powered by the W3C standard, ActivityPub](https://thenewstack.io/devs-are-excited-by-activitypub-open-protocol-for-mastodon/) — has continued to grow. [Bluesky’s AT Protocol](https://thenewstack.io/blueskys-at-protocol-pros-and-cons-for-developers/) also has some intriguing new apps. But overall, app development on these protocols is still in a nascent phase. Let’s be frank here: the open social web hasn’t gotten the developer attention it deserves.

This week, I attended the latest edition of [FediForum](https://fediforum.org/), a two-day virtual event, to find out the latest in open social web development.

## The ‘Start Small’ Philosophy of the Open Social Web

The FediForum keynote was delivered by [Ben Werdmuller](https://www.linkedin.com/in/benwerd/), senior director of technology at ProPublica. One of his core themes was “everything big started small.” He referenced how Twitter started as an SMS group messaging service and was inspired by an activism tool called TextMob, which emerged during the 2004 U.S. Democratic and Republican conventions. The idea was to let protest organizers and participants send group text messages via SMS rapidly and securely.

“All of our microblogging tools have this lineage,” Werdmuller said. “Short messages designed for a specific group of people and limited in length for a specific reason, that was an outcome of *that* use case. A specific use case led to a working prototype that led to a wider application. And that pattern is repeated again and again.”

> “…for the Open Social Web to thrive, we need to go back to real communities with real world use cases, and solve their problems better than anything else.”  
> **– Ben Werdmuller, senior director of technology at ProPublica**

That philosophy can be applied more widely to other types of fediverse applications, Werdmuller implied.

“So for the Open Social Web to thrive, we need to go back to real communities with real world use cases, and solve their problems better than anything else — not the needs, necessarily, of individuals within them, but of the interconnected communities themselves.”

## Emerging Fediverse Products and Announcements

Most people [know about Mastodon](https://thenewstack.io/what-its-like-to-run-a-mastodon-server-in-the-musk-twitter-era/) by now, and possibly also about the half-baked adoption of ActivityPub [by Meta’s Threads](https://thenewstack.io/threads-adopting-activitypub-makes-sense-but-wont-be-easy/). If you’re of a geek persuasion, you may also have heard of PeerTube for video, Pixelfed for photos, and Lemmy for social news and link aggregation. But what else is new on the open social web?

At this week’s FediForum, there were some promising announcements.

### AltStore: An Alternative App Store Joins the Fediverse

One was the launch of [AltStore](https://altstore.io/) into the fediverse. AltStore, as the name implies, is an alternative app store for iOS — put another way, it enables “sideloading” of iOS apps. It’s currently only available in Europe, but the company [plans to launch](https://rileytestut.com/blog/2025/10/07/evolving-altstore-pal/) in Japan, Brazil, and Australia “before the end of the year, with the UK to follow in 2026.”

AltStore’s founding CEO, Riley Testut, demonstrated the new fediverse integration at FediForum. Basically, each AltStore source receives its own ActivityPub account, via [the AltStore Mastodon server](https://explore.alt.store/), which can then be followed by any other open social web account — including on Bluesky, via the bridging technology Bridgy Fed.

“It’s a public feed of all the stuff you can see in AltStore, so you don’t need to be in the app anymore to see what’s going on,” explained Testut.

[![AltStore](https://cdn.thenewstack.io/media/2025/10/9536d507-altstore-mastodon-oct25.jpg)](https://cdn.thenewstack.io/media/2025/10/9536d507-altstore-mastodon-oct25.jpg)

AltStore on the fediverse.

The highest profile app on AltStore currently is Fortnite; owned by Epic Games, which has been battling Apple in court over the 30% iOS App Store commission on in-app purchases.

The Fortnite feed includes updates to its app on AltStore, news items, and anything else Epic Games wants to share with the fediverse.

After Testut’s 5-minute presentation, FediForum co-host Johannes Ernst noted that it is a good example of how apps that *don’t resemble Twitter* can join the fediverse. “We could do so many more things that are social in nature, such as social commerce,” Ernst said.

### Bridgy Fed: Connecting Mastodon and Bluesky

I mentioned Bridgy Fed above — and the people behind it also had news to share at FediForum. [Bridgy Fed](https://fed.brid.gy/) basically allows you to syndicate your Mastodon account to Bluesky, and vice versa. Back in August, *A New Social* — the non-profit organization behind Bridgy Fed — launched a product called [Bounce](https://blog.anew.social/bounce-beta-now-live/), which helped Bluesky users to migrate to Mastodon using Bridgy Fed. At FediForum, it announced the ability to do the opposite migration: [from Mastodon to Bluesky](https://blog.anew.social/bounce-mastodon-to-bluesky/) (technically, any AT Protocol account — so this includes BlackSky, a popular BlueSky server for the black community).

As co-founder Anuj Ahooja said at FediForum, “we do this by migrating your Mastodon account to Bridgy Fed and letting you keep all of your followers and all of your bridge follows.”

This news was perhaps delivered at a suboptimal time, given the recent [controversy over moderation](https://techcrunch.com/2025/10/05/waffles-eat-bluesky/) at Bluesky — which seems to have led to a spike in Mastodon sign-ups (or at least a spike in “let’s not drive new users away again” posts by existing Mastodon users).

### Frequency: A Privacy-Focused Photo-Sharing App

Another new application that caught my attention at FediForum was [Frequency](https://frequency.app/about), a photo-sharing app with an emphasis on privacy and no algorithmic engagement bait. It was developed by Jesse Karmani, who presented at FediForum. She described Frequency as “a federated photo and video sharing app that lets you share your personal life with your friends and family.”

[![Frequency app](https://cdn.thenewstack.io/media/2025/10/80e494a2-frequency-app-screenshots.jpg)](https://cdn.thenewstack.io/media/2025/10/80e494a2-frequency-app-screenshots.jpg)

Frequency app

In my tests, I was able to sign up to an account (there is a small monthly or yearly fee), follow that account from Mastodon (it requires approval from the Frequency account), post a photo, and then see that photo in Mastodon as a followers-only post. The focus on privacy differentiates Frequency from the public-by-default setting of your typical microblogging app — or even the current leading fediverse photo-sharing app, Pixelfed.

### CrowdBucks: A Monetization Platform for Creators

Speaking of paying a small amount of money, [CrowdBucks](https://crowdbucks.fund/) is a new project hoping to bring that to creators on the fediverse. It’s described as “a Fediverse-native crowd-funding, tipping, payments, and membership platform.”

Founder Charles Iliya Krempeaux (a.k.a. reiver) spoke about the product at FediForum. The motivation, he explained, is to help “make the fediverse last.”

“Part of that [is] I think that people need to be able to support themselves in the fediverse. This includes the sysops that run the servers, developers that create the software, creators, and others.”

[![CrowdBucks](https://cdn.thenewstack.io/media/2025/10/bfd1b64e-70de82f4bdec5f0f.png)](https://cdn.thenewstack.io/media/2025/10/bfd1b64e-70de82f4bdec5f0f.png)

CrowdBucks user interface.

## The Developer Opportunity in the Fediverse

Similar to the fediverse products I wrote about at [the previous FediForum in June](https://thenewstack.io/bringing-joy-back-to-the-web-fediverse-vs-centralized-apps/), the products mentioned above — AltStore, Bounce, Frequency, CrowdBucks — are still early-stage and (in some cases) difficult for ‘normies’ to adopt. But that shouldn’t distract from the opportunity here: to build new ways to connect communities, in a privacy-conscious way and with an open mindset in line with the ethos of the web. Remember that the web was designed by Tim Berners-Lee to be an open network, not one controlled by corporations.

The applications being built on the open social web may be small right now, but they’re bringing decentralization and true freedom back to the internet. Everything big started small, to use Werdmuller’s phrase.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)