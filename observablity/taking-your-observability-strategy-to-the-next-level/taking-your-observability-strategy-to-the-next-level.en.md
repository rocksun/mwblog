Observability strategy is a tricky concept. Everyone wants to talk about it, but nobody can agree on how they’re talking about it. Consequently, we end up talking past each other without even realizing it.

I like to think of this as a multifaceted spectrum, built up of trade-offs; You pick somewhere on a spectrum in a few different areas, and then you figure out how to optimize the trade-offs, and slowly your strategy emerges from there.

That works up to a point, but then you’ll hit a strategy cliff, usually around three years of implementation (or ~250 engineers). That strategy cliff is when having a single strategy breaks down and stops being sufficient.

It turns out that while you can split up a company into pre-product market fit (pre-PMF), small-to-medium business (SMB) and enterprise, you’re probably going to have all three of these paradigms existing in your company at the same time, regardless of company size. That can be quite confusing to work with.

But rather than splitting up into a million separate strategies, building a meta-strategy around observability can make this much easier to deal with. Let’s walk through how that can happen and what that looks like.

## Strategy? What Strategy?

Smaller companies tend to not have an observability strategy, and larger companies tend to want to improve their existing one. That would be one of the spectrums I mentioned earlier.

I find this a lot easier to explain in story form, which is why user journeys are so valuable to me. So let’s talk about a few company personas that we’ll sketch out briefly.

## The Pre-PMF Seed Startup

Picture this: You’ve raised a seed round. You have 12 months of runway. You have plans about what users need. You also have plans about your plans. You might even think you know who your users could be. Better yet, you’ve even built something.

