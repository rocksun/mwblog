At this month’s [Google](https://cloud.google.com/?utm_content=inline+mention) [Web AI summit](https://rsvp.withgoogle.com/events/web-ai-summit-2025), the primary focus was [client-side AI in the browser](https://thenewstack.io/how-google-is-shifting-ai-from-the-cloud-to-your-browser/) — but we also heard a lot about Model Context Protocol (MCP) and its web variant, [WebMCP](https://thenewstack.io/how-webmcp-lets-developers-control-ai-agents-with-javascript/), agents, and how “compute abstractions” like WebGPU and WebNN are enabling web developers to access device hardware.

After an introduction by Google’s Web AI lead, [Jason Mayes](https://www.linkedin.com/in/webai/), the event kicked off with a keynote from [Parisa Tabriz](https://www.linkedin.com/in/parisatabriz/), vice president and general manager for Chrome and the web ecosystem at Google. Tabriz described this moment in time as a “renaissance of the web,” adding that “many of the tools and techniques of development are fundamentally changing, whether you call it vibe coding or AI assistance.”

With the present job squeeze on web developers and online creators, I’m not sure “renaissance” is the right word here. But I take Tabriz’s point that the way the web is being built and used is fundamentally changing due to AI technologies.

[![Parisa Tabriz at Web AI Summit](https://cdn.thenewstack.io/media/2025/11/2a2de3c0-webai-tabriz2.jpg)](https://cdn.thenewstack.io/media/2025/11/2a2de3c0-webai-tabriz2.jpg)

Parisa Tabriz, VP/GM of Chrome, at the Web AI Summit.

Many in the web industry have [questioned Google’s commitment to the open web](https://thenewstack.io/is-ai-the-ultimate-version-of-google-as-larry-page-wanted/) in the AI era. But according to Tabriz, Google is still committed to investing in the open web.

“In Chrome web ecosystem org, a thing to know, to take away, is that we are super committed to continuing to invest in an open, interoperable Web,” she said.

> Google is “super committed to continuing to invest in an open, interoperable Web.”  
> **— Parisa Tabriz, Google Chrome VP/GM**

She cited WebAssembly — “it’s all about bringing desktop-class power to the browser” — and WebGPU as examples of technologies that her team has been improving recently.

She also referenced the built-in AI APIs that were added to Chrome last August, along with the release of Gemini Nano — Google’s main on-device model — as a built-in feature in Chrome last June. All these features are outlined in Google’s “[AI with Chrome](https://developer.chrome.com/docs/ai)” web page.

## Democratizing AI Development Through the Browser

Tabriz framed the Web AI movement as a kind of democratization of AI.

“It [Web AI] really is around, how do we democratize AI to ensure that new capabilities are more accessible and efficient, with a goal of making AI available on any device, in any browser, anywhere.”

Interestingly, this language mirrors a [May 2017 blog post](https://blog.google/technology/ai/making-ai-work-for-everyone/) from Google CEO [Sundar Pichai](https://www.linkedin.com/in/sundarpichai/), entitled “Making AI work for everyone.” As Pichai wrote at the time, “the more we can work to democratize access to the technology [AI] — both in terms of the tools people can use and the way we apply it — the sooner everyone will benefit.” Note that this was a month before the publication of the now famous “[Attention Is All You Need](https://arxiv.org/abs/1706.03762)” academic paper, authored by multiple Google employees, which inspired OpenAI to start building what became ChatGPT.

My point is, while sometimes we can fault Google on its execution of AI technology (just google “AI Overviews glue pizza”), you can’t fault the company’s consistent vision for AI — up to and including Tabriz saying that Web AI aims to make AI available on any device and any browser.

## The Future of the Browser in the AI Era

Tabriz then talked a little about the future of the browser in the AI era. She said that the browser is shifting from a “window to the web that renders pixels to a … partner platform for productivity.” She noted that “the browser has become the new endpoint” for Chrome’s enterprise customers, given that so many people now work in browsers every day (“at least on the desktop,” she qualified).

> The browser is shifting from a “window to the web that renders pixels to a … partner platform for productivity.”  
> **— Parisa Tabriz, Google Chrome VP/GM**

As for developers, Tabriz sees “strong interest” in “on-device AI and hybrid solutions.”

She finished with three predictions for the future of the Web:

1. **More proactivity:** “It’s not just going to react to user queries, it’s going to understand user intent.” This, of course, is also where [AI agents](https://thenewstack.io/the-agentic-web-how-ai-agents-are-shaping-the-webs-future/) come in.
2. **More personalized, dynamic experiences:** In particular, Tabriz talked about “dynamic user interfaces that will be [AI] generated and actually adapt to what is best suited for the individual,” which suggests on-demand websites, or at least web UI layers customized to each user.
3. **New forms of human-AI collaboration:** Here, she referenced the [recent integration of Gemini in Chrome](https://thenewstack.io/chrome-switches-on-ai-the-future-of-browsing-begins-now/) “as a browsing assistant.”

[![Parisa Tabriz at Web AI Summit](https://cdn.thenewstack.io/media/2025/11/e857e98d-webai-tabriz1.png)](https://cdn.thenewstack.io/media/2025/11/e857e98d-webai-tabriz1.png)

Parisa Tabriz at Web AI Summit.

## The Developer Playbook for Web AI

Later in the Web AI Summit, we heard more about how developers can approach building browser-based AI applications. [Kenji Baheux](https://www.linkedin.com/in/baheux/), a product manager for Chrome who works on Web AI initiatives, gave [a useful presentation](https://docs.google.com/presentation/d/1wTRhaujJnJDxhhuG7KNhHfBl_2wQ0yqIX1V7xs4OesI/edit) outlining his ideas for a Web AI playbook — in other words, a guide for developers.

Baheux talked about two main approaches to Web AI development. The first, “the paved road,” is about using existing frameworks (including perhaps [Antigravity](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/), an “agentic development platform” Google released just this week) and the built-in AI APIs for Chrome. With this approach, developers needn’t worry themselves about GPUs — or indeed WebGPU.

“This is clearly the path of simplicity and speed, and it’s designed for the builder who wants to ship valuable AI features without having to worry about the AI infrastructure or the stack,” Baheux told the Web AI Summit audience.

[![Web AI pathed road](https://cdn.thenewstack.io/media/2025/11/47b78531-webai-paved-road.png)](https://cdn.thenewstack.io/media/2025/11/47b78531-webai-paved-road.png)

Web AI paved road. (Source: Kenji Baheux)

He then presented the other path, which is actually *a field* in this metaphor. “The open field” enables developers to access the device hardware, which means getting your hands dirty with the “low-level APIs” of Wasm, WebGPU or WebNN.

“This is the path of maximum flexibility and control,” explained Baheux, “and it’s essentially designed for two key groups. It’s for the builders that need to deploy their own custom models, or maybe some people that want total control over the whole AI stack. And second, this is also the workshop for … the folks that build frameworks [or] tools, so that they can expand the scope of the paved road by providing easy-to-use solutions.”

[![Web AI open field](https://cdn.thenewstack.io/media/2025/11/64171b87-webai-open-field.png)](https://cdn.thenewstack.io/media/2025/11/64171b87-webai-open-field.png)

Web AI open field. (Source: Kenji Baheux)

Later in his talk, Baheux noted that we also need new design patterns for AI-fueled web applications. He said that with client-side AI, “you can be more proactive.” He said the biggest mistake developers have made so far with AI is to add an “AI feature trap” to their site — for instance, an intrusive chatbot that interrupts the user’s flow.

“I think the better approach is to be subtle and helpful,” he said. “The goal is really to augment the workflows your users already have, so that you have AI that disappears into the background.”

[![Kenji Baheux at Web AI Summit](https://cdn.thenewstack.io/media/2025/11/17f97596-webai-summit-kenji.jpg)](https://cdn.thenewstack.io/media/2025/11/17f97596-webai-summit-kenji.jpg)

Google PM Kenji Baheux at Web AI Summit.

## Conclusion

Web AI as a specific type of AI application development is clearly playing to Google’s strengths — its dominance in the web browser market (which OpenAI and other AI companies are coveting with [their new browsers](https://webtechnology.news/a-new-web-browser-from-openai-initial-reactions-to-atlas/)), its ability to mold emerging web standards like WebGPU and Wasm to its vision, its web engineering capabilities and its increasingly sophisticated AI models and tooling (Gemini and tools like Antigravity).

The counterpoint is that many developers might still prefer to rely on cloud computing — server-side AI — to power their AI apps. But personally, I see a lot of potential in on-device AI, in large part because it plays beautifully into the strengths of the web platform itself — deployability, user privacy and (most of all) openness.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)