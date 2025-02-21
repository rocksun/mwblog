# After 29 years, a veteran Microsoft Engineer admits "MS-DOS could do graphics," but the company opted for a lackluster UI — as Windows 3.1 runtime already checked the missing boxes
[News](https://www.windowscentral.com/news)
[Kevin Okemwa](https://www.windowscentral.com/author/kevin-okemwa)
Microsoft employee Raymond Chen reveals why text-based setups were so common despite MS-DOS shipping with support for graphics.

![Windows 95 virtual machine running Solitaire](https://cdn.mos.cms.futurecdn.net/wB3p4ESGaRCJYqX5FykaxN-1200-80.jpg)
##### Recent updates
**Feb. 19 @ 12:11 PM ET:*** Headline edited for acknowledgment and clarification: Windows 95's setup was not, in fact, entirely text-based but could have theoretically been built with graphics within MS-DOS alone. Original article follows.*
On August 24, 2025, Microsoft's Windows 95 operating system turns 30. Feeling old yet? Windows Central is a big fan of the operating system, often covering nostalgic bits, including its birthday, [the introduction of the Iconic Start menu into the revolutionary taskbar](https://www.windowscentral.com/software-apps/celebrating-29-years-of-windows-95), and the tale behind [the Start menu's development as a Windows 95 feature](https://www.windowscentral.com/software-apps/windows-11/microsoft-veteran-software-engineer-explains-the-development-of-the-start-menu-as-a-windows-95-feature-before-it-turned-into-a-windows-11-billboard).

As [Windows 10's imminent death looms](https://www.windowscentral.com/software-apps/windows-10/microsoft-gives-a-subtle-reminder-about-the-upcoming-death-of-windows-10) and Microsoft doubles down on its [Windows 11 campaign](https://www.windowscentral.com/software-apps/windows-11/microsoft-temporarily-pumps-the-brakes-on-its-intrusive-windows-11-ads-after-receiving-constant-backlash-from-windows-10-users) to get more users to upgrade, it's interesting that [the former still ships with many Windows 95 features](https://www.windowscentral.com/windows-95-20-years-old-today-and-windows-10-still-has-lot-its-features). But one question has remained unanswered, well up until recently. *Did the Windows 95 setup team forget that MS-DOS can do graphics?*

Veteran Microsoft Engineer Raymond Chen, who's been involved in the evolution of the Windows operating system for over 30 years, revealed why the company decided to make Windows 95 setup text-based instead of using graphics.

## Why was Microsoft's Windows 95 setup text-based?
Windows 95 stands out from the herd compared to newer Microsoft operating systems. This is quite apparent because of its lackluster user interface, which is consistent with dull text, compared to its successor operating system, which features rich graphical elements during the installation process.

Microsoft Engineer Raymond Chen revealed that "MS-DOS (Microsoft Disk Operating System) could do graphics." Why did Microsoft opt for a text-based Windows 95 instead? Despite being able to support graphics, Chen indicated that the operating system's support for graphics was primitive and time-constraining:

*"Yes, MS-DOS could do graphics, in the sense that it didn’t actively prevent you from doing graphics. You were still responsible for everything yourself, though. There were no graphics primitives aside from a BIOS call to plot a single pixel. Everything else was on you, and you didn’t want to use the BIOS call to plot pixels anyway because it was slow. If you wanted any modicum of performance, you had to access the frame buffer directly."*
The Microsoft engineer revealed that featuring graphics in Windows 95's setup would have been daunting as its primitives were limited to a BIOS call for plotting a single pixel. Chen further added that leveraging this avenue to introduce graphics to the setup wasn't a great idea because it was slow. The only way around the performance bottleneck was directly accessing the frame buffer.

## Get the Windows Central Newsletter
All the latest news, reviews, and guides for Windows and Xbox diehards.

But this was just the tip of the iceberg. The process was far more complicated, including writing a graphics library for drawing complex things than a single pixel. Luckily, Windows 95 shipped with a minimum VGA video card system requirement, alleviating CGA or EGA concerns. However, you'd still have to tinker with planar modes, which was not an easy feat.

**FLASHBACK**:
*Windows 95 was released to manufacturing on July 14, 1995, and it became generally available to the public on August 24, 1995 . This release marked a significant milestone in personal computing with features like the Start menu and taskbar, which are still familiar to users today*(Image credit: Getty Images | Brooks Kraft)
For context, planar modes are electromagnetic modes propagating through planar waveguides. They enable the confinement and controlled propagation of light. "Fortunately, you have a team of folks expert in VGA planar modes sitting down the hall working on Windows video drivers who can help you out," added Chen.

Beyond pixels, the setup program also requires dialog boxes, which consequently require you to write a window manager to complement your graphics library within a standard GUI dialog interface. It would also require keyboard support for tabbing between elements and assigning hotkeys.

The process also included adding support for typing characters in non-alphabetic languages like Japanese. Luckily, you could lean on the Windows expert team working on Japanese input sitting in Tokyo, but the time difference would negatively impact your progress. This is on top of the new controls developed by the UI team, which would follow a similar protocol.

Don't forget animations that require a scheduler to trigger events based on the system hardware timer. You'll need to write code that isn't even part of the Windows 95 setup process. Perhaps more concerning, after all the effort, it would have been an uphill task trying to squeeze everything into just 640KB of storage. You could circumvent this by writing a protected mode manager to leverage the extra storage space allocated for protected mode.

The efforts seem counterproductive as Microsoft already has a similar product **— ** the Windows 3.1 runtime. It was "fully debugged, with video drivers, a graphics library, a dialog manager, a scheduler, a protected mode manager, and input methods."

Kevin Okemwa is a seasoned tech journalist based in Nairobi, Kenya with lots of experience covering the latest trends and developments in the industry at Windows Central. With a passion for innovation and a keen eye for detail, he has written for leading publications such as OnMSFT, MakeUseOf, and Windows Report, providing insightful analysis and breaking news on everything revolving around the Microsoft ecosystem. You'll also catch him occasionally contributing at iMore about Apple and AI. While AFK and not busy following the ever-emerging trends in tech, you can find him exploring the world or listening to music.

### You must confirm your public display name before commenting
Please logout and then login again, you will then be prompted to enter your display name.