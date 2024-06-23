# AI-in-a-Box With Podman AI Lab
![Featued image for: AI-in-a-Box With Podman AI Lab](https://cdn.thenewstack.io/media/2024/06/12c91cf8-podman-playground-1024x678.jpg)
AI is everywhere. You can throw a stone at any given collection of companies and you’ll hit one that is currently employing AI in
[ some form or function](https://thenewstack.io/pyconus-simon-willison-on-hacking-llms-for-fun-and-profit/).
Most AI is experienced through the likes of companies such as
[Microsoft](https://news.microsoft.com/?utm_content=inline+mention). For some, that’s fine. For others, the idea of working with a third party on such a divisive piece of technology is a no-go.
Fortunately, you can always opt to run an LLM (Large Language Model) locally. These “AI in a box” tools are a great way to either get up to speed on using AI or have an LLM available to your staff.
One such method of doing that is with
[Podman](https://thenewstack.io/use-podman-to-create-and-work-with-virtual-machines/) and the [Podman AI Lab](https://thenewstack.io/red-hat-podman-lab-gets-developers-started-on-genai/). This option is not only very easy to deploy, it gives you the option to select which LLM you want to use and it works very, very well.
I deployed
[Podman AI Lab](https://podman-desktop.io/extensions/ai-lab) on an [AlmaLinux virtual machine](https://thenewstack.io/jack-aboutboul-how-almalinux-came-to-be-and-why-it-was-needed/) and was surprised at how well it ran. Compared to other AI-in-a-box solutions I’ve tried, the Podman AI Lab functioned far better, even with minimal resources. Speaking of which, you’ll need the following minimums:
- 4 GB available memory
- 4 vCPU cores
Once you have that (and a running version of any Linux distribution that supports Podman), you’re ready to get this up and running. One thing to keep in mind is that your version of
[AlmaLinux](https://almalinux.org/) will need to have a desktop environment installed, otherwise you won’t be able to run [Podman Desktop](https://thenewstack.io/install-and-use-podman-desktop-gui-to-manage-containers/) (which is essential).
Let me show you how.
## Installing Podman Desktop
The first thing you must do is install Podman Desktop. The easiest method of doing that is with the help of Flatpak. AlmaLinux ships with Flatpak pre-installed and ready to go, so installing Podman Desktop is as simple as issuing the command:
|
1
|
sudo flatpak install flathub io.podman_desktop.PodmanDesktop
Once the installation is completed, you should find Podman Desktop listed in your desktop menu. Click that bad boy and let’s get the AI Lab installed.
## Installing the Podman AI Lab
With Podman Desktop up and running, it’s time to install the Podman AI Lab extension. To do that, click the extension icon in the sidebar (the puzzle piece icon). In the resulting window (Figure 1), type Podman AI Lab in the search bar and hit Enter.
-
Figure 1: The Podman Desktop Extensions window.
When the Podman AI Lab listing appears, click the associated download button (downward-pointing arrow) to install the extension. You’ll know the extension was successfully installed when it appears with a green indicator. You’ll also see a new icon appear in the sidebar that looks like the top of an Android head.
## Downloading an LLM
It’s now time to download your first Large Language Model. To do that, click the Podman AI Lab icon in the sidebar and then click Catalog. Here, you’ll see a listing of the available LLMs. Select one and then click the associated download button (Figure 2).
-
Figure 2: You’ll find several LLMs to choose from.
Depending on which LLM you’ve chosen, the download can take some time. When it finishes, you’re ready to move on to the next step.
## Create a Service
Now that you have an LLM downloaded, click the Services button. In the resulting window, click New Model Service and then click Create Service (Figure 3).
-
Figure 3: Creating your first service with Podman AI Lab.
Two things:
- If you have more than one LLM downloaded, you can select which one you want associated with this service by clicking the LLM drop-down.
- Unless you have a good reason not to, I would suggest using the default port for the service.
The service shouldn’t take much time to deploy. Once it completes, you can now launch a playground, where you can start interacting with your LLM.
## Create a Playground
Click Playground (under Models). In the resulting window, you can either give the playground a specific name or leave the Playground Name field blank and Podman will assign a random name. Make sure the correct model is chosen and then click Create Playground. The new Playground should become available almost immediately.
## Use Your New Playground
When the Playground is ready, you’ll see a prompt at the bottom of the window (Figure 4).
-
Figure 4: Your new AI Lab Playground is ready to accept your queries.
I did a quick test of the Podman AI Lab and typed What is Linux?. Almost immediately, the AI Lab responded with a valid answer (Figure 5).
-
Figure 5: I was surprised at how quickly the Playground responded.
I then decided to try some a bit more complicated, by asking the Lab to explain quantum mechanics. Once again, I was pleasantly surprised at how quickly it produced an answer. Given this was running on a virtual machine, the performance was remarkable.
And there you have it, another AI in a box you can deploy and use. With enough power, you can deploy a fairly powerful AI tool for your personal usage (or even your small business).
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)