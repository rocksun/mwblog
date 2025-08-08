In modern [frontend application development](https://thenewstack.io/frontend-development/), two things are undeniably true: Systems are more complex, and users are less forgiving than ever before.

Expectations for speed, reliability and seamless experiences are sky-high. And yet, the tools teams use to understand and improve these experiences remain deeply siloed.

On the one hand, you have classical product analytics tools (think Mixpanel and Amplitude). The type of data you get with these is great at telling you what users are doing and where they’re dropping off. These typically focus on funnel analysis and are indispensable to the product manager’s toolkit.

On the other hand, you have traditional [observability](https://thenewstack.io/observability/) tools. These excel at telling you how a system or application is performing under the hood, focusing on technical telemetry like logs, metrics and traces. These fit squarely in the realm of engineering, and, for a long time, were fairly limited to [backend](https://thenewstack.io/backend-development/) engineering teams, with frontend engineers only embracing observability practices more recently.

Both types of tooling measure, through a different lens, how successfully an app can deliver on what it’s meant to do.

However, product analytics and technical observability have traditionally lived in separate worlds, siloed to different teams. This is a problem because neither tells the full story on its own.

A modern way of building applications requires a more cohesive approach that tethers technical and behavioral elements. We need to bridge the gap between [product analytics](https://thenewstack.io/live-data-is-rapidly-reshaping-product-development-practices/) and observability to truly understand, and ultimately optimize, end user experiences.

## The Limitations of Relying on Only Product Data

The problem with conventional product analytics is that they’re optimized for visual and interaction design. Funnels, drop-offs and engagement maps highlight where friction occurs, but say little about why. These tools rarely account for performance — and when they do, it’s often via generic thresholds like, “if it takes more than two seconds, users are unhappy.”

But that assumption doesn’t hold up in practice. The reality is much more nuanced, and generic performance baselines often do not translate across different industries and app types.

For example, users may tolerate a two-second delay on a content feed but abandon a checkout flow over an additional 300 milliseconds. Context matters. Without connecting technical performance to behavioral variables, teams are left guessing.

Relying solely on product analytics tools often creates a frustrating loop between product managers, designers and engineers that fails to adequately solve issues.

This is a situation many product managers are familiar with, and it often goes like this:

“A product analytics tool is telling you that your user engagement metric is not trending the way you want it to, yet offers no insight into why. You go to the engineering team, and they say, ‘Tell us what to change.’ With no technical direction from your tool, you cannot give them an answer. So, you then go to the product design team to ask for help. The team assigns a designer to go through a bunch of (often futile) exercises to understand what’s wrong with the UI and make changes that are largely laden with assumptions rather than data. You’ve now changed the UI/UX, and everyone seems pleased that the engagement issue should be solved. Over time, the metric has still not improved, and three months later you are stuck wasting another two sprints running through the exact same process hoping that ‘this time, we’ll make a difference.’ And the whole time, some frontend component was shaky, inconsistent and slow, which you would have known about had you been able to capture technical data alongside product analytics.”

If this sounds familiar, then you have likely experienced the limitations of product analytics firsthand.

## The Limitations of Traditional Observability Data

Traditional observability tools also have their own set of limitations.

While metrics, logs and traces are a great window into the health of the software, they don’t offer much insight into the software’s effects on the user. They are inherently low-context, intended to work for engineers with a deep understanding of the technical operation. A huge reason for this is that observability as a practice started on the backend, and only recently has it been evolving and adapting to consider the very different and much less controlled world of the software frontend.

Take, for example, typical observability metrics around API endpoint performance. While an endpoint critical to an app feature, such as product search, may be healthy and operational, the content intended for the user’s device may be delayed due to frontend rendering issues. This results in poor performance and potential user abandonment, which traditional observability tools may not even notice.

## Taking a User-Centric Approach

This is where [user-focused observability](https://thenewstack.io/the-case-for-user-focused-observability/) comes in. By connecting frontend telemetry (Core Web Vitals, network events, JavaScript exceptions, etc.) to real user behavior, engineering and product teams can collaborate around a shared understanding of the actual user experience. To do this well, you need tools that bridge the gap between the high-context, low-granularity product space and the low-context, high-granularity engineering space.

This closes the loop between system performance and the end user impact, allowing teams to prioritize improvements based not just on what’s broken, but on what truly matters: your users doing the things they want to do.

## The Cultural Shift in Engineering

There’s also a cultural shift to support this movement toward cohesive, user-centric observability.

Engineering teams have gotten faster and more efficient at writing and debugging code thanks to better tooling, automation and deployment practices. Growing past these P0/1 issues means they should be thinking about optimizing performance through the experience of the user. The natural next step is for engineering teams to take a seat at the strategy table. The best products in the world have engaged, active and collaborative engineering teams invested in their end users.

Tools that surface how engineering-led changes, such as improving paint time or reducing long tasks, affect user engagement create a feedback loop that empowers engineers to build with more empathy for the end user, rather than just velocity.

## Final Thoughts

As much as we, on the build side, may be inclined to silo our work and responsibilities, end users don’t see it that way. A failure is a failure… a delay is a delay. It doesn’t matter if the root cause is a poor design decision or a rendering bug, because end users don’t distinguish between these types of issues. A confusing interaction and a delayed response feel the same.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/08/096aa2c4-cropped-fb6b3cfb-kasey-smith-600x600.png)

Kasey Smith is a senior product manager at Embrace, focused on delivering innovative, in-platform solutions that help engineers understand technical performance through the lens of real end user experiences. Kasey is an expert at solving complex problems by harnessing the...

Read more from Kasey Smith](https://thenewstack.io/author/kasey-smith/)