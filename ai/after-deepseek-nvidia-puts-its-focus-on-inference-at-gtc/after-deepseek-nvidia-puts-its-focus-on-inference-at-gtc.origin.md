# After DeepSeek, NVIDIA Puts Its Focus on Inference at GTC
![Featued image for: After DeepSeek, NVIDIA Puts Its Focus on Inference at GTC](https://cdn.thenewstack.io/media/2025/03/7958b117-nvidia_jensen_tshirt-cannon-1024x768.jpeg)
Earlier this year, the news that [DeepSeek](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/) built a highly competitive reasoning model with only minimal training cost sent NVIDIA’s stock into a nosedive as analysts started wondering whether the age of large-scale AI hardware investments was coming to an end. It’s maybe no surprise then that much of this year’s keynote at GTC, NVIDIA’s annual conference, felt like a reaction to this. Jensen Huang, NVIDIA’s CEO and co-founder, announced the usual slew of new software and hardware, including the next generation of its flagship accelerators and an interesting array of desktop-scale AI systems for developers. But at the core of all of this was one message: the next generation of applications will be AI-based — and making that work, especially in the age of reasoning models and agents, will take massive amounts of compute power, which NVIDIA is more than happy to provide.

Indeed, NVIDIA says it expects demand for AI compute to increase by 100x compared with previous estimates. Interestingly, when Huang wanted to demonstrate how much compute power the new reasoning models will need, he chose to compare Meta’s more traditional Llama model to DeepSeek R1. That was surely no coincidence. DeepSeek, as it turns out, used 150 times more compute and generated 20 times more tokens.

“Inference at scale is extreme computing,” Huang said. There is always a trade-off between latency and compute cost to be made here. Either way, Huang argued, the amount of tokens generated will only continue to increase. Training wasn’t completely left out of the keynote, of course, but it was hard to look at a large part of the presentation and not think that at least the first half or so was a reaction to DeepSeek.

Huang also argued that there is a general platform shift happening from hand-coded software built on general-purpose computer storage to machine learning software built on accelerators and GPUs. This also means — and that’s good for NVIDIA — that the future of software development means capital investments. Before, Huang noted, you wrote software and you ran it. Now, “the computer has become a generator of tokens,” he said, and in his view, most enterprises will soon build what he likes to call “AI factories” that will run in parallel to their physical plants.

For developers, NVIDIA announced the DGX Spark and the [DGX Station](https://www.nvidia.com/en-gb/data-center/dgx-station/). The Spark can run in parallel to an existing desktop or laptop and looks somewhat akin to a Mac Studio. The DGX Station, meanwhile, is essentially a full-blown desktop workstation for data scientists with up to 500 teraFLOPS of compute power.

To speed up inferencing and drive down the cost in the data center, NVIDIA announced several new accelerators, including the Blackwell Ultra family and the upcoming Vera Rubin, Rubin Ultra and the Feynman generations of its chips, all of which will boast significant increases in compute performance and memory bandwidth over their respective predecessors.

NVIDIA is clearly going for a somewhat Intel-like tick-tock cadence here with a new generation of chip every year and then an optimized ‘ultra’ version soon after. To put a point on this, Huang joked that he was the “chief destroyer of revenue” at NVIDIA because nobody should be buying the current generation of its Hopper chips anymore.

![](https://cdn.thenewstack.io/media/2025/03/3b604b9b-nvidia-dynamo.jpg)
NVIDIA’s Dynamo inferencing framework.

Another new project the company announced today is [Dynamo](https://nvidianews.nvidia.com/news/nvidia-dynamo-open-source-library-accelerates-and-scales-ai-reasoning-models), an “open source inference software for accelerating and scaling AI reasoning models in AI factories,” as NVIDIA describes it. The idea here is to provide an optimized framework for running reasoning models in the enterprise data center.

“Industries around the world are training AI models to think and learn in different ways, making them more sophisticated over time,” said Huang. “To enable a future of custom reasoning AI, NVIDIA Dynamo helps serve these models at scale, driving cost savings and efficiencies across AI factories.”

And as if to stress its overall focus on inference even more, NVIDIA is also launching its own family of reasoning models, Llama Nemotron, which is optimized for inferencing speed (and boasts a 20% increase in accuracy over the Llama model it’s based upon).

Overall, the reaction to this year’s GTC keynote seemed a bit more muted than to last year’s event. In part, that may be because there just weren’t as many announcements as in previous years, or that they were technically impressive but also a bit esoteric (like its photonics-based networking hardware) — but also because the show felt more reactionary than visionary this time around.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)