IBM on Wednesday announced that it has built and cooled the first two modules of a new cryogenic dillution refrigerator designed to house the processors in its future [fault-tolerant quantum computers](https://www.ibm.com/quantum/blog/large-scale-ftqc).

One major caveat: those refrigerator modules don’t actually house any quantum processors yet, but IBM says plans to install one [Nighthawk processor](https://www.ibm.com/quantum/blog/whats-new-q1-2026) in each unit later this year.

This will be the first test of whether processors will work inside the new refrigerator and can communicate across the connection between its modules. That’s a crucial next step for IBM’s quantum ambitions, given that its plans for future quantum computing systems hinge on its ability to efficiently connect multiple individual processors and cryogenic modules into a single system.

![](https://cdn.thenewstack.io/media/2026/08/bb9d1a7f-ibm-modular-cryogenics-5-1024x768.jpg)

Credit: IBM.

## Why build a better fridge?

To work, superconducting quantum processors need to operate at a fraction of a degree above absolute zero to reduce noise, which is, after all, one of the main enemies of stable, long-running quantum computers.  
At this point in the development of quantum computers, it’s all about building larger, more fault-tolerant machines, but building larger systems isn’t just about adding more qubits. Each processor needs control and readout wiring, shielding, cooling, and electronics. All of that has to fit inside or around the refrigerator without producing too much heat to disrupt the qubits.

“It’s really about all the infrastructure and the supporting pieces around it as well in the system,” Jerry Chow, IBM fellow and chief technology officer for quantum-centric supercomputing, pointed out in a press briefing ahead of the announcement.

![](https://cdn.thenewstack.io/media/2026/08/fae3cbd8-ibm-modular-cryogenics-2-1024x768.jpg)

Credit: IBM.

IBM’s new design splits that refrigeration infrastructure into rectangular cells that can be connected to create a shared ultra-cold environment for the quantum processors. The first two modules together measure about 8 feet tall and 8 feet wide and can reach temperatures below 15 millikelvin.

During its tests, IBM also added a 30-microwatt heat load to simulate the processors, wiring, and electronics that will eventually sit inside. With that load added, the units operate at 23 millikelvin.

## More room for wiring

Currently, IBM’s quantum systems house processors with more than 100 physical qubits, but its planned fault-tolerant computers will need thousands — and later hundreds of thousands — of physical qubits to create a smaller number of error-corrected logical qubits.

Each added qubit means more wires. Indeed, IBM says each new module has about 12 times more wiring space than Quantum System One, the company’s first commercial quantum computer it introduced in 2019.

Because of their modular nature, the new fridge modules will let IBM place the individual quantum processors closer together, but there’s still the actual connection between the processors to deal with.

“For now, this provides more physical room for a lot of that,” Chow says.

IBM says it is researching more efficient control systems, but the current design will give its engineers more space for the wiring they already know they will need. Since the entire system is modular, if IBM changes the wiring for a new processor generation, it can replace that assembly without rebuilding the rest of the refrigerator.

“We can redesign and replace this piece very quickly while keeping the rest of the system the same,” Oliver Dial, IBM fellow and vice president of quantum systems, says.

Thanks to this, IBM can also build and test each cell before shipping it to a client site, where the modules can then be connected into a larger system. Dial acknowledges that a single enormous vacuum chamber could be cheaper for one machine, but it would be harder to manufacture, ship, and repeat.

## Connecting processors across modules

Connecting individual quantum processors to each other is still a work in progress and a lot of R&D is spent on it. IBM plans to connect processors inside the refrigerator with its L-coupler, a superconducting cable that can carry microwave photons between chips separated by as much as a meter. The coupler can transfer a quantum state or perform a two-qubit operation between chips, according to the company.

IBM previously demonstrated L-couplers with [Flamingo](https://www.ibm.com/quantum/blog/qdc-2024), a prototype that connected two Heron processors. Dial says IBM’s best two-qubit operation across an L-coupler has now reached 99.3% fidelity. The idea is to get this to 99.9% for IBM’s fault-tolerant systems.

[Researchers have previously connected individual qubits](https://arxiv.org/abs/2008.01642) housed in separate dilution refrigerators.

## Scaling up

IBM says it expects to be able to start deploying these modular refrigerators next year. Its first systems will use two or three cells and support about 1,000 programmable physical qubits.

For the upcoming [Starling](https://www.ibm.com/roadmaps/quantum/2030/) systems, the fault-tolerant computer it intends to deliver in 2029, IBM expects to need about 12 modules.

Dial identifies reliability as the largest problem on the way to a fault-tolerant machine.

“We’re talking about systems going from thousands of qubits to hundreds of thousands of qubits,” he says. “We need everything about our systems to become 1,000 times more reliable.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)