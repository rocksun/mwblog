# Choosing a Linux Distribution
![Featued image for: Choosing a Linux Distribution](https://cdn.thenewstack.io/media/2024/05/1b25004d-penguins-352080_1280-1024x682.jpg)
[series of Linux articles](https://thenewstack.io/tns-linux-sb00-1-intro-to-the-linux-skill-blocks-repository/")covering various sysadmin topics. You can [review Linux commands](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line)or build a lab environment by following the information in the [Linux: Companion Lab for Linux Skill Blocks Repository](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/)piece.
Unlike Microsoft Windows and Apple macOS, Linux is available in thousands of variations that are supported by communities and businesses worldwide. These versions are called distributions, and they offer you far more options than other operating systems provide.
This tutorial discusses Linux distributions before providing a variety of examples for you to download and try yourself. Remember, Linux is free of charge, so you can try as many distributions as you want!
This article doesn’t provide technical configurations. Instead, it discusses your options for selecting one or more versions of Linux to use. The following articles in the series discuss your hardware choices before getting into the actual installation process.
## How Open Source Licensing Enables So Many Distributions
[Open source licensing](https://thenewstack.io/a-guide-to-leveraging-open-source-licensing/) can be a bit of a mystery to Windows and macOS users. The gist is that anyone is free to modify open source code and release their modifications (to potentially be modified more by other users). In the case of Linux, that means anyone can create their own Linux version, custom-made to their needs or whims.
And not only
*can* users make their own Linux versions, but many actually *do*. Furthermore, companies release their own Linux versions and may even provide technical support plans and additional applications.
Linux distributions are the result of building your own Linux version. Distributions (often simply called “distros”) are usually purpose-specific. After all, they were created by someone for a reason — perhaps graphic design, security audits, gaming, or day-to-day internet use. Distros typically include the necessary software to accomplish the purpose or goal of that particular Linux version. Thousands of Linux distributions exist today.
Take a few minutes to browse the
[Distrowatch website](https://distrowatch.com/) for a list of the most popular Linux distributions and news related to recent releases.
## What Is a Linux Distribution?
Why are there so many Linux distributions available? What makes them different and unique? Linux distros are typically created to fill a need.
Linux distribution characteristics include the following:
- Linux kernel + open source applications.
- Specific target audience and goals.
- Retains an individual release cycle.
- Some are commercially backed, and others are community-supported.
Linux distributions are complete operating systems with applications tailored to meet a specific need or goal.
Possible goals of Linux distros:
- Home user operating system.
- Engineering, science, or graphics workstation.
- Network devices, such as a web server, file server, or virtual machine host.
- Security audit and penetration testing workstation.
The creator of a new distribution typically wants to use the OS and applications to accomplish a task. They are careful to configure the system with the necessary services and applications for that purpose. Just as importantly, they do not include any extra components that might make the OS bloated or introduce unanticipated security problems.
This approach differs from that of Microsoft Windows and Apple macOS. Those operating systems tend to be much more generic rather than purpose-specific and often include far more software than users need.
## Identify Common Linux Distributions
If there are thousands of Linux distributions to choose from, how does one get started? Many distros have a reputation for ease of use and include the general software most users want. It’s usually best to begin with one of those. As you gain experience, you can experiment with other distros. After all, Linux distributions are free, so you can try as many as you want!
The following descriptions outline some common or well-known Linux distributions.
### Ubuntu Linux
[Ubuntu Linux](https://ubuntu.com/desktop) is derived from another distribution named [Debian](https://www.debian.org/) (another great choice). Ubuntu is very user-friendly and offers a [great place to start](https://thenewstack.io/ubuntu-pro-tackles-the-challenge-of-enterprise-open-source-adoption/) with Linux. It’s highly customizable and receives regular security and feature patches. It’s a great desktop operating system for any user. Ubuntu also offers server and other business-oriented versions.
### Fedora Linux
[Fedora Linux](https://fedoraproject.org/workstation/) is where [Red Hat ](https://www.openshift.com/try?utm_content=inline+mention)tests news features for its Red Hat Enterprise Linux. Fedora focuses on innovative features, security enhancements, and a user-friendly interface. It installs on a wide range of hardware and offers a rapid release cycle, providing users with cutting-edge features. Like Ubuntu, Fedora has various specialized versions to meet any need.
### Linux Mint
[Linux Mint](https://www.linuxmint.com/) is a derivative of Ubuntu that offers many desktop environments and [strong community support](https://thenewstack.io/tutorial-install-linux-mint-on-a-windows-laptop-using-a-usb-stick/). It is stable and customizable. Unlike Fedora and Ubuntu, Linux Mint is not backed by a commercial entity. It’s a great choice for new Linux users and well worth downloading.
### Red Hat Enterprise Linux
[Red Hat Enterprise Linux](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) (RHEL) is a server operating system that supports powerful, scalable, high-performance workloads. It does not include common end-user applications like media players; instead, it offers network services, container management, automation and orchestration software, and more. RHEL emphasizes business requirements.
Red Hat offers a robust training and certification platform, as well as technical support. If you intend to work as a Linux administrator, you’ll likely encounter RHEL.
### SUSE Linux Enterprise Server
[SUSE Linux Enterprise Server](https://www.suse.com/products/server/) is another server Linux operating system. It offers high reliability and flexibility in providing enterprise resources, including virtualization, containerization, and cloud integrations. SUSE offers technical support—a critical feature for business environments. The company also supports various end-user Linux deployments.
Enterprise Linux solutions often come bundled with additional software and vendor tech support options that are not free.
### Kali Linux
[Kali Linux](https://www.kali.org/) is also a Debian derivative. It is a great example of a purpose-specific distro. Kali serves as a [security auditing and penetration testing platform](https://thenewstack.io/how-kali-linux-can-help-security-test-your-network/). It comes preinstalled with the necessary tools and services to discover, exploit, and correct the security configurations of business environments. As such, Kali is a not a great place to begin with Linux. It assumes more advanced knowledge and experience. ![](https://cdn.thenewstack.io/media/2024/05/35ec9253-kali2023.png)
## How Does Software Management Impact Distros?
One of the first differences you’ll notice between distributions is the graphical user interface (GUI). Linux supports many different GUIs, meaning the desktop environment varies much more with Linux than with Windows or macOS. However, you’ll probably find that software management is the biggest practical difference.
The two main ways of installing, updating, and removing software trace their origins back to the original Debian and Red Hat distributions of the early 1990s. Many of today’s most popular distributions use either the Debian or Red Hat approach to managing software.
The Debian approach typically uses the apt command to install, update, or remove software. The Red Hat method uses the dnf command to accomplish the same goals. There are other software management techniques, but these two are the most used.
Distributions that use the Debian approach include:
- Debian
- Ubuntu
- Mint
- Kali
![](https://cdn.thenewstack.io/media/2024/05/ead7f6b4-apt-small.png)
Distributions that use Red Hat’s approach include:
- Fedora
- Red Hat Enterprise Linux
[Rocky Linux](https://thenewstack.io/start-developing-with-rocky-linux-as-a-docker-container/) ![](https://cdn.thenewstack.io/media/2024/05/dd0756f5-dnf-small.png)
Other software package managers exist, but the Red Hat and Debian approaches are the most common.
## Which Distribution Is Best for You?
If you’re new to Linux, consider beginning with Ubuntu, Fedora, or Mint. These distributions are well-developed and supported. They contain applications you’ll probably want, such as web browsers, office productivity, and music streaming apps. They are flexible enough to be installed on many types of hardware.
If you’re more familiar with Linux, you might investigate server-oriented distributions like RHEL or SUSE Enterprise. Ubuntu also offers a server version. These are good choices if your career goals include Linux administration or you’re pursuing Linux certifications.
Security folks are probably already aware of
[Kali Linux](https://thenewstack.io/how-kali-linux-can-help-security-test-your-network/). Kali is not as user-friendly as other distributions, so I don’t recommend beginning with it. Other advanced security distros include [BlackArch](https://www.blackarch.org/) and [Parrot Linux](https://www.parrotsec.org/).
Another interesting alternative is the Linux distribution created specifically for the
[Raspberry Pi](https://www.raspberrypi.com/) hardware. Raspberry Pi devices are surprisingly powerful microcomputers often used with a variety of different Internet of Things projects. The company offers a variation of the Debian Linux distro called the [Raspberry Pi OS](https://www.raspberrypi.com/software/) (formerly called Raspbian) to manage Pi systems.
Evaluate your goals and needs when selecting a distribution, and don’t be afraid to explore. It takes time to settle on a preferred Linux system.
Here are a few ideas of what you might use Linux for to get you started:
- Learn
[Python programming](https://thenewstack.io/what-is-python/).
- Learn to manage Linux software.
- Set up a web server or file server.
- Stream multimedia to your TV or stereo.
- Create a smart mirror.
## Wrap Up
Those more familiar with Windows and macOS will be surprised by the freedom of choice Linux offers. In fact, the options may be a little overwhelming at first. Thousands of distros exist, each with its own purpose and advantages. Start simple by downloading a few of the standard, well-developed desktop versions, such as Ubuntu and Fedora. One of the easiest ways to do this is by using virtualization. Using a host system with virtual machines allows you to run several Linux distributions on a single piece of hardware. Another alternative is an older computer you might have lying around.
In addition to finding an easy Linux distribution, consider your purpose for using Linux. You may be embarking on a journey to learn
[Python](https://thenewstack.io/set-up-python-on-fedora-linux-4-steps/) or another programming language. Or maybe you’re sharpening your penetration testing skills as you pursue a new position at work. Whatever your goal, there’s a Linux distribution available to help. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)