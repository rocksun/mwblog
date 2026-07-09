The software code review process is a systematic, peer-driven quality assurance procedure that scrutinizes code when a developer submits a pull or merge request.

Although poor code review procedures are bemoaned for their inevitable delays and the potential for people to create bottlenecks over inconsequential niggles, good code review catches bugs early, fosters mentoring relationships, and is seen as a democratic way of sharing responsibility.

That’s all there is to it, except that it’s not.

Senior software engineer [Mark Dominus](https://www.linkedin.com/in/mark-jason-dominus-93545b/) tells *The New Stack* that although many companies do obviously perform code reviews, they don’t “articulate what the result of the review is supposed to be”, and that’s a problem.

“Say you’re a junior engineer, and you’re told for the first time to do a code review. What’s your deliverable? In many places I’ve worked, the deliverable has been left unspecified,” Dominus says.

In a [Mastodon post](https://mathstodon.xyz/@mjd/115096720350507897) on this subject, Dominus wrote that “anyone who depends on code review to find bugs is living in a fool’s paradise”, primarily because it is “not in general possible” to find bugs by examining code. He underlined his comment, saying that the “primary purpose of code review” is to find code that will be hard to maintain in the future.

## A sure path to code review bad results

He suggests that in scenarios where a software engineer is expected to take a leisurely walking tour through the [change set](https://en.wikipedia.org/wiki/Changeset) and call out things they don’t like, that leads to bad results, i.e., it encourages people to try and enforce their own preferences about how things should be done, and arguments generally ensue.

> “Finding bugs, just from examining a change set, is extremely difficult and requires a certain amount of luck.” – Mark Dominus.

“Sometimes the boss gives the junior engineer a little more to go on, such as: ‘see if you can find any bugs,’ and this puts the junior in an unpleasant position,” clarifies Dominus. “Maybe they do find a bug, great! But what if they don’t? [Finding bugs](https://thenewstack.io/what-can-we-learn-from-historys-most-bizarre-software-bugs/), just from examining a change set, is extremely difficult and requires a certain amount of luck.”

He suggests a different approach in which software team project leaders drive the code review process by saying: “Look at this for two hours, write a note about anything you don’t understand, and if you don’t get all the way through, make a note about where you stopped.”

## A route to delivering real software engineering value

“Now, if the reviewer doesn’t have time to look at everything, you have learned something valuable: the changes are too big or complex to be understood in two hours. Perhaps the change set should be broken into two or more smaller submissions that should be reviewed separately. No matter how junior, inexperienced, or hungover the reviewer is, they can deliver what was asked, and what they deliver will have real engineering value,” explains Dominus.

That real engineering value is a positive negative in this case. The team has now identified code that another team member can’t understand, or that the change set is too unwieldy for the current code review process… or both.

## Code review is theatre, playing soon, near you

Agreeing broadly with these sentiments, [Mikhail Golikov](https://www.linkedin.com/in/michael-golikov-b19308263/), a QA engineer at a high-load e-commerce platform company, tells *The New Stack* that “code review is theatre” if a team is leaning on it to catch bugs.

> “When a team treats review as its bug filter, it ships with a warm feeling and no evidence, then finds out in production,” – Mikhail Golikov.

“A human [skimming a diff](https://www.codecademy.com/article/what-is-diffing) cannot see a race condition or a discount that goes negative under load. Review is for code you will hate maintaining later; tests are for code that is broken now,” Golikov underlines. “A reviewer reads a clean diff, sees sensible names and tidy functions, and clicks approve. None of that tells you a key part of the app malfunctions and delivers a broken service to the user.”

Golikov, who is also [a maintainer of open-source Python](https://github.com/golikovichev) testing tools, explains that the kind of bugs that cause these errors don’t live in the code developers can read. Instead, they live in the states the code gets into at runtime.

## Don’t ship with a warm feeling and no evidence

“When a team treats review as its bug filter, it ships with a warm feeling and no evidence, then finds out in production,” Golikov confirms. “Review is for the question ‘will I hate maintaining this in six months’ and ‘does it actually work’ when a test is run against real inputs, not for a human skimming a pull request at 5 pm.”

There’s little argument among developers and vendors alike that code review processes need to change, especially in the era of AI with the increasing presence of agentic coding tools.

[Judah Taub](https://www.linkedin.com/in/judah-taub-3773247b/), managing partner at [Hetz Ventures](https://www.hetz.vc/), agrees with the narrative here and tells *The New Stack* that for years, engineering teams have treated code review as the last line of defense against bugs, but that was never really their strength.

> “The role of the engineer continues to move further away from the actual code and toward validating architecture, intent and business logic. In the future, even that may be automated,” Judah Taub.

“Code review catches style, architecture, readability and maintainability,” Taub says. “Tests catch bugs. Production catches everything else. The best engineering organizations don’t rely on another developer spotting a subtle edge case buried in hundreds of lines of code – they build systems that automatically verify correctness long before a pull request reaches another human. Code review is to ensure the next engineer can work on the code seamlessly.”

## The future for code review

As [AI-generated code](https://thenewstack.io/anthropic-launches-a-multi-agent-code-review-tool-for-claude-code/) now enters the fray, Taub thinks the inevitable new equilibrium will be one in which humans review less code directly and increasingly review AI reviews of code instead.

“The role of the engineer continues to move further away from the actual code and toward validating architecture, intent, and business logic. In the future, even that may be automated,” he predicts.

We can surely extract key trends here and say that software engineering teams certainly need to get out of the nineties, if that’s where they currently reside.

The combined revolutions of cloud-native, platform engineering, and vibe coding onward to agentic coding (you can add in big data, DevOps, and the standardization towards enterprise open source if you wish) have changed the way software developers work, so there should arguably be a commensurate change in the way they review what just happened.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)