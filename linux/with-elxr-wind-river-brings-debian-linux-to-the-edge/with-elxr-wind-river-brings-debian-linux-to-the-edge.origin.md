# With eLxr, Wind River Brings Debian Linux to the Edge
![Featued image for: With eLxr, Wind River Brings Debian Linux to the Edge](https://cdn.thenewstack.io/media/2024/08/ce349d59-elxr-1024x683.png)
Long-time embedded systems provider [Wind River Software](https://www.windriver.com/) has launched an enterprise-grade [Linux](https://roadmap.sh/linux) distribution aimed for a new generation of edge deployments.

Rather than upgrade the company’s [Wind River Linux](https://www.windriver.com/products/linux) distribution, which has been for the past 20 years tailored for traditional embedded systems (notably telecommunications), Wind River engineers built a new distro to match emerging cloud native environments with heterogenous, computationally limited edge computing devices running in remotely placed devices.

The distro, called [eLxr](https://usw2.nyl.as/t1/283/3jyu8ygrh1j1sc37a8yofh1kn/10/8f56c2943b0cc46647a279257325aa02b409f6516a42a5cecce8a2c7d370b665), will be based on Debian but will also include advanced features as over-the-air (OTA) updates, [software bills of materials (SBOMs)](https://thenewstack.io/a-good-sbom-is-hard-to-find/), edge processing, predictive maintenance and data aggregation. The distro is released under the [MIT open source license](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/).

And rather than overseeing the project itself, Wind River’s plan is to have eLxr be community driven.

“Edge-to-cloud” is how Wind River principal technologist [Mark Asselstine](https://www.linkedin.com/in/mark-asselstine-88b3367/?originalSubdomain=ca) described the goals of the project to The New Stack (TNS).

The distribution aims to cut down on the fragmentation of the edge computing market, where large organizations have collected countless software and hardware variants that all must be managed independently, and, as a result, not that efficiently. A single unified stack for both edge devices and the cloud servers that support them could simplify management considerably.

The idea behind eLxr was “how can we approach it differently so that you could have one supplier and one operating system that could cover both cases, from from the edge all the way into your servers,” Asselstine said.

Asselstine introduced the distribution last week at the [DebConf](https://usw2.nyl.as/t1/283/3jyu8ygrh1j1sc37a8yofh1kn/11/ac7384b252db4c31af258a49acb502950007a7f08859ded708692c4ca52688b3) in Busan, South Korea, in a [technical presentation](https://gemmei.ftp.acc.umu.se/pub/debian-meetings/2024/DebConf24/debconf24-337-a-unified-approach-for-intelligent-deployments-at-the-edge.av1.webm).

## Origins of eLxr
eLxr sprang from another Wind River Linux Project, [StarlingX](https://www.starlingx.io/), a cloud native Linux-based distribution. An[ OpenInfra Foundation Project](https://www.openstack.org/), StarlingX has found a home in many large telecommunications providers, which use it to manage thousands of nodes on their 5G networks.

StarlingX was originally based on [Red Hat](https://www.openshift.com/try?utm_content=inline+mention)‘s CentOS. But Red Hat[ changed that distribution](https://thenewstack.io/red-hat-deprecates-linux-centos-in-favor-of-a-streaming-edition/) to a [streaming model](https://thenewstack.io/havent-migrated-off-centos-yet-you-have-until-june-30/), where updates are installed as soon as they are available.

StarlingX was not prepared to move to a streaming model, given the instability of rapid updates, so the decision was made to move the base to Debian.

The development team found that [Debian](https://thenewstack.io/build-a-debian-deb-file-from-your-projects-source/) would be a suitable base for running edge devices. [Debian](https://www.debian.org/) has been issuing stable releases for 30 years and was not controlled by a corporate entity with its own agenda.

After migrating StarlingX to Debian, Wind River’s dev team wanted a Linux distro for “edge-to-cloud” operations.

For Wind River, edge devices are not only switches, routers, multiplexors and other networking gear, but the whole expanse of industrial and retail embedded devices. This would include everything from point-of-sale machines to medical devices: Anything with internet connectivity and a bit more computational power than a bare-bones programmable logic circuit (PLC).

These edge systems have more constraints than a cloud server. They may be run in low-power environments, or be limited in CPU power or memory. Connectivity and bandwidth may be limited, which could truncate any window for applying security updates.

“Most binary Linux distributions aren’t necessarily solving for the problems with edge devices,” Asselstine said in his talk.

Another differentiator for eLxr is it will rely heavily on modern build and runtime tools, such as [Docker](https://www.docker.com/?utm_content=inline+mention) and [GitLab](https://about.gitlab.com/?utm_content=inline+mention).

Asselstine hopes that such cloud native tooling may also bring in a set of younger set contributors. As TNS freelance reporter
[Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/) has pointed out elsewhere, open source has a [graying issue](https://www.theregister.com/2024/07/15/opinion_open_source_attract_devs/) with maintainers.

“We want to get young people involved in operating systems again,” Asselstine told TNS.

## How eLxr Works
With a standard distribution like Debian, an image is installed on a device then configured for that particular environment by removing and [adding the needed packages](https://thenewstack.io/debian-retools-apt-for-superior-dependency-management/).

Because the package manager software must be installed locally, this approach does not work well for edge devices.

“When you’re deploying to an edge device, you’re not always going to have access to a package manager. Nor do you want to use a package manager to do updates,” Asselstine told TNS.

So eLxr takes the opposite approach: Developers create a manifest for building a preconfigured image, which then can be downloaded and installed.

eLxr uses [OSTree](https://ostreedev.github.io/ostree/introduction/) to update packages as atomic commits. So, in your build system, you can commit a single package, such as [systemd](https://thenewstack.io/unix-greatest-inspiration-behind-systemd/) or libc, to be updated. “The manifest will let you include only what you need,” Asselstine said.

In the future, eLxr will have some sort of support for SBOMs although the team is still working out what this will entail. They are reviewing what work Debian has done. Their goal is to have a SBOM delivered when the user’s final image is created.

## Building eLxr From Source
Wind River engineers were able to use the [Yocto Project](https://usw2.nyl.as/t1/283/3jyu8ygrh1j1sc37a8yofh1kn/8/b7800902d2d7cdb166fb16abd424cc1950c8c5d7d00a8aadd005ff1147f282dc) and [Buildroot](https://usw2.nyl.as/t1/283/3jyu8ygrh1j1sc37a8yofh1kn/9/3616e3de5686889026350160d6c05e8d79ffc15d2c8bba9a9fbda0df7add778f) to assemble the distribution and to generate a software development kit (SDK) for a cross-platform toolchain.

The Yocto project, started by Wind River and Intel in 2011, can be thought of as a distribution builder, providing a way to users to build a custom image from source. It can even produce an SDK for the distro it generates.

Yocto was perfect for building operating systems for customized environments. The downside was that it requires a lot of work to build a distribution. eLxr can streamline that process significantly.

eLxr will have a “upstream first” release policy. It follows the [Debian release cycle](https://wiki.debian.org/DebianReleases), with its releases expected to appear a few months after Debian’s.

Currently, eLxr is built on [the most recent](https://wiki.debian.org/DebianReleases) Debian “Bookworm” release, and when Debian releases the next version, “Trixie,” eLxr will follow with its own release within three to four months.

Core engineers will do their preparation work on the test releases of Debian, allowing them to contribute back to the Debian community with their features and fixes.

## eLxr for the Community
Discussion is still underway for how to establish long-term and commercial support for eLxr.

Wind River is still working out how to build rLxr as a true community-led project, sorting out the details on things like governance and contributor models.

But overall, the idea is “Wind River doesn’t have to control the project in order for us to benefit from it,” Asselstine said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)