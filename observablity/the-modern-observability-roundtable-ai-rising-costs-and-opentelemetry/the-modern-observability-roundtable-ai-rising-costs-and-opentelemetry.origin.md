# The Modern Observability Roundtable: AI, Rising Costs and OpenTelemetry
Is the term “observability” still productive? When it first entered common parlance around 2017, it was instructive in differentiating itself from traditional infrastructure and application monitoring. Back when applications were a bit more static, SREs would set up “monitors” on their critical applications, and receive alerts when certain thresholds were crossed e.g. an unwanted CPU spike, a customer-facing latency concern, and perhaps an entire service being knocked offline.

But what modern observability solutions are trying to unlock is the ability to ask real-time questions of our systems, without having to pre-define what may go wrong in advance. Because in a distributed world of microservices, it’s simply not possible to set up monitors on everything that matters; we need the ability to deal with unexpected situations and react accordingly.

Given the success of various observability solutions (Datadog’s IPO in 2019, Lightstep’s acquisition by ServiceNow in 2021), many startups and large enterprises alike co-opted the term observability, becoming a catch-all term for any solution that offers some sort of insight into your digital business.

So I sat down with some of the most respected thought leaders in observability to ask the tough questions.

[Paige Cruz](https://www.linkedin.com/in/paigerduty/), Principal Developer Advocate at[Chronosphere](https://chronosphere.io/).[Severin Neumann](https://www.linkedin.com/in/severinneumann/), Head of Community and Developer Relations at[Causely](https://www.causely.ai/).[Shahar Azulay](https://www.linkedin.com/in/shahar-azulay-54156bb4), CEO and co-founder of[groundcover](https://www.groundcover.com/).[Avi Freedman](https://www.linkedin.com/in/avifreedman/), CEO and co-founder of[Kentik](https://www.kentik.com/).[Charity Majors](https://www.linkedin.com/in/charity-majors/), CTO and co-founder of[Honeycomb](https://www.honeycomb.io/).
## Is Observability Still an Appropriate Term?
Just like teams don’t necessarily want more tools, they also don’t necessarily want new terms. Many companies still lack basic monitoring, leaving considerable room for most enterprises to [improve their observability](https://thenewstack.io/the-new-face-of-data-quality-anomalo-and-automated-monitoring/) practices. So while it’s fun to think about carving out further distinctions, such as * understandability *and

*controllability,*as practices and platforms continue to evolve, the group here seems to reach consensus that observability still holds as a term and practice.
## Are Costs Getting Too High for Customers?
There’s agreement that the cost of observability is a legitimate concern. Modern applications are becoming more complex at an unprecedented rate, driven by AI, and as a result, [operational costs scaling](https://thenewstack.io/can-companies-really-self-host-at-scale/) alongside that complexity may become untenable for many businesses. That said, the nuance lies in whether the value scales alongside the cost or not. Too often, costs are increasing, but the user experience is deteriorating. Different solutions to this problem are discussed in the roundtable, ranging from improved sampling to the new practice of Bring Your Own Cloud (BYOC), which enables customers to store their data while maintaining a SaaS experience.

## Is OpenTelemetry Critical to Modern Observability?
OpenTelemetry is the second most active open source project in the Cloud Native Computing Foundation (CNCF) behind only Kubernetes. Funny enough, many Kubernetes users still prefer Prometheus, at least for metrics. And so while the idea of open [standards for observability](https://thenewstack.io/chronosphere-nudges-observability-standards-toward-maturity-prometheus/) telemetry has unanimous support within the group, there’s still plenty of room to grow in execution for OTel, particularly in areas like logging and networking.

## How Will AI Impact the Future of Observability?
The group as a whole certainly wants to avoid the overpromises of AIOps back in 2017. That said, AI-driven development is moving faster than ever, and some on the panel go so far as to say that removing humans *from the loop* when it comes to IT Management is a legitimate possibility. Others on the panel stick more to [traditional messaging around the importance of socio-technical systems and keeping](https://thenewstack.io/werner-vogels-6-lessons-for-keeping-systems-simple/) humans in the loop, even as machines take on more responsibility. I think it’s fair to say that for the moment, humans aren’t going anywhere anytime soon when it comes to performance and reliability engineering… but leveraging AI solutions will certainly be part of any modern SRE toolkit.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)