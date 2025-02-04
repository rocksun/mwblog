# How Developers Can Take Advantage of Perplexity’s Sonar LLMs
![Featued image for: How Developers Can Take Advantage of Perplexity’s Sonar LLMs](https://cdn.thenewstack.io/media/2025/01/b44afe14-getty-images-iod0xnmozbe-unsplashb-1024x576.jpg)
Perplexity, the [AI search startup](https://thenewstack.io/more-than-an-openai-wrapper-perplexity-pivots-to-open-source/), has developed the Sonar series of [large language models](https://thenewstack.io/llm/) (LLMs). These models transform AI search capabilities by providing real-time access to internet information. They are designed to overcome key limitations of traditional language models, such as outdated information and potential [hallucinations](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/).

## Understanding Sonar Models
Sonar is available in two versions: Sonar (basic) and Sonar Pro. These models distinguish themselves from conventional LLMs by leveraging real-time internet connectivity, allowing them to provide responses grounded in the most current information available. Unlike traditional LLMs that are limited by their training data, Sonar’s real-time web access ensures that the information provided is always current and relevant, making it a significant advancement in the field of search-enhanced LLMs.

Sonar is a lightweight and affordable option optimized for speed and basic queries, making it ideal for simple question-answering and straightforward integrations. Sonar Pro, on the other hand, is designed for complex, multistep queries that require deeper understanding and context retention.

The Sonar models support structured outputs, enabling developers to receive responses in organized formats that are suitable for a variety of applications.

A key feature of these Sonar models is extended context windows, enabling the handling of extensive input data while maintaining coherence over long interactions. Additionally, Sonar models provide built-in citations with their responses, ensuring transparency and allowing users to verify information sources. Moreover, they support structured outputs, enabling developers to receive responses in organized formats that are suitable for a variety of applications.

## Why Should Developers Care
For developers, Sonar offers a unique opportunity to build innovative applications using the power of real-time AI search. Here are some key benefits:

**Real-time information:**Sonar models access the latest information from the web, ensuring that your applications always provide the most up-to-date results.**Enhanced accuracy:**By grounding responses in real-world data, Sonar reduces the risk of hallucinations and provides more reliable information.**Built-in citations:**Sonar models automatically generate citations for their responses, allowing you to build transparent and trustworthy applications.**Flexible API:**The Perplexity API provides a simple and efficient way to integrate Sonar models into your projects.**Customizable outputs:**Sonar supports structured outputs, enabling you to tailor responses to your specific needs.
## A Closer Look at the Models
Perplexity’s Sonar Pro models are designed to handle intricate, multistep tasks that require deep understanding and context retention. These models are particularly suited for applications demanding comprehensive information retrieval and nuanced responses.

Some of the key features of Sonar Pro include:

**Enhanced complexity handling:**Sonar Pro models are optimized for complex queries, providing in-depth answers with a higher number of citations compared to standard Sonar models.**Advanced information retrieval:**These models perform multiple web searches to gather and synthesize information, ensuring responses are thorough and well-rounded.**Larger context windows:**With expanded context windows, Sonar Pro models maintain coherence over longer interactions, making them ideal for detailed discussions.
The key differences between Sonar and Sonar Pro are their complexity, citation volume and information-retrieval approach. While standard Sonar models are designed for straightforward queries, Sonar Pro models are specifically built to handle more complex tasks, delivering deeper insights and more comprehensive answers. Additionally, Sonar Pro models provide approximately twice as many citations as standard Sonar models, significantly enhancing the transparency and verifiability of the information.

In terms of information retrieval, standard Sonar models typically rely on single web searches. In contrast, Sonar Pro models conduct multiple searches to gather diverse perspectives and data points, resulting in more nuanced and well-rounded responses.

Sonar offers flexible pricing options to suit a variety of needs and budgets. The basic Sonar model is a cost-effective choice, priced at $5 per 1,000 searches, with an additional $1 charge for every 750,000 input or output words, making it ideal for lightweight integrations and basic queries. For more demanding applications, Sonar Pro is available at $3 per 750,000 input words and $15 per 750,000 output words.

## Exploring Sonar Models Through the API
Let’s delve into some code examples that demonstrate how to use Sonar models for citations and structured output.

While the code looks familiar and almost the same as invoking any LLM’s chat completion API, what’s unique about Sonar is the ability to get the latest information based on online and real-time search results. The response is firmly grounded in the search, increasing users’ confidence.

The other key aspect of Sonar is the citations. The API response contains a list of URLs used for citations.

The code snippet below prints the search result along with the citations. Note that the query is based on recent news. The API not only returns the correct response but also cites the actual sources used to aggregate it.

12345678910111213141516171819202122232425262728293031323334353637383940 |
import requestsdef get_results_citations(api_key, query): """ Retrieves citations from the Perplexity Sonar API for a given query. Args: api_key: Your Perplexity API key. query: The question you want to ask Sonar. Returns: A list of citations (URLs). """ url = "https://api.perplexity.ai/chat/completions" headers = { "Authorization": f"Bearer {api_key}", "Content-Type": "application/json" } payload = { "model": "sonar-pro", "messages": [{"role": "user", "content": query}] } response = requests.post(url, json=payload, headers=headers) response.raise_for_status() return response.json()# Example usageapi_key = "YOUR_API_KEY"query = "Who are the prominent tech CEOs that attended Trump's inauguration?"response = get_results_citations(api_key, query)# Extract content and citationscontent = response['choices'][0]['message']['content']citations = response['citations']# Print the resultsprint("Content:\n", content)print("\nCitations:")for i, citation in enumerate(citations, start=1): print(f"[{i}] {citation}") |
The output has both the content and the citations that point to the results.
Sonar supports structured outputs using JSON Schema. You can specify the desired output format in the `response_format`
field of the API request.

For example, the following query retrieves the correct response (the number of terms Trump served as president) and formats it in JSON. This is extremely useful for integrating Sonar with agentic workflows.

12345678910111213141516171819202122232425262728 |
import requestsfrom pydantic import BaseModelclass AnswerFormat(BaseModel): first_name: str last_name: str year_of_birth: int num_seasons_in_nba: inturl = "https://api.perplexity.ai/chat/completions"headers = {"Authorization": "Bearer YOUR_API_KEY"}payload = { "model": "sonar", "messages": [ {"role": "system", "content": "Be precise and concise."}, {"role": "user", "content": ( "Tell me about Donald Trump." "Please output a JSON object containing the following fields: " "first_name, last_name, year_of_birth, num_times_as_president. " )}, ], "response_format": { "type": "json_schema", "json_schema": {"schema": AnswerFormat.model_json_schema()}, },}response = requests.post(url, headers=headers, json=payload).json()print(response["choices"][0]["message"]["content"]) |
This prints the below output:
Perplexity’s Sonar models offer powerful tools for developers seeking to integrate advanced AI-driven search capabilities into their applications. With features like real-time web access, extended context windows, built-in citations and structured outputs, these models enhance the quality and reliability of information retrieval. Using the Perplexity API, developers can seamlessly incorporate these capabilities, providing users with accurate and up-to-date information tailored to their needs.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)