[API monetization](https://thenewstack.io/the-dos-and-donts-of-api-monetization/) is expected to reach $8 billion by 2027 in the US alone. That figure could be driven higher by the advent of AI-powered APIs, said [Adrian Machado](https://www.linkedin.com/in/adrianmachado/), a staff software engineer with [Zuplo](https://zuplo.com/), an [API management](https://thenewstack.io/introduction-to-api-management/) platform designed for developers.

For instance, in the travel sector about 90% of revenue is coming from APIs, he said. Expedia, airlines, travel products — all sold through APIs, he added.

“One thing you should know is that the market for API monetization is growing and [in] the U.S. alone, API monetization revenue is going to reach $8 billion in 2027, so that’s only two years from now — and maybe even higher with the advent of AI-powered APIs,” Machado told audiences at Postman’s [POST/CON](https://www.postman.com/postcon/2025/), held in Las Angeles this month.

It’s not just about charging money for an API. It’s also about the exchange of value through APIs; and that can include indirect monetization as well as ecosystem expansion, he explained.

“But there are some other indirect benefits as well,” he said. “Some of that is connecting with your developer community and empowering them to build new features on top of your existing platform. Facebook is a good example of this, the games ecosystem that they built and so many users built on top of — like messenger, for example, for businesses.”

An [API monetization strategy](https://thenewstack.io/apis-are-driving-new-business-models-and-unlocking-revenue-streams/) can also help support larger customers, such as enterprises or the government using your API, he added.

“The government comes along, they’re not going to want to click through your funky web portal,” he said. “They’re going to want an API to automate with their existing systems, like HubSpot or whatever, to facilitate automation of your platform.”

The last thing to consider is that your competition is probably already formulating an API monetization strategy, he said.

## Charging Models for APIs

The first thing to consider is your API monetization model. That’s the business aspect of it — essentially, how you bill for the API. Machado said that developers have three options:

**The Usage-based Model or Pay Per Use.** “This is, as the name implies, charging on how much usage your consumer is using of your API,” he said. “Oftentimes, this looks like API calls.”

Rates can be based on points or cents per [API call](https://thenewstack.io/sentrys-front-end-performance-monitoring-pinpoints-sluggish-api-calls-and-database-queries/), or even $1 per 1,000 API calls.

“Whatever it is, it’s some flat amount of API call,” he said. “But it doesn’t have to be great API call. Recall, again, an AI example. Token consumption is also usage-based billing as well.”

In a similar vein, you can also charge for data consumption.

“Imagine you’re Dropbox and someone uploads 3MB files to your server — you’re going to charge them for storage cost,” he said. “Not for API calls, because they can upload a giant file and really small files.”

One challenge with this approach, however, is that there’s no way to know how much you’ll make off the API — it could be $10,000, it could be $15,000, or it could be nothing.

**The Subscription Model.** The opposite of the usage-based model is the subscription model. Basically, you create buckets for users, such as a tier that gets 1,000 requests for free, a startup tier that gets a million requests, and then the enterprise tier, which might get 100 million requests. Each tier is charged a different monthly fee.

“It’s actually very hard to start with subscription-based billing,” he said. “Determining those tiers in the first place is actually very difficult. Typically, you need to do a little bit of data science to see what the average usage is like, depending on the organization size and stuff like that.”

There’s also a percentage fee, which is more common in payments and fintech. Think of a credit card API or crypto companies that charge 1 or 2% for every transaction that goes through the API.

**The Revenue Share Model.** This is not a model he sees a lot of. In revenue share, there’s a partnership between the API provider and the person calling the API, where they essentially work together to make money. This is the model used by Google Adsense.

“For example, you’re calling the AdSense API, they’re going to get, let’s say, $1 for the ad impression,” he said. “They’re going to give you 50-cents on the dollar, for example. So you both make a little bit of money.”

The two most common monetization models, he said, are the subscription-based and usage-based billing.

One option that he briefly mentioned was **API marketplaces** as a means of monetization. He’s not a fan and discouraged developers from choosing that option.

“First of all, that revenue share that they charge you — they charge, I think, roughly, after fees and everything, about 20% of your revenue — essentially just to act as a billing provider and a little bit of marketing for your API,” he said. “I recommend [to] steer clear. No serious business sells on the API marketplace.”

## Implementation Details

In a usage-based model, the developer basically charges for the number of requests. It’s typically implemented with a distributed counter. He used [Redis](https://thenewstack.io/redis-is-open-source-again/), which is a NoSQL in-memory cache database, to store account runs per IP address, Machado said. He used a managed Redis provider, but noted it could be self-hosted.

“Very simply, I’m invoking Redis over here,” he said. “I just authenticate with the rest of Redis in lines six through eight, and then within lines 11 through 23 have a brief, very simple function that reads in the user. In my case, I would be reading in the IP address of the request. But this could just as easily be a job token, an API key, whatever you really want to be charging based on right.”

Then he created a counter, seen on line 19. That’s the key he put into Redis to uniquely identify how many requests the user has.

“In this case, I look at the day, month and year, so that this counter is for this user, for this day, month and year, how many requests came in,” Machado said.

He takes that value in the database for the date, he can then look back and see it made 2,000 API calls. He then takes that number and charges them accordingly using some sort of payment gateway.

“There’s plenty of advantages to this,” he said. “It’s very flexible.”

In a subscription-based model, he now introduced the concept of a quota.

“I’m going to limit you to 10 API requests per minute, let’s say, and as soon as you hit that, I’m going to start rejecting you, because I have a plan, and that plan is only entitled to 10 API requests,” he said. “If you want to get more API requests, you got to talk to me, you got to upgrade your plan.”

The approach allows 10 API requests per quota period, so much of the early code remains the same. But in this case, he needs to find the plan for the user. Typically, this would be metadata that the developer would attach, he explained — it may be included in the job token. It could also be set up as external system that pulls in what the plan of the user is. Line 29 introduces the new quota system built in, where the code checks to see if the user has exceeded the rate or quota limit for its plan, he noted. If the user has, the code going to send back a bad request called retail response.

“There are many advantages to this,” he said. “Now that you’re charging, let’s say a flat rate, like $100 a month for 10,000 API requests. You know you’re going to have that $100 a month next year, as long as the user doesn’t cancel. So you have better forecasting and predictable revenue, which makes it easier for your budget, for the future, for developments in your API or otherwise.”

But there are some disadvantages. It’s harder to start, for one, requiring a little bit of data about usage ahead of time to establish tiers.

It also may not be ideal for customers that straddle the boundary of the tiers. It may not be worth it to go up a tier, so they may reduce using your API.

## The Tech Stack

He noted that the minimum tech stack to support these models is to have:

* **A billing provider**, such as a fintech system for managing your products, creating pricing tables, managing subscriptions and facilitating payments. Possible providers include [Stripe](https://stripe.com/), [Paddle](https://www.paddle.com/) and [Apigee](https://thenewstack.io/building-adaptive-apps-like-google-now-with-apis-and-analytics-with-apigee-insights/), he noted.
* **An API gateway** for tracking and reporting usage, enforcing authentication and authorization and enforcing quotas. He admitted to a bit of a bias here, since he works for Zuplo, which he recommended, but he noted [Moesif](https://www.moesif.com/) plus any gateway and Apigee are other options.
* **A** [developer portal](https://thenewstack.io/api-governance-and-developer-experience-in-a-developer-portal/) to provide a nice developer experience, where developers can browse documentation, purchase API subscriptions, track usage and manage authorizations.

If you prefer to roll your own solution, he suggested:

* **A load balancer**. API calls can come from anywhere, so stand a load balancer in front of your service and make sure to autoscale to handle high traffic using a serverless host (e.g., Lambda).
* **Rate limiter + Web Application Firewall (WAF).** [Cloudflare](https://thenewstack.io/cloudflare-for-ai-helps-businesses-safely-use-ai/) can provide the WAF if you want too write your own rate limiter service, he said.
* **API Key System**. He noted that API keys provide the best UX and you can write your own or use [Unkey](https://www.unkey.com/).

*Editor’s Note: Postman paid travel and accommodations for Loraine Lawson to attend the POST/CON conference.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)