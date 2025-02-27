# Event Destinations: A Faster Alternative to Webhooks
![Featued image for: Event Destinations: A Faster Alternative to Webhooks](https://cdn.thenewstack.io/media/2025/02/1ba83ce4-eventdestinationsalternativetowebhooks-1024x683.jpg)
Webhooks are widely used but are not without their challenges. For instance, there’s a lack of [broadly adopted standards](https://thenewstack.io/new-open-source-standard-brings-consistency-to-webhooks/), which means there’s not a universal approach to retries, timeouts, authentication or payload formats.

A webhook, which Atlassian [defines](https://developer.atlassian.com/server/jira/platform/webhooks/) as a “user-defined callback over HTTP,” can create performance bottlenecks for both [API](https://thenewstack.io/api-governance-using-patterns-from-paypal-netflix-and-more/) platforms publishing webhooks and developers building applications that ingest webhooks, resulting in high operational and infrastructure costs.

To address these weaknesses, a recent manifesto launched Monday proposes an alternative approach called Event Destinations, which offers a scalable, faster alternative to webhooks.

”Webhooks are the least common denominator,” the [Event Destination Initiative website](https://eventdestinations.org/) noted. “They offer amazing reach but lack capabilities at scale. How can you combine the reach of webhooks with the capabilities of other event paradigms? With Event Destinations.”

## What Are Event Destinations?
Event destinations are a set of guidelines for a new way to deal with events, but you might also think of them as a new pattern that’s emerged. [Phil Leggetter](https://www.linkedin.com/in/leggetter/?originalSubdomain=uk), head of developer relations at [Hookdeck](https://hookdeck.com/), explained that event destinations are [endpoints or systems](https://hookdeck.com/blog/event-destinations) to which event producers can send events, while allowing the developer the choice to use the tools they are familiar with directly.

Leggetter launched the site [EventDestinations.org](https://eventdestinations.org/) on Monday to act as a clearinghouse for explaining the approach and guidelines. There’s also a [GitHub repository](https://github.com/hookdeck/event-destinations/blob/main/specification.md), which offers the source for the website and a more detailed specification for Event Destinations.

Online payment processing platform [Stripe first introduced Event Destinations](https://docs.stripe.com/event-destinations), but it’s also used by [Twilio](https://www.twilio.com/docs/events/event-streams/sink-resource) and [Shopify](https://shopify.dev/docs/apps/build/webhooks/subscribe/get-started?deliveryMethod=pubSub), and supported by event gateway Hookdeck.

“You could deliver Stripe platform events — payments, events that you want the applications you’re building to consume from the Stripe platform — via not just webhooks, not just an HTTP request notification from Stripe, but delivered directly to Amazon EventBridge,” Leggetter explained.

The implementation guidelines state that it must support at least two types of event destination, one of which must be HTTP webhooks because of their widespread use and simplicity.

![Chart showing event destinations can send to HOOKDECKAMAZON EVENTBRIDGE GCP PUB/SUB KAFKA RABBITMQ](https://cdn.thenewstack.io/media/2025/02/0636cd67-event-destinations-1-2.png)
Courtesy of Phil Leggetter via [EventDestinations.org](https://eventdestinations.org/)

But the second type can be chosen from other popular event destinations, such as [message queues or event](https://thenewstack.io/choosing-between-message-queues-and-event-streams/) buses. Examples of supported event destination types include:

- Message queues (e.g.,
[AWS SQS](https://aws.amazon.com/sqs/),[RabbitMQ](https://thenewstack.io/rabbitmq-is-boring-and-i-love-it/)) - Event buses (e.g.,
[Amazon EventBridge](https://aws.amazon.com/pm/eventbridge/),[Google Cloud Pub/Sub](https://cloud.google.com/pubsub))
“This requirement ensures that the implementation can cater to different use cases, integration needs, and preferences of developers,” the documentation stated.

## What Customers Want
From an API platform builder perspective, event destinations remove a huge burden, Leggetter said.

“It actually takes the load off of them because other destination types’ successful delivery rates will be higher, removing the need to queue and manage retries,” Leggetter said. “They know a higher percentage of events are going to be successfully ingested by Amazon EventBridge or by GCP Pub/Sub because these are highly available, fast services that will reliably ingest events.”

Plus it’s what customers want, he added.

“We’ve observed that API platform vendors want to deliver in a different way to only webhooks, to reduce their burden from an infrastructure perspective, but also provide a better [developer experience](https://thenewstack.io/api-governance-and-developer-experience-in-a-developer-portal/) — less infrastructure for their customers to manage,” he said.

## Early Adopters
Stripe, Twilio and Shopify all allow developers to send events directly to supporting event destinations, which includes messaging queues and brokers such as AWS Simple Queue Service (SQS), GCP Pub/Sub, Hookdeck and RabbitMQ, as well as the distributed streaming platform [Kafka](https://thenewstack.io/shift-left-meets-kafka-testing-event-driven-microservices/).

Stripe’s Event Destinations implementation allows developers to select the best destination for their needs, with webhooks being one option.

“By enhancing existing webhook capabilities while introducing new destination types, developers can transition at their own pace, maintain backward compatibility and leverage the best of both worlds,” the manifesto stated.

For event producers such as Shopify, Twilio and Stripe, this creates efficiency gains along with reduced failure rates and retried deliveries compared to public HTTP endpoints.

This unlocks improved performance for high-throughput scenarios, according to the Event Destinations site.

“Smart retry logic, improved deliverability and scalable infrastructure minimize resource consumption, reducing operational costs while ensuring seamless event delivery at any scale,” the site noted.

Event producers must support a set of guidelines for event destinations to work:

- Allowing two event destination types, including webhooks;
- Automatic delivery retries with exponential backoff;
- APIs to create, update and delete destinations; and
- Alerts for destination failures.
## Benefits to Developers
“This DX evolution helps everyone; developers gain tools that are more powerful and simpler to use and maintain,” the manifesto stated. “Developers are more successful and faster at [adopting developer](https://thenewstack.io/platform-teams-adopt-these-7-developer-productivity-drivers/) platforms.”

In particular, the site outlines these benefits to developers:

- Easier integration, because developers no longer need to set up, manage and scale HTTP endpoints;
- A reduced cognitive load, as standardization in retries, security and performance handling allows developers to rely on consistent and predictable event delivery;
- A built-in scalability, because as systems scale, efficient protocols, batching, and proven resilient infrastructure ensure event delivery remains reliable, even under high throughput;
- Reduces maintenance overhead by eliminating the need for API gateways, load balancers, HTTP consumers and other infrastructure components; and
- Predictable behavior and standardized event expectations — the message bus handles timeouts, retries and security.
“This evolution isn’t just about solving pain points — it’s about unlocking new possibilities for developers building event-driven applications,” the manifesto stated. “By prioritizing interoperability, security, and efficiency, Event Destinations represent the next step in creating a developer experience that empowers everyone.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)