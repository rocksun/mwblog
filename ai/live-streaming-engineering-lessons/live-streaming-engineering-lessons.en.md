Live sports involve myriad unknowns, but one thing is certain: the live video feed must play flawlessly, and simultaneously, for all the fans tuning in. If some hear their neighbors cheering or groaning 5 seconds before each score, they won’t have kind words for their streaming platform.

In 2023, Ashutosh Agrawal and his JioHotstar (then JioCinema) engineering teammates prepared for the Indian Premier League (IPL) cricket finals as intensely as the athletes. While the players ran on the pitch, the engineers ran their own training simulations and drills to ensure every fan could celebrate (or commiserate) in sync.

A year ago, he joined us at P99 CONF to share how they built and tested the system behind that record-setting game, plus lessons learned that can help anyone preparing for high-uncertainty events (Black Friday, anyone?).

*Watch the complete talk, or read the highlights below. And if you enjoy these types of engineering case studies, join 30K of your peers for P99 CONF 2026, which is free and virtual. Grab* [*a complimentary pass*](https://www.p99conf.io/?latest_sfdc_campaign=701Rb00000qrLWi&campaign_status=Submitted&utm_campaign=smo%20new%20stack%202026-10-21%20p99%20conf&utm_medium=social%20media%20-%20organic&utm_source=the%20new%20stack&lead_source_type=the%20new%20stack) *and join us October 21 and 22!*

## Pre-game

The IPL is the premier cricket tournament and one of the world’s most-watched sports. And Ashutosh is an IPL pro, from the engineering perspective at least. After working on the backend streaming platform since 2018, he’s learned that “with cricket, you never know what will happen.”

In 2023, the final ended up drawing a then-record-breaking 32M concurrent viewers. But they were ready for even more. Just to be safe, the team builds and tests for roughly double the capacity they expect: “a scary number that scares the hell out of everyone on the team,” as Ashutosh put it. That year, they prepped for 50M to 75M. Aiming that high provides the headroom needed to absorb traffic spikes without requests piling up.

Keeping the video feed flawless is their top priority. He explained, “You can sacrifice every other system and component in the line, but anything in the line of video delivery has to be a golden path — it cannot fail. Because if that fails, the entire promise of the platform goes away.”

> “You can sacrifice every other system and component in the line, but anything in the line of video delivery has to be a golden path — it cannot fail. Because if that fails, the entire promise of the platform goes away.”

The first step in safeguarding that stream is identifying all the systems and components in that critical path. Although the actual video feed stems from CDNs, one of the biggest potential bottlenecks occurs before the final video delivery URL. Ashutosh explained:

“The user has to be logged in and authenticated; we use SMS and OTP authentication. Sending out that many SMSs across the country in a short span of time is a problem statement of its own. And the key thing: the real peak on some of these systems isn’t during the final; it’s actually on the first day. That’s when a massive number of new users, or users who haven’t logged in for the last 360 days, show up, and they all try to log in within the first five or ten minutes. That’s where you see peak concurrency.”

To handle the surges, they preemptively scale critical systems like authentication. Partners undergo rigorous load testing, and any who aren’t meeting the latency SLAs will be cut off during the event. Whenever one partner’s latency degrades, traffic is instantly redirected to the next partner in the hierarchy.

## A 200-point checklist

The pre-game prep also includes an extensive system audit with a 200-point checklist. For example, for the database, they look at whether they’re running the latest version and check if there’s a maintenance window during game time. For other partners, they look at their key dependencies, redundancy, and timeout configurations. Timeouts between load balancers and services, services and application servers, application servers and the database, all the way up through the CDN are covered.

Most of these checkpoints stem from lessons learned. “There was one incident where a service didn’t have keep-alive timeouts configured properly,” Ashutosh recalled. “During peak traffic, it was discarding connections instead of reusing them – so the load balancer started to crash because it couldn’t handle the request load.” That became a checkpoint for the next season.

> “If all your SMS partners die, what does your system do? It can’t just block traffic and lock users out; it has to let users in. We go to that extent to identify every point of failure.”

Every developer or service owner uses the checklist exercise to identify the key points of failure, then they’re tasked with documenting their mitigation strategy. For example, “If all your SMS partners die, what does your system do? It can’t just block traffic and lock users out; it has to let users in, maybe in a non-authenticated way. That might require going back to Product to design something like a five- or ten-minute free viewing session without authentication, or a temporary token, deferring authentication to later. We go to that extent to identify every point of failure.”

## Testing, testing

Next up: testing, lots of testing. They perform:

* **Vertical testing**, which is initially run on individual systems and services to ensure that each system can scale in isolation. Then, it’s performed on each partner (SMS partner, email partner, ad provider – anyone integrated into the critical path or surrounding paths).
* **Multi-system load testing** ensures clusters of systems work together properly. As Ashutosh explained, “A service might scale beautifully in isolation but reveal its true colors once you add dependencies.” For example, testing playback might involve testing a cluster with content systems, analytics, load-balancing systems for CDNs, and so on.
* **Full user-like simulation**, which simulates user behavior on the mobile app or website and looks at how that impacts all the associated systems.

> “A service might scale beautifully in isolation but reveal its true colors once you add dependencies.”

That realistic end-user simulation is critical, according to Ashutosh: “It has actually helped us identify some critical system issues. For example, content systems get called from multiple places (the listing page, the details page, somewhere getting playback metadata). If a team forgets to account for that fan-in, those budget and scaling issues only show up in a full simulation. It stresses the system at a different level than a vertical load test does.”

## Latency budgeting

When asked about their budget for end-to-end latency, Ashutosh shared their rule of thumb: Any system that’s entirely in-house (not talking to a third party) must operate within a budget of about 10 to 15 ms – purely server-side, no network involved – for a simple O(1) lookup and downstream response.

In more complex cases (for example, with multiple database calls or a downstream third-party call), 40-50 ms is allowed. If anything in the critical path crosses 50 ms, they start thinking about what can be [handled asynchronously](https://thenewstack.io/async-processing-hides-latency/).  With client, network, CDN-to-origin, and last-mile latencies factored in, the user experiences 60-100 ms latencies.

The strictest latency budget is reserved for the API that sits between a viewer tapping a video tile and the video actually playing. If something fails there, users end up hitting retry, or closing/reopening the app…and that hits the API even harder. That API response is difficult to cache since every call has to run CDN load balancing and check authentication in real time. “Even when a third-party call is unavoidable in that path, it runs under a strict circuit-breaking time budget – 5 or 10 ms – because it’s okay to fail fast and recover rather than wait to be correct,” Ashutosh said.

Ashutosh summed up their thinking on latency budgets:

“These response budgets help us question and challenge service owners: what can you optimize, how can you reduce load on the live system, [how much more can you cache](https://thenewstack.io/redis-vector-caching-tradeoffs/), how much can you pre-prep. Login obviously can’t be cached, but the moment you land on the homepage, we try to response-cache as much of the page as possible. With personalization, that gets tricky. So, we cache bits and components of the page separately, with the layout configuration cached separately from the content. That combination keeps page response times quick.”

## 3 tips for engineers preparing for big events

Ashutosh closed by offering 3 recommendations for engineers prepping for high-uncertainty events, like Black Friday sales, other live events, and so on:

“First: set your principles correctly. Get org-wide alignment with leadership and your team on what your priorities are. That alignment is critical because it drives decision-making before, during, and after the event. If you have a conflict of principles, you end up in a decision-making bottleneck, and that leads to a bad situation. So that’s number one.”

“Second: challenge your systems. Don’t settle — don’t accept that 100ms response times are just okay. The technology has evolved massively, computing power has improved massively, and there’s no reason for [server-side latencies](https://thenewstack.io/agentic-ai-latency-infrastructure/) to sit in the hundreds of milliseconds. Client-side latency, I understand that’s a different story — but server-side latency is very much within your control.”

> “Don’t settle — don’t accept that 100ms response times are just okay. Server-side latency is very much within your control.”

“Third: identify your critical path and make sure it’s solid. Critical path identification is a genuinely tricky problem — it doesn’t just mean looking at the high-level systems. I mean things like: if there’s a synchronous call to send analytics data, that call should not be synchronous — it shouldn’t be anywhere in the critical path at all. Nothing that isn’t a true P1 or P2 dependency should sit in that synchronous critical path to the experience you’re trying to deliver. Optimize for that. It might mean saying no to things, or it might force you to re-architect some pieces. But that’s the most important piece, in my opinion.”

**Bonus round:** Hear more from Ashutosh in this chat with Gergely Orosz on [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/live-streaming-at-world-record-scale).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/01/14adf317-cynthiadunlop.jpeg)

Cynthia Dunlop has been writing about software development and testing for much longer than she cares to admit. She's currently senior director of content strategy at ScyllaDB.

Read more from Cynthia Dunlop](https://thenewstack.io/author/cynthiadunlop/)