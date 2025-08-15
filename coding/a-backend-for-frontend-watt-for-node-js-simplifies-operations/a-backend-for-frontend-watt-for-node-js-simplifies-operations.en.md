Duesenberg was an American racing and luxury automobile manufacturer founded in 1920. It was unusual in that it shipped with the engine, chassis, frame, tires and wheels, but the buyer had to pay a luxury carriage maker to build the body. Fun fact: Jay Leno has a 1932 Duesenberg SJ Murphy Convertible whose value is difficult to estimate because it’s so unusual, but a 1931 Model J with a disappearing top sold for over $4 million in 2023 at an auction.

That’s what [Watt](https://docs.platformatic.dev/docs/getting-started/quick-start-watt) is to [Node.js](https://thenewstack.io/node-js-24-your-next-big-frontend-upgrade/).

Node.js provides the engine and the raw mechanical parts for things like real-time applications, APIs and [microservices](https://thenewstack.io/introduction-to-microservices/). It’s used for building web apps with RESTful APIs. [Express.js](https://thenewstack.io/a-showdown-between-express-js-and-fastify-web-app-frameworks/), [NestJS](https://thenewstack.io/configure-microservices-in-nestjs-a-beginners-guide/), [Hono](https://thenewstack.io/hono-shows-the-way-for-microframeworks-in-a-post-react-world/) and [Fastify](https://thenewstack.io/introducing-fastify-speedy-node-js-web-framework/) all use Node.js, which can run [JavaScript](https://thenewstack.io/introduction-to-javascript/). It’s even leveraged by JavaScript frameworks such as [Next.js](https://thenewstack.io/next-js-react-router-tanstack-when-to-use-each/), which uses Node.js for server-side rendering (SSR).

Watt makes Node.js more “comfortable” to use, providing structure and automation to building with Node.js. It is the specialized toolkit that automates the assembly of the Node.js parts. Watt, which was created by [Platformatic](https://docs.platformatic.dev/), is a [Node.js application platform](https://blog.platformatic.dev/introducing-the-node-application-platform). It provides a pre-configured and managed instance of an application server, but it also does more. For instance, it helps with building, managing the server, and creating [APIs](https://thenewstack.io/generative-ai-creates-apis-faster-than-teams-can-secure-them/) and microservices.

## A Bridge Between Worlds

Platformatic is an open source development platform that helps developers build and manage Node.js applications. Co-founders [Luca Maraschi](https://www.linkedin.com/in/lucamaraschi/?originalSubdomain=ca) (CEO) and [Matteo Collina](https://www.linkedin.com/in/matteocollina/?originalSubdomain=it) (CTO) created Watt after realizing that enterprises needed help with Node. For instance, many banks use Java as their backbone, Maraschi said.

“What was missing was that bridge to connect those two worlds, the world of developers and the world of operators,” he said. “We knew that something was missing there, and the application server for Node, what was really missing [was] something that could actually harmonize the conversation between developers and operators.”

[![A diagram of Watt and how it interacts with Node.js and frameworks like Next.js](https://cdn.thenewstack.io/media/2025/08/1a45e74a-watt.jpg)](https://cdn.thenewstack.io/media/2025/08/1a45e74a-watt.jpg)

Image via [Platformatic’s blog](https://blog.platformatic.dev/introducing-the-node-application-platform).

They started working on Watt, so named because they believed it was “the second greatest revolution in the Node world,” Maraschi said.

“As the steam engine changed the industrial world for better, we thought that an engine that would change the whole game in the Node enterprise ecosystem was required,” he said.

It’s almost like a language that creates a common bridge between the two spectrums of the enterprise world, he added.

“In Java, you have application servers like [JBoss](https://thenewstack.io/red-hat-jboss-data-grid-not-just-storing-java-objects-anymore/), [WebSphere](https://www.ibm.com/products/websphere-application-server) and [WebLogic](https://www.oracle.com/java/weblogic/), to name the three most popular,” Maraschi said. “Node needed something that would create the same comfort. We knew that there were some functionalities that were required — like logging, metrics, telemetry, multi-threading, all the functionalities that Watt provides us out of the box — they should have also provided for the JavaScript and Node world.”

## Examples of Problems Watt Solves

Collina pointed to the problem of [event loop block](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop).

“It’s essentially very easy for developers to self-‘denial of service’ their systems by misusing Node.js and essentially make the event loop block; and because of that problem, if the event loop is blocked, nothing is getting executed,” he said.“So doing any work, anything going there, is essentially bad.”

It’s a problem that can only be mitigated and prevented, Collina added, but developers struggle with it.

“Essentially, recycle that app,” Collina said. “You tell [it to] gracefully close that app, stop sending requests to that system and then start a new one in its place, therefore keeping the event loop healthy and the system healthy.”

In their consulting work with Platformatic, Collina and Maraschi found this was a big problem, he added. Rather than force developers to change their code, Platformatic developed a self-monitoring system that detects when an event loop of a Node.js application is getting blocked.

“They are either not willing to implement it, or they don’t know how to do it, or, even worse, their framework does not support it, and then that is the worst possible situation, because if their framework does not support a way to do this safely, then they are essentially on their own,” Collina said. “In order to implement this kind of solution by hand, you need a little bit of ‘underneath’ knowledge.”

A key feature of Watt is that it takes your application and runs in a thread.

“By having this duality, we can do a lot of things that normal Node applications cannot do because we have essentially an embedded monitor for this system,” he said.

Watt also supports a socket option — a configurable parameter that allows an application to modify the behavior of a network socket — called `SO_REUSEPORT` from the Linux kernel. It allows the system to run multiple, separate processes to bind to and listen on the same port. It helps performance when there is high traffic, making it more resilient and performant. `SO_REUSEPORT` was recently added to Node.js.

## A Backend for the Frontend

Watt supports JavaScript out of the box, with full JavaScript compatibility with all of its features. Among the frameworks it supports are Remix, Astro and Next.js, as well as Node.js apps with TypeScript.

“If you want to run Next.js on [Kubernetes](https://thenewstack.io/kubernetes/), this is probably the tool you should be using,” Collina said. “It has all the things working out of the box. … For a lot of companies, this is a big struggle, especially with Next.js, but also with all the other frontend frameworks.”

There’s also an adapter for [Apache Kafka](https://thenewstack.io/the-new-look-and-feel-of-apache-kafka-4-0/), which is a distributed event streaming platform for building real-time applications.

In addition, Watt supports serverless functions with a Platformatic tool called [AI Warp, an AI-gateway](https://blog.platformatic.dev/ai-warp-1-0-0).

Although Watt is a backend tool, it significantly helps [frontend developers](https://roadmap.sh/frontend) by dramatically speeding up their workflow and reducing development bottlenecks. For instance, Watt can generate a fully functional API from a database schema. This means frontend developers don’t have to wait for the backend team to build an API before they start building and testing their user interface against a real API.

Frontend developers also can use it to create a full-stack application for a proof-of-concept without a dedicated backend person.

With Watt, the creators’ goal was to keep the backend extremely close to the frontend to create the best performance.

“We actually believe that with these modern applications, the backend and frontend blend into this full stack,” Maraschi said. “That was the promise that was made to the enterprise, this full-stack application.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)