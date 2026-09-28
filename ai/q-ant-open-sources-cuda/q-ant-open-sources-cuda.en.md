[Q.ANT](https://qant.com/), a startup out of Stuttgart, Germany, builds processors that use light instead of electricity to do some of the math behind AI. The company pitches them as a way to run AI on a fraction of the power today’s chips need.

Now developers can start writing software for those chips without owning one. Q.ANT pushed a free, open-source software kit to GitHub this week that lets developers build and test programs on a normal computer, then run them on the real chips once they get access.

This is a move out of Nvidia’s playbook. Nvidia owes its lead in AI as much to CUDA, the software developers use to program its GPUs, as it does to the chips themselves.

But with Q.ANT, the catch is the hardware. Q.ANT’s chips are running at a few research computing centers, and everyone else has to wait “the coming months” for cloud access through German provider IONOS or an on-site server from Q.ANT.

The kit, called the [Q.ANT Native Computing Toolkit](https://github.com/Q-ANT-GmbH/qant_native_computing_toolkit), is free on GitHub under a license that allows commercial use. Developers can work in Python or C. The key piece is a simulator that mimics the chip on a regular computer, with no Q.ANT drivers required.

What can it do today? The AI tools in this first version focus on running models that have already been trained. The examples read handwritten numbers, identify objects in photos and outline shapes in images. Training still happens on regular CPUs and GPUs.

The pitch for photonic computing is power. AI chips burn a lot of energy moving data back and forth between memory and the processor. Q.ANT’s chips do part of the math with light, specifically wave-shaped functions similar to a cosine, which regular chips calculate digitally. Q.ANT says AI models built around those functions get better results with fewer parameters, the settings a model learns during training. Fewer parameters means a smaller model, less data to move and less power. The kit includes examples comparing a standard model with one built Q.ANT’s way. Those comparisons are the company’s own.

“An ecosystem isn’t created by hardware alone. It emerges when the software layer is open and others can build on it,” said Michael Förtsch, Q.ANT’s founder and CEO. He calls the release the “Linux moment” of photonic computing.

Q.ANT is betting light can do the math itself. Lightmatter, one of the best-known companies in the field, now puts its focus on Passage, which uses light to move data between chips. The idea of light-based AI isn’t new, either. TNS covered [MIT’s photonic processor for building optical neural networks](https://thenewstack.io/mit-devises-photonic-processor-building-optical-neural-networks/) back in 2017.

Q.ANT raised €62 million in July 2025 in a round led by Cherry Ventures, UVC Partners and imec.xpand. In March, it said its second-generation chips were running at the Leibniz Supercomputing Centre near Munich. The [results it published from there](https://qant.com/press-releases/higher-performance-less-energy-q-ant-deploys-second-generation-photonic-processors-at-supercomputing-center-lrz/) compare the new chip with its old one: more than 50 times faster at the kind of math that does most of the work in AI models, and six times less energy on typical jobs, by the company’s numbers. Its bigger claims, like up to 30 times better energy efficiency, don’t say what they’re measured against.

Good software alone won’t carry a new chip. Nvidia has been building CUDA for nearly 20 years and is still adding to it, including [deeper native Python support](https://thenewstack.io/nvidia-finally-adds-native-python-support-to-cuda/) last year. Graphcore, the British AI chip startup, had its own software kit and still ended up being sold to SoftBank in 2024.

Q.ANT calls this the first openly available software kit for programming a photonic processor. That depends on how you count. Xanadu has offered free, open software for its light-based quantum computers since 2018. For now, developers can play with the simulator. What they can’t do yet is test Q.ANT’s power-saving claims on their own models. That has to wait until the chips open up.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)