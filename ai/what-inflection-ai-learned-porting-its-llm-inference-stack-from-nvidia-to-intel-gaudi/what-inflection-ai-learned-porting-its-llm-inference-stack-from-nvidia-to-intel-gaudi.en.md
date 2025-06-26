At Inflection AI, we recently made a major shift in our infrastructure: we ported our LLM inference stack from NVIDIA GPUs to Intel’s Gaudi accelerators. The reasons behind the shift are ones that nearly every enterprise is also facing today: GPU supply shortages, rising prices, and inflexible long-term leases meant building on NVIDIA hardware could limit our ability — and our customers’ ability — to scale.

It was clear we needed a more flexible stack. When assessing the options, Intel rose to the top of the list as it already has the largest footprint for enterprise hardware globally. This meant if we could achieve performance parity on Intel hardware, enterprises could leverage their existing data center investments for their AI deployments, rather than vie for access to NVIDIA GPUs.

The journey wasn’t easy, taking several weeks and many kernel rewrites, but ultimately, we [managed to adapt and optimize our custom](https://thenewstack.io/how-to-optimize-customer-identity-and-access-management/) inference runtime to achieve near-performance parity. In solving those problems, we learned several lessons that we believe are widely applicable to anyone building more flexible, efficient inference systems.

## **Solving Unsupported Ops**

Mapping AI architectures to the underlying accelerator hardware is key to achieving efficient and scalable AI workloads. When moving to Gaudi, we found that the full range of PyTorch operations (which today exceeds 2,000 operations) wasn’t fully supported by SynapseAI, the backend that powers Intel’s accelerator stack. In particular, operations like Pythonic (numpy-like) tensor slicing and more obscure ones, such as torch.triu\_indices, were not supported.

In some cases, unsupported ops caused segfaults. In others, PyTorch fell back to CPU execution, which introduced [large performance penalties due to data](https://thenewstack.io/processing-large-data-sets-in-fine-grained-parallel-streams-with-sql/) transfers between CPU and HPU.

To solve these challenges, we rewrote unsupported or problematic ops, which alone yielded a nearly 15x performance improvement and eliminated segfaults.

## **Eager vs. Lazy Execution**

The Lazy loading vs. Eager loading dichotomy is found in many areas of computing, and many AI [software and hardware stacks attempt to support](https://thenewstack.io/nvidia-wants-more-programming-languages-to-support-cuda/) both. For simplicity’s sake, we first tried to run our model in PyTorch’s default Eager mode. While the outputs were accurate, the latency was significantly higher than that of NVIDIA due to the “one-by-one” operation execution.

However, switching to Gaudi’s default Lazy mode resulted in even worse performance, with execution twice as slow. Dynamic operations, [such as data-dependent branching and variable](https://thenewstack.io/transparency-from-behind-the-generative-ai-curtain/) input shapes, were breaking the graph, introducing host overhead from reaccumulating operations and generating new graphs.

Thankfully, we saw a path forward to solve the issues we encountered in Lazy mode. [Addressing this problem involved identifying and removing every dynamic operation](https://thenewstack.io/5-steps-to-identify-and-address-incident-response-gaps/) causing graph breaks in our forward pass, and then integrating HPU graphs. HPU graphs are similar to CUDA graphs, as they enable the recording and replaying of computation graphs directly on the HPU without involving the host. Since these abstractions operate on fixed shapes of input tensors, we used a bucketing strategy with padding for variable input tensor shapes to match the shapes of our cached HPU graphs.

Through these optimizations, we [achieved a 4x speedup that rivaled our model’s performance](https://thenewstack.io/5-tips-to-achieve-performance-engineering-at-scale/) on NVIDIA hardware.

## **Perfecting With Profilers**

While these model optimizations provided dramatic improvements, we hoped to achieve more. To fully optimize performance, we utilized Habana’s torch-based profiler stack to gain visibility into how the Gaudi hardware was being utilized across its two main compute engines: MME for GEMM operations and TPC for element-wise operations. To fully utilize the hardware, both needed to stay busy.

Initially, our attention mechanism ran as a single kernel, so we worked with the Intel Habana team to split the attention block. While the MME handled one layer’s matrix multiplications, the TPC could simultaneously begin working on the next. It was a delicate process due to complications with increasing memory overhead, but unlocking data parallelism allowed us to approach the theoretical maximum throughput of the accelerator. Combined with the model optimizations, our methods now scale with model sizes ranging from 1B to over 100B+ parameters.

## **Flexible Architecture for the Future**

The hard work that went into this port has implications far beyond just using Gaudi. Hardware design patterns tend to recur across different accelerators, which means the insights gained will give us an advantage in building for any new architecture in the future.

With the rapidly evolving AI hardware landscape, companies should not assume NVIDIA is the only viable option. For us, Gaudi was the first real test of that hypothesis, and it proved that with the right understanding of the architecture, performance and flexibility don’t have to be at odds.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/06/6064326b-cropped-1bd0bc1b-20240419_tsf_seniorheadshots-05843-scaled-1-600x600.jpg)

Raghav Garg is a member of Inflection AI’s technical staff, working primarily on inference optimizations and deployment. Raghav led the team’s effort to port its LLM inference stack to Intel’s Gaudi accelerator. Raghav has a B.S. and M.S. in Computer...

Read more from Raghav Garg](https://thenewstack.io/author/raghav-garg/)