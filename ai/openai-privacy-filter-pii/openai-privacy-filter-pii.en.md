OpenAI has debuted Privacy Filter, a bidirectional token-classification model for detecting and redacting personally identifiable information (PII) that can scan long-form text in a single pass, run locally, and deliver greater context-awareness.

## Scanning text in a single pass for emails, numbers, and more

For developers working with large language models (LLMs), data privacy has long been a recurring issue. But with its new Privacy Filter, released on Wednesday, OpenAI is essentially opening up access to what it uses in-house for its own privacy-preserving workflows.

So, how does it work?

As OpenAI explains in its announcement [blog post](https://openai.com/index/introducing-openai-privacy-filter/), it starts with an autoregressive pretrained checkpoint and converts it into a token classifier over a fixed taxonomy of privacy labels.

Rather than generating each token at a time, it “labels an input sequence in one pass and then decodes coherent spans with a constrained Viterbi procedure.”

There are eight such labels, allowing Privacy Filter to mask or redact names, addresses, emails, phone numbers, URLs, dates, account numbers, and secrets (e.g., API keys or passwords).

(It’s a decent round-up, but it doesn’t catch everything; social security numbers and passport numbers, for example, are overlooked.)

## Greater context-awareness, run locally

OpenAI claims Privacy Filter has greater context awareness, allowing it to pick up on subtler personal information and make more nuanced decisions.

> “By combining strong language understanding with a privacy-specific labeling system, it can detect a wider range of PII in unstructured text, including cases where the right decision depends on context.”

Specifically, the AI company claims its bidirectional token-classification model is a step up from traditional PII detection tools (such as regular expressions (RegEx) or NLP libraries), which typically rely on deterministic rules for format.

While these approaches might get the job done for simpler cases, like phone numbers or email addresses, they’re more likely to run into problems when context introduces more subtlety:

“By combining strong language understanding with a privacy-specific labeling system, it can detect a wider range of PII in unstructured text, including cases where the right decision depends on context.”

For example, Privacy Filter should be able to distinguish between publicly available information that it can preserve and private information that it should mask or redact, such as a public business address versus a private home address.

This focus on context also comes into play when processing lengthy documents with unstructured text. OpenAI says Privacy Filter was specifically designed to catch PII in “noisy, real-world” texts, perhaps support logs, long legal filings, and the like. To scan these long-form texts without chunking, the model supports up to 128,000 tokens of context.

Privacy Filter is also notably small.

At 1.5 billion total parameters with 50 million active parameters, the model is snappy enough to run locally on a browser or laptop. Besides efficiency gains, this means developers can use Privacy Filter to mask and redact PII in their own environments, thereby reducing exposure risks for sensitive data.

## How it compares to the competition

In its announcement blog post, OpenAI boasts that Privacy Filter “achieves state-of-the-art performance on the [PII-Masking-300k benchmark](https://huggingface.co/datasets/ai4privacy/pii-masking-300k), when corrected for annotation issues we identified during evaluation.”

What it calls “state of the art” is an F1 score of 96% (94.04% precision and 98.04% recall).

Of course, OpenAI isn’t the first to offer a PII detection and redaction solution.

[Microsoft’s Presidio](https://github.com/microsoft/presidio), for example, is an open-source framework for detecting, redacting, masking, and anonymizing text, images, and structured data. Here, Microsoft might win: In its blog post, OpenAI flat-out states that Privacy Filter is not an anonymization tool but “one component in a broader privacy-by-design system.”

[Amazon’s Comprehend](https://aws.amazon.com/comprehend/), meanwhile, is a managed service for PII detection and redaction in AWS workflows.

Stacked up against existing competitors, Privacy Filter stands out for its context-aware, locally run design.

Where Microsoft may give developers more capabilities than Privacy Filter, OpenAI’s model makes up for its smaller scope with greater context-awareness and local deployment — at least against Amazon’s managed service.

## What this means for developers

For developers building RAG systems, developing customer support pipelines, or orchestrating any other workflow that requires feeding user text into an LLM, OpenAI says Privacy Filter should slot in nicely.

It’s the option for fine-tuning that adds extra appeal to OpenAI’s model.

And supposedly, it only takes a small amount of data to see results. In its [model card](https://cdn.openai.com/pdf/c66281ed-b638-456a-8ce1-97e9f5264a90/OpenAI-Privacy-Filter-Model-Card.pdf), OpenAI reports that “training on 10% of the dataset is enough to drive F1 scores above 96%.”

That means with relatively little data, developers can adapt OpenAI’s model for different data distributions, privacy policies, and domain-specific tasks.

That said, OpenAI expresses caution about high-sensitivity domains, such as legal, medical, and financial workflows, reminding developers to keep human review in the loop and prepare for potential mistakes.

> “Training on 10% of the dataset is enough to drive F1 scores above 96%.”

## One more piece in OpenAI’s stack

Privacy Filter is available today on [Hugging Face](https://huggingface.co/openai/privacy-filter) and [GitHub](https://github.com/openai/privacy-filter) under the Apache 2.0 license.

It comes alongside [OpenAI’s launch of GPT-5.5](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/), released on Thursday, a new model that OpenAI calls “a new class of intelligence.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)