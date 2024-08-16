# Bringing Back the Joy of Software Development
![Featued image for: Bringing Back the Joy of Software Development](https://cdn.thenewstack.io/media/2024/08/90353c94-priscilla-du-preez-xkkcui44im0-unsplash-1024x683.jpg)
Years before he was a CEO, an investor or an executive making his way up the corporate ladder, [Andy Lin](https://www.linkedin.com/in/andylin888/) was a software engineer, his fingers deep in the 1s and 0s, working 12 to 14 hours a day and sometimes spending as many as 48 consecutive hours coding on projects he was really into.

Lin remembers clearly the ongoing conflicts between developers and their project managers fueled by disagreements over timelines and priorities and the constant push and pull between quality and speed of delivery.

“What happens when you have this mismatch and that lack of understanding is we start thinking of the worst of each other as human beings,” Lin, now the CEO of [Provoke Solutions](https://provokesolutions.com/), told The New Stack. “Managers go, ‘Developers just aren’t working hard enough. Why don’t they just work a little harder and give me more widgets?’ Engineers look at managers and go, ‘They just don’t understand us. They don’t care about quality. They’re just a bunch of bean counters.’”

This disconnect comes down to what he calls “all of the technical debt that we do — the soul-sucking tasks that we do as a developer. That’s not something that a manager is going to understand. That’s not something that goes into a work plan.”

To address this, Provoke recently introduced Knovva (pronounced “nova”), a generative AI-based platform and suite of digital co-workers that can be used to do those routine, soul-sucking tasks and freeing developers to more quickly create the functions and features that managers are looking for, bringing greater peace to the meeting rooms.

Lin said developers spend as much as 40 percent to sometimes 90 percent of their time on these low-value, rote chores, like running test automation scripts or testing code quality with a [static code analysis](https://thenewstack.io/how-static-analysis-can-save-your-software/) tool that then spits out defects and improvements that become the task of developers to make. That adds hours to work weeks that already are bursting at the seams.

“I remember driving to a client knowing this week was going to be ‘code quality cleanup week,’” he said. “I was in typical L.A. traffic, and I was enjoying the traffic more than the idea of going in there and then spending the next three days trying to fix code quality issues.”

## Generative AI Brings Help
There were steps made to improve the technical debt problem, like [Agile development](https://thenewstack.io/heres-what-a-software-architect-does-in-an-agile-team/) or using a product mindset so that code is treated like a product and nothing is deprioritized. But they were Band-Aids, Lin said. Nothing was solved.

Then came [generative AI](https://thenewstack.io/generative-ai-tools-for-infrastructure-as-code/).

“With generative AI and our digital coworkers, you can actually crack that nut,” he said. “Now, as a developer, I will not have to worry about some of these soul-sucking tasks because we’ve built digital coworkers to do those. The ROI is amazing. It’s like 10x. What used to take 300 hours will take our digital coworkers 30 hours.”

Provoke’s patent-pending Knovva platform includes pre-trained digital coworkers that automate many of the tasks in the software development lifecycle, including code development and quality, [test automation](https://thenewstack.io/test-automation-tools-unite/) and [DevOps](https://thenewstack.io/devops/). One is designed to do the work of a quality engineer, ensuring that products and services meet quality standards.

Another focuses on app modernization, as organizations run initiatives like transitioning an application from [Angular](https://thenewstack.io/google-angular-lead-sees-convergence-in-javascript-frameworks/) to [React](https://thenewstack.io/meta-releases-open-source-react-compiler/) or from React v9 to React v18. The digital coworker will make the transition, gather the list of defects, and try to fix them.

Another is Align, which takes a UI spec, compares it to the UI that was built and identifies all the variances. Align gives a list of variances to the developer, who can move them into [Jira](https://thenewstack.io/anti-agile-project-tracker-linear-the-latest-to-take-on-jira/) or Azure DevOps and resolve them. In the second iteration of Align, the digital coworker doesn’t just put the variances into the queue and leave them for the developer, but “makes all those adjustments,” Lin said. “They don’t just identify the problems; they fix the problems.”

## Still in the Early Stages
The company, which has about 75 customers and 150 employees spread across offices in Dallas and New Zealand, has been building Knovva for more than eight months. Provoke engineers have built infrastructure services in the platform and have other patent-pending technology to maintain state between snapshots of content windows, which initially were small but have become larger.

“Enterprise code bases are 6 million lines of code,” he said. “That’s pretty easy to come across. It doesn’t matter how large your context window is. You need this chunking strategy that we developed and to be able to maintain state across all those different chunks of code across context windows.”

Throughout all this, the human is still prominent in the loop. There is human feedback-reinforced learning built into the platform and captured via [retrieval-augmented generation (RAG)](https://thenewstack.io/retrieval-augmented-generation-for-llms/). Every enterprise, as it’s fixing defects, will generate code and Provoke wants humans to review whether it meets coding standards.

“Just like you would review every developer, you’d have a tech lead review developer code, and you say, ‘Yeah, this looks good. This not so good. This one needs this tweak,’” Lin said. “All of that gets fed back into the Knovva system and be a RAG the next time you run it. That code will be a lot closer to what that enterprise’s or organization’s standards are.”

## Runs in the Cloud
It’s a cloud-based service. Provoke builds a platform in its environment for demos, but then places it into a container and shipped to the customer, which can then place it into any cloud-based [large language model](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/) (LLM) they want, whether that’s in [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) (AWS), [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure or something else. It’s also self-contained, so whatever data the customer puts into it doesn’t become public data that is used to train a competitor’s LLM.

The company has moved into the next phase of developing Knovva, where engineers developing a way for custom agents that can be configured to meet an organization’s specific needs, Lin said.

“We don’t know every single business problem out there in the world,” he said. “We’re focused on engineering and user experience problems, but there are these [specific] kinds of problems, and we can still use the platform and use the same services that we’ve built our own digital code off of to build what we’re calling ‘custom digital coworkers.’”

## A Growing Pipeline
Provoke is working with some enterprises, including a bioinformatics company that outsourced its entire product development operation to the vendor. They needed to get started while hiring their own team. Typically, they would have to hire two quality engineers. With Knovva, they need only half of a quality engineer, with Provoke’s technology reaching 85 percent to 90 percent code coverage.

Another company is using Knovva and its coworkers to resolve conflicts as it moves from one version of React to another. Lin also said the company is “on the goal line” of getting its first customer for Align. “The pipeline is strong,” he said.

Lin’s hope is that Knovva and its digital coworkers change the job of being a software engineer.

“A side effect of using Knovva is you will save money, but I think the real reason, the real motivation behind it — the real North Star for us — is bringing joy back to the work environment,” he said. “We spend eight to 10 to 12 hours a day with people at work — virtually, physically, whatever. Shouldn’t that time be more positive? Shouldn’t it be more joyful? Shouldn’t it be that way so that when we do get home with our families, we’re happier human beings?”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)