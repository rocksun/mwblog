Enough is enough. [Daniel Stenberg](https://www.linkedin.com/in/danielstenberg/), lead developer and founder of [cURL](https://curl.se/), the popular, open source internet file transfer protocol, is [closing down cURL’s bug bounty program](https://github.com/curl/curl/pull/20312) at the end of January.

Why? Because cURL’s maintainers are being buried in AI slop. In an interview conducted over Mastodon, Stenberg told The New Stack, “It is our attempt to remove the incentives for submitting made-up lies. The submission quality has plummeted; not only are lots of the submissions plain slop, but the ones that aren’t obviously AI also seem to a high degree be worse (possibly because they, too, are AI but just hidden better). We need to do something to prevent us from drowning.”

## The impact of AI slop on open source security

He’s not the only one who’s sick and tired of AI slop bug reports. [Viktor Petersson](https://uk.linkedin.com/in/vpetersson), founder of [sbomify](https://sbomify.com/) and co-founder of [Screenly](https://www.screenly.io/), was the first person to spread the news of cURL’s change in a LinkedIn post, wrote, “We at Screenly are probably only seeing a fraction of the amount that curl gets, but the [amount of AI slop that the bug bounty is very taxing on human reviewers](https://www.linkedin.com/feed/update/urn:li:activity:7419042849993682945/).” Amen.

Stenberg continued, “The plan is to close it down [at the] end of January, so there will be more messaging about it from the project probably next week. It also times nicely with my talk about open source security and AI on [FOSDEM](https://fosdem.org/) that weekend.”

This move comes as no surprise. Stenberg has been the most vocal opponent of indiscriminate use of AI bug reports for some time now. In May 2025, he had [complained about a flood of “AI slop” bug report](https://thenewstack.io/curl-fights-a-flood-of-ai-generated-bug-reports-from-hackerone/)s from the bug bounty site [HackerOne](https://www.hackerone.com/). He’d said, on LinkedIn, “We now [ban every reporter INSTANTLY who submits reports we deem AI slop](https://www.linkedin.com/posts/danielstenberg_hackerone-curl-activity-7324820893862363136-glb1/). A threshold has been reached. We are effectively being DDoSed. If we could, we would charge them for this waste of our time. We still have not seen a single valid security report done with AI help.”

## Distinguishing between AI slop and effective AI-assisted bug finding

That’s not to say, however, that Stenberg rejects using AI to find bugs. He doesn’t. In September 2025, for example, he praised Joshua Rogers on Mastodon for sending “[us a \*massive\* list of potential issues in #curl](https://mastodon.social/@bagder/115241241075258997) that he found using his set of AI-assisted tools. Code analyzer style nits all over. Mostly smaller bugs, but still bugs, and there could be one or two actual security flaws in there. Actually, truly awesome findings.”

You see, Stenberg’s problem isn’t with AI per se; it’s how lazy people are using AI thoughtlessly to look for a bounty check or a reputation as a security researcher.

Mind you, if you do find an honest-to-goodness bug, with or without AI help, the cURL maintainers still want to know about it. But, if you do use AI, you must follow [cURL’s AI usage rules](https://curl.se/dev/contribute.htm). That is not optional. If you don’t obey them, you won’t be contributing to cURL. Considering how buried the cURL maintainers are by AI slop, it’s not like you can blame them for taking such a strict stance. I would too in their shoes.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)