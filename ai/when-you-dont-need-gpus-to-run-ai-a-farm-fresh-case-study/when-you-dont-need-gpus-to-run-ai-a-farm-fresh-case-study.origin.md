# When You Don’t Need GPUs to Run AI: A ‘Farm Fresh’ Case Study
![Featued image for: When You Don’t Need GPUs to Run AI: A ‘Farm Fresh’ Case Study](https://cdn.thenewstack.io/media/2024/09/37fe0ae7-vmware-explore-ruby-bradley-1024x768.jpg)
While Nvidia enjoys [unprecedented demand](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/) for GPUs as companies ramp up their AI projects, quiet progress from Intel and other chip makers has reduced the need for GPUs in the first place, allowing at least some workloads to be run without graphical processing units at all.

This was the takeaway of a talk at the [VMware Explore](https://tanzu.vmware.com?utm_content=inline+mention) conference, held last week in Las Vegas.

It was a presentation from the Ontario-based Nature Fresh Farms. The Ontario-based farming operation has 250 acres of greenhouses in the U.S. and Canada, growing 1.6 million plants at any one time through the year: bell peppers, tomatoes, cucumbers and strawberries.

All aspects of the grow cycle is managed by AI. With a handful of servers, all aspects of the plant’s life are monitored and controlled: water, light (both outside and greenhouse-generated), temperature, C02 levels, humidity, and nutrition in the soil.

Number of GPUs used? Zero.

## Nature Fresh Farms
Bradley and his team started with a simple three-node Kubernetes cluster, along with Intel’s [OpenVINO](https://github.com/openvinotoolkit/openvino), an open source framework for running [inference](https://thenewstack.io/5-open-llm-inference-platforms-for-your-next-ai-application/) and other AI jobs.

The system pulls in information not only from greenhouse sensors, but from video and photos, and also from nearby weather stations. This allows the system then to fine-tune operations, such as giving a plant water only when it is sunny, or kicking on artificial light when it is cloudy outside.

“We’ve learned that, just like a human being, if you feed us when we’re hungry, we do better,” [Keith Bradley](https://www.linkedin.com/in/keith-bradley-76105049), vice president of IT and security for [Nature Fresh Farms](https://www.naturefresh.ca/).

Overall, the company collects about 12MB per plant for the entire life of the plant, or 23TB a year for the whole operation.

“We analyze everything and use AI ML to improve each day’s growth to get more optimal results,” Bradley said.

All this data is used not only to optimize the health of the crops but also to give sales projections to the sales team.

“AI helps us do that prediction because there are so many variables you don’t see,” Bradley said.

AI is also used to scan the crates to ensure all the produce is ready for sale, identifying rotten pieces of produce from contaminating the entire box.

Because of AI, the company has seen 2-3% increase in yields over successive years, and increasing the amount of farming that can be done by a small crew.

What’s surprising here is that Nature Fresh is a relatively small operation. “We’re not a multi-billion dollar company that can build a platform for an AI farm,” Bradley said.

Nature Fresh uses [OneAPI](https://www.intel.com/content/www/us/en/developer/tools/oneapi/overview.html) to run workloads on different CPUs, so the IT team doesn’t have to worry about writing specific workloads to specific CPUs or hardware accelerators. The company, along with Kubernetes also uses OneAPI to optimize the workloads, ensuring the live data for real-time decisions gets priority over less-urgent analysis jobs.

Because it is cross-platform, OneAPI gave Nature Fresh the ability to ramp up AI operations without a lot of capital for the latest hardware, Bradley said.

The [OpenVINO site](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.htm) is a good place to learn about what AI jobs could be done by CPUs alone, which turns out to be quite a bit. It includes a robust set of [Jupyter Notebook](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/)-based tutorials for starting a variety of AI jobs, including chatbots, LLMs, text image generation, video analysis, image colorization, noise reduction, gesture detection, object recognition and classification, facial recognition, handwriting-to-text, next word suggestion, medical image analysis, sound classification, gaze detection, defect recognition.

## GPUs or CPUs
GPUs do one thing: matrix math.

The advantage of GPUs is that they can do mathematical operations in parallel on matrices really quickly. Although they were originally designed for rendering graphics, parallel math operations turn out to be really useful for [AI](https://thenewstack.io/ai/) as well.

But GPUs are no longer the only silicon available that can do matrix math. AMD has enhanced matrix capabilities with its latest [EPYC line](https://www.amd.com/en/products/processors/server/epyc.html) processors, and there are a growing number of [hardware accelerators](https://thenewstack.io/developers-can-now-access-the-worlds-fastest-ai-chip/) coming on the market.

In the latest round of Intel Xeon fourth generation (“Sapphire Rapids”) and fifth generation (“Emerald Rapids”) [CPUs](https://www.intel.com/content/www/us/en/products/details/processors/xeon/scalable.html), Intel has included [Advanced Matrix Extensions](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html) (AMX), which puts some matrix math instructions in each core of the CPU itself.

Intel has estimated that AMX can increase Pytorch performance 10x, and works out-of-the-box with TensorFlow and OpenVINO (and VMware’s[ vSphere 8](https://core.vmware.com/resource/whats-new-vsphere-8) virtual machine platform).

Introduced in 2023, AMX introduced the “two-dimensional registries called tiles upon which accelerators can perform operations,” said [Earl Ruby](https://earlruby.org/tag/broadcom/), principal engineer, R&D, Broadcom, who also spoke at this session.

“It is intended as an extensible architecture. So the first accelerator implemented is called the matrix multiply unit, or TMOL, and data comes directly into the tiles same time. The host hops ahead and dispatches the loads for the tiles. TMOL operates on the data the moment it’s ready,” he said.

“At the end of each multiplication round, this tile moves the cache and does some parallel processing that enables the processing of multiple data with a single instruction. And the goal of the software side is to make sure that both the host and the AMX unit are running simultaneously, which maximizes throughput and performance.”

## Demo, Please
With this new hardware and supporting software, there are many AI workloads that, contrary to popular belief, could be run without GPUs, Ruby said

As an example, Ruby ran a demo. He opened the [Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) 7 billion parameter model on a cluster of older “Ice Lake”-third generation of Intel Xeon server processors and compared the speed of that initialization with that of an identical ramp-up on a cluster of AMX-based processors.

The Ice Lake chip performance was sluggish at best.

“This is why people were thinking, ‘Oh, you have to have GPUs because if you want to do this sort of thing, performance is just not that great on CPU,” Ruby said.

In comparison, booting Hugging Face on the Sapphire Lake processor was quite snappy.

“It’s responsive enough to get real work done,” Ruby said.

Ruby then showed an example of fine-tuning the Hugging Face model with about 17,000 finance questions, which the AMX cluster was able to knock out the job in about 3.5 hours.

“So if you’ve got AMX sitting around in a data center and you want to do some fine-tuning overnight, you can do it,” Ruby said. “You don’t need GPUs.”

Ruby also used that model to run three chatbots, all on a single fourth-generation Xeon:

There are still cases where GPUs are essential: Where low latency or immediate responses are required, for fine-tuning huge models, or for creating models from scratch, Ruby said.

But there are an increasing number of cases where the latest CPUs will work just fine: Batch processing ML workloads, light inferencing, or when keeping operating costs down and [power requirements](https://thenewstack.io/how-amazon-matches-power-needs-to-green-energy-sources/) in check, Ruby said.

“You don’t have to use GPUs. CPUs will cover [many] use cases. And if you’re trying to get started, and you don’t want to have to buy a bunch of hardware just to get started, you can get started today with what you’ve got,” Ruby said.

“We don’t need to be instantaneously responding all the time. A three- or four-minute lag doesn’t affect us,” Bradley added. “But once we hit that point, it’s great to know we can start to convert.”

“I don’t know when we will hit that point, but it’s great to know we keep building the platform and use what we have.”

You can enjoy the entire talk [here](https://www.vmware.com/explore/video-library/video/6360760637112).

*Disclosure: Broadcom paid travel/lodging for the reporter to attend this conference.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)