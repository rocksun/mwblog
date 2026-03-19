[Oracle](https://www.oracle.com/developer?utm_content=inline+mention) released Java 26 on Tuesday, the opening day of its [JavaOne 2026](https://www.oracle.com/javaone/) conference in Redwood Shores, Calif., continuing the platform’s six-month release cadence with a package of incremental but meaningful improvements spread across performance, security, and language expressiveness.

The release delivers 10 JDK Enhancement Proposals (JEPs), touching on things from HTTP/3 networking support to garbage collection efficiency, cryptographic tooling, and an overdue cleanup of the Applet API. Java 26 is not a Long Term Support (LTS) release; JDK 25 held that designation. That means enterprise teams on conservative upgrade cycles will largely sit this one out, but developers chasing the leading edge have plenty to examine, says [Simon Ritter](https://www.linkedin.com/in/siritter/?originalSubdomain=uk), deputy CTO at Java platform provider [Azul](https://thenewstack.io/azul-cto-java-at-30-still-rules-enterprise-dev/).

[Stephen O’Grady](https://www.linkedin.com/in/sogrady/), principal analyst at RedMonk, tells *The New Stack* that this release is all about keeping Java current.

“There are some developer experience and cryptographic improvements, but the biggest takeaways for me are the performance-oriented enhancements — one that improves garbage collection and another for lazy constants that is particularly relevant for AI usage and workloads,” O’Grady says. “Overall, it’s another release focused on moving the ball forward across the board, keeping Java up to date and relevant.”

Oracle frames the release in enterprise terms. “For more than 30 years, organizations have relied on the Java platform and language to help power their mission-critical systems and support the rapid development of applications and services,” says [Arnal Dayaratna](https://www.linkedin.com/in/nextgenai/), research vice president for software development at IDC, in a statement. “By extending Java’s functionality with new features and services such as advanced AI and security capabilities, Java 26 offers organizations a faster path to innovation.”

> “The biggest takeaways for me are the performance-oriented enhancements — one that improves garbage collection and another for lazy constants that is particularly relevant for AI usage and workloads… it’s another release focused on moving the ball forward across the board, keeping Java up to date and relevant.”

Meanwhile, [Georges Saab](https://www.linkedin.com/in/georgessaab/), senior vice president of the Oracle Java Platform and chair of the OpenJDK governing board, ties this release to the AI moment. “The new features in Java 26 reflect Oracle’s commitment to helping customers harness AI and cryptography to build applications that accelerate business growth,” Saab says in a statement.

## Performance takes center stage

There are two JEPs that make the case for Java 26 as a platform that developers should care about, even in a non-LTS cycle.

[JEP 522](https://openjdk.org/jeps/522) targets the G1 garbage collector, reducing synchronization overhead between application threads and GC threads. The practical result is higher throughput with the same hardware, with applications running faster, serving more users, and incurring lower infrastructure costs without requiring architectural changes. For teams running high-concurrency workloads, that’s a meaningful free upgrade on the next JDK bump, Ritter says.

[JEP 516](https://openjdk.org/jeps/516), a [Project Leyden](https://openjdk.org/projects/leyden/) feature, extends ahead-of-time object caching to work with any garbage collector — including the low-latency ZGC. The JEP was introduced in JDK 25 but was limited in GC compatibility; Java 26 closes that gap. It allows the HotSpot JVM to load cached pre-initialized Java objects from a GC-agnostic format at startup, cutting both startup delay and warm-up time.

“One of the things they found was that they had this idea of doing this, but it didn’t work with all garbage collectors,” noted Ritter during a pre-release technical briefing with *The New Stack*. “So, they now have fixed that so it works with ZGC.” For cloud-native applications where cold-start performance directly affects cost and user experience, this matters.

[JEP 526](https://openjdk.org/jeps/526), Lazy Constants, in its second preview, rounds out the performance story. The feature — formerly called Stable Values before being renamed — provides developers a new API for objects that hold unmodifiable data, initialized once on demand rather than at class load time. The JVM treats lazy constants as true constants once set, enabling the same performance profile as final fields while giving developers control over initialization timing.

“The reason for having lazy constants, rather than just final fields, is that with lazy constants, you can have greater control over when the value is set,” Ritter explains. “It’s a nice thing that gives developers greater control over how they can use this and be more efficient.” That flexibility is particularly useful for AI and data-driven applications that need to load large models or configuration data without incurring the upfront cost — a point O’Grady flagged in his assessment.

## Language and library housekeeping

[JEP 530](https://openjdk.org/jeps/530), Primitive Types in Patterns, instanceof, and switch, arrives in its fourth preview. The JEP addresses friction that arises when primitive types interact with Java’s pattern-matching features — edge cases where behavior doesn’t align with developer expectations. It tightens dominance checks in switch constructs, allowing the compiler to catch a wider class of errors at compile time rather than at runtime. Oracle says the work helps streamline the development of applications that integrate [AI inferencing](https://thenewstack.io/scaling-ai-inference-at-the-edge-with-distributed-postgresql/) by making Java more uniform and expressive. The work is less exciting than a headline feature, but matters to developers doing serious work with pattern matching, [Chad Arimura](https://www.linkedin.com/in/chadarimura/), Oracle’s VP of Java Developer Relations, tells The New Stack.

[JEP 525](https://openjdk.org/jeps/525) brings Structured Concurrency to its sixth preview under [Project Loom](https://www.baeldung.com/openjdk-project-loom). The API treats groups of related tasks running across threads as a single unit of work, simplifying cancellation and shutdown handling and reducing the risk of thread leaks. Ritter described the approach as borrowing the structure of try-with-resources blocks.

“You can have a try statement, you can have a set of tasks within that, and then when you get to the bottom of the try block, you know that everything is either going to have completed normally, or you’ve got the ability to terminate some of the threads that are being used internally — and that is much more efficient than the way that we do things at the moment,” he tells *The New Stack*. Its relevance to AI and cloud-native workloads, where multithreaded coordination is endemic, is not incidental.

[JEP 517](https://openjdk.org/jeps/517) adds HTTP/3 support to the HTTP Client API. HTTP/3 uses the QUIC protocol over UDP rather than TCP’s traditional transport, which requires building reliability back on top — but delivers lower latency and better performance for [microservices](https://thenewstack.io/introduction-to-microservices/) and API-driven applications.

Ritter noted the architectural strategy during the briefing: “HTTP/3 uses UDP as the transport protocol rather than TCP, and UDP is an unreliable transport protocol, so they’ve actually had to build a layer on top of that to give it effectively TCP — but I guess it works faster somehow.” For Java developers building networked services, the ability to interact with HTTP/3 servers with minimal code changes is a practical win, he says.

## Security and cleanup

[JEP 524](https://openjdk.org/jeps/524) adds a PEM encoding API for cryptographic objects in its second preview, streamlining how developers handle [cryptographic keys](https://thenewstack.io/akeyless-wants-you-to-throw-away-the-encryption-key/), certificates, and certificate revocation lists across enterprise and cloud deployments. The API simplifies compliance work and improves portability across security formats, which is useful for any team dealing with regulatory requirements around encrypted data. Oracle says the change reduces error risk and enhances the interoperability of secure Java applications.

Beyond the JEP, Java 26 also introduces hybrid public key encryption support, post-quantum-ready JAR signing for supply chain security, and updates to Unicode 17.0 and CLDR v48. Additional updates include faster JVM startup, expanded C2 JIT compilation, smarter heap management, and a new dark mode for JavaDoc.

[JEP 500](https://openjdk.org/jeps/500), Prepare to Make Final Mean Final, begins enforcing Java’s integrity-by-default principle on a longstanding inconsistency: final fields could be mutated through deep reflection, forcing the JVM to hedge on immutability and limiting optimization.

Ritter explained the stakes.

“It has some impact in terms of performance, because it means the JVM has to accept that final fields still can potentially be changed through deep reflection,” he says. “What they want to do is prevent that — quite logically, a final field really is a final field — and that will then allow the JVM to make better use of the layout of objects and values within the heap and memory so that it can be more efficient.” The JEP now issues warnings, setting up a future enforcement step that unlocks those heap layout gains.

And [JEP 504](https://openjdk.org/jeps/504) finally removes the Applet API, which has been deprecated for removal since JDK 17.

“Applets are dead technology, really,” Ritter said plainly. “There are no browsers left that actually have security patches for them and still support the necessary things for applets. So, they’ve finally done away with those.” The removal reduces the platform’s footprint and eliminates a surface area that carried both performance and security liabilities, he adds.

## Beyond the JEPs

Alongside the release, Oracle announced the [Java Verified Portfolio](https://www.oracle.com/java/technologies/downloads/jvp/) (JVP), a curated bundle of Oracle-supported ecosystem components — including commercial support for [JavaFX](https://openjfx.io/) and the [Helidon microservices framework](https://helidon.io/) — packaged under unified licensing and support terms. Helidon AI extends Helidon, enabling Java developers to build high-performance AI applications. Helidon also integrates with [LangChain4j and](https://thenewstack.io/java-developers-get-multiple-paths-to-building-ai-agents/) Helidon MCP, and facilitates building AI Agents as microservices.  JVP also includes Oracle support for Oracle’s Java Platform Extension for [Visual Studio Code](https://thenewstack.io/vs-code-ai-copilot/).

> “What most people really want to do in companies is integrate models that exist into their existing applications, or build agents… We believe that the Java platform is a great language and platform for AI development. The ecosystem is really stepping up — and all this stuff is already built in Java.”

Oracle also used JavaOne to unveil [Project Detroit](https://openjdk.org/projects/detroit/), an OpenJDK initiative to enable Java to call [JavaScript](https://thenewstack.io/introduction-to-javascript/) and [Python](https://thenewstack.io/what-is-python/) runtimes in-process within the JVM — a direct bid to let enterprise Java developers tap into Python’s AI library ecosystem without leaving the JVM or spinning up separate processes.

Inside the briefing, Oracle’s team was candid about the AI opportunity Java is chasing.

“What most people really want to do in companies is integrate models that exist into their existing applications, or build agents,” Arimura tells *The New Stack*. “We believe that the Java platform is a great language and platform for AI development. The ecosystem is really stepping up — and all this stuff is already built in Java. They don’t want to reskill into other areas.”

Oracle Cloud Infrastructure (OCI) has become the first cloud provider to support Oracle JDK 26, which is available at no additional charge to OCI customers.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)