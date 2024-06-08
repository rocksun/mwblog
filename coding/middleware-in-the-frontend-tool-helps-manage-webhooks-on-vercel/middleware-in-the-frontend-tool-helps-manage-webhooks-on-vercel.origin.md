# Middleware in the Frontend? Tool Helps Manage Webhooks on Vercel
![Featued image for: Middleware in the Frontend? Tool Helps Manage Webhooks on Vercel](https://cdn.thenewstack.io/media/2024/05/4c3fc462-gateway-1024x683.jpg)
A new open source middleware by
[Hookdeck](https://hookdeck.com/) will help developers manage asynchronous events on Vercel. [Hookdeck Vercel Middleware](https://github.com/hookdeck/hookdeck-vercel) is designed to run on Vercel’s system with just three lines of code.
The middleware adds the ability to authenticate, delay, filter, queue, throttle, and retry asynchronous HTTP requests (via webhooks) made to a Vercel application, Hookdeck co-founder and CEO
[Alexandre Bouchard](https://www.linkedin.com/in/alex-bouchard/?originalSubdomain=ca) told The New Stack.
Two use cases are dealing with
[webhooks](https://thenewstack.io/new-open-source-standard-brings-consistency-to-webhooks/) from API providers such as Stripe, [Shopify](https://thenewstack.io/dev-news-rust-based-slint-matures-and-shopify-cleans-up/) or Twilio, or building [asynchronous APIs](https://thenewstack.io/api-management-for-asynchronous-apis/). It was a natural extension for Hookdeck, which calls itself an event gateway. Event gateways are like a software central hub for managing the flow of events between services, orchestrating events that come into or leave your system via a third party, he said.
## Webhooks: A Gateway to Event-Driven Architecture
“I call
[webhooks the gateway drug](https://thenewstack.io/webhooks-the-building-blocks-of-an-event-driven-architecture/) to event-driven architecture because, for a lot of developers, it’s their first exposure to the asynchronous programming paradigm and event-driven architecture concerns,” Bouchard said. “Hookdeck sits in front of the… infrastructure that you have and ingests those events; and we deal with the management, the queuing, the error recovery, and all the security aspects to it, too. What that means is that we become a central point for the ingress and egress of those events.”
Hookdeck considers the event gateway as
[an evolution of the API gateway](https://thenewstack.io/shadow-apis-breaking-your-security-the-enroute-api-gateway-could-help/), but for event-driven stateful workflows. The company counts its competitors as [Azure Event Grid](https://thenewstack.io/tutorial-exploring-azure-event-grid-custom-webhooks/), [AWS EventBridge](https://thenewstack.io/going-serverless-on-aws-lambda-recognize-potential-risks/) and the open source project, [Convoy](https://getconvoy.io/). But when it comes to the Hookdeck Vercel Middleware in particular, Bouchard doesn’t think there is a competing offering.
“You’re not going to go to Shopify and tell them, hey, you know what guys, come back in half an hour — right now, I can’t deal with this,” Bouchard said. “You don’t really have the benefit of any margin for error when it comes to you not controlling the publisher. Webhooks is a subset of the problem.”
## But Why Middleware?
The middleware approach lends itself well to serverless runtimes, Bouchard said. Hookdeck Vercel Middleware solves two problems, he explained. The first is it provides a different web developer experience than the full Hookdeck event gateway. There are a small subset of contexts where this approach will work and
[Vercel](https://thenewstack.io/vercel-creating-new-ai-framework-also-rust-and-adobe-updates/) was the best option for trying the approach, he said.
“Hookdeck right now is very declarative. You have to preconfigure all your configuration, your connections and all that before you can go live,” he said. “The goal in middleware was to be able to do that on the sly. So, basically, to be able to say, in this code, I want this endpoint now to become what we call an asynchronous endpoint — an endpoint where the requests are being deferred, queued, modeled, and so on; and do this in a way where, for the developer, the experience is very transparent.”
The middleware component allows the developers to set up an asynchronous endpoint and establish the rules and conditions for it, he said. The code runs on the Vercel Edge network, but Hookdeck manages the actual requests, he added.
“What happens is basically the middleware will receive HTTP requests like a webhook coming from, say, Shopify,” he explained. “It receives a webhook, it evaluates whether or not that should be deferred and queued — and if it does, then, the middleware will forward that request to the Hookdeck edge network.”
With the middleware, developers can manage:
- Queues;
- Throttling, for when a third part sends more webhooks than your system can process;
- Retrying a synchronous HTTP request;
- Delays, which, for example, would be used in situations where customers can edit an order within a certain time frame;
- Filters, which would allow filtering based on the data in the payload to let an event through or not. For example, it would allow developers using Shopify to filter all product update webhooks for only the ones where a production is out of stock, Bouchard said.
For scenarios where there will be hundreds of millions of events ingested or anything that’s mission-critical, he recommends using Hookdeck’s core event gateway solution.
## Potential Areas of Expansion
JavaScript was also a top choice for trying this approach because it’s so widely used, but if this goes well, Hookdeck plans to develop the middleware for other languages as well, he said.
Hookdeck is also considering expanding the approach to other providers. The code itself is written in a way that much of it could be used outside the context of Vercel, although there are some developer experience considerations that are Vercel-specific, he added.
[Supabase](https://supabase.com/), an open source alternative to [Firebase](https://thenewstack.io/supabase-takes-aim-at-firebase-with-a-scalable-postgres-service/), is one such provider that he mentioned as a possibility.
“We’re seeing a lot of usage on top of Supabase functions,” he said. “That’s definitely one that we’re seeing and we’re thinking about as well.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)