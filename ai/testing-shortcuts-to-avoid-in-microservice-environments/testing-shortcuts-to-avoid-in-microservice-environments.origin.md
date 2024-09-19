# Testing Shortcuts to Avoid in Microservice Environments
![Featued image for: Testing Shortcuts to Avoid in Microservice Environments](https://cdn.thenewstack.io/media/2024/09/e7c91d21-shark-1024x576.jpg)
What are the dangers of a quick fix? It seems like I could publish an article with an evergreen opener reading “given the most recent major tech outage,” but my mind goes back to the Southwest Airlines outage of 2023.

In that case, for years the cost of major IT overhauls prevented Southwest from [upgrading its system](https://thenewstack.io/faa-flight-cancellations-a-lesson-in-application-resiliency/), until its entire network, which was still based on automated phone routing systems, crashed. Planes and crews had to be flown home empty, the worst possible inefficiency, just to give its systems a place from which to start over. A literal “have you tried turning it off and on again”?

The Southwest example is one of truly ancient architecture, but the problem of prioritizing easy solutions over quality affects modern microservice architectures as well. In the world of microservice architecture, we see engineers valuing the speed of [testing and QA](https://roadmap.sh/qa) over the quality of information received.

In general, this looks like optimizing for the fastest way to test new code changes without a focus on the reliability of the information gained from those tests.

**The Challenges of Growth**
When we see a system that’s clearly not working for an organization, the explanation is almost always the same: This was a great solution at a different scale. Monoliths made tons of sense when a web server fit reasonably well on a PC. And as we scale up beyond single instances and single machines, the [solutions to problems of testing](https://thenewstack.io/shifting-testing-left-the-request-isolation-solution/) and consistency can often be solved by “quick fixes” that work well for a given scale.

What follows is a list of the ways that platform teams take shortcuts to make testing and releasing code to “just work”’ as they increase in scale, and how those shortcuts come back to bite you.

**How Platform Teams Prioritize Speed Over Quality**
I’d like to go over some of the failure modes we see in modern architecture teams.

**Over-Rotating to Unit Testing**
Talking to multiple platform engineers, one of the recent themes has been a renewed emphasis on unit testing. Unit testing is an appealing option since, generally running on a developer’s laptop, it runs quickly and efficiently.

In an ideal world, the service each developer is working on would be nicely isolated from others, and with a clear spec for the performance of the service, unit tests should cover all test cases. But sadly we develop in the real world, and interdependence between services is common. In cases where requests pass back and forth between related services, unit tests struggle to test in realistic ways. And a constantly updated set of services means that even efforts to document requirements can’t stay up to date.

The result is a situation where code that passes unit [tests can’t be relied on to work correctly on staging](https://thenewstack.io/why-staging-doesnt-scale-for-microservice-testing/) (or whatever other environment you deploy to before production). When developers push their pull requests without being certain they’ll work, their testing is faster, but the time to get real feedback is slower. As a result, the developer’s feedback loop is slower. Developers wait longer to find out if their code passes integration testing, meaning that implementation of features takes longer. Slower [developer velocity is a cost](https://thenewstack.io/cutting-the-high-cost-of-testing-microservices/) no team can afford.

**Providing Too Many Environments**
The problem of waiting to find problems on staging can suggest that the solution is to clone staging. With multiple teams trying to push their changes to a single staging environment, if we clone that environment surely we’ll increase speed. The cost of this solution comes in two pieces: infrastructure costs and loss of reliability.

Keeping dozens or hundreds of environments up and running for developers comes with real infrastructure costs. I once heard a story of an enterprise team spending so much on these replica clusters that they calculated in one month they’d spent nearly a quarter of their infrastructure cost on dev environments, second only to production!

Setting up multiple lower-order environments (that is, environments that are smaller and easier to manage than staging) has a number of drawbacks, the biggest being test quality. When tests are run with mocks and dummy data, the reliability of passing tests can become quite low. We run the risk of maintaining (and paying for) environments that really aren’t usable for testing.

Another concern is synchronization; with many environments running clones of a service, it’s very difficult to keep all those services updated.

In a recent case study with Fintech company Brex, platform developers talked about a system of namespace replication, which had the advantage of giving every developer a space to do integration tests, but that many environments were very difficult to keep updated.

Eventually, while the platform team was working overtime to keep the entire cluster stable and available, the developers noticed that too many services in their cloned namespaces weren’t up to date. The result was either developers skipping this stage entirely or relying on a later push to staging to be the “real testing phase.

Can’t we just tightly control the policy of creating these replicated environments? It’s a difficult balance. If you lock down the creation of new environments to require highly qualified use, you’re preventing some teams from testing in some situations, and hurting test reliability. If you allow anyone anywhere to spin up a new environment, the risk increases that an environment will be spun up to be used once and never again.

**A Totally Bullet-Proof QA Environment**
OK, this seems like a great idea: We invest the time in making a near-perfect copy of staging, or even prod, and run it as a perfect, sacrosanct copy just for testing releases. If anyone makes changes to any component services, they’re required to check in with our team so we can track the change back to our bullet-proof environment.

This does absolutely solve the problem of test quality. When these tests run, we are truly sure that they’re accurate. But we now find we’ve gone so far in pursuit of quality that we abandoned speed. We’re waiting for every merge and tweak to be done before we run a massive suite of tests. And worse, we’ve gone back to a state where developers are waiting hours or days to know if their code is working.

**The Promise of Sandboxes**
The emphasis on quick-running tests and a desire to give [developers their own space to experiment](https://thenewstack.io/7-reasons-why-developer-experience-is-a-strategic-priority/) with code changes are both laudable goals, and they don’t need to slow down developer velocity or break the bank on infra costs. The solution lies in a model that’s growing with large development teams: sandboxing either a single service or a subset of services.

A sandbox is a separate space to run experimental services within your staging environment. Sandboxes can rely on baseline versions of all the other services within your environment. At Uber, this system is called a SLATE and its exploration of why it uses it, and why other solutions are more expensive and slower, [is worth a read](https://www.uber.com/blog/simplifying-developer-testing-through-slate/).

**What It Takes To Implement Sandboxes**
Let’s go over the requirements for a sandbox.

If we have control of the way services communicate, we can do smart routing of requests between services. Marked “test” requests will be passed to our sandbox, and they can make requests as normal to the other services. When another team is running a test on the staging environment, they won’t mark their requests with special headers, so they can rely on a baseline version of the environment.

What about less simple, single-request tests? What about message queues or tests that involve a persistent data store? These require their own engineering, but all can work with sandboxes. In fact, since these components can be both used and shared with multiple tests at once, the result is a more high-fidelity testing experience, with tests running in a space that looks more like production.

Remember that even on nice light sandboxes, we still want a time-of-life configuration to close them down after a certain amount of time. Since it takes compute resources to run these branched services, and especially multiservice sandboxes probably only make sense for a single branch, we need to be sure that our sandbox will shut down after a few hours or days.

**Conclusions: Penny Wise and Pound Foolish**
Cutting corners in [microservices testing](https://thenewstack.io/shift-left-on-a-budget-cost-savvy-testing-for-microservices/) for the sake of speed often leads to costly consequences down the line. While duplicating environments might appear to be a quick fix for ensuring consistency, the financial burden of maintaining these setups can escalate rapidly.

The temptation to rush through testing, skip comprehensive checks or rely on incomplete staging setups is understandable under pressure. However, this approach can result in undetected issues, unstable releases and eventually, more time and resources spent fixing problems in production. The hidden costs of prioritizing speed over thorough testing are felt in delayed projects, frustrated teams and lost customer trust.

At Signadot, we recognize that effective testing doesn’t have to come with prohibitive costs or slow down development cycles. Using strategies like dynamic provisioning and request isolation, we offer a way to streamline the testing process while keeping infrastructure costs under control. Our shared test environment solutions allow teams to perform safe, canary-style tests without duplicating environments, resulting in significant cost savings and more reliable staging setups.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)