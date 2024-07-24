# 5 Agile Techniques To Help Avoid a CrowdStrike-Like Issue
![Featued image for: 5 Agile Techniques To Help Avoid a CrowdStrike-Like Issue](https://cdn.thenewstack.io/media/2024/07/5ecc3ccb-lala-azizli-tfnytfjpkvc-unsplash-1024x683.jpg)
One of the underplayed strengths of the [Agile](https://en.wikipedia.org/wiki/Agile_software_development) software development approach is its ability to quantify the value of “what if” questions without risking the coherence of the project. That is, Agile has plenty of built-in systems for checking the ground around a project and questioning current practices.

This post looks at how the techniques and ceremonies of Agile can play a vital part in the discovery and confrontation of issues that can cause serious damage if unchecked — as the recent [CrowdStrike controversy](https://thenewstack.io/7-urgent-lessons-from-the-crowdstrike-disaster/) illustrated.

## 1. Outside Context Problem
The “Outside Context Problem” is [a reference](https://en.wikipedia.org/wiki/Talk%3AOutside_Context_Problem), made popular in science fiction, to threats from events we can’t immediately comprehend:

“An Outside Context Problem or OCP is **a challenge utterly outside a given group’s (organization, society, culture or civilization) experiences**. Because an OCP is something that has never happened before, the end result is unpredictable.”

There are many other terms you’ve probably heard that express similar things; from [“unknown unknowns”](https://en.wikipedia.org/wiki/There_are_unknown_unknowns) to [“black swans”](https://en.wikipedia.org/wiki/Black_swan_theory). What we saw from the CrowdStrike issue recently was partly one of these — security software causing a massive outage without a malign actor.

By pushing on the boundaries of a project, even if based only on hunches or experience, insights arrive.

There are plenty of bugs, of all kinds, sitting in code that never cause a problem. We only notice the ones that circumstances reveal. Our job during development is to reduce the surface area where bugs can hide, and figure out reasonable processes to fix whatever rises up.

Agile is exceptionally good at giving a safe playpen to look around a project, for issues the team may not have focused on initially. It channels people’s interest in areas without losing track of resources.

By definition, no one in an organization will spend time considering the possible outcome of things that they have no experience of. However, by pushing on the boundaries of a project, even if based only on hunches or experience, insights arrive. Even if the initial form of a problem cannot be foreseen, the secondary problems can often be.

What Agile offers is both the techniques and a framework that values them. You or your team can adopt these separately without following other related practices, but it is within Agile teams that these techniques have been strengthened over time.

## 2. The Timebox
This is a formal way of limiting the time a sub-team has to examine a slightly off-track issue while keeping it within a **sprint **— a fixed chuck of time in which the team agrees to work on tasks — and accepting that other tasks will be picked up immediately afterward.

It correctly assumes that if a solution requires jumping down a deep rabbit hole, then the solution may not be applicable in the time constraints of the project. This is a good way to understand how no software is an “ultimate solution,” but simply the right way to do things for now, given the resources available. The issue can be revisited at a later time if circumstances change.

**3. The Retrospective**
It is often seen as just an end-of-week ceremony, but it is in fact an essential way of checking assurances given previously. Actions that were promised to be resolved in the sprint just gone, but haven’t been, is a sign that re-assessment is required. It also gives members of the team a chance to listen to brewing storms and intervene.

These can be a bit too close to Maoist “struggle sessions” if not managed by a sensible scrum master or team leader. Having one member of a team question another member is healthy, but can also create friction. Sometimes the result is just an additional item on a checklist, but sometimes it can trigger a major rethink of the project as a whole.

**Privileged Code**
Let’s just take a quick break to look at the shape of the **CrowdStrike** problem, while it is still fresh in our minds, even though we do not know the full details as yet. In most operating systems like Windows, you have programs that run in “user space” as opposed to code that runs in “kernel space”. Only privileged code can run in the kernel, and program code (or threads) running in user space must politely ask the kernel for information, and await the result. To work efficiently, security software needs to run in the kernel, where it can see the internal state in real time. We know when a kernel process detects an error in Windows: you see the infamous *Blue Screen of Death*, and the OS halts to protect itself from further damage.

Microsoft will run a battery of tests against any third-party system that wants to run on Windows in the kernel and certify if it passes. As Microsoft is a massive and thus slow-moving corporation, you can imagine that certification will take some time. If your job as a security company is to spot Day 0 attacks and then spread the response out to all the machines you are paid to protect immediately, waiting for Bob to come back from holiday to run some tests doesn’t scale.

So to get around this, the security company can, from its certified installed code, load in extra pseudo code to take into account moment-to-moment changes.

Let’s stop there. If you were working in a security team and heard about this solution building up over a series of retrospectives, would you intervene? This is a good example of a perfectly sensible solution that nevertheless does have a flaw. ([This video](https://youtu.be/wAzEJxOo1ts?si=oyCk--9HIKAxZA_p) introduces the area of kernel code nicely.)

## 4. Brown Bags
These are usually just short presentations — often during lunchtime — where a team member can select a topic to talk about with the team. These are used to help prepare the ground for changes or coding challenges to come.

These connect up team members’ genuine interest or experience in an area with relevance to the current project. I remember doing one of these on the topic of [Regex](https://thenewstack.io/regular-expressions-and-solving-the-food-taster-dilemma/).

It isn’t always appropriate to let people with an enthusiasm for an area actually run it, but spreading curiosity throughout the team is always a good thing.

## 5. Sprint Zero
This is the sprint in which research spikes are usually established, as well as other bespoke systems needed for the project to succeed.

Some of the smartest things that people work on are ways to fake services for test environments. These have the byproduct of forcing the developers to understand the real service they are faking a bit more, as well as saving time throughout the service lifetime.

**Conclusion**
If you try working backward from a severe incident — asking “How could we have avoided this?” — you will soon forget that real life doesn’t run in reverse, and create near-irrelevant plans. In short, you will be fighting the last war. Even if you have no interest in Agile, think about the ways you can build into your project ways to check your path that does not impede your journey.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)