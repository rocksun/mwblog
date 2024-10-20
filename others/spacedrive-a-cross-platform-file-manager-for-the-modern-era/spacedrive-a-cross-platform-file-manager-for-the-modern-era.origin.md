# Spacedrive, A Cross Platform File Manager for the Modern Era
![Featued image for: Spacedrive, A Cross Platform File Manager for the Modern Era](https://cdn.thenewstack.io/media/2024/10/bce0f837-spacedrive-1024x768.jpg)
The file manager is often overlooked when it should be considered a critical component of every operating system. With file managers, you can save and organize files, share files, locate and open files, connect to network shares and much more. Without a file manager, it would be fairly challenging to efficiently use your operating system, and that’s why they are so important.

But not every file manager is created equal. Some file managers have more features than others, some file managers are designed with a modern aesthetic, and most file managers are limited to a specific operating system. For instance, you have Finder on macOS, Explorer on Windows, Files (aka Nautilus) on the GNOME desktop and Dolphin on the Plasma desktop. Of that list, it is only possible to install Files or Dolphin on a different desktop, but even then, you’re installing a lot of other components and dependencies that you most likely won’t need.

That’s why I got really excited when I read about a modern, cross-platform file manager.

You see, I use both [Linux](https://thenewstack.io/learning-linux-start-here/) and macOS. Linux is my desktop operating system, while macOS is the OS I use for my laptop as well as video editing. There are times I wish I could use Finder on Linux or Files on macOS. But with the release of Spacedrive, I don’t have to worry about that anymore. Why? Because Spacedrive is a modern, full-featured file manager that can be installed on Linux, macOS and Windows. And although Spacedrive is still in alpha, the full release is coming soon.

According to the [Spacedrive site](https://www.spacedrive.com/), “Spacedrive is a cross-platform file manager. It connects your devices together to help you organize files from anywhere.”

Where most file managers allow you to connect to remote shares via the likes of Samba, Spacedrive takes a totally different approach. Spacedrive will either automatically detect other instances on your network or you can manually enter them. Once connected, you can send files to another instance of Spacedrive on your network with ease (so long as the person on the recipient machine accepts the incoming file — more on that in a bit).

Another thing that sets Spacedrive apart is that is uses a Virtual Distributed File System (VDFS) as a decentralized database to emulate a file system. With this, Spacedrive indexes a hardware file system to create a master database that is synchronized (in real-time) with other instances of Spacedrive on your network.

The current feature set of Spacedrive (remember, it’s in alpha) includes:

- Libraries: This allows you to create a collection of related folders together for easy access.
- Locations: You can add folders to the sidebar for quick access.
- Tags
- Overview
- Recents
- Favorites
I keep mentioning that Spacedrive is still in alpha stage development. The reason for this is because it very much defines what alpha software is: not ready for general use. I’ve had Spacedrive crash on me several times, watched it drop network locations or refuse to add new Spacedrive nodes, and experienced incongruities between operating systems. For example, the Spacedrop feature (which allows you to easily send files from one machine to another) works fine between macOS machines, but from Linux to macOS it’s still a bit iffy. But when everything works, Spacedrive is something special.

Let me show you what I mean. I’ll demonstrate a simple workflow in Spacedrive between two different macOS machines.

Before we get into this, make sure to download the Spacedrive installer for your operating system from the [official Spacedrive site](https://www.spacedrive.com). You’ll find installers for Linux (currently only available as a .deb file), macOS Apple Silicon, macOS Intel and Windows. There’s also a Docker version, there’s indication it will be coming soon to Android, and there’s also a web version.

Make sure to install Spacedrive on at least two machines [on your network](https://thenewstack.io/networking/) so you can test the node functionality.

## Adding a New Node
The first thing you’ll want to do is to add a new node to Spacedrive. For that, open the file manager and click the gear icon in the bottom-left corner of the window. Within Settings, click Network in the left sidebar and then locate the Nodes section at the bottom, where you should see the other instance of Spacedrive discovered on your network. If the instance doesn’t automatically appear, you can manually enter the IP address for the other instance (no port necessary). Then, click Submit.

If you see an automatically detected node listed, click Connect (Figure 1) to make the connection.

-
Figure 1: Spacedrive on my MacBook Pro automatically discovered the instance on my iMac.

Spacedrive on my MacBook did not automatically locate the Linux instance, so I had to manually add it.

Once you’ve added a node, it should appear in the left sidebar under Peers. If you click on that instance, you’ll see a small window stating that you can drag and drop files to send them to the connected machine (Figure 2).

-
Figure 2: A newly added Peer in Spacedrive.

Guess what? That doesn’t work so well. The reason being is that if you navigate away from the window to find the file to send, the window is gone. As well (at least currently), you can’t open a second Spacedrive window that would allow you to drag and drop a file into the transfer window.

Fortunately, there are other ways to share files. Here’s how:

- Using Spacedrop: Click on any entry under Local in the left sidebar and then click the Spacedrop icon (which looks like a tiny Saturn-like planet). Select the device you want to send the file to, locate and select the file (when prompted) and off it goes. The recipient will have to press Accept to accept the incoming file and then decide where to save it.
- Using the context menu: if you navigate to a folder within Spacedrive, you can right-click a file and select Share > Spacedrop > Node (where “Node” is the name of the recipient machine).
Both of the above methods work every time.

## Libraries
Libraries are another important feature of Spacedrive, as they allow you to collect different folders together into a collection of related topics. For example, you might be working on Project X and have several folders related to that project. You could create a new Library like so:

- Clicking the drop-down in the top-left corner of the Spacedrive window.
- Selecting New Library.
- Give the Library a name.
- Click Add Location (under Locations in the left sidebar).
- Locate and select a folder associated with the project.
- When prompted, click Add.
- Continue adding more locations until every folder related to the project has been added.
What I like about Libraries is that you can create as many as you like and add all the necessary locations, and when you switch between Libraries, only the Locations you’ve added will appear, making this a very productive and efficient file manager.

Although Spacedrive isn’t quite ready for general use, it shows serious promise as a file manager, and I could easily see it becoming my default choice for every OS I use. I would highly recommend you install this cross-platform file manager and see what the fuss is all about.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)