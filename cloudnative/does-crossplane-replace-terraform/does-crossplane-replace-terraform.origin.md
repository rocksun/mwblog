## What is Crossplane?
If you don't already know, Crossplane is billed as an:
Open source, CNCF project built on the foundation of Kubernetes to orchestrate anything. Encapsulate policies, permissions, and other guardrails behind a custom API line to enable your customers to self-service without needing to become an infrastructure expert.
Another way to view Crossplane is as a tool that uses a commodity, open source, and well-supported control plane (Kubernetes) to support the creation of other control planes.
We've been using it at Container Solutions for a while, and have recently been talking about how we think it's going to become more important in future:
Just as IBM buys Terraform, Crossplane seems to be becoming a default for our client engagements.— Ian Miell (@ianmiell)
This is for a few reasons, and with some caveats.
🧵
1/
[May 10, 2024]
Recently I've been watching
[Viktor Farcic's](https://www.youtube.com/@DevOpsToolkit) fantastic set of [tutorial videos on Crossplane](https://www.youtube.com/playlist?list=PLyicRj904Z99i8U5JaNW5X3AyBvfQz-16). If you are an engineer or interested architect, then these primers are ideal for finding out what's going on in this area.
While following Viktor's work I saw
[another Crossplane-related video](https://www.youtube.com/watch?v=tgwxMfIsLJY) by Viktor on a subject we both seem to get asked about a lot: does Crossplane replace Terraform/Ansible/Chef/$Tool?
This is a difficult question to answer briefly (aside from just saying "yes and no"), because understanding the answer requires you to grasp what is new and different about Crossplane, and what is not. It doesn't help that - from the user point of view - they can seem to do the exact same thing.
To get to the answer, I want to reframe a few things Viktor says in that video that confused me, in the hope that the two pieces of content taken together help people understand where Crossplane fits into the Cloud Native firmament. Although Viktor and I agree on the role Crossplane plays now and in the future, we do differ a little on defining and interpreting what is new about Crossplane, and how the industry got here.
This post follows the logic of our 'Cloud Native Family Tree', which seeks to explain the history of devops tooling. It's recently been updated to include Crossplane.
## Three Questions
Before we get into the debate, we may want to ask ourselves two deceptively simple questions:
- What is an API?
- What is a cloud service?
And one non-simple question:
- What is a control plane?
Understanding exactly what the answers to these are is key to defining what's new and useful about Crossplane.
If you think you know these already, or aren't interested in the philosophy, skip to the end.
#### What is an API?
Let's start with a definition from an
[AWS page](https://aws.amazon.com/what-is/api/):
APIs are mechanisms that enable two software components to communicate with each other using a set of definitions and protocols.
Nowadays, most people think of an API as a set of services you can call using technologies like HTTP and JSON. But HTTP and JSON (or YAML, or XML etc) are not necessary. In this context, I like to explain to people that the venerable mkdir command is an API. mkdir conforms in these ways:
- enables two software components to communicate with each other [the shell and the Linux API] using
- a set of definitions [the standard flags to mkdir] and
- protocols [shell standard input/output and exit codes]
Pretty much all code is something that calls an API, down to whatever goes on within the hardware (which, by definition, isn't a software component). Technically speaking, code is "APIs all the way down". But this isn't a very helpful definition if it essentially describes all code.
*APIs all the way down: The Linux API calls that *mkdir * makes in order to create a folder.*
It might be argued that mkdir is not an API because it is used by humans, and not for 'two software components to communicate'. However, you
*can* telnet to a server and call its API by hand (I used to do this via HTTP a lot when debugging). Further, mkdir can (and is also designed to) be used within scripts
APIs are
*Stable*
What people really want and expect from an API is
*stability*. As a rule, the lower down the stack an API is, the more stable it needs to be. The Intel x86 API has had very few breaking changes since it came into being in 1978, and even carries over idiosyncrasies from the [Datapoint 2022](https://www.righto.com/2023/08/datapoint-to-8086.html) terminal in 1970 (such as the 8086's 'little endian' design. Similarly, the Linux Kernel API has also had very few changes (mostly removals) since [version 2.6](https://en.wikipedia.org/wiki/Linux_kernel_version_history)'s release over 20 years ago (2003).
The Linux CLI, by contrast, is much less stable. This is one of the main reasons shell scripts get such a bad rep. They are notoriously difficult to write in such a way that they can be run on a wide variety of different machines. Who knows if the ifconfig command in my shell script will run in your target shell environment? Even if it's installed and on the $PATH, and not some other command with the same name, will it have the same flags available? Will those flags do the same thing consistently? Defensively writing code against these challenges are probably the main reason people avoid writing shell scripts, alongside the ease with which you can write frighteningly broken code.
This is why tools like Ansible came into being. They abstracted away the messiness of different implementations of configuration commands, and introduced the notion of idempotence to configuration management. Rather than running a mkdir command which might succeed or fail, in Ansible you simply declare that the folder exists. This code will create a folder on 'all' your defined hosts.
- hosts: all
tasks:
- name: Create a folder
file:
path: /path/to/your/folder
state: directory
Ansible will ssh into them and create the folder if it doesn't already exist, running mkdir, or whatever it needs to run to get the Linux API to deliver an equivalent result.
Viktor says that Ansible, Chef et al focussed on 'anything but APIs', and this is where I disagree. They did focus on APIs, but not http-based (or 'modern') APIs; they simplified the various command line APIs into a form that was idempotent and (
[mostly](/is-it-imperative-to-be-declarative)) declarative. Just as mkdir creates a new API in front of the Linux API, Ansible created a means to use (or create your own) APIs that simplified the complexity of other APIs.
Terraform: An Open Plugin and Cloud First Model
Terraform not only simplified the complexity of other APIs, but then added a rich and open plugin framework and a 'cloud first' model (as opposed to Ansible's 'ssh environment first' model). In theory, there was no reason that Ansible couldn't have done the same things Terraform did, but Ansible wasn't designed for infrastructure provisioning the way Terraform was (as Viktor points out).
This begs the second question: if Terraform was 'cloud first'...
#### What is a Cloud Service?
Many people think of a cloud service as something sold by one of the big three hyperscalers. In fact, a cloud service is the combination of three things:
- A remote network connection
- An API
- A delegation of responsibility to a third party
That's it. That's all a cloud service is.
We've already established that an API (as opposed to just 'running software') is a
*stable* way for two software components to communicate. Cloud simply takes this and places it on the network. Finally - and crucially - it devolves responsibility for delivering the result to a third party.
So, if I ask my Linux desktop (y'know, the one literally on my desk) for more memory, and it can't give it to me because it's run out, then that's my responsibility to resolve, therefore it's not a cloud service.
A colo is not a cloud service, for example, because the interface is not an API over a network. If I want a new server I'll send them an email. If they add an API they become a cloud service.
This table may help clarify:
|
Remote Network Connection |
API |
Delegation of Responsibility
|Abacus
|No
|No
|No
|Linux Server
|
Yes |No
|No
|mkdir CLI Command on Desktop Linux
|No
|
Yes |No
|Outsourced On-Prem Server
|No
|No
|
Yes
|Self-managed API service
|
Yes |
Yes |No
|Windows Operating System on Desktop
|No
|
Yes |
Yes
|Colo Server
|
Yes |No
|
Yes
|
AWS EKS |
Yes |
Yes |
Yes
|
GitHub |
Yes |
Yes |
Yes
- An abacus is a simple calculation tool that doesn't use a network connection, has an interface (moving beads), but not an API, and if the abacus breaks, that's your problem.
- A Linux server has a remote network connection, but no API for management. (SSH and the CLI might be considered an API, but it's certainly not stable).
- mkdir has an API (see above), but from mkdir's point of view, disk space is your problem.
- If you engage a company to supply you with an on-prem server, then it's their problem if it breaks down (probably), but you don't generally have an API to the outsourcer.
- If you build your own API and manage it yourself then you can't pick up the phone to get it fixed if it returns an error.
- If the Windows API breaks (and you paid for support), then you can call on Microsoft support, but the Windows API doesn't need a network connection to invoke.
- A colo server is supplied by you without an API, but if it doesn't get power/bandwidth/whatever else the colo supports, you can get them to fix it, and can connect to it over the network.
Some of these may be arguable on detail, but it's certainly true that only EKS and GitHub qualify as 'cloud services' in the above table, as they fulfil all three criteria for a cloud service.
#### What is a Control Plane?
A less commonly-understood concept that must also be understood is the 'control plane'. The phrase comes from network routing, which divides the router architecture into three 'planes': the 'data plane', the 'control plane', and the 'management plane'.
In networking, the data plane is the part of the software that processes the data requests. By contrast, the control plane is the part of the software that maintains the routing table and defines what to do with incoming packets, and the management plane handles monitoring and configuration of the network stack.
You might think of the control plane as the state management of the data that goes through the router, as opposed to the general management and configuration of the system (management plane).
This concept has been co-opted by other technologies, but I haven't been able to find a formal definition of what a control plane when used outside of networking. I think of it as 'whatever manages how the useful work will be done by the thing' rather than the thing that does the actual work. If that doesn't seem like a rigorous definition to you, then I won't disagree.
For Kubernetes, the control plane is the etcd database and the core controllers that make sure your workloads are appropriately placed and running.
All cloud services need a control plane. They need something that orchestrates the delivery of services to clients. This is because they have a remote API and a delegation of responsibility.
## So Does Crossplane Replace Terraform?
OK, now we know what the following things are:
- APIs
- Cloud services
- Control planes
We can more clearly explain how Crossplane and Terraform (et al) relate.
#### Resources, APIs, Cloud Services
Crossplane and Terraform both deal with the creation of resources, and are both designed to help manage cloud services. In this sense, Crossplane
*can* replace Terraform. However...
#### 'One-shot' vs Continuous
...whereas Terraform is 'one-shot' (you run it once and then it's done), Crossplane is continuous.
*Part* of its job is to provision resources, but it's not its only job. Its design, and main purpose, is to give you a framework to ensure that resources remain in a 'known state', ultimately deriving its source of truth from the configuration of its own Kubernetes control plane (or Git, if this configuration is synchronised with a Git repository).
#### Terraform 'Under' Crossplane?
If you want, you can run your Terraform code in Crossplane with the
[Terraform provider](https://marketplace.upbound.io/providers/upbound/provider-terraform/v0.16.0). One thing to note here, thought, is that you can't just take your existing Terraform code or other shell scripts and run it unchanged 'within' Crossplane's control plane just as you would have done before. Some work will need to be done to integrate the code to run under Crossplane's control. In this sense, Crossplane does replace Terraform, subsuming the code into its own provider.
#### Control Planes
In a way, Crossplane is quite close to Chef and Puppet. Both those tools had 'control planes' (the Chef and Puppet servers) that ensured the targets were in a conformant state. However, Chef and Puppet (along with Ansible) were designed to configure individual compute environments (physical servers, VMs etc), and not orchestrate and compose different APIs and resources into another cloud service-like API.
## Our Experience with Crossplane
So much for the theory. What about the practice? Our experience with Crossplane, and how it plays out in the field will be outlined in Part II...