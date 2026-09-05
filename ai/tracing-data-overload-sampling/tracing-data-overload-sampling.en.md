**A metrics dashboard can tell you** a system’s health with ease. A log can help you understand a discrete failure. But if you want to understand where in a query’s journey things went awry, you need traces.

By tracking a request from its point of origin through data and microservices to the end user, traces offer unparalleled insight into how systems work and where failures occur. SREs offer the fastest path to remediation. That means less downtime, fewer burned-out developers, and happier customers.

VIDEO

Sadly, the promise of traces often doesn’t match the on-the-ground reality.

Why? Simply collecting and holding onto all your company’s traces is an exercise in hoarding. Do you need to store terabytes of tracing data just to show when your systems worked? Not only is that much information expensive to hold onto, but collecting it can slow the very systems you are trying to monitor. And when you have all the stored tracing data, finding what you need in the ocean of information can take too long.

## Is tracing cooked? Not at all.

Is tracing cooked? Not at all. There are several ways to beat back tracing data overload: Head sampling collects only a portion of tracing data, reducing storage concerns; tail sampling asks whether, after a trace is recorded, it is worth holding onto, making it easier to find what you’re looking for down the road. And dynamic sampling can automatically cull similar or highly repetitive traces, so you don’t accidentally flood your storage system with nearly identical data.

You can avoid the most common tracing pitfalls by building your observability system intelligently. That’s precisely what I was hoping to learn from [Sarah Hudspeth](https://www.linkedin.com/in/shhudspeth/) of [Chronosphere](https://chronosphere.io/) (a Palo Alto Networks company), who is my guest on the latest episode of *The New Stack* podcast.

Whether you are just starting your tracing journey or deep in the trenches looking for help, Hudspeth’s ability to turn abstract technical concepts into simple, digestible analogies is enviable.

Hit play on the episode above, and let’s jump the chasm between the promise of tracing and getting it to work for you in a production setting.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/04/03000ee4-cropped-4cd6e98e-image.png)

Alex Wilhelm is a journalist focused on technology and finance. He co-hosts the This Week in Startups podcast, and writes the Cautious Optimism newsletter. He was previously Editor in Chief of TechCrunch+.

Read more from Alex Wilhelm](https://thenewstack.io/author/alex-wilhelm/)