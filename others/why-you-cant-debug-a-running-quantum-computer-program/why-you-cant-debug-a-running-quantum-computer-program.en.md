In a sense, writing applications for quantum computing is very much a case of going back to the future. Much like the mainframe programmer of the 1970s, Today’s quantum computing programmer has to debug their code before it runs on the iron, because the quantum runtime itself is so very expensive, and still is quite limited in capability.

In fact, by its very nature of the technology, quantum computing programs can not be debugged, at least not while they are running.

Test in production? Not a chance.

“Running on quantum hardware is very expensive, so you don’t want to find out that your code has a bug once you get there,” said [Mariia Mykhailova](https://www.linkedin.com/in/mariiamykhailova/), in a virtual talk last week for the [Association for Computing Machinery](https://www.acm.org/about-acm) about the quantum computing behaviors developers should keep in mind.

Mykhailova is the principle software developer for quantum startup [PsiQuantum](https://www.psiquantum.com/software), and has worked as an engineer for Microsoft’s Quantum business unit. She also teaches the subject at [Northeastern University College of Engineering](https://coe.northeastern.edu/people/mykhailova-mariia/).

In the talk, she introduced a workflow for quantum software development. It’s a job that requires not only writing the code — involving both classical and quantum languages — but also validating of the correctness of quantum programs as well as estimating their performance on fault-tolerant quantum computers.

The talk was timely. With cloud providers such as [Microsoft Azure](https://azure.microsoft.com/en-us/solutions/quantum-computing), [Amazon Web Services](https://aws.amazon.com/braket/), [IBM](https://quantum.cloud.ibm.com/) all offering [quantum computing services](https://thenewstack.io/ibm-cracks-code-for-building-fault-tolerant-quantum-computer/), now may be the time to testing out quantum computing.

## When Do Quantum Computers Have an Advantage?

Many jobs will never be suitable for [quantum computing](https://thenewstack.io/why-d-wave-thinks-quantum-is-the-next-step-for-blockchain/). [Machine learning](https://thenewstack.io/machine-learnings-next-frontier-quantum-computing/), for instance, which requires ingestion of large data sets, may not be suitable. Image recognition, web search or text editing are other apps that wouldn’t benefit from quantum computing, she said.

Keep in mind that loading data into a classical computing is easy and inexpensive, but quite a chore with quantum computing.

“In quantum computing, loading input data in some sort of quantum state that can later be used is already an expensive operation,” she said.

The ideal quantum computing job, she said, has a limited input, a lot of computation, and a limited output.

Today, most computing jobs do not need [quantum power](https://thenewstack.io/quantum-computing-use-cases-how-viable-is-it-really/), she said. She presented a graph showing a range of possible application characterized by the time it takes to solve them against the size of the problem itself.

[![Screenshot of a chart. ](https://cdn.thenewstack.io/media/2025/09/14294dde-acm-quantum-mykhailova-00.png)](https://cdn.thenewstack.io/media/2025/09/14294dde-acm-quantum-mykhailova-00.png)

For larger problems, both a classical computer and a [quantum solution](https://thenewstack.io/microsoft-makes-quantum-computing-breakthrough-with-new-chip/) will consume more resources.

“When you think in these terms, in becomes clear which programs are good for quantum computing, and which ones are not so good,” she said.

Quantum offers no advantage for smaller applications. Rather, quantum is best for the jobs that would take prohibitively long periods of time for classical computers to complete, if they can be completed at all.

One such example would be finding the energy of the ground state of a molecule. A classical computer can do a quick analysis of a simple molecule such as hydrogen with no problem. Understanding the larger, more complicated molecules will be the domain of the quantum, she said.

So the first task in developing quantum software is to characterize its performance, to see if it’s advantageous to use a quantum program to begin with.

## The Challenges of Noisy and Slow Quantum Hardware

One thing to keep in mind is that [quantum computers](https://thenewstack.io/googles-quantum-computer-can-exponentially-suppress-errors/) are slow, much slower than traditional computer systems, in fact: A query on a quantum computing system is much slower than that of a classical computer.

Why such? Quantum computers are noisy, so the operation of every single logical gate must be error-corrected. Plus, the gates themselves are slow, and most quantum computing systems, for the foreseeable future, will have precious few gates.

As a result, the algorithms that you develop must be highly efficient and must be thoroughly tested before they hit the hardware

![Software development workflow](https://cdn.thenewstack.io/media/2025/09/e418b20b-acm-quantum-mykhailova-01.png)
:   A workflow for developing a quantum application — before it even touches the hardware.

“You need to figure out whether this solution is going to be good enough. You need to estimate its performance. You need to basically figure out how many resources it’s going to need,” both in terms of how many resources you need and how long the job will take, Mykhailova advised.

If the job takes too long, it’s back to the drawing board.

## The Unique Difficulties of Debugging Quantum Programs

As Mykhailova said, testing on actual quantum hardware is expensive. And, like any debugging, you’ll need multiple runs.

Plus, owing to the nature of quantum computing, “state” can not be measured directly.  The developer’s debugging process of stepping through a program line-by-line won’t work. “Doing this will ruin your state,” she said.

And their noisy nature is problematic as well: If you get an incorrect result (or even a correct one for that matter), you don’t know if it is because of system noise, or because the algorithm is operating incorrectly, or correctly, as the case may be.

The good news is that there are simulators to help with these estimates. Quantum simulation software runs on classical hardware, but replicates a quantum computer through many of the same operations. Plus, they offer the traditional debugging tools. These work well for programs that require up to 30 qubits or so.

It is still “an open question” of how to test larger quantum computing programs, she said.

She walked through [an example](https://www.psiquantum.com/news-import/psiquantum-launches-construct) of preparing a set of quantum bits to produce a “state” for the machine.

## A Workflow for Developing Quantum Applications

The first step is to design the algorithm to do what you want it to do, formatting it in a circuit diagram to illustrate the multiple versions of the qubit.

[![Qubit design diagram.](https://cdn.thenewstack.io/media/2025/09/726e10fa-acm-quantum-mykhailova-03.png)](https://cdn.thenewstack.io/media/2025/09/726e10fa-acm-quantum-mykhailova-03.png)

The next step is to write the code. Her example was written in [Python](https://thenewstack.io/what-is-python/) and utilized PsiQuantum’s *psiqworkbench* library to express the qubits and qubricks in the code.

The resulting program mixes classical and quantum computing, with the specific methods used to express gates. She used [Pytest](https://docs.pytest.org/en/stable/) to validate the code, with the correct results embedded in the code itself for validation.

From these numbers, you can also estimate the number of qubits needed to run the program, and make your comparisons to a classical approach or just arrive at an idea if the algorithm needs to be refined. Repeat as needed.

## Learn How To Program in Quantum

A big advocate of learning by doing, Mykhailova recommends writing quantum programs to learn the craft. She suggested learning the basics through the Microsoft [Quantum Katas](https://quantum.microsoft.com/en-us/tools/quantum-katas) site. Then delve more deeply into Microsoft’s [Q# language](https://learn.microsoft.com/en-us/azure/quantum/qsharp-overview), the [Qiskit](https://www.ibm.com/quantum/qiskit) software stack from IBM, and the [two](https://www.oreilly.com/library/view/q-pocket-guide/9781098108854/) [books](https://www.manning.com/books/quantum-programming-in-depth) she authored on the subject.

And don’t worry, you don’t need to know quantum physics to program a quantum computer.

” Under the hood, quantum computing is linear algebra and probability theory,” she said.

“You need to know physics specifically if you work on the lowest, lowest levels of the stack, the levels that basically do control of the actual physical objects and processes that implement your quantum computer,” but most devs won’t need that. The qubits are rendered as mathematical constructs that can be readily understood.

“If you work on the compilation stack, on user-facing software, like I do, you don’t need to know physics. That bit is abstracted away several layers under you,” Mykhailova said.

ACM will [have the free talk online](https://events.zoom.us/ev/AqZToK3BMn0keNLwD_ZBBgJ4H7Oo-_7wU_KUBe1OhmVRoo7qzpLX~AuM0BSSw2kkvpz7I2HvUbkNNGsZDwOXtw8IGKL3t1h6StnkybixUsSuLvg) for replay for a limited time, though it will eventually get moved to the [archive page](https://learning.acm.org/techtalks-archive).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)