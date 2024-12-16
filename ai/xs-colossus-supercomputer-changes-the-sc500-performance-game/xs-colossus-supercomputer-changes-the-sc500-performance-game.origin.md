# X’s Colossus Supercomputer Changes the SC500 Performance Game
![Featued image for: X’s Colossus Supercomputer Changes the SC500 Performance Game](https://cdn.thenewstack.io/media/2024/11/06b7cb90-xai-1024x683.png)
For computing hardliners, performance is non-negotiable — a snappy response on an [AI service](https://thenewstack.io/ai/) is as important as the speed of the latest GPUs in their home PCs.

Mind-boggling AI supercomputers like X’s Colossus supercomputer are replacing conventional systems, and these systems are indirectly impacting the overall computing experience of users.

Hardware experts are now tuning into the new computing reality. Old ways of measuring system performance are going out the window as new AI supercomputers replace conventional systems.

This week, the Top500 organization [released a list](https://top500.org/) of the world’s [fastest supercomputers](https://thenewstack.io/sc500-microsoft-now-has-the-third-fastest-computer-in-the-world/). The U.S. Department of Energy hosts three of the [fastest supercomputers in the world](https://thenewstack.io/top500-chinas-supercomputing-silence-aggravates-tech-cold-war-with-u-s/), according to the list.

For more than 30 years, the Top500 list has served as a document of record showing advances in conventional computer speed. AI supercomputers are upending that trend and could make the Top500 list a relic of the past. Top500 typically releases lists twice a year.

The latest Top500 list has a new leader with El Capitan at Lawrence Livermore, achieving 1.74 exaflops of performance, followed by the formerly top-ranked 1.35-petaflop Frontier at ORNL, and then the 1.01 exaflops Aurora at Argonne.

## Out With the Old
Conventional computing and AI are fundamentally different ways of processing data, and their performances are measured differently. They cannot both be included in the same list.

Hyperscalers are making way for AI servers by dismantling old-school data centers and non-AI servers. There is less interest in conventional systems used for databases, ERP, and web serving.

[X.AI](https://x.ai/about) has just finished installing Colossus, which is the largest AI supercomputer in the world. Colossus was used to train Grok 3. It has more GPUs than any known conventional supercomputer in the world.
X hasn’t published the system performance of Colossus, but it could easily make the top 10 list if benchmarked as a conventional computer.

Hyperscalers Microsoft, Google, Facebook, Amazon, and Oracle are spending billions on AI supercomputers with thousands of GPUs.

## Architectural Changes
CPUs defined conventional computer performance for decades. Scientists have said that Moore’s Law is dead, and with it, CPU scaling is coming to a standstill.

GPUs are the way to move performance forward. GPUs are also the focal point in AI systems, with CPUs acting more as schedulers.

GPU performance will only increase as Nvidia and AMD release new GPU architectures yearly.

Nvidia next year is shipping Blackwell GPUs to replace the Hopper H100 GPUs that went into Colossus. Blackwell delivers approximately twice the performance compared to H100, according to benchmarks published by the independent organization MLPerf.

Hyperscalers are deploying new servers designed for GPUs. Oracle’s upcoming Colossus-killer will have up to 131,072 Nvidia GPUs, which is “more than three times as many GPUs as the Frontier supercomputer and more than six times that of other hyperscalers,” according to the company.

The AI supercomputers pack more memory and storage and prioritize faster communication between components.

## Technical Differences
Conventional computing and AI supercomputers compute differently. The fundamental difference is in the precision of the response to a query. A higher bit generally represents more precision in computing.

Conventional systems compute accurately and deliver precise answers. That requires using the most 64-bit or 32-bit computing resources at one time to generate the best possible answer. Systems run hotter with 64-bit or 32-bit computing.

Top500 runs a 64-bit benchmark to measure how long it takes for a processor to answer a query. High-precision computing is essential for financial forecasting and scientific computing, which rely heavily on data accuracy.

AI is different. The computation style is more comparable to guesswork, with answer accuracy improving over time. These systems prioritize computing efficiency over numerical precision.

The Top500 organizers are now trying to find ways to rank the fastest AI servers.

AI computing goes down to 4-bit to 16-bit data types, which are less accurate than 64-bit. AI supercomputers present probable answers to users, and GPUs work in parallel to improve accuracy based on queries and data trends. As the system learns more, the answers become more accurate.

Forks of open source generative AI models Llama and Gemma have been quantized down to 8-bit and 4-bit to work with mobile devices, which are limited in speed and memory capacity.

AI benchmarks also have to factor in the quality of the response and relevance of the model, which complicates hardware measurements. A quantized 4-bit model will be faster but much less accurate than an 8-bit quantized AI model.

Independent organization [MLPerf has set up rules](https://thenewstack.io/nvidia-h200-gpus-crush-mlperfs-llm-inferencing-benchmark/) to measure AI speed based on the task (training or inference), the generative AI model, quantization, and other specifications.

Chip makers, including Nvidia, Google, Intel, and AMD, release AI benchmarks via MLPerf.

## In With the New
Top500 organizer Erich Strohmaier last year surmised that conventional supercomputing won’t reach 10 exaflops by 2030. Intel, in 2021, [declared](https://www.intel.com/content/www/us/en/newsroom/news/innovation-cloud-edge-news.html#gs.0x7ak1)) conventional computing speed would reach a zettaflop by 2027.

Microsoft’s 561-petaflop Eagle supercomputer is ranked fourth on Top500, and it is the only commercial cloud system in the top 10. The Azure system combines Ubuntu Linux with Nvidia’s H100 GPUs and Intel’s 4th Gen Xeon processors.

Cloud providers aren’t submitting benchmarks to Top500 as it would cost time and money. Doing so would make the systems inaccessible to customers for days or weeks, which is not practical with AI demand soaring.

Some AI hardware is inaccessible as components aren’t available off the shelf. Google is using homegrown TPUs — which aren’t available off the shelf — to run its AI workloads. Similarly, AWS’s Trainium AI chip is available only through its cloud service.

The Top500 organizers are now trying to find ways to rank the fastest AI servers.

The organization has a benchmark called HPL-MxP that covers mixed-precision measurements. It factors in 4-bit to 16-bit data types to measure the AI speed of a supercomputer. HPL-MxP will be relevant to scientists merging AI with conventional workloads.

Experts are also gathering this week at the SC2024 supercomputing conference to find ways to measure AI speed. X.AI’s Colossus supercomputer will be a big part of the conversation.

Nvidia has classified Colossus as the world’s largest accelerated system.

The supercomputer was built in record time, “going from equipment delivery to training in just 19 days and full-scale production within 122 days,” said Dion Harris, director for accelerated computing at Nvidia.

Colossus’ performance numbers aren’t available, but Harris said, “X has been thrilled with the system performance.”

“This deployment sets a new standard for AI at scale,” Harris said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)