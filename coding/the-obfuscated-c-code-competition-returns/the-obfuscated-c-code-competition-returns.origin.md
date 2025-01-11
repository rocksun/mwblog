# The ‘Obfuscated C Code’ Competition Returns
![Featued image for: The ‘Obfuscated C Code’ Competition Returns](https://cdn.thenewstack.io/media/2024/11/c7e3eb34-c-safety-1024x683.jpg)
After a four-year hiatus, the “International Obfuscated C Code Contest” is making its glorious return in 2025.

The goals of the IOCCC:

- To write the most obscure/obfuscated C program within the rules.
- To show the importance of programming style, in an ironic way.
- To stress C compilers with unusual code.
- To illustrate some of the subtleties of the C language.
- To have fun with C!
As the fun ramps up again, the judges will begin accepting wonderful [new “obfuscated C” programs](https://thenewstack.io/a-tradition-continues-the-international-obfuscated-c-code-contest/) starting on January 31 (with their window closing on April 1 — April Fool’s Day). But they’ve also spent the last four years massively updating [the contest’s website](http://www.ioccc.org/) — so even winning entries archived from the past 40 years now possess “the ability of reasonable modern Unix/Linux systems to be able to compile and even run them.”

An [updated FAQ](http://www.ioccc.org/faq.html) acknowledges that, rather than keeping that code obfuscated, the site “has shifted to a more educational theme.”

Maybe the organizers are finally recognizing their own status as a cultural icon — their ongoing role of inspiring young coders with examples of incredible complexity and creativity, while also bearing witness to their own bits of programming history.

Although, in the true spirit of the competition, sometimes they seem to be making things up as they go along.

![Screenshot from Landon Curt Noll's GitHub profile](https://cdn.thenewstack.io/media/2025/01/a5947686-screenshot-from-landon-curt-nolls-github-profile.png)
Screenshot from the GitHub profile of IOCCC co-founder Landon Curt Noll

## Where Chocolate Meets Steganography
The playfulness seems to be everywhere — and it ultimately becomes contagious. “Over the years, more than one IOCCC judge has been known to bribe another IOCCC judge into voting for a winning entry by offering a bit of high-quality chocolate,” noted [the official guidelines](http://www.ioccc.org/next/guidelines.html). So one [2012 entry](http://www.ioccc.org/2012/vik/index.html) demonstrated its steganography application — hiding source code within an image — by using a photo of some luscious chocolates.

[Rule 26](http://www.ioccc.org/next/rules.html#rule26) of the official rules consists of nothing but nonsense sentences using all 26 letters of the alphabet exactly once. Meanwhile, the contest’s official FAQ offers cheeky answers to questions like [why they’re on Mastodon](http://www.ioccc.org/faq.html#try_mastodon). “The IOCCC no longer uses Twitter, or whatever that someone who appears to have poor impulse control (allegedly) calls their platform these days. The IOCCC prefers to reside in the [fediverse](https://fediverse.info/).”
And [how did the contest start?](http://www.ioccc.org/faq.html#ioccc_start) “It was a dark and stormy night…”

## Competing To Be the Worst
The context began on March 23, 1984, when a 23-year-old Landon Curt Noll was working with Larry Bassel at the National Semiconductor, porting [UNIX](https://thenewstack.io/unix-creator-ken-thompson-to-keynote-scale-conference/) onto the company’s microcontrollers. Bassel was wrestling with a bug in the Bourne shell, while Noll was working on a version of the finger command from early BSD. Soon they’d [announced a contest](https://groups.google.com/g/net.lang.c/c/lx-TAuEyeRI/m/HdOOnNx6LC0J?hl=en) “to compete with the worst C hackers around,” and the first entries started pouring in.

“When we began to receive messages from outside of the U.S., Larry and I decided to include International in the name,” Noll wrote in the FAQ.

Even in that first year, they saw entries from some of the big names in the coding world, including Bell Labs programmer [David Korn](https://en.wikipedia.org/wiki/David_Korn_(computer_scientist)), creator of the Korn shell (1987), and [Perl programming language](https://thenewstack.io/week-programming-renaming-perl-save-terminal-unpopularity/) creator [Larry Wall](https://en.wikipedia.org/wiki/Larry_Wall) (1986, 1987). It set a high bar that continued as the contest rolled along.

Over the last 40 years, its judges have recognized 197 different winners. And several of them have their own Wikipedia entries:

- Google DeepMind researcher
[Nicholas Carlini](https://en.wikipedia.org/wiki/Nicholas_Carlini)won 2020’s “[Best of Show: abuse of libc” award](https://www.ioccc.org/2020/carlini/index.html). - In 1989 the “Best of Show” award went to
[Ora Lassila](https://en.wikipedia.org/wiki/Ora_Lassila), known for his early work on the Semantic Web and the RDF specification. Now a long-time member of the W3C advisory board and a principal graph technologist at AWS, Lassila won in 1989 for writing a[compressed Lisp interpreter](http://www.ioccc.org/1989/jar.2/index.html). - Other winners have been prominent figures in the C community, including
[Walter Bright](https://en.wikipedia.org/wiki/Walter_Bright), creator of the D programming language and the Zortech C++ compiler, and[Fabrice Bellard](https://en.wikipedia.org/wiki/Fabrice_Bellard), creator of the Tiny C compiler.
There are also several noted CS academics, including [David Applegate](https://en.wikipedia.org/wiki/David_Applegate), [Lennart Augustsson](https://en.wikipedia.org/wiki/Lennart_Augustsson), [Daniel J. Bernstein](https://en.wikipedia.org/wiki/Daniel_J._Bernstein), [Vern Paxson](https://en.wikipedia.org/wiki/Vern_Paxson), [Diomidis Spinellis](https://en.wikipedia.org/wiki/Diomidis_Spinellis), and [John Tromp](https://en.wikipedia.org/wiki/John_Tromp).

And the guidelines even include a special rule directed specifically at [Peter Honeyman](http://www.citi.umich.edu/u/honey), a professor emeritus at the University of Michigan:

*“Some people, in the past, have attempted to obfuscate their identity by including comments of famous Internet personalities such as Peter Honeyman. The judges are on to this trick and therefore consider any obfuscated source or data file claiming to be from Honeyman to not be from Honeyman.”*
The message seems to be that gloriously obfuscated C code should also be *anonymous* obfuscated C code — at least until the judging is finished. And this led to a funny and remarkable coincidence for one [winning entry from 1990](http://www.ioccc.org/1990/scjones/index.html). The judges’ remarks grasped that the ANSI C standard now included three-character “trigraphs,” which “has made it easier to make programs hard to read.” So they created a special award for programmer [Larry Jones](https://www.linkedin.com/in/larry-jones-6894331/), recognizing him for crafting 46 undulating lines of C code [clogged with dozens of the three-character abominations](https://github.com/ioccc-src/winner/blob/master/1990/scjones/scjones.c) (mostly question marks).

After receiving his award for the “ANSI Committee’s worst abuse of C,” Jones contacted the judges with a simple question: “Were you aware that I *am* a member of the committee?”

The judges assured him it was a coincidence, and Jones added that he was “quite grateful” for the award. Although he “was really hoping for something more along the lines of ‘Closest Resemblance to Line Noise.'”

But mixed in with all the hilarity, the Obfuscated C competition still manages to become almost an accidental yearbook of[ each generation’s programmers](https://thenewstack.io/the-key-fundamentals-of-programming-you-should-know/), gathering them together in a display of our own collective history. Also contributing was [Mary Ann Horton](https://en.wikipedia.org/wiki/Mary_Ann_Horton), a BSD contributor described as “a Usenet and internet pioneer” and an early activist for transgender rights. “To have invented the email attachment is one thing,” Horton said in [a 2022 biography](https://www.amazon.com/Trailblazer-Lighting-Transgender-Equality-Corporate/dp/B0BCDF3D3Y/). “To have done so while transitioning from male to female and paving the way for Trans rights in the workplace is quite another.”

And somewhere in the mix is [George Sicherman](http://www.ioccc.org/1985/sicherman/index.html), whose claim to fame is creating an [alternate numbering scheme for dice](https://en.wikipedia.org/wiki/Sicherman_dice) in 1978, which still produces the same probability distribution as regular dice.

## Through the Ages
It’s all part of the event’s long and storied history. “We suggest that you avoid trying for the ‘smallest self-replicating’ source,” the guidelines warn — since someone has already won [with a 0-byte-sized entry](http://www.ioccc.org/1994/smr/index.html).

But other milestones are just as wacky and unpredictable:

- Programmer Thomas Covell had
[the code](https://www.ioccc.org/1984/anonymous/index.html)for the contest’s first winner[tattooed on his arm](https://web.archive.org/web/20070120220721/https://thomasscovell.com/tattoo.php). - Then there was the time Bill Gates asked contestants in a 1993 trivia competition for the name of the event for creating “the most unreadable, creative, bizarre but working C program.” And one of the contestants answered “Windows.” That year the competition added a commemorative
[Bill Gates Award](http://www.ioccc.org/1993/cmills/index.html). - Even the new site’s logo links to
[a 2011 IOCCC entry](https://www.ioccc.org/2011/zucker/index.html), a ray-tracing program whose default output was … the site’s logo. (It won 2011’s “most shiny” award.)
There’s a sense that anything can happen, maybe because the judges really *are* making things up as they go along. “When the number of submissions thins to about 25 submissions, we begin to form award categories,” explained [the official guidelines](http://www.ioccc.org/next/guidelines.html). So every year the names for the final awards “will vary depending on the types of submissions we receive.”

There’s been some C-specific award categories like “worst abuse of the C preprocessor” and “least likely to compile successfully.” A [2020 entry](http://www.ioccc.org/2020/tsoj/index.html) won an award for “most [misleading indentation](https://github.com/ioccc-src/winner/blob/master/2020/tsoj/prog.c)” for carefully justifying its code to the *right* margin.

But as the programs got crazier, so did the category names:

- One 2001 entry won the “best abuse of the user” award. (Its
[repository page warns](http://www.ioccc.org/2001/rosten/index.html)that the program “will mess with your mouse” and can also “make it hard to quit the program.”) - In 2006
[an entry](http://www.ioccc.org/2006/sloane/index.html)won the newly created “Homer’s favorite” award — for printing out an animated donut. - A
[2012 entry](http://www.ioccc.org/2012/dlowe/index.html)won the honor of being the “best way to lose a life” for creating an arcade-style video game based on Conway’s “Game of Life”. - In 2015 programmer Christopher Mills won the “For the Birds!” award for
[recreating the mobile game Flappy Bird](http://www.ioccc.org/2015/mills1/index.html)with customization options for changing physics in the bird’s universe.
## Looking Ahead
What keeps it all going? Where do the judges find the passion to keep poring through piles of obfuscated C code — and for four consecutive decades? What gives all of this craziness its purpose?

Search the web long enough and you’ll find a clue on Landon Curt Noll’s personal website. It includes some [very old photos](http://www.isthe.com/chongo/pictures.html) from his time as a cryptologist/number theorist at SGI — and an official picture from when Noll was a city council member for Sunnyvale, California.

But it also offers a glimpse at his unique appreciation for the art of algorithms. “I think of mathematics as both an art as well as a science,” Noll writes.

“Some people, when they doodle while talking on the phone, will draw ‘bunny rabbits.’ I like to doodle equations and plots, usually via the Mathematica tool.”

But the return of the contest is almost like a reunion of long-lost relatives — a kind of geek alternate history that continues on into the future.

And 2025’s new crop of winners will be announced in a uniquely geeky way — by a git push from the judges of a new winners’ directory with an announcement [on the new @IOCCC Fostodon feed](https://fosstodon.org/@ioccc).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)