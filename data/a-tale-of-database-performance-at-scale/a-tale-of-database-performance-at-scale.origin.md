# A Tale of Database Performance at Scale
![Featued image for: A Tale of Database Performance at Scale](https://cdn.thenewstack.io/media/2025/01/4e148000-database-1024x569.png)
Lured by impressive buzzwords like “hybrid cloud,” “serverless” and “edge first,” Joan readily joined a new company and started catching up on its technology stack. Her first project recently started a transition from the in-house implementation of a database system, which does not scale at the same pace as the number of customers, to one of the industry-standard database management solutions.

The new pick was a distributed database, which, as opposed to NoSQL, strives to keep the original ACID (atomicity, consistency, isolation, durability) guarantees known in the SQL world.

Due to a few new data-protection acts that tend to appear annually nowadays, the company’s board decided that it would maintain its own data center instead of using one of the popular cloud vendors for storing sensitive information.

On a very high level, the company’s main product consisted of only two layers:

- The
[frontend](https://thenewstack.io/frontend-development/), the entry point for users, which runs in its own browsers and communicates with the rest of the system to exchange and persist information. - The everything else, customarily known as “backend,” but actually includes load balancers, authentication, authorization, multiple cache layers, databases, backups and so on.
Joan’s first introductory task was to implement a simple service for gathering and summing up various statistics from the database and integrate that service into the whole ecosystem so that it fetches data from the database in real time and allows the DevOps teams to inspect the statistics live.

To impress management and reassure them that hiring her was their best decision this quarter, Joan decided to deliver a proof-of-concept implementation on her first day. The company’s unspoken policy is to [write software in Rust](https://thenewstack.io/adoption-of-rust-whos-using-it-and-how/), so she grabbed the first driver for the database from a brief crates.io search and sat down to her self-organized hackathon.

The day went by smoothly, with Rust’s ergonomy-focused ecosystem providing a superior developer experience. But then Joan ran her first smoke tests on a real system. Disbelief turned to disappointment and helplessness when she realized that every third request (on average) ended up in an error, even though the whole database cluster reported to be in a healthy, operable state. That meant a debugging session was in order.

Unfortunately, the driver Joan hastily picked for the foundation of her work, even though open source on its own, was just a thin wrapper over precompiled, [legacy C code](https://thenewstack.io/linus-torvalds-c-vs-rust-debate-has-religious-undertones/), with no source to be found. Fueled by a strong desire to solve the mystery and a healthy dose of fury, Joan spent a few hours inspecting the network communication with Wireshark, and she made an educated guess that the bug must be in the hashing key implementation ([it happens](https://github.com/apache/cassandra/blob/56ea39ec704a94b5d23cbe530548745ab2420cee/src/java/org/apache/cassandra/utils/MurmurHash.java#L31-L32)).

In the company’s database, keys are hashed to later route requests to appropriate nodes. If a hash value is computed incorrectly, a request may be forwarded to the wrong node that can refuse it and return an error instead.

Unable to verify the claim due to missing source code, Joan decided on a simpler path — ditching the originally chosen driver and reimplementing the solution on one of the officially supported, open source drivers backed by the database vendor with a solid user base and regularly updated release schedule.

## Joan’s Diary of Lessons Learned, Part I
The initial lessons include:

- Choose a driver carefully. It’s at the core of your code’s performance, robustness and reliability.
- Drivers have bugs too — and it’s impossible to avoid them. Still, there are good practices to follow:
- Unless there’s a good reason, prefer the officially supported driver (if it exists).
- Open source drivers have advantages: They’re not only verified by the community; they also allow deep inspection of the code (and even modifying the driver code to get even more insights for debugging).
- It’s better to rely on drivers with a well-established release schedule since they are more likely to receive bug fixes (including for security vulnerabilities) in a reasonable period of time.
- Wireshark is a great open source tool for interpreting network packets. Give it a try if you want to peek under the hood of your program.
The introductory task was eventually completed successfully, which made Joan ready to receive her first real assignment.

## The Tuning
Armed with the experience gained working on the introductory task, Joan started planning how to approach her new assignment: a misbehaving app. One of the applications notoriously caused stability issues for the whole system, disrupting other workloads each time it experienced any problems. The rogue app was already based on an officially supported driver, so Joan could cross that one off the list of potential root causes.

This particular service was responsible for injecting data backed up from the legacy system into the new database. Because the company was not in a great hurry, the application was written with low concurrency in mind to have low priority and not interfere with user workloads.

Unfortunately, once every few days something kept triggering an anomaly. The normally peaceful application seemed to be trying to perform a denial-of-service attack on its own database, flooding it with requests until the backend got overloaded enough to cause issues for other parts of the ecosystem.

As Joan watched metrics presented in a Grafana dashboard clearly suggest that the rate of requests generated by this application started spiking around the time of the anomaly, she wondered how this workload could behave like that. It was, after all, explicitly implemented to send new requests only when fewer than 100 were in progress.

Since collaboration was heavily advertised as one of the company’s “spirit and cultural foundations” during the onboarding sessions with an onsite coach, she decided it’s best to discuss the matter with her colleague, Tony.

“Look, Tony, I can’t wrap my head around this,” she explained. “This service doesn’t send any new requests when 100 of them are already in flight. And look right here in the logs: 100 requests in progress, one returned a timeout error and …” She stopped, startled at her own epiphany.

“Alright, thanks Tony, you’re a dear — best [rubber duck](https://rubberduckdebugging.com/) ever!” she said, returning to fixing the code.

The observation that led to discovering the root cause was rather simple: The request didn’t actually *return* a timeout error because the database server never sent back such a response. The request was simply qualified as timed out by the driver and then discarded.

But the fact that the driver no longer waits for a response for a particular request does not mean the database is done processing it. It’s possible that the request instead just stalled, taking longer than expected, but the driver gave up waiting for its response.

With that knowledge, it’s easy to imagine that once 100 requests time out on the client side, the app might erroneously think that they are not in progress anymore and happily submit 100 more requests to the database, increasing the total number of in-flight requests (concurrency) to 200. Rinse, repeat and you can achieve extreme levels of concurrency on your database cluster — even though the application is supposed to keep it limited to a small number.

## Joan’s Diary of Lessons Learned, Part II
The lessons continue:

- Client-side timeouts are convenient for programmers, but they can interact badly with server-side timeouts. Rule of thumb: Make the client-side timeouts around twice as long as server-side ones, unless you have an extremely good reason to do otherwise. Some drivers may be capable of issuing a warning if they detect that the client-side timeout is smaller than the server-side one, or even amend the server-side timeout to match, but in general it’s best to double-check.
- Tasks with seemingly fixed concurrency can actually cause spikes under certain unexpected conditions. Inspecting logs and dashboards is helpful in investigating such cases, so make sure that observability tools are available both in the database cluster and for all client applications. Bonus points for distributed tracing, like
[OpenTelemetry](https://opentelemetry.io/)integration.
With client-side timeouts properly amended, the application choked much less frequently and to a smaller extent, but it still wasn’t a perfect citizen in the distributed system. It occasionally picked a victim database node and kept bothering it with too many requests, while ignoring the fact that seven other nodes were considerably less loaded and could help handle the workload too.

At other times, its concurrency was reported to be exactly 200% larger than expected by the configuration. Whenever the two anomalies converged in time, the poor node was unable to handle all the requests it was bombarded with. It had to give up on a fair portion of them.

A long study of the driver’s documentation, which was fortunately available in [mdBook](https://rust-lang.github.io/mdBook/) format and kept reasonably up to date, helped Joan alleviate those pains too.

The first issue was simply a misconfiguration of the non-default load balancing policy, which tried too hard to pick “the least loaded” database node out of all the available ones, based on heuristics and statistics occasionally updated by the database itself. Unfortunately, this policy was also “best effort,” and relied on the fact that statistics arriving from the database were always legit, but a stressed database node could become so overloaded that it doesn’t send updated statistics in time.

That led the driver to falsely believe that this particular server was not actually busy at all. Joan decided that this setup was a premature optimization that turned out to be a footgun, so she just restored the original default policy, which worked as expected.

The second issue (temporary doubling of the concurrency) was caused by another misconfiguration: an overeager speculative retry policy. After waiting for a preconfigured period of time without getting an acknowledgment from the database, drivers would speculatively resend a request to maximize its chances to succeed. This mechanism is useful to increase requests’ success rate. However, if the original request also succeeds, it means that the speculative one was sent in vain.

To balance the pros and cons, speculative retry should be configured to only resend requests if it’s very likely that the original one failed. Otherwise, as in Joan’s case, the speculative retry may act too soon, doubling the number of requests sent (and thus also doubling concurrency) without improving the success rate at all.

Whew, nothing gives a simultaneous endorphin rush and dopamine hit like a quality debugging session that ends in an astounding success (except writing a cheesy story in a deeply technical publication, naturally). Great job, Joan!

**Want to read more? “**[Database Performance at Scale,” a free open source book](https://www.scylladb.com/2023/10/02/introducing-database-performance-at-scale-a-free-open-source-book/), offers a similarly cheesy database performance story plus tons of practical advice for understanding and overcoming your own database performance challenges.
Also, Piotr Sarna will be speaking at [Monster Scale Summit,](https://www.scylladb.com/monster-scale-summit/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) a new (free and virtual) conference on extreme scale engineering and data-intensive applications held March 11-12. Engineers from Canva, Slack, Disney+/Hulu, Netflix, Salesforce, Atlassian and more will share strategies and case studies.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)