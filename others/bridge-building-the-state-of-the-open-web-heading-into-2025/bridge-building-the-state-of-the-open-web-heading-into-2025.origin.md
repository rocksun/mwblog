# Bridge Building: The State of the Open Web Heading Into 2025
![Featued image for: Bridge Building: The State of the Open Web Heading Into 2025](https://cdn.thenewstack.io/media/2024/12/6e1ccba1-red-morley-hewitt-c5xkmrtmvao-unsplashb-1024x576.jpg)
“We build bridges, not walls.” That statement comes from a new non-profit organization that launched yesterday called “[A New Social](https://www.anew.social/).” I spoke to the two founders, [Anuj Ahooja](https://www.linkedin.com/in/anujahooja/) and [Ryan Barrett](https://github.com/snarfed), to discuss where the open web is at now, its potential for massive growth in 2025, and how their new organization plans to help.

*A New Social* is built around Barrett’s product, [Bridgy Fed](https://fed.brid.gy/), which enables you to connect together your website, fediverse account and Bluesky account. As it says on the tin, “You can use it [Bridgy Fed] to make your profile on one [account] visible in another, follow people, see their posts, and reply and like and repost them.”
To my mind, Bridgy Fed is the perfect representation of the [state of the Open Web](https://thenewstack.io/the-state-of-the-open-web-3-takeaways-heading-into-2024/) as we close out 2024. It’s both a practical solution to an otherwise difficult problem (there are too many social networks and none of them talk to each other), but it’s also not without its own problems (Bridgy Fed is rather geeky and has some limitations).

To illustrate what Bridgy Fed enables, see the image below of my Mastodon account as viewed in the Bluesky website. Note the handle, which I’ve highlighted, indicating that a third party (Bridgy Fed) is making this cross-connection possible.

There are some limitations to the Bridgy Fed approach. For instance, Bluesky allows less text in its biography and posts than Mastodon (hence the “[…]” in the above screenshot). However, given that these are two entirely different protocols — [AT Protocol for Bluesky](https://thenewstack.io/blueskys-at-protocol-pros-and-cons-for-developers/) and [ActivityPub for Mastodon](https://thenewstack.io/devs-are-excited-by-activitypub-open-protocol-for-mastodon/) — this is as good as it gets for cross-connection between social networks. And it’s significantly better than what walled garden networks like X and Facebook allow (i.e. zero interconnectivity).

Incidentally, it’s [technically possible](https://tomkahe.com/@tom/113595942585497989) to at least partially bridge a Threads account to Bluesky. But it’s a work in progress: “I’m actively working on interop with the Threads people right now,” [wrote Barrett](https://www.threads.net/@shnarfed/post/DDKwt5NSS-c) earlier this month.

## Does Big Tech Play Well With Open Web?
Speaking of Threads, it’s been interesting to watch how the 800-pound gorillas of the internet have — or haven’t — shown support for the open web this year. Meta’s Threads has been both [a threat and an opportunity](https://thenewstack.io/threads-adopting-activitypub-makes-sense-but-wont-be-easy/) for open web proponents. In March, Threads began federating with Mastodon, but it was only a one-way connection (and it wasn’t activated for EU residents). Mastodon users could follow Threads users, but the reverse wasn’t possible. That changed in early December, when Threads finally allowed its users [to follow Mastodon accounts](https://mastodon.social/@ricmac/113596089816652081). But even then, it was (and still is) limited two-way support — you cannot reply to a Mastodon account from within Threads, for example.

Meta is a member of the [Social Web Foundation](https://socialwebfoundation.org/) (SWF), a non-profit organization [launched in September](https://thenewstack.io/social-web-foundation-launched-how-in-is-w3c-on-fediverse/) by Evan Prodromou ([a co-creator of ActivityPub](https://thenewstack.io/the-creator-of-activitypub-on-whats-next-for-the-fediverse/)), Mallory Knodel and Tom Coates. The SWF is very much focused on ActivityPub — and Prodromou, in particular, has not been shy to voice his concerns about Bluesky. So I asked Ahooja and Barrett how A New Social will work with SWF and, indeed, Meta.

“We’re going to be in a constant conversation with the SWF, with Bluesky, Meta, all of these folks.”

– Anuj Ahooja, CEO, A New Social
“We’re going to be in a constant conversation with the SWF, with Bluesky, Meta, all of these folks,” said Ahooja. In regards to SWF specifically, he noted that “our partnership with them is, if they’re building something for ActivityPub — if there’s something that’s in the pipeline [and] they’re actively developing it — how can we make sure that when that ‘new version’ of ActivityPub launches, or new features of ActivityPub launch, how do we make sure that we’re ahead of it and [that] Bridgy Fed is ready to go with that integration.”

In A New Social’s [announcement post](https://www.anew.social/hello-social-web/), Prodromou himself is quoted as saying, “A New Social provides essential infrastructure that helps people connect across platform boundaries.”

![Tom Gauld](https://cdn.thenewstack.io/media/2024/12/f6f43764-mastodon-bridgy-example.jpg)
![Tom Gauld](https://cdn.thenewstack.io/media/2024/12/f6f43764-mastodon-bridgy-example.jpg)
Cartoonist Tom Gauld has over 1,200 followers on Mastodon, thanks to Bridgy Fed, despite Gauld not actually using Mastodon.

Despite the words of support, there is an ongoing tension between all the different decentralized web products — between Mastodon and Bluesky, Threads and Bluesky, and even Mastodon and Threads (which are partners in SWF). In the days before Meta turned on its limited two-way federation with Mastodon, there was a debate in the comments of [a Mastodon post I wrote](https://mastodon.social/@ricmac/113566660783143714) about whether Threads was a part of the fediverse at that time — I argued no, Evan Prodromou said yes. Then Mastodon creator and leader Eugen Rochko [jumped in](https://mastodon.social/@Gargron/113566922060731761):

“I think a fair litmus test for whether something is a fediverse app would be if, for moderation reasons, none withstanding, you could follow your cosocial.ca account from it and vice versa. This is true for Mastodon and true for Flipboard, but it is not currently true for Threads.”

That debate was made somewhat moot several days later when Threads finally allowed its users to follow Mastodon users (albeit with limitations). But the point is, these are the kinds of inter-network tensions that have characterized the open web in 2024 — and are likely to continue into 2025.

## Bridges and Switzerland
I suggested to Ahooja and Barrett that their new organization will be kind of like Switzerland in this emerging decentralized social media landscape. Ahooja agreed.

“So for us, it’s very important to not be just ActivityPub or just AT [Protocol], or just both of those,” he said. “Long term, we want to see […] what are other protocols doing that are innovative, and is this worth investing in and bringing into the bridge as well? Like, this doesn’t have to just be ActivityPub [and] AT long term. We want this to be: where are the users, and how do we make sure that those users are being bridged over in the right way?”

“A big focus for probably the first year or so is education and outreach, improving UX [on Bridgy Fed], that kind of thing.”

– Ryan Barrett, CTO, A New Social
Bridgy Fed currently has over 60,000 users. So it’s very much a niche product — and few people are relying on the bridge to stick with just one account. I asked Barrett what the plans are for introducing Bridgy Fed to mainstream users.

“To some degree […] bridges will always be a bit awkward,” he replied. “They’ll never have perfect feature parity across different networks because different networks just do different things. […] But yeah, a big focus for probably the first year or so is education and outreach, improving UX, that kind of thing.”

## Open Web Predictions for 2025
Finally, I asked the guys what they predict for the open web in 2025?

Barrett thinks fragmentation in social media will continue into the new year. “But I think in a lot of ways that is good,” he added, “because we were much too stagnant, and there was not enough experimentation and evolution and trying different things. And so I kind of love that — and part of why I built and run Bridgy Fed [and am] really excited to work on pushing it forward more with this [organization], is I want to see a lot of those wild swings in all different directions.”

Ahooja agrees that fragmentation will continue next year, although he hopes Bridgy Fed will alleviate some of the friction. He also thinks there will be an expansion of the open web from microblogging to other types of online content.

“Right now, a lot of the focus is on these microblogging platforms,” he said. “There’s already a bit more focus on how do we get long-form into these [open] spaces? People are considering better ways to do media. I think videos are the super-hairy end game for the [decentralized] networks; it’s a very tough problem to solve.”

Ahooja hopes that once these other forms of content coalesce around open networks, then together these open web products will become big enough to challenge the centralized platforms.

But we’re not there yet, so let’s get to building (and using) those bridges.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)