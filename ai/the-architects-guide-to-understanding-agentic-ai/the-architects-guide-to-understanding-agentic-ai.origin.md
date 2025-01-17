# The Architect’s Guide to Understanding Agentic AI
![Featued image for: The Architect’s Guide to Understanding Agentic AI](https://cdn.thenewstack.io/media/2025/01/6061276b-ai-1024x576.jpg)
Often, while accessing the legitimacy of a new technology receiving a lot of hype, studying existing core capabilities and history is helpful. If the new technology in question is not based on existing or imminent capabilities, we can label it as hype and move on.

Another litmus test that history can help us apply requires only common sense. Does the new technology fit an existing trend? Is it the next logical step in the direction of progress? Does it solve problems that were previously hard to solve or unsolvable?

In this architect’s guide for [understanding agentic AI](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/), I hope to show that agentic AI is the next logical evolutionary [advance in AI](https://thenewstack.io/ai/), based on existing capabilities and capabilities that are within reach.

Let’s start by looking at how AI has progressed over the years. Many believe that AI has progressed in three waves, so I will present each wave of AI in the next section. For fun, I will also call out the additional resources that enterprises need to acquire to succeed with each wave of AI.

## The Three Waves Of AI
The first wave of AI was traditional AI, sometimes called predictive AI, which is very straightforward. Given an input to a model, a prediction is made. The prediction could be a unique value (regression), a categorization of the input or a classification of the input. These capabilities are useful for tasks like image classification, sorting emails (categorization) and predicting sales (regression).

This first wave brought us neural networks, a complex system of interconnected nodes (neurons) that can learn from data and make predictions based on patterns identified in training data. (Previously, models were created using prebuilt algorithms with clear steps to achieve a specific outcome.) Neural networks could find patterns in an input of hundreds or even thousands of values. To be successful with traditional AI, organizations had to add a [data lake](https://thenewstack.io/the-architects-guide-a-modern-data-lake-reference-architecture/) to store training sets, validation sets, test sets and the models themselves. Also, improving compute capabilities in the form of adding GPUs to data centers was often necessary as this allowed engineers to run more experiments during the development of models.

![The three waves of AI](https://cdn.thenewstack.io/media/2025/01/033b257d-image1.png)
The three waves of AI.

The second wave of AI brought us generative AI, which generates new content. This can take the form of answering a question, summarizing a long, complex document or even a full conversation at a fluency level capable of passing the Turing test.

[Generative AI](https://thenewstack.io/the-architects-guide-to-the-genai-tech-stack-10-tools/) brought us [large language models (LLMs)](https://roadmap.sh/guides/introduction-to-llms), which are neural networks that are even more complicated than the neural networks introduced in wave No. 1. These neural networks are based on the encoder/decoder architecture outlined in the paper “[Attention is All You Need](https://arxiv.org/abs/1706.03762)” from 2017.
Today, cutting-edge LLMs have parameters in the billions, and soon we will have a trillion-parameter LLM. To be successful with LLMs, organizations had to add a few additional resources and workloads to their data centers, such as data lakehouses, retrieval-augmented generation (RAG), LLM fine-tuning, vector databases and custom corpora (usually built with object storage).

Now, we’re entering the third wave, which is agentic AI. Agentic AI systems can plan, take action and even revise the original plan to improve results. While the first two waves of AI focused on making predictions and generating content, we’re now witnessing the emergence of something far more sophisticated: AI agents that can independently plan, perform tasks and revise the original plan if a poor result is produced. This third wave of AI represents a shift in the way artificial intelligence is used to solve problems. Succeeding with agentic AI will require more computing power than the previous waves, and orchestration tools may be needed to help LLMs manage planning.

Admittedly, this last wave sounds a little like science fiction. It sounds like too big a leap from the previous wave. After all, how can we go from generative AI — which can answer questions, summarize and converse — to agentic AI that can plan, take action and revise? To address this question, we need to look at how we use LLMs today and see what is possible with just a little more engineering. We also need to look at the anatomy of a business process and look for areas where agentic AI could add value.

## How We Use LLMs Today
LLM’s today use what is known as a “zero-shot prompt.” In other words, the LLM is asked to create a response as fast as possible using only “top of mind” information, or information readily accessible from parametric memory. For example, let’s say you have a question “X” to send to an LLM. Essentially, you are asking the LLM to do the following: “Please answer my question ‘X’ start to finish in one pass without using the Backspace button, Delete button or arrow keys to go back and redo any part of your answer. Do not break down my question into smaller tasks and do not review your answer for accuracy.” This is sometimes referred to as asking the LLM to think fast.

Surprisingly, LLMs can put together a coherent and organized response using zero-shot prompts because they are machines. If the human mind tried to communicate in this fashion, the result would be a stream of words that made little sense. If you think about your thought process when answering a question, you will notice yourself breaking the original question down into smaller questions that are easier to answer — putting all your answers together to form an answer to the original question, and then, just before you speak, you will review the answer and possibly revise it. All humans think this way — no one is so smart that their mind can operate in a zero-shot fashion and produce a result as good as a planned and revised response. Even William Faulkner planned and revised his text when writing the “zero-shot thoughts” of Benjy Compson, a cognitively disabled man with fragmented perceptions, in “The Sound and the Fury.”

The two examples above beg the question, “What could LLMs do if we allow them to plan and revise?” This is the promise of agentic AI: to get LLMs to go beyond one-shot responses and allow them to plan, review and revise responses. But before we discuss how LLMs can plan and revise, we need to understand the anatomy of business processes as they are implemented today.

## The Anatomy of a Business Process
All business processes can be broken down into two planes: a control plane and a tools plane. See the graphic below. The tools plane is a collection of APIs, stored procedures and external web calls to business partners. However, for organizations that have started their AI journey, it could also include calls to traditional machine learning models (wave No. 1) and LLMs (wave No. 2) operating in “one-shot” mode.

![The control plane and the tools plane of a business process](https://cdn.thenewstack.io/media/2025/01/48e648aa-image2-1024x586.png)
The control plane and the tools plane of a business process.

The control plane contains the logic of the business process. It’s where conditional branching, looping and calls to an organization’s tools plane are orchestrated to solve problems or achieve automation. To understand the value and promise of agentic AI, you must understand two things about the control plane and how it’s built today:

- It is hard-coded at design time. At run time, it cannot change.
- It is built by engineers who may not completely understand the domain in which an organization operates. Also, they may not be familiar with all the functionality within the tools plane. This is especially true within large organizations that operate in complex industries like financial services.
Even a standalone service can be thought of as having a control plane and a tools plane. The control plane is built with a programming language’s conditional statements and looping constructs. The tools plane is the collection of built-in libraries and referenced third-party libraries. The bottom line is that anything you build with software has a control plane and a tools plane.

## The Promise of Agentic AI
The promise of agentic AI is to use LLMs with full knowledge of an organization’s tools plane and allow them to build and execute the logic needed for the control plane. This can be done by providing a “few-shot” prompt to an LLM that has been fine-tuned on an organization’s tools plane. Below is an example of a “few-shot” prompt that answers the same hypothetical question presented earlier. This is also known as letting the LLM think slowly.

Few-shot prompt example:

- Break down my question “X” into smaller questions.
- Write a draft response to each smaller question.
- Consider the smaller questions that need revision or more research.
- Do you need any additional research?
- Revise your answers.
- Put everything together.
- Review your final response.
The assumption with the tasks above is that the smaller questions can be paired with an internal tool that the LLM is aware of, and the response (or answer) is accompanied by a certainty grade that indicates how confident the tool is of the answer. Guardrails like revising tasks and reviewing final answers are the most important steps in the process outlined above.

If agentic AI still seems to be made up of too much magic, then consider the simple example below. Every developer who has to write code daily probably asks an LLM a question similar to the one below.

“Write me a function that creates an iterable-style data set that connects to MinIO.”

1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859 |
from minio import Miniofrom minio.error import S3Errorclass MinIOIterableDataset: def __init__(self, endpoint, access_key, secret_key, bucket_name, prefix='', secure=True): """ Initialize the MinIOIterableDataset. :param endpoint: The endpoint of the MinIO server (e.g., 'localhost:9000'). :param access_key: Access key for MinIO. :param secret_key: Secret key for MinIO. :param bucket_name: The bucket name to fetch objects from. :param prefix: Prefix to filter objects by (optional). :param secure: Use HTTPS if True, otherwise HTTP. """ self.client = Minio(endpoint, access_key, secret_key, secure=secure) self.bucket_name = bucket_name self.prefix = prefix # Check if the bucket exists if not self.client.bucket_exists(bucket_name): raise ValueError(f"Bucket '{bucket_name}' does not exist.") def __iter__(self): """ Iterator to fetch objects from the bucket. Yields: A dictionary containing object metadata and data content. """ try: for obj in self.client.list_objects(self.bucket_name, prefix=self.prefix, recursive=True): data = self.client.get_object(self.bucket_name, obj.object_name) yield { "object_name": obj.object_name, "size": obj.size, "etag": obj.etag, "last_modified": obj.last_modified, "content": data.read() } data.close() data.release_conn() except S3Error as e: raise RuntimeError(f"Error accessing MinIO bucket: {str(e)}") from e# Example usageif __name__ == "__main__": # Configuration endpoint = "localhost:9000" access_key = "your-access-key" secret_key = "your-secret-key" bucket_name = "my-bucket" prefix = "data/" # Optional: Specify a prefix to filter objects dataset = MinIOIterableDataset(endpoint, access_key, secret_key, bucket_name, prefix) # Iterate over the dataset for item in dataset: print(f"Object Name: {item['object_name']}, Size: {item['size']} bytes") # Access the content with item['content'], e.g., item['content'].decode('utf-8') |
ChatGPT was used to generate the response above. What we see in the response is the use of Python as the control plane that orchestrates calls to functions found in the MinIO SDK and PyTorch, which are examples of the tools plane. The response also tells us that ChatGPT has been trained on Python, MinIO and PyTorch documentation. By analyzing these results from the perspective of the LLM’s knowledge and how this knowledge was acquired, we can conclude that it would not be much of a leap to train an LLM to use an orchestration tool and an organization’s internal tools to dynamically generate the control plane of a business process.
# Conclusion
Agentic AI is the next logical evolution of AI. It is based on capabilities with a solid footing in AI’s first and second waves. The promise is the use of AI to solve more complex problems by allowing them to plan, execute tasks and revise— in other words, allowing them to think slowly. This also promises to produce more accurate responses.

There are no shortcuts to agentic AI. Agentic AI may be the third wave of AI, but it does not replace the previous two waves — it builds upon them. Consequently, the best way to start is to build an AI data infrastructure with object storage. [Object storage](https://thenewstack.io/the-architects-guide-to-using-ai-ml-with-object-storage/) can also be used for cloud repatriation and building a data lakehouse. From there, work up the stack by adding MLOps tooling and workloads to support LLMs, such as fine-tuning, retrieval-augmented generation, distributed computing and MLOps.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)