In an article [introducing GPT‑5 to developers](https://openai.com/index/introducing-gpt-5-for-developers/), OpenAI claimed that the new model “excels at front-end coding, beating OpenAI o3 at frontend web development 70% of the time in internal testing.” Romain Huet, OpenAI’s head of developer experience, [added on X](https://x.com/romainhuet/status/1953964802432500186) that GPT-5 is “astonishingly good at frontend development.” There was also support from well-known frontend infrastructure companies, such as Vercel, which calls GPT-5 “the best frontend AI model.”

But, as always on the internet, your mileage may vary. Including, it seems, from people OpenAI used to help promote the GPT-5 launch. Theo Browne, a well-known YouTube influencer, was among the developers featured in [one of OpenAI’s launch day videos](https://x.com/OpenAIDevs/status/1953535155789865423). Browne initially loved GPT-5, even saying that Claude Sonnet and other competitors “[stopped being relevant today](https://x.com/theo/status/1953516806104056096)” because of GPT-5’s coding prowess. However, today he did a complete 180. He’s now posted a video entitled “[I was wrong about GPT-5](https://www.youtube.com/watch?v=k68ie2GcEc4).” In the video, Browne claims that “the experience I’m having now using GPT-5 is significantly worse than the experience I had when I was testing it before.” He [added on X](https://x.com/theo/status/1955766271083209064), “gpt-5 is nowhere near as good in Cursor as it was when I was using it a few weeks ago.”

[![Theo Browne's mea culpa about GPT-5.](https://cdn.thenewstack.io/media/2025/08/fce309f1-gpt5-theo.jpg)](https://cdn.thenewstack.io/media/2025/08/fce309f1-gpt5-theo.jpg)

Theo Browne’s mea culpa about GPT-5.

For other people not employed by or affiliated with OpenAI, the experience of using GPT-5 for coding also hasn’t necessarily been positive. One GitHub Copilot user [complained](https://github.com/orgs/community/discussions/168107#discussioncomment-14073879) that GPT-5 in GitHub Copilot Pro “gives extremely weak summaries or explanations of what it’s doing” and overall has found it “extremely underwhelming and disappointing.” He added that Claude Sonnet 4 is “far superior.”

AI engineering expert Shawn Wang (a.k.a. swyx) ran [a vibe-check poll](https://x.com/swyx/status/1953619552581169543) on X the day after GPT-5’s launch, and over 40% said it was “meh” or “slop.” That’s not scientific, of course, but it does indicate that OpenAI’s publicity blitz presented an overly positive picture of GPT-5’s coding abilities. (Wang, by the way, was another developer featured by OpenAI in its launch day programming.)

[![Swyx poll](https://cdn.thenewstack.io/media/2025/08/20db0cb2-screenshot-2025-08-14-at-11.48.57.png)](https://cdn.thenewstack.io/media/2025/08/20db0cb2-screenshot-2025-08-14-at-11.48.57.png)

There were some amusing reactions, too. On X, AI developer Kevin Kern [joked](https://x.com/kregenrek/status/1953507608456831029) about GPT-5’s propensity for the color purple — implying that the frontend designs being churned out by GPT-5 are not that original.

[![purple problem](https://cdn.thenewstack.io/media/2025/08/6ef1d850-screenshot-2025-08-14-at-12.17.17.png)](https://cdn.thenewstack.io/media/2025/08/6ef1d850-screenshot-2025-08-14-at-12.17.17.png)

## React or No React? You Choose!

In terms of frontend development specifically, OpenAI seems to be throwing its promotional partner Vercel a bone in its “cookbook” [prompting guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_frontend). It recommends Next.js (TypeScript), React and HTML as the frameworks to use with GPT-5.

Many budding AI developers will no doubt ask GPT-5 to help them create React apps. Here’s [an example by Brice Challamel](https://www.linkedin.com/posts/bricechallamel_ai-gpt5-gpt5-activity-7359280792671252480-tB1D?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAAJc5gB1iiLngl5c8J7iqyPa5uC2oX1J-U), whose day job is head of AI products and innovation at Moderna. Challamel decided to build a “cultural discovery” app. “GPT-5 helped me go from concept to a working React prototype inside ChatGPT,” he wrote, “and then generate the full stack code package and a prompt to deploy in Lovable.”

> “GPT-5 helped me go from concept to a working React prototype inside ChatGPT.”  
> **– Brice Challamel, head of AI products and innovation, Moderna**

But one intriguing possibility with GPT-5 is that it may also enable developers to *route around* React. At least that’s the takeaway I took from [a GPT-5 writeup](https://www.latent.space/p/gpt-5-review) by Ben Hylak and Alexis Gauba, co-founders of an AI startup called Raindrop (Hylak joined Browne and Swyx on the OpenAI developer couch on launch day). In his pre-launch tests, Hylak discovered he could create a website with GPT-5 that used “no React, no bundling, no frameworks.” Just HTML, CSS and JavaScript.

The pair were also impressed by GPT-5’s ability to create websites in one go. Or as Hylak put it, “GPT-5 one shots things like no model I’ve ever seen before.”

This raises an interesting question: Will frontend developers need to use React and its frameworks as a prop for their work going forward, when GPT-5 (and competing products, like Claude Code) can develop a skeleton app by just using the underlying web platform? Because that’s basically what GPT-5 is bringing to the table: the ability to “scaffold” a web application for human developers, who can then build on that scaffold — polish it up and launch the app — in their IDEs or in tools like Cursor or Lovable.

> What if we no longer need React as a prop?

Put another way: For many of the current generation of frontend developers, React and similar frameworks have been a constant prop in their careers. Many young frontend devs don’t even know of [a world without React frameworks](https://thenewstack.io/why-react-is-no-longer-the-undisputed-champion-of-javascript/). But what if we no longer need React as a prop?

OK, admittedly, it’ll be because we’re adopting a new prop, in the form of AI. But the point is, web browsers have now reached a [level of sophistication](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/) where you can build complex websites and web applications [just using HTML, CSS and JavaScript](https://thenewstack.io/how-microsoft-edge-is-replacing-react-with-web-components/). GPT-5 might’ve just proven to many developers that React and frameworks aren’t always necessary these days (of course, this depends on whether GPT-5 is in fact as good as OpenAI claims — which is debatable at this point).

## Other GPT-5 Notes for Devs

As noted above, we’ve seen mixed reviews so far for GPT-5 as a frontend tool. But it will take time for frontend devs to properly evaluate it, especially compared to Claude Sonnet. But as Theo Browne commented on, it has become clear over the past week that there is variance in the different models of GPT-5, and how they integrate into certain tools.

The GitHub Pilot user quoted above may have been using a less powerful version of GPT-5, just as [Hylak complains here](https://x.com/benhylak/status/1955460174703104290) about what Cursor calls “gpt-5”.

[![Hylak tweet re Cursor and GPT-5](https://cdn.thenewstack.io/media/2025/08/ab069e71-screenshot-2025-08-14-at-12.23.29.png)](https://cdn.thenewstack.io/media/2025/08/ab069e71-screenshot-2025-08-14-at-12.23.29.png)

As Hylak explains further into that X thread, “gpt-5-high is what i was testing pre-release” (in other words, OpenAI gave him the top-end version to test). It seems that frontend coding results are likely to be less compelling with non-premium versions of GPT-5.

It’s also worth pointing out that coding LLMs all seem to have a different flavor — or “coding personality” as the code security company [Sonar](https://www.sonarsource.com/%20?utm_content=inline+mention) put it in [a new study](https://www.sonarsource.com/resources/the-coding-personalities-of-leading-llms/) released this week. Sonar’s study called GPT-4o “The efficient generalist” and Claude Sonnet 4 “The senior architect.”

[![Sonar coding personalities](https://cdn.thenewstack.io/media/2025/08/fb8ede7f-screenshot-2025-08-14-at-12.20.52.png)](https://cdn.thenewstack.io/media/2025/08/fb8ede7f-screenshot-2025-08-14-at-12.20.52.png)

It’s too early to say what coding personality GPT-5 has, but this is something that frontend developers will be keen to track going forward.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)