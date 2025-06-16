# Agentic Coding: How Google’s Jules Compares to Claude Code
![Featued image for: Agentic Coding: How Google’s Jules Compares to Claude Code](https://cdn.thenewstack.io/media/2025/06/2f5eb6f1-yasa-design-studio-_vlxtjqufue-unsplashb-1024x576.jpg)
[YASA Design Studio](https://unsplash.com/@yasadesign_studio)on Unsplash.
After my successful use of [Claude Code](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/), I was keen to try other equivalent agentic large language model (LLM) tools that aren’t IDE-based. These have better ways to interact with a plan than staring at files. Because a plan can be expressed as an ordered set of well-known coding practices, an LLM just acts as a code wrangler — which we know it does well.

The Google project [Jules](https://jules.google.com/) describes itself as “an async development agent — Jules tackles bugs, small feature requests, and other software engineering tasks, with direct export to GitHub.” I like the way they have limited what they think the tool can tackle. I’m not so happy that it only works over GitHub even at beta — this might make sense for Microsoft, not Google.

My previous example project that I used to test Claude would be suitable for Jules: some early code for a Rails CRUD project that I wanted to add Bootstrap to. The task did not appear particularly challenging for Claude, so what I’m looking at mostly is the workflow with Jules.

## Using Jules
Jules clones your repo into a private virtual machine (VM) and gets to work. When I initially try Jules (marked as beta, like everything Google produces), I get an interesting formal privacy notice that is a somewhat harsh buzzkill to the playful bitmap graphics style on the previous page. It made the usual confusing set of statements about what Google uses and what they don’t read — none of which can be proven. Apparently, they never read code from private repositories, but even that statement is couched in caveats.

There is a [90-second video](https://youtu.be/M2G27_B7BBM) that shows a user connecting to GitHub, selecting a repo and then making a request. I like the fact that it can do anything “you would normally write a PR for.” Again, this is a nice sizing premise for the product — even though it’s slightly different from what I read above. It uploads your code and creates a plan that you can approve. This should feel comfortable for non-developers, with diffs displayed in a side panel.

Jules also pushes the idea of a collaborator, not just a tool — much like Claude. Hence, it has a friendly (and gender-neutral) sounding name. After working on the plan, it then creates a new branch and puts the code on that. That’s a sensible approach from an engineering point of view, but it suddenly forces causal users to understand the semantics of git. That almost feels vindictive.

## Getting Code Into GitHub
OK, my example code project isn’t in GitHub yet, but we can put it there.

In a similar step to what I did with Claude, I untarred an early build of my Rails project for my work with Jules:

Now we’ll push this code to GitHub. The best way to do that is to create a repo in your account, then push your code after adding the new remote. (This is actually a reasonable task for AI, too!)

Go into your GitHub account and set up the repo:

I sadly declined the excellent suggestion of “cautious-octo-succotash” for the repo name, though I’m sure I will use it in the future. Then I take a note of what will become the remote destination:

And then we just push the code from the command line after putting it into a local git repo. You may very well need a personal credential to do this. The trick is to add the remote:

When your code is safely in GitHub, you can go back to using Jules. And once you give permission for the repository, you should finally be able to put Jules through its paces, with your chosen project:

OK, this is roughly what I asked Claude to do with my basic Rails app, so we ask roughly the same thing:

- Use Bootstrap 5 definitions to improve HTML.
- Apply Bootstrap color utilities to improve visual hierarchy.
- Update buttons with Bootstrap button classes.
So I copied this into the chat panel. After booting up the VM, cloning the repo and reading the files (about 2 minutes), it worked out a plan:

Note that if you don’t immediately approve, then it auto-approves after about a minute! But I approved the plan.

Remember, there’s a lot here I have not said. I did have a few examples in code, but not consistently applied.

While working through the tasks, it had already shown me what it did with the main sidebar within **applications.html.erb**, which looked very similar to how Claude cleaned it up.

After some time (remember it isn’t working on your local system, so time is not a big issue), it was ready to publish:

So I could publish the improvements branch, and then merge it into my main branch. While this does require a casual user to align with the git workflow, it’s the correct way to do things. Of course, I can go straight to GitHub and check that there was indeed a new branch:

As expected, it had made a sensible entry for its change:

I created the pull request and merged it. Now, I don’t normally use the pull request method — within internal corporate repositories, it wasn’t the norm — but all we’re doing is confirming that the changes made by Jules are approved to be merged into the project’s main code. When the merge is done, the branch becomes redundant:

So now I’ll do a local pull and see how it looks.

I won’t do a side-by-side comparison of the Rails app after Claude changed it, but I’ll compare the same set of images. Here is the original project code with sidebar:

And here is the same section now after Jules upgraded it:

Apart from the much nicer sidebar, Jules has made no changes to the links on this page. It did clean up nicely elsewhere.

I gave it one more instruction — the exact same hint with Bootstrap that I also gave to Claude to change path links:

It did make the improved changes. Here’s how it looked:

If I was more specific, I would’ve been able to change all the links at once.

## Conclusion
This wasn’t quite as clever as Claude in getting my intents, but with a little more prompt engineering, I know I’ll get the right results. The process of iteration and testing is a little lengthier using pull requests, but it’s more of an industrial workflow. Obviously, I prefer not having to use GitHub; but then again, I appreciate that Google is doing everything on their own hardware.

As usual, Google’s products are internally inconsistent, which is part joy, part head scratcher. But what they have recognized is the causal coder market, recently opened up by vibe coding. I think Jules makes the mark here.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)