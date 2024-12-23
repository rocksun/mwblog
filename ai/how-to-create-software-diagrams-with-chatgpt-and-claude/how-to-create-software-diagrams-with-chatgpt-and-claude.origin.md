# How To Create Software Diagrams With ChatGPT and Claude
![Featued image for: How To Create Software Diagrams With ChatGPT and Claude](https://cdn.thenewstack.io/media/2024/10/d670b1c7-steve-johnson-ojagwhv_gey-unsplashb-1024x576.jpg)
In my previous article, about [what ChatGPT and Claude can see on your screen](https://thenewstack.io/what-chatgpt-and-claude-can-see-on-your-screen/) and how developers can make use of it, I mentioned a [browser extension](https://github.com/judell/cnnlite) that enhances the text-only [lite.cnn.com](https://lite.cnn.com/) with images fetched from the full CNN site. It worked nicely, but used the deprecated [Manifest V2](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline). When I had Claude update it to V3, there were some architectural changes that I wanted to diagram. So, in this post, I’ll review the diagramming adventure.

## First Try: ASCII Art
For the first iteration, I referred Claude to the extension’s JavaScript code and asked it to diagram the architecture. That yielded a useful but slightly broken ASCII diagram.

The major difference between the V2 and V3 versions, by the way, was that in V3, the DOM parsing — which in V2 had been happening in the background script — moved to the content script. That’s because the background script was now a service worker (as mandated by V3) that lacked access to the DOM-parsing API.

What else mandated by V3 had been incorporated into the new version of the extension? I asked, and Claude gave me the rundown: the split between `permissions`
and `host_permissions`
, and promise-based messaging. This was a delightful inversion of the pre-LLM process. Before, I’d have read up on Manifest V3, figured out which aspects were relevant to my project, and then worked out how to apply them. Now I had working code with an explanation that I could interrogate in the context of the code.

We call them language models, but when a picture is worth many words, LLMs will happily work with the picture.

The entities and data flows in Claude’s diagram were roughly what I had envisioned. I could have fixed the broken ASCII layout with a bit of hand editing, but that felt silly. I’d rather enlist a proper tool for this job, especially one that could round-trip a concise human-writeable syntax.

## Second Try: Whimsical’s Custom GPT
When I opened [chatgpt.com/gpts](https://chatgpt.com/gpts), Whimsical Diagrams was right there as a featured GPT. So I fired that up, showed it the JavaScript code, pasted in a picture of Claude’s ASCII diagram and asked for improvements. Here was its first attempt.

That seemed much better. I followed the link to [whimsical.com](https://whimsical.com/), where I could have made further edits, but I didn’t find a way to export to a standard format that I could round-trip through other tools. At this point, I remembered a couple of formats I’d used (not very extensively) in the past: [Mermaid](https://mermaid.js.org/) and [Graphviz](https://graphviz.org/).

## Third Try: Mermaid Live
I asked the Whimsical GPT for a representation of the diagram in either of those formats. It gave me Mermaid syntax for the diagram, along with a rendering of it. [Implicitly](https://thenewstack.io/learning-while-coding-how-llms-teach-you-implicitly/), it taught me that the type of diagram I was aiming for had a name: “sequence diagram.”

But this wasn’t the right place to iterate. So I took the code over to [Mermaid Live](https://mermaid.live/edit#pako:eNqVkjtuwzAMhq9CaE5yAA2ZeoOuXgSatpVKlCtRLYogdy_t2C0Mu0M1SXx8P0nxbjC1ZKwp9F6JkV6867OLDYOe0WXx6EfHAphYiOVyK3tf8EIXZIbZFmgfUSh_eCT4TPmN8gGd-YJJZZ-uXzE4X687voU2RXCIVIqFznMLXQ1hdUPN4ZCzrcKCmqMiXK_EY8A2Y4YspVoYREbI09yKaD4JDtsBLJFwPtJessuYuKj8qjxI_EN61v7pZ1v8PvtfE_R8IxTwUWFT7_rF5mQi5eh8q8txn5iNkYEiNcbqtaXO1SCNafihoa5Kev1iNFZypZPJqfaDsZ0LRV91bJ2sm_UMeXwDdoPckA). That proved I could edit the Mermaid code and see a live preview, but this still wasn’t very effective because I didn’t know *how* to edit the code. What other constructs could occur in my sequence diagram, and how might those improve it?

## Fourth Try: Back to Claude
The diagram did a good job of showing data flow among the parts of the extension, but it didn’t represent the processing steps that occurred within the content script: parsing image URLs from the HTML of the full article page fetched by the service worker, and injecting them into the lite.cnn.com page. Claude offered a couple of ideas: Use the “Note over” declaration to place annotations on the diagram, or use “self-messaging” (a message from and to the same participant). “Let’s see it both ways,” I said. Claude obliged, after which I opted for self-messaging. Later, when I got around to reading the Mermaid documentation, I realized that phrase isn’t part of Mermaid’s official lingo. It’s implicit in the sequence diagram’s [reference page](https://mermaid.js.org/syntax/sequenceDiagram.html).

But because the “Note over” declaration is explicitly documented on that page, I suspect that I wouldn’t have dug deeper to find the alternative I like better.

## Fifth Try: Over to ChatGPT
Now I showed the evolving Mermaid code to ChatGPT and asked for suggested improvements. It came up with a good one.

123 |
alt Article not yet loaded CS->>LitePage: Observe page for article load (dom internal) end |
**Jon**: *What does that mean?*
**ChatGPT**: *In a Mermaid sequence diagram, alt is used to represent an alternative flow or conditional block. It allows you to show a decision point where there could be multiple outcomes. In your scenario, it’s like saying:*
“If the article is already loaded, proceed to fetch and inject images.

If the article is not yet loaded, observe and wait until it appears, and then proceed.”

**Jon**: *Does the code actually do that?*
**ChatGPT**: *Yep, look here.*
1234567891011 |
if (document.querySelector('.article--lite')) { fetchAndProcessImages(); // Article is already loaded } else { console.log('Article not found, waiting for content to load'); new MutationObserver((mutations, observer) => { if (document.querySelector('.article--lite')) { observer.disconnect(); fetchAndProcessImages(); // Article has now loaded } }).observe(document.body, {childList: true, subtree: true}); // Watch for DOM changes } |
More [just-in-time learning](https://thenewstack.io/learn-by-doing-how-llms-should-reshape-education/)! I discovered Mermaid’s `alt`
feature by seeing it applied in a meaningful context. And while I’ve never used a JavaScript `MutationObserver`
, I’ve now seen it applied in a context that’s meaningful to me. When I need it, I’ll likely remember this example.
## Final Version: GitHub
At some point on this journey, I also learned that these Mermaid diagrams render in GitHub Markdown. Here’s the final version in the extension’s README.

I’m pleased with the result, which nicely illustrates how the extension works. I’m even more pleased with the process that led to this result. By applying Rules 3 and 4 from [Best Practices for Working with Large Language Models](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) (“Recruit a team of assistants,” “Ask for choral explanations”), I received the diagram I’d wanted. Even more importantly, I learned about supporting tools and techniques more effectively than I otherwise would have.

## Bonus Learning: Mermaid vs. Graphviz
The exercise also got me thinking about uses of Mermaid and Graphviz. When I asked [my assistants](https://thenewstack.io/elevating-the-conversation-with-llm-assistants/) to reproduce the diagram the Graphviz way, it didn’t turn out well. I concluded that a sequence diagram is the right thing for this purpose, and Mermaid is the right way to make it.

Next, I asked both Claude and ChatGPT to summarize the appropriate uses of both formats. I showed each one’s list to the other to arrive at a merged result with three categories: Mermaid-specific, Graphviz-specific and shared. To be honest, a table with three columns was a good-enough representation. But since I was in a diagramming mood, I thought it would be fun to turn that into a Venn diagram.

Amusingly, that isn’t a strength of either of the formats. When I asked ChatGPT how else to render the table, it wrote a Python program to do it, and I arrived at a usable result after a couple of iterations.

Claude went with SVG, which took a number of iterations as well as cross-checks with ChatGPT.

I’m not sure which approach I prefer, but in both cases, I now have working examples that I can return to and learn from. Note that it isn’t an apples-to-apples comparison. The Python version introduced me to a Venn-specific library that makes the diagram straightforwardly human-writeable. For that, the SVG version would need a wrapping library or tool. But if I want to learn aspects of raw SVG, I’ve got a nice starting point, especially since I asked for — and Claude obligingly provided — comments that link SVG features (like `filter`
) to the documentation for those features.

Finally, this experience amplifies the previous episode about what ChatGPT and Claude can see on your screen. As we iterated on these diagrams, I didn’t have to explain in words how each version was coming along. Pasting screenshots was an easier and equally effective way to send feedback. We call them language models, but when a picture is worth many words, LLMs will happily work with the picture.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)