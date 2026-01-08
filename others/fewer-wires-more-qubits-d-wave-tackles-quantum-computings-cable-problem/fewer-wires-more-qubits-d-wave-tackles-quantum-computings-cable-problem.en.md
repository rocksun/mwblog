Quantum computing pioneer [D-Wave](https://www.dwavequantum.com/) today announced an industry breakthrough in its approach to building and controlling its upcoming gate model quantum computer.

One issue that the quantum computing industry is focused on right now — besides the perpetual question of how to best perform the necessary error corrections to run commercially viable algorithms on these machines — is how to connect the quantum computing unit to the classical machines that control it.

## Why Cables Are a Problem for Quantum Computers

This has typically involved running a handful of wires from each qubit to the machine that controls it to perform error corrections, among other things.

Since qubits are fickle, it takes multiple physical qubits to create what is called a logical qubit. The idea here, essentially, is that since the individual physical qubits could randomly decohere (think of it as a bit flip in classical computing), having quite a few of them work in tandem makes it easier to know which qubit is showing the wrong values. For quantum computers to become useful, it’ll take about a hundred logical qubits, which could mean thousands or hundreds of thousands of physical qubits.

That’s a lot of wires to pass from the cryogenic chamber that houses the quantum computing processor to guard it against outside noise to the outside machine — and each wire adds additional noise and heat to that chamber that has to be cooled to just a few millikelvin.

“If you think about how the semiconducting industry evolved, you’ve got chips in your phone and your laptop with billions of transistors. There’s absolutely not billions of control lines that go down to the chip,” [Trevor Lanting](https://www.linkedin.com/in/trevor-lanting?originalSubdomain=ca), D-Wave chief development officer, told me. “It’s fundamental to the growth and the growing adoption of quantum computing technology to make sure that you have that control nailed down. ”

## D-Wave’s Advantage

D-Wave has a bit of an [advantage](https://www.dwavequantum.com/solutions-and-products/systems/) here because it’s able to reuse a standard semiconductor technology (bump bonding) that it also used for its first set of quantum computers. The company is one of the oldest quantum computing firms, after all, but its original focus was on a very different kind of quantum computer from what most newer companies are focusing on.

Those original D-Wave machines, which the company continues to refine, focus on quantum annealing and are great for solving optimization problems. But that also means they’re more limited in their use cases compared to gate model machines that are a bit more akin to classical computers.

Those annealing quantum computers do have the advantage that error correction isn’t as much of a problem, and D-Wave already has a few commercial customers like [NTT Docomo](https://www.dwavequantum.com/company/newsroom/press-release/ntt-docomo-and-d-wave-improve-mobile-network-performance-by-15-with-quantum-optimization-technology/) that use its annealing system in real-world applications.

Now, with its efforts to build a gate model quantum computer, D-Wave can build on some of that earlier experience, even as it’s using a different kind of qubit (a superconducting fluxonium qubit) from most of the rest of the industry.

## Bump Bonding to the Rescue

[Bump bonding](https://www.appliedmaterials.com/eu/en/semiconductor/markets-and-inflections/heterogeneous-integration/bump.html) is a technique the semiconductor industry pioneered to create its increasingly complex chips. By using tiny dots of a conducting metal, semiconductor manufacturers can stack their intricate components on top of each other — and connect them to the outside world without the need for wires.

D-Wave worked with Minnesota-based SkyWater Technology as its foundry partner to create a multichip package that combines its on-chip control technology and the quantum computing processor, reducing the number of cables to a small fraction of what was previously needed.

“Our annealing systems are built in a multilayer fab stack, and have up to, you know, on order a million active Josephson junction components on the chip,” Lanting explained. “What we’ve done with the gate model control is use this multilayer technology, which allows us to build this cryogenic digital control, and then we’ve integrated it with the high-coherence qubit chip, which is on a separate chip.”

Lanting stressed that for this application, the metal used for the bumps has to be superconducting so that no additional heat is created.

“It’s critical that these bump bonds are superconducting,” he said. “We want to make sure that when we make an interconnect between these two chips via this bump on technology, we’re not breaking the superconducting loop — and that then allows us to basically harness all of the controls that we’ve developed for our annealing technology for the game model processors.”

The company was able to use most of the original design it had developed for its annealing quantum computer, but it did have to do quite a bit of work to ensure that the superconducting interconnect worked as expected.

We’ll likely see different players in the quantum computing industry take different approaches to how they control their individual physical qubits. D-Wave obviously argues that its approach will be far more scalable than current approaches and that it also allows the company to modularize its system and add additional quantum processing units as needed.

The industry has seen rapid advances in error correction lately, so it makes sense for the focus to now shift to putting those into practice in scalable systems.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)