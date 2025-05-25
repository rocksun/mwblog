# Build GenAI Applications Locally With Docker Model Runner
![Featued image for: Build GenAI Applications Locally With Docker Model Runner](https://cdn.thenewstack.io/media/2024/09/b152c34d-docker-1024x683.png)
[Docker Model Runner](https://docs.docker.com/model-runner/) is a new feature of the [Docker Desktop](https://thenewstack.io/create-a-development-environment-in-docker-desktop/) designed to streamline the process of running and testing AI models locally within the [Docker ecosystem](https://thenewstack.io/docker-launches-hardened-images-intensifying-secure-container-market/). It addresses the long-standing challenges developers face when integrating generative AI and large language models into their workflows, such as fragmented tooling, complex environment setup and inconsistent model management.
By embedding a host-native inference engine directly into [Docker Desktop](https://docs.docker.com/desktop/), Model Runner eliminates the need for containerizing every AI workload, which not only boosts performance but also simplifies the user experience. The inference engine, currently built on top of [llama.cpp](https://github.com/ggml-org/llama.cpp), operates as a native process on the host machine. This approach ensures that model weights are loaded efficiently and that the system can take full advantage of local hardware, including direct GPU acceleration on Apple silicon systems. This native execution bypasses the traditional overhead associated with running models inside containers or virtual machines, resulting in faster inference and smoother development cycles.

## Prerequisites for Docker Model Runner
To run Docker Model Runner, you need to meet several prerequisites related to your Docker environment and hardware. First, you must have Docker Desktop version 4.41 or later installed. Docker Model Runner is integrated as a feature within Docker Desktop, so earlier versions do not support it. You also need Docker Compose version 2.35 or later if you plan to use Model Runner with multi-container applications or Compose files.

Hardware compatibility is essential. On Mac, Docker Model Runner requires Apple silicon (M1, M2 or newer). On Windows, you need a system with an NVIDIA GPU to take advantage of local inference acceleration. The feature is not currently available for Linux or for Intel-based Macs.

## Enabling Model Runner
If you are running the latest version of Docker Desktop, you can access the Dashboard settings to enable Model Runner.

From the command line, run the following commands to enable the same:

1 |
docker desktop enable model-runner --tcp 12434 |
You now have a llama.cpp inference engine running on macOS. You can verify the same with the below command:
1 |
docker model status |
Once enabled, you can follow the familiar commands to pull and run models. Similar to `docker images list`
command, you can run `docker model list`
to list all the downloaded models.
## Pulling and Running Gemma LLM
Similar to the container registry, Docker has a registry for generative AI models, which can be accessed at [hub.docker.com/u/ai](https://hub.docker.com/u/ai). Models are stored in the same OCI format as the container images.

Let’s pull and run the [Gemma3](https://blog.google/technology/developers/gemma-3/) model locally.

1 |
docker model pull ai/gemma3 |
After the model is downloaded, you can confirm its availability with the following command:
1 |
docker model list |
We can now use a [cURL command](https://thenewstack.io/curl-fights-a-flood-of-ai-generated-bug-reports-from-hackerone/) to access the model through the OpenAI-compatible API endpoint.
123456789101112131415 |
curl http://localhost:12434/engines/llama.cpp/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "ai/gemma3", "messages": [ { "role": "system", "content": "You are a helpful assistant." }, { "role": "user", "content": "Who was the captain of the Indian cricket team during the 1983 World Cup?" } ] }' |
## Pulling and Running Embeddings Models From Hugging Face
Docker Model Runner supports pulling models directly from the Hugging Face [model repository](https://huggingface.co/models), provided the models are compatible with llama.cpp. For this example, I am going to pull the [mxbai-embed-large-v1](https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1) embeddings model from Hugging Face.

1 |
docker model pull hf.co/mixedbread-ai/mxbai-embed-large-v1 |
Since this has a [GGUF](https://huggingface.co/docs/hub/en/gguf) flavor of the model optimized for the CPU, and is fully compatible with llama.cpp engine, Docker successfully downloads the model.
You can test it using the command shown below.

123456 |
curl http://localhost:12434/engines/llama.cpp/v1/embeddings \ -H "Content-Type: application/json" \ -d '{ "model": "hf.co/mixedbread-ai/mxbai-embed-large-v1", "input": "Embeddings made easy" }' |
You can also see the models downloaded in the Docker Desktop dashboard.
With both the text embedding model and an LLM running locally, we can develop RAG and agentic applications on our development machine without using remote inference engines or endpoints.

Docker Model Runner marks a significant advancement in local AI development by making it fast, simple and integrated within the Docker ecosystem. It enables developers to pull, run and manage AI models directly on their machines without the complexity of traditional infrastructure setup or the overhead of containerized inference. By leveraging a host-native inference engine and supporting direct GPU acceleration, especially on Apple silicon, Model Runner delivers high performance and efficient resource usage. Models are distributed as OCI artifacts, allowing for standardized packaging, versioning and seamless integration with existing Docker workflows. The use of OpenAI-compatible APIs ensures easy adoption and compatibility with existing applications.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)