# The Struggle To Test Microservices Before Merging
![Featued image for: The Struggle To Test Microservices Before Merging](https://cdn.thenewstack.io/media/2024/08/121b1852-traffic-1024x576.jpg)
It’s always a struggle to [test microservices well](https://thenewstack.io/the-struggle-for-microservice-integration-testing/). When you talk about testing, the fuzzy definition of testing phases comes up right away. Is a test involving all the services an integration test? Or an end-to-end test? Is a test of meeting API spec a contract test? Or a unit test? Specifically, the idea of an integration test can cover a number of things:

- Contract testing
- Tests using mocks
- API integration tests
But rather than splitting hairs about what is being tested, I think a better question is “what is the purpose of integration tests?” If the purpose of integration testing is to see how our updated service interacts with the rest of our stack, then we want to run this testing before merging our code with production or pre-production environments.

Proper integration testing can help catch issues early, reducing the chances of defects reaching production. However, the [approach to integration testing](https://thenewstack.io/we-need-a-new-approach-to-testing-microservices/) can vary, each with its own benefits and drawbacks.

Let’s look at the types of integration testing, focusing on pre-merge tests that provide quick feedback to developers and explore how they can be efficiently run on developer workstations and with shared environments during [pull requests](https://thenewstack.io/demo-testing-and-previewing-pull-requests-with-signadot/) (PRs).

**Integration Testing on Your Laptop: Drawbacks of Mocks**
I got my start in the tech industry doing support for an online classroom tool. During a conversation with engineering, I asked about test coverage. The team told me they had automated tests that simulated normal update actions for a virtual classroom. “How many students are in your test case?” I asked. “Oh, a whole bunch, like 50. We wanted to make sure it could handle large classes.” I then explained that the largest virtual classroom I’d seen in the real world was about 2,000 students, and our whole UX really broke at those scales. This points out how a totally contrived testing scenario, no matter how carefully engineered, can fail to simulate real-world situations.

Integration testing using mocks does not require a full environment setup or bringing up many dependencies. With startup times near zero and a testing stack you can run on your laptop, this means very fast feedback.

[Developers can create very custom test setups](https://thenewstack.io/improve-developer-velocity-by-decentralizing-testing/), seeding specific data and running precise tests. The primary benefit here is the ability to simulate specific interactions without needing a full environment.
However, maintaining mocks can be labor-intensive. Tests may focus on synthetic scenarios that might not reflect real-world conditions, making it difficult to achieve comprehensive coverage. Mocks are particularly useful for validating interactions between tightly coupled components, such as [microservices](https://thenewstack.io/microservices/) and [databases](https://thenewstack.io/data/), but they may not be suitable for all types of integration testing.

In general, tests backed with mocks are difficult for establishing “coverage”: We can feel certain we’ve covered cases that we’ve seen before with two components, but not that we’re covering every real-world scenario.

**Integration Testing Via Contract Testing**
There’s some value to performing contract tests for integration testing. When services interact via HTTP and have RESTful relationships, the sending of predicted requests or responses can help ensure that services can still talk to each other after an update. But scripting a large number of requests can be quite time-consuming, and we still get into the space of simulating multiple steps of request handling, which risks having updates that pass all tests but don’t work on production.

**Testing in a Real Environment**
End-to-end testing is really where the rubber meets the road, and we get the most reliable tests when sending in requests that actually hit all dependencies and services to form a correct response. Integration [testing at the API or frontend level using real microservice dependencies](https://thenewstack.io/why-staging-doesnt-scale-for-microservice-testing/) offers substantial value. These tests assess real behaviors and interactions, providing a realistic view of the system’s functionality. Typically, such tests are run post-merge in a staging or pre-production environment, often referred to as end-to-end (E2E) testing. This approach ensures comprehensive coverage and high accuracy, but by only running tests after branches are merged, the dev loop is made much longer, with developers waiting hours or days for test feedback.

What’s worse, in a microservice environment the odds are good that most significant failures are found at the stage of integration testing. We can’t have developers waiting days to get test feedback when it’s highly likely those tests will fail.

**Testing in a Real Environment Before Merging**
What we really want is a realistic environment that can be used by any developer, even at an early stage of working on a PR. Achieving the benefits of API and frontend-level testing pre-merge would save effort on writing and maintaining mocks while testing real system behaviors. This can be done using canary-style testing in a shared baseline environment, akin to canary rollouts but in a pre-production context. To clarify that concept: We want to try running a new version of code on a shared staging environment, where that experimental code won’t break staging for all the other development teams, the same way a canary deploy can go out, break in production and not take down the service for everyone.

Request routing can be used to run API and E2E tests on PRs in a real shared environment with all dependencies, providing early and accurate feedback. Companies like Lyft effectively use this approach to streamline their testing processes.

The implementation of a request routing solution to let “test” versions of services interact with a cluster while also not breaking or modifying flows for other developers can be super effective for your testing process, but it’s not without technical lift to implement, that’s where Signadot comes in.

**Share a Single Environment Pre-merge**
Signadot is a tool to let teams of any scale implement high-quality pre-merge testing with a shared staging cluster. Signadot enables teams to share and maintain a single environment while running tests on select services.

![A Signadot sandbox letting users experiment with a modified version of service C.](https://cdn.thenewstack.io/media/2024/08/a9376f8a-image1-1024x576.png)
A Signadot sandbox letting users experiment with a modified version of service C

By enabling integration tests to run pre-merge, it significantly reduces the time and effort required for testing. This approach eliminates the need to duplicate environments, leading to substantial cost savings. For more details, visit [Signadot](https://www.signadot.com/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)