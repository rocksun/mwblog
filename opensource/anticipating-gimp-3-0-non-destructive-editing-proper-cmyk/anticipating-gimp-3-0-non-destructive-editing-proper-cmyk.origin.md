# Anticipating GIMP 3.0: Non-Destructive Editing, Proper CMYK
![Featued image for: Anticipating GIMP 3.0: Non-Destructive Editing, Proper CMYK](https://cdn.thenewstack.io/media/2024/12/65513765-gimp-1024x715.jpg)
I cannot remember a time when I didn’t use [GIMP](https://www.gimp.org/). For those who do not know, GIMP stands for GNU Image Manipulation Project and it’s the open-source equivalent of Photoshop.

GIMP is powerful, with all the tools you need to create and edit incredible images. I’ve been using GIMP for years to create book covers for myself and many others, as well as create/edit screenshots and other image-related tasks.

GIMP development tends to be a bit on the slow side. For instance, GIMP 2.0 was [first released](https://thenewstack.io/qa-cockroach-labs-spencer-kimball-on-distributing-sql/) 20 years ago. In computer years, GIMP 2.0 may as well have been released when dinosaurs roamed the earth.

After all those years, version 3.0 is near, and it includes some pretty nifty features that have been long overdue.

Let’s take a look at some of the features that should make any GIMP user anxious for this upcoming release.

## Non-Destructive Editing
If GIMP 3.0 only came with one new feature, non-destructive editing would be the feature I’d want. Non-destructive editing makes it possible to edit an image without permanently changing the original.

Think about that. You could open an image, make a ton of changes to it, and instantly revert back to the original. There is no longer the need to undo changes one at a time, hoping the edit history goes back far enough. Instead, non-destructive editing removes zero data from the original image, so it’s always there with no degradation.

I’ve had so many instances where I’ve needed to revert to the original, but I’ve made so many changes that the history doesn’t go all the way back to the beginning. If I’m working on a complex image, that can be a big problem.

Non-destructive editing is controlled in the Layer Effect window, where you’ll see a small fx icon. Click that icon to see all of the layer effects that have been changed (Figure 1).

-
Figure 1: A book cover of mine, as seen in GIMP 3.0, with non-destructive editing.

## Additional Layer Features
For those who depend on layers (such as I do), GIMP 3.0 adds new layer features, such as auto-expanding layers (GIMP automatically adjusts the dimensions of a layer according to the latest changes). There’s also a new layer-snapping option that makes it easier to align your layers more precisely. If you’ve ever had to align a layer, pixel by pixel, you’ll understand why this feature is important.

## Improved Font Handling
If you were to look at GIMP on my machine, you find hundreds of fonts installed. To date, GIMP hasn’t been the greatest with fonts. I’ve experienced it all too many times; when working with book covers, fonts tend to not render properly with artifacts and/or bitmapping.

Thankfully, with GIMP 3.0, font handling has been completely redone, so there’ll be far fewer problems with [fonts](https://thenewstack.io/what-developers-need-to-know-about-fonts-and-typography/).

## Plugins
GIMP depends on plugins to expand the feature set. If you want effects, most likely you’ll be adding a plugin. Many of the plugins have been updated and tweaked for version 3.0. For example, plugins for GEGL (Generic Graphics Library), include GEGL Styles (Figure 2) with several new effects, such as non-destructive stroke, Inner Glow, and Bevels.

-
Figure 2: The new additions to GEGL Styles.

## CMYK Support…Finally!
GIMP 3.0 is finally getting [CMYK support](https://www.digital-print-solutions.com/cmyk-colors). Don’t get too excited because it’s not a full CMYK color space. Even so, GIMP 3.0 will offer much better CMYK support out of the box, so you can better prepare your work for print. If you’re not sure what CMYK is, it’s a color model, that is also known as four color that is used in color printing. Without CMYK support, images produced in GIMP don’t always print with accurate colors.

With version 3.0, users can import a CMYK color profile for “spot proofing,” which means it’ll be possible to work in an RGB color space but view the image in a CMYK profile. That’s pretty huge for anyone who uses GIMP to create images for print.

## What Hasn’t Changed
This may or may not disappoint some users, but the GIMP UI has hardly changed. If you enjoy the GIMP interface, this will bring you a happy sigh of relief. If you hate the GIMP interface, most likely, you’ve moved on from the open-source image editor to something else. Either way, the only big change to the interface is a new splash screen. I’ve always been happy with the GIMP UI, but a lot of users don’t share that opinion, so not changing the UI at all seems like a missed opportunity… especially after 20 years.

For the most part, GIMP 3.0 feels very much like GIMP 2.0.

## When Does It Release?
Currently, there is no official release date for GIMP 3.0, but it is expected soon. I’m fairly confident we’ll see the release in Q1 of 2025. If you’re anxious to test drive GIMP 3.0 on [Linux](https://thenewstack.io/learning-linux-start-here/), here’s how you can do that.

### On Ubuntu
If you use a [Ubuntu-based distribution](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/), add the required repository with[ the command](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/):

1 |
sudo add-apt-repository ppa:ubuntuhandbook1/gimp-3 |
After that, update apt with:
1 |
sudo apt-get update |
Finally, install GIMP 3.0 with the command:
1 |
sudo apt-get install gimp libgegl-0.4-0t64 gir1.2-gegl-0.4 gir1.2-gimp-3.0 gir1.2-babl-0.1 -y |
### With Flatpak
If your [Linux distribution](https://thenewstack.io/choosing-a-linux-distribution/) of choice (such as [Fedora](https://thenewstack.io/fedora-41-offers-zippy-performance/)) uses Flatpak, you can install GIMP 3.0 with the following command:

1 |
flatpak install --user https://flathub.org/beta-repo/appstream/org.gimp.GIMP.flatpakref |
Log out and log back in, and you’ll see the GIMP 3.0 icon in your desktop menu.
To stay up to date on all things GIMP, make sure to check out the official [GIMP News page](https://www.gimp.org/news/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)