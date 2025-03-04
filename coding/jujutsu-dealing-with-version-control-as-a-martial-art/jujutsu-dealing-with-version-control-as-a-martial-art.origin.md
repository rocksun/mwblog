# Jujutsu: Dealing With Version Control as a Martial Art
![Featued image for: Jujutsu: Dealing With Version Control as a Martial Art](https://cdn.thenewstack.io/media/2025/02/db5c82a9-natalia-blauth-znrnassj8f0-unsplashb-1024x576.jpg)
Like most developers over the years, I got comfortable with a handful of git commands that I needed daily — and tried not to get into large merge battles. Even though I have regularly pushed the use of git, I do tell developers to use Google if they can’t remember how to do something, not to try to memorise various scenarios. I remember the resistance when having to explain, on moving from [Apache Subversion](https://en.wikipedia.org/wiki/Apache_Subversion), that basically you needed three commands where previously you only needed two.

On the plus side, I also remember a junior developer deleting our central repository. I then calmly explained to this person that we could probably recover that in minutes, because the ‘central repository’ in git is more of a common agreement than the sole source of truth.

So why is Google using something different? I still use git today in some projects, but mostly [Plastic SCM](https://www.plasticscm.com/) (now controlled by Unity) because it is fully suited to large files. But what can break the stranglehold that git has over most developers?

Enter [Jujutsu](https://github.com/jj-vcs/jj). In Steve Klabnik’s [tutorial,](https://steveklabnik.github.io/jujutsu-tutorial/introduction/what-is-jj-and-why-should-i-care.html) he notes that Jujutsu (or jj) is “a DVCS that takes the best of git, the best of Mercurial, and synthesizes it into something new, yet strangely familiar.” And since Google uses it, it won’t suddenly go away. I’m aware that jujutsu sounds like dealing with version control as a martial art — which doesn’t necessarily bode well, but may be an underlying truth.

For this post I’ll ease into the differences, so I do assume the reader is at least familiar with git at work.

So with git we know we have **an index**, a **staging area**, and **untracked files**. This is what git is telling you about when you use `git status`
after doing some work:

So git recognizes already tracked files that have changed and untracked files that have appeared.

## Working Copy
If you’ve ever used `git stash`
or been told that “Your local changes to the following files would be overwritten by merge,” you have a basic understanding that git treats your tracked and untracked changes as possibly aberrant entities with respect to what is in an upstream central repository.

Jujutsu does away with the staging area or index by representing the working copy as a new commit. So checking out a commit results in a new working-copy commit on top of the target commit. If you regularly use `git add .`
— which stages all new files and modifications — you already consider everything you are working on to be part your next commit. So Jujutsu’s big simplification probably makes sense for many users and use cases.

OK, now I’ve explained something interesting — and we already know that jj is compatible with git — lets install it and have a play.

## Getting Started
As jujutsu is made of Rust, there are various ways you can [install it](https://jj-vcs.github.io/jj/v0.23.0/install-and-setup/). With my MacBook, I simply use:

1 |
brew install jj |
Now, when I said, “jj is compatible with git,” what I meant was that jujutsu uses a compatible model, not that jj can just work directly with an existing git repo. If I try to use a simple instruction `jj status`
within git I get:
So what we’ll do is to keep using git within jj commands to signify that we want git compatibility. I’ll start by cloning a familiar old small demo:

1 |
> jj git clone https://github.com/octocat/Hello-World |
Just as with git, we are warned that we have not set up the user name and email. We have been given clues about this repo, but let’s ask directly what the status is with `jj st`
:

So it placed us in a little read-only editor-style program (called the “pager,” which quits with “q”), but let’s have a look at that response in detail.

Now, jj clearly uses two sets of identifiers: it uses the idea of a **change ID** and a **commit ID**. The first number beginning with “y” on the working copy is the change ID, the second beginning with “3” is the commit ID, and the parent commit has its own pair. We can also see what looks like a branch name of master on the parent commit. Our working copy has no description set, whereas the parent was a pull request.

We would logically learn a little more if we started our own repo locally and looked at the same information. We can use `jj git init`
with the same logic that this is jj using the git format:

Here it is from within the pager for our new repo:

Now we can see that the parent commit has a very specific identification pair, with change ID “zzzzzzzz” and commit ID “00000000”. Unsurprisingly, this is referred to as the **root commit**. This time the new added file is marked as such. And remember, there is no index. As expected there is no set history or branch name.

I set my [user.name](http://user.name) and [user.email](http://user.email) as suggested when I made the clone earlier, so I can journey onwards. Now, or actually, at any time, I can describe my working commit:

So the change ID has not altered, but the commit ID has. That tells us that the commit ID is tracking step by step alterations, whereas everything so far is within the same change ID. Note how we are moving away from git terminology.

So let’s close the loop and “check-in”. We do that by saying `jj new`
. This is a slight change of emphasis — we mark the beginning not the end:

So you can see that our working copy becomes the parent, and we get a new working copy.

This is all great, but we will have to get into some more heavyweight use in another post — but let’s end with a look at our repo as a whole.

I barely use `git log`
, but `jj log`
is a different animal. First, let’s go back to the Hello-World directory to see what the cloned repo looks like:

We can see the various markers (an at a sign, a diamond and a tilde) and the very early date of the commit we started with, and my unused working commit. Note that our natural interest is in the stable change IDs. By the way, the magenta character in the change ID (and the blue character in the commit ID) signify that the one character is enough to uniquely identify it. If you’ve used git, you may already have made use of this concept to save keystrokes in various commands — it is nice that jujutsu makes his explicit.

OK, let’s do the same thing with our fresh repo:

We see the root, my first commit and the new working commit. You can see now that the at symbol is the working copy commit, and the diamond represents the root in this case. I’m guessing the tilde in the clone means “history we don’t have” leaving the circle to mean “other commits”.

## Conclusion
We’ve only seen the basics in use, but there have already been quite a few differences to git — most of them palatable and some even nice. I’ll need to road-test jujutsu more seriously in an upcoming post to see how working with it feels.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)