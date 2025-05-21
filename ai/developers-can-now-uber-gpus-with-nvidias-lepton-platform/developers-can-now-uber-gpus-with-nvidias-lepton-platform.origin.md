# Developers Can Now ‘Uber’ GPUs With NVIDIA’s Lepton Platform
![Featued image for: Developers Can Now ‘Uber’ GPUs With NVIDIA’s Lepton Platform](https://cdn.thenewstack.io/media/2025/04/b4c49fb4-nvidia12-1024x576.jpg)
Do you desperately need an NVIDIA GPU? Don’t stress, you’ll soon be able to order one online.

NVIDIA has [announced](https://nvidianews.nvidia.com/news/nvidia-announces-dgx-cloud-lepton-to-connect-developers-to-nvidias-global-compute-ecosystem) a one-stop shop called [DGX Cloud Lepton](https://www.nvidia.com/en-gb/data-center/dgx-cloud-lepton/), which will allow developers to rent NVIDIA GPUs scattered worldwide across host providers.

Developers can log into Lepton, specify their AI task, and rent a relevant GPU. Using the Uber analogy, GPUs will come to developers who don’t have time to go and find one.

“Similar to modern ride-sharing apps that connect riders to drivers, DGX Cloud Lepton provides a modern marketplace that connects developers to GPU compute and not just locally,” said [Alexis Black Bjorlin](https://www.linkedin.com/in/alexisbjorlin/), vice president of NVIDIA’s DGX Cloud, in a press briefing.

GPU availability isn’t a grave problem, but searching for the right service across dozens of cloud services or independent facilities can be a headache.

A host of NVIDIA GPUs will be available to order — including Blackwell, its latest GPU. Older GPUs, including Hopper (on which ChatGPT runs) and possibly Ampere, will also be available.

The GPUs will depend on the job. If users need large-scale training for models, it may be Blackwell. If users need inferencing, a Hopper or Ampere may be assigned. If users need low latency, then a GPU in a nearby region will be assigned.

## The Problem: More GPU Suppliers
NVIDIA GPUs were in short supply up until last year. Microsoft, OpenAI, Amazon and Meta gobbled up most of the supplies. Even Apple was unable to acquire parts, which put them years behind in AI, [according](https://www.bloomberg.com/news/features/2025-05-18/how-apple-intelligence-and-siri-ai-went-so-wrong) to a Bloomberg story this week.

Cloud providers [initially](https://www.hpcwire.com/2023/10/16/annual-gpu-upgrades-nvidias-plan-for-faster-chips/) charged a premium for access to NVIDIA GPUs. These were only available to large customers.

But as supply normalized, a bunch of independent GPU providers popped up to provide AI computing at cheaper prices. Most of these had previously mined cryptocurrency, but pivoted their hardware to AI as that market took off. Companies like Crusoe Energy, which sold its bitcoin mining business [in March](https://www.cnbc.com/2025/03/25/crusoe-energy-sells-bitcoin-mining-unit-to-nydig-to-focus-on-ai.html), acquired new GPUs and started renting them out as AI infrastructure. Another example is Voltage Park, which was founded by a crypto executive but now offers one-time H100 GPUs at $1.99 per hour.

NVIDIA’s Black Bjorlin acknowledged GPU capacity had grown, adding “finding and efficiently utilizing AI infrastructure in the right regions at high performance can be complex.”

## NVIDIA’s Uber-Like Idea
Delivery of GPUs from Lepton will be from lesser known GPU providers — including CoreWeave, Crusoe, Lambda, Foxconn, and others. It’s not yet clear if users will be able to select the provider.

Lepton does not include the top-4 cloud providers, but users will be able “to bring their compute and the platforms that they currently use, so it’s certainly an option on this platform,” Bjorlin said.

Reading between the lines, NVIDIA may be creating its own cloud service and will compete with the likes of Amazon, Google and Microsoft, which also rent out GPUs.

Bjorlin also indicated that Lepton will be hybrid cloud-friendly, meaning that developers may be able to connect their data or AI workloads to rental GPUs at smaller providers.

## Cheaper Alternatives
Pricing for Lepton wasn’t available, but the service requires some NVIDIA software and tooling, which isn’t cheap.

To avoid the NVIDIA premium, it may be cheaper to rent GPUs directly from smaller service providers that are already a part of Lepton.

A fully loaded NVIDIA H200 GPU [from](https://crusoe.ai/cloud/pricing/) Crusoe Energy, for a single instance over a six-month term, will set users back about $120,000. A slower A100 will be about half the price.

The [price](https://www.coreweave.com/pricing) of the H200 from CoreWeave is about $50 per hour.

Lepton’s strength is in its software backend, which takes care of the [NVIDIA software](https://thenewstack.io/nvidia-wants-to-rewrite-the-software-development-stack/) and [hardware development stack](https://thenewstack.io/nvidias-hardware-roadmap-and-its-impact-on-developers/). Developers can take their programs directly to GPUs and cut off the development and microservices complexity in the middle.

Alternatively, it may be better to get hardware that runs locally — since the processing requirements for AI are also shrinking.

NVIDIA will soon start shipping [DGX Spark](https://thenewstack.io/after-deepseek-nvidia-puts-its-focus-on-inference-at-gtc/) — which delivers one petaflop of performance and can run inference on desktops. The hardware was described as “your own AI cloud sitting right next to you and it’s always on, always waiting for you,” by NVIDIA CEO Jensen Huang during a keynote.

## How Lepton Will Work
Developers first need to sign up as an NVIDIA developer and create a cloud server. After that, developers can [apply](https://developer.nvidia.com/dgx-cloud/get-lepton) for access to the service.

My application for the service is currently under consideration. NVIDIA seems choosy in selecting users, limiting approvals to users who can properly exploit its GPUs and with money to spend. My applications for beta AI services have never been approved — nevertheless, developers should give it a shot.

If you get access, you can adopt LLMs or AI applications from NVIDIA’s Build [website](https://build.nvidia.com/) and deploy them to Lepton. It is possible to be granular and fine-tune the task for deployment to computing nodes.

Users can select the type of job and the GPU, establish the container with the development environment, and dispatch the AI job to GPUs. A training job will go to high-end GPUs, while inference will be sent to lower-end GPUs.

Developers can configure the GPU and manage multiple machines within the Lepton interface. That includes selecting a container image, selecting the instance type (CPU or GPU), and establishing the variables. NVIDIA provides templates for MPI and Torchrun to get started.

Users can also run [Jupyter notebooks](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/) within containers. The pod can be accessed via SSH, browser, or through other tools. Lepton organizes and manages the nodes depending on the job and type of GPU.

Developers can bring their own hardware to integrate into Lepton for more self-managed nodes. But the [hefty list](https://docs.nvidia.com/dgx-cloud/lepton/guides/nodes/bring-your-own-compute/requirements/) of requirements includes 640GB of storage per GPU (recommended: a 20TB NVMe SSD), high-end x86 server CPUs, Ubuntu 22.04 LTS, and [CUDA](https://thenewstack.io/nvidia-making-radical-changes-to-cuda-after-nearly-20-years/) 12.4.1 or beyond.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)