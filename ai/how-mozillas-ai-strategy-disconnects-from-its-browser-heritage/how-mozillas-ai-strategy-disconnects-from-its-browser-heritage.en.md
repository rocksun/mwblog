Last week Mark Surman, president of the Mozilla Foundation, [published an article](https://blog.mozilla.org/en/mozilla/rewiring-mozilla-ai-and-web/) explaining why Mozilla is “doing for AI what we did for the web.” He also pointed to a new [strategy document](https://wiki.mozilla.org/strategy) that is “focused just as much on AI as it is on the web.”

Part of Mozilla’s new AI-centric strategy is an offshoot startup called [Mozilla.ai](http://mozilla.ai). Just a day before Surman’s article was published, I’d spoken to Mozilla.ai’s CEO [John Dickerson](https://www.linkedin.com/in/john-dickerson/). My intention was to find out what, if anything, Mozilla.ai is doing in the “[Web AI](https://thenewstack.io/googles-web-ai-playbook-the-paved-road-vs-the-open-field/)” space that Google has been [busy defining](https://thenewstack.io/how-google-is-shifting-ai-from-the-cloud-to-your-browser/) over the past couple of years. I was surprised to discover that most of Mozilla.ai’s activities are *not* web-related.

## Mozilla.ai’s Mission

Mozilla.ai has been going for nearly three years, but Dickerson himself is relatively new. He was brought in about nine months ago to “reset the company,” as he put it. This entailed shifting Mozilla.ai from an applied R&D organization to a commercial enterprise, albeit as a public benefit corporation. Dickerson says his goal is to produce “a sustainable revenue stream that can support our larger mission around open source AI.”

Dickerson explained that the mission of Mozilla.ai goes beyond just the open web.

> “…it’s kind of like if you take the Mozilla manifesto and you just apply it to AI, as opposed to browsers.”  
> **– John Dickerson, Mozilla.ai CEO**

“Our mission is very Mozilla-y,” said Dickerson. “It’s just about AI as a sort of method to democratize access to information on the internet, information in social networks, and […] push for ownership of your own data, ownership of your own models and control. And so it’s kind of like if you take the Mozilla manifesto and you just apply it to AI, as opposed to browsers.”

Mozilla.ai’s product line is primarily made up of a set of open source AI tools and models. For instance, the company recently released version 1.0 of [any-llm](https://github.com/mozilla-ai/any-llm), “a unified interface that lets developers plug into any large language model.” It is also building the Mozilla.ai Agent Platform, a SaaS product for enterprise that is currently in private beta.

## Where’s the Web?

What seems to be conspicuously absent from the product line Mozilla.ai is building out is…web technologies. Again, I spoke to Dickerson before Surman’s strategy article was released, so I was unaware that Mozilla’s mission is no longer focused purely on the web. But I asked Dickerson what role the web plays in Mozilla.ai.

He pointed to [Wasm-agents](https://blog.mozilla.ai/wasm-agents-ai-agents-running-in-your-browser/), which enables AI agents in the browser, and some of the work they’ve done with the Firefox team (such as the “shake to summarize” feature). But then he reiterated that Mozilla is looking beyond the browser now.

“When it comes to the web in general, the way I see AI and our mission here is, like 20 years ago, 10 years ago, the browser was the way that the world was able to access information. It’s not the only way to access information anymore, right? I can have my own large language model, for example, and that has encoded a lot of the information on the Internet into it, and I can access it [the internet] through that as well. And so when it comes to, again, the higher level Mozilla mission of democratizing access to information and control over information — your own data — it’s not just about the browser anymore, right?”

> “…20 years ago, 10 years ago, the browser was the way that the world was able to access information. It’s not the only way to access information anymore.”  
> **– Dickerson**

I get that Mozilla is trying to adapt to the AI era by broadening its scope, but it strikes me as odd that Mozilla isn’t leveraging its nearly three decades of open web expertise. Especially when Google has been busy promoting its Web AI offerings this year, it’s also become clear to me this year that web technologies will be the “[UI layer](https://thenewstack.io/the-agentic-web-how-ai-agents-are-shaping-the-webs-future/)” of the AI era — just look at OpenAI’s recent moves, first with the Apps SDK ([web apps inside ChatGPT](https://thenewstack.io/openai-launches-apps-sdk-for-chatgpt-a-new-app-platform/)) and then [launching the Atlas browser](https://webtechnology.news/a-new-web-browser-from-openai-initial-reactions-to-atlas/).

I noted Google’s advocacy of “[on-device inference](https://thenewstack.io/how-google-is-shifting-ai-from-the-cloud-to-your-browser/)” and apparent belief that most AI use cases will soon be handled in the browser — thanks in part to the increasing power of small language models. Is Mozilla.ai doing any work on browser-based AI, I asked?

In reply, Dickerson pointed to the [llamafile](https://github.com/mozilla-ai/llamafile) project, an open source project that Mozilla.ai recently announced [it is adopting](https://blog.mozilla.ai/llamafile-returns/), in order “to advance local, privacy-first AI.”

What about [WebMCP](https://thenewstack.io/how-webmcp-lets-developers-control-ai-agents-with-javascript/), a web variant of the Model Context Protocol (MCP) that Google and Microsoft have teamed up to develop?

Dickerson replied that they “haven’t touched WebMCP,” but he pointed to a similar project Mozilla.ai is working on called [mcpd](https://www.mozilla.ai/open-tools/choice-first-stack/mcpd), which is described on its web page as “the toolchain and runtime layer behind the Mozilla.ai Agent Platform.” The ‘d’ appears to stand for ‘declarative,’ because on the project’s [GitHub page](https://github.com/mozilla-ai/mcpd), mcpd is described as “a tool to declaratively manage Model Context Protocol (MCP) servers.”

“A lot of our team believes that there’s a vibrant ecosystem of browser-only, browser-first agentic stuff that’s going to be happening,” he added.

[![Mozilla's choice-first stack](https://cdn.thenewstack.io/media/2025/11/033b829f-mozillaai-nov2025.png)](https://cdn.thenewstack.io/media/2025/11/033b829f-mozillaai-nov2025.png)

Mozilla.ai’s “choice-first stack”.

## The Role of the Browser in the AI Era

In terms of a user interface for agents, I noted that the browser seems to have become a key product in that regard: Google has [added AI functionality to Chrome](https://thenewstack.io/chrome-switches-on-ai-the-future-of-browsing-begins-now/) (and has promised more agentic features to come), OpenAI has launched a brand new browser, Microsoft Edge now has “Copilot Mode,” and others like Perplexity and Atlassian also have [AI browsers](https://thenewstack.io/ai-browsers-dias-chat-based-ui-and-the-future-of-the-web/). The goal in all these cases is clear: The browser becomes the home base for agents.

Needless to say, the web browser as a product line is traditionally Mozilla’s strength. In fact, the organization was named Mozilla in 1998 [because it was](https://web.archive.org/web/19990423143752/http://www.mozilla.org/mission.html) “the generic term referring to web browsers derived from the source code of Netscape Navigator.” So given this heritage, what role does Mozilla’s browser, Firefox, play in the Mozilla.ai strategy?

Dickerson first pointed out that how to define an agent is still an open question — for example, summarizing emails could be done by a browser-based agent every morning, or it could just be a regular feature within a product like Gmail. More importantly, he also thinks the browser itself — as a product category in the agentic era — has also not been nailed down yet.

“The browser is an interesting word there, right? Whatever the portal by which you access information, some of which is online, the person who nails the UI part of that […] is really going to start owning this space moving forward. To be frank, like, I don’t think any of the browsers have totally owned this yet.”

[![Firefox AI](https://cdn.thenewstack.io/media/2025/11/69889f22-forefox-ai.jpg)](https://cdn.thenewstack.io/media/2025/11/69889f22-forefox-ai.jpg)

Firefox’s new “[AI Window](https://blog.mozilla.org/en/firefox/ai-window/)” feature opens up a new window if you want AI features.

It’s a fair point that we don’t yet know what a browser will truly look like once the agent ecosystem has matured — OpenAI’s Atlas is a slick enough browser in 2025, but it’s the same basic paradigm as Chrome (it’s really just a 2000s-era browser with a ChatGPT sidebar). Chrome’s AI features are also basically just chat-based at this point, too.

All that said, I’m surprised Mozilla doesn’t treat Firefox as more integral to its overall AI strategy. Instead, Mozilla seems to believe that the browser is just one of many similar tools in the modern internet. I’m not sure Google and OpenAI see it that way — both of those companies have elevated the browser to a primary product in the AI landscape.

## Why Mozilla’s AI Strategy May Be Flawed

Last month [the Guardian interviewed](https://www.theguardian.com/technology/2025/oct/28/firefox-ai-internet-anthony-enzor-demeo) the general manager of Firefox, Anthony Enzor-DeMeo. When asked about Firefox’s strategy, Enzor-DeMeo noted that “we are slowly launching AI features, but our users have choice. They can turn it off.”

In my view, Mozilla risks being left behind if it doesn’t have a specific AI browser strategy beyond “well, you can turn it off if you want to.” And with all due respect to the “Shake to Summarize” feature in Firefox, it’s not a groundbreaking AI browser technology.

> Why hasn’t Mozilla made its own browser, Firefox, more integral to its AI strategy?

More fundamentally, Mozilla is known for its browsers and its advocacy of the open web. Surely it makes sense to build around your core product, rather than try to own an amorphous “open source AI” market.

While Mozilla.ai is doing sterling work in terms of open source LLMs and AI tooling, I would like to see it more focused on Web AI functionality for developers and consumers alike. It’s a market perfectly suited to Mozilla; and I can’t think of a better organization to compete with Google and OpenAI on this front, if it chooses to do so.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)