# A 5-Step Framework for Test Execution
![Featued image for: A 5-Step Framework for Test Execution](https://cdn.thenewstack.io/media/2024/07/d5969971-steps1a-1024x576.jpg)
In our [previous article](https://thenewstack.io/stop-running-tests-with-your-ci-cd-tool/), we made the point that coupling test execution to CI/CD pipelines has several drawbacks that become apparent as the complexity and scale of your application or deployment infrastructure increases. Let’s take a step back now and look at the initial need solved by [CI/CD](https://thenewstack.io/ci-cd/) in this context: running your tests, which is also known as test execution. As with many things, giving test execution some extra thought and love as you build out your infrastructure can reward you in multiples. Let’s break it down.

## Test Execution in the STLC
The software testing life cycle (STLC) is a well-established step-by-step breakdown of testing activities in the software development life cycle (SDLC). At a high level, the STLC consists of the following steps:

**Requirements analysis**: Understand what needs to be tested.**Test planning**: Plan how the requirements will be tested.**Test case development**: Write actual test cases.**Test environment setup**: Prepare your test environments.**Test execution**: Execute your tests in your test environment.**Test cycle closure**: Ensure that all testing activities are completed.
As you can see, test execution is a specific step in this life cycle, and it in itself is a rabbit hole to delve into. Let’s do just that.

## A 5-Step Framework for Test Execution
Executing tests and consequently managing execution results in a scalable and efficient manner turns out to be a complex undertaking as the number of testing tools, CI/CD systems, engineers and applications grows in your organization. Let’s start by breaking down test execution into five steps to help decide how to execute tests in a way that can grow correspondingly.

**Define**: How will you define the execution of your tests?**Trigger**: How will you trigger your test executions?**Scale**: What scalability needs or constraints do you have for test execution?**Troubleshoot**: How can you effectively troubleshoot your (failed) test executions?**Report**: What reporting do you need to plan your (future) testing activities?
Let’s dig into each of these steps in a little more detail to help you understand what questions you might need to answer within your team.

**Define**– How are you going to run your[tests in a consistent way](https://thenewstack.io/cloud-native/why-you-should-start-testing-in-the-cloud-native-way/), considering:- Your existing (and future?) testing tools and versions
- Input data for data-driven testing
- Test orchestration: for instance, execution of multiple tests in a coordinated way, possibly across multiple/remote environments
**Trigger**– How will you trigger the execution of your tests?- From CI/CD tooling as part of your build and deploy processes?
- Scheduled execution at regular intervals? (For example, “Run our security tests on a daily basis.”)
- Based on external/internal asynchronous event triggers or webhooks? (“Re-run end-to-end tests whenever these components are updated in our infrastructure.”)
*Ad hoc*or manually?- Custom integrations via APIs/CLIs?
**Scale**– As you ramp up your testing activities, make sure you’ve assessed:- How many tests do you anticipate to be running at “peak testing time”?
- Do you have shared/stateful infrastructure that is shared across tests? Do you need to constrain test execution accordingly?
- Do you have very-long-running tests that either need to be:
- Parallelized to cut down on execution time?
- Scheduled asynchronously instead of run for every build?
- Should tests be running inside and/or outside your infrastructure (or both)?
- For load-testing specifically:
- How much load do you need to simulate?
- Can you use your existing/internal infrastructure?
- How can you coordinate with other (testing) activities?
**Troubleshoot**– Troubleshooting failed tests can be a pain in a complex application infrastructure:- Are the logs and artifacts from your testing tools sufficient, or do you also need logs and metrics from the application that is under test?
- Do the right people have access to logs/infrastructure to troubleshoot?
- Can all troubleshooting be done in one place or are there multiple points of access?
- For how long do you need to keep results around?
- Do logs or artifacts contain sensitive information? Do they need to be stored securely?
**Report**– Ask yourself:- What metrics do you need to track over time, and at what granularity? For example pass/fail ratios, total number of tests, etc.
- Could or should you aggregate results from different test executions and testing tools into common reports?
- Access control: Do the right people have access to reports?
- Can reports/metrics be analyzed by required dimensions, such as team/application, etc.?
- Do test execution results need to be pushed to external systems? For example: reporting, incident management, issue tracking
- How should reports be distributed internally and be accessed over time — ephemeral/long-lived URLs? PDFs? etc.
## Test Execution Assessment Criteria
Apart from the somewhat tactical approach to test execution outlined above, we can define a number of criteria that need to be assessed and planned for to scale accordingly with the needs of your team and your application.

**Consistency**– Getting consistent test results is key to building trust in quality metrics and downstream activities, and to that end, your test execution environments should be as homogenous as possible, given the context of your applications.**Decoupling**– Test execution should not be tightly coupled to any other specific framework or pipeline in your infrastructure. The need to run tests will shift both strategically and tactically over time, and your tests should be available for execution whenever needed.– While your tests might execute in multiple places in your infrastructure, managing these executions and their results in one place gives you a holistic view of your testing activities, making it possible to assess, analyze and control test execution consistently as your testing scales with your applications and infrastructure.**Centralization****Integration**– Test execution commonly needs to be integrated — but not tightly coupled! — with your existing workflows and pipelines.- The execution of tests needs to be triggerable from a variety of sources.
- Notifications of test executions or failures needs to be integrated into collaboration platforms and incident/issue tracking.
- Test results or metrics might need to be captured by external monitoring or reporting tools.
**Scalability**– Running tests at scale is one of the most common challenges for teams embracing a proactive approach to test execution.- The need to scale individual tests horizontally to improve execution times or cover more test scenarios
- The need for multiple teams to run their tests using a constrained resource (infrastructure, shared database, etc.)
- The need to scale load tests to generate the required load to ensure the performance and stability of your applications and infrastructure
**Security and Access Control**– This has several aspects:- Who should be able to run tests, see results, etc.?
- If your infrastructure needs to be configured specifically for test execution, does that have any security implications?
## Charting the Course for Test Execution
Neither of the above sections is meant to be exhaustive or conclusive in their respective approach. Each application infrastructure is unique, and so will your team’s needs be on how to run tests. The main point is to make you think about test execution further than “run my playwright test in Jenkins” — as that will surely hit a dead end and stop you from scaling your testing activities in line with the evolution of your applications.

A hands-on approach could be:

- Break down your testing activities into the different steps of the STLC. How are you performing each of these steps? Who is responsible? What needs do you have?
- Break down test execution into the five steps above and ask yourself again: What are your needs, who is responsible, etc..
- Factor in the test execution assessment criteria outlined above into your test execution strategy. Make sure you have at least discussed them all, even if your course of action is “ignore.”
- Make sure the right people are involved in all of these discussions (in no specific order):
- QA leads/managers
- DevOps/platform engineering
- System architecture (if needed/applicable)
- Product ownership (if needed/applicable)
## Testkube for Test Execution
Perhaps not surprisingly, I’m writing this article not only to share insights into test execution, but also to show you how [Testkube](https://www.testkube.io) can help.

Put simply, Testkube is an [orchestration platform for test execution](https://testkube.io/use-cases) in line with many (but not all) points discussed above. The five steps outlined for test execution above are cornerstones for [how to work with Testkube](https://thenewstack.io/testkube-a-new-approach-to-cloud-native-testing/):

**Define**your test execution using a powerful[Test Workflow syntax](https://testkube.io/learn/getting-started-with-test-workflows-for-kubernetes-testing)that supports any testing tool or script you might be using.**Trigger**your tests however you might need to; CI/CD, events/webhooks, CLI, API, etc..**Scale**any testing tool horizontally or vertically to ensure your applications are tested consistently and[at scale](https://testkube.io/learn/advanced-test-orchestration-in-kubernetes).**Troubleshoot**test results using Testkube results and log analysis functionality.**Report**on test results over time to guide you in your testing efforts and activities.
And although Testkube can’t solve for every issue discussed above, it provides a grounded starting point. Try it out at [testkube.io/get-started](https://testkube.io/get-started). There are both open source and free versions available.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)