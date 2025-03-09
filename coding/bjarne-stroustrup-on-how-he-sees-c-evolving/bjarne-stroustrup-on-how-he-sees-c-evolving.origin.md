# Bjarne Stroustrup on How He Sees C++ Evolving
![Featued image for: Bjarne Stroustrup on How He Sees C++ Evolving](https://cdn.thenewstack.io/media/2025/03/27c57b7a-colorized-bjarne_stroustrup_2013-by-victor-zavyalov-icpcnews-creative-commons-via-wikipedia-copy-1024x683.jpg)
“I wanted to educate the community at large, and members of WG21 in particular — on my views of C++’s intended direction of evolution,” [Bjarne Stroustrup](https://stroustrup.com/) told TNS.

The 74-year-old creator of C++ has spent 40 years of his life watching the growth of the language he designed back in 1985.

To encourage some long-desired features, last month in *Communications of the ACM* Stroustrup published “[21st Century C++](https://cacm.acm.org/blogcacm/21st-century-c/)“, a 6,300-word article promising to show “key concepts” for modern, type-safe “21st-century C++” to create “C++ on steroids”. For example, in the article Stroustrup highlighted long-standing experiments in approaches like writing safer code with [guideline-enforcing profiles](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3081r1.pdf). To maintain compatibility with decades of already-written C++ code, “We can’t change the language,” Stroustrup writes. “But we can change the way it is used…”

Yet that evolution isn’t entirely up to him. In [a section towards the end,](https://cacm.acm.org/blogcacm/21st-century-c/#future) Stroustrup acknowledges [WG21, the standardization working group](https://isocpp.org/std/the-committee), and how it will inevitably play a role in how much the language can change. “I am reluctant to make predictions about the future,” Stroustrup wrote, “partly because that’s inherently hazardous, and in particular because the definition of C++ is controlled by a huge ISO standards committee operating on consensus.”

“Last I checked, the membership list had 527 entries. That indicates enthusiasm, wide interest, and provides broad expertise, but it is not ideal for programming language design and ISO rules cannot be dramatically modified.”

Still, when it comes to that crucial audience, “Some are ahistorical and thus miss key points,” Stroustrup told TNS, “such as that guidelines and profiles fit into the long-term direction of C++.” So he’s taking steps to educate them, and “To do so, I have to show where key features fit.”

His detailed article was a good place to start — but it’s also just part of a multi-pronged push. And in the end, it could all change the trajectory of the [entire C++ ecosystem](https://thenewstack.io/introduction-to-c-programming-language/), while also bringing programmers that performant, type safe, and flexible language they’ve long been craving.

And doing all this while fulfilling Stroustrup’s own long-held goals from the 1980s…

## A Call To Urgent Action
Stroustrup has also communicated with the WG21 directly. [The Register noted](https://www.theregister.com/2025/03/02/c_creator_calls_for_action/) that “industry and government cybersecurity experts over the past three or four years have been discouraging the use of C and C++ while evangelizing languages with better memory safety.” So three days after publishing his article, Stroustrup had left an official note to the C++ Standards Committee which he described as “a call to urgent action partly in response to unprecedented, serious attacks on C++.

“I think WG21 needs to do something significant and be seen to do it. Profiles is a framework that can do that.”

Stroustrup’s vision is clear. “Guidelines are fine and useful, but it is essentially impossible to follow them consistently in a large code base,” he wrote in his article. What’s needed is some enforcement mechanism that will actually flag and prevent things like dangling pointers, range errors, and nullptr dereferencing.

And fortunately, just such an enforcement mechanism is already available in the form of those [guideline-enforcing profiles](https://cacm.acm.org/blogcacm/21st-century-c/#guide). A footnote provides the example of their use in Visual Studio 2019, which [implemented an early version of the “Lifetime” profile](https://habr.com/en/companies/microsoft/articles/437660/) which checks C++ for dangling pointers and references and other common errors in the lifetime of an object…

Basically, each profile verifies that the requirements are being met to achieve a specific outcome, usually at compile time. Besides the “Lifetime” checking profile, there are also plans for more, including a “Bounds” profile that ensures all the code accessing arrays include range-checking safety checks.

In our email interview, Stroustrup noted that C++ already supports better protection against range errors through its new [span](https://www.geeksforgeeks.org/cpp-20-std-span/) class template, introduced in 2020. The Bounds Profile simply confirms that those bounds-safety-ensuring functions are actually in place.

“Much of this is standard and available for use today,” Stroustrup told me. There are also plans for several other profiles to help code avoid type or arithmetic errors. Stroustrup believes that “In the near future [Profiles](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3589r0.pdf) will provide a framework for enforcement of a variety of constraints.”

Hopefully this could provide C++ [with the safety guarantees](https://thenewstack.io/secure-coding-in-c-avoid-buffer-overflows-and-memory-leaks/) people are looking for. But it’s also a natural progression in Stroustrup’s original, 40-year-old vision for C++.

## ‘A Much Better Approximation’
Features like type safety have always been among Stroustrup’s [safety and performance goals](https://thenewstack.io/bjarne-stroustrups-plan-for-bringing-safety-to-c/) for C++.

“This has not changed since the earliest days,” he writes in his article, with a footnote referring readers to his 1994 book, [ Design and Evolution of C++](https://www.stroustrup.com/dne.html). But contemporary C++ can achieve these long-standing goals much better than earlier versions of C++, partly because the language “was designed to evolve,” Stroustrup writes at the end of his article. So after decades of improvement, he calls “contemporary C++” like C++ 23 (the version released in October) “a much better approximation” of his original ideals.

He also stressed this point in his note urging the WG21 to adopt Profiles: “As I have said before, this is also an opportunity because type safety and resource safety (including memory safety) have been key aims of C++ from the very start.”

“I feel strongly about this. Please don’t be fooled by my relatively calm language.”

One problem with an evolving language is “Many people got stuck with an outdated view of what C++ is,” according to Stroustrup’s article. “Today, we still see endless mentions of the mythical language C/C++, usually implying a view of C++ as a minor extension of C embodying all the worst aspects of C together with grotesque misuses of complex C++ features…” But C++ is continuing to grow, Stroustrup emphasizes, with “work in progress” and experimental features already available for improvements like a [general model for asynchronous computing](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3109r0.html) and [SIMD](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p1928r9.pdf).

“One serious concern is how to integrate diverse ideas into a coherent whole,” Stroustrup wrote. Unlike most software projects — and even most CS work in academia — designing a language requires “decisions in a space where not all relevant factors can be known, and where accepted results cannot be significantly changed for decades.”

In short, it’s a hard problem — and that remains a known issue. “The fact that almost all language design efforts over the decades have failed demonstrates the seriousness of this problem.”

But that doesn’t mean C++ has simply stopped trying to evolve…

## Dramatic Improvements
Profiles aren’t the only way 21st Century C++ has improved. “I’ll also point to [modules](https://en.cppreference.com/w/cpp/language/modules) as a mechanism for cleaner code and vastly improved compile times,” Stroustrup said in our email interview.

Stroustrup’s article cites “a 7-to-10 times advantage” in speed when importing compiled modules rather than using old-fashioned *#include* statements.

“Most people could dramatically improve their code today by using what is offered by C++23,” he tells me. And looking to the future, Stroustrup predicts even more performance-enhancing features ahead. “In C++26, we will likely see improved concurrency support, static reflection, and contracts as well as many minor improvements and standard-library components.”

That forward-looking hope may explain why Stroustrup wanted to ground his call for Profiles in the larger history of C++. Stroustrup told me his article “presents the direction of C++ evolution. Safety guarantees are coming, and it isn’t a novel idea in the context of C++ but a part of the long-term aims. Complete type safety and resource safety were among C++’s initial aims, but moving the huge range of application areas forward takes time and must be done incrementally.”

He’s aware that the codebase already installed is widespread and that C++ “covers a huge range of application areas today. The safety guarantees must and will address those areas where C++ is already used to deliver high-quality applications.

“People focusing on memory safety should note that C++ isn’t C and that solutions based on safer programming styles and hardened libraries are already widely deployed in C++.”

I asked if there’s signs that his *ACM* article had made an impact — though that’s obviously hard to quantify. “I am reluctant to make predictions about the future,” Stroustrup says, “but we already see better support for generic programming in the form of [concepts](https://en.cppreference.com/w/cpp/language/constraints).”

And if you’re looking for impactful improvements, Stroustrup notes you can also look beyond the language itself. A wide range of tools are currently available for C++ developers.

“A language is not just what you find in a language specification or formal standard.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)