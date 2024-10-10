# Buildkite Expands Scale-Out Continuous Delivery Platform
![Featued image for: Buildkite Expands Scale-Out Continuous Delivery Platform](https://cdn.thenewstack.io/media/2024/10/e6c1ea3d-buildkite-1024x683.png)
[Buildkite Pty Ltd](https://buildkite.com/) has expanded its namesake concurrency-minded [continuous integration and delivery software](https://thenewstack.io/ci-cd/) to make it a full-fledged platform, adding in a test engine, a package registry service and a mobile delivery cloud.
Launched a decade ago, by now Buildkite CEO [Keith Pitt](https://x.com/keithpitt), the software was designed to run concurrently, allowing users to run a hundred times as many agents compared to traditional build pipelines.

As a result, the software found use in many scale-out companies, being put to work at Airbnb, Canva, Lyft, PagerDuty, Pinterest, PlanetScale, Shopify, Slack, Tinder, Twilio, Uber and Wayfair, among others.

On TNS, we’ve documented how [Equinix uses Buildkite](https://thenewstack.io/how-our-bare-metal-cloud-keeps-up-with-all-the-new-os-releases/) to update the many OSes it supports on its bare-metal cloud.

Pitt created the software when he was a developer, working with [Heroku](https://thenewstack.io/how-heroku-is-positioned-to-help-ops-engineers-in-the-genai-era/) and a [git code repository](https://thenewstack.io/need-to-know-git-start-here/).

“Heroku was a magical platform. Heroku did something that no other platform did, and then they cared about the developer experience,” Kitt said. The company he worked at mandated the use of [Jenkins](https://thenewstack.io/cloudbees-scales-jenkins-redefines-devsecops/), which was, at the time, difficult to work with, especially when accessing assets remotely.

“I needed a different approach to do my job,” he said.

Overall, software built on the software is used by more than a billion people per day, according to the company.

According to a statement from Uber Engineering Manager Shesh Patel, the ride-share giant had cut its build times in half by switching to Buildkite. “Adopting a delivery-first mindset has been crucial to our ability to grow,” he asserted.

## How Buildkite Differs From Other CI/CD Systems
Buildkite is different from other CI/CD software and service providers in two major ways, Kitt claims. One is that it is built to run concurrently, supporting the ability to run multiple jobs at the same time. Another is that it doesn’t charge by the build minutes or number of concurrent jobs, two widely-used billing methods in the CI/CD space.

Instead, Buildkite offers a [per-seat, unlimited-use pricing model](https://buildkite.com/pricing).

In many cases, organizations are tied to “legacy DevOps tools” that tie them to slowed build cycles, noted Jim Mercer, program vice president of Software Development DevOps and DevSecOps at IDC, in a statement.

To illustrate why speeding continuous integration is so important for scale-out companies, Kitt offered an example: A company like Uber may have 5,000 developers. At the start of the workday, the majority of those developers will start making code commits more or less simultaneously. With Uber’s complex codebase of 50 million lines of code or more, each change may kick off up to 50,000 separate tests. Multiply that by the 5,000 changes, and a build system may be managing hundreds of millions of events simultaneously.

“You can’t run one test after another. Otherwise, it would take weeks, months, years, even some cases, to run tests sequentially,” Kitt added. “So you have to paralyze you have to run them concurrently.”

The software, [available as open source](https://github.com/buildkite), can be easily duplicated to run as many build workflows as needed.

Developers define the steps, or a [pipeline](https://buildkite.com/docs), that a set of code should go through before being placed into production, which may involve unit and integration tests, as well as other checks. Each of the steps is handled by build runner agents, written in the Go programming language so they can be run on different platforms. Each agent polls Buildkite’s agent API over HTTPS. Outputs are [stored and reused](https://buildkite.com/docs/pipelines/artifacts) as artifacts.

Another issue in this space that impedes the ability to scale out continuous integration is how customers are billed, Kitt noted.

“A lot of the other players in this space are incentivized not to make you go faster, because their main revenue streams are from compute,” Kitt said. “They resell electricity, so they’ve got no raw incentive for you to go faster.”

As an alternative, Buildkite charges per active user, which gives the company to drive down workflow times to as close to zero as possible through concurrency.

Buildkite runs on a hybrid architecture, meaning it uses the customer’s compute capabilities, while the company runs operations on its own cloud-based control plane (Kitt calls this approach the [Bring Your Own Cloud [BYOC]](https://www.confluent.io/learn/bring-your-own-cloud/)). BuildKite itself has no access to the code itself (a true security benefit for many organizations).

## How Buildkite Has Been Expanded
For the new release, Buildkite expanded its BYOC format to package registries, offering a high-performance asset management service with rapid indexing and enhanced security features. The customer provides the storage and Buildkite provides the management.

The company has also ramped up its own cloud environment for running mobile applications on behalf of clients, based (unlike other Buildkite offerings) on per-usage pricing. It is ideal, Kitt said, for organizations that don’t want to manage the complicated logistics of mobile application delivery.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)