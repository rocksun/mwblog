# Oxide Computer Installs On-Premises Servers for Lawrence Livermore
![Featued image for: Oxide Computer Installs On-Premises Servers for Lawrence Livermore](https://cdn.thenewstack.io/media/2023/07/42bf8d69-oxide-1024x683.jpg)
The host of the world’s fastest supercomputer (called El Capitan), Lawrence Livermore National Laboratory, is installing [Oxide Computer](https://thenewstack.io/oxide-launches-the-worlds-first-commercial-cloud-computer/)‘s [minimalist cloud servers](https://thenewstack.io/in-pursuit-of-a-superior-server-oxide-computer-ships-its-first-rack/) to protect valuable assets and data.

The cloud servers will run in parallel alongside the high-performance computers hosted at the lab.

El Capitan will be used to maintain responsibly the U.S.’s nuclear stockpile. The system stores critical data, and on-premises cloud hardware reduces the chances of hackers breaking into the system.

Oxide Computer’s cloud server design uses a custom motherboard stripped of unnecessary parts, wires, and components typically found in off-the-rack servers.

The company has completed the installation of the first Oxide Cloud Computer at LLNL’s Livermore Computing HPC center.

“We’ll continue to work with them on building out cloud capabilities, and they plan to deploy additional Cloud Computers in the future,” [Bryan Cantrill](https://thenewstack.io/bryan-cantrill-predicting-the-present/), chief technology officer at Oxide Computer, told The New Stack.

Removing the bloated components and software allows the software to work more closely with silicon. The cloud server provisions virtual machines and services via self-service APIs and can blend into HPC jobs.

The cloud computer “enables LLNL to introduce secure hyperscale-like cloud capabilities within their HPC center,” Cantrill said.

These capabilities include deploying critical, persistent services like databases, Jupyter notebooks, orchestration tools, Kubernetes clusters, and more.

The public cloud has innovated and developed extensive APIs, security layers, and automated cloud environments, which has left traditional on-premises data centers behind, Cantrill said.

## State of the Art
“The current state of the art for on-premises computing consists of cobbling together a set of disjointed hardware and software components from various vendors,” Cantrill said.

The Oxide systems differentiate themselves with a unified hardware and software approach. Oxide has developed open source software that includes elastic virtual compute, storage, and networking services. No licensing costs are involved, which can save the lab money.

“This allows virtual resource provisioning on-demand for smooth integration with LLNL’s Flux resource manager,” Cantrill said.

The on-premises cloud server also boosts data security at LLNL. U.S. government labs still prioritize air-gapped on-premises systems for security reasons.

Oxide’s Cloud Computer software “enables multitenancy and allows LLNL to give each team a silo inside the rack,” Cantrill said.

The stripped-down hardware and software also reduces the attack surface for hackers to break into the hardware and steal data. Hackers could use firmware and middleware layers to break into systems and steal data.

“This is really powerful and an example of how they want the HPC center to function in the future… the ability to enhance isolation capabilities has been key,” he said.

## What’s in the Box?
Cantrill is well-known among open source enthusiasts. He created DTrace while employed at [Sun Microsystems](https://thenewstack.io/sun-microsystems-a-look-back-at-a-tech-company-ahead-of-its-time/) and co-founded Oxide in 2019. The company faced hardware development challenges during the pandemic due to component shortages but shipped its first server last year.

The compute sleds include all the necessary components, including CPUs, memory, storage, and networking. A custom switch facilitates communication via external PCIe to an adjacent compute sled. The networking is connected directly to the switch over Ethernet.

Some innovations include a stripped-down service processor that handles power, serial console, and environmental monitoring. Traditional servers do this via their baseboard management controllers, which often include firmware and components that customers don’t need.

Oxide has slashed power supplies and installed a DC busbar at the back of the rack that distributes power to compute sleds. This improves power efficiency. A control plane facilitates the functionality of hardware and components in the system.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)