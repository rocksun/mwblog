# Honeycomb Says Don’t Give Up on Frontend Observability
![Featued image for: Honeycomb Says Don’t Give Up on Frontend Observability](https://cdn.thenewstack.io/media/2024/10/db65cc62-olivie-strauss-olllcdnwqrg-unsplash-1-1024x680.jpg)
[Honeycomb](https://www.honeycomb.io/?utm_content=inline+mention) is emphasizing how a lack of frontend observability is unacceptable and how its fix draws largely from [OpenTelemetry,](https://www.youtube.com/watch?v=I-dAQfzR2Vs&ab_channel=Honeycomb) with the generally available release of [Honeycomb for Frontend Observability](https://www.honeycomb.io/frontend-observability).
With it, Honeycomb engineers designed the tool to debug Core Web Vitals (CWVs) and pinpoint causes — “wherever they occur in your stack,” Honeycomb claims in a blog post — with traces and and other data. Honeycomb also says it is offering “thousands” of free custom attributes.

At issue is how real user monitoring (RUM) tools are always essential for accessing [telemetry](https://thenewstack.io/exploring-telemetry-idf-2016/) for the frontend. But [debugging tools](https://thenewstack.io/debugging-software-using-generative-ai/) are often lacking. When it comes to actually debugging issues in your web app, you’re often left piecing together outputs from browser devtools, with details (if you’re lucky) from customer support tickets to replicate issues locally in hopes of identifying the source of the issue, Honeycomb says.

[Winston Hearn,](https://www.linkedin.com/in/winston-hearn/) senior product manager at Honeycomb, was previously an engineer debugging web performance issues for large media companies. “We ran into this issue often — all the RUM tools available before now collect CWV metrics which helps identify roughly that there’s a problem, but do not give you any helpful context on causes or needed fixes,” Hearn told The New Stack. “At Honeycomb, we have worked closely with our customers’ engineering teams to ensure that they have the data they need to get down to specific causes, allowing them to cut down debugging from many hours or days to a few minutes.”
Without a proper tool, debugging Core Web Vitals (CWVs) to improve scores can be even worse. Literally any asset or third-party service could be affecting the performance of the page, so narrowing in on what’s affecting the metrics is a cycle of guess and check, Honeycomb says.

## Deeper Analysis and Scrutiny
While fields can be divided up by any set of criteria, determining which ones are important for deeper analysis and scrutiny is critical. This is a key functionality of Honeycomb for Frontend Observability. When checking what is happening with poor values for cumulative layout shift and after selecting BubbleUp, Honeycomb analyzes every one of three fields and graphs them, starting with the ones that differ the most, Honeycomb showed in a [demo.](https://www.youtube.com/watch?v=I-dAQfzR2Vs&ab_channel=Honeycomb) The yellow bars represent the poor results, and it appears they occurred after the loading was complete. They are located on the homepage, which is useful information. What element caused them? Further investigation can be conducted by any attribute, Honey cays.

As the demo revealed, other information Honeycomb provides might include the ability to ask more questions such as: Which backend requests are the slowest and, more importantly, why are they slow? By filtering down to the cart page and selecting one of these slow requests, Honeycomb shows the request from the frontend all the way through backend services in a distributed trace. This waterfall view reveals what is slow. It seems there is significant network latency, but the backend was very fast. The trace shows all the services involved and how they fit together. The system as a whole can be understood, as it is generated from distributed traces that start in the browser, Honeycomb says.

Other features Honeycomb communicated that Honeycomb for Frontend Observability offers include:

- Honeycomb connects the frontend to “everything” behind it, providing a full view of the user experience. With OpenTelemetry, the required telemetry data is revealed for the creation of “rich events.”
- Access to all fields and high-cardinality values, spanning application development. WithMetrics can be monitored with all the necessary context to improve them.
In addition to standard OpenTelemetry auto-instrumentation, dozens of attributes have been added, including CWV attribution data and user interaction data such as clicks. This allows for a clear understanding of what is affecting the user experience and where improvements are needed, Honeycomb says.

Custom attributes are free in Honeycomb. Any relevant custom data, such as user authentication status, entry page type, or traffic source, can be added. Data from other tools like Fullstory and Amplitude can also be consolidated, providing rich insights from correlated data, with a default data retention period of 60 days.

The Web Launchpad, at first glance, resembles popular RUM dashboards, offering visualizations of common performance data such as CWVs.

Honeycomb has two primary components: the open source instrumentation package and the Web Launchpad. The Honeycomb web instrumentation package is an open source wrapper around OpenTelemetry’s web instrumentation, providing a vendor-neutral way to instrument web apps in under an hour. It allows the sending of real-time data on every user interaction and the context surrounding it directly to Honeycomb, according to Honeycomb documentation.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)