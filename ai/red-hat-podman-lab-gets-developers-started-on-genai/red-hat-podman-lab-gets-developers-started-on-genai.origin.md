# Red Hat Podman ‘Lab’ Gets Developers Started on GenAI
![Featued image for: Red Hat Podman ‘Lab’ Gets Developers Started on GenAI](https://cdn.thenewstack.io/media/2024/05/051f11ac-podmanai-summit-1024x708.jpg)
Podman,
[Red Hat](https://www.openshift.com/try?utm_content=inline+mention)‘s [desktop tool](https://thenewstack.io/red-hat-podman-container-engine-gets-a-desktop-interface/) for [managing container pods](https://thenewstack.io/check-out-podman-red-hats-daemon-less-docker-alternative/), has been given extended duty, that of providing developers a workspace to build generative AI-based applications.
Unlike many tools for building generative AI tools, this one was built specifically for developers, rather than data scientists, Red Hat asserts. There’s not much support for training models here. Instead, the user is expected to build code around open source models already available via API and packaged as
[microservices](https://thenewstack.io/microservices/).
The
[Podman AI Lab](https://github.com/containers/podman-desktop-extension-ai-lab) provides the ability for a developer to build a generative AI application on their local machine, and, when ready, ship it off to [OpenShift](https://www.openshift.com/try?utm_content=inline+mention)/ [Kubernetes](https://thenewstack.io/kubernetes/) deployments in a set of [containers](https://thenewstack.io/containers/).
Being able to build and test an application on your own laptop “gives you the speed, freedom and security as a developer to start hacking on something immediately,” said
[Michael Clifford](https://www.linkedin.com/in/jamesmichaelclifford/), a Red Hat data scientist in the Office of the CTO, speaking at a session at the Red Hat Summit, held last week in Denver. The AI Lab “makes things really easy to fit into the existing development paradigm that people are already familiar with. And it makes it even easier to get things into the cloud.”
Like
[Docker Desktop](https://thenewstack.io/create-a-development-environment-in-docker-desktop/), [Podman](https://podman.io/) itself provides a way to easily move code from a local development environment (such as VS Code) and into a Kubernetes/OpenShift operating environment. And so for Red Hat, it was a natural platform to launch AI applications.
To make things even easier for the dev, the AI Lab has a recipe catalog of sample applications, including:
- Chatbot
- Text summarizer
- Code generator
- Object detection
- Audio-to-text transcription
These are highly functioning templates, though they were not designed to be used as-is. The source code is available to inspect and customize against. Each recipe is built from an existing model and has an API to interact with. Red Hat is hoping a community grows around these recipes, and that more will be created as time goes on.
The project came about from a customer request to find a way to run LLMs on desktop machines, for development purposes.
One nice AI advancement in the past few years is that you no longer need to train your own model for some specific use. Instead, you can build an application around a general-purpose model, Clifford explained.
Of course, there are popular commercial models such as
[OpenAI](https://thenewstack.io/beyond-chatgpt-exploring-the-openai-platform/), but there are an increasing number of open source models as well (Clifford had counted over 90,000 [ openly-available language models](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) in a recent tally). ![](https://cdn.thenewstack.io/media/2024/05/a7b1a03f-stevan_lemeur-1024x686.jpg)
Stevan Le Meur explained the dev AI workflow and how it fits with Podman.
## Getting Started With Podman AI Lab
The Podman AI Lab interface provides a catalog of open source models to download and includes most of the open source models such as
[GGUF](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md), [Pytorch](https://pytorch.org/) or [Tensorflow](https://www.tensorflow.org/). Users can import their own models as well. ![](https://cdn.thenewstack.io/media/2024/05/ee20814f-download-model.gif)
The models are not included in containers. Instead, they are added through a separate mounting of storage volumes during runtime. This allows you to swap models during runtime.
This can take some work, all this ideation and prototyping, where “I need to find the right model in order to complete my application,” explained Red Hat Principal Product Manager
[Stevan Le Meur](https://www.linkedin.com/in/stevanlemeur/?originalSubdomain=fr), in his own Summit presentation. “What is the model that is going to be the most appropriate for my use case?”
Once a model is chosen, the user can fire up an inference server on their own computer. All the model servers are built on a Linux Universal Base Image (
[UBI](https://www.redhat.com/en/blog/introducing-red-hat-universal-base-image)) base for maximum compatibility. Support for hardware accelerators, such as for [Llama.cpp](https://python.langchain.com/v0.1/docs/integrations/llms/llamacpp/), Nvidia and AMD, are included for many of the servers. ![](https://cdn.thenewstack.io/media/2024/05/a4ba0b90-start-inference-server.gif)
The extension also provides a playground to test different models, allowing developers to try different models on different tasks.
![](https://cdn.thenewstack.io/media/2024/05/8fc8c615-playground.gif)
The recipes show what sort of features could be wrangled from these models. “We try to provide samples that can inspire you about what you can do inside of your own applications,” Le Meur said.
## The Future of AI
The AI Lab is one of a number of extensions for Podman Desktop, which is itself based on the
[OCI-compliant](https://thenewstack.io/open-container-initiative-launches-container-image-format-spec/) Podman container engine. There’s also a copy of [minikube](https://thenewstack.io/install-minikube-on-ubuntu-linux-for-easy-kubernetes-development/) for running K8s locally, a local host of OpenShift, and an extension for making [bootable containers](https://thenewstack.io/red-hat-rethinks-the-linux-distro-for-the-container-age/), among others.
Podman AI, however, fits in nicely with Red Hat’s overall AI strategy, which is to support a wide variety of approaches in building AI applications.
The future of AI “won’t be built by a single vendor, using a single model. It will be open source,”
[said](https://twitter.com/Joab_Jackson/status/1787849813851017720) Red Hat CEO [Matt Hicks](https://www.redhat.com/en/about/company/leadership/matt-hicks), during his keynote at the Summit. *Disclosure: Red Hat paid travel expenses for the writer of this post to attend Red Hat Summit. * [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)