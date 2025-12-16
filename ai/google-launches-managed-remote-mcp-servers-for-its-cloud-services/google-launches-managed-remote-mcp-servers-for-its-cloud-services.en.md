Model Context Protocol (MCP) has become the de facto standard for large language models (LLMs) to interact with third-party services, and to enable this, those third-party services must offer an MCP server that the LLM can connect to. At this point, even as MCP has barely turned a year old, virtually every online service features an MCP server. Today, [Google](https://cloud.google.com/?utm_content=inline+mention) is [extending its MCP support](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services) by offering [fully managed MCP servers](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services) for many of its Google and Google Cloud services — with many more to come.

Until now, developers had to use Google’s community-built local servers or deploy open source solutions, which, as Google notes, were often difficult to install and manage. By offering these new managed MCP servers, Google is removing all of this additional work, making it far easier for a developer to build an agent that is backed by Google’s new Gemini 3 model, for example, and that connects to both the BigQuery data service and Google Maps to enrich this data with geospatial information.

“With these new and extended MCP capabilities, we are ensuring developers and agents can easily interact with data and take actions too. Google is committed to leading the AI revolution not just by building the best models, but also by building the best ecosystem for those models and agents to thrive,” [Michael Bachman](https://www.linkedin.com/in/michael-bachman-07aa821/), Google’s VP and GM of Google Cloud, and [Anna Berenberg](https://www.linkedin.com/in/annaberenberg/), Google Cloud engineering fellow, write in today’s announcement.

BigQuery and Maps are among the first services to get the new managed MCP servers, together with the Google Compute Engine (GCE), which will allow agents to manage infrastructure workflows and provision and resize instances, for example, as well as the Google Kubernetes Engine (GKE), which will offer a server that allows agents to work with the Kubernetes and GKE APIs.

Here are the other services that will also get MCP support in the coming months:

* **Projects, compute and storage:** Cloud Run, Cloud Storage, Cloud Resource Manager
* **Databases and analytics:** AlloyDB, Cloud SQL, Spanner, Looker, Pub/Sub, Dataplex Universal Catalog
* **Security:** Google Security Operations (SecOps)
* **Cloud operations:** Cloud Logging, Cloud Monitoring
* **Google services:** Developer Knowledge API, Android Management API

To discover, govern, use and monitor these services, Google is using the Cloud API Registry, which is still in preview. The Registry will provide all the details of which APIs and tools are available for the agents to use (and which features of these APIs they can access).

Today’s announcement comes a day after Anthropic [donated the MCP protocol specs](https://thenewstack.io/anthropic-donates-the-mcp-protocol-to-the-agentic-ai-foundation/) to the Linux Foundation as part of the new vendor-neutral Agentic AI Foundation (AAIF).

“Google‘s support for MCP across such a diverse range of products, combined with their close collaboration on the specification, will help more developers build agentic AI applications,” said [David Soria Parra](https://www.linkedin.com/in/david-soria-parra-4a78b3a/), a co-creator of MCP and member of technical staff at Anthropic. “As adoption grows among leading platforms, it brings us closer to agentic AI that works seamlessly across the tools and services people already use.”

Google’s Apigee API management service is also getting extended MCP support, allowing enterprises to manage their custom MCP servers and how agents access them from the same tool they already use to manage their APIs.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)