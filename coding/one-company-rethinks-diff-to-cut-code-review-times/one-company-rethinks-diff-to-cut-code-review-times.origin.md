# One Company Rethinks Diff to Cut Code Review Times
![Featued image for: One Company Rethinks Diff to Cut Code Review Times](https://cdn.thenewstack.io/media/2024/09/32e5470e-gitclear.png)
A [Stack Overflow blog post](https://stackoverflow.blog/2024/08/05/this-developer-tool-is-40-years-old-can-it-be-improved/) calls it “the oldest tool still widely used by contemporary developers.” The file-comparing program [ diff](https://man7.org/linux/man-pages/man1/diff.1.html) has now been around for literally half a century.

And to this day, its underlying “Myers *diff* algorithm” still finds its way into our workflows — including the way we see changes on [GitHub](https://thenewstack.io/what-github-pull-requests-reveal-about-your-teams-dev-habits/) (with its red highlighting for changed code, and green highlighting for new code).

Is it time for a fresh look? Even *diff’*s official *info* file notes that the GNU project “has identified some improvements as potential programming projects for volunteers.”

But the Stack Overflow blog post offers the fascinating case study of one developer tooling company that decided to try building a better diff…

## All About Alloy
Alloy.dev’s [website](https://alloy.dev/) says it’s in the business of “fine software products,” with a subhead promising their tools are “dogfooded daily by people who love building software.” And it specifically touts two products that “help ambitious creators squeeze the most value from every working hour” — one of which is Amplenote, a note-taking/to-do list app.

And then there’s “[GitClear](https://www.gitclear.com/)” — which the company released after three years of iteration in 2018. “For GitClear, we’re eager to make pull request review take more like 1-5% of the average dev team’s week, instead of 20%,” says Alloy’s [webpage](https://alloy.dev/).

*Harding and his team added new ways to show when code had simply been moved, received minor updates, or experienced name changes from a find-and-replace command.*
Doing some research, the company had found that only 5% of [code changes](https://thenewstack.io/what-github-pull-requests-reveal-about-your-teams-dev-habits/) are truly “substantive” changes, Alloy founder/CEO Bill Harding said in his [2022 presentation](https://www.youtube.com/watch?v=11WQeDdGlgI), with the rest being what they consider “change noise”.

And about 30% of all changed lines in a pull request are just chunks of code that were only moved to a new location. “Why are developers still reading pull requests where this 30% of unchanged code is emphasized equally alongside the substantive changes that deserve attention?” Harding asked.

As Harding said in [a June demonstration](https://www.youtube.com/watch?v=ZulFo7DijWU), “We want to help developers review as little code as possible.”

## Building a Better Diff?
In a guest post on Stack Overflow, Harding describes how Alloy first ran experiments with a new set of diff operators. His goal was to see whether “a deeper lexicon” could condense the way commits are represented. “Can change be shown more concisely than what was possible nearly 40 years ago?” So besides additions and deletions, Harding and his team added new ways to show when code had simply been moved, received minor updates, or experienced name changes from a find-and-replace command.

Reducing lines makes things better, Harding says in [another video](https://www.youtube.com/watch?v=zj8TIGpbaGs). “This can end up being hours more time that you have available to write code instead of reviewing it.”

Alloy presents several examples and [videos](https://www.youtube.com/@gitclear5499) to substantiate their claim that their tool results in 30% less code to review in pull requests.

## How It Works
Obviously, its usefulness depends on what it’s trying to summarize. But when a chunk of code is moved into a separate function, GitClear doesn’t highlight all that moved-but-still-the-same code — only the newly-added method definition.

And Harding’s blog post also highlights a case where they’d made a minor change to a constant value — adding a 0 in front of it. Rather than displaying this as a line deleted and then another different line added, the tool simply displays the changed line with its changed character highlighted (and shown inline).

The end result? Roughly 28% fewer “changed lines” to review — which Harding sees as a clear win. “This implies that updating git diff processing tools could reduce the volume of lines requiring review by almost a third.”

Harding even says they recruited 48 test subjects from CodeMentor to review pull requests — half of which came from GitClear. The results found “equivalent comprehension” of code. But with fewer lines to review, less time was spent reviewing — between 23% less time (on average) and 36% less time (the median).

## Other Features
When I submitted a URL to the company’s “[alternative pull request review tool](https://www.gitclear.com/best_github_alternative_pull_request_review_tool),” GitClear sent me an email highlighting just how many lines of code I wouldn’t have to review using the tool…

But their tool includes other features.

Visiting the pull request pulls up an overview page offering what Harding calls “high-level details of where the pull request is at… and how it compares with previous pull requests that have been submitted.” One graph shows how many days the pull request has been open — and even lets you compare that to other files in your repository — or to pull requests for *all* your repositories, or even “to other companies within your industry.” (Another graph performs the same comparisons for the amount of test coverage in a pull request.)

And then there’s a graph of the “diff delta,” which the company’s site touts as GitClear’s proprietary but “[empirically-validated appraisal](https://www.gitclear.com/diff_delta_factors) of how much durable change occurred per commit,” weaving together a commit’s entire history to track “the long-term fate of each line of code authored — through moves, renames, and other updates.”

They’ve added other ways to try to improve the code-reviewing experience. In a [video demo](https://www.youtube.com/watch?v=ZulFo7DijWU), Harding notes their tool also offers a view of just “unreviewed commits since last review”

“For the way that our team works, this might be the single feature that saves the most time… Because if your team goes through multiple rounds of review on a pull request, you’ve certainly felt the pain of trying to look at a file you’ve already seen before and pick out, ‘Which of the changes were in response to my feedback? And which of these changes were already here, and I’ve already looked at before?'”

And it’s also possible to look [back in time](https://youtu.be/ZulFo7DijWU?si=P2eSN4QwB6bf4XvL&t=317). Hovering over a line displays its whole history of commit messages, “which often elucidates why a particular line evolved into its final form,” Harding explained in his blog post. And this means that even when a line is moved — and may be changed by a find-and-replace command — that line’s original position is still available. [Their essay argues it’s useful seeing that the code appeared in past revisions of an application.]

## Less Time on Code Reviews
Harding’s essay closes by making the case for their tool. How many hours are spent reviewing those additional 28% lines of code? Harding estimates it costs a 10-person team thousands of dollars a week. And Harding also suggests developers might appreciate spending less time on code reviews.

“Considering that code review is often one of the most [unpleasant, high-willpower chores](https://stackoverflow.blog/2024/07/05/what-can-devs-do-about-code-review-anxiety/) included in a developer’s responsibilities, the morale improvement gained by reducing code review time may rival the gains in ‘time saved.'”

It’s not the only alternative. In the comments on Harding’s story was a fan of another alternative named [Difftastic](https://github.com/Wilfred/difftastic).

And in [a 2022 presentation at GitKon](https://www.youtube.com/watch?v=11WQeDdGlgI), Harding acknowledges there’s at least 10 companies now offering Git analysis/developer analytics tools (often combined with issue tracking).

But Harding’s post sparked some lively discussions around the web about the current state of code-reviewing tools. Various long-time Stack Overflow readers left their comments on his blog post:

- “It would be great to recognise [sic] a complete function with the comment block and usually a trailing empty line as one unit and therefore one change”
- “It would be great if a diff recognised [sic] a renamed file…”
- “A lot of improvements in the review process can come from intentionally separating the commits in a way that facilitates review.
Whatever the future holds, there’s clearly an appetite for the best possible code-reviewing tools. And maybe it’s not hard to understand why.

In [another 2022 presentation](https://www.youtube.com/watch?v=11WQeDdGlgI), Harding said with a smile that “developers naturally have a lot more enthusiasm for writing code than we do for reviewing it.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)