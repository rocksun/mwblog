In 2025, the [Ada programming language](https://www.adacore.com/languages/ada) made what might be considered a comeback. ([But don’t call it one](https://www.youtube.com/watch?v=vimZj8HW0Kg)! Yet.)

Last March, Ada broke into the [TIOBE Index](https://www.tiobe.com/tiobe-index/ada/) top 20 (reaching number 18), and by July, Ada broke the top 10 (reaching number 9 – its highest-ever position on TIOBE). It is now back to number 18.

Moreover, this month Ada also broke into the top 10 in the [PopularitY of Programming Language Index (](https://pypl.github.io/PYPL.html)[PYPL)](https://pypl.github.io/PYPL.html), landing at number 9.

While programming languages such as [Python](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/), C/C++ and [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) continue to rank amongst the most popular languages, the resurgence of interest in Ada could partially be explained by the push to use more [memory-safe languages](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/).

Indeed, in a world increasingly focused on software security and safety, Ada stands out, said [Tony Aiello](https://www.linkedin.com/in/manthonyaiello/), product manager at [AdaCore](https://www.adacore.com/), which provides software development tools for mission-critical systems.

“Ada is the language with the longest and strongest pedigree: Ada was designed from the ground up for secure, safety-critical systems,” Aiello said. “Ada offers strong static typing and runtime memory safety, two language features in growing demand.”

Moreover, thanks to [SPARK](https://en.wikipedia.org/wiki/SPARK_(programming_language)), which brings deductive formal verification to Ada, developers can prove static memory safety and the absence of runtime errors, guaranteeing the elimination of significant classes of serious security vulnerabilities before the software is even executed, Aiello told The New Stack. SPARK is a programming language based on Ada and intended for developing high-integrity software.

These capabilities make Ada especially popular in the aerospace, defense and automotive industries, which have been receiving considerable attention recently, he said.

Meanwhile, “Ada proves that a language capable of delivering concurrency and safety can remain viable for nearly five decades,” said [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at The Futurum Group. “Currently, features such as strong typing and robust memory management are driving interest in languages like [Rust](https://thenewstack.io/rust-programming-language-guide/) and [Go](https://thenewstack.io/introduction-to-go-programming-language/) across the board, as developers can build software with less concern for both stability and security. With Ada, it’s easy to see that those techniques and capabilities, like runtime and compile-time checks, make it a great choice for large-scale projects that need to deliver performance and stability.”

> According to an [AdaCore blog post](https://www.adacore.com/blog/what-would-ada-think-of-the-rise-in-ada-language-popularity), Ada is a powerful language for developing safe, reliable, high-performance software. Its combination of strong typing, memory safety, efficient code generation, and precise low-level control makes it an ideal choice for high-integrity systems.

Also, “as an imperative, procedural language, Ada feels familiar to developers with experience in C, C++, or Rust,” the post said.

## Updating FAA Systems

The U.S. [Federal Aviation Administration (FAA)](https://www.faa.gov/) has used Ada extensively in its [air traffic control](https://www.faa.gov/air_traffic) (ATC) systems. In 1989, [IBM](https://www.ibm.com/solutions/automation?utm_content=CPWWW&p1=Display&p2=434371219&p3=227599223&utm_term=20APO&utm_content=inline-mention), under contract with the FAA, began working with the agency to deliver the Advanced Automation System (AAS) program, an ambitious effort to modernize the entire ATC system. The AAS was slated to consist of 2 million lines of Ada code. The FAA’s interest in Ada coincided with the Department of Defense (DoD) mandating Ada for its systems.

[![](https://cdn.thenewstack.io/media/2026/01/8e7fe2f9-a-c-q6lmojl7ofm-unsplash-1.jpg)](https://cdn.thenewstack.io/media/2026/01/8e7fe2f9-a-c-q6lmojl7ofm-unsplash-1.jpg)

The DoD mandated Ada as its standard language in 1987, but this mandate became law via the 1991 Defense Appropriations Act, which took effect June 1, 1991, and required Ada for weapons systems and other mission-critical systems. That mandate ended in 1997.

However, Ada continues to be used in critical systems within the aviation industry, including commercial aircraft like the Boeing 777, and in various ATC systems globally.

As the [Trump Administration has vowed to overhaul the ATC](https://www.faa.gov/new-atcs), the question arises of [what the FAA will do](https://www.faa.gov/newsroom/brand-new-air-traffic-control-system-bnatcs-fact-sheet) with all that Ada code? Are they looking at moving to Rust or a new language?

> “Moving from Ada to Rust sounds like a pretty heavy lift,” Shimmin said. “Do you think, based on some of the early work we’ve seen from IBM in refactoring [COBOL](https://thenewstack.io/cobol-everywhere-will-maintain/) to Java, that we’ll be seeing more and more of these major migration/modernization efforts?” he asked.

Shimmin added that his guess is that the rise of “generative and agentic AI actually makes it less likely that companies will feel they need to ‘modernize’ code that already works and works well. I’m thinking that’s down to the fact that the biggest issue with maintenance is domain expertise and institutional knowledge, two areas where AI simply shines.”

## Ada and AI?

Speaking of AI, AdaCore’s Aiello said Ada and especially SPARK are the best-suited languages for AI-assisted development.

“Both Ada and SPARK embed self-checking capabilities in the language, allowing LLMs [large language models] to reason more precisely as they develop the code and provide the user with code that is not only free of a number of common programming mistakes, but also functionally correct,” he said.

## Other Factors Driving Ada’s Popularity

In addition to Ada’s memory safety and other features, some observers see other reasons for its recent spurt in popularity.

“The recent growth in languages’ popularity indices can also be explained by the modernization of the Ada/SPARK ecosystem, for example with the [Alire package manager](https://alire.ada.dev/) or the [VS Code plugin](https://marketplace.visualstudio.com/items?itemName=AdaCore.ada),” said [Fabien Chouteau](https://www.linkedin.com/in/fabienchouteau/?locale=en_US), community and advocacy manager at AdaCore. Alire is also known as the Ada Library Repository.

Meanwhile, “We are also witnessing a virtuous cycle of new Ada/SPARK developers joining the community, driving new initiatives for collaboration, and therefore bringing new people to learn and contribute,” Chouteau said.

In addition, [Nvidia’](https://www.nvidia.com/en-us/)s interest in Ada could also play a part in its recent popularity.

“It’s likely that Ada’s ranking in the TIOBE index is influenced by Nvidia’s experimentation with Ada and SPARK, and may be confounded because they have products by those names as well,” said [Andrew Cornwall](https://www.linkedin.com/in/acornwall/), an analyst at Forrester Research.

Indeed, Nvidia offers its [DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) product and Nvidia [Ada Lovelace Architecture](https://www.nvidia.com/en-us/geforce/ada-lovelace-architecture/).

## Ada’s History

Ada was named after [Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace), who is considered to be the world’s first computer programmer.

According to Wikipedia, “Ada is a structured, statically typed, imperative and object-oriented high-level programming language, inspired by Pascal and other languages. It has built-in language support for design by contract (DbC), extremely strong typing, explicit concurrency, tasks, synchronous message passing, protected objects and nondeterminism. Ada improves code safety and maintainability by using the compiler to find errors in favor of runtime errors.”

The language was created by a team led by French computer scientist [Jean Ichbiah](https://en.wikipedia.org/wiki/Jean_Ichbiah) of Honeywell under contract to the DoD from 1977 to 1983 to supersede over 450 programming languages then used by the DoD.

Moreover, Ada was originally designed for [embedded](https://en.wikipedia.org/wiki/Embedded_system) and [real-time](https://en.wikipedia.org/wiki/Real-time_computing) systems. Then the [Ada 95 revision](https://www.adaic.org/ada-resources/standards/ada-95-documents/95intro/), designed by [S. Tucker Taft](https://www.linkedin.com/in/sttaft/) of [Intermetrics](https://en.wikipedia.org/wiki/Intermetrics) between 1992 and 1995, improved support for systems, numerical, financial and [object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming) (OOP). Taft is currently a vice president and the director of language research at AdaCore.

## A Language That Prevents Errors

Meanwhile, an [article from Ada Germany](https://gi-radar.de/372-sicherer-durch-ada/) last year by Chair [Tobias Philipp](https://www.linkedin.com/in/tobias-philipp-1088988a/?locale=en_US), Deputy Chair [Christina Unger](https://github.com/cunger), [Dr. Hubert B. Keller](https://www.linkedin.com/in/hubert-b-keller-3786395/?originalSubdomain=de) and experts from Ada Deutschland e.V., said “programming languages like Ada can systematically prevent entire classes of errors through strong typing and extensive compile-time and runtime checks. In Ada, an array is not merely a pointer to the first element, but a semantic structure that inherently includes its index types and bounds. Read and write operations are verified by both the compiler and at runtime.”

> In addition, [the article](https://www.adacore.com/blog/safer-with-ada) argues that 12 of the [Top 25 software weaknesses](https://cwe.mitre.org/top25/index.html) as defined by the [Common Weakness Enumeration](https://cwe.mitre.org/) (CWE) “would be precluded by the use of Ada and its syntactic and semantic checking mechanisms at compile and runtime — prevented solely through the choice of programming language, regardless of coding mistakes.”

## Other Ada Users

Displaying the varied uses of Ada today, AdaCore compiled a list of organizations that depend on the language every day.

These include [the Victoria Line](https://tfl.gov.uk/tube/route/victoria/) in London, which is touted as the world’s first fully automated underground railway. Its Automatic Train Operation (ATO) system uses Ada for the main control logic, while the emergency braking system was written in SPARK.

Also, [BNP Paribas](https://group.bnpparibas/en/), one of the world’s leading banking and financial services institutions, uses Ada to enhance its ability to meet the demands for its risk calculation models. Ada empowers a robust and reliable risk calculation engine that can handle millions of daily requests with high accuracy, performance and reliability, AdaCore explained.

[Deep Blue Capital](https://deepbluecap.com/) uses Ada to implement trading algorithms that execute thousands of transactions per second. The company’s engineers chose Ada not just for its efficiency, but for its compile-time safety features, strong typing and memory safety guarantees, AdaCore reported.

Additionally, [Stratégies Romans](https://www.romans-cad.com/en/company), a French software vendor, developed a comprehensive 3D computer-aided design (CAD) suite using Ada. Their software supports a range of design and modelling tasks and is used by engineers and designers in industrial settings. Ada’s use here demonstrates that Ada is equally suited to large-scale interactive systems, not just embedded controllers, AdaCore noted.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)