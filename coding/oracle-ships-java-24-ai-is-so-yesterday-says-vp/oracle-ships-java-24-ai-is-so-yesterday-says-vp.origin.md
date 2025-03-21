# Oracle Ships Java 24: ‘AI Is So Yesterday’ Says VP
![Featued image for: Oracle Ships Java 24: ‘AI Is So Yesterday’ Says VP](https://cdn.thenewstack.io/media/2025/03/71dfe572-getty-images-jpx9yr5rggw-unsplash-1-1024x683.jpg)
[Oracle](https://developer.oracle.com/?utm_content=inline+mention) has released [Java](https://thenewstack.io/introduction-to-java-programming-language/) 24, which delivers 24 [JDK Enhancement Proposals (JEPs)](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/) to help developers improve productivity and enhance the [Java language](https://thenewstack.io/language-wars-2024-python-leads-java-maintains-rust-rises/). The release comes as Java approaches its 30th anniversary later this year.
In a briefing with members of Oracle’s Java team, the group spoke about Java 24’s numerous enhancements, including better support for AI integration, post-quantum cryptography, and performance optimizations.

The story of [Java 24](https://openjdk.org/projects/jdk/24/), released on March 18 at the [JavaOne conference](https://www.oracle.com/javaone/), represents a significant chapter in the programming language’s journey to 30 years. With 24 JEPs and more than 3,500 smaller improvements, this latest version brings innovations across language features, libraries, and performance enhancements.

“The numbers are strong, the excitement around Java is better than it’s ever been… no one would necessarily have predicted that this was the trajectory that we were going to be on as we were zeroing in on our 30th anniversary,” [Georges Saab](https://www.linkedin.com/in/georgessaab/), senior vice president of the Oracle Java Platform and chair of the [OpenJDK](https://thenewstack.io/the-hidden-risks-of-unsupported-openjdk-in-financial-systems/) governing board, told The New Stack.

## Favorite JEPs
As we’ve come to expect with the current six-month cadence for major Java releases, Java 24 does a great job of moving the language forward at a steady clip, solidifying several enhancements that have been “cooking” in the background over the past few release cycles, said [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), vice president and practice lead at The Futurum Group.

“While there are many interesting JEPs to choose from, I think one of the most interesting is JEP 483: Ahead of Time Class Loading and Linking,” he told The New Stack. “I love this as it continues to bring us closer to native code speeds for Java startup times. We’re seeing this same focus on optimizing performance in order to achieve greater scale at less cost broadly across the technology landscape… and for a good reason.

“As [Jensen Huang](https://www.linkedin.com/in/jenhsunhuang/), CEO of Nvidia, said just a few moments ago during his [GTC](https://www.nvidia.com/gtc/) keynote, every data center will be energy-constrained in the future. If you want to know how much you as a company can make, you need to look no further than the amount of energy you have available in your data center.”

**JEP 483****: Ahead-of-Time Class Loading & Linking: **Helps developers increase productivity and improve startup time by making classes of an application instantly available in a loaded and linked state when the HotSpot Java Virtual Machine starts, Oracle said in a statement. This feature does not require the use of the jlink or jpackage tools, and it does not require any change to how applications are started from the command line or any change to the code of applications, libraries, or frameworks. As a result, it helps lay a foundation for continued improvements in startup and warmup time.
## New Language and Libraries Features
Meanwhile, new language features include primitive types in patterns, flexible constructor bodies, module import declarations, and simple source files for beginners.

For instance, [ JEP 488](https://openjdk.org/jeps/488):

**Primitive Types in Patterns, instanceof, and switch**in in its second preview release. This JEP helps developers increase Java programming productivity by making the language more uniform and expressive. This feature helps developers enhance pattern matching by removing restrictions pertaining to primitive types that developers encounter when using pattern matching, instanceof, and switch. It also allows primitive type patterns in all pattern contexts, extends instanceof, and switches to work with all primitive types. Developers of applications that integrate AI inferencing will especially benefit from the support of primitive types, Oracle said in a statement.
Meanwhile, new Java libraries features include Stream Gatherers API, Class-File API, and Vector API improvements that benefit AI inference.

**JEP 485****: Stream Gatherers**, helps developers become more efficient in reading, writing, and maintaining Java code by enhancing the Stream API to support custom intermediate operations, which allow stream pipelines to transform data in ways that are not easily achievable with existing built-in intermediate operations.
“Java 24 introduces Stream Gatherers, a powerful enhancement that gives developers fine-grained control over how elements are grouped and processed within streams,” said [Richard Fichtner](https://www.linkedin.com/in/richardfichtner/?locale=de_DE), CEO of XDEV Software GmbH, in a statement. “This makes complex data transformations more expressive and efficient. I love the feature because it eliminates workarounds like custom collectors or flatMap gymnastics, allowing for more readable and maintainable stream pipelines.”

## ‘AI Is So Yesterday’
While AI has dominated tech discussion recently, Java’s architects are already looking ahead. “AI is so yesterday,” quipped [Donald Smith](https://www.linkedin.com/in/donaldojdk/), vice president of product management at Oracle, in an interview. “Let’s talk about [post-quantum crypto (PQC)](https://thenewstack.io/nist-secures-encryption-for-a-time-after-classical-computing/). That is the new hot topic.”

This forward-thinking approach has become Java’s hallmark, with engineers already implementing quantum-resistant cryptography algorithms to prepare for a future when traditional methods become obsolete.

CIOs and security officers are increasingly asking, “Can we rely on Java to deliver a solution when the deprecation of traditional cryptography schemes becomes mandatory,” Smith said. Oracle’s response draws on experience: they successfully navigated similar transitions with TLS 1.3 and are applying those lessons to post-quantum security, he noted.

## PQC and More Security
Indeed, **JEP 478****: Key Derivation Function API** is a new feature in preview that helps developers prepare for emerging quantum computing environments by offering cryptographic security for data in transit. This improves confidentiality and communication integrity.

“In JEP 478, we’re introducing a new API to deal with the derivation function in cryptographic algorithms,” [Bernard Traversat](https://www.linkedin.com/in/btratra/), vice president of software development for the Java Platform (Language, JVM, Libraries, Security/Vulnerability, UI, Embedded), at Oracle, told The New Stack. “So basically, the goal is to enable you to know about the HMAC [Hash-based Message Authentication Code] based calibration function. This kind of standard is coming out that people in the PQC space are now looking at foundation mechanisms for implementations of the protocol that are currently the initial set of cryptographic protocols that are being placed by the IETF [Internet Engineering Task Force].”

Moreover, from the business perspective, the way cryptography has been implemented for the last three or four years at this point has involved the generation of private keys, Smith noted.

“What this JEP does is allows you to generate quantum-resistant keys or the keys that you’re going to need for quantum-resistant algorithms,” he said. “And so that generally is going to mean bigger keys that are harder to guess and correlate… And as Bernard mentioned, the different standards bodies and international groups that are discussing this stuff. And this is our implementation of that.”

Other security enhancements, in addition to new quantum-resistant cryptography features in the Key Derivation Function API, include the Module-Lattice-Based Key Encapsulation Mechanism and Digital Signature Algorithm.

## 30 Years Young
“As Java approaches its 30th anniversary later this year it continues to expand its toolset to meet developers’ evolving needs, including capabilities that support the development of AI-powered applications,” said [Arnal Dayaratna](https://www.idc.com/getdoc.jsp?containerId=PRF004946), research vice president of software development at IDC, in a statement. “The wide range of capabilities in the new release will help increase developers’ productivity, enabling them to deliver feature-rich applications to their organizations and customers faster and more efficiently. The Java 24 release underscores that Java is unparalleled for the development of enterprise-grade, mission-critical applications at scale.”

[Holger Mueller](https://www.linkedin.com/in/holgermueller/), an analyst at Constellation Research, said Java is turning 30, and like many real 30-year-olds out there, it is no longer rambunctious like a 20-year-old but also not an “elder” statesperson.
“Like a 30-year-old, it is well versed — with the addition of language features, new libraries, tools, runtime updates and source code animations,” he told The New Stack. “But it is not boring with the additions of AI vectors, as well as responsible with the post-quantum resistant lattice additions. Java will be active in its 30s and beyond with this update.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)