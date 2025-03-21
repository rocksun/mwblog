# NixOps Lives On: Introducing NixOps 4
![Featued image for: NixOps Lives On: Introducing NixOps 4](https://cdn.thenewstack.io/media/2025/03/2cd596d3-tim-hufner-fobq12oj6sy-unsplash-1-1024x683.jpg)
[Nix](https://nixos.org/) has been a work in progress for over a decade. Some say it will never live up to its promise of completely reproducible environments and workloads, along with the work that goes into [NixOS](https://thenewstack.io/nixos-a-combination-linux-os-and-package-manager/) as the associated [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) distribution.
However, immense progress has been made. The fact that the project has been ongoing for so long attests to both the strong interest in the community and its prevailing certitude that, yes, it can be done in theory. While it is very difficult to achieve, significant advancements have been made. This is evident, for example, in [Flox](https://thenewstack.io/docker-replacement-flox-has-libraries-for-kubernetes/), which was built on top of Nix. Flox aims to improve usability and deployment, and it has demonstrated the ability to replace [Docker](https://thenewstack.io/revised-docker-hub-policies-unlimited-pulls-for-all-paying-customers/) functionalities for a wide variety of applications, leading to a significant increase in demand.

## NixOps Saga
Then, there is [NixOps](https://releases.nixos.org/nixops/nixops-1.5.1/manual/manual.html), the deployment and management platform for NixOS. It provides [Infrastructure as Code](https://thenewstack.io/introduction-to-infrastructure-as-code/) (IaC) functionality, enabling users to deploy and manage NixOS systems and applications programmatically. However, the initial versions of NixOps faced significant challenges, and for a time, it was considered essentially dead.

Now, NixOps has been revived. The latest iteration, [NixOps 4](https://github.com/nixops4/nixops4), was discussed during the [FOSDEM](https://fosdem.org/2025/) event held in Brussels earlier this year. The session covered lessons from past failures and key takeaways on what not to do. Here’s what the NixOps team had to say.

“NixOps failed…but NixOps4 creators and maintainers have learned from past mistakes,” said Robert Hensing, during his

[@fosdem]talk « NixOps4: new, sustainable platform for deployment technology. »[@thenewstack][pic.twitter.com/nBTBow9AE9]
— BC Gain (@bcamerongain),[February 1, 2025]
As NixOps used to be the only Nix-native deployment and provisioning tool, NixOps4 represents a “complete redesign of the tool,” with lessons learned from NixOps and the help of its original maintainers, [Robert Hensing,](https://www.linkedin.com/in/rhensing/?originalSubdomain=nl) co-founder at Hercules CI and a member of the Nix Community steering committee, said. NixOps4 was also inspired by [Terraform.](https://opentofu.org/)

“In our current project, we’re using NixOps in much the same way we have been so far,” Hensing said during his talk at FOSDEM. “There are also some resource limitations and questions to consider,” Hensing said.

One key question is whether the NixOps state lifecycle will become overly cumbersome, Hensing said. “It might be a bit early to fully assess its ecosystem, as I’ve spent considerable time ensuring that resource state is managed correctly,” Hensing said. “I haven’t completely decided on that yet.”

NixOS was selected by [Doctors Without Borders (MSF)](https://www.msf.org/) due to the complexity of its operations. As [Sohel Sarder](https://www.linkedin.com/in/sohel-sarder-84a5379a/), a DevOps engineer for Doctors Without Borders, said during his talk at FOSDEM, “[NixOS @ Doctors Without Borders (MSF) — Why We Use It and How](https://fosdem.org/2025/schedule/event/fosdem-2025-5165-nixos-doctors-without-borders-msf-why-we-use-it-and-how/)“: “Our complex IT operations needs a system that is a robust and resilient, and we wanted the system that can evolve quickly by itself, with minimal maintenance. And also we wanted a system that the same system can run both for our field operations management and headquarter operation management. So there we select NixOS as it supports for declarative configuration management and Infrastructure as Code.”

## The Flox Flex
The startup Flox has demonstrated how its adaptation of Nix can serve as a viable alternative to Docker, making it worth a closer look. While Nix has been around for years and is known for its complexity, Flox has simplified its use and adoption. More recently, Flox has positioned its version of Nix as a potential replacement for Docker containers on Kubernetes.

Flox is described as an environment and platform for both developers and operations teams, offering reproducibility and app deployment in a cross-platform way. However, it achieves consistency across different environments and can leverage Flox, which incorporates the best features of Nix, making it much more accessible and simplifying the use of Nix environments.

The Nix store operates differently from traditional OCI registries. While OCI registries function effectively, their container layers rely on hierarchical file systems. In such systems, altering one layer invalidates all subsequent layers.

The Nix store, by contrast, offers many derivations within the Nix store, with more than 120,000 of what Flox calls Nixpkgs packages. They may consist of single files or shell scripts, which helps to avoid unnecessary invalidations.

For instance, when setting up a dependency tree for sh, only a few related files are required. These files can then be reused across various projects, delivering a much finer resolution in dependency management compared to container-based systems.

## Cloud Native Nix
As Flox’s [Leigh Capili,](https://www.linkedin.com/in/leighcs/) senior DevRel engineer and Kubernetes contributor explained during his talk, “Cloud Native Nix!” at [Cloud Native Rejekts](https://www.linkedin.com/posts/the-new-stack_cloud-native-rejekts-na-2024-activity-7257357682527907840-bii5/) last November, a cloud native individual — who already benefits from container images and runtimes — would be interested in packaging software in a way that ensures it only accesses what it needs. The goal is to contextualize the significance of such an approach.

This environment makes it easy to list what software I’m using from the Nix packages ecosystem. Flox is an open source project we’re building to make it easy for me to demonstrate how to use these packages. For example, I can list the software in my home directory, showing the packages I want installed on my system. You’ll see tools like zsh, my favorite text editor, and utilities for terminal tasks.

Typically, software is developed to function, pass tests, and be packaged into a container image that can be uploaded to a registry. With this approach, there seems little reason to reconsider habits. “Modern tools,” Capili said, “allow the creation of a working artifact that can be stored indefinitely and deployed on platforms such as Functions as a Service (FaaS), Kubernetes clusters, or even Docker Desktop. This workflow appears sufficient to meet most needs.”

However, one compelling reason to rethink packaging arises when using a MacBook, Capili said. MacBooks feature advanced kernels, like the Darwin kernel, which is also used on iPhones. While the Darwin kernel provides impressive isolation features, it cannot currently run OCI containers in the desired way. Although there is an intriguing Darwin Containers project that could potentially support this in the future, Capili explained, it is not yet widely adopted.

To package and use the desired software as cloud native professionals, Capili said users often rely on tools like Docker, Podman, or nerdctl to access a daemon running on a Linux environment. Interestingly, the vast majority of software in modern Nixpigs packages — approximately 120,000 packages — are cross-built on public build farms. These are then stored in a binary cache hosted on a one-and-a-half petabyte instance. This setup makes the software available natively for macOS, reducing the need to run virtual machines as frequently, which is a significant advantage, Capili said.

During his presentation, Capili explained why a cloud native user, who already benefits from container images and runtimes, would be interested in packaging software in a way that ensures it only accesses what it needs. “The goal is to contextualize the significance of such an approach,” Capili said.

As Capili explained, typically, software is developed to function, to pass tests, and to be packaged into a container image that can be uploaded to a registry. With this approach, there seems little reason to reconsider habits, Capili said. Modern tools allow the creation of a working artifact that can be stored indefinitely and deployed on platforms such as FaaS, Kubernetes clusters, or even Docker Desktop. This workflow appears sufficient to meet most needs, Capili said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)