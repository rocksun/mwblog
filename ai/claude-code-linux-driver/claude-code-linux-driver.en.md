Christian Schaller, a Red Hat engineering director and longtime GNOME and Fedora contributor, had a box of old family negatives to digitize and a scanner that wouldn’t talk to Linux. He’d bought the Plustek OpticFilm 8200i because it was listed as supported, then discovered that the manufacturer had swapped in a chipset no Linux driver recognized. He tried getting Claude Code to produce a working driver and got nowhere for a long time, so he eventually set the project aside for a few months.

When he returned to the project, [Schaller](https://www.linkedin.com/in/cschalle/) tried a different approach. Within hours, he had his first recognizable scan. A few days later, the driver supported infrared scanning, too.

Schaller has since [released the underlying approach as an open-source project called hw-harness](https://github.com/cschalle/hw-harness) under an MIT license. It bundles the tooling for capturing how a device behaves, comparing a working implementation against a broken one, and giving a coding agent the information it needs to work on hardware that Linux doesn’t support yet.

## Reverse-engineering the scanner driver

Schaller got the idea from a [post](https://x.com/GloriousEggroll/status/2103816580966830314) on X by Tom Crider, better known as Glorious Eggroll, who had used an AI agent to fix a mouse driver by giving it access to a Windows machine. Schaller fed the post to Claude and asked it to build a similar setup for his scanner.

In his [account on Wednesday](https://blogs.gnome.org/uraeus/2026/10/15/aiandreverseengineerhardware/), Schaller described the painstaking process of piecing together undocumented device protocols from USB captures, register values, and control transfers. Although the work isn’t very complicated, he said, it “takes a lot of patience and skills.” His earlier attempts to build a SANE backend with Claude had stalled because the agent had no working driver to compare against.

With the new setup, Claude could run the manufacturer’s Windows software, capture the USB traffic, and compare it with what his Linux driver was sending. It used the Windows driver as a reference to find where the Linux implementation went wrong and make changes accordingly.

> As Schaller put it, Claude “doesn’t get bored.”

Schaller thinks improvements to Claude Code itself may also have helped. Better yet, as Schaller put it, Claude “doesn’t get bored.” He still had to test the changes on the scanner, since a working driver is a different challenge from generating code that looks correct.

By the time Schaller finished, his driver was no longer the only option. Support for the newer OpticFilm 8200i had landed in SANE back in September, courtesy of another developer. “It happens sometimes,” he wrote. Schaller isn’t planning to maintain a competing driver, saying he’ll switch to the upstream version when it has the features he wants and keep his own as a proof of concept.

## A faster SANE scanner driver

His implementation does have a few advantages. It supports infrared dust removal and exposure adjustments for dense negatives, plus color and grayscale scanning at 300 to 7,200 dpi. The hardware difference that started the whole project was a chipset swap: newer 8200i scanners use a Genesys GL128, replacing the GL845 already supported by SANE.

Schaller also [put the two drivers through a single-frame test](https://htmlpreview.github.io/?https://github.com/cschalle/OpticFilm8200i-sane/blob/main/docs/comparison/drivers-comparison.html). His finished a full-resolution scan in 34.6 seconds; the upstream version took 54.4 seconds. Both resolved the same detail at 3,600 dpi, though SANE supports more resolution options. It’s a limited comparison, but Schaller came away with a working driver and a method he could apply to other hardware.

The scanner project also gave Schaller a reason to build an app of his own. He called it [Negative Vibes](https://github.com/cschalle/negative-vibes), written in Rust with Claude’s help, the GNOME app keeps the original 16-bit scan data intact, including the infrared channel. From there, users can remove dust, adjust images without altering the originals, calibrate colors with ArgyllCMS and export the results as TIFF, JPEG, PNG or DNG files.

> He called it Negative Vibes, written in Rust with Claude’s help, the GNOME app keeps the original 16-bit scan data intact, including the infrared channel.

## Fixing the ThinkPad camera

Schaller also had a problem with the camera on his Lenovo ThinkPad X1 Carbon Gen 14 Aura Edition. Under Linux, images came out too dark, with noticeably darker corners and a yellow-green tint. The laptop uses a Sony IMX471 sensor and Intel’s IPU7 imaging system, but unlike the scanner, its internal MIPI camera didn’t have USB traffic for Claude to examine.

He worked around that by feeding Claude the Windows driver’s configuration files, registry entries, ACPI tables, and device properties. He also hooked up a USB webcam to give it a working camera to compare against. That turned out to be the key. By the end of the day, he had patches for the Linux kernel and libcamera.

The [kernel fixes](https://cschalle.github.io/mipi-fixes-x1-aura/) addressed three problems: a crop-selection bug that made libcamera use the wrong pixel area, an incorrectly defined test-pattern register, and an analog gain limit that was costing the camera roughly 1.8 stops of sensitivity. Claude also found problems in libcamera’s image processing. Missing lens-shading correction left the corners about 2.7 stops darker than the center, while a mismatch in how sensor data and black levels were calculated threw off the white balance.

The difference was measurable. In Schaller’s low-light test, frame brightness rose from 31.1 to 90.9, and the color ratios moved much closer to the reference webcam.

There’s still work to do. In low light, the blue channel remains about 17% below the reference, and neither set of patches has been merged. AI developer technology engineer at Nvidia, [Kate Hsuan](https://www.linkedin.com/in/kate-cheng-26051420b/), is reviewing the kernel changes, while principal software engineer at Red Hat, [Wim Taymans](https://www.linkedin.com/in/wim-taymans-6a4a099/) is handling the libcamera work. A separate Claude-generated Linux page-cache fix [recently ran into a race condition during review](https://thenewstack.io/torvalds-claude-code-kernel/).

Schaller has since [published hw-harness on GitHub](https://github.com/cschalle/hw-harness). He notes that the released version isn’t the exact tooling he used for the scanner and camera projects. Instead, the setup runs the manufacturer’s Windows driver in a KVM virtual machine, with the physical device passed through to the guest. Claude operates the Windows session remotely while `usbmon` captures traffic on the Linux host. The developer then switches the device back to Linux, repeats the operation with the experimental driver and has Claude compare the traces.

The repository includes `winctl` for controlling the Windows VM, `usbcap` for capturing traffic, `hostdev` for switching devices between host and guest, and `hwdbg` for Linux-side debugging. PowerShell scripts collect device descriptors, registry entries, ACPI tables, and INF files.

He says the approach can produce a driver that “a maintainer can actually merge.” Licensing questions remain, and the generalized harness hasn’t yet been tested across a broad range of hardware.

> He says the approach can produce a driver that “a maintainer can actually merge.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)