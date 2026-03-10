[MariaDB](https://mariadb.com/) is one of the stalwarts of the open-source database world. Born out of the MySQL fork following Oracle’s acquisition of Sun Microsystems[in 2010](https://www.crn.com/news/components-peripherals/222600081/oracle-sun-acquisition-a-done-deal), the project has served as a bedrock for web applications and enterprise systems alike for more than a decade.

But the demands placed on databases are shifting. As companies experiment with AI systems and so-called “agentic applications” that can plan tasks and query enterprise data, developers are running into an all-too-familiar constraint: Many of the databases underpinning business systems were designed in an era when millisecond response times were considered fast enough, and AI workloads were unheard of.

MariaDB believes it has a way to address that. On Monday, the company [announced](https://mariadb.com/newsroom/press-releases/mariadb-to-acquire-gridgain-architecting-the-real-time-foundation-for-the-agentic-enterprise/) it had agreed to acquire [GridGain Systems](https://www.gridgain.com/), the company behind the commercial GridGain in-memory computing platform and the original creator of the open-source [Apache Ignite](https://ignite.apache.org/) project. The deal will combine MariaDB’s relational database with GridGain’s in-memory data processing technology to support AI applications that rely on faster access to large datasets.

## Tackling the “AI latency gap”

As developers experiment with AI-driven software, one emerging challenge is the speed at which applications can retrieve and update data. [Vikas Mathur](https://www.linkedin.com/in/v-mathur/), chief product officer at MariaDB, tells *The New Stack* many organizations hesitate to allow AI agents to interact directly with operational databases because a flood of automated queries could overwhelm systems that still run core business applications.

Mathur said the difficulty stems from the way enterprise data is stored today, with important datasets spread across different systems that AI tools are rarely allowed to access directly.

> “To build effective AI applications, you need real-time data to contextualize the agents.”

“To build effective AI applications, you need real-time data to contextualize the agents,” Mathur says. “Today, that data is typically split across legacy silos and is often off-limits for AI; organizations fear that agents pushing heavy read queries will slow down or crash existing mission-critical enterprise applications. The implication is that deploying agentic applications at scale in production is nearly impossible due to technical fragility and these organizational constraints – this is the AI latency gap.”

The result, he said, is that deploying AI systems in production environments can become difficult as infrastructure struggles to keep up with the volume of requests agents generate.

And so MariaDB is betting that pairing its relational database with GridGain’s in-memory computing layer could address that problem. That layer is designed to respond quickly to large numbers of requests, while MariaDB continues to handle durable storage and transactional guarantees expected from enterprise databases.

## Why in-memory computing matters

GridGain’s technology traces its roots to [Apache Ignite](https://thenewstack.io/apache-streaming-projects-exploratory-guide/), an open-source distributed database and caching system developed internally and donated to the Apache Software Foundation around 2014.

Ignite is designed to process large volumes of data directly in memory rather than retrieving it from disk. For developers working on AI systems, this architecture can be important, as agents often maintain contextual information and repeatedly query underlying datasets while carrying out tasks.

Mathur said keeping that information in memory allows AI agents to access context quickly and maintain state across interactions.

“With an in-memory layer, agents get access to its context within sub-milliseconds,” Mathur says. “This makes it easier for agents to update long-term context instead of rebuilding that context each time.”

MariaDB says the combination could enable developers to run AI applications that interact more directly with operational enterprise data while maintaining the durability guarantees of traditional relational databases.

[Lalit Ahuja](https://www.linkedin.com/in/lahuja/), CTO of GridGain, said the acquisition is aimed at bringing high-speed in-memory processing closer to the databases enterprises already rely on for transactional data.

“Enterprises today cannot afford the latency introduced by siloed data architectures,” Ahuja said in a statement. “With MariaDB and GridGain, enterprise customers will get a unified platform that provides performance without giving up durability.”

## A simpler stack for developers?

Another part of MariaDB’s pitch focuses on complexity. Developers building AI systems today often rely on several different technologies: relational databases for transactional data, vector databases for embeddings, caching layers to speed up queries, and additional tools for orchestration.

Mathur said this arrangement can leave developers stitching together multiple systems in order to maintain application state and retrieve relevant information.

“MariaDB can do the heavy lifting of tying the layers together by embedding vector data type, vector index, and vector search into our core database storage engine,” he says, adding that GridGain’s in-memory technology would provide another piece of that architecture. “With the agreement to acquire GridGain, developers can tie in the caching layer closely with the database, providing a unified, integrated approach.”

With their respective open source foundations in MariaDB and Apache Ignite, organizations can, of course, run the software in their own environments. However, the company plans to offer the combined platform through managed cloud services, which it says could reduce the operational burden for development teams.

Asked what the acquisition means for the Apache Ignite community, MariaDB said it plans to continue working with the Apache Software Foundation, though it stopped short of outlining any specific commitments around the project’s future direction.

“[MariaDB Community Server](https://mariadb.com/products/community-server/) remains the primary engine of our innovation, and the foundation of our ecosystem,” Mathur says. “We are committed to ensuring it is the most dependable open-source database for modern applications and are looking forward to working together with the Apache Software Foundation to shape the future of Apache Ignite.”

It’s worth noting that MariaDB, the corporation, has had a turbulent run in recent years. The company [went public](https://www.theregister.com/2022/12/21/mariadb_uses_spac_to_begin/)[via a SPAC merger](https://www.theregister.com/2022/12/21/mariadb_uses_spac_to_begin/) in 2022, then [was](https://techcrunch.com/2024/09/10/mariadb-goes-private-with-new-ceo-as-k1-closes-acquisition/)[taken private again](https://techcrunch.com/2024/09/10/mariadb-goes-private-with-new-ceo-as-k1-closes-acquisition/) by investment firm K1 Investment Management in 2024. Around the same time, [Rohit de Souza](https://www.linkedin.com/in/rohit-de-souza-42b3871/) took over as CEO, signaling a renewed focus on rebuilding ties with the open source community and sharpening the company’s product strategy.

Whether that approach resonates with developers remains to be seen. The database infrastructure landscape has become crowded in recent years, with hyperscale cloud providers offering their own data services alongside a growing ecosystem of specialised AI data platforms.

Still, MariaDB appears to be betting that familiar relational foundations, paired with faster in-memory processing, could appeal to organisations trying to connect AI systems to the large datasets already sitting inside enterprise databases.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)