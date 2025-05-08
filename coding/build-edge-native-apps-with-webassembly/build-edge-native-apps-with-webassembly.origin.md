# Build Edge Native Apps With WebAssembly
![Featued image for: Build Edge Native Apps With WebAssembly](https://cdn.thenewstack.io/media/2025/05/50a5769a-ilias-haddad-oekcfimctcg-unsplash-1024x683.jpg)
[Ilias Haddad](https://unsplash.com/@iliashaddad3?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash.](https://unsplash.com/photos/a-man-sitting-on-a-couch-with-a-laptop-OeKCFIMcTcg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
The client-server model is so deeply ingrained in traditional software development that we rarely challenge the dogma. However, edge computing, once consisting only of CDN acceleration and DDoS prevention, has emerged as a third tier of computing.

We are witnessing a transformation in edge computing as more powerful runtimes like WebAssembly enable developers to build entire applications at the distributed edge instead of in cloud services.

What if your app could run in 50 cities simultaneously and without traditional servers? That’s the promise of edge native development, powered by WebAssembly.

**What Is Edge Computing and Why It Matters for WebAssembly**
The client-server model is the classic architecture upon which the Internet was built. Our common online tasks — email, web, messaging, and so on — were all initially conceptualized in that two-part model, in which a user has a client that presents data, but the data itself is managed by (and stored on) servers.

In the late 1990s, a third tier quietly inserted itself between clients and servers. At the time, we called it the Content Delivery Network (CDN). Its initial job was to store static assets, like images and stylesheets, closer to the user. A typical CDN might have dozens, hundreds, or even thousands of [Points of Presence (POPs)](https://networkencyclopedia.com/point-of-presence-pop/) located around the globe. And these small banks of computing and storage power interceded in webpage loads to deliver assets faster. CDN was about improving delivery speed, but only for the assets that do not frequently change.

CDN networks proved good places to run other kinds of operations as well. Over time, CDNs expanded into the security world and became edge providers. For example, their distributed nature meant they could stop Distributed Denial of Service (DDoS) attacks before attackers could take down the upstream servers.

As [cloud providers dethroned on-premise data](https://thenewstack.io/the-architects-guide-to-the-modern-data-stack/) centers, edge providers made gentle forays into hosting compute. By providing simple JavaScript engines embedded in CDN locations, edge companies let customers do lightweight transformations on inbound HTTP requests. Edge compute was used to do things like:

- Issue redirects when the content was relocated
- Manage CORS headers in HTTP requests
- Intelligently route traffic based on location information
Developers loved the model, but the system’s constraints meant only a certain amount of processing could be done at the edge. This opened a new opportunity.

**How Edge Computing Evolved to Support WebAssembly**
Early edge computing — running small JavaScript snippets to alter HTTP requests — is essentially an assistive function. The code executed at the edge was not designed to do any heavy work or return complete results to the user. It was designed to make small decisions to streamline how the upstream servers would handle the request, or to offload some work from the upstream servers by making decisions early. For example, performing authentication at the edge is a small task, but one that (for failed authentication attempts) can offload work from busier and expensive upstream servers.

However, two things held back edge computing. The first was the low amount of [computing power available to edge](https://thenewstack.io/vmware-discloses-its-edge-computing-future/) workers. The second was the dearth of data services running at the edge. It’s hard to do any significant computing when there is no place to store data.

**WebAssembly: Solving Edge Runtime Challenges**
If low compute power is the first problem, then there are two potential solutions: increase the power of the available edge hardware or make the runtimes more efficient. Expanding hardware is necessary anyway, but it tends to move slowly because it is so expensive. While over the long term, edge locations may gain better hardware, in the short term, this solution is untenable.

But the emergence of a faster class of runtimes has changed the game. Fastly was the first to use WebAssembly as an edge runtime with its [Compute@Edge](https://docs.fastly.com/products/compute) platform. Akamai and Fermyon have joined forces to [provide a WebAssembly-powered runtime](https://thenewstack.io/should-you-care-about-fermyon-wasm-functions-on-akamai/) as powerful as Amazon’s Lambda serverless environment, but running on Akamai’s core edge regions. Both Fastly and Akamai now support small snippets of JavaScript code and an increasing portfolio of other programming languages, all running as WebAssembly binaries. Even Cloudflare, a staunch JavaScript advocate, has made forays into multi-language support [backed by WebAssembly](https://developers.cloudflare.com/workers/runtime-apis/webassembly/).

WebAssembly has four virtues when it comes to edge computing:

- It’s secure by default, and is multitenant safe.
- WebAssembly binaries are small, especially in comparison to
[containers and virtual machines](https://thenewstack.io/containers-vs-virtual-machines-another-perspective/)(the technologies behind first-generation serverless). - Programs compiled to WebAssembly can run on just about any hardware and operating system without alteration.
- Cold starting WebAssembly is extraordinarily fast, making it both high-performance and highly scalable.
WebAssembly, a secure and platform-neutral runtime, is opening up the possibility of sophisticated edge computing that may completely replace the server component, in some cases. In addition to accommodating all of the early edge computing use cases, it is robust enough to run distributed content management systems, digital experiences platforms, and AI inferencing without needing upstream support from a cloud provider.

Instead of one centralized bank of compute running in a cloud region, WebAssembly distributed along the edge means tens of thousands of instances of the same application can run spread across the globe, answering requests with jaw-dropping speed. If cloud native computing defines the movement to the cloud, then this emerging trend is aptly named edge native computing.

**Why Distributed Storage Is Critical for WebAssembly at the Edge**
The second requirement of edge native [computing is the need for distributed storage](https://thenewstack.io/what-are-time-series-databases-and-why-do-you-need-them/) that is easily accessible from edge functions.

Cloudflare led the way, introducing distributed key/value storage, object storage, and database storage a few years ago. Akamai acquired Linode, which supplied hefty cloud computing capabilities (which Akamai proceeded to roll toward the edge) and cloud-grade storage. And a host of third parties, including [Harper](https://www.harperdb.io/), [Neon](https://neon.tech/), and [Turso](https://turso.tech/), have introduced edge native SQL databases that solve the data access problems associated with distributed computing. In March of this year, the new [Graft database](https://sqlsync.dev/posts/stop-syncing-everything/) announced a synchronization mechanism ideally suited for serverless workloads at the edge.

**The Rise of Edge Native Applications Powered by WebAssembly**
Combining data access at the edge with the massive improvements in edge computing runtimes, [developers can now build applications](https://thenewstack.io/google-wants-developers-to-build-on-device-ai-applications/) that run distributed along the edge and have little or no reliance on upstream in-datacenter servers. The older client/server model gave way to a client/edge/server model, which has now opened the potential for a distributed client/edge model.

This new edge native approach will not only make distributed computing easy but also be a home base for the emerging inferencing-based AI applications (including agentic workflows). By bringing work closer to the end user, edge applications not only meet speed requirements but also localize information and abide by data sovereignty requirements. All of this will be powered by WebAssembly.

*The owner of TNS, Insight Partners, also invests in Fermyon. As a result, Fermyon receives preference as a contributor.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)