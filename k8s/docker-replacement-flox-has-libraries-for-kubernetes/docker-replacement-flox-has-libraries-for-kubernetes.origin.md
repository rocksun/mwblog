# Docker Replacement Flox Has Libraries for Kubernetes
![Featued image for: Docker Replacement Flox Has Libraries for Kubernetes](https://cdn.thenewstack.io/media/2025/01/c7fe7be5-capture-decran-2025-01-10-201516-1-1024x575.png)
The [startup Flox](https://thenewstack.io/flox-gears-up-nix-for-the-enterprise/) has demonstrated how its adaptation of [Nix](https://thenewstack.io/flox-gears-up-nix-for-the-enterprise/) can serve as a viable alternative to [Docker](https://thenewstack.io/when-webassembly-replaces-docker/), making it worth a closer look. While Nix has been around for years and is known for its complexity, Flox has simplified its use and adoption. More recently, Flox has positioned its version of Nix as a potential replacement for Docker containers on [Kubernetes](https://thenewstack.io/kubernetes/).

[Flox](https://flox.dev/) is described as an environment and platform for both developers and operations teams, offering reproducibility and app deployment in a cross-platform way. However, it achieves consistency across different environments, and can leverage Flox, which incorporates the best features of Nix, making it much more accessible and simplifying the use of Nix environments.
The [Nix store](https://nixos.org/) operates differently from traditional OCI registries. While OCI registries function effectively, their [container](https://thenewstack.io/containers/) layers rely on hierarchical file systems. In such systems, altering one layer invalidates all subsequent layers. The Nix store, by contrast, offers many derivations within the Nix store — with over 120,000 of what Flox calls “Nixpkgs packages.” They may consist of single files or shell scripts, which helps to avoid unnecessary invalidations.

Open source Nix can replace containers and

[@Docker], and now extends to[@kubernetesio]says[@floxdevelopment]‘s Leigh Capili at[@rejektsio].[@thenewstack][pic.twitter.com/cECa6woCrg]— BC Gain (@bcamerongain)

[November 11, 2024]
For instance, when setting up a dependency tree for .sh, only a small number of related files are required. These files can then be reused across various projects, delivering a much finer resolution in dependency management compared to container-based systems.

## Cloud Native Nix
As Flox’s [Leigh Capili,](https://www.linkedin.com/in/leighcs/) senior DevRel engineer and Kubernetes contributor, explained during his talk “Cloud Native Nix!” at Cloud Native Rejekts in November, a cloud native individual — someone who already benefits from container images and runtimes — would be interested in packaging software in a way that ensures it only accesses what it needs. Let me contextualize the significance of such an approach.

This environment makes it easy to list what software I’m using from the Nix packages ecosystem. Flox is an open source project we’ve built to make it easier to understand how to use these packages. For example, I can list the software in my home directory, showing the packages I want installed on my system. You’ll see tools like [zsh](https://www.zsh.org/), my favorite text editor, and utilities for terminal tasks.

Typically, software is developed to function, pass tests and be packaged into a container image that can be uploaded to a registry.

However, one compelling reason to rethink packaging arises when using a MacBook, Capili said. MacBooks feature advanced kernels, like the Darwin kernel, which is also used on iPhones. While the Darwin kernel provides impressive isolation features, it cannot currently run OCI containers in the desired way. Although there is an intriguing Darwin containers project that could potentially support this in the future, Capili explained, it is not yet widely adopted.

In order to package and use the desired software as cloud native professionals, Capili said users often rely on tools like Docker, [Podman](https://thenewstack.io/whats-new-with-podman-5-multiplatform-images-vm-support/) or [nerdctl](https://thenewstack.io/containers/how-to-deploy-containers-with-nerdctl/) to access a daemon running on a Linux environment. Interestingly, the vast majority of software in modern Nixpkgs packages are cross-built on public build farms. These are then stored in a binary cache hosted on a 1.5-petabyte instance. This setup makes the software available natively for macOS, reducing the need to run virtual machines as frequently, which is a significant advantage, Capili said.

During his presentation, Capili explained why a cloud native user, who already benefits from container images and runtimes, would be interested in packaging software in a way that ensures it only accesses what it needs. “The goal is to contextualize the significance of such an approach,” Capili said.

As Capili explained, typically, software is developed to function, to pass tests and to be packaged into a container image that can be uploaded to a registry. With this approach, there seems little reason to reconsider habits, Capili said. Modern tools allow the creation of a working artifact that can be stored indefinitely and deployed on platforms such as Functions as a Service, Kubernetes clusters or even Docker Desktop. This workflow appears sufficient to meet most needs, Capili said.

“Let’s say we want to add more infrastructure-related tools. I could install these packages easily, though I might need to pull a new version,” Capili said. “Ultimately, we want to look at the runtime directory, where my configuration files, binaries and other system components all point to symlinks in my Nix store.”

To fulfill these tasks, there are many different types of software inside the Nix store. Every build happens in a sandboxed environment with network access locked down. The system clock is pinned to ensure outputs are bit-for-bit identical across builds. “This makes it possible to trust that recipes will produce consistent results, enabling us to cache binaries efficiently,” Capili said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)