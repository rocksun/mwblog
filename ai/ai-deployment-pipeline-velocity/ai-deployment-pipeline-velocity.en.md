**There’s mounting evidence** **that AI coding tools** are delivering on their less outlandish promises. With adoption shifting from [76% in 2024 to 90% in 2025](https://dora.dev/ai/), we must accept that only the most staunch holdouts are working without AI.

To get a sense of the rate of change flowing through today’s deployment pipelines, we can look at the project deployment rate. This is the number of deployments across all environments for a single application or service each month. If you made a single change and successfully deployed it to dev, test, staging, and production, you’d have a project deployment rate of 4.

Between 2021 and 2025, project deployment rates increased from 357 per month to an average of 988 per month. Even if you have four environments and a 30% change failure rate, that means deploying to production 35 times each working day of the month.

If you still deploy once a week, this is what you’re competing against. It’s not a 10x improvement; it’s 175x. That’s because high-performing teams aren’t using AI alone; they’re amplifying their existing technical excellence and continuous improvement practices.

The really bad news is that since the end of 2025, project deployment rates have streaked past the 1,000-per-month milestone

![](https://cdn.thenewstack.io/media/2026/06/fc2c64da-image3-1024x633.png)

*The rate of change continues to accelerate. Source: Octopus Deploy.*

The rate of increase is variable. The largest climb was 46% in 2024, but even the leanest was an impressive 17%. These gains compound over time. The waves vary in magnitude, but the tide only rises.

Some leaders are responding to this competitive pressure by demanding that teams deliver more code faster. However, a more sophisticated approach is needed than flat-out speed.

## Speed Without Direction Is Wasted

There’s a cautionary tale to keep in mind as you look at the rate of change and consider how you’ll move from weekly to daily to continuous deployments. The effectiveness of this rapid approach will depend entirely on product velocity, which is a combination of speed and direction.

Imagine an archery target with a bullseye at its center. The bullseye is the ideal version of your product. It’s better, faster, safer, and cheaper than the competition. You already have some idea of the gap between your current product and the ideal product if you have a roadmap.

Each change you make to the software as part of your planned roadmap is an arrow flying toward the target. You hope that each arrow will be closer to the bullseye than the last, but when you’re solving complex problems, it’s not guaranteed to be.

The line between the previous arrow and the one that just landed indicates your product velocity. If it’s moving closer to the bullseye, the change is helping you achieve your goals. If you’re drifting away from the bullseye, you’re learning important lessons that should improve your accuracy on subsequent shots.

Only a careless organization celebrates speed without paying attention to direction.

![](https://cdn.thenewstack.io/media/2026/06/70125379-image1-1008x1024.png)

*Vectors have distance and direction.*

With the Bullseye Model, increasing your project deployment rate gives you more shots, more knowledge, and more chances of reaching that ideal state, as long as you check where the arrows hit the target. In Continuous Delivery, much of that checking is automated. Is the software stable? Does it behave as we planned? Does it comply with our security policies?

The part that isn’t automated is sharing your changes with the people who use the software and finding out whether it solves a valuable problem for them.

So, speed does matter, but it’s not the goal. Your ultimate aim is to reach the bullseye, but being able to smoothly and quickly deliver arrows creates more opportunities to check your vector and adjust course. Crucially, when you start trending away from the center, you can rapidly reverse course without over-investing in the wrong approach. You might start building an “offline mode” only to discover users are confused by how you’ve implemented it, or that they don’t value the idea at all and would prefer to be notified when they are back online.

Any speed you have in excess of your ability to check your vector and change course is wasted, as it’s as likely to move you rapidly away from the bullseye as it is to move you closer. You need to develop feedback cycles in concert with your software delivery throughput, while maintaining stable operations.

Moving in the right direction is the primary concern, and high-throughput is a valuable way to increase the frequency with which you check your vector.

![](https://cdn.thenewstack.io/media/2026/06/66e5a549-image2-1008x1024.png)

*Modest progress in the right direction always beats a great leap in the wrong directio*n

## AI Makes Deployment Pipelines Crucial

The introduction of AI-assisted software development enables teams to increase their throughput. There are preconditions for this to be true: the techniques and practices described in Continuous Delivery, like test automation, automated deployments, and streamlined change approvals, as evidenced by research programs like [DORA](https://dora.dev/research/?view=detail).

When you increase change throughput, you must adapt to this rate of change in other areas, or queues will eat all your gains. Manual stages in your deployment pipeline need refinement. You may automate, augment, or prioritize them, but leaving them as they were before AI-assisted development is not an option.

Deployment governance has become crucial in regulated organizations and those working at scale, as fragmented governance processes will result in a total loss of all return on your AI investments. Your default path to production must be the easiest, safest, and most compliant way to deliver changes, with no exceptions or expediting.

The Bullseye Model also reminds you that the rate at which you can collect and absorb feedback is a crucial consideration of how quickly you can introduce changes. If you can’t tell if a change is moving you toward the ideal product, you’re simply spinning out of control.

While your competitors are counting token use, pull requests, or lines of code, the thing that you should focus on above all else is how rapidly we are closing the gap between where your product is today and the ideal product described in our roadmap.

## The Crucial Question

So, here’s the question for every engineering leader. Has your deployment pipeline scaled at the same rate as your code output? You can tell it hasn’t if you see an uptick in developer activity without an associated increase in user satisfaction, win rates for new business, or money arriving in the bank.

You need to pay attention to where the arrows are landing and close the feedback loops to achieve the required change in direction. If the arrows are hitting obstacles placed before the target, like heavyweight change approval processes or out-of-band reviews and sign-offs, they need to be fixed, too.

The next competitive frontier isn’t about generating more code. Every team has access to the same tools. Your deployment pipeline is the competitive edge to discovering your ideal product and producing something that looks ever closer to it. The metric that matters is how rapidly you’re moving toward the bullseye, and that requires a pipeline that can keep pace.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/06/0d969cd0-u85necb0yelklkgxjdlge4uqo93nsanbq9ewfhzmyng.png)

Paul and Sonia Stovell founded Octopus Deploy in 2012. In the years before, Paul had watched programmers at organizations of all sizes routinely remote into production machines to patch configuration files or write long and semi-complete documents because automating deployments...

Read more from Paul Stovell](https://thenewstack.io/author/paul-stovell/)