Now what? Well … are users using it? Do they like it? Sure, you can email all of them, but there’s a difference between what they say and how they behave, and you’re going to need the [right data to see user behavior](https://thenewstack.io/the-case-for-user-focused-observability/). Your observability is probably going to look a lot more like user tracking and marketing funnel analysis than it is “hyper-optimize this endpoint to be 2% more efficient.”

And you know what? That’s fine! User journeys are super valuable here, but in a weird way: You don’t know the user journey, and you want to find it out. Typically, you’re only measuring them if you have a good idea of what they are, but pre-PMF? It could be anything.

If you’re thinking that this sounds like an [“unknown unknown”](https://thenewstack.io/the-4-evolutions-of-your-observability-journey/), you know, the type of thing observability is supposed to be amazing at approaching, you’re not wrong.

Translating that into the business impact, what really matters is whether you can figure out what that product market fit is, and [how it relates to your users](https://thenewstack.io/observability-is-stuck-in-the-past-your-users-arent/) and your revenue streams. Rather than observability being an afterthought, leaning into it and [integrating it with your user journeys](https://thenewstack.io/when-performance-is-product-bridging-the-gap/) can be the difference between thinking you have product-market fit and being able to observe when you hit product-market fit.

## Observability Check for My SMB Era

You found product-market fit. Revenue is growing. You have actual customers who will be angry if things break. Suddenly, you have problems you didn’t have six months ago. Congratulations! Condolences! Everything in between!

This is the pain zone for observability: Your main goal is to keep things from falling over. Everything is going to change every six months, and nothing is going to make sense. You’re going to be building systems faster than you can keep track of them, and you’re going to be duct taping stuff together so much that your eyes will glaze over.

Those user journeys of yours are going to start landing in an uncomfortable middle; you’re still not quite sure about them, but a lot of load-bearing revenue now lies on the personas you’ve built out. Unfortunately, the assurances you get with enterprise scale, enterprise purchase plans, tooling integration and conveniences of large companies with unlimited budgets are still going to seem so far away.

You still want to do more with less, and you want to focus on tool consolidation, but you’re in the uncomfortable spot of simultaneously knowing you have to spend money to make money and saying, “Haha, but what money, right?” Likewise, with your users, you definitely have them, but the confidence you have in how those user demographics have been split is probably going to feel like it varies from day to day.

If only you had a magic wand that you could wave, which would let you know which efforts to focus on. If only you could know those user journeys were driving revenue. If only you had a way to divine the levers of impact that let you maximize operational return on investment (ROI). If only you had … observability. But wait, not *that* observability. This observability looks way different than the observability you implemented two years ago.

Well, observability actually doesn’t look that different than it does now, does it?

You’re not exactly losing any of the capabilities you needed pre-PMF; you just have more things to care about and different trade-offs to make. Which means that your observability strategy can grow seamlessly from pre-PMF to the SMB era, assuming, of course, that you focused on transferrable skills and technology choices rather than punting operational knowledge until later.

So, even as you’ll likely focus less on adding new user journey experiments, because discovery is less important, they’re still going to be an essential part of your observability strategy. Reliability and cost efforts need similar things and pair well with user journeys, especially if you can correlate that data together.

## The O11y-Ship Enterprise

Congratulations! You’ve made it: You can officially say “at our scale” whenever a vendor starts hitting you up. It’s guaranteed to make your colleagues roll their eyes, and you’ll elicit a nervous chuckle from the vendor. Are you running a tool? Pffh, you’re running every tool, and many of them more than once. Your vendor might know more about how your company uses the tool than you do, and you’re the people that bought it in the first place. Those user journeys? Set in stone, baked, ossified; Entire departments exist because those user demographics are the shape they are. You could set your clock on the ability to detect user behavior that you’ve painstakingly curated.

Something interesting happens in this environment. Money changes shape. Rather than trying to reduce cost to an absolute minimum on a case-by-case basis, you start becoming very willing to spend large amounts of money to buy systemic improvements.

And when you’re in that stage, it does mean that tooling integration and catering to people outside the expert domain of tool usage become incredibly important. In addition, your faith in those user journeys and personas have grown to the point where you’re likely to dismiss most contrary experiences and user reports as outliers rather than as signals that your market research was flawed.

After all, in a startup, you can assume that anyone using a tool is probably interested in using that tool — you often don’t have a lot of pressure forcing you to use tools against your will in smaller companies. As for users, you can probably assume you don’t know them, or even if you do… The rule of startups is that “the only constant is change.”

Enterprises, on the other hand, experience mandatory tool consumption on a daily basis. As evidence of this, look no further than that ticketing system that has 37 mandatory fields to create the zillions of reporting charts for management needs. They also have a stickiness of users and a predictability of user behavior that makes it possible to build a foundational enterprise on top of that data. It’s not just a moat; it’s the life of the business.

Projects like [Weaver for OpenTelemetry](https://github.com/open-telemetry/weaver) become super important, whereas you’ll likely not care about them as much in smaller companies. Internal platforms, marketplace offerings and other consumption models of observability start making sense as well.

User journeys go from a discovery mechanism, to a profit mechanism, to a basic essential of life. The same goes for blueprints: They sound silly until you need to get tens of thousands of engineers to wrap their heads around a thing they don’t really care a whole lot about. All of the sudden, they become astonishingly necessary.

## Observability as a Meta-Strategy

Now, looking at these three sorts of company shapes, one thing that you’ll readily notice is that the main thing they have in common is that they don’t seem to have anything in common. Even if user journeys or observability or “understanding the unknown unknowns” feels constant, the reasons and motivations behind that are going to change. So you might be wondering to yourself how exactly you’re supposed to do this magical meta-strategy thing and solve all your observability problems with one strategy.

Rather than treating strategy as a static document, or treating it as a living one, have a strategy around your strategy and build that into observability. I like to think about the S-curve of technology adoption. Imagine an observability initiative, like “use OpenTelemetry” for example (another example could be “[implement user journeys](https://embrace.io/blog/user-journeys-walkthrough/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=observability-strategy)“, whatever that means for you). Every stage of the initiative will start slowly and have an exploration phase before it starts to click. Then it will start to get traction and accelerate through a growth phase as it starts to take hold. Finally, it plateaus as the initiative hits saturation in the company.

Now, imagine that every single observability initiative in your company has its own S-curve. Adding user journey tracking? That’s a curve. Implementing sampling? Another curve. Migrating to OpenTelemetry? Yet another curve. And these curves overlap, intersect and sometimes contradict each other.

Which means that any company is going to find itself with dozens of these S-curves, all overlapping, and you’ll drive yourself up the wall trying to figure out how to build a meta-strategy that handles all these different combinations of strategies to understand where your company is and what you should do.

So instead, I like to think of transitions between strategies. Focus on identifying what stage of a strategy you’re at and build your strategy around understanding how to transition from one stage to another. For example, how do we transition an initiative (or product) from pre-market fit to market fit? How do we transition from SMB to enterprise? Or how do we transition a project from “Oh, I need to use OpenTelemetry” to “Now we’re ready to implement user journeys.” Is that the order you go in? Do you do it in a different order? Why?

If you think of the strategy as understanding inflection points rather than mapping out the combinations, you’ll help prevent yourself from running into the trap of needing to write dozens of strategies to cover every random combination of scenarios. This becomes particularly important when you realize that you’re going to end up with dozens, if not hundreds, of these S-curves all interlapping together.

It’s going to be impossible to predict when you’ll run into certain combinations of strategy inputs, so rather than predicting the future, adapt to the present. After all, building that operational adaptability is one of the strong points of observability. Your ability to do this in your strategy is part of an indication that you are maturing in your observability practice.

## Strategy Is Embracing the Tangled Layers

There’s a huge temptation to think of taking a complex domain and attempting to simplify it by removing the complexity. The problem is that true complexity cannot be removed; it can only be handled. That complexity can only be grappled with by reframing your mindset.

But to make matters worse, reframing your mindset only works in that new stage of complexity handling: Once you’ve learned how to handle an SMB, for example, you can’t magically use SMB strategies on your new pre-PMF product line.

So, while you’re going to end up with a series of successive mental model shifts in the company throughout different periods of time and throughout different maturity areas of your various products, each one is going to apply only in that one domain; there’s no universal strategy.

Over time, they’ll proliferate, and you’ll end up having quite the tangled layer of strategies. Embracing the tangled layers, rather than trying to enforce a uniform strategy that can’t exist, will give you the flexibility you need to adapt observability successfully in a world where software development is seemingly changing every few months.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/10/58af1826-cropped-06daf154-screenshot-2024-10-02-at-10.13.52%E2%80%AFam.png)

Hazel Weakly spends her days building out teams of humans as well as the infrastructure, systems, automation and tooling to make life better for others. She’s worked at a variety of companies, across a wide range of tech and knows...

Read more from Hazel Weakly](https://thenewstack.io/author/hazel-weakly/)