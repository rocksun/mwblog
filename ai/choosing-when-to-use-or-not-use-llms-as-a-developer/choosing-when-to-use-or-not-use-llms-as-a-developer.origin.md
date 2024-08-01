# Choosing When To Use (or Not Use) LLMs as a Developer
![Featued image for: Choosing When To Use (or Not Use) LLMs as a Developer](https://cdn.thenewstack.io/media/2024/07/e210ce01-sebastian-herrmann-jb4ar34u248-unsplash-1024x683.jpg)
“My daughter will never know what it’s like to be lost.” I forget who said that about 10 years ago, but the message sank in and resonates more deeply as we are ever more profoundly augmented by tech. The speaker was referring, of course, to the fact that almost nobody younger than 15 (now 25) is ever without the handheld GPS wayfinding device that we anachronistically call a phone.

Of course, zooming and panning the small screen of a mobile device is a terrible way to visualize paths through a city or landscape. Our brains are built to absorb patterns from much larger visual fields. A small screen can’t compete with a real map that you can unfold and scan in a holistic way. Nor does following turn-by-turn directions help you build the mental map of a region that enables you to visualize relationships among arbitrary locations. That’s why, if the stakes for getting lost are low — or when getting lost is actually [the goal](http://rebeccasolnit.net/book/a-field-guide-to-getting-lost/)! — I like to leave the phone in my pocket and practice dead reckoning.

LLMs offer a level of augmentation that I wasn’t sure I’d live to see. They also bring an array of perils.

In a similar vein, I’ve long been annoyed by the snarky “[Let me google that for you](https://letmegooglethat.com)” (now, of course, also “Let me GPT that for you”) response to a question. There’s a kind of shaming going on here. We are augmented with superpowers, people imply, so you’re an idiot to not use them.

Well sure, we can always look things up. But going there directly is a conversation killer. Can’t we pause, put our heads together and consider what inboard knowledge we may hold individually, or can collectively synthesize, before consulting the outboard brains?

Here’s my favorite tale about the power of the unaugmented mind. In “[Behind the Dream](https://search.worldcat.org/title/behind-the-dream-the-making-of-the-speech-that-transformed-a-nation/oclc/631748997),” Clarence Jones (Martin Luther King’s lawyer and adviser) reveals that the “Letter from Birmingham Jail” was written without access to books.

“What amazed me was that there was absolutely no reference material for Martin to draw upon. There he was pulling quote after quote from thin air. The Bible, yes, as might be expected from a Baptist minister, but also British prime minister William Gladstone, Mahatma Gandhi, William Shakespeare, and St. Augustine.”

He adds:

“Martin could remember exact phrases from several of his unrelated speeches and discover a new way of linking them together as if they were all parts of a singular ever-evolving speech. And he could do it on the fly.”

MLK’s power flowed in part from his ability to reconfigure a well-stocked working memory and scan it like a big map. He’d arguably have been far less effective if he had to consult outboard sources serially in small context windows.

Fast-forward to now. LLMs offer [a level of augmentation](https://thenewstack.io/elevating-the-conversation-with-llm-assistants/) that I wasn’t sure I’d live to see. They also bring an array of perils, many of which are ably documented in Baldur Bjarnason’s fiercely critical “[The Intelligence Illusion](https://illusion.baldurbjarnason.com/),” including the one I’m addressing here:

“We’re using the AI tools for cognitive assistance. This means that we are specifically using them to think less.”

Full disclosure: Baldur and I speak often, though not much about AI because we are far apart on the kinds of benefits that I claim to regularly experience and have been documenting in this column. But on this key point we agree. And, *mea culpa*, I have sometimes found myself getting lazy about exercising the muscle between my ears. So, when not to LLM?

## When You Don’t Want To Think
I’ve written a lot of code over the years, but I am first and foremost a writer of prose. I’m also a spectacularly good copy editor because I rarely fail to spot misspellings and errors of punctuation and grammar. This can be an annoying superpower because even a few such unignorable errors interrupt my flow when reading for business or pleasure. It means, though, that spellchecking is one form of augmentation I’ve never come to rely on.

My brain isn’t a fuzzy parser — I’m just not wired to see that kind of problem.

LLMs make pretty good proofreaders, because they grok higher-order patterns. But I don’t rely on them for that purpose either. I want to keep exercising my proofing and copy-editing muscles. And rereading prose for which I’m responsible — mine or that of a colleague — is just intrinsically valuable. There are always ways to improve a piece of writing.

I’m wired differently when it comes to reading code. A bug caused by inconsistent spelling of a variable doesn’t jump out at me in the same way that misspellings in prose do. Neither does a logical error. I’ve noticed that many of my more code-oriented colleagues catch misspellings, and structural problems, more readily in code than they do in prose. Because reading code doesn’t come as easily to me as to others, I’ve tended to lean on LLMs for help. Now I’m reevaluating.

For certain things, the LLM is a clear win. If I’m looking at an invalid blob of JSON that won’t even parse, there’s no reason to avoid augmentation. My brain isn’t a fuzzy parser — I’m just not wired to see that kind of problem, and that isn’t likely to change with effort and practice. But if there are structural problems with code, I need to think about them before [reaching for assistance](https://thenewstack.io/learning-while-coding-how-llms-teach-you-implicitly/). That’s a skill that can improve with effort and practice.

## When You Don’t Want To Be Social
LLM-backed developer tools can serve as proxies for coworkers when you shouldn’t interrupt them.

We all know that knowledge workers, and especially software developers, need to achieve mental flow supported by rich context that’s hard to assemble and tragically vulnerable to interruption. Because LLM-backed developer tools like [Cody](https://sourcegraph.com/pcody) and [Unblocked](getunblocked.com) mine local knowledge — your code, your documentation — they can serve as proxies for coworkers, and thus shields that protect them from interruption. Even if you haven’t tried these specialized tools, you’ve likely achieved the same effect relative to the world knowledge marshaled by ChatGPT and Claude. It’s a real and important benefit.

But let’s not go overboard. Programmers are stereotypically not the most social people. When LLMs help us avoid unnecessarily interrupting others’ flow? Great. When they provide one more reason not to talk to people we should be talking to? Not great.

## When You Need To Be Creative
Baldur nails the paradox:

“The most productive way to use generative AI is to not use it as generative AI.”

Instead, he argues we should use it “primarily for derivation, conversion, and modification.” Here too we agree. The uses I’ve described in this column — to which I ascribe more value than does Baldur — belong in that category.

The hybrid solution I arrived at in my last column, [Human Insight + LLM Grunt Work = Creative Publishing Solution](https://thenewstack.io/human-insight-llm-grunt-work-creative-publishing-solution/), was, on the other hand, if not completely novel, then at least rare enough to not appear in the literature absorbed (at that time) by the language models. I claim it was the kind of creative act that transcends derivation, conversion, and modification.

For me, LLMs are software components.

It’s true that my use of LLMs to help implement the idea was, arguably, another form of creativity. For me, LLMs are software components, and my strongest superpower in the technical realm has always been finding novel ways to use and remix such components. Learning to work effectively with this new breed of insanely powerful pattern recognizers and transformers affords plenty of scope for that kind of innovation.

But the idea itself didn’t, and wouldn’t, come directly from my team of assistants. They played a supporting role, by accelerating my exploration of conversion strategies that ultimately proved to be dead ends. When the idea came to me, though, it did not appear on a screen in a conversation with Claude or ChatGPT: It appeared in my head while hiking up a mountain.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)