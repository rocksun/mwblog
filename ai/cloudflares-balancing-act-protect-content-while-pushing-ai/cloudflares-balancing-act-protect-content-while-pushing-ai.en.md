This year Cloudflare has been outspoken in its support of the web’s content creators in the AI era, who have had to endure wholesale ransacking of their content by [LLM providers](https://thenewstack.io/gpt-5-a-choose-your-own-adventure-for-frontend-developers/) and [AI search engines](https://thenewstack.io/is-ai-the-ultimate-version-of-google-as-larry-page-wanted/) — not to mention [ever-diminishing visits](https://thenewstack.io/google-ai-overviews-and-citations-tips-for-web-publishers/) from web users. A couple of months ago, CEO Matthew Prince declared 1 July to be “[Content Independence Day](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)” and demanded that companies like Google, OpenAI and Anthropic compensate creators for AI crawls.

At the same time, Cloudflare is also working to integrate AI into its content delivery platform in a way that (hopefully) benefits publishers. Late last week it [announced an implementation of NLWeb](https://blog.cloudflare.com/conversational-search-with-nlweb-and-autorag/), a nascent protocol that enables publishers to integrate AI chat into their websites.

We spoke to [William Allen](https://www.linkedin.com/in/williamallen2050/), a VP of product at Cloudflare, about the company’s goal to “make your website conversational for people and agents.”

There are two aspects to Cloudflare’s initiative. Firstly, [NLWeb](https://github.com/nlweb-ai/), an open source project announced by Microsoft in May — it was promoted as a way to “effectively turn your website into an AI app.” The second key technology is [AutoRAG](https://developers.cloudflare.com/autorag/), Cloudflare’s “managed retrieval engine, [that] can automatically crawl your website, store the content in R2, and embed it into a managed vector database.”

> “So the second we saw [NLWeb] announced, we went out and started looking into it, and said: okay, how do we make this simple for Cloudflare customers.”  
> **William Allen, VP of product at Cloudflare**

Think of AutoRAG as a way to scan your website and put it into a vector database, which you can then search and interact with using AI models, Allen told me.

AutoRAG is fairly new — it was [announced back in April](https://blog.cloudflare.com/introducing-autorag-on-cloudflare/) as “a fully managed Retrieval-Augmented Generation (RAG) pipeline.” Combining it with NLWeb makes a lot of sense, as it allows web publishers to effectively add a custom AI search bot to their sites.

“Together, NLWeb and AutoRAG let publishers go beyond search boxes, making conversational interfaces for websites simple to create and deploy,” said R.V. Guha, creator of NLWeb and a Technical Fellow at Microsoft, in a prepared statement for Cloudflare’s post.

“So the second we saw it announced,” Allen said about NLWeb, “we went out and started looking into it, and said: okay, how do we make this simple for Cloudflare customers to be able to implement themselves on their own properties.”

## Yes, There’s MCP

As with nearly everything to do with AI and application development these days, there is an [MCP component](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) to this. “Each NLWeb instance also operates as a Model Context Protocol (MCP) server,” states the Cloudflare blog post. I asked Allen if this means each publisher gets their own MCP server?

He replied that NLWeb gives you a conversational interface to your website, “but it also comes with these endpoints that can be used via MCP servers.” He clarified that, yes, “it’s an MCP endpoint that is particular for your NLWeb instance.”

In other words, external applications can access your website’s content via that MCP connection.

## Cloudflare Wants to Extend NLWeb

The blog post announcement also stated that Cloudflare is “actively working with Microsoft to extend the [NLWeb] standard with the goal to let every site function like an AI app, so users and agents alike can query its contents naturally.” I asked Allen in what ways does Cloudflare want to extend the spec?

“Adoption is probably the biggest and most important thing,” he replied. “Making sure it works for all of our customers, being able to make it easy for customers to drop in their own branding, their own look and feel — so a level of customization.”

Also, Cloudflare would like their users to have the ability to bring in “whatever your favorite AI provider is, seamlessly,” said Allen.

> Cloudflare wants to extend NLWeb by making it “easy for customers to drop in their own branding, their own look and feel.”

While NLWeb does hold a lot of promise (I have spoken to Guha about it, but unfortunately, it was off-the-record), there have been recent concerns raised about its security. Last month, [The Verge reported](https://www.theverge.com/news/719617/microsoft-nlweb-security-flaw-agentic-web) on a security flaw in NLWeb that allowed any remote users to read sensitive files. While that flaw was immediately patched, I asked Allen if Cloudflare is closely monitoring the security aspects of NLWeb.

“Absolutely, and look, [like] a lot of these things, it’s very early in the standard,” he replied, pointing to MCP being another example of a brand new standard that’s getting rapid adoption. “You need to be very careful as you think about bringing these things truly into production, […] in particular with your content. And so we’re launching this, it’s a beta, [and] the beauty of an open standard is that it’s transparent, it’s open. Other people can help kick the tires and find these vulnerabilities, and then anyone out there can submit a PR to make sure that if there is a vulnerability, it’s patched pretty quickly.”

## Cloudflare’s Compensation for Creators Drive

Broadening the conversation, I asked Allen if there has been any progress in the content creator compensation project that Cloudflare CEO Matthew Prince blogged about in July? Prince has continued to do interviews about this, including one last week [with Fred Vogelstein](https://crazystupidtech.com/2025/08/30/cloudflares-ceo-wants-to-save-the-web-from-ais-oligarchs-heres-why-his-plan-isnt-crazy/), in which he references a kind of marketplace for content that Cloudflare would be the middleman for.

“We’re still in the very early days,” said Allen. “I mean, we have this very radical but simple philosophy, which is that when you, as a content creator, put your content online, when you connect your website to the internet, you should get to decide how that content is used for commercial purposes by others, right? So you should be in the driver’s seat.”

He noted that a number of their customers are leveraging Cloudflare’s tools “for the enforcement side” (i.e., blocking content from AI crawlers) and then striking their own deals with various AI companies.

> “…with our early experimentation with pay-per-crawl, we’re still in an early private beta, working very closely with agent developers and other AI companies, as well as the publishers, to find the right balance there.”  
> **– Allen**

“Then in terms of the direct monetization, with our early experimentation with pay-per-crawl, we’re still in an early private beta, working very closely with agent developers and other AI companies, as well as the publishers, to find the right balance there.”

What’s interesting is that Cloudflare appears to be focusing just as much on giving AI agent developers ways to use the content of publishers — with their permission, of course. So it’s not just about protecting websites and adding AI to them. It’s also about throwing a bone to AI developers (as long as they pay for the meat on those bones).

“If you’re building an agent […] and [you] want to bring great content to [your] users, how do we [Cloudflare] make it simple for them? How do we let [you] know that, hey, there’s some new, updated information on this particular website that you should get access to, and make it easy to pay.”

So Cloudflare is treading a fine line here, trying to support content creators but also keeping an open mind about the potential benefits of AI technology for the future of the web. The NLWeb initiative is a good example of that balance — it gives the website publisher a new type of conversational search for their site, while also leaving open opportunities (via the MCP connection) to let external parties access their content too.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)