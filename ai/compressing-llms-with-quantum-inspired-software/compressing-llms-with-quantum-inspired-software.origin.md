# Compressing LLMs With Quantum-Inspired Software
![Featued image for: Compressing LLMs With Quantum-Inspired Software](https://cdn.thenewstack.io/media/2024/12/a412e797-enrique-laszos-olmos-cropped-1024x576.png)
Large language models are inefficient, period. That’s apparent at [AWS re:Invent](https://reinvent.awsevents.com/) this week. [Inference](https://thenewstack.io/5-open-llm-inference-platforms-for-your-next-ai-application/) is a hot topic, and conversations center on how to make the most of LLMs, considering the cost of training and the energy consumption required.

[Multiverse Computing](https://multiversecomputing.com/), a company participating in the [AWS Generative AI Accelerator,](https://aws.amazon.com/startups/accelerators/generative-ai?lang=en-US) has developed ways to compress LLMs using quantum-inspired software. Based in San Sebastián, Spain, the company accelerates computing with quantum-inspired tensor networks, said founder and CEO [Enrique Lizaso Olmos](https://www.linkedin.com/in/enriquelizaso) in an interview before [AWS](https://aws.amazon.com/?utm_content=inline+mention) re:Invent.
Tensor networks are powerful mathematical structures using “methods that attempt to use a classical computer to simulate the behavior of a quantum computer, thus making the classical machine operate algorithms that benefit from the laws of quantum mechanics that benefit real quantum computers,” [according to a post](https://thenewstack.io/quantum-algorithms-vs-quantum-inspired-algorithms/) by [Pedro L e S Lopes](https://thenewstack.io/author/pedroleslopes/), on the topic of quantum-inspired computing and how it compares to [quantum computing](https://thenewstack.io/machine-learnings-next-frontier-quantum-computing/).

[Consider the cost and energy needed to train models and perform inference](https://medium.com/@gmicloud/inference-innovation-how-the-ai-industry-is-reducing-inference-costs-889b79275a8c). Multiverse compresses LLMs with techniques that, according to the company’s own published research, reduce by 93% the memory size of LlaMA-2-7B; it also reduces by 70% the number of parameters, accelerating 50% the training and 25% the inference by times of the model. Additionally, the accuracy drop is 2% to 3%.
Multiverse, Lizaso said, works with many companies that have already tried LLMs but have found it expensive to deploy. The problem: LLMs need to be more efficient. They scale in parameters, but accuracy only improves linearly. The costs increase as more computing is used. Buying the GPUs is costly, and just as costly or even more costly is buying the GPUs from a cloud services provider.

Multiverse started working with [Bosch](https://www.bosch.com/), a German engineering and technology company that wanted help with an on-premise AI system to reduce defects, Lizaso said.

“So we applied our tensor networks,” Lizaso said. “We developed a completely new set of algorithms for [machine learning](https://thenewstack.io/the-ultimate-guide-to-machine-learning-frameworks/). Well, it worked quite well. So we applied those same systems to finance and defense and so on. But at some point, and that was in 2023, we asked ourselves, can we just prepare a better system, a compressed system of large language models?”

## What’s the Future of Compression?
When we come to the age of quantum computing, the compression will be sped up, so almost anything will have some form of embedded intelligence due to quantum computing’s ability to analyze vast amounts of data far beyond what is possible using classical computing methods. It acts unlike a classical computer, processing information in the binary sense of 1s and 0s, using a quantum mechanical property called superposition, explained [Kimberly Mok](https://thenewstack.io/author/kimberleymok/) in [a previous post on The New Stack](https://thenewstack.io/robots-learn-faster-with-quantum-technology/).

It’s a bit mind-boggling, but in essence, information gets processed as either or both 1s and 0s simultaneously.

We’re not quite in quantum land. Progress toward trustworthy quantum computing is measured in [qubits](https://thenewstack.io/quantum-algorithms-vs-quantum-inspired-algorithms/). The number of qubits to achieve usefulness is upwards of a million or more. When we all get to that point, we’re a long way; by the way, we will see compression on a level unimaginable to us now.

Lizaso compared the brain of a fruit fly to the size of an LLM. A fruit fly has 140,000 neurons and 55 million synapses, meaning neurons or connections between cells, according to a recent article in [Nature](https://www.nature.com/articles/d41586-024-03029-6), which published a story about a fruit fly’s brain diagram.

A fruit fly has intelligence. It can walk, fly, mate, fight. It’s autonomous. It does not need a network connection. An LLM does not do a heck of a lot, compared to any creature. But what does it take to create? [Unprecedented electrical power, billions of dollars in training](https://thenewstack.io/meeting-the-operational-challenges-of-training-llms/). And what can it do?

But what if the intelligence of a fruit fly can be embedded in a robot? It would open up a whole new way of thinking about how LLMs today will seem prehistoric when we can compress enough data to give robots the ability to fly. This means that someday, connected and unconnected devices will have super intelligence with the help of quantum computing. The fruit fly has nature on its side. But our efforts are unsustainable. We will never have the capabilities of sentient beings using classical computing. This means that what we can do now is unsustainable.

Multiverse sells two products: CompactifAI and Singularity. Both provide capabilities to make LLMs more efficient. The company supports multiple models, including [Mistral](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/), Bert, and Zephyr. Access to the model itself is needed to compress it. According to Multiverse, [OpenAI](https://openai.com/) provides an API to access (query) the model, “therefore Multiverse Computing’s product is not able to compress it.”

Tradeoffs? There are a few. You need a lot of expertise and there may be the need to retrain. Accuracy is still a question mark, but still, quantum-inspired computing may be an answer to a problem that we need to solve. There’s just so much electricity we can produce for LLMs that are only increasing in size.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)