# Cascii and Why Developers Should Use ASCII Diagrams
![Featued image for: Cascii and Why Developers Should Use ASCII Diagrams](https://cdn.thenewstack.io/media/2025/03/55b2e003-viktor-forgacs-iv72ujcnptw-unsplashb-1024x576.jpg)
“Is that something devs do regularly, ASCII diagrams?”

This post is an answer to this editorial challenge. It started after hearing about the [Cascii app](https://cascii.app/) and reflecting on the fact that the development community still doesn’t have a very efficient way of making and sharing simple diagrams.

Cascii itself is a very neat American Standard Code for Information Interchange (ASCII) editor or, [as the project describes itself](https://github.com/casparwylie/cascii-core),** **“a web-based ASCII and Unicode diagram builder written in vanilla JavaScript.” It has no dependencies, packing, or libraries.

You can just go to the [hosted app](https://cascii.app/), or run your own local version by downloading the HTML and opening a browser:

This will get you started with the light theme version, which uses Unicode. In the Settings, you can change to dark mode and switch to straight ASCII.

A note on Unicode vs. ASCII: Unicode is the universal, variable-length encoding that encompasses most languages — you will notice some fancier arrows and dotted effects when that mode is on. While Unicode gives you more symbols to play with, it is much less bulletproof than the standardized and much older ASCII.

The hosted version of Cascii allows you to save drawings and share them via a URL — you can see these at the bottom of the diagrams you copy.

If you’ve used an image editor recently, you won’t have any trouble using Cascii. You can create shape components, line connectors, and text. You can select, then resize, duplicate, and move these components (however, I couldn’t move the diamonds). You can shift components to the back or front, although I can’t imagine anything that would need this.

A simple flowchart diagram was done fairly quickly with just squares, a diamond, lines, and text. The true revelation comes when you hit the Export button, in which Cascii copies your diagram into your paste buffer. Voilà.

I copied my first attempt into my Warp terminal just to prove it is just ASCII art:

You can go straight to the URL shown and load it up yourself. But my diagram is a bit unwieldy, so I made a smaller version to use as art. Before we play with that, let’s look at where you may have actually come across an ASCII diagram or art.

## Where Do Devs Use ASCII?
If you look at the raw markdown for the [Cascii GitHub README.md page](https://raw.githubusercontent.com/casparwylie/cascii-core/refs/heads/main/README.md), you will see their structure diagram between the three backticks
, which is the GitHub Markdown dialect for formatting text into its own distinct block. I can do it in WordPress too:```

1234567891011121314151617181920212223242526 |
┌╶╶╶╶╶╶╶╶╶╶╶╶╶╶┐ │ GroupManager │ └╶╶╶╶╶╶╶╶╶╶╶╶╶╶┘ ┌─────────────┐ / ┌─────────────┐ │EventManager │ / ┌───────│SquareLayer │ └─────────────┘ / │ │─────────────│ ┌───────────────┐ \ / │───────│CircleLayer │ ┌────│SwitchLineLayer│ \ / │ │─────────────│ │ │───────────────│ ┏━━━━━━━━━━━━┓ │───────│BaseLineLayer│◀──┐────│FreeLineLayer │ ┃LayerManager┃◀──────┘ │─────────────│ │ │───────────────│ ┗━━━━━━━━━━━━┛ │───────│DiamondLayer │ └────│StepLineLayer │ ┌────────────┐ / / \ │ │─────────────│ └───────────────┘ │CharManager │/ / \ │───────│FreeLayer │ └────────────┘ / \ │ │─────────────│ / \ └───────│TableLayer │ ┌────────────┐ \ └─────────────┘ Pixels! │ ModeMaster │ • └────────────┘ • • ▲ • • │ • • │ • CanvasCom ────────────────────────────────┘ • • • • • • •Edit/view: https://cascii.app/7c24a |
There are also common memes that appear as ASCII art, of course. So, I can make a git check out note with ASCII art. Perhaps that is where the meme “table flip” appeared most:
# (╯°□°）╯︵ ┻━┻
Basic diagrams have often appeared in code comments — normally system flowcharts or network diagrams. Amongst developers using VIM, or at least monospaced (fixed-pitch) fonts like Courier in their IDEs, these would all be easily discernible.

In the old days, when even simple image rendering needed machines with good graphics cards, ASCII art represented an easily shareable default. Only the combination of decent font control and eventually emojis eroded its use. Eventually, developers got access to tools like Microsoft Visio, a diagramming and vector graphics application that became almost ubiquitous. While Visio lives on, it is a more complicated beast, preferred by architects and marketers.

## Cascii: Good for Diagrams
Let’s get back to a simpler version of my flowchart example:

123456789101112131415161718 |
+ / \ +---------+ / \ +--------+| | / \ | || Start! |+ Continue? +--------| Done! || | \ / | |+---------+ \ / +--------+ \ / + | | | +---------+ | | | +-------| Cancel | | | +---------+ Edit/view: https://cascii.app/02e0e |
Now you can copy this and paste it straight into Cascii. Almost. By the time you see this on your browser, it will have been processed many times and will likely be slightly different from the original, perhaps losing a vital line-ending character. However, if you drop it into a terminal program like Warp and then paste it into Cascii, you will likely see the diagram:
There are a few other tools that can convert images to ASCII format, or bigger things like [playscii](https://jp.itch.io/playscii) that are more dedicated to full art. But Cascii seems to be out on its own for simply drawing diagrams.

## Why Devs Should Use ASCII
While it is still relatively easy to create, share, and re-edit ASCII images, helped by tools like Cascii, the enemy is the rapid format transformations media regularly goes through as we move text through messages, social media, and document forms. Also, it is far from simple to follow the fate of line endings and positioning, without which fixed-width, multiline ASCII is easily defeated.

The advantage is the flexibility of the full loop, from creation of a diagram through sharing via copying and re-editing when needed. None of these steps require tools at all — it is in making multiple small update changes on the fly anywhere text can exist that brings out their true efficiency. It is much easier for an ASCII diagram to “live” with the code if it is drawn above it and stored with it.

So the real answer to the question posed at the beginning of the article is that developers can and should use ASCII diagrams, but to get the full flexibility, they might need to be working in teams with similar tools. And in that case, they may as well just agree to use the same modern diagramming tools. It just so happens that there really are no simple diagramming tools that developers have all settled on, so a tool like Cascii can fill the role for lightweight cases that are easy to maintain.

┳━┳ ヽ(ಠل͜ಠ)ﾉ

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)