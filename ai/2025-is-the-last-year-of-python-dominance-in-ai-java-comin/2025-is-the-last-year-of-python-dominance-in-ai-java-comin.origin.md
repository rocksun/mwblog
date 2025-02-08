# 2025 Is the Last Year of Python Dominance in AI: Java Comin’
![Featued image for: 2025 Is the Last Year of Python Dominance in AI: Java Comin’](https://cdn.thenewstack.io/media/2025/02/5691ee7b-omar-the-wire-1024x576.webp)
2025 is the last year of Python dominance in AI, according to the deputy CTO of a major [Java](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/) platform provider.

[Simon Ritter](https://www.linkedin.com/in/siritter/?originalSubdomain=uk), deputy CTO at [Azul Systems](https://www.azul.com/), told The New Stack that based on Azul research including a recent [survey of Java developers](https://www.azul.com/newsroom/azul-2025-state-of-java-survey-report/), Java could encroach on [Python](https://thenewstack.io/python/)’s lead in use for AI development within a year and a half.
“It’s well known in developer circles that Java is better for developing enterprise AI applications given better scalability and performance, but right now Python outpaces Java with its libraries and other infrastructure to support the development of AI,” Ritter said. “However, enterprises are realizing that Java is the better choice for enterprise-level deployments. We’re likely to see Java outpace Python within the next 18 months to three years.”

Ritter explained that Python’s current supremacy for AI is actually a cultural thing as it’s a simpler programming language. People who are more familiar with AI techniques have a mathematical background versus a software development one, so Python’s simplicity was more appealing to them, he noted.

## Enterprise Roadblocks
However, “As enterprises depend on more and more AI deployments, we are going to run into roadblocks where they can’t scale beyond Python’s capabilities,” Ritter said. “These will require substantial rewrites and re-architecting of applications. Organizations will need to ensure their applications are running in tandem with Python and Java, with Java AI applications developed for the long term, to avoid hitting a brick wall.”

Moreover, crucial to Java’s eventual dominance is its ability to deliver better performance out of GPUs, Ritter expressed. For instance, “[Project Panama](https://openjdk.org/projects/panama/) has already been delivered in the JDK, making it easier to use non-Java libraries from Java code,” he said. “This will be augmented by [Project Babylon](https://openjdk.org/projects/babylon/) that is exploring how Java can take direct advantage of GPUs to deliver better performance without having to change the code.”

The Azul report showed that Java developers are actively leveraging AI and 50% of survey participants who build AI functionality use Java, surpassing the use of other popular languages like Python and JavaScript that are more culturally associated with AI.

## Java Fit for Purpose
“This highlights Java’s ‘fit-for-purpose’ nature in AI, offering scalability, extensive libraries, and seamless integration with existing enterprise systems,” the report said.

Indeed, Java’s long-standing strengths in performance, scalability, and stability make it a natural fit for developing AI-powered applications, offering the computational efficiency and enterprise-grade reliability that AI solutions demand, the report stated.

Also, among those organizations that use Java to build AI functionality, [JavaML](https://github.com/AbeelLab/javaml) is the most commonly used Java AI library. As AI is having an impact on the way organizations strategize, build code, and maintain applications and infrastructure, all this activity requires compute power, so 72% of survey participants say their compute consumption will have to grow for them to support Java applications with AI functionality.

## Could Java Take Over?
Asked if he believed Java could overtake Python for leadership in AI development, [Arnal Dayaratna](https://www.idc.com/getdoc.jsp?containerId=PRF004946), an analyst at IDC, told The New Stack: “Yes, definitely, this could happen, especially since Java is unparalleled for the development of enterprise-grade, mission critical applications at scale.”

However, another seasoned appdev market observer sees things differently.

[Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at Omdia, told The New Stack he does not believe Java can displace Python for AI development.
“The performance gains we’re starting to see for the Python language itself coupled with the burgeoning ecosystem of libraries ([PyTorch](https://thenewstack.io/why-pytorch-gets-all-the-love/), Panda, etc.) available to developers, I would not expect Java to overtake Python in supporting AI,” he said. “Certainly, where security and performance are a must, as withing finance, for example, we would expect some Python code to be refactored as Java or [Scala](https://thenewstack.io/scala-creator-proposes-lean-scala-for-simpler-code/). But even there, AI practitioners would rather start with Python. With the rise of [GenAI](https://thenewstack.io/generative-ai-in-2023-genai-tools-became-table-stakes/), I would expect to see other languages coming into play, particularly those used for full-stack development like [Typescript](https://thenewstack.io/typescript/).”

Meanwhile, some developers (who requested anonymity) said they believe the Java community needs to do much more to innovate with respect to the language to render it more suitable for AI development.

## Oracle Working on It
[Oracle](https://developer.oracle.com/?utm_content=inline+mention), the steward of the Java language and platform, is working on just that.
[Georges Saab](https://www.linkedin.com/in/georgessaab/), senior vice president of Oracle Java Platform and chair of the OpenJDK governing board, said Oracle has seen increasing use of Java in emerging technologies as they mature, and AI is no exception.
“Java is where a large percentage of enterprise business logic resides and the strong typing, [memory safety](https://thenewstack.io/out-with-c-and-c-in-with-memory-safety/), good core libraries, and extensive tooling mean Java is naturally drawn to these growing ecosystems,” Saab told The New Stack. “In the area of computationally intensive AI training and model creation, we are seeing increased interest in Java thanks to performance improvement options around native library integration and the JIT. Going further, Project Babylon has the goal to extend the reach of Java to GPU programming models, pulling Java even deeper into the AI space. And [Project Valhalla](https://openjdk.org/projects/valhalla/) is expected to make dealing with complex data types as efficient as primitives with value types allowing the JVM to better flatten memory.”

Additionally, on the inference side, [Project Amber](https://openjdk.org/projects/amber/) is allowing developers to model data much more easily and expressive with sealed types, Record classes, and pattern matching, he noted.

“As an example, [langchain4j](https://docs.langchain4j.dev/) has the capability of asking LLM models to return answers that are stuffed directly into Records, effectively marshaling unstructured AI-generated answers into strongly typed systems,” Saab said. “And since a large percentage of business applications are already written in Java, this gives the developers of those applications the capability to ‘stay within Java’ to build in AI intelligence.”

## Overall Report Findings
The Azul report includes responses from more than 2,000 Java professionals worldwide, looking at how enterprises are tackling Oracle Java pricing and licensing challenges, the strategies organizations are adopting to address cloud costs, factors impacting DevOps productivity, and the role Java is playing in AI development, the company said.

Of all businesses contacted globally to participate in the Azul 2025 State of Java Survey & Report, only 1% of respondents were disqualified from taking the survey because they did not use Java in their enterprise — highlighting that 99% of organizations surveyed actively use Java, according to the company. In addition, nearly 70% of respondents indicate that more than half of their applications are built with Java or run on a Java Virtual Machine (JVM), confirming Java’s fundamental role in today’s businesses.

Other key findings from the 2025 State of Java Survey & Report include:

### The Shift Away From Oracle Java
Two years after Oracle introduced its employee-based pricing for Oracle Java SE, concerns remain high, Azul said. 82% of Oracle Java users expressed unease with its cost model — the same percentage reported in the Azul 2023 State of Java Survey & Report. The percentage of organizations considering alternatives to Oracle Java has also jumped significantly – from 72% in 2023 to 88% today, the company said.

The top five reasons given for considering a migration away from Oracle Java (where respondents could select all that apply) include cost (42%), preference for open source (40%), Oracle sales tactics (37%), uncertainty created by ongoing changes to pricing and licensing (36%), and restrictive Oracle policies (33%), according to the report.

“Well, we have to consider the source here, of course,” Shimmin said, noting that Azul is a key Oracle competitor. “But I do know that Oracle is somewhat vulnerable here, as there are a number of alternative JDKs out there from Azul and others that feature a more flexible and potentially cheaper licensing model compared to Oracle’s Oracle Java SE Universal Subscription.

“It’s really down to Oracle to prove the value of software maintenance, patching, and support services — a business model that has worked for open source-engaged companies like [Red Hat](https://www.openshift.com/try?utm_content=inline+mention), Databricks, and many others. In my opinion, given that there are many options out there, Oracle will need to work cooperatively with its existing customer base to bring them forward without imposing any financial or technical friction here. To me, a good approach for any company in this situation would be to offer both a free edition and a committed use license that can scale up and down in tandem with a customer’s needs.”

IDC’s Dayaratna agrees.

“I have some concerns about the findings: I mean, it would be reasonable for any organization to consider moving from away from an expensive and well-established technology…I’m not sure what ‘consider’ means in this context: Does it mean they have thought about it? Does it mean they have developed a plan to do this?” he said.

Of the survey, [Holger Mueller](https://www.linkedin.com/in/holgermueller/), an analyst at Constellation Research, said, “It is a little bit a self-serving report by Azul — who wants people to move off Oracle Java. The reality is migrating platforms is hard, and the business case of mostly questionable… now if Azul would offer a working code migration powered with AI — then these migrations may as well happen. Automated migration lowers the cost of migration…we will see.”

## Security and DevOps
Meanwhile, the Azul survey looked at DevOps and security issues, including that 62% of respondents reported dead or unused code affecting DevOps productivity, 33% of DevOps teams spend over half their time dealing with false positives from Java security vulnerabilities, and 49% said they still experience [Log4j](https://thenewstack.io/log4j-why-organizations-are-failing-to-remediate-this-risk/) security vulnerabilities in production.

“As Java continues to be the backbone for business-critical applications in the enterprise, we’re seeing important trends — from the growing interest in Oracle Java alternatives to cloud optimization strategies, improvements in DevOps productivity, and innovation with AI,” said [Scott Sellers](https://www.azul.com/leadership/scott-sellers/), co-founder and CEO at Azul, in a statement.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)