# Who Should Run Tests? On the Future of QA
![Featued image for: Who Should Run Tests? On the Future of QA](https://cdn.thenewstack.io/media/2024/06/65338d94-testspassfail-1024x573.png)
*This is part of an ongoing series. Read previous parts:* [Why We Shift Testing Left: A Software Dev Cycle That Doesn’t Scale](https://thenewstack.io/why-we-shift-testing-left-a-software-dev-cycle-that-doesnt-scale/) [Why Shift Testing Left Part 2: QA Does More After Devs Run Tests](https://thenewstack.io/why-shift-testing-left-part-2-qa-does-more-after-devs-run-tests/) [How to Shift Testing Left: 4 Tactical Models](https://thenewstack.io/how-to-shift-testing-left-4-tactical-models/) [Shifting Testing Left: The Request Isolation Solution](https://thenewstack.io/shifting-testing-left-the-request-isolation-solution/)
QA is a funny thing. It has meant everything from “the most senior engineer who puts the final stamp on all code” to “the guy who just sort of clicks around randomly and sees if anything breaks.” I’ve seen seen QA operating in all different levels of the organization, from
[engineers tightly integrated with each team](https://thenewstack.io/top-challenges-to-creating-high-performing-engineering-teams/) to an independent, almost outside organization.
A basic question as we look at shifting testing left, as we put more testing responsibility with the product teams, is what the role of QA should be in this new arrangement. This can be generalized as “who should own tests?” Microsoft retired its “dedicated software engineer in test” (SDET) position in 2014, while Apple and Amazon retain a high focus on dedicated QA. If the FAANG companies can’t decide whether we need dedicated QA roles, how can the rest of us answer the question?
Let’s explore how QA’s role grows in a world where testing is shifting left.
## QA Has Long Been a Victim of Trends, but QA Continues
In my first technical role at New Relic, I was meeting all the engineering teams who wrote APM (application performance management) agents for the major web development languages. Each team had a similar makeup, but I asked, “Who’s the QA person on the Ruby team?”
“There isn’t one,” The head of the Ruby team replied. “Rails doesn’t require QA.”
That team’s hubris can be forgiven: There’s never a new hot language on the scene without someone insisting that it solves every known software problem, and makes bugs, failures and unexpected behavior impossible. However this conversation led me to a more general principle: Some would always see QA as an embarrassing thing to need, meaning some teams would proudly proclaim that they no longer needed people dedicated to testing.
In the decade since this conversation, it’s become clear that no language or framework is free from the need for testing. That work can be highly distributed, with every single engineer doing their best to write tests, run them and interpret the results. Alternately, the work can be centralized, with a selected few running a compendious set of tests on every release.
## There Was Never a Time When Developers Didn’t Run Tests
“Back in the day, QA was responsible for running all the tests and developers just wrote code.” This was never true. Since the era of groundbreaking figures like
[Grace Hopper](https://thenewstack.io/lets-say-happy-birthday-amazing-grace/), developers have always been able to run the code they were writing, and no one has handed off truly untested code to QA. We all have added debug statements, checked console log outputs and clicked around an interface running on localhost. If we’re shifting testing left now, that doesn’t mean that developers will be running tests for the first time.
Rather, shifting left means giving developers access to a complete set of highly accurate tests, and instead of just guessing from their understanding of API contracts and a few unit tests that their code is working, we want developers to be truly confident that they are handing off working code before deploying it to production.
## QA Shouldn’t Be Testing Code That Devs Haven’t Tested
It’s a simple, self-evident principle that when QA finds a problem, that should be a surprise to the developers. If devs are sending off code for testing and they have no idea whether it works, there will be a number of simple, easily detected bugs that could have been solved in a day that now will pend an extra week waiting on the outer loop feedback cycle.
All this may sound self-evident, but when it comes to integration testing — seeing how your code really works in relation to the other services and dependencies in your stack — many organizations still rely on a separate team to run tests at this level. Without access to full and accurate integration tests, when a developer submits a pull request, they are creating a situation where many surprises lurk ahead.
## It’s No Longer Separate: Embedded QA Within Teams
Rather than a separate QA team that oversees code just before release to production, an approach that may work well in a microservice environment is embedding QA professionals and/or SDETs within teams.
QA professionals who are embedded within teams should not merely execute tests; their responsibilities extend to writing comprehensive test suites and identifying regressions across the service. This proactive approach ensures that quality is maintained throughout the codebase. An engineer shouldn’t be the one to test code they are too close to; it’s more effective when a dedicated QA evaluates it objectively.
One key value QA brings is assessing the testability of a codebase. By focusing on encapsulating business logic, QA professionals facilitate easier testing and contribute to a more robust architecture. For example, this approach allows for swapping out database services as needed for financial optimization, beyond just improving testability.
In a microservices-based environment where teams own individual microservices, QA professionals play a critical role in overseeing the interactions between these services. Individual teams often concentrate on their specific microservices, potentially overlooking the broader system interactions where issues frequently arise. By acting as a separate entity, QA can holistically evaluate the architecture, ensuring comprehensive test coverage and assisting teams in bootstrapping their testing efforts.
## What QA Does Now
The change, then — as QA embeds itself within
[teams and more developers](https://thenewstack.io/managing-software-development-team-dynamics-from-within/) know how to run high-quality tests — is that QA ends up doing more, not less. The work that QA does becomes more strategic, and has a greater effect on overall developer velocity. Things like:
- Coming up with the testing strategy
- Building testing frameworks
- Choosing the right testing tools
- Focusing on more complex end-to-end automation
- Shifting left and embedding themselves within product teams to enable earlier testing
As the need for development velocity and reliable deployments grows, QA will become more valuable than ever.
## Join the Signadot Slack
At Signadot, we’re trying to make testing easier for every part of your software development life cycle. If you’re interested in hearing more,
[join us on Slack](https://signadotcommunity.slack.com/join/shared_invite/zt-1estxm8pv-qfiaNfiFFCaW~eUlXsVoEQ#/shared-invite/email) to meet our community. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)