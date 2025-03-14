# How Slack Transformed Cron into a Distributed Job Scheduler
![Featued image for: How Slack Transformed Cron into a Distributed Job Scheduler](https://cdn.thenewstack.io/media/2025/03/ba6da07a-monster-scale-slack-cron-cover-1024x683.png)
For a decade, Slack ran its cron jobs on a single server. But when the server started having issues and chewing up maintenance time, the company’s admins knew a more resilient job scheduler was needed. So, they turned cron into a distributed system.

In [a talk](https://www.scylladb.com/tech-talk/scaling-cron-at-slack/) at [ScyllaDB](https://www.scylladb.com/?utm_content=inline+mention)‘s [Monster Scale Summit](https://www.scylladb.com/monster-scale-summit/agenda/), held virtually last week, [Claire Adams](https://www.linkedin.com/in/clairebadams/), infrastructure software engineer for [Slack](https://slack.com/what-is-slack), described how the collaboration service provider turned the Unix scheduling utility [Cron](https://thenewstack.io/linux-how-to-use-cron-to-schedule-jobs/) into a distributed service,

“People were really fed up with dealing with this one cron box. Nobody really wanted to maintain it. It had been set a long time ago,” Adams said. “People had some legacy knowledge, but nobody really had total knowledge on all the quirky stuff with it.”

“We needed something more reliable.”

## Cron for One
Like every hardcore [Linux user](https://thenewstack.io/learning-linux-start-here/) knows, [cron](https://man7.org/linux/man-pages/man8/cron.8.html) is a time-based job scheduler, allowing admins to run scripts and apps at specific times and dates, by scheduling them in a file called the [crontab](https://man7.org/linux/man-pages/man5/crontab.5.html).

As you can imagine, [Slack](https://thenewstack.io/a-look-at-the-slacks-new-gitops-based-build-platform/), with over [38 million daily users](https://www.demandsage.com/slack-statistics/), has plenty of tasks to run.

Overall, Slack has about 385 cron scripts that collectively execute 2,000 an hour, which tallies up to 340,000 jobs a week, or 20 million a year.

For Slack, Cron handles tasks to power both user features — such as reminders and e-mail notifications, as well as back-end maintenance duties like database cleaning and running analytic jobs.

For the first 10 years of Slack, cron was run from a single crontab, running on a single server on [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention).

The system had its limitations, however. Especially tricky were software updates, which were done by duplicating the service on another server, then switching over — quickly enough as to not miss any scheduled jobs.

The final straw, however, was that in its last year, the cron server kept stumbling from errant out-of-memory errors, necessitating manual remediation. More downtime.

“We can’t have a lot of incidents that might impact users. We need to be more reliable and more stable as a product,” Adams said. “So that led us to this rewrite.”

## A Distributed Replacement
Clearly, a scheduling system distributed across multiple servers would be needed. Moving to a distributed system, the company hoped to increase reliability, reduce maintenance windows, and gain more insight into the jobs that were run.

There were different approaches the team could take. For instance, Slack is a big Kubernetes user, so they investigated using Kubernetes’s own built-in cron, [cronjob](https://www.youtube.com/watch?v=eVjgXyrcdjM). This approach, however would have required spinning up 53,000 pods a day, and would have been difficult to debug. And would have to require users to rewrite their scripts. So, major hassle.

Nonetheless, “it made sense for us to use the technologies that we had already invested in” she said.

## It Helps To Have a Monster Job Execution Service
In the end, it took three different components to replace the once-mighty cron box.

The system would continue to use cron, which would run the cron scripts without modification. But instead of running the jobs in its own memory, cron would hand them off to a separate job execution engine.

As it happened, the company had already built and maintained an asynchronous computing platform, or job execution service. Based on Kubernetes and written in the [Go programming language](https://thenewstack.io/get-ready-get-set-go-survey-recap/), it was a beast, executing 10 billion jobs a day.

But, remarkably enough, it did not have a scheduler. Just queues. Cron itself is a very good scheduler. And fortunately, Go has a [Cron library](https://github.com/robfig/cron) that could be used. This meant none of the cron scripts would have to be rewritten.

In this setup, all the cron jobs get their own dedicated queue. Each script is wrapped as a job so it can be executed.

Queuing is done through [Kafka](https://thenewstack.io/how-kafka-and-redis-solve-stream-processing-challenges/), with each job getting its own Kafka topic. An AWS EC2 instance actually executes the work.

Because the cron server was not executing the scripts in its own memory, it could still run on a single server.

The design team initially considered an approach of spreading out the scripts across multiple cron servers, but this would lead to a lot of complexity, determining which server should run which script.

Instead, the team went with another approach: leader election with locking.

Instead of having each server execute some of the scripts, a leader server executed all the scripts, handing them off to the job engine. Back-up servers were ready to take over should the primary server fail quickly.

The last piece of the system was a database that would track how the scripts executed. Typically, this information is found in the cron logs recorded on the server, though these are difficult to track down and parse.

Wouldn’t it be better to have a centralized portal where all the statuses were kept, providing info such when the last time the was job run, of if it was successful? This is the role of the database.

## More Components But Easier to Manage
Adding a few more cron scripts to a 10-billion-jobs-a-day monster job executer proved to be no problem. As a bonus, it was a mature, fully supported system.

“We already had invested years to making this job queue system very reliable, very scalable, have good guarantees and have a good on-call rotation and good maintenance,” Adams said, recalling the reasoning of the moment. “So if we can just leverage that, [it would] make our lives a ton easier.”

It’s been about a year since Slack migrated to its distributed cron. The new system has thus far successfully executed over six million scripts. Even better, it has reduced its on-call burden, relieving admins from resetting a server each time it’s befouled by a memory error.

“Even though there are more components, it is easier to maintain,” Adams said.

Adams’ takeaway? Use what you have. In their case, it was an existing job queue, Golang and Kubernetes. “You decrease the maintenance burden while getting huge-scale wins,” she said.

And even the lowly cron box held a lesson or two.

“Slack ran key functionality for 10 years on one node. That’s a long time to deal with this less-than-ideal system. But it was good enough. It got the job done. And I think that is really a key takeaway,” she said. “It’s okay to keep it really simple, even if it’s kind of janky, for a long time.”

“And then, when you’re fed up, you can try something better.”

View the entire presentation here:

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)