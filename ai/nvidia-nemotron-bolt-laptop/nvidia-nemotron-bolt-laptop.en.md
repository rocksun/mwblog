Nvidia on Thursday announced a few new additions to its [Nemotron family](https://thenewstack.io/nvidias-launches-the-next-generation-of-its-nemotron-models/): Nemotron 3.5 Super VL, a 120B vision-language model for enterprise agents and two small Bolt models ([Nemotron 3.5 Bolt 74B-A9B 24GB](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB/blob/main/accuracy.png) and Nemotron 3.5 Bolt E4B 4GB) for running coding, research, and conversational workloads locally.

The Bolt models, Nvidia [says](https://developer.nvidia.com/topics/ai/nemotron), are meant to run “everyday agentic tasks on laptops, balancing speed and intelligence needed to handle multistep reasoning, tool calling, and web browsing.”

And while they come in very different sizes and are meant for different use cases, the focus for all three is on speed and efficiency.

The two larger models are available today, while the smaller Bolt E4B 4G model will launch in the near future.

## Nemotron 3.5 Super VL

The marquee release here is Nemotron 3.5 Super VL, a 120-billion-parameter model that combines reasoning and tool use with image and document understanding.

In the announcement, Kari Briski, Nvidia’s VP for open models and software, notes that the large model is meant to deliver “leading accuracy on multimodal agentic tasks — instruction following, tool use, multistep business workflows, and visual understanding — comparable with NVIDIA’s largest reasoning model at roughly one-fifth the parameter count.”

Super VL builds on [Nemotron 3 Super](https://thenewstack.io/nvidia-launches-nemotron-3-super-a-120b-open-model-for-large-scale-ai-systems/), which launched in March. Both have 120 billion total parameters, with 12 billion active during inference, and context windows of up to 1 million tokens. But while the earlier model only accepted text, Super VL now adds support for image and video input (though not output).

## Mixed results against Qwen

But when it comes to [the benchmarks](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16#benchmarks), though, especially when compared to other open models of comparable size, the results are mixed.

In Nvidia’s own evaluations, Super VL outperforms Alibaba’s Qwen3.5-122B-A10B on scientific reasoning and terminal tasks, while scoring slightly lower on SWE-bench Verified and document understanding.

The five tests are GPQA-Diamond, Terminal-Bench 2.1, SWE-bench Verified, IFBench, and MMLongBench-Doc. Super VL scores 66.7 on Terminal-Bench, compared with Qwen3.5’s 48.7, but trails it on SWE-bench Verified, 71.1 to 71.9.

Qwen has 122 billion total parameters and 10 billion active, compared with Super VL’s 120 billion and 12 billion. The newer Qwen3.8-Flash-Next scores higher on all five tests, though its additional embedding and prediction components bring its total parameter count to about 180 billion.

Thinking Machines’ [Inkling-Small](https://huggingface.co/thinkingmachines/Inkling-Small) has 276 billion total parameters and 12 billion active. It also trails Super VL on terminal tasks but scores higher on instruction following.

Nvidia also reports Super VL ahead of Ultra on [Hermes Bench and LangChain behavioral evaluations](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/#accuracy_and_efficiency_across_agent_tasks), scoring 63.44% versus 56.33% and 87.05% versus 84.3%, respectively.

Overall, though, the focus here was clearly on speed.

Nvidia [reports fourfold faster completion](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/#accuracy_and_efficiency_across_agent_tasks) of 10,000 SWE-bench Pro tasks on four B200 GPUs, though its chart shows lower accuracy than Qwen3.8-Flash-Next and DeepSeek V4 Flash.

![](https://cdn.thenewstack.io/media/2026/10/bc11fd18-nemotron-super-vl-figure-1-updated-1024x426.webp)

## Hybrid Mamba architecture, faster decoding

As for how Nvidia built the model, it’s worth noting that the Nemotron coalition is sticking to the 3.5 family’s hybrid architecture, which combines Mamba-2, attention, and mixture-of-experts layers — but with the addition of a vision encoder. Nvidia also continued training the language model using distillation from Nemotron 3 Ultra before further training for software engineering, vision, and agent tasks, according to its [model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16).

To speed up text generation, Nvidia also uses [LiLiCorr](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/#lilicorr_an_open_speculative_decoding_technique), a technique for speculative decoding. With this, a smaller helper model drafts several tokens ahead, which Super VL checks together instead of generating each token individually. Nvidia says this speeds up token generation on DGX Spark by up to 2.3 times compared with decoding without speculation.

For document workflows, Nvidia says Super VL focuses on optical character recognition, tables, charts, and structured information.

On [CharXiv](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/#combine_text_and_visual_understanding_in_one_workflow), a chart-reasoning benchmark, Nvidia reports 80.8% accuracy, compared with Nano Omni’s 63%. Python code interpretation raises Super VL’s result to 84%.

## Bolt runs 74B in 24GB

If you’re interested in running local models, the new Bolt models may be the most interesting release here — and their benchmarks tend to outperform most comparable models.

Nemotron 3.5 Bolt 74B-A9B 24GB is derived from Super VL. Its hybrid mixture-of-experts architecture activates 9 billion of its 74 billion parameters at a time.

In Nvidia’s [tests](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB#benchmarks), Bolt scores 51.0 on Terminal-Bench 2.1, versus 44.4 for Qwen3.6-35B-A3B and 37.2 for Gemma4 26B-A4B, both tested in BF16. Bolt uses mixed precision, including two-bit experts.

To get to this size, Nvidia used two-bit quantization to reduce the 74B model’s memory footprint to 24GB. The company says it is optimizing the model for RTX Spark and DGX Spark systems, with support for llama.cpp, Ollama, LM Studio, and vLLM.

![](https://cdn.thenewstack.io/media/2026/10/401bdf3f-accuracy-1024x495.png)





Nemotron Bolt 3.5 24GB benchmarks. Credit: Nvidia.

A second, even smaller version of this model, Nemotron 3.5 Bolt E4B 4GB, is scheduled for later this month. With this one, Nvidia is targeting conversational and physical agents on GeForce RTX, Jetson, and Spark hardware, including device assistants and interactive characters that need multiturn tool use and awareness of application state.

## Availability

The new models are now available for download on Hugging Face under the [OpenMDW 1.1 license](https://openmdw.ai/license/1-1/), which permits commercial use and modification.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)