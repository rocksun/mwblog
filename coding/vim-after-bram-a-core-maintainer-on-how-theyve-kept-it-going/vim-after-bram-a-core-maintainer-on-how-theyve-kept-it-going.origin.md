# Vim After Bram: A Core Maintainer on How They’ve Kept It Going
![Featued image for: Vim After Bram: A Core Maintainer on How They’ve Kept It Going](https://cdn.thenewstack.io/media/2025/02/fa86b348-albuquerque-sunset-october-2022-photo-by-david-cassel-1-1024x774.png)
What happened to the [Vim open source text editor](https://thenewstack.io/a-look-at-vim-a-text-editor-for-the-ages/) after its creator [Bram Moolenaar](https://thenewstack.io/bram-moolenaar-author-of-the-open-source-vim-code-editor-has-died/) passed on in August 2023?

Its community performed a quietly heroic effort to make sure his project stayed alive.

Vim maintainer [Christian Brabandt](https://github.com/chrisbra) [told the tale] in late November at [VimConf 2024](https://vimconf.org/2024/). It was a true-life inspiring story of resilience, perseverance and commemoration.

“What you can see is basically that the development did not stop,” Brabandt told his audience in Tokyo.

Every day there are fresh pull requests and issues to review, so “It’s still quite active. There’s a lot of activity going on on GitHub.”

And in January of 2024, they released Vim 9.1 — and dedicated it to Moolenaar.

## ‘The Development Did Not Stop’
Platform consultant [Christian Brabandt](https://github.com/chrisbra) had been active in the Vim community since 2006, contributing bug reports, fixes and a few new features. He’d worked on things like Vim’s regular expression handling and its support for encryption, as well as helping build its daily Appimage and “moving the home page around.” And then suddenly in August of 2023, “I became one of the main maintainers of Vim.”

The news of Moolenaar’s death was “quite shocking for all of us,” even though Vim’s mailing list had gone “pretty quiet” in the weeks before, and “people already started to wonder what happened with Bram? Where is he?”

“We had to decide what we were going to do.”

Brabandt first acknowledged that they “lost a lot of knowledge” — and not just Moolenaar’s test scripts.

Moolenaar started Vim 30 years ago, and he carried in his head “a lot of knowledge on the original Vim of all the features he wanted to have.” But more than that, Moolenaar was also the project’s leader. “He basically determined the strategy — where he wanted the project to go and what he wanted to be included and what he didn’t like.”

“We had to restructure and find ways to continue.”

And right from the beginning, there was one essential crisis. When it came to Vim’s GitHub account, “Bram was the owner. That means only he could make certain decisions — final decisions like setting up roles and permissions for other maintainers… We needed to have this power to continue working and invite other maintainers to the project.”

Fortunately, GitHub actually has a “[deceased user” policy](https://docs.github.com/en/site-policy/other-site-policies/github-deceased-user-policy), including “[pre-designated successors](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/maintaining-ownership-continuity-of-your-personal-accounts-repositories).” But unfortunately, Brabandt told his audience, using that policy “is not as easy as it sounds,” since after the paperwork is filled out, the GitHub account “becomes basically deactivated. Which wasn’t the best thing for us, since Bram’s family was able to access his account, and I didn’t want them to lose this ability.” Instead, Moolenaar’s family changed the permissions so that other maintainers could be invited.

Shortly after Moolenaar’s death, “Quite a few pull requests” started accumulating on GitHub, Brabandt said. “So I started going through those and importing them.” And when another long-time contributor and core maintainer, Charles Campbell, decided to retire, “I decided to invite a few more maintainers… mainly people who have been long-time contributors to Vim.”

But besides the source code, they also had to manage the project’s other infrastructure, and unfortunately, there were no documented processes, “so I had to find out all of this — how this is managed — basically, the hard way.”

And it seems like everything that could go wrong did.

- The site handling Vim’s vulnerability reports was
[acquired by an AI-security company](https://www.businesswire.com/news/home/20230808746694/en/Protect-AI-Acquires-huntr-Launches-World%E2%80%99s-First-Artificial-Intelligence-and-Machine-Learning-Bug-Bounty-Platform)that Brabandt says “just wanted to concentrate on AI and only on AI… Open source vulnerability reporting was basically shut down almost immediately.” So the project turned to GitHub Security Advisory. - Brabandt learned the basic code of Vim’s home page hasn’t changed in 20 years. It still included PHP 7 code — though support for Php 7
[ended in November of 2022](https://www.php.net/releases/index.php). - The service hosting their home page was acquired by Open Source China in July of 2023, and soon began serving visitors database errors, while support tickets went unanswered. So in the middle of restructuring the Vim project, the project team had to also find a new host for Vim’s home page — but, “Unfortunately, this also meant that we had to upgrade the home page from PHP 7 to at least PHP 8 support.”
- The FTP server was still being run by the
[Dutch Unix User Group](https://en.wikipedia.org/wiki/NLUUG). “This was fine in the ’90s and maybe early 2000s,” Brabandt said, but “Nowadays I think people typically just download everything from GitHub or from the home page!” The Dutch Unix User Group was also reluctant to give Brabrandt access, and “It’s fine…” he said, “because we then decided to retire the old FTP server. And if a download needs to be done, it can be done via the Vim home page.”
And since retiring FTP access, Brabandt says he hasn’t heard a single complaint.

## What About the ICCF?
It wasn’t until late 2024 that they realized the help pages still mentioned email addresses that were forwarding to Moolenaar’s old email account. “Just two weeks ago or so, I changed those, so now they have been forwarded to my address,” Brabandt told his audience in November.

Vim famously urges its users to contribute to Moolenaar’s favorite charity, the [International Child Care Fund Holland](https://iccf-holland.org/), and Brabandt says the Moolenaar family is still maintaining [Bram’s Paypal account for those donations](https://www.paypal.com/donate?token=GuL3qWPYJL3FgOkjPAvH6zDTpScmwWX1L-e_6b58Oj-7yKhpaM9KeyMMGzfgTsICdLw2HDRrLssfR9sS) (still linked to from [Vim.org](https://www.vim.org/)). After Moolenaar passed a lot of people donated to the ICCF, with another 90,000 euros donated in 2024. Brabandt is also committed to making sure those donations go through as intended — and says he’s not planning to create any Vim sponsorships any time in the near future.

There was one change made: Bram Moolenaar’s feature which allowed ICCF donors to vote on future Vim features was shut down. It was hard to figure out which ICCF donations should be linked back to Vim.org users. (“I’m not sure how Bram did it in the past,” Brabandt says, and “the other people from the ICCF weren’t able to tell me!”) But in reality, it turns out that most of the new enhancement requests and issues are already coming from other sources like GitHub and Vim’s own to-do list.

## ‘Maintenance Mode’
So what does the future hold? Vim plans “a bit more potentially controversial changes” for the upcoming release of Vim 9.2, Brabandt told the audience. These include supporting the XDG specification’s [base-directory specifications](https://www.freedesktop.org/wiki/Specifications/basedir-spec/) (“The community has been wishing for it at least maybe 10 years.”) and better support for [Wayland](https://en.wikipedia.org/wiki/Wayland_(protocol)). There are a few new options and plugins and some inevitable bug fixes.

So while changes are being made, this led Brabandt to a quietly momentous statement on the future of Vim. “However, currently I would say Vim is more or less in maintenance mode. I don’t think any of the maintainers can perform full-time work on Vim or bigger features.” As an example, he’s aware the Neovim community has been making big changes like support for parsing library [Tree-sitter](https://tree-sitter.github.io/tree-sitter/), but adding that to Vim would take a “tremendous effort… I’m not quite sure we can achieve it, at least not in the near-term.”

But Brabandt announced another worthy goal: making sure that the community is healthy. And this means welcoming new contributors and making it easy for them to start contributing code. Brabandt has even imported some automatic code-formatting tools, since before Vim’s source code used an idiosyncratic formatting style that Brabandt called “strange. It’s basically Bram’s style of working, which is okay, but it doesn’t help new users.”

A later slide suggested things people could work on include “Tree-Sitter integration?” along with a GTK-version of Vim’s GUI interface and more advanced terminal features. Vim’s spell-checking code, for instance, “hasn’t been touched for a few years.”

“If you’re looking for big new features in the future, we do depend on the community to help us with this,” Brabandt said. But he always advises new contributors to “start small” while they’re first getting familiar with the codebase.

And for right now, “most of the changes that have been merged are relatively self-contained, small-feature sets, which can be easily tested and don’t have that much impact on other parts of the code.”

## Testing, Refactoring and Maybe Retiring That Python 2 Interface
They’re still using “defensive and safe” C coding — Brabandt says refactoring everything into a modern programming language like Rust just isn’t an option right now. There’s a comprehensive suite of tests that he’s running over all changes — and every day they run the code-analyzing tool [Coverity](https://en.wikipedia.org/wiki/Coverity). And going forward, they’ll refactor parts of the code “which are quite long and lengthy and complex and hard-to-understand.” (Does Vim really still need an external interface to Python 2? Since the Python community moved on to Python 3 years ago, Brabandt believes it’s an example of one of the outdated interfaces that could be retired “at some point in the future.”)

A big policy goal is making sure to continue Vim’s backward compatibility. And of course, learning from the past, Brabandt put up a slide titled “The new Vim Project — future,” which included a key “policy” bullet point: “Better documentation of (internal) processes.”

Brabandt said he came up with these policy principles while going through Moolenaar’s backlog of outstanding pull requests.

But another improvement he’d like to see is just a better understanding of Vim’s community — and he’s even considering a user survey. Toward the end of his talk, Brabandt told the audience what he’s learned since Moolenaar’s passing: that maintaining Vim is *hard* — and that it’s a full-time job. “It’s not only about writing code; it’s about managing the community.” And that means *listening* to that community — “Listening to their requests, fixing bugs that come up and making sure that we can keep up and do what the community wants.”

“It’s an open-source project — that means the community can contribute and should contribute and also help us steer the project into the future.”

And Brabandt said there’s already a clear signal of that [healthy community](https://thenewstack.io/open-source/): the Vim conference itself.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)