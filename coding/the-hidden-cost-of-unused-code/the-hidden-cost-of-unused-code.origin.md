# The Hidden Cost of Unused Code
![Featued image for: The Hidden Cost of Unused Code](https://cdn.thenewstack.io/media/2024/11/ed293088-xray-1024x576.jpg)
Imagine your doctor showing you a scan of your arteries at the yearly health check. It shows that plaque has been building up over the years and you are heading to a stroke, without you ever feeling the upcoming danger. Your heart’s performance is going down… Do you continue to ignore the problem because you have many other things to do? Or do you prevent bad things from happening by taking immediate action to adjust your lifestyle and slowly recover?

That’s precisely what can happen with the code in your application.

## The Silent Accumulation
Just as cholesterol can build up gradually in our arteries, unused code accumulates in our applications over time without notice. A method gets replaced by another; a feature is no longer used; commented code is checked in; and there is that little part of code that nobody dares to touch… All this unused code limits [developer time and resources](https://thenewstack.io/its-time-to-build-some-empathy-for-developers/) needed to build, run and maintain your applications:

[Unit tests](https://thenewstack.io/expedia-3-tips-for-more-effective-unit-testing/)that need to be executed for methods that are never used. Feedback loops become longer as testing checks unused code. When libraries change or tests flake, you need to investigate the problem and fix it. But in the end, the fixed code is never used in production.- Developers often find their enthusiasm waning as they have to dig through mountains of legacy code just to implement a simple feature or track down a bug. They get distracted from their tasks as they navigate unneeded code. This results in longer development times because your team needs to work around the clutter.
- Deployment packages become bigger, taking up memory, disk space and network traffic.
- Unused code can depend on outdated libraries that introduce security risks. Some of these risks can have a high severity score, screaming for a solution. Such fixes need to be prioritized over work that brings new features, while the fix is actually not needed because the code and
[dependency](https://thenewstack.io/to-reduce-tech-debt-eliminate-dependencies-and-refactoring/)are not used at all.
## Time for a Code Health Check
Just as your body deserves (and needs) a regular health check, your code base deserves (and needs) the same. With the right tools, you can reveal the “buildup of plaque” in your projects that can eventually lead to “productivity blockages.”

There are a few aspects that correlate with buildups of unused code. Generally, the larger and older an application is, the more people there are who have worked on it and the more unused code is sitting around. After monitoring many applications, the ballpark number is nearly 20% of code, going up near 66% in some larger applications. This is not just external dependencies; these numbers filter for companies’ own packages. By trimming down this unused code, developers could save themselves significant time in navigating the clutter to shorter CI/CD feedback loops.

## Take Small Actions
Dealing with unused code does not require drastic action or significant refactoring. Instead, there are ways to deal with it in each sprint to lower the problem and have a large impact of clearing the code blockage.

Start by monitoring code to identify which methods are used and which are unused over a short period. After a brief period, you will often confirm suspicions about certain parts of the code; for other parts, you may monitor for longer.

Smaller teams do not need a formal deprecation process. Start by picking packages, classes or methods that are unused. Tell your colleagues that these will be removed over Slack, at lunch or however you like. Then remove the code: Red diffs are the best diffs.

Larger teams that can’t just talk to everyone can use a process that’s more formal but still simple. Start by marking the code as @Deprecated, indicating to team members and tooling that a certain method or class is not intended for use. Teams can add an additional logging statement to the method as a sort of double comfort. Apply the additional flag @Deprecated (forRemoval=true) when you like, then remove the code in a future update. A short while after that, it’s time to formally say goodbye and remove the code.

Most members of your team who are familiar with the code will have an idea of unused or unneeded code. This allows for a steady process of code improvements by following these steps:

**Monitor code:**Find ways to monitor your code to find unused parts, or have your team review it.**Deprecate:**Using the @Deprecated annotation, we can mark the methods that are candidates for removal.**Continue monitoring:**Build tools will alert you when deprecated methods are still used.**Adjust tests:**Refactor the unit tests reported to be using deprecated code.**Remove deprecated code:**You can safely remove it when your monitoring doesn’t reveal any problems.**Cycle:**Keep repeating this process. Cleaning up big projects with a long history will take some time. However, this process will eventually result in an easier-to-maintain, more efficient codebase.
[Azul Intelligence Cloud’s Code Inventory](https://www.azul.com/products/intelligence-cloud/) can help you in the monitoring step by providing insights to help you make informed decisions about your code health. Code Inventory provides detailed insights into code usage patterns. You can compare it to a continuous monitor for your codebase, showing exactly which classes and methods are being used in production — with zero performance impact on your running applications.
With such a good health plan, you’ll achieve faster deployment times, reduced maintenance costs, improved developer productivity, lower security risks and better application performance.

## Conclusion
As you might work with a health professional to improve your physical fitness, Azul is here to help you with your code health. Contact our sales team to get you started with Intelligence Cloud and find the unused spots in your code.

Start today. Your codebase’s health can’t wait.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)