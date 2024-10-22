# New GitHub Features for Issues Tracking — and Memories of Its Past
![Featued image for: New GitHub Features for Issues Tracking — and Memories of Its Past](https://cdn.thenewstack.io/media/2024/09/184b0282-github-1024x683.png)
On Oct. 1, GitHub [launched](https://github.blog/changelog/2024-10-01-evolving-github-issues-public-beta/) a public beta for a “major evolution of issues and projects,” promising highly requested enhancements that “make it easier than ever to break down work, visualize progress, categorize and find just the right issue in GitHub.”

As one of the most popular code-hosting sites, any changes at GitHub — now owned by [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) — will ultimately affect millions of organizations, and [over 100 million developers](https://github.blog/news-insights/company-news/100-million-developers-and-counting/). So it’s worth taking a look at exactly what’s being introduced — and how developers are reacting today.

And to also take a moment to remember how far we’ve come…

## A Traditional Bug Tracker
Just 14 months after GitHub launched in 2008 — when it had a mere 100,000 users, [according to CNBC](https://www.cnbc.com/2018/06/04/chris-wanstrath-co-founded-github-which-microsoft-bought-for-billions.html) — it launched its first issue tracker.

And at least one user was skeptical. “It is a nice basic and traditional issue tracker, but at least what is exposed is nowhere near any of the interesting issue trackers built on top of git that people have been playing around with the past year,” [complained](https://news.ycombinator.com/item?id=566290) a 2009 comment on Hacker News.

History will remember that this drew [a response](https://news.ycombinator.com/item?id=566341) from Chris Wanstrath — GitHub’s CEO — who posted (from his own Hacker News account *defunkt*) that a “nice basic and traditional” issue tracker was “exactly what it’s meant to be. We’re not in the business of building fancy bug trackers :) ”

But that was just the beginning. “I was there 2010-2015,” remembers developer Zach Holman — one of GitHub’s first engineering hires, according to his [website](https://zachholman.com/about), “and helped build and grow their product and culture over five years, from nine employees all the way to 250.”

In an email interview with The New Stack, Holman agreed that CEO Wanstrath’s promise of a “nice basic and traditional” issue tracker “really summed up my kind of feelings on Issues. It’s the biggest issue tracker in the world, so you’re somewhat constrained with what you can really *do* and support from GitHub’s point of view… We had a ton of ideas about the ‘right’ way of tackling issues and doing software development in general, but companies do things *so many* different [ways in practice, so GitHub kind of](https://thenewstack.io/nvidia-ceo-details-a-new-ai-way-of-developing-software/) ends up being the neutral, unopinionated tool.

But he’s still seen a lot of history. “The last big ship I did was Issues Three, which was basically the version of GitHub Issues that wasn’t really touched until a week or two ago when they started previewing the new stuff.”

Holman [shared his memories](https://thenewstack.io/linux-at-30-early-converts-share-memories-of-their-journey/) as a new era is about to begin.

## How ‘Issues’ Evolved
Holman remembers the first upgrade to GitHub’s original Issues “was a lot more Ajax-y and more… complicated.” So when tackling [Issues 3](https://markdotto.com/2014/08/04/shipping-the-new-github-issues/) back in 2014, “My main approach was to make the main focus be a single column instead of the three-column craziness from before, and [put search at the top](https://github.blog/news-insights/the-library/the-new-github-issues/).”

And GitHub’s position as a neutral, unopinionated tool “is also helpful because lots of third-party tools build on top of GitHub Issues (and pull requests…) So yeah — the goal is kind of… let’s do a more basic approach that’s extendable for the opinionated ecosystem to be able to grow around it.”

But work on updates has continued over the years — and this month GitHub is ready to unveil a whole new round of features.

The highlights in this latest round of new features include:

- Sub-issues
- Issue types
- Advanced issue-searching options
GitHub’s goal was keeping things “fast and familiar,” according to their announcement, so the new features were added on to their existing issues frontend. There are also some minor improvements, like a new “copy link” button to make URL-sharing easier. (And when reviewing long issues for comments and other events, “selecting ‘load more’ will now fetch 150 events instead of 50.”)

[Signups](https://github.com/features/issues/signup) are only available for organizations — but beta testers are already reporting on their experience…
## Sub-Issues!
Sub-issues are perhaps the biggest change. In the new public beta, “Sub-issues add support for hierarchies of issues,” explains GitHub’s [Issues documentation](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues), noting you can create “multiple levels” of sub-issues.

Up to eight levels of nested sub-issues are allowed, according to GitHub’s [community discussion about the feature](https://github.com/orgs/community/discussions/139932#discussioncomment-10817810) — and each parent issue can have up to fifty sub-issues.

But every sub-issue always contains a link back to its parent issue below its title — even if that parent issue came from an entirely different repository. (One feature being discussed: Actually displaying that repository’s name in the sub-issue list…)

Every GitHub issue description in the public beta now features a button at the bottom labeled “Create sub-issue,” with a drop-down menu that lets you make existing issues into sub-issues. Sub-issues can be created just by pasting in the URL of an issue — or by finding it with a search. And best of all, a toggle lets you then collapse (or expand) all sub-issues, instantly de-cluttering your view.

GitHub is also considering whether to let pull requests also be added as sub-issues — because, as one developer [pointed out](https://github.com/orgs/community/discussions/139932#discussioncomment-10821434), “it feels like it’d be very fitting for the pull requests to be located alongside/as a sub of the issue they’re closing.”

And the community discussion also included some general [positive feedback](https://github.com/orgs/community/discussions/139932#discussioncomment-10916234).
“Thank you for pushing this new feature through. Sub-issues are clearly an essential improvement for modern project management.”

## Issue Types
Another new beta feature is Issue types, which aim for a “shared and consistent language” across an organization’s repository. (Default types are *task*, *bug*, and *feature*, but they can be customized by organization administrators.)

And not only will the type be displayed on issue lists (and in the issues themselves). “You can [filter](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#filtering-by-issue-type) and search by issue type,” explains the feature’s [documentation](https://docs.github.com/en/issues/tracking-your-work-with-issues/configuring-issues/managing-issue-types-in-an-organization). “We are continuing to improve the Issues experience, and so we’d love to hear your feedback…”

GitHub senior product manager Riley Broughten [explained in a comment](https://github.com/orgs/community/discussions/139933#discussioncomment-10824654) how they differ from labels. “Issue types are managed at the organization level for a global classification of an issue, while labels are managed at the repository level. This [ensures that issues are classified consistently](https://thenewstack.io/ensure-consistency-in-hybrid-clouds-with-amazon-web-services-eks-d-and-istio/) across repositories…

Or, as one [commenter](https://github.com/orgs/community/discussions/139933#discussioncomment-10882191) put it, “we are liking the org-level types as that removed a pain point of keeping labels in sync across several repos…”

GitHub is also testing [enhanced searching for issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests#building-advanced-filters-for-issues), adding “AND” and “OR” keywords (as well as parentheses)

This allows users to build more complex filters to find the exact set of issues you’re looking for….

## Reactions and React
Earlier this month Holman shared his reaction in a comment on X.

I built the last major update to GitHub Issues over a decade ago now, and I was… kind of hoping for more. Feels more like it’s checkbox-driven development instead of sitting down and really planning long-term about what improvements could be made.

[https://t.co/AhazpHFKTH]— Zach Holman (@holman)

[October 1, 2024]
“Also it has React,” Holman added.

In our email interview, Holman acknowledged that “I’m kind of… okay with the recent new Issues changes.” And in at least one way, there’s a sense of completion. “One thing they finally did was put more autocomplete and smarts around the search bar, which was the natural extension I was going to do next in 2015/16 had I stuck around longer.”

Holman also [posted on X about a JavaScript error he’d found](https://www.twitter.com/holman/status/1842241385912746438)…)

github's move from html to javascript is going great

[pic.twitter.com/6fcvEfTIdF]— Zach Holman (@holman)

[October 4, 2024]
It’s a reminder we’re living in a different era, Holman seemed to say in our email interview. “The earlier versions of Issues were all effectively built with two-person teams, which is how we did the majority of our product work well into scaling into being a ‘large’ site.”

Now Holman watches as GitHub performs “a multi-year push to move Issues (and the rest of the site) to React and GraphQL, in spite of the user and performance challenges in doing so.”

Holman also told The New Stack that “after GitHub shipped Issues they put a moratorium — again — on React/GraphQL until they move to yet another framework that they’re looking to use going forward.”

“Part of that is just life… GitHub is a huge, huge organization now, and you can’t push things through without dozens and dozens of people working on something. Such is life. But also why I like working in startups instead of large companies…”

GitHub’s announcement of the new issues also drew 110 upvotes [on Hacker News](https://news.ycombinator.com/item?id=41708174) — and an even wider variety of reactions:

- “They’d already made it borderline too complicated, this will complete the transition from productivity to ‘legibility’…”
- “[I] like these new changes and I’m looking forward to even more to
[dependencies between issues](https://github.com/github/roadmap/issues/956).” - “They should have some AI solution categorize the issues and separate actual issues/tickets from support requests and other noise.”
- “A big part of the problem is the name ‘issues’. A lot of large projects have dozens or even close to a hundred feature requests and other non-issue ‘issues'”
- “If we can’t effectively communicate work priorities between titles, comments & labels, maybe we need to go back to email for a while.”
But this also resembles past reactions. Speaking of their original Issues system in 2011, GitHub [acknowledged](https://github.blog/news-insights/issues-2-0-the-next-generation/), “Some people love it, some people hate it” — while announcing Issues 2.0. (New features included the ability to assign issues…)

At almost the same moment, another 2011 blog post announced a GitHub Issues iPhone app — though the top of that post now reminds readers the app [is no longer supported](https://github.blog/news-insights/the-library/announcing-github-issues-for-iphone/). Yet it was just three years later, in 2014, that GitHub added its now-familiar dropdown menus below the search box to filter results by author, label, milestone, or open/close state.

It’s a good reminder that Issue features will come and go—some popular, some forgotten — as we embark on the next round of improvements. While supplying their own critiques and suggestions, at least [one GitHub user](https://github.com/orgs/community/discussions/139932#discussioncomment-10879862) also made sure to pass on this message to GitHub’s developers: “I love the update.

“The new features are hugely helpful…!”

🆕 We’ve made several enhancements to GitHub Issues and Projects with sub-issues, issue types, and advanced search! 🎉

Learn more and sign up for the public preview. ⬇️

[https://t.co/5j3GZgpc8b]— GitHub (@github)

[October 2, 2024]
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)