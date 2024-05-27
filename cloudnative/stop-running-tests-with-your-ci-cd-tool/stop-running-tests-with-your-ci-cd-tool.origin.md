# Stop Running Tests With Your CI/CD Tool
![Featued image for: Stop Running Tests With Your CI/CD Tool](https://cdn.thenewstack.io/media/2024/05/57546f25-swamp-1024x576.jpg)
Implementing a consistent testing infrastructure and workflow for cloud native applications has its challenges. Multiple stakeholders have different needs in regard to testing/QA, the testing tool stack is constantly evolving in line with new technologies and requirements,
[CI/CD](https://thenewstack.io/ci-cd/)/GitOps pipelines are transforming the way we deliver software, and the testing of both legacy and cutting-edge components needs to be maintained to ensure the delivery of high-quality applications to end users.
With the advent of CI/CD tooling and workflows, it felt natural to use
[CI/CD for running tests](https://testkube.io/learn/test-automation-in-ci-cd-shouldnt-be-hard) also. Testing is part of the software delivery life cycle after all, and automating test executions as part of builds and deployments makes sense at a conceptual level. Unfortunately, many [CI/CD tools put very little emphasis on the specific needs of testing and QA](https://testkube.io/learn/the-challenges-of-testing-in-your-ci-cd-pipeline). To them, testing is just another task to run in the pipeline, which often makes additional testing support in CI/CD tools feel more like an afterthought than a primary objective.
Add in the common scenario where multiple CI/CD tools are used within the same organization: Jenkins for building your Java microservices backend, GitHub actions for building (and deploying?) your frontend applications and maybe even something like Argo for adopting a
[GitOps approach](https://thenewstack.io/i-need-to-talk-to-you-about-kubernetes-gitops/) to deploying your applications to Kubernetes. Not only is testing often an afterthought, that afterthought is now spread across multiple tools! What could go wrong?
Let’s drill down into six specific needs of a successful test-automation strategy and how relying on CI/CD tooling will often send you into the testing swamp of no return (TSONR — this is where you read it first!).
## 1. Consistent Test-Tooling Support
No matter how you set up test runs in your CI/CD pipelines and tools, maintaining consistent support for legacy tools, modern tooling, version changes and legacy tests is a challenge.
One of the last things you want to hear at the end of the day is “our CI/CD tool doesn’t support your testing framework” or “we can’t run multiple versions of [testing tool] in our pipelines. You’ll have to upgrade all your scripts to work with version X.”
Many CI/CD tools rely on plugins to support a specific testing tool/version — not a guarantee for consistency. Their fallback is usually some kind of scripting environment, which might do the job but adds complexity and maintenance overhead, making it hard to scale and diversify testing efforts.
## 2. Consistent Test-Execution Environment
“Works on my machine.” You’ve surely heard and uttered those words with disbelief when a test you’ve meticulously crafted in one environment doesn’t give the desired results when run in a different (more important) environment.
Running the same set of tests should give consistent results, obviously. Unfortunately, running tests in a multi-CI/CD tooling environment often results in results that vary depending on where (and how) you run them. Different CI/CD tools have different runtimes, environments and infrastructure, making it hard to predict the consistency of your testing efforts, especially when it comes to nonfunctional tests like performance, security and compliance testing. Add to this that tests run locally during development are often run “manually” directly with the corresponding testing tool, which is usually far from a testing or production environment.
## 3. Run Tests Whenever Needed
Running automated tests as part of your CI/CD pipeline is common practice, but running those tests outside your pipeline is hard, and you don’t want to rerun an entire build just to rerun some updated tests against a development environment.
The possibility to run tests outside your CI/CD pipelines, both manually (for example, load-tests) or in response to other system events (such as a Kubernetes event) is a must in a distributed and diversified infrastructure to ensure that both DevOps and QA teams can (re)run tests whenever needed.
## 4. Run Tests at Scale
[Running automated tests at scale](https://testkube.io/learn/advanced-test-orchestration-in-kubernetes) entails two vectors:
- Scaling load tests to generate massive load for simulating peak usage scenarios for your applications or APIs.
- Scaling end-to-end (E2E)/functional tests to cover a matrix of execution scenarios, including different browsers, operating systems, users, etc.
CI/CD tooling will rarely have dedicated functionality that caters to either of these needs in the context of test execution. They might allow you to launch different “workers,” but all logic beyond that in regard to your testing tool at hand will have to be managed by custom scripts and/or third-party solutions.
## 5. Single Pane of Glass for Test Results
Getting access to consistent test results and artifacts across all testing tools used in your CI/CD pipelines is key to both tactical troubleshooting of failed tests and strategic understanding of overall testing efforts.
Unfortunately, most CI/CD tools have little inherent knowledge about test results at a higher level. They might make it easy to see the log/artifact output of each individual test, but aggregating quality metrics such as pass/fail ratios and execution numbers across all your testing tools is not their concern, and providing you with an easy way to access specific test-execution results and artifacts for in-depth troubleshooting of failed tests will often require you to do a fair amount of scripting yourself or export these to external tooling for deeper analysis.
## 6. Giving Control to QA
Need to update some arguments or the version of your testing tool running in your pipelines? File a ticket with the
[DevOps team and hope they have time](https://thenewstack.io/qa-why-observability-data-sampling-can-cost-devops-teams-time-and-money/) later today, or this week or month.
Once test automation is handed over to the team(s) managing CI/CD pipelines, QA often has little control or insight into that automation, which can considerably slow down the evolution of testing in your CI/CD pipelines.
CI/CD tooling rarely has the role-based access control granularity required to give testers access to just the testing aspects of build pipelines, so QA-initiated improvements/changes related to test execution often need to go through a tedious process before they get implemented, causing everything from frustration within teams to lacking test coverage.
Alternatively, QA is given access to areas of the build infrastructure they should not have, which could introduce security concerns in a more regulated organization.
## OK, Now What?
OK, you’ve heard the arguments and hopefully you’ll think twice before you ask your DevOps team to automate your Playwright scripts or Postman collections in your pipelines going forward.
But how do you address all these challenges and decouple test execution from your CI/CD pipelines without sacrificing the value of testing in CI/CD itself?
## Solution 1: A Test Orchestration Platform
Testkube is a test-orchestration platform for CI/CD specifically built to solve the above problems (and more):
- It supports the execution of tests for any testing tool/version without the need for extensive scripting.
- It uses Kubernetes to run all your tests, which brings a consistent and scalable execution environment for all your tests.
- It allows you to run your tests whenever needed — as part of CI/CD, manually from a CLI, dashboard or API, through external triggers, etc.
- It has built-in support for scaling any testing tool — either horizontally for load-generation or vertically for multi-scenario E2E/functional tests.
- It provides a
[single dashboard for all your test results and artifacts](https://testkube.io/learn/testing-control-planes-a-single-pane-of-glass-to-improve-team-productivity), ensuring you have a consistent way to troubleshoot any test and gather both operational and quality insights for your testing activities over time.
- It separates test automation orchestration/authoring/configuring from your CI/CD tooling, putting QA back in control of all test-execution activities in your environment.
Testkube always runs tests in your own infrastructure, helping you
[manage both costs and security aspects](https://thenewstack.io/kubecost-broadens-scope-beyond-kubernetes-cost-management/) of test executions. The Testkube Dashboard can either be hosted [ in the cloud](https://app.testkube.io) or [run on premises](https://www.testkube.io/download) (air-gapped, if needed), giving you both easy-to-start and security-compliant alternatives going from an evaluation to production setup.
## Option 2: Manual Scripting and Duct Taping
If Testkube isn’t for you, what are your options to circumvent some of the above challenges?
If you’re using at least one CI/CD tool in your organization, you can look into creating micro-pipelines specific to testing, and call/reuse those from your existing build pipelines. This could possibly help you with points 3, 5 and 6 above.
- These pipelines can be run whenever needed (although individual tests within them cannot).
- All test results will be found in the output of these pipelines, although if you use multiple testing tools they will still be disconnected.
- You might be able to ensure the testers/QA have access to managing them without having to touch the rest of your build configurations.
Unfortunately the level of support for the other points will vary greatly depending on the CI/CD tool you are using and how much effort/time you are willing to put into custom script authoring/maintenance.
## Summary
Automated test execution is a mandatory practice in large-scale CI/CD pipelines, but it comes with many challenges not addressed by CI/CD tooling. The shortcomings of CI/CD tools in this regard hamper a successful testing strategy that can scale across teams, projects and testing tools.
[Testkube](https://www.testkube.io/) provides a holistic solution to these challenges while maintaining compatibility with any testing tool, workflow or pipeline already deployed in your organization. An [open source version is available](https://docs.testkube.io/articles/testkube-oss/#:~:text=Welcome%20to%20the%20Open%20Source,signing%20up%20for%20Testkube%20Pro.). Give it a try at [testkube.io/get-started](http://testkube.io/get-started) to take your automated test execution to the next level. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)