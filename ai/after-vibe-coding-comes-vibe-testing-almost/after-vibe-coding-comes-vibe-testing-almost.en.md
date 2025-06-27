[DevOps](https://thenewstack.io/devops/) platform provider [Harness](https://www.harness.io/) today made its [Harness AI Test Automation](https://www.harness.io/products/ai-test-automation) tool generally available as what the company calls the industry’s first AI-native, end-to-end test automation solution.

Harness AI Test Automation introduces “intent-based testing” — a revolutionary approach where users describe what they want tested in [natural language](https://thenewstack.io/can-english-dethrone-python-as-top-programming-language/) rather than writing test scripts. The [AI agent](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) then figures out how to execute and validate the tests, even when UIs change, [Sushil Kumar](https://www.linkedin.com/in/sushil-kumar-343780/), head of business for Harness AI Test Automation, told The New Stack.

Kumar said that while AI tools like [GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) and [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) have dramatically accelerated code generation, testing remains stuck in 2012-era practices. This creates a bottleneck where code can be generated in hours, but it takes weeks or months to reach production due to slow, manual testing processes — especially end-to-end testing, he said.

Harness AI Test Automation is designed to meet the speed, scale and resilience demanded by modern DevOps. The tool enables enterprises to replace outdated test frameworks with a seamless, AI-powered solution that delivers smarter, faster testing across the [software development life cycle (SDLC)](https://thenewstack.io/how-ai-is-reshaping-the-software-development-life-cycle/). With this offering, Kumar said Harness can provide a fully automated software delivery platform where users can code, build, test and deploy applications using the Harness platform. It eliminates manual gaps and toolchain silos and completes the Harness end-to-end DevOps platform used by major brands like Citi, United Airlines, Choice Hotels and The Home Depot.

## Code Fast, Test Slow? Not Anymore

“Productivity has gone up through the roof,” Kumar said. “Unfortunately, the code that you create doesn’t reach the customer as fast, because now testing has become the bottleneck.”

The Harness tool enables software development teams to deliver quality software faster.

“Traditional testing methods struggled to keep up — it is too manual, fragile, and slow. So, we’ve reimagined testing with AI,” Kumar said in a statement. “Intent-based testing brings greater intelligence and adaptability to automation, and it seamlessly integrates into your delivery pipeline.”

Moreover, Kumar noted that [Google](https://cloud.google.com/?utm_content=inline+mention)‘s [2024 DORA report](https://dora.dev/research/2024/dora-report/) found software delivery actually slowed down despite AI productivity gains because testing cannot keep up, and that around 70-80% of organizations are still reliant on manual testing methods, thus slowing down delivery and introducing risks.

However, with internal use of the tool within the company, Harness has seen significant productivity improvements, as have early (beta) users of the product.

For instance, one Harness project manager with zero quality assurance (QA) background built 55 automated tests in 2.5 weeks — a feat that normally takes a dedicated QA team months. The company also achieved up to 10 times faster test creation internally.

“With AI Test Automation, I just literally wrote out and wireframed all the test cases, and in a matter of 15 to 20 minutes, I was able to knock out one test,” said [Rohan Gupta](https://www.linkedin.com/in/swarnendurohan-gupta/), principal product manager at Harness, in a statement. “Using the templating functionality, we were able to come up from a suite of zero to 55 tests in the span of two and a half weeks.”

Meanwhile, using Harness AI Test Automation, Harness customer [Siemens Healthineers](https://www.siemens-healthineers.com/) slashed its QA bottlenecks and transformed test creation from days to minutes.

“We could just see in the browser exactly where it went wrong and directly edit that step. That was really fast and quick,” [Amrita Majumder](https://www.linkedin.com/in/amritamajumder/?originalSubdomain=in), lead QA engineer at Siemens Healthineers, said in a statement.

“They have reduced the test creation time by 90% because they don’t have to write scripts anymore. They simply write the prompts,” Kumar said.

## First Came ‘Vibe Coding’ — Now Comes ‘Vibe Testing?’

Instead of writing brittle scripts, users write natural language prompts like “add sneakers under $100 to cart, checkout as new user,” and AI handles execution, data generation and outcome verification, Kumar said. And when UI changes break traditional scripts, this AI adapts automatically.

“You don’t write scripts anymore,” Kumar told The New Stack. “You simply tell our [agentic AI](https://thenewstack.io/agentic-ai-the-missing-piece-in-platform-engineering/) platform what the workflow is, and you will describe it exactly like you want it. An e-commerce site user could write ‘Go to the storefront, pick items based on ratings, add to cart, validate totals and checkout,’ and the system will figure out what to do, even if the UI changes.”

This sounds like vibe testing to me.

“We were actually thinking, like, ‘Hey, should we call it vibe testing?’ We can accept that, but I think there is a difference,” Kumar said.

Validation is key to testing, so a vibe-style approach is less effective, Kumar said.

Indeed, there is a parallel to “[vibe coding](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/)” where developers express high-level intentions rather than detailed instructions. Kumar acknowledged the conceptual similarity but explained why they chose “intent-based testing” instead, emphasizing the need for rigorous validation that goes beyond just “vibes.”

“In intent-based testing, we actually take more granular steps. At each step of the way, we validate if the application responded,” he said. “It’s a similar idea, but if you’re doing vibe coding with natural language prompts, you need a technique like what we are calling intent-based testing to complete the end-to-end flow.”

## AI Testing AI

A key element of the tool involves using AI to test AI-generated code. Harness uses the platform internally to test its DevOps assistant, which generates YAML pipeline code based on natural language requests.

“We are using AI to test AI,” Kumar noted. “The conventional approach of writing deterministic outcomes doesn’t work because AI responses depend on the context.”

The system automatically invokes the DevOps assistant, analyzes the generated YAML code, and validates whether it performs the requested functions — all without human intervention.

## Major Features

### **No-Code Test Creation**

* Live test authoring by recording interactions
* Natural language test cases (“Did the login succeed?”)
* AI auto-generates assertions after each step
* Visual testing with human-like AI validation

### **Self-Healing Maintenance**

* AI-generated selectors adapt to UI changes
* Up to 70% reduction in test maintenance
* Smart selector technology works across environments

### **Intelligent Execution**

* AI distinguishes between transient issues and real bugs
* Parallel execution scaling to thousands of tests
* Data-driven testing with dynamic parameterization

## How It Started

Kumar said work on Harness AI Test Automation began three years ago at [Relicx](https://relicx.ai/), the company he founded that [Harness acquired last year](https://relicx.ai/blogs/exciting-news-announcing-the-next-phase-of-our-journey). The tool represents three years of R&D in agentic AI development.

“…We’re excited to see how the combined strengths of Harness and Relicx will continue to disrupt the test automation space, especially with rapid advances in Generative AI,” Kumar wrote in a blog post announcing the acquisition last August. “We believe this next step will bring significant value to your development processes, and we’re eager to continue supporting you on this journey.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)