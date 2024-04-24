# Ukrainian Coder’s New Programming Language: One Big Data Structure
![Featued image for: Ukrainian Coder’s New Programming Language: One Big Data Structure](https://cdn.thenewstack.io/media/2024/04/8f4d7751-head-1597572_1280-1024x655.jpg)
This year saw the launch of a new programming language consisting of one giant data structure — so that programmers can avoid ever having to name things.
It’s “a tongue-in-cheek reaction to the everpresent naming problem,” software engineer
[Oleksandr Kaleniuk](https://www.linkedin.com/in/okaleniuk/recent-activity/all/) said in an email interview. “Naming is hard so let’s not name anything at all and see if this way programming gets any easier.”
Spoiler: He then added, “It doesn’t.”
“The language has no real-world applications but it’s fun to play with both as a developer and a user.”
Even the language itself has no name.
![The namingless programming language - code snippet](https://cdn.thenewstack.io/media/2024/04/e0a6f63e-the-namingless-programming-language-code-snippet.png)
A snippet from the namingless programming language documentation.
## The Language
“There is one and only one data structure,” explains
[the language’s repository](https://github.com/akalenuk/the_namingless_programming_language) on [GitHub](https://thenewstack.io/github-developer-productivity-at-30-billion-messages-per-day/). “Since there is only one, *it doesn’t need a name*.” Yet branches and sub-branches within that data structure can represent smaller arrays and even matrixes. Pairs of characters indicate everything from strings and numbers — as well as logical comparison and mathematical operations. (And there are even symbols for reading or writing data from a file — or even deleting that file.)
“There is also the operation. Not ‘an operation’ but ‘the operation’ since there is only one operation in the language.
“Since there is only one,
*it doesn’t need a name* either.”
The interpreter works its way through its one-and-only data structure, adding values onto the stack whenever it encounters the
*_* symbol, or operating on them (if the _ symbol precedes a mathematical operation).
“Since there is only one such language in existence, it doesn’t need a name.”
And the character pair for “help” is
*e_* (so running a file named *the_namingless_programming_language* would launch the help menu as soon as the parser hits the *e_* characters…)
The resulting glob of source code is even used as the filename “to avoid the naming problem for the programs you write.”
And finally, the official repository on GitHub also stresses that even the language itself also has no name. So the act of referring to it as “the namingless programming language” is, instead, merely speaking a
*definition* of what this as-yet-unnamed language is attempting to accomplish.
“Since there is only one such language in existence, it doesn’t need a name.”
## Inspirations
Yet there are some real programming concepts at work here. Kaleniuk says namingless is “just a fancy name for stack-oriented and tacit.”
This means it was inspired by languages like Forth, APL, and
[Uiua](https://www.uiua.org/) (which Kalenuik says also incorporates array programming and stack orientation). However, in our email interview, he said his main inspiration was another stack-oriented language: [PostScript](https://en.wikipedia.org/wiki/PostScript).
PostScript is famously a “page description” language for the electronic publishing industry, sending not just data (about where lines and curves should be drawn) but also code, according to Kaleniuk — “a runnable program that is open for interpretation by the machine that does the actual printing.” And the same need crops up at Kaleniuk’s job as a software engineer for a global 3D printing company.
Wouldn’t it be useful if the shapes to be printed could be encoded in a
*formula* instead of a just one massive dump of data?
Kaleniuk settled on an array-processing language to keep everything concise. “We’re talking about gigabytes of code/data.” And since it’s “99% machine produced and 100% machine consumed,” it can also be highly abstract (since, as Kaleniuk sees it, “Nobody would want to read that anyway.”) That led Kaleniuk to settle on a stack-oriented language using highly abstract
[tacit programming](%E2%80%9Dhttps://en.wikipedia.org/wiki/Tacit_programming%E2%80%9D).
Kaleniuk calls it “just an
[experiment in design](https://thenewstack.io/the-power-of-prototyping-in-user-experience-design/), a thing to play with, a toy…
## Coding in Kyiv
Kaleniuk also writes a website with programming and math tutorials (along with demos and quizzes) called
[. (Just last month he added a post running through all the technologies that were supposed to have a competitive advantage Words and Buttons Online](https://wordsandbuttons.online/) [over his long-time programming language, C++](https://wordsandbuttons.online/the_real_cpp_killers.html).) And last year Kaleniuk also authored the book *Geometry for Programmers*. (“Master the math behind CAD, game engines, GIS, and more!” says its [official page](https://www.manning.com/books/geometry-for-programmers)at Manning Publications (where the entire text is available online for free).
But since 2015 he’s been a software engineer at the Kyiv branch of
[3D printing company Materialise](https://www.materialise.com/en/about/locations/ukraine), switching to a project manager role two years ago. “I hope to put that aside as soon as war is over and we’re back to normal,” Kaleniuk said in our email interview.
“To be honest, I was hoping the war would be won by now…”
Kaleniuk was working in Eastern Ukraine in 2014 so he’d already spent a few months under Russian occupation, and reached the conclusion that “Russia is not that strong, just barbaric.” And he also remembers the first day of Russia’s full-scale invasion. “On February 24, 2022, I woke up to the sound of an incoming missile, went to my PC, opened my bank app, and donated to the army. I did the same in 2014. It’s like a rule. Every time you hear a blast — you donate. That gives you the illusion of control…
“You also check that the financial system is still working.”
Today he
[says most of the software engineers](https://thenewstack.io/85-of-engineers-say-theyll-use-an-idp-in-2024/) he knows who aren’t in the army pay their taxes “and split the rest between the army and the family. Although some work for the front directly… We want the war to be over and we’re willing to pay for it…”
Hanging over it all is a very clear sense that this is a war. “Some already paid with their lives. My friend was killed in action a few days before my book came out in print. He was a software engineer too.” Kaleniuk tries to split his own donations between the ministry — who he said “buy shells and rockets” — and non-governmental organizations and individual volunteers (who “help close urgent requests fast but they don’t do weapons and ammunition.”)
The first payment from his book’s publisher came in early March of 2022 — just weeks after Russia’s invasion — “and I immediately donated that too.” And the war continued… In December Kaleniuk
[wrote on his website](https://wordsandbuttons.online/why.html) that “About an hour ago, a Russian missile hit something in my neighborhood. Again.”
“As a civilian, an engineer, and a mathematician, I can’t do much about this. But I can earn a few bucks and donate to people who can. That’s what I have been doing since February, and that’s what I’m planning to do until the victory.”
## Reactions
Earlier this year Kaleniuk found his programming language being
[discussed on Hacker News](%E2%80%9Dhttps://news.ycombinator.com/item?id=39362200%E2%80%9D). And Kaleniuk was delighted that it received a “mostly positive reception”.
“This kind of reminds me of super low-level programming, manipulating stacks of data etc,”
[wrote](https://news.ycombinator.com/item?id=39364589) Australia-based web developer [Ben Winding](https://benwinding.com/about/), adding “it could prove to be a useful learning tool.”
There was the inevitable discussion about how naming improves readability, but several commenters were appreciative of Kaleniuk’s efforts, with one saying saw the
[true value of the experiment](https://news.ycombinator.com/item?id=39426993). “From my own experience, working on ‘silly’ projects like this, with severe artificial constraints for example, can be quite interesting and challenging and lead to lessons learned that can be applied to real projects later.”
Kaleniuk says he’s moved on to other projects — but feels richer for the experience. “I do keep the lessons I learned in mind so maybe some day you’ll see some awesome 3D printed thing and think ‘How did they manage to print something that complex?’ And you’ll remember that small esoteric language with no real-world applications at all…”
## Epilogue
Towards the end of the README file, Kaleniuk acknowledges the language was created “to get it out of my system and it was a great success. I mean, I did get it out of my system successfully, and I somehow don’t feel like playing with it anymore.”
“Is it beautiful? No,” Kaleniuk posted on LinkedIn. “Is it practical? Hell no. Is it fun? More than you’d think it would be.”
In our email interview, Kaleniuk also told us where that all leads to. “I had fun with it, and now I shared the code so others could play with it too.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)