As software systems grow larger, they become less comprehensible to any one engineer. Organizations expand in size, responsibilities become narrower and domain knowledge becomes more diffuse. A successful software organization, whether a medical information provider or a delivery service, will begin to split responsibilities among engineers.

Then, once everything is in production, teams run into the [unknown unknowns](https://thenewstack.io/the-4-evolutions-of-your-observability-journey/) of deployed software: business risks, performance degradation and any other thing one can only learn from computer systems that are actively running in the world. This means that teams need information to understand a system that is too large for one person’s continuous comprehension or intuition to keep up with.

The solution to this issue, increasingly, has become observability. [Observability is a loaded term](https://thenewstack.io/observability/), especially since its tools, practices and purpose are mostly prescribed by the vendors selling their version of it. Common to the [many](https://hazelweakly.me/blog/redefining-observability/) [definitions](https://charity.wtf/tag/observability-2-0/) of [observability](https://blog.bitdrift.io/post/observability-3-0), however, is the investigation and the making sense of unpredictable applications in production.

## Making Sense of What?

Observability is about [making sense of our live software systems](https://thenewstack.io/observability-every-engineers-job-not-just-ops-problem/), so the question should arise: making sense of what?

* Site reliability engineers (SREs) might wish to know what effect changes had on reliability metrics.
* Engineers working in their specific domain might want to know what went wrong with the services or modules they deployed.
* Product managers and analysts might use the information to evaluate the business impact of new features or experiments.

Each type of professional evaluates and learns from production data in a way that reflects their priorities.

## Who Makes Sense in the System?

But observability offers meaning for entire software systems, not tactics specific to any particular perspective. Software is, after all, a product of both technology and the humans who shape that technology. This [socio-technical](https://www.geeksforgeeks.org/socio-technical-systems/) system usually conceives of those humans as the developers who build the system.

However, the other humans that must be accounted for in our systems, and the perspective that’s missing from the observability picture above, are the users. Users are people, and any application exists to be used by a person in some way, even if that use is indirect. The evaluation of production data should reflect what happens to people, or our picture of the system is incomplete.

All the data in the world is meaningless if it doesn’t ultimately let you know what happened for users. There are certainly proxies for the user in data: product analytics derived from high-level funnel data, [crash reports and exceptions in web and mobile applications](https://thenewstack.io/developing-a-mobile-crash-model-for-opentelemetry/) or service measurements that approximate interaction with a client.

But none of these focuses on the user’s experience with the technical system they’re engaged with. Frontend applications are the manifested interface between people and technology, and yet observability has not reflected that interaction until now.

To focus on the user in observability means expanding our focus in the socio-technical system to make sense of the people who purposefully apply that software. By borrowing principles from other businesses, we’ll see that this isn’t a controversial assertion.

## Supply Chain Fundamentals

How did you last get paper towels? Did they come off a shelf? Did they get delivered?

Obviously, they didn’t appear out of thin air. They came from raw materials called trees, were turned into pulp and manufactured, then packaged and shipped. Ultimately, at the end of this journey came a purchase and some means of bringing them into your home.

Businesses are built to make sense of the value of each step in this process, and they use what was formerly called paperwork to track what might go wrong at any step. They can know exactly when a shipment was late, when a vendor failed to deliver packaging or if costs changed. Finally, at the purchase step, the consumer might or might not buy paper towels, based on a variety of factors involving human psychology, physical presence and need.

This last step is consumer behavior. Paper towel makers might want to sell you paper towels every day of the week, but you likely won’t buy them unless it’s necessary. What if you spill something and need to clean it up? What if you already have paper towels in your home?

## Life in an Interface

That dirty word from before, paperwork, clearly has an analogy in observability. When your product, whether towels or an application, goes off-premises, whether out of a warehouse or transmitting off the data center, you need information about what happened to it. If a shipment is slow, it can be tracked and explained, just as a service with high latency requires drilling into telemetry coming from its processes and related services.

Consumer behavior also applies to engineering, but with a vital twist: the interface. While purchasing physical products represents the end of the relationship with a seller, frontend applications provide value by keeping users in the experience. This means all the steps of the “supply chain” of software have to stay active and have to reflect the user’s needs during that relationship.

If a user can’t log in to their web portal for medical records due to a failing backend service, or because the modules are too old to load on contemporary browsers, or one of any other technical factors, the engineering team has failed in their relationship to the user. It might appear as an error or crash or failure to load, but to someone who intends to check on their blood tests, it’s simply frustration.

## Observability’s Dirty Secret

As software has become more complex, observability into its processes has been key. But the reason for this observability might have been lost.

Observability hasn’t focused on intention: what people are trying to do with the system. While product analytics might give a broad sense of “what happened,” learning from telemetry and pointing to “why it went wrong” is key to improving the system. For users, the specific issue doesn’t matter because the software doesn’t work!

In the world of browsers and mobile devices, technical issues prevent the success of the system. This success should be the goal for the entire engineering team. After all, if an API delivers a payload that the client can’t use, it has failed the user. An examination of the system that points to the person using it, with telemetry from all technical parts of that system, is the only way forward. That is user-focused observability.

## Getting Started With User-Focused Observability

At [Embrace](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=user-focused-observability), our mission is to empower engineering teams with user-focused observability so that they can connect technical performance to real user impact. We provide full technical visibility into user experiences so you can measure and improve the reliability of your software across every screen, device and platform.

We recently launched our latest product, [Web RUM](https://embrace.io/blog/introducing-embrace-web-rum/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=user-focused-observability) (Real User Monitoring), and we’ll be [presenting a live webinar](https://get.embrace.io/web-rum-launch-webinar?utm_source=the-new-stack&utm_medium=paid&utm_campaign=user-focused-observability) on June 26 at 10 a.m. PDT on the benefits of adopting a user-focused observability approach. Sign up today if you’d like to learn how you can understand performance and reliability from the perspective of your users.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/09/b01db1df-david-rifkin.jpeg)

David Rifkin is a developer relations engineer at Embrace. He brings eight years of experience as an iOS educator and engineer. Before joining Embrace, David worked as a mobile engineer at FanDuel, served as a lead iOS instructor at Pursuit...

Read more from David Rifkin](https://thenewstack.io/author/david-rifkin/)