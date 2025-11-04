[![Update and shut down in Windows 11](https://www.windowslatest.com/wp-content/uploads/2025/11/Update-and-shut-down-in-Windows-11-696x403.jpg "Update and shut down in Windows 11")](https://www.windowslatest.com/wp-content/uploads/2025/11/Update-and-shut-down-in-Windows-11.jpg)

Starting with Windows 11 25H2 Build 26200.7019 (or 26100.7019 on 24H2) and newer, your PC will finally shut down when you explicitly choose “**Update and shut down**.”

If your PC restarts after “Update and shut down,” you’re not alone. It affects Windows 11 and 10, and is one of the most reported issues. Microsoft shipped a broken “Update and shut down” toggle with Windows 10, and it never acknowledged it until now.

I don’t want to recall the countless number of times I’ve been deceived by “Update and shut down.” When it’s 11 PM and I’ve to go to work the next morning, but there’s a pending Windows Update. I’d select **Update and shut down**, and go to bed, but the next morning, Windows would be on the login screen if its battery didn’t drain out.

![Update and shut down option in Windows 11 25H2](https://www.windowslatest.com/wp-content/uploads/2025/10/Update-and-shut-down-option-in-Windows-11-25H2.jpg)

Because those update options sit side by side, you might assume you hit “Update and restart” instead of “Update and shut down,” which would explain the return to the login screen. But no, it was a Windows bug all along, and you’re not alone if you can’t trust the ‘Update and Shut Down’ button.

We don’t know what actually causes “Update and shut down” to restart Windows. But Microsoft confirmed that the October 2025 optional update ([KB5067036](https://www.windowslatest.com/2025/10/29/windows-11-kb5067036-25h2-adds-new-start-ui-direct-download-links-msu/)) finally fixed an underlying issue that blocked “Update and shut down” from working in some cases.

“Addressed underlying issue which can cause ‘Update and shutdown’ to not actually shut down your PC after updating,” Microsoft [noted](https://support.microsoft.com/en-us/topic/october-28-2025-kb5067036-os-builds-26200-7019-and-26100-7019-preview-ec3da7dc-63ba-4b1d-ac41-cf2494d2123a#) in a support document.

Microsoft told Windows Latest that it’ll ship a fix for Update & Shut down with the November 11 Patch Tuesday, so the optional update (KB5067036) is not a requirement.

## Why “Update and shut down” was broken in Windows 11 and Windows 10

Microsoft won’t tell us what really happened, but there’s a chance it was a race condition or an issue with the Windows Servicing Stack.

When you use Update and shut down, Windows has two tasks to perform. First, it’ll begin installing all pending updates. Second, it’ll power off the computer at the end of the process, but the catch is that the process isn’t just about “install update and turn off.”

![Working on updates](https://www.windowslatest.com/wp-content/uploads/2025/09/Working-on-updates.jpg)

Windows can’t skip a reboot just because you told it to shut down after updating. It must reboot into an offline servicing phase, which is when you see “working on updates” on your screen. This step is required because Windows cannot finish replacing files when it’s running.

After the “working on updates” phase, Windows is supposed to finally power off, but it doesn’t, and Windows boots to the login screen. The issue was most likely with the Servicing Stack, and the “power off” task is never carried across Windows reboots. It’s either cleared or a race condition, like Fast Startup, that blocks it.

[Home](/)








Share
[Newsletter](#fluentform_4)

Subscribe

![](https://www.windowslatest.com/wp-content/plugins/push-notification-for-post-and-buddypress/public//img/pushbell-pnfpb.png)

![](https://www.windowslatest.com/wp-content/plugins/push-notification-for-post-and-buddypress/public//img/pushbell-pnfpb.png)

Subscribe Push notifications