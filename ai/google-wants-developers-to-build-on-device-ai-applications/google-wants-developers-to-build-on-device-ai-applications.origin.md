# Google Wants Developers to Build On-Device AI Applications
![Featued image for: Google Wants Developers to Build On-Device AI Applications](https://cdn.thenewstack.io/media/2024/05/acc90dc8-googleio_2024-1024x682.jpg)
Today’s phones and PCs are equipped with new hardware to directly run AI on devices; and
[at Google I/O this year](https://thenewstack.io/devs-get-ai-pixie-dust-at-google-i-o-but-no-search-updates/), Google encouraged coders to take advantage of it.
The idea is to run large language models on locally stored data, even without an internet connection. The data remains private, does not leave the device, and the approach saves money.
“As a developer, you reduce or eliminate the need to deal with server-side maintenance, capacity, constraints or cost for another entrance,” said
[Sachin Kotwani](https://www.linkedin.com/in/sachinkotwani/), group product manager, during a session at Google I/O.
**The Way It Works**
The ability to develop on-device AI applications is significant progress from the way AI processing is done today.
Neural processors in new phones and PCs make on-device AI possible.
AI already exists on devices, if you haven’t noticed. It runs basic smartphone activities, such as suggesting text messages, improving images, and analyzing power consumption to save battery.
Neural processors in new phones and PCs make on-device AI possible. But running LLMs with a billion or more parameters, such as TinyLlama or Phi-2 on PCs, without any AI accelerators is painfully slow. You can run LLMs only on CPUs with
[Jan.ai](https://jan.ai/) or [GPT4All](https://gpt4all.io/index.html), but it will tax your computer.
Running LLMs rocks on PCs with
[powerful GPUs](https://thenewstack.io/free-gpus-and-ai-chips-are-available-to-run-ai/). But the setup is a chore — you need to download the models, load the neural network environment (such as Nvidia’s CuDNN), install developer tools and compile it.
A new wave of accelerators and GPUs capable of matrix math on-devices makes AI possible on mobile phones.
As a result, most of the AI happens in the cloud on powerful GPUs, which can be as simple as loading a GPT-4 API into a chatbot interface, which then offloads queries to GPUs in OpenAI’s server infrastructure. But these APIs aren’t free, and you must pay to use OpenAI’s infrastructure.
A new wave of accelerators and GPUs capable of matrix math on devices makes AI possible on mobile phones.
Google’s new Pixel 8A phone has an Edge TPU (Tensor processing unit) for AI, and Intel and AMD have neural processing units on PCs. The on-device AI can also be coupled with cloud-based AI resources.
## Dev Tools
Development tools to run LLMs on devices are becoming available from chip makers that include AMD, Intel and Nvidia.
Most recently, Google talked about development kits, APIs, and other tools that leverage its own
[Gemini](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/) Nano LLM for mobile devices. This LLM is multimodal, which means developers can build speech, image, video or chatbot applications around it.
“Gemini Nano is Android’s recommended path to production.”
– Thomas Ezan, Google
Google reps said that Gemini Nano is the most capable model for on-device AI, and it also integrates well into Android apps.
“Gemini Nano is Android’s recommended path to production,” said
[Thomas Ezan](https://www.linkedin.com/in/tezan/), senior developer relations engineer at Google at I/O.
For those who prefer not to get stuck in Google’s proprietary AI development environment, Google will support open source LLMs between two to three billion parameters.
“If you want to run generic inference on devices, open large language models have also grown in popularity in the past year, although they are not a good fit for production due to performance and memory challenges,” Ezan said.
Those include Falcon 1B (1.3 billion parameters), Flan-T5 (2.7 billion parameters), StableLM 3B (2.8 billion parameters) and Llama 2B (2.5 billion parameters). Google will also support a 7-billion parameter model of its open source Gemma LLM.
## Google’s Own Tools
Developers can integrate Nano AI into apps and development via the Edge AI SDK. The SDK provides high-level APIs, pipelines, model inference and hardware hooks to run AI models efficiently.
Mobile devices are constrained in computation power, bandwidth, and memory. Developers can fine-tune models by accessing a system service called AICore, which is integrated in Android 14 running on eligible devices such as Pixel 8A and Samsung’s S24.
Developers can optimize models for mobile devices using quantization to reduce model size and processing requirements.
LoRA is considered an important building block to fine-tuning AI to devices and applications.
“The context window will also likely be smaller and the model will be less generalized… this means that fine-tuning is critical in order to get production quality,” said
[Terence Zhang](https://www.linkedin.com/in/zhehaozhang1997/), a developer relations engineer at Google.
AICore also includes a fine-tuning layer called low-rank adaptation, LoRA, which allows app developers to customize a model to perform specific tasks. LoRA is considered an important building block to fine-tuning AI to devices and applications.
“Apps can train their own specialized LoRA fine-tuning blocks to optimize the performance of the Gemini Nano model,” said
[Miao Wang](https://www.linkedin.com/in/miao-wang-108b072b/), software engineer at Google.
## Supports Open Source LLMs
MediaPipe is a critical API that allows developers to create on-device AI applications using multiple open source LLMs, which include Falcon and Gemma.
Developers will rely on the MediaPipe API to write AI web apps for Android and iOS devices.
The MediaPipe API provides the pre-optimized models, and developers have to bring the weights to run on-device applications. It supports vision, text and audio applications. Some LLMs excel at specific tasks, and the API provides the flexibility for developers to select their models.
Developers will rely on the MediaPipe API to write AI web apps for Android and iOS devices. Chrome 126, which is
[in beta](https://developer.chrome.com/blog/chrome-126-beta), integrates support for low-code APIs that connect web apps to the Nano and open source LLMs.
“This is all running fully locally in the browser, and it’s fast. And that’s because it’s accelerated on the computer’s GPU through
[WebGPU](https://thenewstack.io/google-talks-web-platform-os-integration-webgpu-and-more/). And that makes it fast enough to build pretty compelling, fully local web applications,” said [Cormac Brick](https://www.linkedin.com/in/cbrick/), principal software engineer of core machine learning, at Google I/O.
## TensorFlow Lite
Google is also using the TensorFlow Lite development environment, which is a lightweight version of the TensorFlow machine learning framework. TFLite also includes a kit to convert TensorFlow models into more compact versions that can run on-device.
“You can find off-the-shelf models or train models in the framework of your choice,” Brick said. “It converts your models to TensorFlow Lite with a single step. And then you can run them all on runtime bundles with your app across Android, web and iOS.”
Chip maker Qualcomm last week said that developers will be able to port their LLMs to smartphones using its latest chips.
## Challenges
App developers are in a gold rush to take advantage of every last ounce of processing that they can to make their apps more efficient.
New generations of devices will have more AI horsepower, which will boost on-device AI brains.
Another challenge is to match apps to the right AI chips. New generations of devices will have more AI horsepower, which will boost on-device AI brains.
Dell has introduced new PCs with Intel’s NPU, but on-device AI will really take off once developers discover relevant apps, said
[Zach Noskey](https://www.linkedin.com/in/zach-noskey-86660951/), director of product management at Dell.
Developer participation in tools such as Intel’s
[OpenVino](https://thenewstack.io/intel-openvino-brings-ai-inferencing-to-the-desktop/) is important to drive the industry. Vendors also need to work closely on application readiness with developers, who may not know where to start.
For example, OpenVino provides an Intel NPU plugin for Gimp to support Stability Diffusion image-generation prompts.
“It is about continuing to enable that in the community — it’s kind of going a little bit slower, like in years past with CPU and GPU utilization of applications,” Noskey said.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)