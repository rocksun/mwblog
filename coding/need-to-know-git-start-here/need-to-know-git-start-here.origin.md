# Need To Know Git? Start Here
![Featued image for: Need To Know Git? Start Here](https://cdn.thenewstack.io/media/2024/08/9dcdffe9-git-1024x683.png)
If you’re a developer, you’ve probably heard of [Git](https://git-scm.com/). If you’re not a developer or are just now starting your journey toward becoming a developer, [Git](https://thenewstack.io/developers-want-pragmatic-gitops-and-better-cd-tools/) might not be on your radar, [but it will be](https://thenewstack.io/beyond-code-control-git-for-everything/).

Eventually, every developer comes [in contact](https://thenewstack.io/git-is-15-years-old-what-now/) with Git. Even some non-developer types make use of Git. In fact, a vast number of people and organizations, from all over the globe, depend on Git.

According to [Kinsta](https://kinsta.com/blog/github-statistics/), around 100 million developers around the world use [GitHub](https://thenewstack.io/github-models-review-of-microsofts-new-ai-engineer-platform/) (the web service based on Git) and over 90 percent of Fortune 100 companies use the service. Over [30 million developers](https://ir.gitlab.com/) use a competing service, [GitLab](https://about.gitlab.com/?utm_content=inline+mention), as well. It’s nearly impossible to estimate how many people use Git itself, as many use it internally, which means any statistic would be inaccurate. Suffice it to say, Git is everywhere and you didn’t even know it.

But what is this Git thing of which I speak?

Git was created in 2005 by [Linus Torvalds](https://thenewstack.io/linus-torvalds-on-security-ai-open-source-and-trust/) (the creator of Linux). According to him, there’s a lengthy history as to why he built Git, but it centers around his inability to continue using the BitKeeper revision control system.

Wait … what?

Okay, let’s back up a bit.

## Understanding Git
To understand Git, you have to understand revision control because that’s at the heart of the matter. Revision control (or version control) is a system for managing changes to documents, computer programs and other types of information. Revision control is crucial to collaborative environments, especially those centered around software development.

With revision control, you can best manage changes to code (or other documents) over time. Such a system keeps track of even the smallest changes or updates that are made to the files within.

Git is one such revision control system. In fact, Git is the most popular revision control system on the market. Git works with repositories that serve as centralized hubs for everything related to a project.

Git can work with both local and remote repositories (depending on your needs). Git can manage commits, branches, merging and cloning. Git is also a distributed system, with every developer able to have a local copy of the project for offline work. Git is fast, capable of scaling, makes collaboration on a project possible, keeps track of all changes and is free to use.

Here’s the kicker: Git isn’t exactly the easiest tool to use. It’s actually fairly complex to learn, but once you understand how it functions, it becomes second nature.

Before you start working with Git, there are certain terms you’ll need to understand. Let’s dive into those terms.

## Git Terms
Here are some basic terms you’ll need to know to understand Git.

### Pulls
A pull is [a two-step process](https://thenewstack.io/getting-legit-with-git-and-github-your-first-pull-request/) that first pulls down changes from a remote repository and then updates your current branch with any new commits from the remote branch.

### Pushes
A push is the [opposite of a pull](https://thenewstack.io/push-vs-pull-in-gitops-is-there-really-a-difference/), in that it updates the remote branch with local commits. By default, a push only updates the corresponding branch on the remote. In other words, if you’ve checked out code from the main branch, any change you push will only affect that branch.

### Merge
A merge is used to [combine the changes](https://thenewstack.io/dont-mess-with-the-master-working-with-branches-in-git-and-github/) from one or more branches into the current branch and integrate the history of those branches so all changes are included and all conflicts are resolved.

### Commit
A commit is like a snapshot of a local repository at a specific time. Commits should be made often because they serve as the history of changes to the files within a repository.

### Init
To use a repository, it must first be initialized.

### Clone
To download a remote repository to a local repository, you [clone it](https://thenewstack.io/development-git-clone-a-project/).

### Origin
Origin is the name of the remote repository where you publish your commits. The default remote repository is called “origin.”

### Staging Area
This is like a rough draft, where you can add new versions of a file to be saved with your next commit.

### Branch
A branch is a new version of the main repository that makes it possible to work on various aspects of the project without making changes to the main branch.

## The Git Workflow
Let’s now talk about how Git is used. Here’s a basic Git workflow:

- Install and configure Git on your local machine.
- Create a new repository.
- Add files to the repository.
- Commit changes.
- Check the status of the repository.
- View the commit history.
- Create a branch.
- Merge branches.
- Push changes to a remote repository.
- Pull changes from a remote repository.
## Git for All
I said it wasn’t exactly the easiest tool in the shed to use. To complicate this even more, most people use Git from the command line. Yes, there are various GUIs that simplify Git usage, but the majority of developers tend to stick with the command line.

Speaking of which, Git is available for Linux, macOS and Windows. For Linux, Git is found in all the standard repositories, so installation is quite simple. For macOS, the best way to install Git is to issue the command `git`
, which will prompt you to install the application. On Windows, [download this installer](https://git-scm.com/download/win) and run it as you normally would any installer.

Now that you have a basic understanding of what Git is, in the next few tutorials, I’ll walk you through an actual Git workflow to show you how to set up a local repository and start working with files.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)