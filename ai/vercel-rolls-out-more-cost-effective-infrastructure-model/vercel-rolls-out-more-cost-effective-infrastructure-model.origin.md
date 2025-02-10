# Vercel Rolls Out More Cost-Effective Infrastructure Model
![Featued image for: Vercel Rolls Out More Cost-Effective Infrastructure Model](https://cdn.thenewstack.io/media/2025/02/4b6a91e4-vercel-introduces-fluid-1024x684.jpg)
Gone are the days of the edge worker/runtime for frontend cloud hosting provider Vercel, CEO [Guillermo Rauch](https://www.linkedin.com/in/rauchg/) tweeted early yesterday.

“In fact, as of last week, all Edge middleware runs on Fluid in the Vercel cloud,” he added.

Edge Network is a Vercel offering that is both a Content Delivery Network (CDN) and a globally distributed platform for running compute in regions around the globe.

[Fluid](https://vercel.com/fluid) is a new web application infrastructure model that purports to blend the best of servers and serverless, while offering efficient resource utilization and — more importantly for Vercel customers — reduced costs.
Fluid is multiregion, but that doesn’t mean “dozens or hundreds of [CDN edges](https://thenewstack.io/from-cdn-edge-to-fornax-toward-a-next-gen-edge-cloud-platform/),” Rauch wrote.

## ‘Edge Not for Apps, APIs, Databases’
[Edge computing](https://thenewstack.io/edge-computing/what-is-edge-computing/) is best for routing, static assets and pre-renders, but it’s not for apps, APIs and databases, Rauch stated in his tweet and reiterated in a webcast later that day with CTO [Malte Ubl](https://www.linkedin.com/in/malteubl/).
“The big insight is that your application, [the] real logic, has to run close to the data, because you’re going back and forth as data waterfalls; that’s going to be slow,” Ubl said. “The dream of edge compute, that you suddenly have your data in all these 200 locations, that dream is just not reality.”

Plus, the vast majority of Vercel customers host their data in one location, he added.

“The example I like to give is that Google has eight data centers for Google search,” Rauch added. “Google did pretty well with eight data centers. You’re not going to [copy petabytes of data](https://thenewstack.io/linux-low-level-data-copying-with-dd/) to 200 locations.”

With Fluid, the compute runs closer to where your data already lives instead of “attempting unrealistic replication across every edge location,” wrote [Mariano Cocirio](https://www.linkedin.com/in/mcocirio/?originalSubdomain=de), product manager for CI/CD and Compute, in a [post introducing Fluid](https://vercel.com/blog/introducing-fluid-compute).

“The dream of edge compute, that you suddenly have your data in all these 200 locations, that dream is just not reality.”

— Vercel CTO Malte Ubl
“Rather than forcing widespread data distribution, this approach ensures your compute is placed in regions that align with your data, optimizing for both performance and consistency,” he said. “Dynamic requests are routed to the nearest healthy compute region — among your designated locations — ensuring efficient and reliable execution.”

For enterprise customers, multi-region failover is the default when activating Fluid, he added.

## Fluid Reduces Cold Starts
[Serverless computing](https://thenewstack.io/serverless-computing-in-2024-genai-influence-security-5g/) can suffer from cold starts, which are delays that occur when a function is invoked for the first time or after inactivity.
Serverless functions run in [containers](https://thenewstack.io/introduction-to-containers/). When the function is deployed, the cloud provider packages the code and dependencies into a container. Containers need initialization when a function is invoked, a process that takes time as the container is allocated, initialized, and the code loaded. Also, containers shut down due to inactivity to save resources.

Customers pay for cold starts, though.

![Vercel CTO Malte Ubl introduces Fluid's benefits.](https://cdn.thenewstack.io/media/2025/02/7dc8721e-vercelvideo.png)
Vercel CTO Malte Ubl explains the benefits of Fluid.

“If I turn on Fluid, which I just did, I’m going to send another four requests, 1-2-3-4, they’re all hitting the same instance,” Ubl said. “What you can see in the demo is it counts the total duration of the time the function was alive, in this case, 3.4 seconds. So that’s all I’m billed for. Yes, so you get built for 3.5 seconds instead of 12 seconds […] that’s what Fluid is.”

Fluid reduces the frequency of cold starts by maintaining a ‘warm instance.’ It trades single-invocation functions for high-performance mini-servers, Cocirio stated.

“When cold starts do happen, a [Rust-based runtime](https://vercel.com/blog/vercel-functions-are-now-faster-and-powered-by-rust) with full [Node.js](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/) and [Python](https://thenewstack.io/what-is-python/) support accelerates initialization,” Cocirio wrote. “[Bytecode caching](https://vercel.com/blog/introducing-bytecode-caching-for-vercel-functions) further speeds up invocation by pre-compiling function code, reducing startup overhead.”

As a result, the model maximizes resource efficiency and, in early adopters, has reduced costs by up to 85%, he added.

Fluid bills on actual compute usage, minimizing waste, he emphasized. It also prioritizes using existing resources before creating new instances, “eliminating hard scaling limits and leveraging warm compute for faster, more efficient scaling,” Cociro said. “By scaling functions before instances, Fluid shifts to a many-to-one model that can handle tens of thousands of concurrent invocations.”

## Other Fluid Features
Fluid also [mitigates the risk](https://thenewstack.io/mitigating-risks-in-cloud-native-applications/) of uncontrolled execution, which can drive up costs, Cicirio explained. Functions that are waiting on backend responses can [process other requests instead of wasting](https://thenewstack.io/how-to-identify-your-wasteful-processes/) compute.

Fluid also supports advanced tasks such as [streaming and post-response processing](https://thenewstack.io/real-time-stream-processing-apps-edge-computing-and-kafka/). It’s fully managed, which retains one of the appealing aspects of the serverless model.

Despite that, Vercel is not automatically switching customers over to Fluid — it does require customers to flip one switch in the functions tab under Project Settings to enable it. Rauch explained that Vercel decided not to enable it for everyone because the execution model slightly changes.

“It requires no code changes. We have … mitigations built in. It’s powered by [Node](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/) and Python and more open runtimes to come, and you’re ready to enable it today,” Rauch said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)