**The AI industry has largely focused on language-based approaches**, using transformers trained on massive datasets to predict words or fill in missing information.

As AI expands into more structured fields, however, the limitations of text-generation models are becoming clearer. Nvidia is pursuing a different approach.

The company just dropped [JEPA-DNA on Hugging Face](https://huggingface.co/nvidia/NV-JEPA-DNA-DNABERT2). It’s a genomic foundation model that *adds* a latent-space prediction objective alongside MLM.

This release is a win for hybrid architectures that go beyond purely generative training. It’s the kind of shift Executive Chairman of AMI Labs, formerly Meta’s Chief AI Scientist, [Yann LeCun](https://www.linkedin.com/in/yann-lecun/), has been pushing for years. He’s championed predictive architectures as a general alternative to next-token prediction, which researchers are now applying to biology.

## Latent space over literal tokens

Conventional genomic base models have historically mirrored NLP models, relying purely on MLM, masking parts of a DNA sequence and forcing the model to guess the missing literal tokens. This approach favors local token reconstruction and teaches the model the basic “syntax” of the sequence, but it frequently struggles to grasp the wider functional “meaning.”

JEPA-DNA changes the paradigm. The newly released checkpoint, JEPA-DNA-DNABERT2, serves as a model-agnostic continual pre-training framework. It couples standard token-level DNA language modeling with JEPA, adding a second learning objective.

> Instead of forcing the architecture to reconstruct missing tokens, JEPA-DNA supervises the model’s global sequence embedding in a latent space.

Instead of forcing the architecture to reconstruct missing tokens, JEPA-DNA supervises the model’s global sequence embedding in a latent space. It predicts the functional representation of masked genomic segments rather than their literal, character-by-character makeup.

Token prediction is still part of the training process, but it is no longer the model’s only learning objective. The model also learns the basic structure of the data, proving that predictive architectures can produce representations that are easier to work with for biological tasks without sacrificing generative capabilities.

> Token prediction is still part of the training process, but it is no longer the model’s only learning objective.

## How DNABERT-2 gets upgraded

The model builds on DNABERT-2, a 117 million-parameter model developed by Zhihan Zhou and collaborators. Nvidia layers its continual pre-training approach on top of that architecture, letting the model learn from both token-level predictions and latent-space representations.

Nvidia has released the model globally for non-commercial research. According to the company, the model is meant to support research workflows, including feature extraction, linear probing, continual pre-training experiments, and zero-shot scoring of DNA sequence changes. It isn’t a diagnostic tool or a clinically validated medical product.

## Beyond the generative hammer

DNA contains patterns and relationships that aren’t captured by sequence prediction. JEPA-DNA supplements masked-token prediction with a latent-space objective intended to capture broader sequence-level information.

Ultimately, models like JEPA point to a new path for AI that combines next-token prediction with other ways of learning and helping models build a deeper understanding of complex systems.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)