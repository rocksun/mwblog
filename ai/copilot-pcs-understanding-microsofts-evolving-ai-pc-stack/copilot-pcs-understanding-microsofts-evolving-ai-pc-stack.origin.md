# Copilot+ PCs: Understanding Microsoft’s Evolving AI PC Stack
![Featued image for: Copilot+ PCs: Understanding Microsoft’s Evolving AI PC Stack](https://cdn.thenewstack.io/media/2024/05/4713ebc2-microsoftpluspc-1024x618.jpg)
Data centers are bursting at the seams with AI workloads, but PCs are now in the loop to take some stress off the mega GPU installations.
“AI PC” may be a buzzword, but it also ably describes the new types of PCs hitting the market in the coming years.
“Even the PC computing stack is going to be revolutionized.”
– Nvidia CEO Jensen Huang
PCs – previously relegated to running executables for logical tasks — now have a little AI brain inside that can reason and make decisions, answer questions, create programs, or improve the user experience. Developers will write software so that these brains spit out the best answers.
Software is getting bigger and better for users to load
[large language models](https://thenewstack.io/what-is-a-large-language-model/) on PCs and run AI without an Internet connection.
“Even the PC computing stack is going to be revolutionized,” Nvidia CEO Jensen Huang said in a financial earnings call this month.
PCs already have
[AI chips](https://thenewstack.io/gpu-rich-gpu-poor-whats-new-in-the-ai-chip-boom/), but they are mostly deadweights, as they don’t meet the minimum requirements set by Microsoft’s qualifications for AI PCs. LLMs were not fine-tuned to take advantage of the low power consumption of AI PCs, but that is changing.
“AI is not a chip problem… but it’s a systems problem,” Jensen said.
**Microsoft’s Concept of AI PCs**
Microsoft announced the concept of Copilot+ PCs at its
[Build conference](https://thenewstack.io/microsoft-copilot-for-azure-managing-cloud-ops-through-chat/).
These PCs — in theory — are an early instance of hardware-software co-design to run AI under the hood of Windows PCs.
The software company is setting the tone on the hardware it wants to see in AI PCs, which includes specialized chips that deliver a minimum of 45 TOPS (trillions of operations per second).
“What Win32 was to graphical user interface, we believe the Windows Copilot Runtime will be for AI.”
– Satya Nadella, Microsoft CEO
The first qualified AI PCs are Copilot+ PCs with Qualcomm chips, which were announced on the sidelines of the Build Developer Conference.
“We are introducing the Windows Copilot Runtime to make Windows the best platform for you to be able to build your AI applications. What Win32 was to graphical user interface, we believe the Windows Copilot Runtime will be for AI,” Nadella said.
Microsoft already has AI in Windows with the Copilot feature — queries entered in PCs are redirected to data centers, which output the answer to desktops.
The company sees an opportunity to offload low-priority tasks like that to PCs, which can save bandwidth and free up GPUs in their data centers. The Copilot feature in Bing relies heavily on a custom version of GPT-4 to answer questions.
The PCs include a Windows Copilot Library, which has localized APIs that help connect applications to the
[Copilot stack](https://thenewstack.io/microsoft-one-ups-google-with-copilot-stack-for-developers/). Microsoft developed the ONNX runtime, an inference runtime, which is popular with the major chip makers.
To be clear, Windows PCs with Nvidia’s RTX GPUs can also run local AI — mainly for chatbots and image generation — by manually loading Nvidia’s cuDNN neural network environment, loading PyTorch, and installing Python. But that’s a painful process because the stack has to be reloaded with every restart — which can take 10 minutes or more.
Microsoft is automating that entire process with system libraries and drivers, which containerizes the AI workloads. Microsoft already has a machine-learning driver called DirectML, which is more like a DirectX for on-board machine learning.
**Local Copilot**
Microsoft also understands that AI has evolved to expand to a range of large language models, which score differently on math, coding and reasoning. Some may want to use other
[open source models](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) and not rely on Microsoft’s stack.
Microsoft introduced a library of large language models that developers can install and load on Windows 11 PCs.
“We have 40-plus models available out of the box… which we specifically designed to run locally on your inputs on Copilot+ PCs, bringing that lightning-fast local inference to the device,” Nadella said.
Microsoft’s Copilot+ integrates the RAG (retrieval augmented generation) technique to provide more accurate answers.
The self-service model includes Phi Silica, a 3.8-billion parameter version of Microsoft’s open source Phi-3-mini LLM, which “we specifically designed to run locally on your inputs on Copilot+ PCs,” Nadella said. The on-PC Phi Silica LLM allows Microsoft to offload some of the Copilot prompting from GPUs in the cloud.
Microsoft’s Copilot+ integrates the RAG (
[retrieval augmented generation](https://thenewstack.io/retrieval-augmented-generation-for-llms/)) technique to provide more accurate answers. In this case, the responses also rely on other data fed from external sources, such as information on PCs. That helps provide more accurate answers and not completely rely on LLMs that are based on information scraped from the internet months ago.
Microsoft said it would provide tools to feed various inputs into its AI stack, ensuring that developers can work with images, voice, video, and text when writing AI apps that can be processed on-board PCs. Microsoft has made provisions for
[vector embeddings](https://thenewstack.io/comparing-different-vector-embeddings/) to ensure different types of data can be easily correlated and integrated into AI features.
The Windows App SDK 1.6 Experimental 2 has many APIs to run chatbots, do calculations, or solve problems. These can be connected to applications and integrated into the user interface.
At Build, Microsoft also announced native Windows support for PyTorch — a necessity to run LLMs made using that framework. Now users don’t have to go through the grueling process of installing PyTorch every time they want to load an LLM on PCs.
“Native PyTorch support means thousands of OSS models will just work out of the box on Windows, making it easy for you to get started. In fact, with WebNN, web developers finally have a web-native machine learning framework that gives them direct access to both GPUs and NPUs,” Nadella said.
**Device and Chip Makers**
AI on devices can only be as fast as the hardware, and these LLMs are designed for the NPUs on the device. Google at its IO trade show
[shared details](https://thenewstack.io/google-wants-developers-to-build-on-device-ai-applications/) on how developers can write AI applications that run locally on smartphones.
Qualcomm is the first to market for CoPilot+ with Snapdragon Elite chips.
Last year, Intel released its
[latest generation x86 chip](https://thenewstack.io/intels-generational-on-chip-change-apx-will-make-all-the-apps-faster/) called Meteor Lake, which has an NPU that peaks at 10 TOPS. Unfortunately, it doesn’t qualify for the Windows minimum of 45 TOPS to be called an AI PC for Windows, also called CoPilot+ PCs.
Qualcomm is the first to market for CoPilot+ with Snapdragon Elite chips, which have NPUs topping 45 TOPS. All major PC makers — including Dell, HP, Asus, and Lenovo — have announced PCs with AI chips.
Qualcomm has also introduced its own AI Hub as a resource for developer tools. It provides an IDE that can be installed through some typical command line prompts and also provides an API token for app integration.
Intel is hurrying up its next-gen PC chip called Lunar Lake.
Developers will be able to download LLMs to test out. The API token typically means developers will be able to integrate LLMs into third-party applications, as outlined by Microsoft in its plans for bringing Copilot into apps.
Intel is hurrying up its next-gen PC chip called Lunar Lake, which the company claims will meet the minimum requirements of AI PCs with a 45 TOPS NPU, and possibly go beyond 100 TOPS with GPUs. Lunar Lake chips are expected to come in a couple of months.
Intel also has its own development environment called OneAPI, which is complicated to use. Intel provided an example of loading Stability Diffusion AI for image generation in GIMP, but it is a complicated process that involves installing OpenVino, running command-line installs and further fine-tuning.
Intel also provides Jupyter notebooks to try out AI on its various chips via its Tiber Developer Cloud service, which could be a safer bet. But cloud versions of the AI PC chips aren’t yet available.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)