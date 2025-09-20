[Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) has had a reputation for being somewhat daunting for new programmers, but with [Java 25](https://www.oracle.com/news/announcement/oracle-releases-java-25-2025-09-16/), released this week, [Oracle](https://www.oracle.com/developer?utm_content=inline+mention) has something to say about that.

While [Python](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/) lets students write their first program in one line, Java traditionally forced them through a gauntlet of confusing syntax just to print “[Hello World](https://thenewstack.io/how-to-define-and-use-your-own-functions-in-python/).” Oracle’s Java 25 fixes this.

The centerpiece is [JDK Enhancement Proposal (JEP) 512](https://openjdk.org/jeps/512) **Compact Source Files and Instance Main Methods**, which eliminates the intimidating `public static void main(String[] args)` that has confused beginners for decades. Students can now start with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | void main() { |
|  |  |
|  | println("Hello World"); |
|  |  |
|  | } |

This is not just about removing characters. “Students can write their first programs in a concise manner without needing to understand language features designed for large programs,” Oracle said. [Rémi Forax](https://github.com/forax) from [Université Gustave Eiffel](https://www.univ-gustave-eiffel.fr/en/) called the JEP a game-changer.

JEP 512 “dramatically simplifies Java for beginners by allowing them to write programs without the traditional boilerplate code,” he said in a statement.

Oracle made an important adjustment from the preview version. Originally, they auto-imported IO methods to make things even simpler, but pulled that back. [Chad Arimura](https://www.linkedin.com/in/chadarimura/), Oracle’s vice president of Java Developer Relations, told The New Stack: “We felt like making that implicit and hiding that away just to get rid of those couple of characters made it so that you had to go backwards when you wanted to grow your program.”

The goal is to create what Oracle calls a “smooth onramp” — features that help beginners get started but do not become obstacles as their programs grow more complex.

“The idea behind JEP 512 is not just reduction in boilerplate, although that is an excellent side effect of it, but it makes it so that the language is much more concise for people who are learning Java, there’s not a lot of overhead in terms of the concepts that somebody needs to learn to get to their first line of code, or, I should say, their first Hello World on the screen,” Arimura said.

In addition to students, system and IT administrators who may not be Java experts can reduce the formality of writing small programs such as scripts and command line utilities, the company said.

“I like how Java 25 evolves the language in a more accessible and expressive way, doing away with some of the tedious (e.g., boilerplate) aspects of the language,” [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at The Futurum Group, told The New Stack.

“For example, you don’t need to wrap everything in a class within source files, and you don’t have to include `super()` or `this()` function calls at the beginning of a constructor,” he said. “These may seem trivial, but with so many developer-friendly systems and backend languages to choose from right now, Java needs to evolve to provide new functionality without bogging developers down in overhead. That’s a tough job, but as you can see from these two examples alone, the language maintainers are focusing on making Java easy to adopt and enjoyable to use.”

## Supporting the Learning Ecosystem

Meanwhile, Oracle backed up the language changes with educational infrastructure. The company partnered with the College Board to update AP Computer Science A courses, ensuring high school students learn current Java instead of outdated versions. Many schools were still using Java 7 and 8 for instruction, Arimura said.

The company also launched [Learn.java](https://learn.java/), a dedicated site for programming beginners separate from its developer-focused [Dev.java](https://dev.java/) portal, he said. The Java Playground now includes snippet sharing, letting instructors create coding exercises that students can run directly in their browsers without installing anything.

“Students can now start with simple programs and gradually expand their understanding to more advanced concepts as they grow, creating a smooth learning path from basic programming concepts to full object-oriented programming,” Forax noted.

Moreover, [Cay Horstmann](https://www.linkedin.com/in/cay-horstmann-659a4b/?originalSubdomain=de), professor emeritus at San José State University, said he sees broader benefits.

“My favorite parts of Java 25 are compact source files, instance main methods and module import declarations, as these features create a low ceremony on-ramp to Java for beginning programmers,” he said in a statement. “They also benefit experienced programmers, expanding the reach of Java to small, everyday tasks.”

As Java approaches its fourth decade, Oracle appears to recognize that language adoption depends as much on the first programming experience as on enterprise capabilities.

## Building AI Skills Early

Java 25’s beginner focus also extends to AI development. While Python dominates machine learning (ML) research, Java remains crucial for production AI systems at enterprise scale.

During a briefing with The New Stack, Arimura outlined three patterns where Java intersects with AI work:

First, AI tools increasingly generate Java code. Services like [Oracle’s Code Assist](https://thenewstack.io/oracles-code-assist-fashionably-late-to-the-genai-party/) and popular editors with AI features help developers write Java faster. “There’s a lot of Java code being built and generated by AI,” he said. “We need to make sure that it continues to be top-notch code.”

Second, existing applications need AI functionality added. “Maybe your CEO said, we need to make all of your applications integrate AI now,” Arimura joked. “We’re no strangers to that here at Oracle.” Frameworks like [LangChain4J](https://github.com/langchain4j/langchain4j) and [Spring AI](https://thenewstack.io/production-worthy-ai-with-spring-ai-1-0/), both of which hit 1.0 releases recently, make this integration easier.

Third, specialized teams build custom ML systems in Java, leveraging its performance characteristics and ecosystem.

The simplified syntax particularly helps with AI scripting and prototyping. [JEP 511](https://openjdk.org/jeps/511) **Module Import Declarations** makes it easier to import entire modules at once, which Arimura noted is “beneficial for simple applications that stitch together AI inferencing and workflows from popular libraries.”

In addition, [virtual threads](https://thenewstack.io/how-do-javas-virtual-threads-help-your-business/), introduced in [Java 21](https://thenewstack.io/we-can-have-nice-things-upgrading-to-java-21-is-worth-it/), are seeing heavy adoption in AI workloads because ML inference often involves many concurrent operations that don’t need full OS threads, Arimura said.

## From Classroom to Career

The path from beginner-friendly Java to AI-ready Java is becoming clearer. Students who start with simple syntax can gradually learn more advanced features like pattern matching — [JEP 507](https://openjdk.org/jeps/507) **Primitive Types in Patterns, instanceof, and switch** extends this to primitive types in Java 25, and [JEP 505](https://openjdk.org/jeps/505) **Structured Concurrency** and the [JEP 508](https://openjdk.org/jeps/508) **Vector API** are used for optimized computations and in AI inference and compute scenarios.

Also, [Oracle’s VS Code extension](https://inside.java/2023/10/18/announcing-vscode-extension/), which is approaching 4 million downloads with a 5.0 rating, bridges this gap. Arimura noted growth “because there’s a lot of new developers, there’s a lot of people learning Java, but there’s also a lot of work happening in the AI space. Many AI development environments center around [VS Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/), bringing Java developers into that ecosystem.”

The release also includes performance improvements that matter for AI workloads. [Project Leyden](https://openjdk.org/projects/leyden/)‘s ahead-of-time compilation features ([JEP 514](https://openjdk.org/jeps/514) **Ahead-of-Time Command-Line Ergonomics** and [JEP 515](https://openjdk.org/jeps/515) **Ahead-of-Time Method Profiling**) speed up application startup without code changes. [JEP 519](https://openjdk.org/jeps/519) **Compact Object Headers** reduces memory usage by shrinking object headers. These optimizations help Java applications run efficiently in cloud environments where resource efficiency directly impacts costs.

JDK 25 AI-related JEPs include:

* **Primitive Types in Patterns, instanceof, and switch** JEP 507, which makes integrating business logic with primitive types from AI inference now easier.
* **Module Import Declarations** JEP 511, to more easily integrate business logic with AI inference, libraries and/or service calls.
* **Vector API** JEP 508, often used in AI inference and compute scenarios.
* **Structured Concurrency** [JEP 453](https://openjdk.org/jeps/453), for AI development often involving running multiple tasks in parallel.
* **Scoped Values** JEP 506 enables sharing of immutable data within and across threads with lower space and time costs vs. thread-local variables.

## Java Ecosystem Steps Up

Arimura noted that there has been lots of progress in the Java plus AI ecosystem, including LangChain4j hitting its 1.0 GA release, introducing Virtual Threads, model expansion, agentic mode, enhanced reasoning support, multimodality and more.

Also, Spring AI hit 1.0 GA release with model expansion, [Model Context Protocol (MCP)](https://thenewstack.io/what-is-mcp-game-changer-or-just-more-hype/) integration, tool calling and more.

In addition, [Spring Creator](https://www.eweek.com/development/springsource-gains-momentum-in-enterprise-java/) [Rod Johnson](https://www.linkedin.com/in/johnsonroda/?originalSubdomain=au)’s [Embabel](https://thenewstack.io/meet-embabel-a-framework-for-building-ai-agents-with-java/) [agentic framework](https://thenewstack.io/java-for-agentic-ai-app-development-what-you-need-to-know/) launched in May with goal-oriented action planning, seamless LLM integration and more.

“We can see increasing use of AI to move beyond just prompt-based interaction. The idea of autonomous agents that learn and adapt as situations change is both intriguing (and a bit scary),” [Simon Ritter](https://www.linkedin.com/in/siritter/?originalSubdomain=uk), deputy CTO at Java platform provider Azul Systems, told The New Stack. “We will need to see how tools like this progress into real-world applications and whether they work as intended.”

Meanwhile, [Georges Saab](https://www.linkedin.com/in/georgessaab/), senior vice president of Oracle Java Platform and chair of the [OpenJDK](https://thenewstack.io/the-hidden-risks-of-unsupported-openjdk-in-financial-systems/) governing board, said: “Java 25 highlights Oracle’s ongoing investment in features and capabilities that power AI solutions and to simplify the language, making Java easier for new developers and IT teams to learn.”

One prominent industry analyst said he sees Oracle continuing to deliver new features that will keep Java at pace with modern development.

“As Java embarks on its fourth decade, it continues to deliver features to help ensure that applications, including those powered by and integrated with AI capabilities, will be highly efficient and scalable across hardware platforms,” said [Arnal Dayaratna](https://www.linkedin.com/in/nextgenai/), research vice president for software development at IDC, in a statement. “Java is well-positioned to deliver a continuous stream of modern features that address next-generation, AI-powered application development.”

## Long-Term Investment

Java 25 is a long-term support (LTS) release, with free updates until September 2028 and commercial support until at least September 2033.

This gives organizations the flexibility to keep applications in production longer with minimal maintenance and eventually migrate on their own terms, the company said. Oracle JDK 25 is planned to receive quarterly security and performance updates until September 2028 under the Oracle No-Fee Terms and Conditions (NFTC), and JDK 25 updates released after that date will be offered under the Java SE Oracle Technology Network (OTN) License planned until at least September 2033, Oracle said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)