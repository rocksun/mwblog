# Microsoft Open Sources OpenVMM Rust-Powered VM Monitor
![Featued image for: Microsoft Open Sources OpenVMM Rust-Powered VM Monitor](https://cdn.thenewstack.io/media/2024/10/c0437f19-pawel-czerwinski-4vkaa4ovycm-unsplash-1024x683.jpg)
There’s a new virtual machine monitor (VMM) in town: [OpenVMM](https://github.com/microsoft/openvmm). This new open source, cross-platform, modular VMM represents a step forward in Microsoft’s commitment to [open source technologies](https://thenewstack.io/open-source/) and secure, efficient virtualization solutions.

Of course, there are many VMMs. Hyper-V, QEMU, and VirtualBox all quickly come to mind. What’s different about OpenVMM is that it’s written in Rust. That’s important because, as [Joe Stocker](https://mvp.microsoft.com/en-US/mvp/profile/f9cb9fdd-37e8-ea11-a814-000d3a8dfe0d), CEO of [Patriot Consulting](http://www.PatriotConsultingTech.com), a Microsoft security company, wrote on Twitter, “[Rust is more secure than C or C++](https://x.com/ITguySoCal/status/1847101065268744345) because its ownership model and borrow checker enforce strict compile-time memory safety and concurrency guarantees, preventing common vulnerabilities like null pointer dereferencing, buffer overflows, and data races.”

OpenVMM is designed to operate on various operating systems, showcasing Microsoft’s dedication to cross-platform compatibility. The project, available on GitHub under the [MIT license](https://opensource.org/license/mit), supports a wide range of architectures and virtualization APIs, making it a versatile and powerful tool for developers and system administrators alike.

Primarily developed as a component of [OpenHCL, Microsoft’s new open source paravisor](https://thenewstack.io/microsoft-open-sources-openhcl-a-linux-based-paravisor/) for confidential computing VM. OpenVMM enables hardware-backed confidential VMs and supports existing operating systems without modifications. It can also manage conventional VMs.

## Confidential VMs
Specifically, for OpenHCL, OpenVMM supports virtual operating system guests with assigned devices and provides device translation support. Additionally, it allows users to share confidential and non-confidential architecture and guests. In both cases, the VMM provides the same services tailored to each requirements. This, according to Microsoft’s Caroline Perez-Vargas [in a blog post](https://techcommunity.microsoft.com/t5/windows-os-platform-blog/openhcl-the-new-open-source-paravisor/ba-p/4273172), “avoids fragmented virtualization solutions among confidential and non-confidential VMs, moving towards closing the feature gaps of confidential VMs.”

However, it’s important to note that OpenVMM is still in its early stages. Microsoft has been transparent about the project’s current limitations, stating that it’s not yet ready for production use. The company describes it as “more akin to a development platform for implementing new OpenVMM features, rather than a ready-to-deploy application.”

## Early Stages
Specifically, [“not a lot of “polish” has gone into making the experience of running OpenVMM](https://github.com/microsoft/openvmm/blob/main/Guide/src/user_guide/openvmm.md#disclaimer) in traditional host contexts, particularly “pleasant. This lack of polish manifests in several ways, including but not limited to:

- Unorganized and minimally documented management interfaces (e.g., CLI, ttrpc/grpc)
- Unoptimized device backend performance (e.g., for storage, networking, graphics)
- Unexpectedly missing device features (e.g., legacy IDE drive, PS/2 mouse features)
- No API or feature-set stability guarantees whatsoever.
In short, you can use OpenVMM without too much pain in Azure and in partnership with OpenHCL. For any other uses, though, you’ll be pretty much on your own.

That said, OpenVMM could become a significant player in the [virtualization ecosystem](https://thenewstack.io/how-one-small-startup-is-changing-the-virtualization-landscape/). But make no mistake about it: we’re in the very early days of making OpenVMM a generally useful hypervisor. For the specific use case of running both confidential and run-of-the-mill VM workloads, OpenVMM demands your attention.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)