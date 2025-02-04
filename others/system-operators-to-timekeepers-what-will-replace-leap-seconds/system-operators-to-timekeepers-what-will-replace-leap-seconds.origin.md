# System Operators to Timekeepers: What Will Replace Leap Seconds?
![Featued image for: System Operators to Timekeepers: What Will Replace Leap Seconds?](https://cdn.thenewstack.io/media/2025/02/81a06816-george_washington_french_empire_mantel_clock-creative-common-image-via-wikipedia-by-george_washington_french_empire_mantel_clock-creative-commons-image-by-maulleigh-via-wikipedia-1024x772.jpg)
Earlier this month, many tech workers woke to disturbing news from the *San Francisco Chronicle* that [climate change is literally impacting time itself](https://www.msn.com/en-us/science/earth-science/climate-change-is-literally-impacting-time-itself/ar-AA1xqgGj).

The newspaper states:

*Earth’s rotation, for thousands of years, has mostly slowed, the biggest driver being the changing tides that come with the gravitational tug of the moon. Currents in the planet’s outer core, which scientists are still trying to figure out, also have slowed the spin. But the core can speed up the spin, too, which may be what’s been happening recently. Additional leap seconds have become a lot less frequent in the past two decades.*
That impact would be miniscule, according to [a Nature article](https://www.nature.com/articles/s41586-024-07170-0) the Chronicle cites — changing the speed of the earth’s rotation by less than a second a year. But it did raise the possibility that the world could start spinning just a hair

*faster*than expected, which would ultimately create “an unprecedented problem for computer network timing.”
*Nature*‘s article is the work of Duncan Agnew, a geophysicist at Scripps Institution of Oceanography at U.C. San Diego. The *San Diego Union-Tribune* [called him](https://www.sandiegouniontribune.com/2025/01/01/someone-san-diego-should-know-duncan-agnew/) “a “leading scientist in the so-called Earth tides field,” and he’s also a deputy editor-in-chief [at the Royal Astronomical Society](https://ras.ac.uk/journals/Editorial-Boards-and-Team/prof-duncan-agnew-deputy-editor-chief-2015-present).
“A second doesn’t sound like much,” Agnew told the *Chronicle*, but “In today’s interconnected world, getting the time wrong could lead to huge problems.” Imagine timestamped databases and synchronized network operations suddenly dealing with a handed-down-from-above edict to *speed up* by a second at the end of the year — for the first time ever.

If that came to pass, the *Chronicle* writes, it could be a scenario “reminiscent of [Y2K](https://thenewstack.io/how-the-y2k-bug-returned-on-jan-1-2020/), when widespread bugs were feared when the calendar flipped to 2000.”

But fortunately, the world’s timekeepers have already started work on some changes that could head off a problem like this before it starts.

![San Francisco Chronicle headline — Climate Change Impact Time Itself (Agnew on negative leap seconds)](https://cdn.thenewstack.io/media/2025/01/1836500e-20250127_131829-scaled.jpg)
Water from the melting polar ice caps could be subtly affecting the earth’s rotation, the Chronicle writes, citing an article published last year in Nature.

## End of the Leap Second?
Since 1972, tiny changes in the Earth’s rotation speed have been accounted for by adding a “[leap second](https://www.timeanddate.com/time/leapseconds.html)” at the end of some years. This syncs our observed rotation speed with the more precise time-duration measurements from [atomic clocks](https://thenewstack.io/farewell-to-the-internets-master-timekeeper-david-mills/). (Agnew’s article cites a [1960 textbook](https://archive.org/details/rotationofearthg0000munk) that made the point that “the Earth is a geophysical laboratory, not a timekeeper.”)

But those leap seconds have always had their critics. The Chronicle remembers how 2012’s leap seconds caused problems for Reddit and Qantas Airlines, and a 2010 article in *Computerworld* added that 2008’s leap seconds also “[caused Oracle cluster software to reboot unexpectedly in some cases](https://www.computerworld.com/article/1521003/time-waits-for-no-one-leap-seconds-may-be-cut.html).” Concerns finally reached the highest echelons in the world of timekeeping: the [General Conference on Weights and Measures](https://www.bipm.org/en/cgpm-2022) (known by its French acronym *CGPM*), which meets once every four years and chooses the members of the official International Bureau of Weights and Measures.

At their last meeting in 2022, the conference voted to officially reduce the frequency of leap seconds in the future by making rule changes “in, or before, 2035.”

The CGPM’s reasons are clear. Their [2022 resolution](https://www.bipm.org/en/cgpm-2022/resolution-4) acknowledges that using leap seconds “creates discontinuities that risk causing serious malfunctions in critical digital infrastructure including the Global Navigation Satellite Systems, telecommunications, and energy transmission systems.” (And in addition, operators of those satellite systems — and of digital networks — “have developed and applied different methods to introduce the leap second, which do not follow any agreed standards. The implementation of these different uncoordinated methods threatens the resilience of the synchronization capabilities that underpin critical national infrastructures.”)

Their resolution also noted “an extensive survey amongst metrological, scientific and technology institutions” which found agreement on a need to address leap second-related “discontinuities”…

## Undefined Details
So, where do we stand? “There is no change to the leap second rules now,” says Judah Levine, an adjunct physics professor at the University of Colorado at Boulder. Levine is also a fellow at America’s [National Institute of Standards and Technology](https://www.nist.gov/) — and has studied clock synchronization — and says that while changes may be coming from CGPM, they’re also on a slow track. “If the system is changed, it will happen in or before 2035, with a possible additional delay until 2040.”

Still, discussions are already underway. Levine stressed that while the details of the change “are not defined now,” the plans is for the CGPM to “discuss and decide the change at the next meeting in 2026. I assume that there will be a decision at that time, but maybe not.”

For the last 52 years, leap seconds have been added at the end of some years to adjust for a difference between two standard measurements of time — Coordinated Universal Time (UTC) and Universal Time (UT1). The goal is to keep the difference to less than 0.9 seconds, according to a [helpful explanation](https://www.nist.gov/pml/time-and-frequency-division/leap-seconds-faqs) from NIST, which notes, “Usually leap seconds are added when UTC is ahead of UT1 by 0.4 seconds or more.”

Levine tells me that when the CGPM meets again, “The decision will involve an increase in the maximum tolerance between UT1 and UTC, but the value of the maximum tolerance and what happens when this maximum is reached are not defined now.” Still, Levine has been watching the discussion carefully, and several of the proposals mean we won’t see another leap second for many, many years. “The tolerance will probably be increased to at least 60 seconds, but there are a number of alternatives: 100 seconds or one hour.

“There is also the possibility that the tolerance will be increased to a much larger value or may be removed altogether, but I think these possibilities are not likely.”

So what kind of ideas are being put forward? “The community is divided into two main groups,” Levine says:

- “There is a group that advocates for a maximum tolerance on the order of 100 seconds or a few minutes and
- “There is a group that advocates for a much larger maximum tolerance on the order of at least one hour.”
Levine has already given some thought to how this would all play out. “If the maximum tolerance were set to one hour or longer, it would take centuries for the tolerance to be reached and the adjustment process would be decided a long time in the future closer to the event.

“If the tolerance were of the order of minutes, then the maximum tolerance would be reached in about a century, more or less, and the question of what to do at that time is important.

“There are a number of different proposals. I have suggested a periodic algorithmic adjustment, but there are other possibilities and there is no decision.”

## No Negative Leap Seconds?
Agnew’s article raised the possibility of network operators desperately adjusting for a [faster-rotating earth](https://thenewstack.io/webreduce-programmers-on-earth-humans-in-space/) by speeding up their timestamps at the end of the year with a “negative leap second” — and possibly as soon as 2029. The Chronicle reminded its readers that the CGPM voted to get rid of leap seconds by 2035, but “Whether this will be done before the potential need for a negative leap second is unknown.”

So what happens if there’s another leap event — or even a possible “negative leap event” — before the larger difference can be officially ratified? Levine acknowledges that “This whole business would almost certainly be changed if a negative leap second appeared to be imminent before 2035. The most likely solution is that the maximum tolerance would be increased more or less immediately to avoid the negative leap second.”

But he also adds an important caveat. “The probability of a negative leap second is difficult to determine accurately. There are papers on both sides of this question, but an extrapolation on the order of a decade has a large uncertainty, and I would not bet the farm either way.”

Agnew’s article was published beside [a second article](https://www.nature.com/articles/d41586-024-00850-x) agreeing Agnew’s calculations could be cause for concern. And making it impossible to ignore, this second article was co-authored by Dr. [Patrizia Tavella](https://www.bipm.org/en/bipm-staff/tai), director of the Time Department at the International Bureau of Weights and Measures — the group that maintains UTC. If Agnew’s calculations are correct, and adjustments have to trickle through our current time-keeping system, “the problems it could create are without precedent,” Tavella wrote.

But that’s a big if. *The San Francisco Chronicle* had also published Levine’s warning that “The short-term variations in the rotation rate of Earth means that any extrapolation has a very significant uncertainty… I would not make any prediction about a leap event before 2035.”

It’s a day-to-day reality in the life of the world’s standard-makers for the measuring of time itself. And when I asked Tavella about this — about that “significant uncertainty” that Levine says he sees around earth-rotation predictions for the year 2035 — Tavella suggested that he also sees that same uncertainty.

On the difficulties in predicting the specific time intervals of Earth’s rotation, “I completely agree with my colleague Judah Levine.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)