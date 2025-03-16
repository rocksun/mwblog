# What Is a Linux Tiling Window Manager and Should You Use One?
![Featued image for: What Is a Linux Tiling Window Manager and Should You Use One?](https://cdn.thenewstack.io/media/2025/03/c3d1f8c3-child-5578046_1280-1024x715.jpg)
When using your [Linux desktop machine](https://thenewstack.io/choosing-a-linux-distribution/), how do you open application windows and then adjust them to fit on your desktop precisely where you want them?

Or do you?

Maybe you just open applications and leave their placement up to chance and fate.

However you work with your desktop, chances are pretty good you’re always looking for find ways to make it more efficient.

Maybe a tiling window manager is what you need?

## What Is a Tiling Window Manager?
Before we answer that question, let’s ask another.

What is a window manager?

Essentially A window manager is a piece of software that handles the appearance, placement, and behavior of application windows on your display. Window managers control how windows are opened, closed, resized, and moved, as well as the look and feel of borders, title bars, and buttons.

Key features of Linux window managers include:

- Window control
- Layout management
- Keyboard shortcuts
- Multiple workspaces
- Customization
Without a window manager, [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) wouldn’t know exactly how to open and “draw” your windows.

But what about this “tiling window manager?” What exactly is it?

Okay, let’s talk about something else first… window snapping.

You’ve probably heard of window snapping. If not, here’s the gist:

- You open an app.
- You want the app to take up the left half of the display so you grab the title bar and drag it all the way to the left.
- You open another app and want it to take up the right half of the screen, so you grab the title bar and drag it to the right side of the display.
- You want to split the right half of the display between the second app you opened and a third app so you open the third app and drag it to the bottom right corner of your display.
That’s window snapping.

Now, imagine if your window manager could do that for you automatically. So you open app 1 and it automatically takes up the full screen. Open the second app and the window manager will shrink the first app to fit the left half of the screen and the second app gets the right half. Open a third app and it will continue to split the screen vertically.

Once those apps are open, you can use your keyboard to move them. Say you want your web browser in the top left corner, your file manager in the top right corner and your terminal window taking up the bottom half of the display (Figure 1).

-
Figure 1: The i3 window manager with three apps open.

Most tiling window managers offer easy keyboard shortcuts for moving windows. One tiling window manager is [i3](https://i3wm.org/) and to take care of this action, you’d use the following keyboard shortcuts:

- Super+Shift+right arrow – moves the focused window to the right.
- Super+Sift+left arrow – moves the focused window to the left
- Super+Shift+up arrow – moves the focused window up
- Super+Shift+down arrow – moves the focused window down
In i3, you can also:

- Moving windows between workspaces with the Super+Shift+num keyboard combination (where num is the number of the target workspace (0-9))
- Hold the Super key down and right-click on a window to manually resize.
- Switch to another app window with your keyboard using Super+j (focus left), Super+k (focus down), Super+l (focus up), and Super+; (focus right)
With that collection of keyboard shortcuts, you navigate your way around the i3 tiling window manager desktop with ease.

Sounds like a lot of work for your fingers and your brain, right?

It does take a while to get used to, especially if you’re not accustomed to working with keyboard shortcuts beyond Ctrl+c and Ctrl+v.

Why bother?

The answer to that question is fairly simple — efficiency.

If you really want to create a workflow that’s incredibly efficient, a tiling window manager is a great option because it limits the number of times you have to switch between the keyboard and the mouse. When you have to constantly move your hand from keyboard to mouse, everything comes to a temporary halt. If you keep your fingers on the keyboard, work continues. And by not having to think about where your windows need to be placed, you’re working with even more efficiency.

And that, my friends, is the main reason why you would want to use a tiling window manager.

## Where Do I Get Started?
You might think I would suggest starting with the most popular tiling window manager, i3, but I’m not going to say that. Instead, I would highly recommend you go with [Pop!_OS](https://thenewstack.io/pop_os-one-of-the-best-linux-distros-for-creators-of-all-types/) and use its tiling window manager extension. With this, you can switch back and forth between a traditional desktop and one that tiles.

To enable the Pop!_OS tiling feature, click the tiny icon of three rectangles in the top bar and click the On/Off slider until it’s in the On position (Figure 2).

-
Figure 2: The Pop!_OS Tiling window drop-down.

In that same drop-down, you can configure exceptions to allow certain windows to float, change the shortcuts, show or hide window tiles, show active hint, change the active border-radius and the active hint color, and increase/decrease the gaps between windows.

The Pop!_OS tiling option is a great introduction to tiling window managers, so if you’re curious as to how effective they can be, give it a go.

A tiling window manager isn’t for everyone, but those who do adopt this type of desktop find them to be efficient on a level traditional desktops cannot match.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)