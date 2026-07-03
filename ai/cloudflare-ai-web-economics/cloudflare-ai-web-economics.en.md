AI has changed the web right before our eyes. With Google’s AI Overviews doing the heavy lifting, publications that once owned the first page of search results are being replaced by summaries. Readers get their answer without ever clicking through. Much of the traffic has simply stopped.

Cloudflare on Wednesday [announced](https://blog.cloudflare.com/monetization-gateway/) a slew of updates for publishers who are facing this new reality. From new crawler classifications and analytics dashboards to Answer Engine Optimization tools and an expansion of its Pay Per Crawl program, it’s clear the company is trying to become the economic pipes of the AI web.

## The shift from ‘keep out’ to ‘let’s make a deal’

[A year ago](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/), Cloudflare’s pitch was practically defensive, asserting that website owners should be able to block AI crawlers. And while that still holds true, the company has pivoted to discussing building “rails” for an “agentic economy.” And it makes sense. If AI agents are already browsing the web, collecting content, and in some cases buying things, someone needs to handle the business end of how the sites they visit are compensated. Cloudflare thinks that someone should be Cloudflare.

## Paying for value, not visits

Roughly a year ago, Cloudflare launched [Pay Per Crawl](https://www.cloudflare.com/paypercrawl-signup/), which let publishers set a price for AI companies to pay when they fetched a page. Now the company is pushing toward [Pay Per Use](https://blog.cloudflare.com/monetization-gateway/), which means publishers get paid when their content actually appears in an AI-generated answer.

To backtrack, under the old model, an AI crawler pays to visit your site, whether or not it does anything useful with what it finds. Cloudflare says it’s already testing this with [Ceramic.ai](http://Ceramic.ai) and [You.com](http://You.com), each running slightly different versions of the concept.

> Instead of charging for access — which is basically a toll booth — publishers are charging for value.

The economics here flip. Instead of charging for access — which is basically a toll booth — publishers are charging for value. That’s closer to how affiliate marketing or licensing deals work, and it’s a much harder problem to solve. It requires knowing which content contributed to which answer, which means an attribution infrastructure that doesn’t really exist at scale yet.

![](https://cdn.thenewstack.io/media/2026/07/957639d0-blog-3342_2-1024x309.png)

Credit: Cloudflare.

## Crawlers need clearer labels

But here’s where things get more technical — and a bit political.

Cloudflare wants AI companies to stop lumping all their crawlers together. Right now, a single bot from a major AI company might be fetching pages for search indexing, model training, and agent tasks all at once. That makes it impossible for site owners to say yes to one use and no to another.

Starting September 15, Cloudflare plans to change the defaults for new and free-tier sites. [AI search crawling stays on](https://blog.cloudflare.com/making-ai-search-smarter/), but training and agent access get blocked on ad-supported pages unless the site owner opts in. Mixed-use crawlers that refuse to separate their traffic get blocked entirely.

The company is clearly taking a shot at Google here, noting that Google’s bundled approach gives it access to roughly twice as much content as AI-native competitors. Separating crawlers’ intent has become a prerequisite for any kind of functioning market between publishers and AI companies. Because if site owners can’t distinguish between “index my page for search” and “train your model on my writing,” they’ll increasingly just block everything.

> Separating crawlers’ intent has become a prerequisite for any kind of functioning market between publishers and AI companies.

## Optimizing for AI answers

Cloudflare is also rolling out a dashboard designed for business teams, called Attribution Business Insights. Think of it as the AI equivalent of knowing your Google Search Console numbers, except the “search engine” is now ChatGPT or Perplexity or whatever agent your reader happened to ask.

On top of that, Cloudflare is introducing Answer Engine Optimization (AEO). The idea is that ranking in Google is no longer enough; for publishers to succeed, they also need to understand how and where their content gets cited in AI-generated responses. That’s a different optimization problem than SEO, and right now almost nobody has good tooling for it.

## Infrastructure as competitive advantage

Cloudflare already sits between websites and the internet. It sees the traffic and knows what changed on a page and what didn’t. It can tell a crawler to come back later because nothing’s new, which, by the way, it says would eliminate over 50% of current AI crawl traffic.

That puts Cloudflare in a unique position. It’s already part of the path between AI companies and the web. Now it wants to become the layer that manages access, attribution, and eventually payments between them. If AI agents become the primary way people find information online, Cloudflare is betting the next battle won’t be over who builds the smartest model but instead over who builds the infrastructure everyone else relies on.

> If AI agents become the primary way people find information online, Cloudflare is betting the next battle won’t be over who builds the smartest model — it’ll be over who builds the infrastructure everyone else relies on.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)