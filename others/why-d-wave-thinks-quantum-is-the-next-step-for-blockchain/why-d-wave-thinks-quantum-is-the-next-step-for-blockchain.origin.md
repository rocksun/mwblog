# Why D-Wave Thinks Quantum Is the Next Step for Blockchain
![Featued image for: Why D-Wave Thinks Quantum Is the Next Step for Blockchain](https://cdn.thenewstack.io/media/2025/03/e75f170b-d-wave-1024x564.png)
Two weeks ago, D-Wave made a splash when its researchers published a [paper](https://www.science.org/doi/10.1126/science.ado6285) in Science that claimed that its latest annealing [quantum computer](https://thenewstack.io/quantum-computing-use-cases-how-viable-is-it-really/) had been able to solve a complex materials science simulation problem that, D-Wave claims, would have taken a classical supercomputer a million years to solve. Now, D-Wave wants to use this same quantum computer and algorithm to power blockchain applications, by offering a faster and environmentally friendly alternative to today’s mining operations.

As Nvidia CEO Jensen Huang joked during a panel at his company’s GTC conference last week, every quantum computing milestone seems to come with a controversy, and so it’s maybe no surprise that D-Wave’s breakthrough was also met with quite a bit of skepticism. A number of researchers, including those at New York University’s Flatiron Institute Center for Computational Quantum Physics argued that a laptop could have easily solved the same problem, something D-Wave’s outspoken CEO Alan Baratz forcefully dismissed when I talked to him at Nvidia’s GTC conference last week.

“First of all, they only computed one property on a small lattice,” Baratz said. “There are several properties that we computed, and the other properties are much more complex, and [the New York University researchers] never talked about how they would address those other properties. Secondly, they also didn’t address all the topologies that we addressed, and they never even mentioned whether they could address them or not. And then finally, there are two key parameters. It scales linear in one of the parameters; it scales exponentially in the other parameter — and they don’t talk about that. And to get to the bigger lattices and the full set of properties, you need to scale in the other parameters, okay? So it just it was a gross overstatement of what they had done, and, I think, a grab for notoriety. Honestly, that’s my view.”

![D-Wave's Advantage quantum computer.](https://cdn.thenewstack.io/media/2025/03/b5c1deef-dwave_advantage_system.png)
D-Wave’s Advantage quantum computer.

We’ve seen other quantum supremacy claims recent years, including from [Google](https://cloud.google.com/?utm_content=inline+mention), and as is so often the case in quantum computing, it’ll take a while before the community to agree on how to interpret these results.

What is clear, however, is that quantum computing is currently moving toward usefulness at a faster clip than ever before, as years — and sometimes decades — of fundamental research and development in hardware and software start to pay off. Most researchers would likely agree that we are still a few years away from seeing fully error-corrected quantum computers (though there have been some recent [breakthroughs](https://blog.google/technology/research/google-willow-quantum-chip/) there, as well as some novel hardware approaches from [the likes of Microsoft](https://thenewstack.io/microsoft-makes-quantum-computing-breakthrough-with-new-chip/), too) that can solve real-world problems.

The current line of thinking, one that was reiterated multiple times during Nvidia’s GTC Quantum Day, is that it will take about 100 fully error-corrected logical qubits to run algorithms that can have a real-world impact on science problems. One logical qubit consists of dozens — or maybe hundreds — physical qubits, which, as a group, help ensure that a logical qubit can be protected from errors and stay coherent, even as individual physical qubits lose their state. The current state of the art is 24 logical qubits, which was the result of a partnership between [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) and Atom Computing.

Where does blockchain come in here? D-Wave calls its [paper](https://ir.dwavesys.com/news/news-details/2025/D-Wave-Introduces-Quantum-Blockchain-Architecture-Featuring-Enhanced-Security-and-Efficiency-over-Classical-Computing/default.aspx) “Blockchain with Proof of Quantum Work,” playing off the idea of ‘proof of work,’ which powers Bitcoin, for example. The twist here is that instead of solving a highly compute-intensive problem on a classical machine, users would submit the proof of work done on a quantum computer. And to do that, D-Wave chose the algorithm it used to show supremacy on its quantum processor.

D-Wave started the work on the supremacy efforts two years ago, Baratz said. “We almost treated it like a product deliverable,” he explained. Then, last year, he gave the team the challenge to build an application on top of this work and the result of that was this blockchain effort.

“When you do blockchain, essentially what you’re doing is you’re presenting an experiment, and then you have to do computation to basically perform the experiment,” Baratz explained. “So the experiment that we are presenting is compute the property of this material with this lattice.” Since D-Wave argues that this specific computation can’t be done classically, using a quantum computer is the only way to present a valid solution.

Baratz also argued that this essentially makes the entire system [quantum-safe](https://thenewstack.io/nist-secures-encryption-for-a-time-after-classical-computing/) from the outset. “In some sense, we are developing a system that’s almost quantum-safe by construction,” he said. “In other words, what does it mean to be quantum safe? If you’ve got a classical algorithm, what you’re worried about is that quantum can do it faster. And quantum-safe means that quantum can’t do it faster. Well, if, by construction, it requires quantum, then there’s no notion that quantum can do it faster.”

He also stressed the fact that a quantum computer consumes only a fraction of the power that traditional mining operations use.

Right now, D-Wave has this running on four quantum computers in two different countries, which Baratz argues marks the first-ever “distributed quantum application.” He noted that this is still a proof of concept and that important enhancements are still necessary before this system could be considered production-ready, but D-Wave continues to work on this.

It’s worth stressing that D-Wave did this work on its quantum annealing processor. That’s a very different technology from the gate-model machines like superconducting quantum computers or trapped ion machines that others in the field are working on.

The core idea behind a quantum annealing is to guide a quantum system to its lowest-energy state to find the optimal solution to a given problem. That makes them great for solving problems that focus on optimization (be that routing cars or simulating the properties of a material). This also bypasses the question of having to create logical qubits. Gate-model machines, meanwhile, are more flexible and more akin to classical computers in that they use logic gates, but with more overhead and complexity because of the error correction needed.

D-Wave itself is working on a gate-model quantum processor, which uses many of the techniques the company developed in its quantum annealing work. Baratz says the company is “making good progress” and expects the program to be able to demonstrate that the company can build a logical qubit soon.

The company is also in the process of rolling out its newest quantum annealing processor, the Advantage-2, which was already used in some of the quantum supremacy work.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)