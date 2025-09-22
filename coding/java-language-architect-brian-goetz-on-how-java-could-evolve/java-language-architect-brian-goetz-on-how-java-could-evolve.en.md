Java language architect [Brian Goetz](https://inside.java/u/BrianGoetz/) spoke at last month’s JVM Summit, delivering [a talk that looked to Java’s future](https://www.youtube.com/watch?v=Gz7Or9C0TpM).

Goetz discussed not the [Java we have now](https://thenewstack.io/introduction-to-java-programming-language/), but a hypothetical “set of features that are designed not to be used by themselves as a way to write better programs — but as a mechanism for making the language more growable and more extensible.”

In short, Goetz explained how he sees the Java language evolving.

“I spent a lot of time looking at what other languages did,” Goetz said, “and we feel like we’ve come to a point now where we have a pretty good idea of which way we want to go with this.”

On Reddit, Goetz described his talk as a “[statement of likely direction](https://www.reddit.com/r/java/comments/1mwaba5/growing_the_java_language_jvmls_by_brian_goetz/na320i0/).” There’s no official Java Enhancement Proposal, and “This is literally the first time we’ve talked about this in any detail. You have to start somewhere.”

But it was a fascinating chance to see not only how a programming language changes, but also the thoughtful philosophy that’s motivating those decisions.

## The Philosophy of a ‘Growable’ Language

Beginning his talk, Goetz had stressed that he wasn’t speaking about “features that we’re planning to deliver immediately.” Instead, he would look at “more *motivational* examples” for the long term. Goetz had titled his talk “Growing the Java Language” — and for a heartfelt reason. Goetz remembers a famous 1998 paper ([and talk](https://youtu.be/uXLtyhNUleg?si=o8oX2H2P8gjxVIbD)) by Sun Microsystems computer scientist [Guy Steele](https://en.wikipedia.org/wiki/Guy_L._Steele_Jr.) titled “Growing a Language.”

Goetz said Steele had made “a call to action for language designers to consider growability as an axis of design in programming languages.”

While many languages let users extend the “vocabulary” through user-created libraries, Steele noted that it’s harder if this new vocabulary doesn’t look the same as the language’s own essential “primitives.” Goetz said, “In many ways, this paper was kind of the starting gun for project Valhalla” — an OpenJDK project started in 2014 to incubate new Java language features, which is led by Goetz.

So Goetz wanted to describe not just a new Java feature, but also a language evolution philosophy that prioritizes extensibility when adding new [Java features](https://thenewstack.io/frontend-gets-smarter-ais-javascript-revolution/), and a mechanism for making it happen. “Some will say this goes too far,” says a bullet point on Goetz’s slide. “Some will say this doesn’t go far enough.”

“And that’s how we know we’re … right in the middle.”

## Introducing ‘Witnesses’: A New Concept for Java

So what’s the new idea? Java’s method-defining interfaces have been called “[blueprints of behavior](https://www.geeksforgeeks.org/java/interfaces-in-java/).” Goetz suggested that now “We want to do all the things interfaces do — take a set of named behaviors and group them into a named bundle, that you can claim that this type conforms to, or this group of types conforms to (and allows the compiler to type check that).”

So there’s a crucial difference. Java’s language design team wants it to be about types — and not instances of types.

“We want to move this behavior to a third-party *witness* object instead,” explains one slide.

What’s being proposed is a simple, straightforward keyword — a witness literal (along with the ability to “summon” a witness, Goetz says, “merely by uttering its type”).

So…

`public static final Comparator` COMPARATOR =

becomes…

`public static final witness Comparator COMPARATOR =`

Elaborating later, Goetz told his audience that “We can add type classes to Java by adding relatively little to the language — a mechanism for *publishing* witnesses, and a mechanism for *finding* witnesses — that we can piggyback on existing language constructs like interfaces, fields and methods.”

Why not just define interfaces with all the desired methods, and then let classes implement that interface? It turns out this isn’t always a useful place for abstraction, Goetz said, facing language designers with lots of tricky corner cases and “gotchas.”

Goetz’s next slide explained that this is “really using the wrong tool.”

“We need something that is similar but not exactly the same thing as interfaces.” Haskell has type *classes* (which “abstract over types, and not the behavior of types”), while C# and Kotlin are “both going through their own set of explorations of this.” The C# community proposed something similar called [shapes and extensions](https://github.com/dotnet/csharplang/discussions/164).

“All of these are sort of dancing around the same puzzle. Which is: how do I abstract over the behavior of types, without it being part of the definition of a type?”

## Opportunities for Growth: Potential New Java Features

Goetz says this idea went through many iterations, but “we’ve kind of distilled it down to something that fits into Java much more cleanly than some of our previous ideas.”

“It’s about growing the language,” says one slide. Goetz sees huge potential for “growability” — and presented several new potential features:

* **New numeric classes,** but “with the runtime behavior of primitives” — like 16-bit floating point numbers.
* **Math operators.** Using a standard plus sign for your Float16 variables “would be really nice,” rather than having separate methods, Goetz said. Other languages have attempted this so-called “operator overloading” — associating the symbol with multiple operations, depending on the type of variables involved. Goetz says that’s “somewhat of a linguistic minefield … a number of languages have hatched various flavors of disasters with operator overloading.”
* **Collection expressions** “for building a sequence-like structure,” similar to what’s available [in C#](https://developers.redhat.com/articles/2024/04/22/c-12-collection-expressions-and-primary-constructors#collection_expressions). “This is at the ‘why don’t you just’ level of specification. But it seems like a viable path to get there, in the way that the proposal back in the Java 7 days was not a viable path to get there.”
* **Creational expressions.** When creating an array today, the default value for its elements is always “null” or zero. What if there were a witness that could indicate when there is (and isn’t) a valid “blank” value? In Project Valhalla, Goetz says, adding validity checking when initializing an array “is a feature that we’ve been kind of diffident about,” because they didn’t want to add it into Java’s virtual machine (VM). But “This is a way to keep that feature in the language, but allow a given class to participate in the feature based on whether they’ve done some extra work or not. So it means that we get to put this behavior in the right place, which is a good feeling.”

A multipurpose language addition isn’t without precedent. Goetz presented two earlier “notable examples of language features designed to be extensible by libraries” — the *foreach* loop and *try*. Developers could use the *foreach* feature just by implementing the *Iterable* class. (Goetz says the JDK’s developers then “went and retrofitted a bunch of classes to implement iterable” — as did other Java developers.) But most importantly, it just “looked like it was built-in.”

Goetz was glad [Java](https://thenewstack.io/azul-cto-java-at-30-still-rules-enterprise-dev/) didn’t just restrict the feature to just a handful of obvious use cases (like *list*, *map* and *set*). “I’m really glad that somebody stood up and said, ‘No, no, it’s really important for classes other than these few magic classes to be able to participate in it.'”

Goetz said he wanted to continue that tradition.

## The Future Roadmap for Java’s Evolution

In concluding his talk, Goetz said it demonstrated not only the idea of witnesses, but sketched out “how we would use it for four potential features that have been irking us for quite a while.”

Looking ahead, Goetz believes witnesses “enable you to design better features, richer features, features that users can do more with, and ultimately maybe we won’t have to design as many language features in the future as a result. … Hopefully in the long run, we’ll be able to use this build richer generic libraries and conditional behavior and those things as well.

“But in the short term, we can use this to deliver growable language features, including features people have been asking for for quite a while.”

One Reddit commenter even [joked later](https://www.reddit.com/r/java/comments/1mwaba5/comment/n9wg1ke/) that Goetz’s talk reminded them of “Dungeons and Dragons” spells. “There was definitely a point where I felt like Brian was about to cast magic missile.”

[![Brian Goetz, Java language architect - Reddit comment about 2025 JVM summit talk on witnesses](https://cdn.thenewstack.io/media/2025/09/9cbca623-brian-goetz-java-language-architect-reddit-comment-about-2025-jvm-summit-talk-on-witnesses.png)](https://cdn.thenewstack.io/media/2025/09/9cbca623-brian-goetz-java-language-architect-reddit-comment-about-2025-jvm-summit-talk-on-witnesses.png)

The Reddit commenter added later that “It was a good an interesting talk. I hope these features land.” But one of Goetz’s final slides explained clearly where we stand. “The examples in the previous slides are not designs, they are ideas.”

[![Brian Goetz, Java language architect - Reddit comment about complexity and 2025 JVM summit talk on witnesses](https://cdn.thenewstack.io/media/2025/09/7fd2db3f-brian-goetz-java-language-architect-reddit-comment-about-complexity-and-2025-jvm-summit-talk-on-witnesses.png)](https://cdn.thenewstack.io/media/2025/09/7fd2db3f-brian-goetz-java-language-architect-reddit-comment-about-complexity-and-2025-jvm-summit-talk-on-witnesses.png)

Still, in [another Reddit comment](https://www.reddit.com/r/java/comments/1mwaba5/comment/na311aa/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button), Goetz said Java’s design team now has a story they’re “comfortable” with, “so we were ready to share it. But note, it is still a *story*, and there’s a lot of other Valhalla stuff that has to happen first.”

And Goetz had drawn a warm round of applause after his presentation — and then opened up his talk to questions from the audience. And the first questioner acknowledged that they already saw a lot of value in the idea, calling Goetz’s talk “a really big proposal packaged in a fairly small syntactic change.”

Goetz’s response? “Shh, don’t tell them!”

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)
[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/82081813-7zddypfe_400x400.jpg)

David Cassel is a proud resident of the San Francisco Bay Area, where he's been covering technology news for more than two decades. Over the years his articles have appeared everywhere from CNN, MSNBC, and the Wall Street Journal Interactive...

Read more from David Cassel](https://thenewstack.io/author/destiny/)