I’ve always [liked Markdown](https://thenewstack.io/obsidian-and-the-case-for-using-more-markdown/) for both clarity and brevity, and now more LLM agents will appreciate it, too. In response to the growing number of LLM agents making searches, [Cloudflare’s network now supports real-time Markdown conversion](https://thenewstack.io/cloudflares-markdown-for-agents-automatically-make-websites-more-aifriendly/) [at the source](https://thenewstack.io/cloudflares-markdown-for-agents-automatically-make-websites-more-aifriendly/).

Let’s look at a less busy page than the one they suggest in their own documentation, and ask `curl` for a request with Markdown. If we ask for verbose mode as well, we can see a bit more coming in:

![](https://cdn.thenewstack.io/media/2026/02/27fb2f35-image-1024x74.png)

We can see both the extra headers, including the `x-markdown-tokens:`

![](https://cdn.thenewstack.io/media/2026/02/acef2ec5-image-1-1024x364.png)

So, assuming that tokens are defined the same way by all LLMs (I don’t believe they are), then we know that swallowing the following data will take 297 tokens of context window space.

If we look at the body response:

![](https://cdn.thenewstack.io/media/2026/02/65ebb53d-image-2-1024x339.png)

This is the HTML representation of the same page:

![](https://cdn.thenewstack.io/media/2026/02/ad12ba03-image-3-1024x393.png)

You can clearly see the four links in either representation. But you can also see bits of the right-hand column (e.g., “Was this helpful?”) have wandered into the Markdown. There is nothing particularly strange about this — although we think the “contents” is just the middle column, exactly what comes back is decided by the page configuration. But we know that spatial information on a web page cannot be transmitted sensibly in Markdown. And agents don’t need that spatial information.

What Cloudflare is doing is perfectly reasonable here, and so are the shouts of “the web must work for agents as well as humans!” But we do need to be a bit clearer about whether the web is *actually* working very well for humans at the moment.

## The web may be the problem

The web has required quite a lot of work to turn it into a shop with financial actions (which it wasn’t built for) or to check user identities (again, that it wasn’t really built for). As actual web use has veered away sharply from the original vision, the average web page has got increasingly complicated.

The point is that a modern web page is designed as a visual experience with plenty of competing tensions; it is not just text content with a fixed, irrelevant visual framing that can be skipped past. If it were trivial to “suck out the contents,” then the ad model would be much easier to suborn than it is.

So while it might be true that much of a website looks like noise to an AI Agent on a limited fetch quest, well, reader, I don’t know how to tell you this, but then that web page is mainly noise to everyone else, too.

While protecting the limited context window of an LLM is sensible, it is clearly not a permanent problem. The bigger problem here is treating agents like they can’t comprehend a website as a whole.

## Intent engineering

Originally, using LLMs was about **prompts****;** then it was about **context;** now it is about [**intent**.](https://natesnewsletter.substack.com/p/klarna-saved-60-million-and-broke) So, to assume an agent has only an extractive need for the web is not really correct. As LLMs only get “smarter,” it isn’t a good idea to restrict how they operate. As I showed [with Claude using GSD](https://thenewstack.io/beating-the-rot-and-getting-stuff-done/), the way to guide an LLM is with a good set of objectives and let it work out the details.

It is quite possible, for example, that an LLM will judge that actually answering the “Was this page helpful?” query would help its overall objectives in improving its data sources. Why would this only be something for humans?

A supermarket requires you to navigate to what you need, whereas an old-fashioned shop with a single counter is much easier for users. And now we use delivery services, we are kind of back to letting an underpaid junior go and fetch all of our shopping. But the supermarket model is closest to how a website works for all users, and the ability to browse similar goods before buying is something an agent can also benefit from. Instead of giving an agent a list of ingredients to buy, just tell it you want to bake a pizza. In other words – focus on the intent.

## Your site can be nicer to agents and humans, too

The world of [progressive enhancement](https://www.gov.uk/service-manual/technology/using-progressive-enhancement) (which was in vogue about a decade ago) recognised that JavaScript was fine, as long as everything worked the same way if JavaScript wasn’t running. It is true that a human likes a button that responds to hovering over it – but these embellishments shouldn’t interfere with navigation.

While some bad sites produce strange alphanumeric enigmas as their URLs, most do just use simple and logical structures like `/products/items` that help both humans and bots to navigate.

If your site says “Call for a Quote,” we already know OpenClaw will do just that. It is no longer the case that you can put your hands up and say, “Fleshy humans only from here on in.” So maybe now is the time to design with a little more transparency.

If you find you need to give bots specific endpoints to avoid “UI clutter,” it might be better to address the bad UI first before worrying about bots. Ironically, most LLMs can analyse, interpret, and assist in the creation of websites fairly well.

## Using microdata for a limited win

I really haven’t noticed much use of [Schema.org](http://Schema.org) markup, and giving machine readers cues about content is slightly dated, as LLMs’ very internal structure is a vast network of semantic relationships. Nevertheless, using microdata is not expensive. Let’s look at an early film catalogue example they give:

Starting with the undecorated:

```

<div> 
   <h1>Avatar</h1> 
   <span>Director: James Cameron (born August 16, 1954)</span> 
   <span>Science fiction</span> 
   <a href="../movies/avatar-theatrical-trailer.html">Trailer</a> 
</div>
```

This can be better defined by a fixed scope:

```

<div itemscope itemtype="https://schema.org/Movie"> 
  <h1>Avatar</h1> 
  <span>Director: James Cameron (born August 16, 1954)</span> 
  <span>Science fiction</span> 
  <a href="../movies/avatar-theatrical-trailer.html">Trailer</a> 
</div>
```

I’ve not used an LLM that would need this help, but it might well improve search efficiency.

[Nate Jones](https://www.linkedin.com/in/natebjones/) has this about right when he [states that](https://natesnewsletter.substack.com/p/klarna-saved-60-million-and-broke) “prompt engineering told AI what to do. Context engineering tells AI what to know. Intent engineering tells AI what to want.”

Don’t treat web browsing by AI agents as a Delta Force raid on a webpage, whose mission is to smuggle the information out as quickly as possible. Step back and give the agents meaningful objectives.

And on the other hand, if your website is designed to bamboozle users and you are worried about agents bypassing it, check your priors.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)