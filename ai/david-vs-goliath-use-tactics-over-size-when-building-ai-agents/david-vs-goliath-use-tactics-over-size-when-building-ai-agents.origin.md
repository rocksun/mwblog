# David vs. Goliath: Use Tactics Over Size When Building AI Agents
![Featued image for: David vs. Goliath: Use Tactics Over Size When Building AI Agents](https://cdn.thenewstack.io/media/2025/05/d79559f1-artem-sapegin-b18trxc8upq-unsplash-2-1024x683.jpg)
[Artem Sapegin](https://unsplash.com/@sapegin?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/turned-on-macbook-air-displaying-coding-application-b18TRXc8UPQ?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
In recent months, remarkable advances have been made in general-purpose browser agents powered by large language models (LLMs). Industry leaders, such as OpenAI and Anthropic, have released these agents, Operator and Computer Use, respectively, for the public to use. These browser tools have demonstrated impressive capabilities, from booking restaurant reservations to answering diverse and complex questions.

General-purpose browser agents, despite their flexibility, fail to perform structured, repeatable business tasks. Precise analytics, automated workflows, and reliable [data](https://thenewstack.io/automating-context-in-structured-data-for-llms/) enrichment depend critically on consistently structured data. Without a predictable structure, extracted data rapidly becomes unreliable, severely limiting its practical value for downstream processes essential to business and technical applications.

## Why General Agents Struggle With Scale
Several [key issues are limiting the effectiveness of general-purpose AI agents](https://thenewstack.io/ai-agents-key-concepts-and-how-they-overcome-llm-limitations/), like OpenAI’s Operator and Claude’s Computer Use, when applied to large-scale data extraction tasks:

**Lack of Structure:**Agents typically produce outputs that aren’t consistently structured. Since most have been built with question-answering as their primary focus, their outputs tend to be paragraph-formatted or loosely organized.**Limited Website Coverage:**Existing benchmarks to evaluate these agents typically include only a narrow set of websites, often simulated or tightly controlled environments. As a result, general-purpose agents struggle to adapt to the complexity, variability, and messiness of real-world websites.**Model Laziness:**Open AI Operator or Claude Computer Use frequently stops execution prematurely after extracting only partial data (such as a single page of listings). For example, for specific tasks with several pages of data, these models would save partial information on the first page and terminate execution.
## Key Insight: All Problems Have Structure
At [Bardeen](https://www.bardeen.ai/), our approach to web agents is fundamentally different. Rather than competing head-to-head with large model providers by building increasingly bigger and more computationally expensive models, we chose to leverage the inherent structure of real-world web tasks. Through building millions of automations for team and enterprise customers, we’ve learned that many critical business tasks — like extracting job postings, monitoring company blog updates, or analyzing customer testimonials — rely heavily on structured data.

Moreover, we’ve observed that websites presenting this data consistently use repetitive HTML structures.

By recognizing and exploiting this underlying structure, both in the business problems themselves and the websites presenting the data, we realized we could build a significantly more efficient, accurate, and scalable AI Agent without resorting to brute computational force.

## BardeenAgent: A New Approach To Building Browser Agents
Our solution, BardeenAgent, implements this structured approach through a two-step execution process:

**Capture the Extraction Structure (Once)**
First, BardeenAgent navigates to the desired data on a webpage and uses an LLM to identify and record how to extract a single data item. This step generates robust CSS selectors and a structured extraction script, essentially creating a reusable “recipe” for capturing similar data.

**Replay with Precision (Many Times)**
Instead of repeatedly invoking an expensive AI inference for every subsequent data item, BardeenAgent replays this recorded extraction script [across multiple pages or data](https://thenewstack.io/stream-data-across-multiple-regions-and-clouds-with-kafka/) points. This approach drastically reduces computational overhead and improves reliability.

**Why It Works: Efficiency Through Reusability**
This structured approach is powerful because it ensures the following:

**Consistency**: Structured scripts reliably extract data, ensuring consistent output formats.**Scalability**: Once the structure is captured, extraction[scales quickly and efficiently to hundreds or thousands of data](https://thenewstack.io/five-strategies-for-securing-and-scaling-streaming-data-in-the-ai-era/)points.**Cost and Time Efficiency**: Fewer AI calls mean dramatically lower costs and faster data extraction.
## Real-World Applications and Results: Introducing WebLists
To evaluate BardeenAgent’s effectiveness in extracting structured data, we evaluated how well [LLM browser agents performed on our new benchmark](https://thenewstack.io/benchmark-llm-application-performance-with-langchain/), WebLists, composed of use cases requested by real enterprise customers. This includes scenarios like:

- Tracking
**job postings**to identify competitors’ growth or hiring trends - Monitoring
**company blogs**and product updates to prepare informed sales outreach. - Extracting
**customer testimonial**s for robust competitive analysis.
When evaluating the BardeenAgent against other methods on the WebLists benchmark, the results were clear: Our evaluation demonstrated that BardeenAgent’s structured approach significantly outperforms existing state-of-the-art agents, including [Wilbur](https://www.bardeen.ai/posts/wilbur-adaptive-in-context-learning-for-robust-and-accurate-web-agents) (Bardeen’s previously published agent), [Agent-E](https://www.emergence.ai/blog/agent-e-sota), and [Perplexity](https://www.perplexity.ai/). BardeenAgent achieved a 66.2% recall, more than **doubling the best method’s performance**. On top of that, the structured method also translated directly into cost efficiency: BardeenAgent **achieves roughly 3x lower cost per extracted row** compared to competing solutions.

## A Different Approach
General AI is impressive, but when the structure and accuracy of the results matter for your business, you need a different approach. BardeenAgent addresses this gap by leveraging the inherent structure of web data, enabling businesses and researchers alike to extract valuable insights efficiently and reliably at scale.

Read our full technical paper and [blog post here](https://www.bardeen.ai/blog) if you want to move beyond general AI limitations and tap into structured web intelligence.

If you’re interested in testing how your own agent compares or exploring this approach further, reach out to us at ml@bardeen.ai. We’re excited to collaborate with and support the broader AI community.

*The owner of TNS, Insight Partners, also invests in Bardeen. As a result, Bardeen receives preference as a contributor.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)