# Why Now Is the Time to Migrate From Redis to Valkey
![Featued image for: Why Now Is the Time to Migrate From Redis to Valkey](https://cdn.thenewstack.io/media/2024/11/128b3026-migration-1024x576.jpg)
Redis’s decision earlier this year to shift the world’s most popular NoSQL database away from the open source licensing that earned it that popularity was met with rapid response. Within weeks, former members of the Redis community and major industry players — including [AWS](https://aws.amazon.com/?utm_content=inline+mention), [Google](https://cloud.google.com/?utm_content=inline+mention) and the [Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) — were aligned in support of [Valkey](https://valkey.io/) as a fork of, and fully open source replacement for, Redis.

But the change also left teams deciding which path to take in the wake of the Redis shift. For those that count Redis among the key technologies fueling their data layer, my recommendation is to make the move to Valkey — and to [complete that migration](https://thenewstack.io/how-we-completed-a-massive-kafka-and-cassandra-migration/) as soon as possible. Because [Valkey is a fork of Redis](https://thenewstack.io/valkey-is-a-different-kind-of-fork/), its codebase [started out as identical to Redis](https://thenewstack.io/valkey-a-redis-fork-with-a-future/) and remains highly compatible. However, that will become less so as time goes on. In other words: the switching costs associated with a Redis-to-Valkey migration are now as low as they’re ever going to be.

Let’s look at some of the core questions teams are asking about their potential migrations to Valkey, including the benefits of the move and how to complete a transition that is as seamless as possible.

## What to Expect If You Simply Keep Using Redis
Given that Redis previously stated its commitment to keeping the solution fully open source — a commitment that was not kept — users should expect the company to make whatever licensing changes it finds useful to support its own goals from here on out. That means there’s no guarantee against further restrictions and costs, up to and including the vendor and technical lock-in that so often becomes a risk in cases where companies move away from [open source licensing](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/).

Teams currently using Redis should therefore brace for new licensing and service fees, and the likelihood of the software increasingly catering to priorities not their own. Similar examples of formerly open-source software companies going down Redis’s route, such as Elastic and MongoDB, each saw those companies put their resources into closed-source offerings while their free community versions languished and lost contributors. It’s fair to assume Redis may follow a more or less similar trajectory.

## So, Why Valkey?
Looking at the landscape of available Redis alternatives, Valkey stands out as the ideal open source in-memory data store and heir to the Redis community — in no small part because it’s literally the current solution of choice for many of that community’s former members and partners. Valkey continues with the same open source licensing and the same single-threaded C familiar to Redis users. Other alternate options like Garnet, Redict, KeyDB and DragonflyDB cannot claim the same.

With major [cloud providers like AWS](https://thenewstack.io/aws-adds-support-drops-prices-for-redis-forked-valkey/) and Google supporting Valkey, organizations can also be confident that the project will remain [tuned to their requirements](https://thenewstack.io/valkey-whats-new-and-whats-next/) for operating efficiently and reliably while using cloud resources at scale. Valkey’s current performance and reliability characteristics match Redis’s from a technical perspective, but that may change as the two evolve in their own directions. At the same time, Valkey’s major draw is in eradicating any current or future licensing costs, delivering a lighter total cost of ownership than Redis in its closed iterations going forward.

## How Should Teams Proceed With a Migration to Valkey?
As a Redis fork, Valkey begins with a lot of advantages for smooth and successful enterprise migrations from Redis. Valkey nodes can join existing Redis or Valkey clusters, offering a clear migration path that teams should take advantage of.

Redis and Valkey also use the same command line and API calls, making migration and operation easy for experienced Redis users. Because of Valkey’s prominence as a popular replacement for Redis, organizations can also easily tap into managed support options if additional expertise for migration and optimization (particularly at scale) is necessary.

## Redis and the State of Open Source Data-Layer Technology
From Elastic to [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention) to [Red Hat](https://www.openshift.com/try?utm_content=inline+mention), and now Redis, many data companies have followed the path of developing open source solutions and then shifting their business models to generate revenue via closed source licensing and subscriptions.

While some companies have found success with closed models, this commercialization of open source software is also responsible for conflicts of interest, reduced community involvement and fragmentation of software ecosystems.

The future of open source will depend on a balance between commercial interests and community-driven collaboration. Further organizations that try to commercialize open source software will need to maintain strong connections with open source communities and ensure that the core principles of openness and collaboration are upheld. Where they don’t, communities will step in with Valkey-like solutions to close that gap.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)