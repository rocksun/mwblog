# Windsurf: An Agentic IDE That Thinks and Codes With You
![Featued image for: Windsurf: An Agentic IDE That Thinks and Codes With You](https://cdn.thenewstack.io/media/2025/01/1beac1f7-getty-images-b2lu5f9rohq-unsplash-1024x662.jpg)
I’ve tested several [IDEs](https://thenewstack.io/best-open-source-ides/) over the years, many of which offer the same tried and true features you’d expect in such a tool. Many of those IDEs are highly functional and help to make the development process flow with ease.

Some of them even add AI into the mix.

And then there’s [Windsurf](https://windsurfai.org/), which claims to be the first “agentic IDE” on the market. That description caught me off guard, so I had to figure out what “agentic” means. According to Merriam-Webster, agency refers to someone or something capable of achieving outcomes independently (“functioning like an agent”) or possessing such ability, means or power (“having agency”).

Agency is a powerful word these days because it describes the capacity for individuals to have the power and resources to fulfill their potential. Without agency, could we get anything done? Probably not, so having an IDE that empowers agency could be a game-changer.

The developers of Windsurf are all in on AI, and it starts with [Codeium](https://codeium.com/).

Codeium is an AI-powered [code autocompletion tool](https://thenewstack.io/ai-code-assistants-are-moving-beyond-auto-complete-heres-whats-next/) that was created to assist developers by providing code suggestions and completions for over 70 [programming languages](https://thenewstack.io/programming-languages/). Although Codeium integrates with several IDEs, Windsurf is the first to have AI functionality built in this deeply. The goal of having Codeium AI baked into Windsurf is so that it can collaborate with you to help tackle complex tasks.

Windsurf features Workspaces, Cascade (for deep codebase understanding and full contextual awareness), Flows (to help you and AI operate on the same state at all times), multi-file editing, automatic reasoning of explicit actions, and more.

According to Codeium (the company behind Windsurf), “We started with the existing paradigms of AI use. Copilots are great because of their collaborativeness with the developer — the human is always in the loop. That being said, to keep the human in the loop, copilots are generally confined to short scoped tasks. On the other hand, agents are great because the AI can independently iterate to complete much larger tasks. The tradeoff is that you lose the collaborative aspect, which is why we haven’t seen an agentic IDE (yet). An IDE would be overkill. Both copilots and agents are super powerful and have their use cases, but have generally been seen as complementary because their strengths and weaknesses are indeed complementary.”

Sounds great, right? But how does it work?

First, let’s get it installed.

## How To Install Windsurf
I’m going to demonstrate the installation on [Pop!_OS Linux](https://thenewstack.io/pop_os-one-of-the-best-linux-distros-for-creators-of-all-types/), which is [Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/)-based. The first thing to do is open your terminal window and add the required repository with this command:

*curl -fsSL “https://windsurf-stable.codeiumdata.com/wVxQEIWkwPUEAGf3/windsurf.gpg” | sudo gpg –dearmor -o /usr/share/keyrings/windsurf-stable-archive-keyring.gpg echo “deb [signed-by=/usr/share/keyrings/windsurf-stable-archive-keyring.gpg arch=amd64] https://windsurf-stable.codeiumdata.com/wVxQEIWkwPUEAGf3/apt stable main” | sudo tee /etc/apt/sources.list.d/windsurf.list > /dev/null*
Once you’ve added the repository, update apt:

*sudo apt-get update*
Finally, install Windsurf with this command:

*sudo apt-get install windsurf -y*
Once the installation is complete, you’ll find the Windsurf launcher in your desktop menu. Start the app and you’ll be presented with a login screen where you can sign up for a free account. After that, you can select whether you want to import your settings from [VS Code](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/) or start from scratch (**Figure 1**).

**Figure 1**
![](https://cdn.thenewstack.io/media/2025/01/ddd04c61-windsurfer1.jpg)
If you have VS Code installed, I’d suggest importing your information.

You can then select the theme you want to use. Then, you’ll be presented with Windsurf’s main window (**Figure 2**).

**Figure 2**
![](https://cdn.thenewstack.io/media/2025/01/5fca8da5-windsurfermain.jpg)
The Windsurf UI is quite well-designed.

The first thing you should do is click Open Folder to open a previously created project or click the “Generate a project with Cascade” text area below that. When you click Generate, a prompt window opens where you can generate a project with AI.

For example, you might want to create a Python app that accepts user input and writes it to a file. Click Generate, and then type “Create Python app to accept user input and write it to a file.” Click Select Folder: When your file manager opens, either select the folder or create a new one to house the project. After you’ve selected the folder, hit Enter on your keyboard, and Windsurf will do its thing.

After creating my test project, I decided to dig a bit deeper to see how well the AI would work. Near the bottom of the window, there’s another AI query field, into which I typed, “How do I specify the type of input to be entered?” After hitting Enter, Windsurf gave this some thought, rewrote the application and even explained the changes (**Figure 3**).

**Figure 3**
![](https://cdn.thenewstack.io/media/2025/01/01b7ffaa-windsurferupdate.jpg)
Windsurf made some changes based on my query.

I then hit Accept All to accept the changes made by Windsurf, at which point it asked whether I would like it to add any specific type of validation to the project.

This is getting spooky.

Out of curiosity, I ran the application to see if it would work. Windsurf includes a built-in terminal, so at the bottom of the window, the Python app ran and asked me for input **(Figure ****4**). Lo and behold, the script ran to perfection.

**Figure 4**
![](https://cdn.thenewstack.io/media/2025/01/968cce73-windsurferouput.jpg)
You can run your new app and see how it performs.

I’m not advocating the use of AI in programming, but I will say this: If you’re just learning a new language, Windsurf is a brilliant IDE to help you get up to speed. With the right prompts, you can easily build an app and even learn how things work as you go.

Color me impressed.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)