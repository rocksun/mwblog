# How To Generate ‘AI’ From a Database: Bruce Momjian
![Featued image for: How To Generate ‘AI’ From a Database: Bruce Momjian](https://cdn.thenewstack.io/media/2025/02/3ed2bd43-bruce-monjian-1024x768.jpg)
The next time you ask ChatGPT or another Generative AI service a question, take note of the order of the words in the answer you get.

The last few words in your query will almost invariably be the first few words of the generated response.

That’s an important process of how large language models (LLMs) works — backwards, evaluating each word in terms of each previous one — pointed out [Bruce Momjian](https://momjian.us/), [EDB ](https://www.enterprisedb.com/?utm_content=inline+mention)VP and [Postgres](https://thenewstack.io/the-slow-climb-of-postgres-and-the-value-of-persistence/) evangelist, in a talk at [FOSDEM 2025](https://fosdem.org/2025/schedule/), in Brussels, last month.

Using database technology as a launching point, Momjian walked the audience through how data gets converted into AI, and why we shouldn’t yet mistake data manipulation for actual human intelligence.

## From Descriptive to Generative
Before 2022, what we knew of as “AI” were mostly tasks of discrimination and clarification, where AI would answer questions such as “dog or cat?” or whether or not a credit-card transaction was real. It was great for predictions, classifications, recommendations.

The new “AI,” manifested by the [instant success of ChatGPT](https://thenewstack.io/just-out-of-the-box-chatgpt-causing-waves-of-talk-concern/), is about generating content that did not exist before: summarization, chatbots, semantic search, the creation of images, programming, sounds and video.

Instead of looking for boundaries, as the earlier predictive AI did, generative AI is effectively *generating* new content.

“We’re in the Wild West. We don’t actually know all the things we can do,” Momjian said.

## A Massive Universe of Vectors
The key to this approach starts with [vector processing](https://thenewstack.io/vector-processing-understand-this-new-revolution-in-search/). Google pioneered this technique in a 2018 paper, titled “[Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781),” and offered a model called [word2vec](https://www.tensorflow.org/text/tutorials/word2vec).

A vector is a mathematical object with two numbers, a magnitude (length) and a direction.

Each word in the [training data](https://thenewstack.io/pyconus-simon-willison-on-hacking-llms-for-fun-and-profit/) has a vector with every other word, forming a highly dimensional vector space. (For simplicity’s sake, Momjian focused on text-based generative AI, though the images and other forms of content generation operate on similar principles).

![Slide showing generative vector.](https://cdn.thenewstack.io/media/2025/03/6e38898c-fosdem-momjian-databases_ai-vectors.png)
Slide: Bruce Momjian

This universe of words is very large indeed.

“We’re dealing at a scale that’s just way off the charts for anything we can understand in the physical world,” Momjian said.

A ChatGPT LLM can [have as many](https://community.openai.com/t/what-version-of-gpt-is-text-embedding-ada-002-based-on/404462) as 12,288 dimensions, which total to more than 10 to the 188,000 dimensions, which is way more than the total number of atoms in the universe, Momjian pointed out.

Each word’s vector is given the same length. It is also assigned a direction, a floating point number at random that exists somewhere in this universe of 10 to the 188,000 dimensions.

## Training Day
The next step is to [feed into this space](https://stackoverflow.blog/2023/11/09/an-intuitive-introduction-to-text-embeddings/) a massive amount of training documents.

For each word, its vector will be adjusted to be closer to its surrounding words, and for each of its surrounding words to be closer to the original word.

In this famous set of training data:

*The king is a tall man. *
*The queen is a beautiful woman. *
*They sit together in the throne room of the castle.*
The vector “king” bends toward “man,” “queen” toward “woman” and “throne” to “castle,” and so on, multiplied across the thousands of dimensions.

Over successive iterations, words such as “man,” and “woman” will grow closer together, as will “king” and “queen.”

Also, note that “man” and “woman” will have a similar distance as “king” and “queen,” allowing the LLM to do some basic math to further understand the relations among the words.

And because there are so many dimensions, moving one word closer to another in one dimension won’t necessarily mean that these words will grow more distant to other words.

“When we move ‘man’ closer to ‘woman,’ we’re not moving it necessarily farther from ‘king,’ because the ‘king’s’ closeness to ‘man’ is probably on a different dimension than the closeness of ‘man’ to ‘woman,'” Momjian said.

## From Data to Intelligence
Relational databases do offer full-text search but do not search the meaning of words. This is the power of a vector-based semantic search brings.

Typically in the [LLM training process](https://thenewstack.io/3-ways-llms-can-let-you-down/), blocks of text can be “chunked” into shorter passages. They can be chunked into sentences, paragraphs, or the entire passage can be a single chunk.

Semantic search averages all the vector scores across each chunk.

The Generative AI then takes an average of the vectors in the query itself and finds the sentence, or text chunk, with the nearest score.

Ergo, a query of “Who is the King?” would average most closely to the phrase “The king is a tall man,” meaning the average vector of this phrase is the closest to the average vector of the query.

Momjian revealed [some SQL code](https://momjian.us/main/writings/pgsql/trenches.sql) to make this sample happen, which can be executed using [PGVector](https://github.com/pgvector/pgvector), the vector extension to PostGreSQL. He created a table to hold the content and a table for their embeddings. A python script Momjian created calls OpenAI, sends over each word and gets an embedding back. The vectors are averaged and stored in the database as well.

Then the query “Who is the King?” is sent over, via an API call, to [OpenAI](https://platform.openai.com/docs/overview) for embedding numbers as well. It too is averaged and then compared to all the averages in the database, which was ranked from most similar to least:

![Comparing vector scores](https://cdn.thenewstack.io/media/2025/03/916ed384-fosdem-momjian-databases_ai-vector-compare.png)
Comparing vector scores for the nearest match

“This is different than a full-text search because it has understanding of how the words are related,” Momjian said.

## Generative AI
Vector processing is only the first block of generative AI, Momjian explained. To generate full sentences, you also need [state transformers](https://thenewstack.io/get-ready-for-faster-text-generation-with-diffusion-llms/), a type of [neural network](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) for [natural language processing](https://thenewstack.io/recent-advances-deep-learning-natural-language-processing/).

An [attention block](https://www.datacamp.com/blog/attention-mechanism-in-llms-intuition), also pioneered [by Google in 2017](https://arxiv.org/abs/1706.03762), is a weighted version of the input text. Every query gets a new attention block. Each word is looked up and given 128 dimension number from the LLM. Each word in the input text is weighted to be closer to the others, word by word.

This process of moving words closer together in vectorized space continues for multiple iterations until a full sentence is produced.

And this is why the last phrase in your ChatGPT answer often appears first in the answer — “The capital of France is Paris” — because it is the last to be vectorized. An LLM interprets a sentence in reverse order:

*Columbus is in Ohio. Where is Paris? *
…might bring you this answer:

*Paris is in France. There is also a city named Paris in the United States, located in Texas. If you were referring to a different Paris, please specify!*
Answers can also be further refined through [retrieval augmented generation](https://thenewstack.io/rag-and-model-optimization-a-practical-guide-to-ai/), which gives the LLM additional instructions, such as to keep the reply brief. In this case, a question about the location of Paris would be the simple reply that Paris is in France.

You can also use RAG to return an answer to [data analysis questions](https://thenewstack.io/save-valuable-genai-tokens-with-this-one-simple-trick/). For instance, Momjian showed how you can enter three SQL database insertions into the RAG prefix and it will return the data each command was committed, because the LLM “knows” SQL.

In summary, Momjian concluded that while the speed at which AI is evolving is truly staggering, LLMs are, nonetheless, a sophisticated form of data manipulation and not the possessor of any sort of actual sentience.

*Enjoy Momjian’s entire presentation here. The slides are available here. *
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)