# Developers: Mastodon and Bluesky Want Your Twitter Bots
![Featued image for: Developers: Mastodon and Bluesky Want Your Twitter Bots](https://cdn.thenewstack.io/media/2024/11/cdc1b941-bots-nov24-1024x576.jpg)
In early October 2022, I published one of the worst-timed articles of my career: [Developers: Twitter Wants Your Bots](https://thenewstack.io/developers-twitter-wants-your-bots-and-other-read-write-apps/). It was an interview with [Amir Shevat](https://www.linkedin.com/in/amirshevat/), then head of the developer platform at Twitter, and it was about how third-party developers were being welcomed back to Twitter’s platform.

About three weeks later, Elon Musk acquired Twitter. Shortly after that, [Shevat was fired](https://thenewstack.io/twitter-turmoil-we-need-an-open-protocol-for-public-discourse/), along with all of his team. Needless to say, X (the company formerly known as Twitter) no longer wants your bots. But there is good news. Mastodon and Bluesky, the primary alternatives to X from a third-party developer perspective, would welcome your bots — and any other apps, for that matter.

By bots, I mean automated accounts that use the platform’s API to publish, typically on a schedule defined by the developer. They’re a good way to get to know the API and app development capabilities of a social media platform.

## Running Bots on Mastodon and Bluesky
To host a bot on Mastodon, you can either use a server that specializes in bots — although the only one I found currently open for registrations is [mastodon.bots](https://mastodon.bot/about) — or you can just use one of the general-purpose instances. One of the bots I follow, [never obsolete](https://mastodon.social/@256), runs on mastodon.social, the primary Mastodon server. (More on specialized bot servers in a minute!)

Many Mastodon developers use Glitch, [a free online web app builder](https://thenewstack.io/developers-can-now-discover-and-curate-open-web-apps-on-glitch/), to run their bots. For example, [Stefan Bohacek](https://stefanbohacek.com/), a bot developer who also runs the resource site [Botwiki](http://botwiki), has a collection of 54 active Mastodon bots [running on Glitch](https://stefans-creative-bots.glitch.me/). However, there are alternative ways to create a bot, such as via [a Python app](https://shkspr.mobi/blog/2018/08/easy-guide-to-building-mastodon-bots/) or using [GitHub Actions](https://til.simonwillison.net/mastodon/mastodon-bots-github-actions).

As for dealing with the [Mastodon API](https://docs.joinmastodon.org/client/intro/), it’s easy, says Bohacek.

“Specifically with Mastodon, creating a bot account is super easy,” [he wrote](https://stefanbohacek.online/@stefan/113373504557329086) in response to my query on Mastodon. “Just like setting up a regular account, you don’t need to verify your phone number, which has been a requirement on Twitter. The Mastodon API is also very easy to use and pretty well documented, at least for my own needs. And I like that you can mark your account as “automated” on its profile page.”

If you’re interested in creating a Mastodon bot, you can find [more resources on Botwiki](https://botwiki.org/resources/fediverse-bots/).

So what about Bluesky? You can create a bot there using the [AT Protocol SDK](https://atproto.blue/en/latest/). Bluesky even helpfully gives you [a code template](https://docs.bsky.app/docs/starter-templates/bots) for creating bots (it’s in TypeScript), and it recommends Heroku or Fly.io to deploy it.

As of the time of writing, there are 21 bots listed in Bluesky’s [community showcase](https://docs.bsky.app/showcase/?tags=bot). But one I enjoy that isn’t listed is [Retro Computers](https://bsky.app/profile/retrocomps.bsky.social), which was actually inspired by *never obsolete* on Mastodon. Retro Computers uses a [Python](https://thenewstack.io/what-is-python/) script to generate its “semi-automated” posts.

## Mastodon: Stable Bot Platform, but With Risks
Since Mastodon has been around longer than Bluesky, it has built up a solid ecosystem around bots. Some bot developers have been active on Mastodon since 2017. One of those is [Darius Kazemi](https://tinysubversions.com/), who [I interviewed back in May 2022](https://thenewstack.io/why-developers-should-experiment-with-the-fediverse/). Kazemi had previously been a prolific creator of bots on Twitter but switched to the fediverse in 2017 after a crackdown on bots by Twitter. “And then they also changed all their APIs,” Kazemi explained, “which are the programmatic interface for how a bot talks to Twitter. So they changed those without really any warning, and everything broke.”

So even well before Elon Musk arrived, Twitter had messed up on bot development. Like Bohacek, Kazemi now hosts his Mastodon bots on Glitch.

Although bot development on Mastodon has been happening for years now, there are risks associated with the server you choose. Until very recently, the leading Mastodon server that specialized in bots was botsin.space. But it just announced it will be closing in December.

The developer behind botsin.space, Colin Mitchell, outlined his reasons for closing it in [a blog post](https://muffinlabs.com/posts/2024/10/29/10-29-rip-botsin-space/). After explaining that he’s a tech professional (“server management is part of my job description”), he noted that his server expenses have been gradually increasing. It reached a kind of crisis point after the recent Mastodon upgrade — [Mastodon 4.3](https://blog.joinmastodon.org/2024/10/mastodon-4.3/) was released in October — which he said “caused a significant amount of performance degradation” for his service. Rather than “throw a lot of money into hardware,” he’s instead opted to gracefully shutter botsin.space.

None of this is an indictment of the Mastodon software, but it is a cold hard reality than many [people who run Mastodon instances](https://thenewstack.io/what-its-like-to-run-a-mastodon-server-in-the-musk-twitter-era/) do so at a loss — so these servers are more at risk of shutting down than platforms like Threads (owned by Meta) or a VC-funded company like Bluesky.

## Bluesky’s Developer Risks
But the risks at Bluesky are just as stark, if not more so. As I noted in my previous post, [Bluesky is not very decentralized](https://thenewstack.io/blueskys-at-protocol-pros-and-cons-for-developers/) at the present time — roughly 99% of its infrastructure is under the direct control of Bluesky, the company. What if Bluesky gets sold (as happened with Twitter)? Or what if it decides to change the rules for developers (as also happened with Twitter)?

Since I published that article, a more in-depth critique of Bluesky has emerged. Gavin Anderegg, a freelance software developer, [explained](https://anderegg.ca/2024/11/15/maybe-bluesky-has-won) that a key part of Bluesky’s infrastructure — a [Relay](https://docs.bsky.app/docs/advanced-guides/federation-architecture#relay), which crawls data and outputs it into “one big stream” — is extremely expensive for third-party developers to run. In other words, devs will likely have to use Bluesky’s Relay for the short-to-medium term. He also pointed out that the DID:PLC (a cryptographic public ledger of credentials, used to manage identity) and DMs are also “directly under Bluesky’s control.” The money quote from Anderegg was this:

“Bluesky is slightly more decentralized than, say, Facebook — but not by much. Yes, you can host your own data. Yes, you can scrape all of the content on the network. But you can’t do anything with it unless you’re attached to the Bluesky service. I believe this will change with time, but it will be prohibitively expensive and we’re not there yet.”

## Conclusion
I think both Mastodon and Bluesky are worth experimenting with as platforms for third-party development, although obviously, bear in mind the above risks. But since bots are relatively low-risk as an application type (it’s not as if you’re building a large app like TweetDeck), it’s a good way to kick the tires on a new social platform.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)