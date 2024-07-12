# The Complexity of Solving Performance Problems
![Featued image for: The Complexity of Solving Performance Problems](https://cdn.thenewstack.io/media/2024/07/f4ae4b21-slow-1024x576.jpg)
When Google’s Database Black Belt leader talks, people pay attention. Kerry Osborne’s P99 CONF 2023 talk, “[How to Improve Your Ability to Solve Complex Performance Problems](https://www.p99conf.io/session/how-to-improve-your-ability-to-solve-complex-performance-problems/),” is still getting considerable attention even months later.

In a conference that typically features 15-to-20-minute TED Talk-like sessions, Kerry’s came in at just over 40 minutes. But even that wasn’t enough. Kerry has much more expertise to share, and the P99 CONF community is eager to hear it. So, we’re pleased to announce that Kerry will return for P99 CONF 24 to deliver a follow-up talk.

In his own words:

“This is the second part of a talk I did at P99 CONF 2023. The first half focused on the basics of how our brains solve complex problems in the performance space along with the characteristics we need to have/develop in order to be good at it. And finally, I covered some of the basic approaches used, both from experience and from a research standpoint. This talk, ‘How to Improve Your Ability to Solve Complex Performance Problems: Part 2,’ will focus on specific things we can do to get better at it, including an almost foolproof method to reach a successful outcome.”

Since we’re already ramping up for P99 CONF 24, we thought it was a good time to look back at some highlights from Kerry’s original talk.

*Note: P99 CONF is a technical conference on performance and low-latency engineering. It’s virtual, free and highly interactive. This year’s agenda spans Rust, Zig, Go, C++, compute/infrastructure, Linux, Kubernetes and databases. Speakers include Michael Stonebraker, Andy Pavlo, Bryan Cantrill, Liz Rice, Gunnar Morling, Tanel Poder and Ashley Williams. *
[See featured speakers + access a free P99 CONF 24 pass](https://www.p99conf.io/)
## Why Performance Problems Are So Hard To Solve
Let’s talk about the problem characteristics of what we’re trying to solve in the performance space. They’re complex, right? There’s almost always multiple solutions to any given problem.

If somebody comes to me and says, “Hey, my database is slow,” there’s a million different things that could cause it to be slow — or just cause the perception that it’s slow. There could also be a lot of different solutions that would speed that system up. If somebody has a more specific issue — like “My IO system is slow” — there are often many solutions that I could apply to make the IO system work better.

Those solutions vary in a number of different ways: benefits, cost and risk.

### Benefits
Most people focus on the benefits. For example, if the IO system is slow, I could try to improve the speed of the IO system by putting in solid-state disks, or by trying to separate the large multiblock reads from the single-block reads so that my single-block reads are not delayed by having to wait in a queue behind large multiblock reads that take longer.

There’s a number of ways that I could go after that, and the benefit of each of those potential solutions could be different. The solid-state disk could speed it up by 10 or 100 times. Changing the queuing mechanism might speed it up by five times. There are different amounts of benefits that can be accomplished by the different solutions that are proposed. That makes the problem space complex.

### Costs (Monetary, Time To Implement, Opportunity Cost)
Another thing that varies is the cost of implementing those solutions. It’s probably a lot more expensive to go buy a whole solid-state disk system than it is to work on how the IOs are queued or something else related to software. And there are multiple types of costs to consider: monetary costs, time to implement and also the opportunity cost. What’s lost by taking longer to implement a solution can far outweigh the monetary cost. We have all these different spaces to keep in mind, just in the cost area.

### Risk
Risk is also a factor. When we’re talking about implementing systems and production systems, anything that you do on a production system introduces some amount of risk. We’re often trying to minimize the risk of any changes that we make, while still maximizing the benefit. It’s a trade-off between at least these three areas — and often many others as well.

### Proposing Performance Solutions With These Characteristics in Mind
When working with stakeholders, we often have to explain: “Hey, we’ve got three or four potential solutions here. We’re going to recommend this one, and here’s why.” In my team’s reports, we often include a sentence like this:

“The following list of recommendations is a balance between urgency and ease of implementation, slightly leaning towards urgency.”

In this case, the cost of “time to implement” was really important. It was urgent to get it resolved quickly. Other times, risk or value might take precedence. When proposing solutions to performance problems, it’s important to consider the various priorities and explain why you recommend one solution over the other. It’s not always about maximum benefit.

## Your Brain Solving Performance Problems
Our brains work in two different modes, particularly as we’re solving problems: intuitive and analytical. Intuitive is the mode that our brain is in when we’re not actively and effortfully thinking about something. It’s automatic. Analytical is the mode where we’re actually applying effort and working diligently in a focused manner in our brains.

For example, if you see this very simple equation, 1 + 1 =, you’re not going to apply any effort to solving it. You already know from your childhood that 1 + 1 = 2. The answer is immediate. That’s something that your brain does in automatic mode.

Our brains run in this automatic, intuitive mode all the time throughout our day-to-day activities. Unfortunately, a lot of biases can creep in when we’re in that mode, and often we don’t even know that they’re happening.

For example, when I see a set of symptoms on a computer system or a database system, I have a tendency to think that I’ve got enough information at this point — that I know everything there is to know about the problem set. Often, that’s not the case at all. I have to constantly remind myself: “Hey, there may be other facts that you need to be looking at before you start trying to solve this problem.”

So what really happens in our brains when we start trying to solve a performance problem?

### Step 1: Defining the Problem
With a traditional problem-solving approach, the first step is defining the problem. That sounds super simple, but defining the problem is actually more important than you might think. How we define the problem can significantly narrow the solution space, so we want to be very careful about how we define the problem.

For example, assume our problem is that our user contacted us and said “Hey, we’ve got this batch job that runs every night, from 1 a.m. to 2 a.m. We have to deliver the end result to the next system in the pipeline by 2 a.m., but this system is no longer completing the job in that one-hour timeline. And it seems like the IO system is the main problem: It’s running slow; it’s not behaving the way we’re used to seeing it behave.”

How do we define that problem?

- “The batch process is not finishing in an hour” is a pretty good broad description of the problem.
- “We need to speed up the IO system because the IO system is slow” is a very narrow definition of the problem.
### Step 2: Gathering Data
Why is this problem definition so important? Because our next step is gathering data to understand what’s causing the problem.

Assume our definition is that the IO system is slow. Thanks to our biases, our brain will automatically want to discard any data that doesn’t have a bearing on what’s causing the IO system to be slow. That’s just the way our brains work. They’re going to discount that data — maybe not ignore it altogether, but certainly discount it and not pay much attention to it. That’s why how we define the problem is super important. We need to gather data in a methodical fashion.

### Step 3: Postulating a Reason for the Problem
In the traditional way of solving problems, it’s very important that we have the mental discipline to defer this step until we’ve got a good definition and a good set of data. If we start postulating about the reason as soon as we get an idea in our head about what’s causing it, our brains start tricking us again. We’ll start evaluating the importance of any data that we see or any symptoms that we see based on that premature postulation — so we have to be careful about that.

### Step 4: Listing the Possible Solutions
This is where we use the creative part of our brains to try to come up with opportunities for fixing the problem. Often, this is where we gather in a room, brainstorming with multiple people and drawing things on a whiteboard, etc.. This is an important step! We want to give ourselves adequate time to do this and also have an environment where nothing is out of bounds in terms of suggestions for ideas. This is not the place to say “Well, that’s a stupid idea.” This is the place to throw everything out there and make a very comprehensive list of everything we can think of.

### Step 5: Ordering the Possible Solutions
The fifth step is ordering the possible solutions. This is where we start potentially eliminating things based on cost or risk. The goal is to create an ordered list of what we think will provide the greatest benefit with the least risk and cost. But remember that priorities vary and we need to weigh those things against one other. Once we have that list and stakeholder buy-in, we attempt to implement the possible solutions in the agreed-upon order.

## Real-World Approaches
Now, let’s look at how experts in the performance space are actually approaching complex performance problems.

### Intuitive (Jump Around Approach)
You can call the intuitive approach the “jump around approach.” The key defining characteristic of it is that we jump ahead. Earlier, I mentioned that it’s hard not to jump ahead to Step 3 of problem-solving, which is theorizing about what’s causing the problem. Keep in mind that when we get pulled into a situation, we always have at least a little bit of information about it.

Nobody ever says, “Come fix my system,” without telling you what the problem is, right? They might just tell you that it’s slow, but there’s almost always something along with that. Maybe “It’s slow and I think there’s an IO problem” or “It’s slow and it looks like we’re pegging the CPU between two and three o’clock in the morning.” There’s always a little bit of information. That information gives us the ability to start theorizing early. That’s the main characteristic of this approach.

There are pros and cons of this approach. We often miss important data because we’re not going through a methodical data-gathering step. We often come up with less creative possible solutions because we’re not going through a rigorous brainstorming session to try to come up with everything we can.

But there are some positives as well. Since we haven’t invested a lot of time, our brains are willing to quickly abandon an option. With a more methodical approach, we might have five options that are very strictly ordered, then try out each one in order until we reach the end of the list. With the intuitive approach, we might start by checking the first option, go part way through testing it, then come across some other fact that we didn’t gather in the initial stage. At that point, we might immediately jump to option 5 because that now looks like the best direction.

Our brains are OK with that because we haven’t invested a super long time in coming up with a methodical approach. We’re flexible with reordering the options as well as with abandoning an approach.

### Methodical Approach
With the methodical approach, we’re basically going dogmatically through the steps outlined above. And the key characteristic of this one is that we have the mental discipline to postpone that theorizing step until after we’ve gathered the data.

There are pluses and minuses with this approach too, of course. The problems are more well-defined, more data is available, more creative solutions are possible. However, since more time is invested, it often takes longer to come up with a solution. Also, we’re less willing to adapt the plan over time because of the amount of effort that we’ve invested in it.

### Combined Approach
There’s also a third “combined approach” option — and this one is the most interesting to me, and it’s also the one that’s most often used by others who are highly experienced in the performance space.

This approach jumps to theorizing almost immediately. Experienced people can almost immediately identify a few usual suspects. If somebody has been in this business for a while, they’ve probably seen something similar, some set of symptoms that were close, and they can pretty quickly theorize. Their brain immediately goes to, “Hey, I’ve seen something like this. I’m going to check this, that and the other.” They can do that very quickly and either say, “Yep, that’s what it is,” or they can eliminate it from contention.

The key thing here is that if you discover that the usual suspects don’t pan out, you can always fall back to the very methodical approach. That transition can be difficult after you start off in this intuitive mode where you’re jumping around.

Also, this approach seems very helter-skelter. If somebody’s watching over your shoulder, it might cause them to lose some confidence in your capabilities. From that perspective, it might look like you’re all over the place and don’t really know what you’re focused on.

This technique is called “[recognition primed decision-making](https://en.wikipedia.org/wiki/Recognition-primed_decision).” It’s used pretty extensively in industries or professions where there’s a high sense of urgency and very high stakes. For example, think of firefighters when they’re trying to come up with a plan to attack a fire in a large building. Lives are on the line, and they have to make decisions very quickly. Airline pilots also have a documented checklist that they go through in emergency situations; that’s based on the same sort of approach.

### Recommendations
In my opinion, this combined approach usually delivers the best results for reasonably experienced people — and especially when the urgency is high. This is absolutely the quickest way to solve the problem if the usual suspects pan out. The methodical approach is better than the straight intuitive approach. For somebody that’s not very experienced, the intuitive approach — just hopping around between things — is generally the worst approach. The methodical approach is better because it generates more confidence with stakeholders.

But although the intuitive approach is generally a great fit for people who haven’t been doing this kind of work for quite a while, it can occasionally be the fastest — if you’re very experienced, or if you’re just lucky.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)