# The Windows Subsystem for Linux Is Now Open Source
![Featued image for: The Windows Subsystem for Linux Is Now Open Source](https://cdn.thenewstack.io/media/2025/05/1e9dffe9-img_20160925_175258-1024x576.jpg)
At its annual Build developer conference, Microsoft today announced that it is open sourcing the Windows Subsystem for Linux (WSL), which allows developers to easily run Linux distributions inside of Windows.

“We want Windows to be a great dev box,” [Pavan Davuluri](https://www.linkedin.com/in/pavand/), the corporate VP at Microsoft in charge of Windows and devices, told me. “At the end of the day, a good dev box means a variety of different things. One of them has been just having great WSL performance and capabilities, so that it is a one-stop shop for our developers to live in the Windows-native experience and to be able to take advantage of all of what they need in Linux.”

Developers can now download the code, build the WSL from source, and contribute features and bug fixes.

The first version of the WSL launched in 2016. At the time, Windows essentially emulated a Linux kernel (using lxcore.sys and lxss.sys), but with the launch of WSL 2 in 2019, the team switched to the Linux kernel itself to offer better compatibility. Since then, WSL added support for GPUs, graphical applications, and support for systemd.

![Windows Subsystem for Linux architecture diagram](https://cdn.thenewstack.io/media/2025/05/c9bc2541-screenshot-2025-05-16-at-12.58.03%E2%80%AFpm.png)
The WSL architecture. Credit: Microsoft.

Davuluri noted that the team had gotten a lot of requests from developers to open source the WSL, but in the early days of the project, the team’s focus was squarely on shipping the project and seeing what developers would do with it. With the launch of WSL 2, the focus was on performance and adding new features. Now, after significantly refactoring some of the core components of Windows so WSL could be a standalone system, [Microsoft felt ready to open source](https://thenewstack.io/microsoft-open-sources-openhcl-a-linux-based-paravisor/) the project.

My intuition is there are a couple of places where Windows services for Linux, or Linux services for Windows, is the first place where we’re going to see a bunch of work that I think reduces the friction between the [native Windows experience for developers](https://thenewstack.io/how-the-developer-experience-is-changing-with-cloud-native/) and the things that they do, both in terms of setup and execute on the Linux side,” Davuluri said when I asked him where he expects developers to start contributing to the project. “That is the first place where we see the most amount of energy for folks to actively execute or grind through things that matter for folks on a day-to-day basis.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)