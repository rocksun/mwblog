About two weeks ago, I posted about [websites returning Markdown](https://thenewstack.io/intent-engineering-ai-agents/) to make life easier for AI agents. While agents are already quite proficient at using browsers, it can still be fiddly, lengthy, and time-consuming. I mentioned adding microdata in the HTML as cues to help navigation, but what about allowing them to use MCP directly on the page?

So you see, [WebMCP](https://thenewstack.io/how-webmcp-lets-developers-control-ai-agents-with-javascript/) almost suggests itself. When agents access the DOM, they can do a good job of working through actions using only recognisable components in HTML declarations. Old web testing tools like Selenium worked this way. When a page is fairly regular (which, of course, is exactly what the web has become as it has migrated into a consumer shop front), it is not hard to navigate. But as humans slowly make way for AI agents, and as agents work alongside humans, it makes sense to ease their passage.

So with a Chrome extension, a web page can now act like an MCP server. This approach was fostered by [Microsoft and Google](https://thenewstack.io/how-webmcp-lets-developers-control-ai-agents-with-javascript/) last year. And this is not unrelated to what OpenAI is doing with their [Apps SDK and ChatGPT Atlas](https://thenewstack.io/openais-apps-sdk-a-developers-guide-to-getting-started/). But with WebMCP, the action is client-side.

## The human web user is still in the picture

When I first read about this, I assumed it was purely so an AI agent could “bypass” the web and speak directly to the page in a structured way. But perhaps because Google still needs humans for ad revenue, the human is still very much in the loop.

Because you may be browsing a site and want to ask an agent a question about the page, the agent needs some knowledge of the context before and during your question. You can imagine a user bringing up an AI chat next to a page and asking about something on the screen. So don’t just imagine an agent hitting a headless browser for some task, but also a user interrupting their own browsing session to query the site.

And again, as with [MCP and **security****elicitation**](https://thenewstack.io/model-context-protocol-evolution/), the agent has to be able to return to the user to ask clarifying questions.

The full [proposal](https://developer.chrome.com/blog/webmcp-epp) mentions two APIs: the **Declarative API** for standard HTML-style actions within a page, and the Imperative**API** for complex actions that require JavaScript.

## Using WebMCP with Chrome

While the Chrome examples are pretty recent, some [inquisitive users have already been experimenting](https://ricmac.org/2026/03/11/webmcp-ai-agents-interact-website/) with them.

I’ll look at one example, based on Google’s [current documentation](https://docs.google.com/document/d/1rtU1fRPS0bMqd9abMG_hc6K9OAI6soUy3Kh00toAgyk/edit?tab=t.0). You are obviously at the whim of Google on the bleeding edge, so sign up to their program first to get updates. The first step is to join the early Google Chrome preview program (EPP) via the [invite page here](https://developer.chrome.com/docs/ai/join-epp).

You need Chrome version `146.0.7672.0` or higher. After looking at the version in the About box, only to see it start updating itself as if looking at Schrödinger’s cat, I could see I was good:

![](https://cdn.thenewstack.io/media/2026/03/40465af5-image-1024x200.png)

Then there is a flag we need to flip the “WebMCP for testing” (that is, the service is off by default), you do this by navigating internally with `chrome://flags/#enable-webmcp-testing`

![](https://cdn.thenewstack.io/media/2026/03/121a10e1-image-1-1024x723.png)

And then relaunch with your new choice, checking back to see if the change stuck. In case you were not aware, this is all experimental:

![](https://cdn.thenewstack.io/media/2026/03/8351caa3-image-2-1024x448.png)

You can then install the [inspector, which lets you see the WebMCP](https://chromewebstore.google.com/detail/model-context-tool-inspec/gbpdfapgefenggkahomfgkhfehlcenpd) tools (i.e., registered functions) under the hood.

With that installed, you can go to the [live demo page.](https://googlechromelabs.github.io/webmcp-tools/demos/react-flightsearch/)

You’ll see the mock flight search page (well, I assume it is mock) and the inspector in the panel on the right that effectively picks out the available MCP tools, such as “searchFlights”:

![](https://cdn.thenewstack.io/media/2026/03/62d40e31-image-3-1024x790.png)

So, for example, we could browse “by hand”, as it wer,e on the left side, and use the form to get information about the following flight (I definitely do not recommend this flight right now) :

![](https://cdn.thenewstack.io/media/2026/03/c6a94a0e-image-4-1024x1011.png)

Sadly, this query was not supported:

![](https://cdn.thenewstack.io/media/2026/03/79d69f18-image-5-1024x578.png)

Naturally, I politely obliged the mock app with the required example data (so no, this is not a real flight search,) and wgotet back a mock result screen as intended:

![](https://cdn.thenewstack.io/media/2026/03/f959726d-image-6-1024x832.png)

So we can now use these details within the inspector tool:

![](https://cdn.thenewstack.io/media/2026/03/ec0e2c31-image-7.png)

This returns the same mock HTML page.

Now, if we had an actual agent, we could see the structured reply. I generated a Gemini API key from Google AI Studio, set the key within the inspector, and queried the agent about the flight page:

![](https://cdn.thenewstack.io/media/2026/03/8a18c1d5-image-8.png)

That “interact with the page” is interesting, as for a user, this is a slightly new context to be operating in – to be asking an agent about the page they are looking at. As an aside,e the page on the introductory site [webmcp.dev](https://webmcp.dev/) mentions (and shows) a small blue square at the bottom-right corner of the page to indicate that WebMCP is available. The Google Chrome example doesn’t have this, but these are very early days so that implementations may vary.

After sending my English query, I got this structured result back:

```

User prompt: "What flights are available?"
AI calling tool "listFlights" with {}
Tool "listFlights" result: 
[
 {
  "id":7,
  "airline":"Spirit Airlines",
  "airlineCode":"NK",
  "origin":"LHR",
  "destination":"JFK",
  "departureTime":"08:49",
  "arrivalTime":"07:05",
  "duration":"22h 16m",
  "stops":0,"price":932
 },
 {
  "id":8,
  "airline":"Southwest Airlines",
  etc
```

This looks like the JSON equivalent results for the mock HTML flight results page above. So we can see that we can get back results intended for an AI agent workflow, but we can also have the agent sit with the human and get back a website. In this example, the query front end would present the data neatly and probably ask for a filter to refine the results.

Just as a quick check, the tool sees no WebMCP behind a normal page, in this ca,se The New Stack:

![](https://cdn.thenewstack.io/media/2026/03/e3752daf-image-9-1024x410.png)

So it seems that for now at least, the human web has a stay of execution. Humans can use WebMCP to enhance their web experience, not just by an AI agent.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)