# How Vendia Helps Delta Sync Data With Its Airline Partners
![Featued image for: How Vendia Helps Delta Sync Data With Its Airline Partners](https://cdn.thenewstack.io/media/2024/08/a8c1f453-board2-1024x576.jpg)
Suppose as a company you want to [share certain data with partners](https://thenewstack.io/deterministic-databases-and-the-future-of-data-sharing/), but you must be able to verify to regulators that other data was not shared. That’s the conundrum that Delta Air Lines has faced in trying to provide a seamless experience for its travelers as well as those using partner airlines including Aeroméxico, Air France, China Eastern, KLM and LATAM.

“Whether global travel teams engage directly with Delta’s sellers or one of our JV [joint venture] partners, we want to deliver a seamless customer experience across brands,” said [Nizar Nanjee](https://www.linkedin.com/in/nizarnanjee/), general manager for Sales Innovation at Delta.

All the partners within the alliance want to ensure that all tickets are correct, no piece of information is out of date. Yet other information that would help a particular company unfairly monetize particular flight plans or markets — data that would be considered collusion — cannot be shared.

Looking to more tightly integrate and synchronize CRM environments across its partnerships, Delta chose [Vendia](https://www.vendia.com/) to provide fast, consistent data automation and ease of use.

“Vendia took a concept we anticipated taking months and delivered it in just weeks,” Nanjee said.

## Data Sharing the Right Way
Vendia cofounders [Tim Wagner](https://www.linkedin.com/in/timawagner/) and [Shruthi Rao](https://www.linkedin.com/in/shruthirao/), veterans of serverless at [AWS](https://aws.amazon.com/?utm_content=inline+mention) and blockchain at cryptocurrency exchange Coinbase, created [Vendia to rethink blockchain](https://thenewstack.io/vendia-serverless-pioneers-rethink-blockchain-for-collaboration/) to address the challenges of data management. They found that companies were not using blockchain to deal with trust issues, as originally hyped, but to collect data in one place in order to work with it.

[Traditional approaches to data sharing](https://thenewstack.io/addressing-the-challenges-of-real-time-data-sharing/) like enterprise application integration (EAI), data lakes and legacy blockchains have inherent limitations, Wagner wrote in a sponsored series for The New Stack.
“An ideal solution would offer the single source of truth achievable with a blockchain but with the low latency, high throughput and fine-grained data controls more typical of an EAI-based solution coupled with all the scalability and fault-tolerance benefits of a public cloud service,” he said.

He posits [data mesh](https://thenewstack.io/data-mesh-liberate-business-value-from-data-lakes-data-warehouses/) is key to maintaining a [single source of truth across multiple parties](https://thenewstack.io/the-real-time-data-mesh-and-its-place-in-modern-it-stacks/) that belong to the platform, not with each of the parties, who would have to implement security, access controls, auditing, compliance and governance capabilities on their own.

“People will automate some workflow, right? In this case, kind of cross-party, cross-company data sharing, but all these other elements of the equation with the auditing, the compliance — the important questions of who shared what with whom and why, remain manual, complicated, expensive processes,” Wagner said in an interview.

“Customers don’t necessarily care if there’s a blockchain or distributed ledger behind it, but they care, they care very deeply, that they can go back and ensure that the right data was shared with the right people in the right way … the trust, control, data privacy kind of trust … that’s incredibly important,” he said.

The company maintains that traditional real-time data sharing requires myriad different tools to connect and sync data, as well as analyze it for business opportunities. It offers a sort of one-stop shop with thousands of pre-built connectors to sync data from any business tool with no-code/low-code integrations, making it easy to expand the number of data sources.

“Today [people] will buy some sort of technology like this, a connector technology, they will buy a database on top of it to make sure that data is synchronized and it’s in some sort of a data hub, then they’ll have the data lakes, data warehouses for analysis, then they’ll have a reverse ETL [extract, transform, load] tool for activation backed into an operational system. And then they will have to have a data lineage or a data leak prevention or DLP product on top of it. So think about like five different categories of technologies and tools that a customer has to buy. And what we have done in one platform is we have basically brought all of this together to solve the data heterogeneity-to-heterogeneity problem, just not within the four walls, but outside the four walls also of an enterprise,” Wagner said.

“So when you imagine, three, four or five different tools multiplied by six, seven, eight different companies, you know, we’re talking about the complexity now of trying to hook up literally dozens of these systems together. And that’s one of the things, in addition to the trust, control and privacy element that that we’re able to provide, this is the other very pragmatic and practical benefit of being able to share data once into a common model. And then having that play all these different roles, you know, at the SaaS level and storage level, at the auditing and compliance level, rather than companies having to build these point-source solutions from all of their different pieces to try to make that work.”

## Finding Its Niche
[AWS](https://thenewstack.io/aws-serves-up-tools-for-data-heads-cloud-native-security/) and [Salesforce](https://www.datanami.com/this-just-in/salesforce-unveils-zero-copy-partner-network-offering-new-open-data-lake-access-via-apache-iceberg/) have recently announced zero-ETL capabilities, which ensures that when source data changes, it’s immediately updated everywhere — something that Vendia maintains it has offered for two years.
Wagner says Vendia has been working to bring data closer to the customer and help them find new ways to put that data to work.

“The public clouds have kind of won the storage tier, they’re the ones providing the large, low-cost, bulk storage solutions. And then you see things like [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) and Databricks are kind of winning the data lake wars. They’re that next layer up, right? … And now that next layer up, like Salesforce’s zero-ETL announcement, at some level, I think is really about not saying they want to kill off Fivetran and other ETL providers, as much as they’re saying… that they understand customers want their data to live in those public cloud storage tiers to be manipulated on the data lakes … and then Salesforce, and increasingly other SaaS companies are going to become the vertical solutions on top of that. I somewhat jokingly [call it] the success stack, the data equivalent of the LAMP stack,” he said.

“Vendia’s role in that is not to compete with any one of those three, but to really think about the sideways motion there. How do you then get from Snowflake to Databricks and back? And the other data lakes there? How do you migrate data and distribute it effectively at the cloud-tier level when you want to share it there? And then obviously, within the SaaS companies.

“Our goal is not to compete with those data with those data stacks so much as to make the sideways and the heterogeneous and cross-party data sharing workout successfully. So that’s why zero-ETL is so important because it’s kind of this recognition of where the industry trend is headed.”

## Adding GenAI
Vendia also has been demonstrating generative AI to help customers harness more power from their data. The GenAI model is offered through [Amazon](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html#:~:text=Amazon%20Bedrock%20is%20a%20fully,suited%20for%20your%20use%20case.) Bedrock, a managed service through a unified API. It plans to unveil that service this fall.

Delta Air Lines already offers an [“Ask Delta” chatbot](https://thenewstack.io/opportunities-and-limitations-of-deploying-large-language-models-in-the-enterprise/) that uses generative AI to help customers find flights, check-in and track their bags.

Vendia’s approach is using GenAI to answer business questions like, “Which customers would benefit most from a discount?” of “How could we package travel to be able to improve segment sales overall?”

“Just as customers can choose to use APIs from us, they can choose whether or not to write SQL queries, they can choose whether or not to distribute files in our system, one of the additional things we could do is just automatically offer to build models for them,” Wagner said. “Because a lot of our customers again, they’re going to want that low code, no code experience, or they’re not necessarily going to be able to go hire a team of you know, 20 ML experts on top of us. So the more we can make that just appear as a simple, easy extension of what we already do, the better.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)