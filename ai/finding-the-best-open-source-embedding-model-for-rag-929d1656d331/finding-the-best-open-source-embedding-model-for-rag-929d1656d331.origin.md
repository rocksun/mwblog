# Finding the Best Open-Source Embedding Model for RAG
Proprietary embedding models like [OpenAI](https://platform.openai.com/docs/models?ref=timescale.ghost.io#embeddings)’s text-embedding-large-3 and text-embedding-small are popular for retrieval-augmented augmentation (RAG) applications, but they come with added costs, third-party API dependencies, and potential **data privacy** concerns.

On the other hand, open-source embedding models provide a cost-effective and customizable alternative. By running these models locally, you can [stop paying the OpenAI tax](https://www.timescale.com/blog/the-emerging-open-source-ai-stack?ref=timescale.ghost.io) and regain complete control over the embedding creation process, enhance data privacy, and tailor the models to your needs.

However, evaluating open-source embedding models can be complex, time-consuming, and resource-intensive, causing many engineers to default to proprietary solutions.

This blog post will walk you through an **easy-to-replicate workflow for comparing open-source embedding models** using [Ollama](https://ollama.com/?ref=timescale.ghost.io), an open-source platform for running large language models (LLMs) locally, and [pgai Vectorizer](https://github.com/timescale/pgai/blob/main/docs/vectorizer.md?ref=timescale.ghost.io), a PostgreSQL-based tool for automating embedding generation and management with a single SQL command. [Paul Graham’s essays](https://paulgraham.com/articles.html?ref=timescale.ghost.io) will be our evaluation dataset to demonstrate this workflow.

# Picking the Best Open-Source Embedding Model: Evaluation Workflow
An evaluation workflow for comparing open-source embedding models typically includes the following steps:

- Preparing the evaluation dataset for embedding generation
- Downloading and setting up the embedding models on your local machine
- Setting up a vector database to store the embeddings
- Generating and storing embeddings for each model
- Designing the evaluation pipeline to assess the models
- Running the embedding through the evaluation pipeline
- Comparing the results to identify the best model
While this workflow may sound straightforward, implementing it can quickly become complex and resource-intensive due to several challenges:

**Access and management of open-source models**: Installing dependencies and ensuring system compatibility for each embedding model can be tedious. Storage management is another concern, as large models can consume significant space on your local machine.**Automating embedding generation**: Building a reliable workflow to generate and ingest embeddings across multiple models is complex. You’ll need to handle resource limitations, monitor errors, and ensure efficiency, which can require significant effort.**Creating a fair and robust evaluation pipeline**: Selecting the proper evaluation dataset and defining clear and relevant criteria — like retrieval quality or search accuracy — are essential to ensuring consistent, unbiased, and meaningful evaluations across all models.
Fear not — we can make this easier!

While the specifics of a robust evaluation pipeline may vary depending on your RAG application, you can significantly reduce the complexity with just two tools: **Ollama** for accessing and managing the embedding models and **pgai Vectorizer** for automating embedding generation and management across multiple models (we shared how to [automate embedding generation](https://www.timescale.com/blog/how-to-automatically-create-update-embeddings-in-postgresql?ref=timescale.ghost.io) in a previous article).

**Want to follow along?** Check out this [GitHub repository](https://github.com/timescale/pgai/tree/main/examples/finding_best_open_source_embedding_model?ref=timescale.ghost.io) for all the code used in this post.
# Ollama: Simplified Access to Open-Source Embedding Models
Ollama makes running open-source models effortless by eliminating dependency and compatibility headaches. Simply download and run the model — no complex setup required. It works seamlessly across macOS, Linux, Windows, and Docker environments. In this evaluation, we are running Ollama within a Docker container.

Ollama simplifies model management by bundling a model’s configuration, data, and weights. This bundle makes cleanup and experimentation straightforward while ensuring full data ownership — you retain complete control over how your data is handled and where it flows.

## Open-source embedding models compared
Ollama provides access to state-of-the-art large language models. In this evaluation, we compared three of the most popular embedding models available on [Ollama](https://ollama.com/search?c=embedding&ref=timescale.ghost.io):

These open-source embedding models rival industry-standard proprietary embedding models like OpenAI’s:

[nomic-embed-text](https://www.nomic.ai/blog/posts/nomic-embed-text-v1?ref=timescale.ghost.io): outperforms**text-embedding-ada-002**and**text-embedding-3-small**on both short and long-context text embedding tasks[mxbai-embed-large](https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1?ref=timescale.ghost.io): outperforms**text-embedding-3-large**while being significantly smaller than the latter.
# Pgai Vectorizer: Automatic Embedding Management in PostgreSQL
[Pgai Vectorizer](https://github.com/timescale/pgai/blob/main/docs/vectorizer.md?ref=timescale.ghost.io) eliminates the need to build complex automation infrastructure to generate and manage embeddings across multiple models. It is an open-source, powerful tool designed to automate embedding creation and management directly in PostgreSQL, a widely adopted and robust database with vector capabilities via extensions like [pgvector](https://github.com/pgvector/pgvector?ref=timescale.ghost.io) and [pgai](https://github.com/timescale/pgai?ref=timescale.ghost.io).
In this evaluation, we use PostgreSQL as our database to store the evaluation dataset and its corresponding embeddings.

What sets pgai Vectorizer apart for this use case is its **integration with Ollama**, allowing you to generate embeddings using any open-source model supported by Ollama.

To configure a vectorizer for each embedding model, just use one SQL command with all the configurations needed for your embeddings, as demonstrated below in the `create_vectorizer`
function. You can find more about these configurations in [pgai Vectorizer’s API reference](https://github.com/timescale/pgai/blob/main/docs/vectorizer-api-reference.md?ref=timescale.ghost.io).

`def create_vectorizer(embedding_model, embeddings_dimensions):`
embeddings_view_name = f"{'essays'}{'_'}{embedding_model.replace('-','_')}{'_'}{'embeddings'}"
with connect_db() as conn:
with conn.cursor() as cur:
cur.execute("""
SELECT ai.create_vectorizer(
'essays'::regclass,
destination => %s,
embedding => ai.embedding_ollama(%s, %s),
chunking => ai.chunking_recursive_character_text_splitter('text', 512, 50),
formatting => ai.formatting_python_template('title: $title $chunk')
);
""", (embeddings_view_name, embedding_model, embeddings_dimensions, )
)
From there, pgai Vectorizer handles all the heavy lifting:

- Automatically generating and updating embeddings as your dataset changes
- Splitting the data into chunks and formatting them
- Creating a table to store the embeddings with the specified name
- Generating a view that combines your data with its embeddings for easy access and querying
- Manages the embedding generation queue
Using this [Docker compose file](https://github.com/timescale/pgai/blob/main/docs/vectorizer-quick-start.md?ref=timescale.ghost.io#setup-a-local-development-environment), you can quickly configure PostgreSQL, the pgai Vectorizer worker, and Ollama services in your Docker environment.

To get started, check out this [quick start guide](https://github.com/timescale/pgai/blob/main/docs/vectorizer-quick-start.md?ref=timescale.ghost.io) for more on pgai Vectorizer’s integration with Ollama.

## Configuring multiple vectorizers
After running your PostgreSQL service, install the [pgai](https://github.com/timescale/pgai?tab=readme-ov-file&ref=timescale.ghost.io#quick-start) extension. Then, you can insert the evaluation dataset, [Paul Graham’s essays](https://huggingface.co/datasets/sgoel9/paul_graham_essays?ref=timescale.ghost.io), using the pgai function
, which loads datasets from Hugging Face directly into your database![load_datasets](https://github.com/timescale/pgai/blob/main/docs/load_dataset_from_huggingface.md?ref=timescale.ghost.io)

`with connect_db() as conn:`
with conn.cursor() as cur:
# Load Paul Graham's essays dataset into the 'essays' table
cur.execute("""
SELECT ai.load_dataset(
'sgoel9/paul_graham_essays',
table_name => 'essays',
if_table_exists => 'append');
""")
Let’s configure a vectorizer for each embedding model using the `create_vectorizer`
function!

`EMBEDDING_MODELS = [`
{'name':'mxbai-embed-large', 'dimensions': 1024},
{'name':'nomic-embed-text','dimensions': 768},
{'name':'bge-m3','dimensions': 1024},
]
for model in EMBEDDING_MODELS:
create_vectorizer(model['name'], model['dimensions'])
The order in which the vectorizers are created is the same as in the embedding generation queue. You can view the queue using the
function like this:[vectorizer_status](https://github.com/timescale/pgai/blob/main/docs/vectorizer.md?ref=timescale.ghost.io#monitor-a-vectorizer)

`with connect_db() as conn:`
with conn.cursor() as cur:
cur.execute("SELECT * FROM ai.vectorizer_status;")
for row in cur.fetchall():
print(f"Vectorizer ID: {row[0]}, Embedding Table: {row[2]}, Pending Items: {row[4]}")
# Evaluation Pipeline
**Rich embeddings** — dense vector representations that capture text’s underlying meaning, relationships, and context — are essential for a RAG application to deliver accurate and relevant results. Our evaluation process focuses on two key aspects of embeddings:
**Semantic understanding**: The ability to capture meaning beyond exact word matches, including synonyms, paraphrases, and nuanced phrasing.**Contextual retrieval**: The ability to comprehend broader relationships, intent, and context within the text, ensuring the model retrieves results that align with the query’s meaning even when phrased differently.
The evaluation pipeline consists of two main stages: **test data generation** and **model evaluation**.

## Test data generation
We create a testing dataset by leveraging the text chunks created by vectorizers during the embedding process. Here’s the step-by-step breakdown of our approach:

**Random chunk selection:**We randomly selected**20 text chunks**by querying one of the embedding tables. Since the vectorizers used the same configurations for chunking and formatting, this ensured consistency across the data.**Question generation:**For each retrieved text chunk, we generated**20 questions**using, a powerful and open-source generative LLM available through Ollama.**Llama3.2**
The questions were evenly distributed across the following five categories to mimic how humans ask questions. These questions allow us to simulate potential queries our RAG application would receive:

This function generates questions of a specific type for each text chunk.

`def generate_questions_by_question_type(chunk, question_type, num_questions):`
prompts = {
'short': "Generate {count} short, simple questions about this text. Questions should be direct, under 10 words",
'long': "Generate {count} detailed, comprehensive questions about this text. Include specific details:",
'direct': "Generate {count} questions that directly ask about explicit information in this text",
'implied': "Generate {count} questions that require understanding context and implications of the text:",
'unclear': "Generate {count} vague, ambiguous questions about the general topic of this text:"
}
prompt = prompts[question_type].format(count=num_questions) + f"\n\nText: {chunk}"
system_instructions = """
Generate different types of questions about the given text following the prompt provided.
Each question must be on a new line. Do not include empty lines or blank questions.
"""
with connect_db() as conn:
with conn.cursor() as cur:
cur.execute("""
SELECT ai.ollama_generate(
'llama3.2',
%s,
system_prompt=>%s,
host=>%s
)->>'response';
""",(prompt, system_instructions, OLLAMA_HOST))
generated_questions = [q.strip() for q in cur.fetchone()[0].split("\n") if q.strip()]
print(f"Number of questions generated for {question_type}: {len(generated_questions)}")
return generated_questions
Here are some of the key insights:

**Prompt design matters**: The quality of your testing dataset depends heavily on how direct and descriptive prompts and system instructions are. Being specific about your desired output leads to more accurate results from the generation question LLM.**Integration with PostgreSQL and pgai:**This function highlights the simplicity of using Ollama models within a PostgreSQL environment by leveraging the pgai function[ollama_generate](https://github.com/timescale/pgai/blob/main/docs/ollama.md?ref=timescale.ghost.io#generate).
Here is an example:

A text chunk selected from Paul Graham’s** **[ How to Start a Startup?](https://paulgraham.com/start.html?ref=timescale.ghost.io) (March 2005):

*I worried about how small and obscure we were. But in fact we were doing exactly the right thing. Once you get big (in users or employees) it gets hard to change your product. That year was effectively a laboratory for improving our software. By the end of it, we were so far ahead of our competitors that they never had a hope of catching up. And since all the hackers had spent many hours talking to users, we understood online commerce way better than anyone else.*
Questions generated from the text chunk and used to test it:

- Were they ahead of their competitors by the end?
**(Short question)** - How did the author’s approach to product development during that year, which was referred to as a “laboratory,” enable them to gain a significant lead over their competitors in terms of software innovation?
**(Long question)** - In what year was the startup’s lab phase concluded, and how far ahead of competitors were they by then?
**(Direct question)** - What motivated the author to initially worry about their startup’s small and obscure size?
**(Implied question)** - In what ways did the growth of the startup force them to adapt and innovate?
**(Unclear question)**
## Model evaluation
We use vector similarity search to evaluate each embedding model’s ability to retrieve the correct parent text chunk. The goal is to check if the original text chunk appears among the `top_K`
closest matches (retrieval window) for each question in the testing dataset. Here are the steps involved:

**Performing vector similarity search:**We use cosine similarity for each model and question to retrieve the`top_K`
closest embeddings.**Scoring**: If the original text chunk appears in the`top_K`
results, a score of 1 is recorded. Otherwise, a score of 0 is recorded.**Tallying results**: We aggregate scores to compute the overall accuracy and the accuracy by question type. Breaking down results by question type provides deeper insight into where each model excels, as outliers can sometimes skew overall accuracy.
Selecting the size of the retrieval window is often a balance between precision and recall. A smaller window can miss correct results ranked slightly lower, while a larger one can skew the overall accuracy. We chose 10 as our `top_K`
because it strikes a balance: it’s large enough to account for semantic overlap in textual data, where many chunks may have similar embeddings yet small enough to maintain meaningful evaluation results.

# The Results
Our evaluation dataset, [Paul Graham’s essays](https://huggingface.co/datasets/sgoel9/paul_graham_essays/viewer/default/train?ref=timescale.ghost.io), offered a diverse mix of short, direct, and contextually rich text. The data was split into **6,257 text chunks of 512 characters each, with a 50-character overlap**. We completed this workflow using only open-source LLMs (embedding and generative models) and **cost-free** — from generation to evaluation!

`bge-m3`
achieved the highest overall retrieval accuracy at **72 %**, significantly outperforming the other models. `mxbai-embed-large`
followed with **59.25 %**, while `nomic-embed-text`
ranked last with **57.25 %**.
While embedding models with higher dimensions (**1,024**) performed the best overall, **the gap between ****bge-m3**** and the other models across all question types is notable**. This superior performance is likely due to `bge-m3`
’s [multi-functionality](https://huggingface.co/BAAI/bge-m3?ref=timescale.ghost.io), allowing it to efficiently handle diverse embedding types such as **dense, multi-factor, and sparse retrieval**. This versatility enables better context comprehension, especially for long and implied questions.

`bge-m3`
particularly excelled at long questions, achieving its **highest retrieval accuracy of** **92.5 %**, showcasing its strong contextual understanding. Similarly, `mxbai-embed-large`
performed well in this category, with an accuracy of **82.5 %**, further supporting **the correlation between higher embedding dimensions and improved contextual capabilities**. Interestingly, `nomic-embed-text`
also achieved its best performance on long questions, suggesting that embedding models, like humans, handle detailed and context-rich queries more effectively.
On the other hand, despite the difference in embedding dimensions between `mxbai-embed-large`
and `nomic-embed-text`
, their performances were comparable across all question types. `nomic-embed-text`
outperformed `mxbai-embed-large`
on short and direct questions, achieving retrieval accuracies of **57.5 %** and **63.75 %**, respectively, **showcasing its strength in handling more minor semantic queries**.

While `mxbai-embed-large`
performed better on context-heavy questions, such as long and implied ones, **the gap in accuracy was not significant**. This suggests that while embedding dimensions contribute to performance, **they are not the sole determining factor when selecting the best embedding model for your RAG application.**

Finally, all three models performed poorly on unclear and vague questions, achieving the lowest accuracies ranging from 51.25 % for `bge-m3`
to 37.5 % for `nomic-embed-text`
.

# Choosing the Best Open-Source Embedding Model
Now that we have explored the evaluation results, how do you select the best open-source embedding model for your RAG application?

Fortunately, **cost** is not part of the conversation here, as all these models are **free to use**. Instead, your choice should depend on the following key considerations:

**What type of questions will your RAG application handle most often?**
Will your queries be **short and direct**, or will they involve **context-heavy and detailed questions**?

This distinction helps determine the **embedding dimensions** you need. For example, models like `bge-m3`
excel at handling context-rich queries due to their higher embedding dimensions, while models like `nomic-embed-text`
are better suited for short semantic queries.

**What resources are you willing to allocate?**
While **embedding dimensions** are critical for performance, you must also consider the **model size** and whether it fits your available resources (e.g., storage, computing).

For instance, if you’re constrained on storage but still need strong performance, `mxbai-embed-large`
is a good option. It balances size and sophistication, outperforming smaller models like `nomic-embed-text`
thanks to its higher dimensions.

**How fast do you need embedding generation to be?**
Another factor to consider is the **speed at which the model generates embeddings**. While embedding generation is often done **asynchronously**, creating the impression of instant processing for users, working with models **locally** can introduce challenges. Limited computational power on local machines can impact delivering a **quick and seamless user experience**.

For instance:

**Larger models**like`bge-m3`
and`mxbai-embed-large`
take longer to generate embeddings due to their higher dimensions and complexity. However, they produce richer**,**more context-aware embeddings.**Smaller models**like`nomic-embed-text`
generate embeddings much faster but at the cost of**reduced richness and depth**.
When selecting an open-source embedding model, evaluating whether the embedding generation speed is critical for your use case and balancing it against the quality of embeddings needed is essential.

# Conclusion
This blog post explored an evaluation workflow demonstrating that choosing the best open-source embedding model for your RAG application requires balancing performance, resources, and query types.

Thanks to **Ollama** and **pgai Vectorizer**, implementing this workflow was simple and efficient. Ollama simplified model access and management, while pgai Vectorizer automated embedding generation and storage in PostgreSQL, removing the need for complex infrastructure.

These tools make evaluating and comparing open-source models more straightforward than ever, empowering you to find the best open-source solution for your needs — **cost-free and with complete control over your data**.

To try this workflow with your own data and models, check out [pgai Vectorizer’s documentation](https://github.com/timescale/pgai/blob/main/docs/vectorizer.md?ref=timescale.ghost.io), [the quick start guide with Ollama](https://github.com/timescale/pgai/blob/main/docs/vectorizer-quick-start.md?ref=timescale.ghost.io), and [pgai’s GitHub repository](https://github.com/timescale/pgai?ref=timescale.ghost.io)!

## Recommended reading
To learn more, check out these blog posts on open-source LLMs and RAG applications with PostgreSQL:

*This article was written by Hervé Ishimwe* a*nd originally published **here** on the Timescale official blog on December 19, 2024.*