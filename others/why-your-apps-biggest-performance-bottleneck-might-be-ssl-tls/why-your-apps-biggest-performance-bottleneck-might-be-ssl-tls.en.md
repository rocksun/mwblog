Your app is slow. You’ve optimized the database, fixed the N+1 queries and tuned your microservices. But what if the biggest performance tax on your service is hiding in plain sight, in a layer so fundamental that we often treat it as a solved problem?

I’m talking about [SSL/TLS.](https://www.haproxy.com/glossary/what-is-transport-layer-security-tls) For decades, we’ve rightfully treated it as a non-negotiable security feature, the lock icon in the browser, the “S” in HTTPS. We enable it, get our certificate from Let’s Encrypt and move on.

However, this “set it and forget it” mentality is becoming a dangerous liability. SSL/TLS isn’t just a security wrapper; it’s an active, CPU-intensive process that runs on nearly every (new) secure connection flowing through the modern internet.

Consider a busy e-commerce [API handling](https://thenewstack.io/api-management/) 1,000 requests per second. If 30% require new TLS (Transport Layer Security) handshakes, that’s 300 cryptographic negotiations per second, competing with your business logic for CPU cycles. Ignoring its performance characteristics is like trying to build a skyscraper without understanding the geology of the ground beneath it. Sooner or later, the cracks will start to show.

## Anatomy of a Handshake: The Cost of a Secure Connection

[![Initial full handshake](https://cdn.thenewstack.io/media/2025/09/a8e70a26-image1-1024x824.png)](https://cdn.thenewstack.io/media/2025/09/a8e70a26-image1-1024x824.png)

To appreciate the overhead of TLS, we have to look beyond our application code. As engineer Hussein Nasser detailed in his fantastic conference session, “[Anatomy of a Request: Beyond Backend Processing](https://www.haproxy.com/user-spotlight-series/anatomy-of-a-request-beyond-backend-processing),” a single client request is a complex dance that begins long before your backend framework sees it.

Before your app can even process a request, the client and server must complete a multistep negotiation. This isn’t just the three-way TCP ([Transmission Control Protocol](https://www.google.com/search?sca_esv=cda52438cd53ad97&rlz=1C5CHFA_enUS981US981&q=Transmission+Control+Protocol&sa=X&ved=2ahUKEwjUlsvtke-PAxWsLdAFHTcdCDIQxccNegQIRBAB&mstk=AUtExfAw4ANP203AdQXUNkmUu8nlYpUsaDZRdCzyho07a2KrYByZV41jDElYHuJ7tU4ckbBdKyLUQa9cl8MblXNQEhrD90B6UgPf540h0DNk9vi-72XDyBv0NBKZbktaMToLJOoHhM5iNKyMTi-SLz5l1UrqyeDfWo2yb9TtuGpJopaOfCQ&csui=3)) handshake to establish a connection; it’s the subsequent TLS handshake to make it secure. This process involves:

1. **Greeting and negotiation:** The client and server say hello (ClientHello, ServerHello) and agree on which cipher suite they will use.
2. **Certificate exchange:** The server presents its digital certificate to prove its identity. The client must validate this certificate against its list of trusted certificate authorities.
3. **Key generation:** This is the most computationally expensive part. The client and server use asymmetric cryptography (slow, but good for securely agreeing on things with a stranger) to generate and exchange a shared symmetric key. This new key is then used for the actual encryption and decryption of application data (fast, efficient).

Nasser’s deep dive highlights a critical point: This cryptographic dance is CPU-intensive. The complex math of public-key cryptography doesn’t come for free. Every copy, every calculation, consumes CPU cycles that could have been used to serve another request.

Think of the TLS handshake as a mandatory security checkpoint before entering a building. Even the most efficient checkpoint has a processing time. Now imagine that checkpoint at the entrance of your favorite coffee shop: You don’t mind the first time, but you’d notice if you had to repeat it for every visit.

## The Ubiquity Tax: When Milliseconds Become a Crisis

[![](https://cdn.thenewstack.io/media/2025/09/bf8a7480-image2-1024x723.png)](https://cdn.thenewstack.io/media/2025/09/bf8a7480-image2-1024x723.png)

“OK,” you might say, “so a handshake takes a few dozen milliseconds. Who cares?”

You should.

To be clear, you don’t pay this cost for every request — modern protocols reduce that dramatically. Persistent connections (HTTP/1.1 [keep-alive](https://en.wikipedia.org/wiki/HTTP_persistent_connection), HTTP/2 [multiplexing](https://www.haproxy.com/glossary/what-is-http2#binary-framing) and HTTP/3’s [QUIC](https://www.haproxy.com/glossary/what-is-quic)) mean many requests share a single handshake. TLS 1.3 session resumption and [0-RTT](https://www.haproxy.com/glossary/what-is-zero-round-trip-time-resumption-0-rtt) (zero round-trip time) can make subsequent handshakes far cheaper.

The problem is that every new secure connection still incurs this cost, and across a busy system with many short-lived connections, APIs without pooling or clients that can’t reuse connections, these handshakes add up fast — both in latency and in CPU load.

Let’s use conservative, real-world numbers:

* A typical full TLS 1.3 handshake might add 1 or 2 network round-trips (~30-50ms depending on network conditions) plus measurable CPU cycles for cryptographic work.
* Resumed or pooled connections cut that sharply, but in workloads where 20 to40% of requests still trigger a new handshake, that’s a significant tax on your infrastructure.

For example, at 1,000 new connections per second with a 40ms handshake, you’re adding a visible latency bump to each of those connection initiations and a measurable CPU hit to your servers. That CPU work competes with business logic for resources, meaning you either slow down under load or provision more capacity to keep up.

At scale, this has two major consequences:

1. **Degraded user experience:** For connection-heavy protocols like [gRPC](https://thenewstack.io/grpc-a-deep-dive-into-the-communication-pattern/) or applications with many short-lived API calls, handshake overhead can become a big factor in perceived latency.
2. **Increased infrastructure costs:** More CPU spent on cryptographic calculations means more servers are needed to handle the same traffic. That “handshake tax” directly inflates your compute bill.

The key point is that this tax is everywhere — in [HTTPS](https://thenewstack.io/http-3-is-now-a-standard-why-use-it-and-how-to-get-started/), secure database connections, some DNS queries (DoH/DoT) and other protocols. While not every request pays, enough do, so ignoring it can be an expensive mistake.

## When the Foundation Cracks: The OpenSSL 3 Change

This theoretical risk became a stark reality for the entire industry when a critical performance issue was introduced in a library most of us use every day. As explored in a [recent analysis](https://www.haproxy.com/blog/state-of-ssl-stacks), the OpenSSL 3.x release introduced a severe performance regression that perfectly illustrates this danger.

OpenSSL is the cryptographic engine underneath countless web servers, operating systems and applications. The 3.0 release, intended as the new Long-Term Support (LTS) version, had an architectural design choice that caused its performance to plummet — in some multithreaded scenarios, by as much as 99% compared to its predecessor. To make matters worse, performance often decreased as more CPU cores were added, the exact opposite of what you’d expect.

This put organizations in an impossible position at that time: upgrade to the new version for critical security patches and suffer a massive performance hit, or stick with the older, faster version and become more vulnerable. It was a real-world demonstration of how a flaw in this “solved” layer can have catastrophic consequences, forcing companies to consider needing [up to 42 times more hardware](https://www.haproxy.com/blog/state-of-ssl-stacks#:~:text=1/42%20of%20its%20performance) just to maintain service levels. The SSL/TLS layer wasn’t just a tax anymore; it was a roadblock.

It should be noted that the current version of OpenSLL is 3.5 at the time of writing, and is the updated LTS version. It has addressed most of the reported performance issues and is recommended for typical use. However, the dynamic design is still less performant at scale than previous versions.

## What You Can Do About It

The key takeaway is that we must stop treating the SSL/TLS layer as an infallible black box. We need to apply the same rigor to it as we do to our own code. Here are some actionable steps:

1. **Profile beyond your app:** Don’t just assume latency is coming from your database. Use profiling tools to see where CPU time is being spent. You might be shocked to see functions like `SSL_read` or `SSL_write` lighting up your flame graphs.
2. **Know your stack:** What SSL/TLS library are you actually using? OpenSSL? BoringSSL? LibreSSL? AWS-LC? Each has different performance characteristics and a different development philosophy. This choice is a critical architectural decision, not a minor implementation detail.
3. **Tune your system:** At the operating system level, tuning kernel settings related to TCP (buffer sizes, connection backlogs) can help your server handle a higher volume of secure connections more efficiently.
4. **Reduce handshakes:** Implement connection pooling, enable HTTP/2 or HTTP/3, and ensure your clients take advantage of TLS session resumption to minimize the number of full handshakes.

SSL/TLS is the bedrock of secure communication online. But like any foundation, it has a load capacity. By understanding its costs, measuring its impact and making conscious choices about connection reuse, protocol settings and cryptographic libraries, we can minimize the impact of secure communications on our apps.

For a deep dive into the most promising SSL libraries, including tests and comparisons, check out “[The State of SSL Stacks](https://www.haproxy.com/blog/state-of-ssl-stacks)” by Willy Tarreau and William Lallemand.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/02/b9306f49-cropped-10957b1b-screenshot-2025-02-21-at-7.53.08%E2%80%AFam-600x600.png)

Ron Northcutt is the director of technical marketing at HAProxy Technologies, where he focuses on performance metrics, developer content, and deep industry knowledge to drive technical innovation and engagement. With over 25 years of experience in the open source ecosystem,...

Read more from Ron Northcutt](https://thenewstack.io/author/ron-northcutt/)