# How Enterprises and Startups Can Master AI With Smarter Data Practices
![Featued image for: How Enterprises and Startups Can Master AI With Smarter Data Practices](https://cdn.thenewstack.io/media/2024/12/921a6cf9-eric-prouzet-rtadxj1qkty-unsplash-1024x683.jpg)
[Eric Prouzet](https://unsplash.com/@eprouzet?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/a-stack-of-books-sitting-on-top-of-a-table-RTAdxj1qktY?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
In the same way that one must carefully water a garden to produce a bountiful harvest, AI systems must be hydrated with high-quality, diverse data to deliver optimal results. While it is unsurprising that AI is only as good as the provided data, it can be a shock that supplying systems with the data they need can be a significant challenge in specific contexts.

Consumer AI companies have excelled at AI data engineering by carefully curating and managing the data they use from the public web, leveraging synthetic data to balance their training sets, and using human reinforcement learning to train AI agents better. This has allowed them to create a virtuous data lifecycle with tight feedback loops to reduce errors and continually improve their AI systems to align more closely with consumer needs.

For enterprises, however, supplying AI systems with the data they need to thrive is more complicated by several orders of magnitude. There are two main reasons for this:

First, enterprises don’t have the same information aggregation ability in the consumer AI world. Consumer AI companies can use any public data on the web to train their AI models; think of it as an entire continent of information to which they have unfettered access. On the other hand, enterprise data exists within minor, disparate, and oftentimes disconnected information archipelagos.

Additionally, enterprises are working with many types of data, including relational data from operational systems, decades of poorly organized folders of documents, and audio and numeric data from payroll and financial systems. Further, enterprises must contend with additional layers of regulatory complexity regarding handling personal and private data. To build impactful AI tools, an enterprise’s algorithms must be fed or trained on specific data sets that span multiple sources, including the company’s human resources, finance, customer relationship management, supply chain management, and other systems.

## Get Specific Regarding Input Data
Selecting the correct data to feed AI systems is critical. Adding to this challenge, the data required for these applications often has strong protections, which can create accessibility issues. Therefore, enterprises must be very clear on the problem(s) they’re trying to solve (more on this shortly) so that they only require access to the most relevant data applicable to those problems.

Taking this hyper-targeted approach accelerates data requests and makes data engineering significantly easier. It also helps with managing data processing and governance requirements since there is a high specificity associated with the workload (i.e., you’re not asking for all of the data in a given database or all of the information about a given entity within the business). On the contrary, when enterprises take too broad of an approach to [solving these problems](https://thenewstack.io/the-future-of-sql-conversational-hands-on-problem-solving/), data governance becomes burdensome, and the quality of their outputs suffers greatly. Minimal data by design is critical for both velocity and quality of production.

Specificity is key to keeping AI systems hydrated and overcoming data accessibility challenges. Still, to achieve this, an enterprise must first narrow down the problem it is trying to solve.

## Involve the Right People
The most effective way for an enterprise to get clear on the problem it needs to solve (and obtain the specific data required to solve it) is by combining the knowledge of business leaders and/or stakeholders with technologists.

Business leaders deeply understand the business itself, including the most pressing issues it needs to address using AI. Therefore, they can articulate prompts for [large language models](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/) (LLMsy). Technologists know how to put pen to paper and build the system. Combining the two can be considered generative AI (GenAI) pair programming.

Together, this pairing can work in a highly iterative fashion to identify target business processes and outcomes, which specific data elements are needed for their use case, and the performance metrics by which their process will be measured. They can also collaborate to decide on the types of data and data pipelines used for their initiative, whether that is a retrieval augmented generation (RAG) architecture or if the data will be used to develop a current model further.

## Well-Hydrated AI in Action
By applying the principles above, enterprises can build accurate, [secure AI models tailor-made to their company’s unique needs](https://thenewstack.io/security-needs-create-more-work-for-open-source-maintainers/) and specifications. But what does this look like in action?

Picture a financial services company that uses predictive analytics to identify fraudulent behavior. The insights the [predictive analytics model](https://thenewstack.io/transform-predictive-analytics-with-time-series-language-models/) provides are invaluable for maintaining security. Still, the outputs are highly technical and challenging for most humans to understand — yet humans ultimately need to review any incidents the system flags.

To circumvent this challenge and improve the quality and speed of fraud review, the company could apply the GenAI pair programming strategy mentioned: A technologist could apply an LLM to the company’s predictive analytics. The LLM is trained using specific datasets that the technologist has identified alongside a business-facing stakeholder who can determine the verbiage outputs need to contain and the exact elements that must be covered to deliver the necessary information for the fraud review.

With full access to the appropriate data, the [LLM could consistently and efficiently describe the analytics output](https://thenewstack.io/improving-llm-output-by-combining-rag-and-fine-tuning/) for those reviewing these cases. Throughout the process, the stakeholder could validate the LLM’s outputs and work closely with the technologist to refine the model further.

As one can imagine, an off-the-shelf consumer LLM wouldn’t work in this scenario because it wouldn’t understand the nuances of the business, nor would it have access to the company’s data, which would violate compliance rules. By using this strategy, enterprises can reap the benefits of consumer-like LLM functionality in a company-centric context while remaining safe within their systems.

The ability to effectively leverage AI is a key factor distinguishing leading enterprises from those quickly falling behind, and this divide will only continue to grow. By implementing the strategies above, companies can maximize the value of their AI systems and create unique customer experiences that set them apart from their competition.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)