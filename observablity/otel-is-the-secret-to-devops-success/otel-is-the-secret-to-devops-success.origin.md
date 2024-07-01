# OTel Is the Secret to DevOps Success
![Featued image for: OTel Is the Secret to DevOps Success](https://cdn.thenewstack.io/media/2024/06/f56ab0c0-otel-secret-devops-success-1024x576.jpg)
8The old demarcation of “developers write code and operators run code” just doesn’t exist anymore. If you write, design or contribute to an application, you have some responsibility for the application’s execution in production. At some point, you will be called in to diagnose and fix it.

When creating applications, developers need to start with the mindset that the real work begins after code deployment. That’s when developers see how their applications perform in the real world and ensure they deliver positive customer experiences.

By capturing detailed information about code and business processes upfront with [application performance management](https://thenewstack.io/streamlined-apm-integration-in-cloud-native-buildpacks/) (APM) tools, operators inherit all the great, thoughtful work developers do. Operators save time and energy pinpointing a critical issue faster during an incident response. And life becomes easier for both developers and operations with access to information that helps fix errors and latency issues unique to each application.

At its heart, APM is about [enabling DevOps](https://roadmap.sh/devops), and the developers who [instrument better observability](https://thenewstack.io/rethinking-observability/) into the applications they develop put themselves on the forefront of this enablement.

## Dev and Ops: Different Perspectives
Even though developers and operators share common ground, the two still operate from different perspectives. Developers spend their careers creating business-critical applications. For each application written, developers expect to be creator, troubleshooter and fixer.

Developers also want to see the variation between usage and input for the new features as they go into production. Is the application working as expected? Is it providing value to the customer? Have the business processes that the application supports improved?

At the same time, operations takes a holistic view of application and infrastructure performance. Is everything running correctly? Is an infrastructure change affecting application performance? Is this issue impacting other services? Are we meeting customer expectations or contractual service level agreements (SLAs)? If it’s a code issue, who needs access to this information to fix it?

Knowing this, how can we get the development feedback loop and the optimal business metrics to enable true DevOps?

## OTel Pros and Cons
Fundamental to creating high-performance applications that don’t tax resources is learning about application code in production through thoughtful instrumentation such as [OpenTelemetry](https://thenewstack.io/why-the-latest-advances-in-opentelemetry-are-significant/) (OTel). By capturing detailed information about an application’s processes and dependencies while the code is created, developers can save a lot of time down the road when they need to fix issues or improve performance.

OTel supports using automated and manual instrumentation together for the same application. This instrumentation enables developers to add code snippets to capture and send custom metrics specific to their applications.

Automatic instrumentation provides prebuilt libraries or agents that capture standard metrics like CPU usage, memory usage, request latency and error rates. Automatic instrumentation doesn’t require developers to modify their code and is much simpler and quicker to implement but is less flexible.

Manual and custom instrumentation give DevOps teams easy access to detailed information on what happened and why, in a helpful format. Additionally, using OTel helps you design and improve monitoring in local and test environments, so you know what to expect in production. You don’t have different sets of data in different environments, as the tooling is the same across all environments.

However, on its own, OpenTelemetry doesn’t know what’s important to the business. The technology captures SQL queries, HTTP/TCP calls, messaging calls, and hardware and network information. OTel does not capture user IDs, non-generic metadata or any number of things specific to your application and business.

This is where custom instrumentation comes in. Custom instrumentation involves work and time to implement but gives developers the flexibility and control to capture the information necessary for troubleshooting in production.

## A Real-World Example
To understand how this works in practice, let’s look at an online cart checkout. A transaction may hit one endpoint, four endpoints, even 10 or more endpoints. Those endpoints may hit additional endpoints. The application may have a Kafka backplane, a messaging bus backplane, databases or NoSQL database stores, or any number of custom APIs or resources. As customers place orders, the system runs all these business-specific applications and services related to order processing, billing, marketing and fulfillment.

So how can you be certain, as many, many users go through the cart checkout, that when a customer hits the purchase button, it properly triggers completion of order processing, procurement, shipping, billing and whatever else is needed? Most importantly, how do you know that everyone gets billed correctly?

With custom instrumentation, OTel enables you to link all those disparate applications together and get a holistic view of that entire business transaction across all those different services.

OTel acts as a bridge between DevOps, connecting the code internals the dev team is concerned with, with the network traffic data and sources your ops team watches. This pinpoint observability enables DevOps to quickly troubleshoot and resolve issues and ensures application and business processes are optimized and accurate.

Custom instrumentation also enables applications to capture business-specific telemetry data that is critical to how your DevOps team ensures a great user experience.

## To OTel or Not to OTel
Companies with large APM deployments may already have highly skilled developers on staff who can leverage OTel with custom instrumentation to improve DevOps efficiency.

If your developers don’t have the chops to do custom instrumentation, it may be worth having them learn. You can embed custom OTel instrumentation into applications in steps, which spreads the time and costs over the entire development cycle.

Existing APM users have more to consider, starting with the breadth of their APM deployment. Adding OTel capabilities when you’re monitoring thousands of applications is certainly more complicated, and the expense may be viewed as prohibitive. These companies can test the benefits of OTel-enabled APM with subsets of their applications, or use low-cost, open source monitoring alternatives in dev or general availability environments.

## OpenTelemetry for DevOps: What’s Next
OTel is all about standardizing the collection and export of telemetry data to give organizations the flexibility to choose their backend APM or observability solution. With the addition of support for profiling, which dynamically inspects the behavior and performance of application code at runtime, the OpenTelemetry project is expanding capabilities to match commercial offerings.

Continuous profiling gives insights into resource utilization at a code level and allows profiling data to be stored, queried and analyzed over time and across different attributes. This data enables developers and operators to correlate resource exhaustion or poor user experiences across services, with the specific service or pod being affected and the function or line of code responsible for it.

Whether your business is large or small, new to APM or an extensive APM user, OTel helps to deliver the promise of observability with minimal additional code or effort.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)