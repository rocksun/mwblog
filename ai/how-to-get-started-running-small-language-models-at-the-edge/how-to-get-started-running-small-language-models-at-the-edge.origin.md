# How To Get Started Running Small Language Models at the Edge
![Featued image for: How To Get Started Running Small Language Models at the Edge](https://cdn.thenewstack.io/media/2024/07/6ecf3e41-getty-images-zyyrzizlmao-unsplash-1024x702.jpg)
In my previous article, I introduced the idea of [federated language models](https://thenewstack.io/federated-language-models-slms-at-the-edge-plus-cloud-llms/) that take advantage of [large language models](https://thenewstack.io/llm/) (LLM) running in the cloud and [small language models](https://thenewstack.io/the-rise-of-small-language-models/) (SLM) running at the edge.

My goal is to run an SLM at the edge that can respond to user queries based on the context that the local tools provide. One of the ideal candidates for this use case is the [Jetson Orin Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-agx-orin-devkit) from Nvidia, which runs SLMs like [Microsoft Phi-3](https://azure.microsoft.com/en-us/products/phi-3).

In this tutorial, I will walk you through the steps involved in configuring [Ollama](https://ollama.com/), a lightweight model server, on the Jetson Orin Developer Kit, which takes advantage of GPU acceleration to speed up the inference of Phi-3. This is one of the key steps in configuring federated language models spanning the cloud and the edge.

## What Is Nvidia Jetson AGX Orin Developer Kit?
The NVIDIA Jetson AGX Orin Developer Kit represents a significant leap forward in edge AI and robotics computing. This powerful kit includes a high-performance Jetson AGX Orin module, capable of delivering up to 275 TOPS of AI performance and offering eight times the capabilities of its predecessor, the Jetson AGX Xavier. The developer kit is designed to emulate the performance and power characteristics of all Jetson Orin modules, making it an incredibly versatile tool for developers working on advanced robotics and edge AI applications across various industries.

At the heart of the developer kit is the Jetson AGX Orin module, featuring an Nvidia Ampere architecture GPU with 2048 CUDA cores and 64 tensor cores, alongside a 12-core Arm Cortex-A78AE CPU. The kit comes with a reference carrier board that exposes numerous standard hardware interfaces, enabling rapid prototyping and development. With options for 32GB or 64GB of memory, support for multiple concurrent AI inference pipelines, and power configurations ranging from 15W to 50W, the Jetson AGX Orin Developer Kit provides developers with a flexible and powerful platform for creating cutting-edge AI solutions in fields such as manufacturing, logistics, healthcare, and smart cities.

See also: our previous tutorial on

[running real-time object detection with Jetson Orin].
For this scenario, I am using the Jetson AGX Orin Developer Kit with 32GB of RAM and 64GB of eMMC storage. It runs the latest version of Jetpack, 6.0, which comes with various tools, including the CUDA runtime.

The most important components of Jetpack are Docker and the Nvidia Container Toolkit.

## Running Ollama on Jetson AGX Orin Developer Kit
Ollama is a developer-friendly LLM infrastructure modeled around Docker. It’s already optimized to run on Jetson devices.

Similar to Docker, Ollama has two components: the server and the client. We will first install the client, which comes with a CLI that can talk to the inference engine.

12345 |
wget https://github.com/ollama/ollama/releases/download/v0.2.8/ollama-linux-arm64chmod +x ./ollama-linux-arm64sudo mv ollama-linux-arm64 /usr/local/bin/ollama |
The above commands download and install the Ollama client.
Verify the client with the below command:

1 |
ollama --version |
Now, we will run the Ollama inference server through a Docker container. This avoids any issues you may encounter while accessing the GPU.
123456 |
docker run -d \--runtime nvidia \--name ollama \--network=host -v ~/models:/models \-e OLLAMA_MODELS=/models \ dustynv/ollama:r36.2.0 ollama serve |
This command launches the Ollama server on the host network, enabling the client to directly talk to the engine. The server is listening on port 11434, which exposes an OpenAI-compatible REST endpoint.
Running the command `ollama ps`
shows an empty list, since we haven’t downloaded the model yet.

## Serving Microsoft Phi-3 SLM on Ollama
Microsoft’s Phi-3 represents a significant advancement in small language models (SLMs), offering impressive capabilities in a compact package. The Phi-3 family includes models ranging from 3.8 billion to 14 billion parameters, with the Phi-3-mini (3.8B) already available and larger versions like Phi-3-small (7B) and Phi-3-medium (14B) coming soon.

The Phi-3 models are designed for efficiency and accessibility, making them suitable for deployment on resource-constrained edge devices and smartphones. They feature a transformer decoder architecture with a default context length of 4K tokens, with a long context version (Phi-3-mini-128K) extending to 128K tokens.

For this tutorial, we will run the 4K flavor of the model, which is [Phi-3 mini](https://ollama.com/library/phi3:instruct).

With the Ollama container running and the client installed, we can pull the image with the below command:

1 |
ollama run phi3:mini |
Check the model with the command `ollama ls`
.

## Accessing Phi-3 from a Jupyter Notebook
Since Ollama exposes an OpenAI-compatible API endpoint, we can use the standard OpenAI Python client to interact with the model.

1 |
pip install openai |
Try the below code snippet by replacing the URL with the IP address of Jetson Orin.

123456789101112131415161718192021 |
from openai import OpenAIOLLAMA_URL="YOUR_JETSON_IP::11434/v1/"client = OpenAI(base_url=OLLAMA_URL,api_key='ollama')prompt="When was Mahatma Gandhi born? Answer in the most concise form."model="phi3:mini"response = client.chat.completions.create(model=model,max_tokens=50,messages=[{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": prompt}])print(response.choices[0].message.content.strip()) |
On the Jetson device, you can monitor the consumption of the GPU with the `jtop`
command.
This tutorial covered the essential steps required to run Microsoft Phi-3 SLM on a Nvidia Jetson Orin edge device. In the next part of the series, we will continue building the federated LM application by leveraging this model. Stay tuned.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)