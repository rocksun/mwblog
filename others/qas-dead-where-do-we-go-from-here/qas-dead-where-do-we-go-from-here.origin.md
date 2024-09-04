[Check Point® Software Technologies Ltd.](https://www.checkpoint.com/) unveiled its innovative Portal designed for both managed security service providers (MSSPs) and distributors.
If you listen to thought leaders, QA is in its death throes. It's useless, it's expensive, and besides, we have machines to do that now. In my own experience, I've been working in organizations without dedicated QA teams for several years, and I think the rest of the world has finally caught up.

If we take a [Betteridge's law of headlines](https://en.wikipedia.org/wiki/Betteridge%27s_law_of_headlines) approach to the question, "Is QA dying?" the inevitable answer is no. QA isn't dying; it's already dead. This death has already had enormous ramifications for QA teams. However, a transformation has happened, ultimately increasing the importance of quality in the software development lifecycle.

The transformation I'm talking about is where quality assurance has moved from a separate, final stage of development to one at the core of software creation, where every developer is expected to tear down their own code to build a better product. And if you're not on board with this shift yet, I have bad news for you.

#### Why QA Changed
Traditional QA went like this:

■ Design: PMs, architects, and developers define the product requirements and design the initial architecture.

■ Development: Developers write the code based on the requirements and designs.

■ Testing: The QA team receives the completed code, creates test plans and cases, and executes manual/automated tests to cover various scenarios. They report bugs back to the development team.

■ Bug fixing: Developers receive bug reports, fix the issues, and pass the code back to QA.

■ Retesting: QA verifies the fixes and may perform another round of regression testing.

■ Release: Once QA approves, the software moves to production.

This compartmentalized model was the standard in software development for decades but became synonymous with a "throw it over the wall" mentality. Coders coded, testers tested. But when laid out like this, it quickly becomes clear what the problems are:

First, everyone is siloed. Development and testing teams work in isolation, leading to communication gaps and misaligned expectations. This compartmentalization can result in a great product but with significant overhead.

Secondly, the development process occurs before any substantial testing begins. This late-stage bug discovery could be more efficient. Bugs found earlier in the development cycle are typically more straightforward and cheaper to fix. Still, this model pushes bug detection to the end, increasing the overall cost and time of development.

Third, the cycle between testing and bug fixing creates significant bottlenecks. As bugs are found, they're returned to developers, fixed, and then returned to QA for retesting. This back-and-forth is time-consuming and can delay releases, especially if significant issues are discovered late in the process.

With this framework, you get slower development cycles, increased costs, and potential quality issues. All this stems from a single problem: a need for more ownership over quality throughout the process.

#### The Shift of Ownership for Quality
In the past, QA teams were the arbiters of quality in an organization. That responsibility has now shifted left to the developer. This shift isn't just a minor adjustment; it's a fundamental reworking of the approach to software quality.

Our linear process above has been moved to a circular process of building, testing, rebuilding, and pushing to production:

All of this happens within the development box above. Developers are now the first line of quality control.

This is possible through two initiatives.

First, iterative development. Agile methodologies mean teams now work in short sprints, delivering functional software more frequently. This allows for continuous testing and feedback, catching issues earlier in the process. It also means that quality is no longer a final checkpoint but an ongoing consideration throughout the development cycle.

Second, tooling. Automated testing frameworks, CI/CD pipelines, and code quality tools have allowed developers to take on more quality control responsibilities without risking burnout. These tools allow for instant feedback on code quality, automated testing on every commit, and integration of quality checks into the development workflow.

What does this look like in practice?

Let's take full-stack API development as an example. Individual developers can now leverage tools that automate much of the boilerplate work and provide instant feedback. For instance, the tools are empowering developers to do the following:

■ API Design: Developers can now create standardized OpenAPI specs quickly. This allows them to start coding almost immediately without spending an entire sprint building the initial design.

■ API Mocking: With the right tools, developers can create dynamic, sharable mocks. This eliminates the need to manually write and maintain mock code, allowing for quick validation and iteration.

■ Code Generation: AI-powered code generation tools can now handle much of the boilerplate code for client- and server-side APIs. This frees up developers to focus on the unique aspects of their API implementation.

■ Testing and Debugging: Modern platforms provide publicly available URLs for testing, allowing developers to run their code in production-like environments. These integrate directly with IDEs, enabling developers to set breakpoints and debug efficiently, minimizing the likelihood of errors making it to production.

■ Deployment: Tools now exist that provide hosted, containerized test environments. This allows for easy progressive and repeated testing without the need for constant reconfiguration.

These are just a few of the advancements that mean developers can now handle many aspects of API development and testing that were previously siloed or required extensive back-and-forth with other teams.

This shift doesn't eliminate the need for specialized QA knowledge. Instead, it integrates quality considerations throughout the development process, with developers taking on more responsibility for ensuring the quality of their APIs from the outset.

#### What Becomes of QAs?
Where does this leave QAs?

Without a home? Kind of, but not really! It is more accurate to say they now have multiple homes. QAs can either become more strategic or more technical, moving up or down the stack.

The first opportunity is down the stack, moving into more technical roles. QA professionals can leverage their quality-focused mindset to become automation specialists or DevOps engineers. Their expertise in thorough testing can be crucial in developing robust, reliable automated test suites. The concept that "flaky tests are worse than no tests" becomes even more critical when the tests are all that stop an organization from shipping low-quality code.

QAs excel at identifying edge cases and potential failure points, making them invaluable in creating comprehensive test coverage that goes beyond basic happy path scenarios. This rigor can balance out any [YOLO-driven development](https://andersoncardoso.github.io/ydd/) in rapid development environments.

The second opportunity is to move up the stack into a strategic role. Testing is now a vital part of the development lifecycle, and it requires thought. QA professionals can evolve into quality strategists, focusing on designing comprehensive testing strategies that cover the entire software lifecycle.

#### QA Is Now in the Hands of the Individual and Their Tools
QA teams have gone, but the mindset of quality engineering will always be needed. That mindset has now shifted from a specific team to being imbued in every developer working on a product. Organizations must now find ways to utilize that mindset daily by giving them the tools and support necessary to produce high-quality software.

The "death" of QA ultimately wasn't about its demise but its integration into every aspect of software development. The challenge for organizations will be fostering a culture where quality is everyone's responsibility while still valuing and leveraging the specialized skills that QA professionals bring. Lean into the tools that can provide that QA check, and empower your own developers to each wear their own QA hat.

## Industry News
[Check Point Software Unveils New MSSP Portal for Partners: Vastly Simplifying Service Delivery and Ease of Doing Business](/check-point-software-unveils-new-mssp-portal-for-partners-vastly-simplifying-service-delivery-and)
Couchbase officially launched Capella™ Columnar on AWS, which helps organizations streamline the development of adaptive applications by enabling real-time data analysis alongside operational workloads within a single database platform.

Mend.io unveiled the Mend AppSec Platform, a solution designed to help businesses transform application security programs into proactive programs that reduce application risk.

Elastic announced that it is adding the GNU Affero General Public License v3 (AGPL) as an option for users to license the free part of the Elasticsearch and Kibana source code that is available under Server Side Public License 1.0 (SSPL 1.0) and Elastic License 2.0 (ELv2).

[Progress](https://www.progress.com/) announced the latest release of [Progress® Semaphore™](https://www.progress.com/semaphore), its metadata management and semantic AI platform.
Elastic, the Search AI Company, announced the Elasticsearch Open Inference API now integrates with Anthropic, providing developers with seamless access to Anthropic’s Claude, including Claude 3.5 Sonnet, Claude 3 Haiku and Claude 3 Opus, directly from their Anthropic account.

Broadcom unveiled VMware Cloud Foundation (VCF) 9, the future of VCF that will accelerate customers’ transition from siloed IT architectures to a unified and integrated private cloud platform that lowers cost and risk.

Broadcom announced VMware Tanzu Platform 10, a cloud native application platform that accelerates software delivery, providing platform engineering teams enhanced governance and operational efficiency while reducing toil and complexity for development teams.

Red Hat announced the general availability of Red Hat OpenStack Services on OpenShift, the next major release of Red Hat OpenStack Platform.

Salesforce announced new innovations in Slack that make it easier for users to build automations, no matter their technical expertise.

GitLab announced the general availability of the GitLab Duo Enterprise add-on.

Tigera now delivers universal microsegmentation capabilities with Calico.

Tabnine announced a new platform partnership with Broadcom Inc., an integration with IBM, as well as continuing extensions of existing partnerships with Amazon Web Services (AWS), DigitalOcean, Google Cloud, and Oracle Cloud Infrastructure (OCI).

Wallarm released API Attack Surface Management (AASM), an agentless technology to help organizations identify, analyze, and secure their entire API attack surface.

LambdaTest launched KaneAI, an end-to-end software AI Test Agent.