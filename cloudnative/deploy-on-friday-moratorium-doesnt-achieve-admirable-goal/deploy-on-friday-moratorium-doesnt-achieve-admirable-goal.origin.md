# Deploy on Friday? Moratorium Doesn’t Achieve Admirable Goal
![Featued image for: Deploy on Friday? Moratorium Doesn’t Achieve Admirable Goal](https://cdn.thenewstack.io/media/2024/08/df335a6a-calendar-1024x642.jpg)
Avoiding Friday deployments is driven by a goal that, while admirable, is better achieved in other ways. Yet, organizations are more likely to deploy on Friday than on a Monday, which shows the industry doesn’t buy the myth that you shouldn’t deploy on Friday.

## Few Practices Are Truly Best Practices
While you used to hear about best practices all the time, you’ll have noticed that industry experts have become increasingly cautious about the term. Best practices do exist, such as using version control instead of a network share to store your source code. Many other practices turn out to be simply good, rather than best.

The idea of best practices is that they are table stakes for software delivery, and working without them can be harmful. Good practices, on the other hand, are options. You don’t have to adopt every good practice, as you can cover risk areas with a carefully selected option from the menu of all tried-and-tested ways to solve a problem.

If your end users are reporting escaped bugs, you can [apply one or more testing](https://thenewstack.io/shift-left-testing-applied-to-kubernetes/) and monitoring good practices to catch similar issues before users experience them. You look at different [testing](https://thenewstack.io/surprise-software-testing-is-every-developers-job-now/) and [monitoring approaches](https://thenewstack.io/observability/) and try one to see its effectiveness. The problem could be solved after you adopt one practice, or it might take several complementary approaches to improve the situation.

Crucially, you should stop adding practices once you’ve solved the problem. Adding further practices that aren’t required results in unnecessary complexity, which can be harmful to software delivery.

Finally, there are practices that are actively harmful when pursued. These are often well-intentioned and almost always presented as best practices, but empirical evidence and rigorous research have proven them to be false. Examples of these harmful practices include Gitflow, working in large batches, and heavyweight change-approval processes.

A good heuristic for spotting an anti-pattern is that you’ve being told something is a best practice, but it doesn’t sound like table-stakes basic software delivery. If there’s any doubt, look for trusted advice from someone with plenty of experience and cross-reference dependable research, such as the Accelerate “[State of DevOps Report](https://services.google.com/fh/files/misc/2023_final_report_sodr.pdf).” (The 2024 report is due out in October.)

## Never Deploy on a Friday
With the practices primer firmly in mind, let’s consider whether we should deploy on Friday. After the recent [CrowdStrike outage](https://thenewstack.io/7-urgent-lessons-from-the-crowdstrike-disaster/), many people suggested things could have been improved if they hadn’t deployed on Friday.

It’s hard to understand how deploying on Thursday would have improved the CrowdStrike issue. Do we not fly planes or use computers on Thursday? We can explore this confusing claim by looking at the perceived benefits of banning Friday deployments.

## Why You Should Avoid Friday Deployments
I asked folks why we should avoid Friday deployments to see if there was some merit to the claims. As someone whose mind was changed on tabs vs. spaces by solid arguments, I believed I could be convinced given a compelling argument.

The most common argument for a Friday moratorium was that it would allow developers to spend the weekend with their families instead of working to restore services.

This is only true if your time to recover from a failed deployment is almost exactly a day. If it takes more than a day, you’ll be working on Saturday to recover from your Thursday deployment, unless you also stop deployments on Thursday. If you can recover in less than a day, you could deploy on Friday and still get to the beach on Saturday.

The longer your recovery times, the further in the past you need to deploy to avoid working on the weekend. For example, if it takes you a week to recover from a failed deployment, you need to deploy last Friday to avoid working this weekend, though this does mean you have to work last weekend.

The reality is that recovery times aren’t constant. Some problems are easier to recover from than others. Having a distribution of recovery times means you are taking a probabilistic approach to protecting the weekend. If you deploy every day, you’ll discover that Friday deployments have a higher probability of disrupting the weekend than Monday deployments.

When you take this approach, you’ll find there are plenty of improvements you can make to your deployment pipeline that reduce the probability of disruption. Banning deployments doesn’t reduce your overall change failure rate, it just means your Monday deployments will fail more often. Improving your deployment pipeline reduces the risk of failed deployments overall, which is far more positive than simply choosing which day will be a bad day.

Work-life balance applies to Monday night just as much as it applies to the weekend. People have personal commitments every day of the week, from school runs to birthdays and anniversaries to arrangements made to meet an old friend. Each of these is important, so making [improvements that reduce failed deployments protects work-life balance](https://thenewstack.io/low-code-tools-improve-devs-work-life-balance-survey-finds/) more than shifting them to a different workday.

## Real Reasons To Plan Deployments
There are reasons to avoid deploying at specific times, but they are related to your industry. For example, in the retail industry, you avoid updating the software on tills when the store is open. You don’t need a new version of software while you’re checking out a customer and have a queue of shoppers waiting.

Your release plan would set out the times to deploy and the times to avoid. It would also capture the process for training retail store staff so they know what’s changed before they raise the shutters.

By thinking of the people affected by our software, we consider many more people than if we just think of ourselves. If we think of all the people depending on our software, we can consider the work-life balance of a thousand times more people. Ideally, we’d never have a failed deployment, and our rollout would have no downtime. In reality, things do sometimes go wrong, and having a strong recovery time can minimize the impact.

The research suggests there are capabilities that let you deploy more often while also reducing the failure rate. The top performers are deploying many times a day, including Fridays.

## Deploying on Friday Is Commonplace
To understand whether the Friday deployment ban was affecting real organizations, I analyzed over 32 million deployments to see when they were taking place. The data cuts across all organization sizes and many industries. It turns out that deploying on Friday is more common than deploying on Monday.

This is great news, as it demonstrates that the myth of avoiding Fridays has little traction in practice.


## Decide for Yourself but Don’t Propagate the Myth
It’s perfectly acceptable for your organization to decide they don’t want to deploy on Fridays, though some curiosity about why will either turn up interesting domain knowledge or highlight some things you can improve in your deployment pipeline. What’s less appealing is broadcasting “don’t deploy on Fridays” as a best practice.

Working in small batches in known to improve software delivery performance. If you are following continuous delivery and DevOps, you might be deploying five times a day. If you rule out Fridays, you build up a Monday deployment that’s five times bigger than your normal batch size. You are opting to downgrade your performance from “on demand” to “daily.”

The more continuously you deploy, the worse the idea of stopping for a day becomes. That means that the members the “don’t deploy on Friday” movement, in the absence of specific organizational context, are opting for mediocrity.

Don’t just start deploying on Fridays. Take this as an opportunity to [assess your situation](https://octopus.com/deployment-capability-assessment), understand users and customers, and start improving your software delivery capabilities.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)