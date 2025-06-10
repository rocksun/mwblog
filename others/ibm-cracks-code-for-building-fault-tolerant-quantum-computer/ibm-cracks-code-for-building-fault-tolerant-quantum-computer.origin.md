# IBM Cracks Code for Building Fault-Tolerant Quantum Computer
![Featued image for: IBM Cracks Code for Building Fault-Tolerant Quantum Computer](https://cdn.thenewstack.io/media/2025/06/77d024b2-ibm-quantum-starling-render-2-1024x576.jpg)
For a while now, IBM has said that it planned to build a fault-tolerant quantum computer by 2029. What wasn’t clear, however, was how the company planned to do that. Error correction — that is, the ability for a quantum processor to recover from the inevitable errors introduced by even the tiniest bit of noise — remained maybe the most crucial unsolved problem in building a fault-tolerant quantum computer. Today, in two technical papers, IBM claims to have solved error-correction with the help of a novel algorithm and details the architecture (dubbed the “bicycle architecture”) that puts this algorithm and some additional pieces into practice.

“I feel we’ve cracked the code for quantum error correction — and now we say we can build it,” [Jay Gambetta](https://www.linkedin.com/in/jay-gambetta-a274753a/), the vice president in charge of IBM’s quantum initiatives (and a co-author of the architecture paper), told me in an interview ahead of today’s announcement. “So we’ve pretty much laid out exactly on the roadmap how we’re going to do it and I view it as an engineering rather than a science challenge now.”

By 2029, IBM expects to launch its Starling quantum computer, which will feature 200 logical qubits and will be capable of 100 million quantum operations. This new machine, IBM claims, will be 20,000 times more powerful than today’s quantum computers and capable of producing real-world results in fields like drug development, materials discovery, chemistry, logistics and finance optimization that classical computers aren’t capable of solving in any reasonable time.

## Creating a Better Error-Correction Algorithm
There’s a lot to unpack here, but it’s worth taking a step back first. A year ago, in a [Nature paper](https://www.nature.com/articles/s41586-024-07107-7), Gambetta and his co-authors described a new error correction algorithm (the Low-Density Parity Check) that brought down the amount of physical qubits it would take to build a working quantum computer with 12 logical qubits from almost 3,000 to 288, all while having an error rate of 0.1%.

To create a logical qubit, the rough equivalent of a bit in classical computing, you need far more physical qubits to detect errors, in part because every single one of the physical qubits may be affected by noise at some point during the calculation. By having a number of physical qubits, you can detect the error in those specific qubits and correct them, protecting the state of this virtual logical qubit in the process.

It’s these errors in the physical qubits that have long plagued the industry. You can’t fully isolate the quantum processor from any kind of noise, after all, if you want to actually use it. With the previous state-of-the-art “surface code” algorithm, it would have taken a million or more physical qubits to build a fault-tolerant machine that could produce real-world results — a massive engineering challenge that nobody knew how to solve.

The problem with that first paper was that it was focused only on quantum memory, not actually running computations on those qubits.

Gambetta acknowledged as much. “The natural criticism of that paper was: you only did it for memory. If I need a computation, I need a way to do gates, and I need a way to entangle and to scale. And the other criticism of that paper was: the decoder you do is so complex that you would never be able to do it in real time.”

Now, in the new architecture paper, IBM shows how it plans to efficiently create quantum gates, which essentially allow the machine to put the qubits into different states, and how to scale these quantum computers up to thousands of logical qubits over time. Those gates are created by what IBM calls the Logic Processing Unit (LPU), and the company created what it called the Universal Adapter to connect the different modules together.

“When you put all that together and you do an end-to-end calculation, you find that it’s still orders of magnitude less qubits than the surface code when you do the computation,” Gambetta explained.

## Building Better Decoders With Disordered Memory
One reason why implementing the existing error correction algorithms was so problematic was because those algorithms have to run on classical computers in real time. Now, that overhead is reduced by 90%, IBM says. And that’s maybe the real breakthrough here. To check whether a physical qubit that is part of the overall logical qubit has an error, quantum computers use what is generally called a “decoder.” Quantum processors regularly check if there are any errors, with the decoder taking in this data, checking what the patterns of errors look like, and then applying the error correction. Until now, the state of the art here was using a message-passing algorithm called belief propagation, which has been around [for quite a while](https://arxiv.org/abs/0706.4094), but which also has a tendency to, as Gambetta pointed out, “get stuck.” When that happens, another algorithm has to kick in (dubbed “ordered statistics decoding”), but that is a very complex calculation that even specialized hardware wouldn’t be able to handle in real time.

So the IBM boffins went ahead and created a new decoder that can run in real time on a field-programmable gate array (FPGA): relay belief propagation. In the belief propagation method, different nodes pass messages back and forth, updating the decoder about their “beliefs” about where errors might be in the logical qubit. But as Gambetta said, those beliefs can end up swinging back and forth, with the algorithm never settling on an answer. A newer algorithm, memory belief propagation, then added a memory component to this, which basically functions as a notepad for the decoder to keep track of the best guesses so far.

What IBM’s researchers have done now is make a crucial change to this memory component by introducing “disordered memory” into the mix. The idea here is to break the symmetries and dampen the oscillation that can lead to stuck decoders by strategically injecting disordered memory strengths into the system, which then allows the algorithm to find valid solutions without having to start from scratch. Basically, instead of every part of the error correction system remembering information in exactly the same way, each node now gets its own memory strength (which can even be a negative number).

The end result is that this algorithm can now run in real-time on an FPGA (with IBM hoping to build specialized chips for this use case before 2029, too).

## Getting to 2029
The current plan is for IBM to release a series of new quantum computers that will each implement a piece of this puzzle for building the Starling machine in 2029.

The new error-correction decoder will make its debut next year. Then, in 2027, IBM plans to show that it can entangle modules with its new Universal Adapter and then, with Starling, it will demonstrate a system that uses multiple of these modules to create a fault-tolerant machine with 100 million gates.

To get there, Gambetta argues, is now a question of improving the various components of these machines to the point where they are reliable in day-to-day use.

There is also an interesting classical computing problem to be solved here, because each FPGA in the current setup needs about 45 watts of power per physical line. IBM has a proof of concept in using a specialized ASIC to control these chips, but how do you scale that? “Even if, say, I succeeded in the modules, I succeeded in the yields, and all those things, if the answer is, I need a nuclear power plant to control this, we’ve messed up,” Gambetta said.

“I still want to be clear there’s a difference between scientifically solving it and building it,” he noted. “I’m not saying it’s done. It’s a huge engineering challenge. But sometimes when I think about science problems, I don’t know which way I’m going to go. And the science is about exploring and then solving with some intuition and the scientific method. Engineering is: I’ve got a solution, but it’s hard. Cycles of learning, engineering, reliability — these things we’ve got to do. So I feel we’ve gone from science to engineering. And, to me, that’s a big statement, because it means these things are going to exist.”

![](https://cdn.thenewstack.io/media/2025/06/68fdebab-2025-development-innovation-roadmap-scaled.jpg)
On June 10, 2025, IBM released an updated IBM Quantum Roadmap to detail its path to IBM Quantum Starling, the world’s first large-scale, fault-tolerant quantum system. Image credit: IBM.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)