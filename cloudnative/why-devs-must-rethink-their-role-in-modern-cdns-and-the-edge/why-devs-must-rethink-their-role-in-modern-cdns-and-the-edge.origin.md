# Why Devs Must Rethink Their Role in Modern CDNs and the Edge
![Featued image for: Why Devs Must Rethink Their Role in Modern CDNs and the Edge](https://cdn.thenewstack.io/media/2025/06/59c84e33-zyanya-citlalli-465kpeg2n-q-unsplashc-1024x576.jpg)
When the web was first scaling up, content delivery networks (CDNs) became a way of dealing with the ever-increasing load. Akamai is widely considered the pioneer of CDN technology in the late-1990s, but arguably it’s been overtaken now by younger, more agile CDN competitors. At least that’s the view of [Artur Bergman](https://www.linkedin.com/in/crucially/), co-founder and chief architect at Fastly, which [started out in 2011 as a CDN](https://thenewstack.io/glitch-fastly-developer-experience/) but now [fashions itself](https://www.fastly.com/products) as an “edge cloud platform.”

“Akamai was the first cloud service, the first multitenant cloud service,” Bergman told The New Stack in an interview. “And I think if they had been developer-friendly, then they should have been as large of a player as AWS, right?”

Akamai may not have been the very first cloud service, but it was definitely among the first — and its CDN debuted well before “[cloud computing](https://cybercultural.com/p/018-birth-of-cloud-computing/)” gained traction. It’s also worth noting that Akamai’s original CDN architecture was highly hardware-centric: lots of boxes in data centers. Today’s CDNs, including Fastly and direct competitors like Cloudflare and AWS CloudFront, are software-centric and hence more developer-focused.

Fastly’s about page certainly emphasizes the developer, claiming with typical corporate gusto that Fastly is “where developers dream bigger.”

## The Edge as Part of Your Software Architecture
In the lead-up to this interview, Fastly had sent me a few ideas for talking points. One of them struck me as something that practicing developers might not immediately agree with: “developers are no longer shielded from infrastructure complexity, they’re actively shaping it.” I asked Bergman to unpack that statement.

“…today, the demands of applications require […] developers to really think about how [software] architecture can use the infrastructure correctly.”

– Artur Bergman, chief architect at Fastly
“Traditionally, CDNs and Edge have been under the control of, like, IT or Ops — or security, or both. […] Developers frankly [didn’t] like it, because it just made it harder for them to do their jobs; it’s not something that enabled innovation. I think today, the demands of the applications require […] developers to really think about how […] the [software] architecture can use the infrastructure correctly. Now, the infrastructure should still be operationally an abstraction — they shouldn’t actually have to care about where our PoPs [points of presence — Fastly’s edge nodes] are. They should just care that they’re fast.”

So when Fastly says that developers are “actively shaping” infrastructure, it means that developers must plan for things like low latency in their applications.

“The fact that the edge should be part of your architecture instead of something that’s bolted on afterwards, I think, is something that’s been changing the last 10 years, and is still changing,” added Bergman.

## The Developer’s Burden
That makes sense, but it also adds to the burden for developers. Even without edge networking, devs have a lot on their plate — they might already be using a complex orchestration tool like Kubernetes, one of many frontend framework “[merchants of complexity](https://thenewstack.io/developers-rail-against-javascript-merchants-of-complexity/),” a variety of DevOps tools, and now AI coding tools.

Also, Fastly is not just one product — if you look at Fastly’s product page, you’ll see there’s a vast range of products. A CDN is just one of them; and it’s categorized under “network services” (there are further lists of products categorized under Security, Compute, and Observability).

So doesn’t the sheer number of products Fastly offers contribute to the creeping complexity that developers have been dealing with in recent years?

“I think AI is helping in a lot of regards with this,” Bergman said. “I think that our job is to shield [developers] from the operational implementation complexity. I do think developers’ lives today are very complex — […] even things that aren’t computing, like working in the EU.”

Bergman says that developers still need to be aware of the complexity, but Fastly’s goal is to abstract it away for them.

“The thing that I think it really helps […] is that we take away a lot of the concerns about reliability and performance — which lets engineering teams […] move faster.”

## A Glitch in the Matrix
Occasionally, though, Fastly cuts a product from its suite. Last month, Fastly [announced the closure](https://blog.glitch.com/post/changes-are-coming-to-glitch/) of one of its most beloved developer products: Glitch, a coding platform that Fastly had acquired in 2022. When [I interviewed Fastly co-founder Simon Wistow](https://thenewstack.io/glitch-fastly-developer-experience/) three years ago, I noted that Glitch was a favorite prototyping tool for a wide range of developers — everyone from amateur programmers to professionals.

I asked Bergman why the Fastly acquisition hasn’t worked out, given Fastly’s developer-friendly focus.

“Ultimately, the world — because of AI — has moved on,” he replied, “and the Glitch platform was not built for a world where AI helps you generate code, helps you run it.”

“The Glitch platform was not built for a world where AI helps you generate code.”

– Bergman
In other words, AI “vibe coding” tools — like [Cursor](https://thenewstack.io/5-ways-cursor-ai-sets-the-standard-for-ai-coding-assistance/) and [Bolt](https://thenewstack.io/how-developers-are-using-bolt-a-fast-growing-ai-coding-tool/)— have eaten Glitch’s lunch, at least when it comes to being a platform to prototype new apps. Bergman compared the situation to how StackOverflow was usurped by ChatGPT and other AI chat tools.

## Competing With the Big Platforms
The Glitch closure aside, the company seems to offer everything but the kitchen sink in terms of internet infrastructure. In a recent in-depth analysis of edge computing, my colleague Mary Branscombe [described modern CDNs,](https://thenewstack.io/the-modern-cdn-means-complex-decisions-for-developers/) such as Fastly and Cloudflare, as “the front door for computing infrastructure.” But isn’t that what the big platform companies like AWS, Google and Microsoft do, I asked?

“We both compete and cooperate,” he replied. “At least, Amazon and Google do offer CDN. I think Amazon has the most sophisticated of those offerings, but it is an offering that’s more focused on accelerating media, file downloads, images — and way less on dynamic traffic. But on a meta level, customers are wary of…if you go all-in on the AWS front door, […] you can’t use that to protect your GCP instance, right?”

His point is that enterprises try to keep these worlds separate, because (in Bergman’s words) “if you go all-in on one vendor, over time you will be charged more.”

He says that Fastly can be used as a kind of conduit to the big cloud providers.

“By putting someone like us in front, you can […] send traffic to one provider and traffic to another provider. [And] you know, migration becomes much easier. All of these things are abstracted away.”

## Modern CDNs: Software-First
So back to the topic of developers and their needs. Near the end of the interview, Bergman made the point that “still so many developers are not fully aware of the possibilities” of a modern CDN.

“As an example, of course API requests are HTTP — depending on what they are, you can cache them, you can accelerate them, you can observe them. But a large percentage of mobile API traffic goes directly to a cloud, because they don’t think about it as HTTP. Like, they [developers] know the images should come from an edge, but API calls? They’re just some magic thing that you do, and it goes back [to the cloud]. And of course, [API calls] also benefit from the Edge. So there’s still a lot more education; and I think, from us on the provider side, making it easier for developers to just use it [Fastly] and see benefits.”

It seems like some of the terminology we use in cloud computing — in particular, the CDN acronym — is obscuring what companies like Fastly and Cloudflare (and who knows, maybe even Akamai?) are actually doing these days. As Bergman put it at one point in our conversation, “[we] prefer to solve our problems with software, other than with hardware.”

One thing is for sure: The modern CDN is no longer just a box in a data center close to you. Nowadays, there’s a lot of software running on top of that box.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)