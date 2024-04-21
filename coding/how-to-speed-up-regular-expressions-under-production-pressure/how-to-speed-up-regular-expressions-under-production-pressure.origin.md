# How to Speed up Regular Expressions under Production Pressure
![Featued image for: How to Speed up Regular Expressions under Production Pressure](https://cdn.thenewstack.io/media/2024/04/33320028-getty-images-g6d6uvrvmmq-unsplash-1024x683.jpg)
I feel a bit guilty about pointing out the advantages of using
[regular expressions](https://thenewstack.io/taming-text-search-with-the-power-of-regular-expressions/) in [several](https://thenewstack.io/regular-expressions-and-solving-the-food-taster-dilemma/) [posts](https://thenewstack.io/magic-regexp-a-javascript-package-for-regular-expressions/), without ever mentioning how slow they can be.
In many application cases, regex speed is not an issue. It is just catching a few problems with a form. But when speed is important, you are suddenly cast into the role of a detective looking for a time murderer. This can force you to discover what bits of code are inefficient, but having to speed things up under production pressure is a high-wire act.
I’ll use C# examples, but the bottom line is that you generally have to take care of how you use a regex in any language you use, and options like compiling the regex may help.
As I’m comparing execution speeds, I will have to use some type of benchmark tool to make valid comparisons. Fortunately,
[BenchmarkDotNet](https://benchmarkdotnet.org/articles/overview.html) exists. It works for console apps, which is all we need.
I’ll continue using Visual Studio Code as it is better for creating and showing projects without needing a Solution. To speed things up, I’ll use a template.
Opening up
[Warp](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/), I first run these steps:
This just sets us up a project called
*BenchmarkRegex* using the available **benchmark template** to set up a suitable project skeleton. We can see the generated files sitting in the directory:
We can then fire up VS Code with
> code . and start the IDE straight in the project workspace.
But first, let’s consider some of the regex tasks I ran in previous posts. We used a
[tricky little pattern](https://thenewstack.io/regular-expressions-and-solving-the-food-taster-dilemma/) using alternation and **lookaround** to prove how the *“i before e except after c”* is regularly broken in English:
The above pattern finds breaking examples by looking for “cie” or “ei” without the “c”. Note that lookaround is one of those functions within Regex that might behave differently in different implementations, and should be used sparingly. In this case, we use a negative lookbehind
(?<!c) to confirm that the “ei” is not preceded by a “c”, but without consuming that “c”. Read the post for more details.
We can slot this example text and pattern straight into our fresh template file,
*Benchmark.cs*:
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
|
using System;
using System.Text.RegularExpressions;
using BenchmarkDotNet;
using BenchmarkDotNet.Attributes;
namespace BenchmarkRegex
{
public class Benchmarks
{
private const string Pattern = @"(cie|(?<!c)ei)";
private const string GoodText = "Good: ceiling, receipt, deceive, chief, field, believe.";
private const string BadText = "Bad: species, science, sufficient, seize, vein, weird.";
static bool printMeOnce = false;
[Benchmark]
public void Scenario1()
{
// Implement your benchmark here var
f = Regex.IsMatch(GoodText + BadText, Pattern);
if (!printMeOnce) foreach (Match match in Regex.Matches(GoodText+BadText, Pattern, RegexOptions.None))
Console.WriteLine("Found '{0}' at position {1}", match.Value, match.Index);
printMeOnce = true;
}
}
}
First, we check that the match works and that it catches the six cases.
We can only do Benchmarking on console apps in release mode, which is fine, so we can run
> dotnet run -C Release in the Warp command line. Shortly in the log, we get our confirmation that the six cases were caught:
At the end, we get the benchmark:
Ok, that’s great. Of course, we now need to get back to our topic, which is speeding up regex. So the first and fairly obvious method is just making the pattern
**static**. Now that we’ve confirmed the pattern works, we can dispense with the printout, which after all made the benchmark very slow!
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
|
..
private const string Pattern = @"(cie|(?<!c)ei)";
private static readonly string StaticPattern = @"(cie|(?<!c)ei)";
..
[Benchmark] public void Scenario1()
{
// Implement your benchmark here
Regex.Matches(GoodText+BadText, Pattern, RegexOptions.None);
}
[Benchmark] public void Scenario2()
{
// Implement your benchmark here
Regex.Matches(GoodText+BadText, StaticPattern, RegexOptions.None);
}
..
So we would roughly expect the second scenario to be a bit quicker. And it is:
(Yes, without the printing we are in the nanosecond range.)
Now that we have tested the benchmarking, we can test the compiled option:
|
1
2
3
4
5
6
7
8
9
|
private const string Pattern = @"(cie|(?<!c)ei)";
private static readonly string StaticPattern = @"(cie|(?<!c)ei)";
private static readonly Regex CompiledRegex = new(Pattern, RegexOptions.Compiled);
..
[Benchmark] public void Scenario3()
{
CompiledRegex.Matches(GoodText+BadText);
}
..
So how does this benchmark?
Well, that’s about half. But this is no open-and-shut conclusion. There are a number of things going on in and around this that you need to be aware of.
When you first started using C#, you probably remember learning that it was converted into an
**intermediate language** (IL or MSIL) and that was later compiled into your operating system’s native format via **just-in-time** (JIT) compilation. (At the time that C# was released way back in 2000, this seemed a little irrelevant as Microsoft was so tightly bound to Windows.)
Regex, however, produces its own nodes,
**parse trees** and operations that are then turned into IL. Remember, regex is much older tech than .NET — by about half a century. This is partly why there are special rules around dealing with it.
Without the Compile flag, an instantiated regex object is interpreted to a set of internal operations as described above. When a method on the object is called (like
*Match*), only then are these operation codes turned into IL so that the JIT compiler can execute them. This is fine if there are few regex calls made. If the regex definition is **static**, then the operation codes get **cached**. By default, the last 15 most recently used get cached. If you really are using a lot of patterns, you can alter this with the **Regex.CacheSize** property.
If the Compile flag is used, pre-compiled regular expressions increase startup time but execute individual pattern-matching methods faster. That’s good if you are repeatedly using certain patterns.
You can create a regex object and pattern, compile it, and save it to a
**standalone assembly**. You can call the **Regex.CompileToAssembly** method to compile and save it. But this makes sense to consider at design time, as you chop your application up into separate assemblies.
In summary, the sensible realization to come to is that regex should not be used in and around time-critical areas at all. If you run very few expressions, these are best done in the usual interpreted fashion. If you run the same patterns a lot, use the Compile flag or put them in a separate assembly. Ultimately, if you can isolate the regex methods and use benchmarks to check comparisons, you can catch the time murderer in the act.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)