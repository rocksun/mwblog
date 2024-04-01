# Will the Real Test Observability Please Stand up?
![Featued image for: Will the Real Test Observability Please Stand up?](https://cdn.thenewstack.io/media/2024/03/86c39852-penguin-1024x576.jpg)
The term “test observability” has started to appear in technical discussions and product marketing. However, its definition varies widely and is sometimes used in questionable ways. You could argue that it is good marketing but bad tech. Let’s discuss the marketing spin and the actual technical meaning of the words. By the end, we hope to clarify the true meaning of test observability.
First, it might be helpful to define what
[observability](https://thenewstack.io/observability/) is. This is a well-known concept in the software world, and it hasn’t changed significantly in the past few years. So let’s have Claude AI provide us with an unbiased definition:
The word “test” is well understood, so “test observability”
[must be the application of observability techniques to tests](https://thenewstack.io/security-testing-must-be-part-of-software-development-life-cycle/) and testing.
**One Possible Candidate**
BrowserStack has a product called “
[Test Observability](https://www.browserstack.com/test-observability).” It’s explained as: *“*Real-time test reporting. Flaky detection. AI-driven test failure debugging. Automation health metrics tracking *.”*
The expanded explanation is:
*“*Basic test reporting tools drown you in noise. Test Observability auto-identifies genuine test failures, employs AI to find the failure reason and enables proactive monitoring of suite health.”
To summarize, BrowserStack provides advanced tools to analyze failure rates among test runs. These tools can differentiate between inconsequential noise and significant failures that warrant further examination. Great!
But is this really “test observability”? At its core, observability is about uncovering the unknown unknowns. It involves instrumenting a system so that when things go wrong, you can investigate and identify the root cause. This approach doesn’t begin with an assumption of what will go wrong. Instead, it acknowledges that unexpected events will happen, and you need to be able to examine the system to understand what happened and why.
A test management system doesn’t classify a failing test run as an “internal state.” A test is executed and it either passes or fails. We understand that tests will fail and that there will be flaky tests. We also recognize the need for failure rate reports. The service provided by BrowserStack could be more accurately termed “advanced test run reporting.” If we let the marketing department add some flair and incorporate a trendy buzzword, it might be relabeled as “test run reporting with AI.” But observability?
**A Different Take on Test Observability**
What is the primary source of unknowns when running tests against your system? Your system! It is complex, it has interactions across many services and has components written by many teams, perhaps written in different languages. Most tests run today are black-box tests, returning just the response, perhaps a status code and test duration. Test tools can try to provide access to other artifacts, such as recordings from Cypress or Playwright tests, to enhance your ability to understand what the root cause of the failure is, but it is still difficult, and that black box is, well, hard to see inside.
Over the past decade, especially in the last five years, companies have embraced observability techniques to tackle troubleshooting complexities in production environments. These techniques can also be adopted in tests and testing environments.
[Denis Peganov](https://medium.com/@dees3g), a QA automation engineer, wrote an excellent blog post titled [ “Elevating Test Quality through Observability](https://blog.stackademic.com/elevating-test-quality-through-observability-48926ca90c15).” He discusses how relying solely on logs for debugging is limiting, and that using both metrics and tracing can provide key benefits such as:
- Faster debugging
- Root-cause analysis
- Proactive issue identification
- Improved test coverage
- Team collaboration
**Implementing Test Observability**
Test products are starting to use observability signals to improve current tests. They employ standards-based observability techniques to do what observability excels at — seeing inside the black box.
Grafana has introduced a feature allowing
[the capture of distributed traces from k6 performance tests](https://grafana.com/blog/2023/09/19/troubleshoot-failed-performance-tests-faster-with-distributed-tracing-in-grafana-cloud-k6/). Customers using k6 can now capture a distributed trace for each test run in a performance test and store the result in Grafana Tempo. The following quote effectively outlines the issues this feature addresses: *“*Understanding performance test results and acting on them, however, has always been a challenge. This is due to the visibility gap between the black-box data from performance testing and the internal white-box data of the system being tested.” [Artillery.io](http://artillery.io) also sees the value in leveraging metrics and traces when running performance tests, and [recently announced OpenTelemetry support](https://www.artillery.io/blog/introducing-opentelemetry-support). [Tracetest](https://tracetest.io/) is addressing this issue in a broader context. It works with any OpenTelemetry-enabled backend, including Grafana Tempo, AWS X-Ray, Honeycomb and Dynatrace. It [integrates with your existing testing](https://thenewstack.io/the-struggle-for-microservice-integration-testing/) frameworks:
- End-to-end (E2E) frontend frameworks like Cypress or Playwright
- Performance-testing tools such as k6 or Artillery
- API tests, by importing Postman or cURL-based tests
Tracetest increases your ability to quickly triage failed
[tests from any of these frameworks](https://thenewstack.io/testkube-cloud-native-testing-framework-for-kubernetes/). It helps identify the team to which bugs should be assigned and provides visibility and detailed information about any failures. This enables software engineers to resolve issues quickly.
By adding Tracetest into your testing environment, your existing tests can now use your current observability. For instance, Playwright test results display not only frontend artifacts such as screen recordings or API call results but also the full distributed trace captured from the backend system.
The use of observability exposes any “unknown unknowns.” With the ability to
[test and debug critical end-to-end flows with Playwright](https://tracetest.io/blog/the-lord-of-playwright-the-two-traces) and OpenTelemetry, you can get a holistic view of the entire process. This provides QA with the ability to determine the root cause of issues easily and assign them to the correct team.
Tracetest allows you to create assertions based on the data in the distributed trace using a technique called “
[trace-based testing](https://thenewstack.io/trace-based-testing-for-a-distributed-world/).” Unlike typical black-box testing, which only verifies response data from a call, trace-based testing allows for assertions against any system activity. This form of white-box testing enables true end-to-end testing.
**Will the Real Test Observability Please Stand Up!**
Clearly, applying
[observability signals like distributed traces](https://thenewstack.io/observability-distributed-tracing-and-kubernetes-management/) to your tests can help answer complex questions and explore the unknown unknowns. It goes beyond just “advanced reporting” — it uses observability in a new, but logical way. It enables quicker mean [time to resolution (MTTR) ](https://thenewstack.io/how-we-slashed-detection-and-resolution-time-in-half/) in your test environments by leveraging existing observability. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)