# PyTorch, Docker and AI Openness Highlight AI_dev Europe
![Featued image for: PyTorch, Docker and AI Openness Highlight AI_dev Europe](https://cdn.thenewstack.io/media/2024/06/d5cec598-nahrizul-kadri-oasf0qmrwla-unsplash-1024x578.jpg)
PARIS — The cofounder of [PyTorch](https://thenewstack.io/pytorch-takes-ai-ml-back-to-its-research-open-source-roots/) told open source AI developers last week that the project had considered closer integration between the AI framework and languages including [Rust](https://thenewstack.io/rust-growing-fastest-but-javascript-reigns-supreme/) and [JavaScript](https://thenewstack.io/top-10-javascript-libraries-to-use-in-2024/) but ultimately decided against it.

[Soumith Chintala](https://www.linkedin.com/in/soumith/) was speaking during a fireside chat at the [Linux Foundation’s AI dev conference](https://events.linuxfoundation.org/ai-dev-europe/) here, during which he outlined the ethos behind the framework. “PyTorch is like your typical hacker, who will take any shortcut to get good performance for users. We’re very pragmatic.”
Asked about the future roadmap for PyTorch, he said, “Tools have to evolve, but they don’t have to evolve very frequently.”

When it comes to the AI space, he said, “I think we’re seeing new tooling every six to seven years or so.” Therefore, “I don’t even expect PyTorch to even have a need for thinking about 2.0 anytime soon. But we keep looking and the landscape keeps changing.”

Following the launch of [ChatGPT](https://thenewstack.io/how-ray-a-distributed-ai-framework-helps-power-chatgpt/), he said, transformers were overwhelmingly the dominant method for doing AI and maybe “that is something that we need to think about carefully. But largely, we’re still pretty happy.”

## Integration With Other Languages?
One thing clearly not on the agenda is closer integration with languages other than Python.

In response to an audience question, “Are we going to have PyTorch for Rust or JavaScript?” His answer was “PyTorch has a ‘Py’ in it, so, officially, no.”

Chintala added the team had thought about it. But he continued, the problem always comes with compilers. “You have to parse the frontend code and writing a frontend that consumes the user code for various languages was a big lift.

“So from the prioritization and research perspective, we decided no, but we actually have no animosity to Rust or JavaScript.”

## Docker and WebGPU
Elsewhere at the event, [Docker](https://www.docker.com/?utm_content=inline+mention) announced that it was previewing support for [WebGPU](https://thenewstack.io/google-talks-web-platform-os-integration-webgpu-and-more/) in Docker, removing the need to build [Docker images](https://thenewstack.io/the-case-for-environment-specific-docker-images/) specifically for each GPU vendor’s proprietary drivers.

Docker’s UK-based CTO [Justin Cormack](https://www.linkedin.com/in/justincormack/?originalSubdomain=uk) said that when the company was launched, the developer hardware landscape was “pretty uniform. You could almost ship your laptop to production.”

But the AI explosion and its reliance on [GPU](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/)s have changed this, he continued. “We’re seeing a huge spread of different kinds of accelerators, on developer machines, on edge machines, in production,” Cormack added. “There’s a huge, huge variety of stuff.”

That made it “a really fun time for hardware” he said, but inevitably developers “are asking us about GPU usage.” The ideal was a portable abstraction with Docker that is available everywhere. And the answer, he said, came in the shape of WebGPU, the [World Wide Web Consortium (W3C)](https://www.w3.org/)-backed API for performing operations on a GPU.

“WebGPU came across as something that already exists, is already shipping in most of the browsers across all consumer GPUs and mobile, and it has an ecosystem.” But, he added, it doesn’t just work in the browser as it has standard definitions that can be used portably, and as a high-performance modern stack, in comparison to [WebGL](https://get.webgl.org/).

Cormack said it was shipping WebGPU support as a preview in [Docker Desktop](https://thenewstack.io/create-a-development-environment-in-docker-desktop/) but would also be making it available for Docker Engine in the future, and for other platforms.

“What we’re working on is really providing container images that have multiple backends baked in,” Cormack told The New Stack.

In the first instance, this should make life easier for developers who might have little choice over the GPU in their development machine. But ultimately it could smooth things when applications go into production.

“The next step for us is showing what that path looks like,” he said. “So you’ve got these pre-baked models that both run locally and run in production.”

## Increased Access and Openness
Cormack said the company is also looking at how it works with [Llama](https://thenewstack.io/coding-test-for-llama-3-implementing-json-persistence/) models: “We’re really excited about working together with these broader communities and bringing more access to GPUs to everyone doing the development and working on the edge in different environments and improving affordability and ease of use for the ecosystem.”

While the conference highlighted the potential of open source AI, both in increasing access to AI technology and bringing transparency to a market that could be dominated by big tech, it also addressed concern about “[open washing.](https://thenewstack.io/calls-to-ban-open-source-are-misguided-and-dangerous/)”

Linux Foundation AI and Data Foundation Executive Director [Ibrahim Haddad](https://www.linkedin.com/in/ibrahimhaddad/) debuted a tool to allow AI model makers – and end users – to assess just how open a model really is.

The [isitopen.AI](https://isitopen.ai/) site is based on the [Model Openness Framework](https://arxiv.org/abs/2403.13784?ref=thestack.technology) developed by the foundation. This breaks down models into 17 different components, spanning code, tooling, data and documentation.

Models are classified into three classes.

**Class I – Open Science**covers the full gamut of components, with all artifacts released, including training datasets. That makes the model fully reproducible.**Class II – Open Tooling**covers the full suite of code, plus key datasets.- The bottom rung,
**Class III – Open Model**, means the core of the model, including architecture, parameters and basic documentation, is released under open licenses.
Haddad said the complexity of AI compared to traditional code meant a binary approach to openness was difficult to maintain, but it was better to have a sliding scale of transparency than none at all.

More practically, the tool and framework meant developers and companies looking to work with models would know exactly how a given model meshed with their own frameworks or internal processes. It also means model developers would be clearer on their own status – and not using inappropriate licenses. Notably, none of the models analyzed so far have achieved anything higher than Class III status.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)