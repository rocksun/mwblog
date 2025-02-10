# How a New Breed of Sync Engines Solves Frontend Problems
![Featued image for: How a New Breed of Sync Engines Solves Frontend Problems](https://cdn.thenewstack.io/media/2025/01/776ff0d3-alex-shuper-ehko-zsjnoi-unsplashb-1024x576.jpg)
Most modern software is built on a standard three-tier architecture — sometimes referred to as the [REST](https://thenewstack.io/happened-rest-world-containers-data-streaming/) architecture — composed of a client, an [API](https://thenewstack.io/apis-are-quickly-becoming-the-latest-security-battleground-and-nightmare/) server that exposes APIs that the client calls, and a database. But some web developers are turning to [a new generation of sync engines](https://thenewstack.io/the-vintage-technology-that-speeds-up-modern-web-apps/) as an alternative.

Under the three-tier architecture, a change triggers the client to send a request to the API server, which stores the request in the [database](https://thenewstack.io/database-trends-a-2024-review-and-a-look-ahead/). If another client calls and makes a request, the API server gets it out of the database and sends a response, explained [Aaron Boodman](https://www.linkedin.com/in/aaron-boodman/), CEO, founder and partner at [Rocicorp](https://rocicorp.dev/), a small partnership that builds developer tools.

Boodman is a software engineer who helped build Google Chrome. He has worked on sync engines his whole career.

“All that’s happening at the lowest level is [that] these requests are getting sent from the client, asking the server to do something, and the servers replying with the answer. And these requests are totally stateless,” he said. “Every single request is totally separate from every other request, and it’s an incredibly simple architecture. But it’s too simple for what people are trying to build. Where you want the UI to be fast, you need the data to be on the client before the user asks for it.”

“Where you want the UI to be fast, you need the data to be on the client before the user asks for it.”

– Aaron Boodman, CEO of Rocicorp and sync engine developer
A sync engine provides an alternative approach. Sync engines are software that’s designed to synchronize data between multiple devices or services. Part of the sync engine resides on the client and part is on the server. Sync engines provide a long-term connection between the client and the server.

What makes it fast, though, is that the server sends information to the client before it asks for it, so that it’s available when the client wants it, Boodman explained.

## The Problems With Sync Engines
One reason that sync engines haven’t been widely deployed previously is that there hasn’t been a general-purpose sync engine on the market. [Replicache](https://replicache.dev/), which Rocicorp started five years ago, was one of the first general-purpose sync engines on the market, Boodman said. It’s used by the frontend cloud provider [Vercel](https://thenewstack.io/introduction-to-vercel-frontend-as-a-service-for-developers/) and the deployment tool SST.

But it’s difficult to integrate Replicache into products, he added. There’s a huge setup cost to get it started. Another problem they’ve seen over the years is that it’s not general purpose enough.

“Current sync engines, including [Replicache](https://replicache.dev/), are fundamentally constrained by the fact … that they sync the data onto the client ahead of time,” he said. “You can try to make the network communication as fast as you as you can. But, like, the client and the server are far apart. They’re often on different continents, you know, and it takes time for data to travel the distance.”

In order to get faster than that, you have to send the data to the client ahead of time so that the client already has what it needs, he said. Then the question becomes *which* data should the developer send.

“We can’t send it all to the client. Typically, there’s way too much to send to the client; it won’t even fit on the client,” he said. Plus, it takes time to send data, and that can slow down the app’s startup, he added.

There’s also the issue of authorization: Obviously, you can’t send other people’s data to the client. Developers must try to send only the data that the app needs.

“There’s this interesting trade-off where the standard architecture, the REST architecture, … it only downloads the data you asked for, so it never over-downloads,” Boodman said. “But then everything is slow because you can’t see the data until you download it. Sync engines download everything. […] So everything is fast, but it only works for applications where you have a small amount of data, where it’s reasonable to download everything.”

That’s a fundamental problem with sync engines that has held them back for years, he said.

## A New Breed of Sync Engines
With [Zero](https://zero.rocicorp.dev/), the company’s latest open source sync engine, Boodman and his team are attempting to solve this challenge.

“It’s built on a new foundation. We call it query-driven sync,” he said.

Instead of downloading all the data the user has access to, or attempting to cut up the data, the application developer performs a normal SQL query indicating what they want to sync. The query can be for a rich data set. While developers can do that today with a REST architecture, the difference is that Zero syncs that query so it live-updates.

Zero is “built on a new foundation. We call it query-driven sync.”

– Boodman
“The application can display the result, and then if it changes the query, the data will automatically come back to the client, and the UI will automatically show the new data without the developer having to do anything,” he said. “They don’t have to write any code to do these live updates. It just happens magically.”

But it goes a step further. Once the data is downloaded into the device and is syncing in Zero with the query, if the developer does a new query that can be answered by the data already on the device, Zero will automatically use that data that’s already on the device to answer the query, without sending a new request to the server, he explained.

If the answer can’t be found in the original data, then it falls back to the server and fetches results, he said.

“This provides this really nice framework where developers can build applications using queries, which is the normal way that they’re used to doing it,” he said. “They can describe data that’s likely to be needed using queries, but they’re not constrained to that. The user […] can still access all the data in the entire application and it doesn’t have to be synced ahead of time. So it enables all the benefits of sync engines, all the UX benefits of sync engines, and the DX benefits of sync engines, the developer productivity benefits, but it doesn’t require downloading all the data up front.”

Zero is one example of a [new generation of general purpose sync engines](https://gist.github.com/pesterhazy/3e039677f2e314cb77ffe3497ebca07b), Boodman said. Other new products include [Power Sync](https://www.powersync.com/), [Electric SQL](https://electric-sql.com/), [Convex](https://www.convex.dev/sync) and [Jazz Tools](https://jazz.tools/).

Currently, Zero is available in alpha, which was released at the end of 2024. It’s more for enthusiasts, Boodman said. A beta of Zero designed for broader adoption is expected to be ready later this year.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)