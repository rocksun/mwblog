# Scrum Sucks Because You’re Doing It Wrong
![Featued image for: Scrum Sucks Because You’re Doing It Wrong](https://cdn.thenewstack.io/media/2024/12/b06b609e-lala-azizli-tfnytfjpkvc-unsplash-1024x683.jpg)
[Lala Azizli](https://unsplash.com/@lazizli?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/people-using-laptop-tfNyTfJpKvc?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
I can hear you screaming at your screen.

*“I’ve done scrum, and it’s terrible. It adds too much structure, too many meetings, and puts values on metrics instead of just doing the work.”*
Most people don’t like scrum because they use it as a checklist of things to do rather than using it as intended, as a mindset to [enable incremental delivery](https://thenewstack.io/software-delivery-enablement-not-developer-productivity/).

In this post, I will highlight the most common issues I have heard and seen with scrum and hopefully give you actionable takeaways to resolve them.

## Scrum Fundamentals
At its core, scrum is an [agile methodology](https://justanothertechlead.com/software/top-agile-cheat-sheet-essential-tips-and-terminology-2/) that focuses on incremental delivery.

**The ideal Scrum team**
**Product Owner**: This is the core person who decides the direction and feature set of the product on which you work. They are experts in the industry and have a clear vision of where the product needs to be. They work closely with senior management, sales, and clients.**Scrum Master**: The organizer of the team. The scrum master ensures that[requirements are accurately gathered](https://thenewstack.io/platform-teams-automate-infrastructure-requirement-gathering/), followed by the scrum process, and deals with any blockers quickly. They also ensure that all scrum ceremonies are held and are helpful.**Dev Team**: A team of cross-functional, self-organizing engineers. The people who write the code.**QA**: A dedicated tester assigned to the scrum team.
**Scrum Ceremonies at a Glance**
**Sprint**: A period that’s usually two or three weeks. This is the period in which the development of a story both starts and finishes.**Planning**: A meeting before the start of the sprint whereby the team decides on which stories they will work on (and, importantly, complete)**Daily Standup**: A ~15-minute daily meeting in which every team member talks about “what I worked on yesterday,” “what I’ll work on today,” and “any blockers.” This is a quick status meeting to ensure that everything is going smoothly.**Sprint Review**: At the end of each review, the team will demo the work they have completed to the product owner and other stakeholders.**Sprint Retrospective**: The team reviews the previous sprint and discusses what went well and what could have been improved.
Remember, at its core, scrum is about committing to pieces of work you will deliver in a certain period. Scrum promotes focusing on small, specific items of work (Stories) that everyone will work on (Swarm) during a small, fixed amount of time (Sprint).

Scrum promotes constant improvement via retrospectives and more accurate planning through velocity.

That’s it. That’s all scrum is.

## So Why All the Hate?
From my perspective, engineers hate scrum. They see it as a waste of time that binds them to arbitrary timelines and adds pointless meetings.

If I boil it down to the following sentence, do you think anyone would disagree that this is a good idea? *Scrum is a way to estimate work more accurately while getting regular feedback on the **product and improving the team** as you go.*

I think that’s a good thing, personally.

## Common Scrum Mistakes
**Partial Adoption**
I’ve been in teams that previously used some waterfall planning methodology and kept the majority of waterfall practices, but now, we have scrum ceremonies every two weeks.

The issue is that waterfall and [agile](https://thenewstack.io/agile-reinvented-a-look-into-the-future/) differ in planning and approach.

Waterfall frontloads the planning and assumes a fixed delivery. Agile has more of a “[plan as you go](https://thenewstack.io/engineers-must-become-agile-collaboration-ninjas/)” aspect, and delivery can change sprint on sprint depending on the input of the stakeholders (the core delivery remains the same, but the details may change).

It’s impossible to backfill a waterfall project plan into an agile one.

If you already have a waterfall plan for a project, you need to do one of two things:

- By delivering the project using the existing waterfall plan, see if it is through.
- Fully adopt agile and restart the project to focus on incremental delivery. Be open to change and deliver something of value every sprint.
**Incorrect Team Setup**
A key aspect of scrum is having a fully cross-functional team. Scrum requires a product person, QA, scrum master, and some engineers. I usually hear people tell me that they use scrum, that their [team is only four to eight engineers](https://thenewstack.io/top-challenges-to-creating-high-performing-engineering-teams/), and they are missing the other roles.

The puzzle needs all the pieces.

Ideally, a team would have dedicated experts for each of these roles. If you don’t have the budget for that, however, you can compromise by nominating engineering team members to take each role and own it for that project.

For example, the engineer with the most product knowledge assumes the product role during ceremonies, and the person with the greatest focus on testing becomes the QA.

**‘Pointless’ Standups**
A standup is a ~15-minute meeting. That’s it. Each member talks about their “Yesterday, Today, Blockers.” When standups are misused, they can become long and drawn-out affairs.

What’s the solution? You need a strong Scrum Master to keep the meeting on track.

In my experience, when a conversation goes too deep, simply saying something like “I’ll make a note that we need to follow up on this in another meeting” is good enough.

As long as people know their concerns will be addressed later, they will be okay. Make sure you book those follow-up meetings, though!

**Metrics Overload**
Scrum’s velocity is derived from stats.

When planning your stories, you as a team give them magical attributes called “story points,” which mean absolutely nothing outside of your team. Story points are a method of assigning a relative size to a piece of work as a team.

Once you’ve been doing this for a while, you start to understand your team’s velocity.

You can accurately predict that your team can complete 30 story points of work in one sprint. As long as your team estimated the work, this should be accurate.

Velocity will only be accurate if you treat it with respect. Scrum masters must review the plan and story points before the sprint starts. This tells you exactly how many points you delivered in that specific period. Generally, you want to average the story points you delivered per sprint over about five sprints. This will give you a reasonably accurate number.

Ensure the same person always awards the points. The numbers are no longer meaningful if your team composition changes every sprint.

**Retrospectives**
A retro should highlight the positives and negatives of your team’s process. You should learn from retrospectives.

But what about if you have the retro at the end of every sprint but never action any of the items? What about if you never do anything with the information you get in the retro? That’s pointless and a common pitfall I see among teams! While it can be cathartic to get in a room once every two weeks and complain, if, after a while, those complaints become noise as nothing is ever done about them, people get (rightly) frustrated.

Make sure you action the takeaways from the retro. Without doing this, your team will miss the benefit of having the meetings.

**Product-Based Reviews**
The engineers should conduct a review to show stakeholders the value of their sprint work.

They should show the stakeholders completed work and get feedback on whether they did the “right” or “wrong” thing in the sprint.

Too often, reviews become a show-and-tell from the product owner and one-way communication between the product and engineering. While potentially helpful, this is not the purpose of the review.

Keep reviews focused on what you have delivered as an engineering team over the last sprint. Get feedback on that work and what is coming up in the following sprint, and leave it as is.

## Summary
I’ve worked in the industry for 20 years in agile, waterfall, and “no real plan” workplaces.

When done well, scrum works very well. Scrum done poorly hurts the product and the morale of the team.

There are plenty of resources out there to learn scrum and agile well, so before completely abandoning them in your company, please first try to address some of the pitfalls I’ve mentioned here.

*This article is part of The New Stack’s contributor network. Have insights on the latest challenges and innovations affecting developers? We’d love to hear from you. Become a contributor and share your expertise by filling out this form or emailing Matt Burns at mattburns@thenewstack.io.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)