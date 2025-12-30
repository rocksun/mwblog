Earlier this year, I wrote an article about how [Java](https://thenewstack.io/introduction-to-java-programming-language/) would soon overtake [Python](https://thenewstack.io/what-is-python/) as the [programming language of choice](https://thenewstack.io/2025-is-the-last-year-of-python-dominance-in-ai-java-comin/) for [AI app development](https://thenewstack.io/what-developers-need-to-build-successful-ai-apps/).

Back then, [Simon Ritter](https://www.linkedin.com/in/siritter/?originalSubdomain=uk), deputy CTO at [Azul Systems](https://www.azul.com/?utm_content=inline+mention), told me that based on Azul research, including a [survey of Java developers](https://www.azul.com/newsroom/azul-2025-state-of-java-survey-report/), Java could encroach on Python’s lead in use for AI development within a year and a half. In fact, Ritter said 2025 would be the last year of Python’s dominance for AI development.

So what can we expect in 2026? In the middle of my research on the topic, I noticed that my old pal [James Governor](https://www.linkedin.com/in/jamesgovernor/?originalSubdomain=uk) of [RedMonk](https://redmonk.com/) had written [a potent piece about Java and agentic systems development](https://redmonk.com/jgovernor/java-relevance-in-the-ai-era-agent-frameworks-emerge/). Then just the other day, on our own TNS site, [Michael Coté](https://cote.io/), another astute analyst I know, wrote a piece entitled [“Your Enterprise AI Strategy Must Start With Java, Not Python.”](https://thenewstack.io/your-enterprise-ai-strategy-must-start-with-java-not-python/) So, I knew I was on the right track.

“It’s well known in developer circles that Java is better for developing enterprise AI applications, given better scalability and performance, but right now Python outpaces Java with its libraries and other infrastructure to support the development of AI,” Ritter told The New Stack in a recent interview. “However, enterprises are realizing that Java is the better choice for enterprise-level deployments. We’re likely to see Java outpace Python within the next 18 months to three years.”

## Java in the Agentic AI Era

Now, as we are in the [agentic AI era](https://thenewstack.io/agentic-ai-is-the-new-web-app-and-your-ai-strategy-must-evolve/), several Java AI agent frameworks and libraries — such as [Embabel](https://medium.com/@springrod/embabel-a-new-agent-platform-for-the-jvm-1c83402e0014), [Koog](https://www.jetbrains.com/koog/), [LangChain4j](https://docs.langchain4j.dev/intro/) and others — have emerged to support Java developers building AI applications.

Yet the question remains whether Java can catch up to Python in AI development.

“My personal opinion is that the increasing availability of Java frameworks will help close the gap between Python and Java usage and in the AI agent space,” Azul’s Ritter told The New Stack in a recent interview. “Although Python is a very popular language for AI development, core technologies, such as LLMs [large language models] and [Torch](https://en.wikipedia.org/wiki/Torch_(machine_learning)), are written primarily in [C and C++](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/). Python has become popular due to the wide availability of libraries like PyTorch and its perceived ease of use.”

However, “As more Java frameworks and libraries are developed — such as LangChain4j — I think developers will find that Java offers additional, more compelling advantages,” Ritter said. “Java excels at scalability and performance, especially in handling multiple concurrent threads of execution (something Python struggles with). With the exponential increase in usage of AI agents, factors such as performance will become increasingly important.”

## A Fighting Chance

Java has a “chance” in this undeclared battle. Some say more than just a chance.

“Java has a chance to catch up to Python for AI apps at the enterprise eventually, but I don’t think that will happen tomorrow,” [Andrew Cornwall](https://www.linkedin.com/in/acornwall/), an analyst at Forrester Research, told The New Stack.

But “AI researchers are still more comfortable in Python than Java, so Python will see the bleeding edge research first,” he noted. “However, enterprises find Java easier to integrate. Java’s got a more robust cloud ecosystem and more mature tooling. Right now, the industry is struggling to keep up with GenAI [generative AI] advances, so building with a dynamically typed language like Python is faster. Once the pace settles down and patterns become well known, frameworks for Java will be available, and probably more desirable for enterprises.”

[Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at The Futurum Group, said he does not think that Java will overtake, or “displace” Python as the preferred language for doing data science.

“Honestly, [Haskell](https://www.haskell.org/) and [Mojo](https://thenewstack.io/mojos-chris-lattner-on-making-programming-languages-evolve/) — an extension of Python — stand a better chance of that. As we’ve seen time and again, developers pick a) what they know and b) what they think will get the job done most effectively,” he said. “I think more developers consider building AI outcomes in Python than in Java, simply due to association and familiarity. You can see this if you compare GitHub projects for supportive libraries. Right now, [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/) has approximately 1,132% more stars than LangChain4j. Does that make Python better? Of course not. I think having tools like LangChain4j and Crew4J at the ready is critical, given the number of developers writing mission-critical code in Java. Frankly, a lot of Python code gets refactored into Java — and [Scala](https://thenewstack.io/scala-creator-proposes-lean-scala-for-simpler-code/) — in order to deliver mission-critical performance, security, etc.”

But we’re talking about the enterprise.

Asked if he believed Java could overcome Python for AI app development, [Dmytro Liubarskyi](https://www.linkedin.com/in/dmytro-liubarskyi/?originalSubdomain=de), LangChain4j creator and [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) senior software engineer, replied: “When it comes to integrating LLMs into [enterprise applications](https://thenewstack.io/how-llms-are-transforming-enterprise-applications/), I believe it can. Python will likely remain the dominant language for research, experimentation, and prototyping. However, Java is exceptionally well-positioned for production use in enterprise environments.”

Moreover, Liubarskyi added: “Java has long been the de facto standard for building large-scale enterprise systems, and I’m confident it will also become the language of choice for enterprise AI and LLM integration.”

## Embabel: Targeting the JVM and the Enterprise

[Rod Johnson](https://www.linkedin.com/in/johnsonroda/?originalSubdomain=au), the creator of Embabel and also the creator of the widely used [Spring Framework](https://spring.io/projects/spring-framework), said he believes Java is better suited to building AI apps in the enterprise.

Johnson told The New Stack that he had been doing a lot of machine learning (ML) stuff, mainly in Python, using [TensorFlow](https://thenewstack.io/googles-new-tensorflow-tools-and-approach-to-fine-tuning-ml/) and [PyTorch](https://thenewstack.io/why-pytorch-won/), and training neural networks.

“So, I decided that it’d be interesting to see what the ideal framework would look like for building agents. And I fairly quickly concluded that for what I wanted to do, and what I think is unlocking the value of existing businesses, the [JVM](https://thenewstack.io/java-language-architect-brian-goetz-on-how-java-could-evolve/) [Java Virtual Machine] is going to be a much better place to do that, because you want to be able to grow that functionality out of the valuable core business functionality you’ve already got, rather than add something that’s alien, that just talks to it,” he said.

Johnson added that “Python’s great for data science, but you’re not talking about that when you’re GenAI enabling business applications. You’re talking about application development, traditional application development, rather than data science or pure ML, and Java has always been probably the single most popular language for building those kinds of applications, and there’s a lot of reason behind that. So therefore, to me, it makes a lot of sense to build it on the JVM and build it on top of Spring, build it on top of the functionality and integrations that people already have, and create something that’s really easy for developers to adopt.”

### Spring Boot Advantage

Indeed, Johnson said if a developer understands Spring Boot, they’re going to be up and running with Embabel in under five minutes.

Embabel is an agent framework, initially for the JVM, that is intended not just to play catch-up with Python agent frameworks, but to leapfrog them, Johnson has said in blog posts.

Johnson told The New Stack that as this space matures, people realize that the key adjacency is not calling your LLM or data science. The key adjacency is your existing business functionality and your existing developer skill set. The existing developer skill set in enterprise is Java, he noted.

“So, when you think about it that way, in a GenAI application, you’re calling the LLM over HTTP. It’s not in process. You’re not using anything magical that Python has to do that. It’s typically an HTTP call that’s so simple,” Johnson said.

## Better Programming Model

Johnson originally created [the Spring Framework](https://thenewstack.io/spring-framework-has-three-major-pitfalls-heres-what-to-do/) to deliver a better programming model for enterprise Java, and now Embabel is aimed at doing the same for building JVM-based AI agents.

Johnson explained that, in Python, you create a state machine; in Embabel, you deploy your actions, and the framework can work out what order to run those actions in to achieve the goal. It’s the framework that’s doing it, using a planning approach called goal-oriented action planning.

“And the beauty of it is that it’s both smart, but it’s deterministic, so the framework will be able to tell you why it did that, and if it finds itself with the same input objects, again, it will do the same thing,” he said. That is “definitely a valuable differentiator in enterprise, because explainability is critical,” Johnson said. “Determinism is critical, and I believe Embabel is the only framework that is absolutely directly focused on that while retaining the ability to be smart, and like you add more actions and can do more things that you didn’t explicitly program.”

### Why Kotlin

Embabel is written in Kotlin, a modern, statically typed programming language from JetBrains, known for its conciseness and interoperability with Java as it targets the JVM.

“I personally prefer programming in Kotlin to programming in Java,” Johnson said. Moreover, “we feel our velocity in developing the framework will be faster in Kotlin rather than Java, but we have written most of our sample applications and quite a lot of our internal applications in Java.”

## JetBrains Koog

Koog is JetBrains’ Kotlin-native framework for creating AI agents that run locally, interact with tools and automate complex tasks. JetBrains created Kotlin as a JVM-based alternative to Java that is known for its conciseness, null safety features and full interoperability with Java.

“For many enterprises, Python is not considered a production-ready language, even though most modern AI tools are built on it,” [Vadim Briliantov](https://www.linkedin.com/in/vadim-briliantov/?originalSubdomain=hu), tech lead for Koog at JetBrains, told The New Stack. “That puts developers who normally work in type-safe languages like Java or Kotlin in a tough spot. Koog effectively bridges this gap, offering these developers a long-needed solution, and abstracts a lot of the ‘AI glue code’ away from devs who don’t necessarily follow all the ML literature in a type-safe way.”

Meanwhile, Briliantov echoes what Johnson said about Python versus Java regarding LLM-based AI.

“While it might seem counterintuitive, Python’s advantage in ML libraries and tools doesn’t really apply to LLM-based AI,” he said. “An LLM call is essentially just an HTTP request to some external service. No magic here. At the same time, an AI agent is a long-running system that might fail or be restarted on another machine. A system that interacts with your database and authorizes some user actions.”

### Real-World Advantages

Briliantov asserts that Java has significant advantages over Python for “real-world” applications.

“People have been building such systems for decades on the JVM and for a good reason. Once AI demos leave the lab, they face real-world limitations,” he said. “They need to be fault-tolerant, for example. And Koog already provides such fault tolerance with database integrations.”

### JVM Advantages

The JVM delivers other important advantages over Python, Briliantov said.

The first advantage is its integration into the existing enterprise ecosystem. If your enterprise backend is already on the JVM, there’s no reason to switch the stack for the sake of AI, he argues.

The second advantage is that its type safety and domain modeling not only allow you to build more maintainable code, but also more predictable and better AI agents, he noted.

“Instead of relying on prompt engineering everywhere, you can describe what you want as a data class; Koog would guarantee that an agentic step would produce a result that complies with the form — nothing can be occasionally forgotten by the LLM. It’s like a paradigm shift: You only think about the data and the process, and the framework enforces that the LLM follows your type-safe rules,” Briliantov said.

## Crew4J

Crew4J is a Java-based framework for building and managing collaborative multiagent AI systems. It is not related to [CrewAI](https://www.crewai.com/).

“My mission is to make advanced AI capabilities accessible to Java developers and enterprises without forcing them to abandon their existing infrastructure and expertise,” [Mahesh Awasare](https://www.linkedin.com/in/mahesh-awasare-5b4b126/?originalSubdomain=in), the creator of Crew4J, said in a statement about his development philosophy.

Awasare is an enterprise architect working at [Avaloq](https://www.avaloq.com/), a financial product company. He has also worked for other international banks and financial institutions such as HSBC, Citi, Credit Suisse and Worldline.

“I noticed that the enterprise systems are written in Java and 90% of enterprise systems are very difficult to migrate to a Python tech stack to leverage AI,” Awasare told The New Stack. “So, I thought, why not create something that will be easy for existing implementations to adopt for AI agentic development. This is the reason I created Crew4J.”

He said he believes that “all enterprise systems are looking to integrate AI, and since most of them are in Java, the demand for such a framework is high. People are trying to mix Java implementations with Python for integrating AI, and it is not easy.”

However, Crew4J is very simple to use, requiring just a [six-step process](https://crew4j.com/step-by-step-guide).

Still, Awasare said he does not believe Java will outpace Python for AI development. “I am not sure if it would overtake, but would it co-exist? BIG YES,” he responded via email.

## LangChain4j

[LangChain4j](https://docs.langchain4j.dev/) is an open source Java framework that simplifies the integration of LLMs and other AI capabilities into Java applications.

It provides unified APIs for a wide range of LLM providers and vector stores, making it easy to switch between them with minimal code changes.

The library also includes many out-of-the-box building blocks for Retrieval-Augmented Generation (RAG) pipelines, agents and related patterns, allowing developers to focus on application logic instead of boilerplate, LangChain4j creator [Liubarskyi](https://www.linkedin.com/in/dmytro-liubarskyi/?originalSubdomain=de) told The New Stack.

It is designed specifically for Java developers who want to build production-ready LLM applications and agentic systems.

### How It All Started

In early 2023, Liubarskyi was working on LLM-powered chatbots in Java and quickly realized that there were no suitable libraries available. Everything had to be implemented from scratch. Around that time, he discovered LangChain and thought, “We need something like this, but for Java.” That idea became the foundation of LangChain4j and even inspired the name.

Despite the name, LangChain4j is not a direct port of LangChain, he said. “Instead, it combines ideas and concepts from LangChain, Haystack, LlamaIndex, and the broader community, along with our own innovations, all adapted to Java’s ecosystem and design principles,” Liubarskyi told The New Stack.

The demand has been very strong. After LangChain4j was presented at the [Devoxx Belgium conference](https://devoxx.be/) in the fall of 2023, the project gained significant momentum and has continued to grow steadily across all metrics. It has recently reached 10,000 GitHub stars and shows consistent growth in both downloads and unique users.

The community is large and active, with a constant stream of pull requests and contributions. Today, LangChain4j is used by a wide range of teams, from startups to large enterprises.

Indeed, the discourse around LangChain4j attracted the attention of [Microsoft](https://news.microsoft.com/?utm_content=inline+mention), which has invested in the project and helped to enhance security for it.

### Microsoft Investment

In [a blog post](https://devblogs.microsoft.com/java/microsoft-and-langchain4j-a-partnership-for-secure-enterprise-grade-java-ai-applications/) entitled “Microsoft and LangChain4j: A Partnership for Secure, Enterprise-Grade Java AI Applications,” [Julien Dubois](https://www.linkedin.com/in/juliendubois/?originalSubdomain=fr), principal manager, Java developer relations, wrote: “Our telemetry data indicates significant growth in LangChain4j adoption, with hundreds of Microsoft customers utilizing the framework in production environments. Recognizing the importance of this open-source initiative, Microsoft has made substantial contributions to enhance the project’s Azure and OpenAI integration capabilities.”

In a statement, Liubarskyi said: “We’re especially grateful for Microsoft’s dedication to strengthening the security of the library — their close collaboration and thorough audit process have helped us build a more secure and trustworthy foundation for AI development in Java.”

### Distinct From the Alternatives

Meanwhile, Liubarskyi said LangChain4j is distinct from Embabel, Koog and the others in several different ways.

He said his goal was to keep LangChain4j lightweight yet powerful. It is intentionally designed as an unopinionated library rather than a full framework, which makes it easy to use with any JVM language and integrate into virtually any stack.

“It works seamlessly with popular Java frameworks and runtimes such as Quarkus, Spring, Helidon, Micronaut, WildFly and Liberty,” he said.

LangChain4j was also one of the first libraries in this space, which means it has had time to mature.

“We place a strong emphasis on API stability and try to avoid breaking changes as much as possible,” he added. “Another key strength is the breadth of integrations: Out of the box, users can work with a wide variety of LLM providers and vector stores.

“Finally, the library offers two distinct levels of abstraction. Developers can use low-level APIs for maximum control, or higher-level AI services and agents to get more functionality with less setup.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)