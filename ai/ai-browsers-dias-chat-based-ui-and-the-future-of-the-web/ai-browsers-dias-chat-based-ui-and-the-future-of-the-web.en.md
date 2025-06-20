The web browser has been *the* core app of the web for more than thirty years. Fundamentally, it hasn’t changed much over that time, but now it’s starting to be reimagined as an AI tool. [Dia](https://www.diabrowser.com/), a new web browser that invites you to “chat with your tabs,” has just been launched as an invite-only beta by The Browser Company. I took it for a spin to find out what AI browsers can offer.

Right now, Dia has fairly basic AI functionality — it opens up a chatbox in which you can either interrogate the content of a web page or get recommendations (for example while shopping on an e-commerce site).

[![Dia welcome screen](https://cdn.thenewstack.io/media/2025/06/b2b36261-welcome-to-dia.png)](https://cdn.thenewstack.io/media/2025/06/b2b36261-welcome-to-dia.png)

Dia welcome screen.

If you’re a developer, you might want to use Dia to query content on a site like Stack Overflow. In this example, I highlighted a phrase I wanted to get further context on and received a useful chat response back.

[![Stack Overflow on Dia](https://cdn.thenewstack.io/media/2025/06/5e29873c-dia-stackoverflow-example.jpg)](https://cdn.thenewstack.io/media/2025/06/5e29873c-dia-stackoverflow-example.jpg)

Stack Overflow on Dia.

I also found Dia useful when you want to know more information about something that isn’t necessarily covered on a particular web page. Using my own internet history website Cybercultural as an example, I asked Dia what exactly happened to the 1990s company PointCast, since that wasn’t covered in [the article](https://cybercultural.com/p/internet-1997/). Dia gave me a satisfying response.

[![Asking for more context on Dia](https://cdn.thenewstack.io/media/2025/06/efa82a43-dia-cybercultural-pointcast.png)](https://cdn.thenewstack.io/media/2025/06/efa82a43-dia-cybercultural-pointcast.png)

Asking for more context in Dia.

Now, in my defence as the page author, I had actually linked to an article about PointCast’s demise, since I felt it was outside the scope of my article. So that information was just a click away for the user, which raises the question: will Dia damage link referrals for website operators? This question is not just about Dia — it’s also a massive concern for web publishers in relation to [Google AI Overviews](https://thenewstack.io/as-search-engines-become-ai-chatbots-what-can-publishers-do/), [Perplexity](https://thenewstack.io/more-than-an-openai-wrapper-perplexity-pivots-to-open-source/), and other [AI search products](https://thenewstack.io/google-ai-overviews-and-citations-tips-for-web-publishers/).

Aside from having the AI chatbot provide further context, you can also question — perhaps interrogate is a better word — the information on a web page. Again using Cybercultural as an example, I challenged the assertion in the article that Microsoft’s vision for DHTML in the 1990s was more innovative than Netscape’s. Dia replied (thankfully) that the page is correct, and explained why.

[![Challenging a website's content on Dia](https://cdn.thenewstack.io/media/2025/06/900ec610-dia-cybercultural-challenge.png)](https://cdn.thenewstack.io/media/2025/06/900ec610-dia-cybercultural-challenge.png)

Challenging a website’s content in Dia.

Dia can also do some nifty recommendation work that is, again, fairly common nowadays in AI chat products like ChatGPT. One example Dia gives on its homepage is asking the chatbot to find a cheaper towel than the one displayed on an e-commerce web page. Dia doesn’t currently have [AI agent technology](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) to go ahead and purchase that cheaper towel for you, but one imagines this functionality will arrive at some point.

[![Dia shopping](https://cdn.thenewstack.io/media/2025/06/13800f91-dia-shopping-example.jpg)](https://cdn.thenewstack.io/media/2025/06/13800f91-dia-shopping-example.jpg)

Dia shopping example.

## How Browsing the Web Is Changing

As you can see, the functionality that Dia offers is still pretty basic in terms of AI functionality — it’s not doing anything that ChatGPT can’t already do. That said, this does feel like a significant change in how we will use browsers going forward. Being able to query a web page, get further information from other parts of the internet to augment a web page, and (eventually, one presumes) having AI agents in the background performing actions for you based on what’s on that web page — these things all change the paradigm of “web browsing.”

For the 30+ years we’ve had web browsers, their primary function has been to take a person from one website or web app to another. Sometimes browser extensions (or add-ons) have extended the functionality of websites, but that’s not the typical use case. For the vast majority of people, browsers are simply there to help you surf from one website to another — or if you’re Gen-Z, a browser is that window that opens up when you click a link in a native app.

> You won’t just be browsing the web now, you’ll be talking with it.

Of course, there have been technical enhancements to the browser over the years. Notably, when Google Chrome launched in September 2008, it had a multiprocess model, where each tab, plugin and extension could run in its own sandboxed process. But aside from browsers getting better and faster, the core functionality has remained the same: browsing the web.

AI browsers, though, might fundamentally change what a web browser is used for. You won’t just be browsing the web now, you’ll be talking with it. Not only that, but eventually AI browsers might do a lot of the browsing for you — it’s likely that within a few years we’ll have access to AI agents that will undertake various actions on the web for you, most likely by using a browser like Dia or a headless browser like Playwright.

## The Future of Browsers

What Dia offers now is just scratching the surface. Some developers have been thinking deeply about how the function of a web browser might change due to AI. [Paul Kinlan](https://www.linkedin.com/in/paulkinlan/) knows a thing or two about browsers: he’s the Lead for Web and Chrome Developer Relations at Google. Kinlan recently started a personal blog called [AI Focus](https://aifoc.us/), in which he’s exploring “how AI is changing the medium of the web and web development at large.”

In one post, he ponders how AI technology could lead to “[super-apps](https://aifoc.us/super-apps/)” — similar to WeChat in China. Essentially, he posits that in the near future you could get dynamically generated UI from prompts to an LLM or chatbot. He says that web technologies could power these new user interfaces:

“HTML, CSS and JavaScript are the most expressive languages available today to render a UI and LLMs are pretty good today at generating them, so to me there is a world where this will be the easiest route to build UI that will service the specific needs of a user request directly in one of these LLMs and you rarely ever need to leave.”

> Are we heading for super-apps instead of standalone web browsers?

That doesn’t sound good for web browsers as a standalone product, but remember smartphone apps already use WebView to open links inside the app — effectively, embedding a browser within an application. So Kinlan’s “super-apps” idea is an extension of that.

Kinlan ended that post with the question: “Who needs a browser anymore?”

Dia, of course, will be hoping to become a super-app itself. As for Google, it will likely upgrade Chrome into an “AI browser” soon, and AI companies like OpenAI and Perplexity will probably release their own browser products (indeed, Perplexity is already [working on a browser](https://www.perplexity.ai/comet), and OpenAI is rumored to be).

We don’t yet know what browsing the web will look like in, say, five years’ time. If I had to guess, I’d say that both Google and OpenAI will have leading AI browser products for consumers that are agentic and chat-based within five years. Regardless, this I know for sure: AI browsers will bring a fundamental change to web browsing; and Dia offers a small glimpse into that future.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)