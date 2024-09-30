# Building an AI Image Gallery with OpenAI CLIP, Claude Sonnet 3.5, and pgvector
![Building an AI Image Gallery with OpenAI CLIP, Claude Sonnet 3.5, and pgvector](/blog/content/images/size/w2000/2024/09/Advanced-RAG-application-with-claude-sonnet-3.5-and-pgvector--1-.png)
Anthropic, a giant in the race of artificial intelligence (AI) research focusing primarily on safe and ethical AI systems, has introduced another family member, **Claude Sonnet 3.5**. For many, the latest member of the Claude family has quickly replaced GPT-4o as the default large language model (LLM) due to its intelligence, speed, and cost-effectiveness, setting a new industry standard. It's not just the versatility but also the reliability of Sonnet 3.5 that has earned it widespread acclaim among developers.

These large language models can understand and process various modalities, such as images, text, and audio, enabling them to power a wide range of future applications, from multimodal search engines to advanced AI-driven creative tools. [ In a previous article](https://www.timescale.com/blog/retrieval-augmented-generation-with-claude-sonnet-3-5-and-pgvector), you learned how to use Claude Sonnet 3.5 and pgvector to build a simple retrieval-augmented generation (RAG) application.

In this article, we’re upping the challenge level to create an **AI image gallery** that lets you search for images and ask questions. We'll build a RAG application using the same tools: PostgreSQL with pgvector as the vector database and Claude Sonnet 3.5 as the LLM.

[RAG is more than just vector search](https://www.timescale.com/blog/rag-is-more-than-just-vector-search/).
## Overview on RAG
RAG, or retrieval-augmented generation, is an AI framework that enhances generative language models by combining them with traditional information retrieval systems.

RAGs operate in two main steps:

1. **Retrieval and pre-processing**: powerful search algorithms query external data sources, with the retrieved information undergoing pre-processing like tokenization and removing stop words.

2. **Generation**: the pre-processed data is integrated into the LLM, enriching its context and enabling more accurate, informative, and engaging responses.

Let’s get into the details of the tools we will use for our RAG application.

## Tool Details
For the RAG application, we'll utilize PostgreSQL with pgvector as our vector database, and Claude Sonnet 3.5 will serve as our LLM. Let’s discuss what they are and their features.

### Pgvector
As of PostgreSQL 16, native vector support isn't available, but **pgvector **addresses this gap by allowing you to store and search vector data within PostgreSQL. This open-source extension allows PostgreSQL to perform tasks typically associated with vector databases, including:

**Advanced search**: Pgvector enables data to be stored as vectors, supporting various nearest-neighbor search algorithms like L2, inner product, and cosine distance for both exact and approximate searches. These algorithms make finding similar and relevant content efficient based on your query.**Versatile applications**: It facilitates finding similar items such as images, documents, or products based on various attributes, enhancing the search functionality in various domains.**Integration with PostgreSQL features**: Pgvector integrates smoothly with PostgreSQL's standard features, including:, which ensures transactional integrity.__ACID compliance__**Point-in-time recovery**, which allows restoration to specific moments., facilitating the combination of data from multiple tables.`JOIN`
support
### Claude Sonnet 3.5
Anthropic’s Claude Sonnet 3.5 outperforms competitors and Claude 3 Opus in various evaluations while matching the speed and cost of Claude 3 Sonnet. Here are some of the key features of the Claude Sonnet 3.5 LLM:

**Speed**: it’s twice as fast as Claude 3 Opus.**Cost**: it’s priced per million tokens, five times less than Opus.**Performance**:- Claude Sonnet 3.5 excels in graduate-level reasoning (GPQA), undergraduate-level knowledge (MMLU), and coding proficiency (HumanEval).
- It outperforms competitor models like OpenAI's GPT-4o and Google's Gemini 1.5 Pro.
**User experience**:- Developers report 3-4 times productivity increases for coding tasks.
- The model is appreciated for its natural and intuitive interaction style.
**Availability**:- Free access to Claude.ai and the Claude iOS app
- Higher rate limits for Claude Pro and Team plan subscribers
- Available via Anthropic API, Amazon Bedrock, and Google Cloud’s Vertex AI
- Web application access is also available
**Input context window**: supports up to 200,000 tokens**Maximum output tokens**: capable of generating up to 4,096 tokens per request
![Cost and intelligence showcase of Claude 3.5 Sonnet](https://www.timescale.com/blog/content/images/2024/09/Retrieval-Augmented-Generation-With-Claude-Sonnet-3.5-and-Pgvector_claude-models-1.png)
__Claude 3.5 Sonnet__## Advanced RAG Implementation
For a basic RAG application example** **using Claude Sonnet 3.5 and pgvector—or simply to refresh your knowledge—you can always check our [ previous article](https://www.timescale.com/blog/retrieval-augmented-generation-with-claude-sonnet-3-5-and-pgvector). For the purpose of this tutorial

**,**we will build a smart image gallery where you can query the images in natural language and ask questions about them.
![The schematic diagram for our AI gallery application using RAG](https://www.timescale.com/blog/content/images/2024/09/Retrieval-Augmented-Generation-With-Claude-Sonnet-3.5-and-Pgvector_diagram-2.png)
Let’s break the architecture down into bits:

**Images**: The process starts with a set of images. These images are the raw data that will be used for processing and querying. Here, we will use Flickr30 as our dataset.**Image embeddings (CLIP)**: The images are then passed through a model like CLIP (Contrastive Language–Image Pre-training), which generates embeddings for each image.**Vector database**: The generated image embeddings are stored in a vector database. This database is hosted onand allows efficient indexing and querying of the high-dimensional vectors.__Timescale Cloud__**Query**: A user or system inputs a query, which is a text description. This query is also converted into an embedding, which is then used to search the vector database for similar images.**Top results**: The vector database returns the top images that are most similar to the query based on the vector embeddings. These results are the most relevant images found in the database.**Prompt and query**: The original prompt (if applicable) and the query are then combined. This combination of context and query is used to refine the results further or to generate a final response.**LLM**: The combined prompt and query are passed to an LLM that uses the contextual information and the top results from the vector search to generate a final output or response.**Result**: The final output, which is a textual description that answers the initial query, is generated.
### Flickr30 dataset
As we build a smart image gallery application, our dataset must reflect images similar to those of a typical phone user. The Flickr30k dataset is an excellent choice for this purpose. It is a well-known benchmark for sentence-based image descriptions, containing 31,783 images that depict people engaged in everyday activities and events.

Widely used as a standard benchmark, Flickr30k is ideal for evaluating models that generate sentence-based portrayals of images. To make it more realistic, we won't provide captions, as they typically aren't included when a photo is taken on a phone. The dataset is available on [ Kaggle](https://www.kaggle.com/datasets/hsankesara/flickr-image-dataset?ref=timescale.com) and can be easily downloaded. Here’s how to do it:

```
od.download("https://www.kaggle.com/datasets/hsankesara/flickr-image-dataset")
```
The code will prompt you for credentials, which can be easily generated by navigating to **Settings** >> **Create New Token**:

![](https://www.timescale.com/blog/content/images/2024/09/Advanced-RAG-With-Pgvector-and-Claude-Sonnet-3.5_kaggle.png)
Since the dataset is quite large, approximately **8 GB**, we will take a sample of 100 images. The following code randomly selects 100 images and copies them to the destination folder using **shutil****. **

```
# Define the path to the folder containing the images
folder_path = 'flickr-image-dataset/flickr30k_images/flickr30k_images'
destination_folder = 'Subset_dataset'
num_images_to_select = 100
# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)
# List all files in the folder
all_files = os.listdir(folder_path)
# Optionally filter out non-image files (if necessary)
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
image_files = [file for file in all_files if any(file.lower().endswith(ext) for ext in image_extensions)]
# Randomly select 100 images
selected_images = random.sample(image_files, num_images_to_select)
# Copy the selected images to the destination folder
for image in selected_images:
src_path = os.path.join(folder_path, image)
dst_path = os.path.join(destination_folder, image)
shutil.copy(src_path, dst_path)
destination_files = os.listdir(destination_folder)
destination_filepaths = [os.path.join(destination_folder, file) for file in destination_files]
```
### Image embeddings
To convert images to embedding, we will use** CLIP** (Contrastive Language–Image Pre-training), developed by OpenAI. CLIP is a model that links visual and textual data by learning from images and descriptions. In the code below, we are:

**Loading the model**:`clip-ViT-B-32`
is loaded using SentenceTransformer.**Encoding images**: The`model. encode`
function generates embeddings for images opened from`destination_filepaths`
, capturing essential visual features for further use.
```
from sentence_transformers import SentenceTransformer
from PIL import Image
# Load CLIP model
img_model = SentenceTransformer("clip-ViT-B-32")
# Encode an image:
img_emb = model.encode([Image.open(filepath) for filepath in destination_filepaths])
img_emb = img_emb.tolist()
```
### Table creation and insertion
We’ll create the `image_gallery`
table to store our images and their embeddings. Usually, the images are not stored directly in a database; a reference is stored in a file system containing the image. We will approach it the same way. The table will have the following columns:

**Id**: Serves as the primary key to identify each row uniquely.**Path**: Stores the file path of the images as.`TEXT`
**Embedding**: This stores the image embeddings as. The`VECTOR`
size is set to 512, the dimension of the embeddings used for image representations.`VECTOR`
```
cursor.execute(document_table)
conn.commit()
```
The code below constructs an** **SQL** **`INSERT`
** **statement to add image file paths and their embeddings to the `image_gallery`
table. It prepares the parameters by interleaving file paths and embeddings, then executes the statement and commits the transaction to the database.

```
sql = 'INSERT INTO image_gallery (path, embedding) VALUES ' + ', '.join(['(%s, %s)' for _ in img_emb])
params = list(itertools.chain(*zip(destination_filepaths, img_emb)))
cursor.execute(sql, params)
conn.commit()
Creating the ivfflat index just like before:
ivfflat = """CREATE INDEX ON image_gallery USING ivfflat (embedding vector_cosine_ops)"""
cursor.execute(ivfflat)
conn.commit()
```
### Image search
The code below performs an image search based on a text query. It defines a function `image_search`
that encodes a query into embeddings. Then, it searches the `image_gallery`
table for the top five closest image embeddings, returning their file paths.

```
def image_search(conn, query):
query_embeddings = img_model.encode(query).tolist()
with conn.cursor() as cur:
cur.execute('SELECT path FROM image_gallery ORDER BY embedding <=> %s::vector LIMIT 5', (query_embeddings))
return cur.fetchall()
query = ["What is my grandpa holding"]
print(image_search(conn, query))
```
This is the image retrieved from the function:

![A man holding a small wooden cabinet](https://www.timescale.com/blog/content/images/2024/09/Advanced-RAG-With-Pgvector-and-Claude-Sonnet-3.5_image.png)
Now, let's ask the Claude model more about the image.

### Combining the LLM and search
You can break down the code below into the following parts:

**Retrieve relevant image:**
- Call
`image_search`
to get relevant images based on the text query - Encode the image to a base64 string
**Augment query:**
- Create a query string incorporating the text query and context about the image
**Query Claude model:**
- Send a request to the Claude model with the augmented query and encoded image.
- Request the model to describe the image
**Return results:**
- Return the file path of the relevant image and the model's response
**Example usage:**
- Execute
`rag_function`
with a sample query - Display the retrieved image using matplotlib
Here’s the code:

```
def Smart_gallery(conn, client, model_name, query):
relevant_images = image_search(conn, query)
image_media_type = "image/jpeg"
with open(relevant_images[0][0], "rb") as image_file:
encoded_string = base64.b64encode(image_file.read())
image_data =encoded_string.decode('utf-8')
full_query = (f"Context: The following are relevant pictures for the given query.\n"
f"Based on the image, explain what is the picture about:\n"
f"Question: {query[0]}")
message = client.messages.create(
model="claude-3-5-sonnet-20240620",
max_tokens=1024,
messages=[
{
"role": "user",
"content": [
{
"type": "image",
"source": {
"type": "base64",
"media_type": image_media_type,
"data": image_data,
},
},
{
"type": "text",
"text": "Describe this image."
}
],
}
],
)
return relevant_images[0][0], message.content
# Example usage:
query = ["What is my grandpa holding"]
image, text = Smart_gallery(conn, client, "claude-3-5-sonnet-20240620", query)
plt.imshow(Image.open(image))
print(text)
```
And here are the results of the image retrieved and the query result:

![A man holding a wooden cabinet](https://www.timescale.com/blog/content/images/2024/09/Advanced-RAG-With-Pgvector-and-Claude-Sonnet-3.5_image-1.png)
*The model provided the result retrieved by the image search by calculating embedding distance and text after the analysis*`>>> The image shows an older man with gray hair and a white beard holding what appears to be a handmade wooden cabinet or small structure. He's wearing a gray t-shirt over a white long-sleeved shirt. The wooden item he's holding looks like it could be a dollhouse, a pet enclosure, or a decorative storage cabinet. It has small doors and windows carved into it, giving it a house-like appearance. The man seems to be in a home environment, with curtains visible in the background. His expression suggests he may be examining or presenting the wooden piece, possibly something he has crafted himself.`
We are all set! Thanks to pgvector and Claude Sonnet 3.5, we have successfully completed the AI-powered image gallery.

## Conclusion
Inspired by the enhanced capabilities of retrieval-augmented generation (RAG) with LLMs, we developed an AI image search gallery. This system retrieves similar images based on a text query and uses them as context for Sonnet 3.5.

To link images and text, we employed the CLIP model to generate embeddings, which were then stored in PostgreSQL using pgvector. We performed similarity searches to retrieve image paths, which were subsequently provided to Sonnet 3.5 for context.

Timescale is here to help you build your AI applications faster and more efficiently. With [ Timescale Cloud](https://www.timescale.com/ai?ref=timescale.com), developers can access pgvector, pgvectorscale, and pgai—extensions that turn PostgreSQL into an easy-to-use and high-performance vector database, plus a fully managed cloud database experience.

Both pgai and pgvectorscale are open source under the PostgreSQL license. To install them, check out the [ pgai](https://github.com/timescale/pgai?ref=timescale.com) and

[GitHub repos (⭐s welcome!). You can access pgai and pgvectorscale on any database service on the Timescale Cloud PostgreSQL platform.](https://github.com/timescale/pgvectorscale?ref=timescale.com)
__pgvectorscale__[.](http://console.cloud.timescale.com/signup?ref=timescale.com)
__Build your AI application with Timescale Cloud today__