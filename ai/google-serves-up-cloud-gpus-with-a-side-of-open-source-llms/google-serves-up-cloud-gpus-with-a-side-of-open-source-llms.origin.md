# Google Serves Up Cloud GPUs With a Side of Open Source LLMs
![Featued image for: Google Serves Up Cloud GPUs With a Side of Open Source LLMs](https://cdn.thenewstack.io/media/2024/08/172dd2cf-george-c-hsyq2hk91lo-unsplash-1-1024x576.jpg)
If you are a big fan of open source AI but don’t have the computing capacity to run AI models locally, Google has your back (but at a cost).

The company is bringing Nvidia’s L4 GPUs to its cloud service. L4 GPUs are lightweight versions of the H100 GPUs, which trained Meta’s Llama 3.1 and OpenAI’s GPT-4o model.

Developers can log into Google’s [Cloud Run](https://cloud.google.com/run?hl=en#build-applications-or-websites-quickly-on-a-fully-managed-platform), load Ollama in a container, fire up [open source LLMs](https://thenewstack.io/linux-foundation-backs-open-source-llm-initiative/) such as Google’s Gemma 2 or Meta’s Llama 3.1, point to L4 GPUs, and get down to inferencing. The instructions are provided further below.

## Finally, Serving the Open Source Community
Google finally has a full hardware and software package on which open source developers can create applications from open source models.

Developers get full control on the front-end and back-end, and can point to the L4 hardware in Google Cloud via Cloud Run.

The Cloud Run service so far was limited to Google’s proprietary models, which include Gemini 1.0 LLM, Imagen for image generation, and Gemini 1.5 Flash for multimodal models.

Cloud Run now has Gemma 2, which is an open source version of Gemini, and Llama 3.1. The L4 GPUs are also a new addition, and made available to run inferencing on open source models.

Amazon offers Bedrock with a wide range of closed and open source LLMs. It offers L4 chips with older AMD x86 chips in its [EC2 G6 instances](https://aws.amazon.com/ec2/instance-types/g6/). Amazon still doesn’t pair GPUs with its homegrown Graviton chips due to compatibility issues.

Microsoft, meanwhile, has an AI strategy around OpenAI’s proprietary LLM and Nvidia’s GPUs (which has its proprietary [CUDA development stack](https://thenewstack.io/nvidia-wants-to-rewrite-the-software-development-stack/)).

## An Alternative to Running LLMs Locally on PCs
Google’s offering is an alternative to the long process of loading Ollama and [running LLMs locally on PCs](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/). Google’s Cloud Run will load LLMs and Ollama in under 30 seconds.

In most cases, most PCs don’t have the GPUs needed to run LLMs within large context windows. Applications like LM Studio have made it possible to download LLMs — and the software shows whether those LLMs will run on local GPUs — but it still takes time.

The latest models available on Cloud Run include the 9-billion parameter Gemma 2 and the 8-billion parameter Llama 3.1. The other models available include the 13-billion parameter Llama 2 and the 2-billion Gemma.

Google said Cloud Run instances with a L4 GPU will load in about 5 seconds, after which it takes a few more seconds to initialize the framework and model with Ollama. The entire LLMs, which are sized up to 7.4GB, are downloaded and initiated in a matter of seconds.

The smallest 2-billion Gemma model takes 11 to 17 seconds, while the latest 9-billion parameter Gemma 2 takes 25 to 30 seconds. The 8-billion parameter Llama 3.1 takes 15 to 21 seconds to load.

Cloud Run GPUs are currently only available in Google’s us-central1 (Iowa), with Europe and Asia availability by the end of this year.

“We may offer more GPU options and expand to more regions in the future,” Google said in an email.

## Instructions
Google has trained its proprietary Gemini model to work on its [TPUs](https://thenewstack.io/train-and-deploy-tensorflow-models-optimized-for-google-edge-tpu/), but built the downloadable open source Gemma to work on commodity hardware. Laptops won’t have TPUs.

Google has help from Ollama on this offering. Developers need to point to the LLM and the hardware.

Google advises to first create a container image with Ollama and the model with this Dockerfile:

12345 |
FROM ollama/ollamaENV HOME /rootWORKDIR /RUN ollama serve & sleep 10 && ollama pull gemma2ENTRYPOINT ["ollama","serve"] |
Then deploy using the following command:
`gcloud beta run deploy --source . --port 11434 --no-cpu-throttling --cpu 8 --memory 32Gi --gpu 1 --gpu-type=nvidia-l4`
The `--gpu`
flag needs to specify the number of GPUs, and the `--gpu-type`
flag needs to specify the type of GPU in the command line. Google said this can also be done in Google Console.

## Pricing
Google hasn’t shared pricing for running the open source Llama and Gemma models on the L4 GPUs. But the cost of using the L4 GPU can be worked out at the [Cloud Run pricing page and calculator](https://cloud.google.com/run/pricing).

If time is money and you don’t have the local processing capacity, the L4 may be the cheapest GPU available. But if you have invested in a laptop with a top-tier GPU and can wait 10 to 20 minutes to download, tinker and load LLMs, stick to that.

## Google’s AI Development Journey
Google tested the patience of the open source community with its bait-and-switch AI strategy. The initial API offerings were free, and a solid reflection of its open source ethos, until it started charging developers to use its tools.

Developers previously borrowed hardware available on Google’s Colab to run inference. It was as simple as Jupyter notebooks with Python scripts, selecting the hardware (CPUs, GPUs or TPUs), and then running video, image, text or voice AI applications. The free tier was intended exclusively for researchers, so developers technically misused it.

But Google Colab ultimately pulled free access to the wide range of GPU access. Most applications couldn’t take advantage of Google’s TPUs, and defaulted to CPUs, which is painfully slow. The only GPU offered on Colab now is Nvidia’s T4, which is close to eight years old.

Google relied heavily on the research and open source community to develop its AI products, but then asked the same community to pay up to use its model.

Google surprised the developer community in April with wholesale changes to monetize its AI development tools.

The company restricted free access to its proprietary Google Gemini model, and [introduced](https://ai.google.dev/pricing) a pay-as-you-go model. That upset developers who created AI applications on Gemini, but now had to pay.

Google was under market pressure to monetize its AI products. It also had to cover the cost of billions invested in data centers to serve AI applications.

Google relied heavily on the research and open source community to develop its AI products, but then asked the same community to pay up to use its model. But the company — a big advocate of open source — hyped the Gemma and Gemma 2 LLMs as its contribution to the open source community.

With Nvidia’s L4 GPU, Google is also bringing relatively more affordable access to hardware to run AI. Fast-performing GPUs are hard to find, and very expensive, so the L4 fills a gap.

Google recently released Trillium, its homegrown AI chip, which is dedicated to training and demanding inferencing workloads. Trillium is the sixth generation of its AI chips, following the TPUv5 family.

Apple trained its homegrown AI models used in Apple Intelligence on Google’s TPUv4 and TPUv5 chips. Developers can access the TPUv4 via Google Colab.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)