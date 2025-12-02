[Hugging Face](https://huggingface.co/) is a powerful AI library that applies pre-trained models to solve real-world problems. It’s a [Natural Language Processing (NLP)](https://thenewstack.io/top-10-nlp-tools-in-python-for-text-analysis-applications/) library, so it focuses primarily on text-based inputs and outputs. Hugging Face performs complex tasks like summarization, question answering, and sentiment analysis at scale. While similar in purpose to other NLP libraries like the Natural library [discussed in this blog,](https://thenewstack.io/how-to-perform-basic-nlp-in-javascript-with-the-natural-library/) Hugging Face is more advanced because it’s powered by stronger models like GPT, BERT, and [LLaMA](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/). Thanks to these advanced models Hugging Face handles more complex tasks at scale, taking what simpler libraries like Natural can do one step further.

What does Hugging Face, complex NLP at scale, do? Here are a few basic examples.

**Market and Media Analysis**  
This turns unstructured text data into actionable insights for strategic decision-making. Examples include sentiment analysis, which helps you understand opinions about brands, campaigns, and products. It also helps with forecasting like trend monitoring to help you stay on top of what’s just ahead.

**Customer Service**  
Hugging Face improves response time and reduces the manual workload. We see this in our everyday lives now, virtual chatbots helping with FAQs and in some live 24-hour help systems. Behind the scenes Hugging Face handles [sentiment analysis](https://thenewstack.io/build-an-advanced-chat-app-with-quix-and-redpanda-part-1/) which can push angry customers to the front of the customer support line.

**Research and Academia**  
Advanced NLP libraries speed up research times. Hugging Face can condense long scientific papers, articles, and reports into key points.

The following tutorial is super basic. We’re going to generate text, analyze the sentiment of text, and classify a different piece of text. When we finish, you might wonder, why would we build this? And I agree: this tutorial, on its face, serves no purpose. We don’t need a basic text analyzer. However, the benefit of doing this is to see how easy it is to use Hugging Face. Hopefully, this basic tutorial will get you thinking about what you can really build using Hugging Face.

## Let’s Get Started With Python and Hugging Face

This tutorial is best suited for developers with at least a basic understanding of Python or similar language.

Open a new project in your IDE and create a [Python](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/) file. I’m going to call mine `main.py`.

Open a new terminal and let’s start with our installs.  
`transformers` is the Hugging Face library with pre-trained NLP models. `torch` is the backend that runs the models efficiently. `numpy<2` fixes any compatibility issues with mac.

```
pip install transformers torch
pip install "numpy<2"
```

The first time I ran my code file, I got a bunch of errors. Turns out I had an issue with [NumPy](https://thenewstack.io/what-is-the-numpy-python-library-and-how-do-you-use-it/) and my Python environment. This will happen a little later than the setup process but I’m leaving it here so you have the fix before the error (if you get it).

Install `numpy<2`. This will downgrade NumPy to a 1.x version that will work with [PyTorch](https://thenewstack.io/why-pytorch-won/)

```
pip install "numpy<2"
```

Then uninstall `torch` and immediately reinstall and verify that NumPy works.

```
pip uninstall torch
pip install torch --index-url https://download.pytorch.org/whl/cpu
python3 -c "import numpy; print(numpy.__version__)"
```

We’re going to run all our Python/Hugging Face code in the same file.

The first thing we want to do is import Hugging Face’s `pipeline` functionality. `pipeline` is a simple way to use pre-trained models for common tasks (like the basic text app we’re building now). With `pipeline` and its ready to use pipelines you can generate text, analyze sentiment, and answer questions without manually handling tokenization or set up.

```
from transformers import pipeline
```

## Generate Text With GP2-2

We’re using GPT-2 because it’s free and accessible. You can easily change the model to more advanced models by updating the `model=“gpt2”` to the model of your choice (note: the advanced models require an account and come with a fee).

Hugging Face’s `generator` will return a list of results. If you don’t fill in the `max_length`, Hugging Face will default to around 1024 tokens which is very long. The default for `num_return_sequences` is 1.

```
generator = pipeline("text-generation", model="gpt2")


prompt = "Explain how self-driving cars work in simple terms."
result = generator(prompt, max_length=50, num_return_sequences=1)


print("=== Text Generation ===")
print(result[0]['generated_text'])
```

output:  
50 words of text, unique to you, on self driving cars

## Analyze Sentiment

The next code we’re going to write will analyze the sentiment of our generated text. Hugging Face’s sentiment analyzer uses a pre-trained model to determine whether the text is positive, negative, or neutral. The model will first tokenize (break the text into individual words). It then processes those tokens and predicts the overall sentiment using its neural network. It will return a score and a label showing how confident the model is in its classification. The score will be a number between 0 -1 with 0 being not confident, 1 being absolutely sure. The score is not a score of how positive or negative the text is.

```
classifier = pipeline("sentiment-analysis")


text = "I love sunny days."
result = classifier(text)


text2 = "I don't like the rain."
result2 = classifier(text2)


print("\n=== Sentiment Analysis ===")
print(result)
print(result2)
```

output:  
[{‘label’: ‘POSITIVE’, ‘score’: 0.9998550415039062}]  
[{‘label’: ‘NEGATIVE’, ‘score’: 0.9930094480514526}]

## Text Classification

Text classification “reads” the text provided then assigns it a classification. With Hugging Face, for more obscure categories, you’ll need to provide the labels. When working with something as commonly classified as the weather, you can select a specific model that will classify for you. For the example below, we’re going to assign our own categories.

Similarly to sentiment analysis, Hugging Face will return a score between 0-1, 1 being sure the classification is correct, and 0 basically saying the model assigned the classification but doesn’t back its claim.

For this example, we’ll use  `“zero-shot-classification”`. `“zero-shot-classification”` lets the categorize text into new labels it wasn’t explicitly trained on. It helps the model understand the meaning of both the text and label descriptions.

```
classifier = pipeline("zero-shot-classification")


text_to_classify = "I love my new blender! It makes smoothies so smooth."
candidate_labels = ["electronics", "kitchen appliance", "sports equipment", "furniture"]


result3 = classifier(text_to_classify, candidate_labels)
print(result3)
```

output:  
{‘sequence’: ‘I love my new blender! It makes smoothies so smooth.’, ‘labels’: [‘kitchen appliance’, ‘sports equipment’, ‘electronics’, ‘furniture’], ‘scores’: [0.9792253375053406, 0.010719629935920238, 0.007687257137149572, 0.002367804991081357]}

## Conclusion

And now you have your first experience working with the Hugging Face library. What can you build now that you’ve seen a preview of what this library can do?

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)