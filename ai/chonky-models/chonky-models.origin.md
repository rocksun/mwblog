A majestic blue tiger riding on a sailing ship. The tiger is very large. Image generated using PonyXL.

AI models can get pretty darn large. Larger models seem to perform better than smaller models, but we don’t quite know why. My work MacBook has 64 gigabytes of RAM and I’m able to use nearly all of it when I do AI inference. Somehow these 40+ gigabyte blobs of floating point numbers are able to take a question about the color of the sky and spit out an answer. At some level this is a miracle of technology, but how does it work?

Today I’m going to cover what an AI model really is and the parts that make it up. I’m not going to cover the linear algebra at play nor any of the neural networks. Most people want to start with an off the shelf model, anyway.

## What are AI models made out of?[](#what-are-ai-models-made-out-of)
At the core an AI model is really just a ball of floating-point numbers that the input goes through to get an output. There’s two basic kinds of models: language models and image diffusion models. They’re both very similar, but they have some different parts.

A text generation model has a few basic parts:

- A tokenizer model to break input into pieces of words, grammatical separators, and emoji.
- An embedding model to take the frequencies of relationships between tokens and generate the “concept”, which is what allows a model to see that “hot” and “warm” are similar.
- Token predictor weights, which the embeddings are passed through in order to determine which tokens are most likely to come next.
Note these are really three individual models
[stacked](https://bojackhorseman.fandom.com/wiki/Vincent_Adultman) on top of
each other, but they only make sense together. You cannot separate them nor
exchange the parts.

Of all of those, the token predictor weights are the biggest part. The number of “parameters” a language model has refers to the number of floating point numbers in the token predictor weights. An 8 billion parameter language has 8 billion floating point parameters.

An image diffusion model has most of the same parts as a language model:

- A tokenizer to take your input and break it into pieces of words, grammatical separators, and emoji.
- An embedding model to turn those tokens into a latent space, a kind of embedding that works better for latent diffusion.
- A de-noising model (unet) that gradually removes noise from the latent space to make the image reveal itself.
- A Variational AutoEncoder (VAE) that is used to encode a latent space into an image.
Most of the time, a single model (such as Stable Diffusion XL, PonyXL, or a
finetune) will include all four of these models in one single `.safetensors`
file.

In the earlier days of Stable Diffusion 1.5, you usually got massive quality gains by swapping out the VAE model for a variant that works best for you (one does anime style images better, one was optimized for making hands look correct, one was optimized for a specific kind of pastel watercolor style, etc). Stable Diffusion XL and later largely made the VAE that’s baked into the model good enough that you no longer needed to care.

Of the three stacked models, the de-noising model is the size that's cited. The tokenizer, embedding model, and variational autoencoder are extras on the side. Stable Diffusion XL has 6.6 billion parameters and Flux [dev] has 12 billion parameters in their de-noising models, and the other models fit into about 5-10% of the model size and are not counted by the number of parameters, however they do contribute to the final model size.

We currently believe that the more parameters a model has allows it to represent nuance more accurately. This generally means that a 70 billion parameter language model is able to handle tasks that an 8 billion parameter language model can’t, or that a 70 billion parameter language model will be able to do tasks better than an 8 billion parameter language model.

Recently smaller models are catching up,
[bigger isn't always better](https://www.scientificamerican.com/article/when-it-comes-to-ai-models-bigger-isnt-always-better/).
Bigger models require more compute and introduce performance bottlenecks. The
reality is that people are going to use large models, so we need to design
systems that can handle them.

## Quantization[](#quantization)
If you’re lucky enough to have access to high-vram GPUs on the cheap, you don’t need to worry about quantization. Quantization is a form of compression where you take a model’s floating-point weights and convert them to a smaller number, such as converting a 70 billion parameter model with 140 gigabytes of float16 parameters (16 bit floating numbers) to 35 gigabytes of 4-bit parameters (Q4). This is a lossy operation, but it will save precious gigabytes from your docker images and let bigger models fit into smaller GPUs.

When you read a model quantization level like `Q4`
or `fp16`
/`float16`
, you can
interpret it like this:

Initial Letter | Number | What it means |
---|---|---|
`Q` or `I` | `4` | Four bit integers |
`f`, `fp`, or `float` | `16` | 16 bit
|
Using quantization is a tradeoff between the amount of video memory (GPU ram) you have and the desired task. A 70B model at Q4 quantization will have a loss in quality compared to running it at the full float16 quantization, but you can run that 70B model on a single GPU instead of needing two to four GPUs to get it running.

Most of the time you won’t need to quantize image diffusion models to get them running (with some exceptions for getting Flux [dev] running on low-end consumer GPUs). This is something that is almost exclusively done with language models.

In order to figure out how much memory a model needs at float16 quantization, follow this rule of thumb:

`(Number of parameters * size of each parameter) * 1.25`
This means that an 8 billion parameter model at 16 bit floating point precision will take about 20 gigabytes of video memory, but can use more depending on the size of your context window.

## Where to store them[](#where-to-store-them)
The bigger your AI model, the larger the weights will be.

AI models are big blobs of data (model weights and overhead) that need to be loaded into GPU memory for use. Most of the time, the runtimes for AI models want the bytes for the model to be present on the disk before they load them. This raises the question of “Where do I store these things?”

There’s several options that people use in production:

- Git LFS such as with HuggingFace.
- Putting the model weights into object storage (like Tigris) and downloading them when the application starts up.
- Putting the model weights into dedicated layers of your docker images (such as
with
[depot.ai](https://depot.ai/)). - Mounting a remote filesystem that has the models already in them and using that directly.
All of these have their own pros and cons. Git LFS is mature, but if you want to
run it on your own hardware, it requires you to set up a dedicated git forge
program such as Gitea. Using a remote filesystem can lock you into the
provider’s implementation of that filesystem (such as with AWS Elastic
FileSystem). Putting model weights into your docker images can cause extraction
time to increase and can go over the limits of your docker registry of choice.
When using Tigris (or another object store), you'll need to either download the
model weights to disk on startup or set up a performant shared filesystem like
[GeeseFS](https://www.tigrisdata.com/docs/training/geesefs-linux/).

Keep all this in mind as you’re comparing options.

## In summary[](#in-summary)
We’ve spent a lot of time as an industry thinking about the efficiency of Docker builds and moving code around as immutable artifacts. AI models have the same classic problems, but with larger artifact size. Many systems are designed under the assumption that your images are under an undocumented “reasonable” size limit, probably less than 140 gigabytes of floating-point numbers.

Don’t feel bad if your system is struggling to keep up with the rapid rate of image growth. It wasn’t designed to deal with the problems we have today, so we get to build with new tools. However, in a pinch shoving your model weights into a Docker image will work out just fine if you’re dealing with 8 billion parameter models at Q4 quantization or less.

Above that threshold, you’ll need to chunk up your models into smaller pieces
[like upstream models do](https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-70B/tree/main).
If that’s a problem, you can store your models in Tigris. We’ll handle any large
files for you without filetype restrictions or restrictive limits. Our filesize
limit is 5 terabytes. If your model is bigger than 5 terabytes, please get in
touch with us. We would love to know how we can help.

# Want to try it out?
Make a global bucket with no egress fees and store all your models all over the world.