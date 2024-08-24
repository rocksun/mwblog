# Devs: Don’t Just Read About Design Patterns, Implement Them
![Featued image for: Devs: Don’t Just Read About Design Patterns, Implement Them](https://cdn.thenewstack.io/media/2024/08/8e6b8f9d-fabrizio-conti-b5rpuibfeme-unsplash-1024x683.jpg)
While [design patterns](https://en.wikipedia.org/wiki/Software_design_pattern) have helped to document software as an engineering discipline, they don’t really help much as a teaching aid. It is useful to confirm the existence of [repeatable patterns](https://thenewstack.io/serverless/serverless-architecture-five-design-patterns/) after you encounter them, but understanding examples is still the best way to prepare to solve new problems.

This post might appear to look at the strategy pattern (or command pattern), but actually it describes hero animals on a mission to find an evil lair.

What counts in extendable software design is what can be altered or added to without breaking a system. You’ll have heard that word “[decoupled](https://thenewstack.io/how-decoupling-can-help-you-write-better-software/)” a lot to describe systems that have this tension. Conversely, some aspects will not be alterable — or will require many touches to update.

In this highly contrived but light-hearted example, we have a flexible roster of hero animals, each of whose attributes go to deciding which are required for a mission. Think of it more as a relay race. I could have used Marvel heroes, but I believe Disney employs a lot of lawyers. I’ve used C#, but any object orientated language can easily support this.

What counts in extendable software design is what can be altered or added to without breaking a system.

A mission involves traveling through a location that has two biomes (a fancy word for an area with a specific climate) and a lair. For example, a forest island castle. Each hero animal is familiar with one home biome and has some natural skills. Given that each animal has only one home biome, a mission team may need two or three heroes.

What matters here is that the system uses any animal heroes you define to complete a mission, and also understands that there could be insufficient available heroes.

So the design decouples missions from the roster of heroes. However, it requires the definition of animal skills to remain the same, as this is the shared understanding.

We start with the list of hero animals, or roster. This is also technically a register.

12 |
public static List<HeroAnimal> roster = new() { new Penguin(), new Shark(), new Goat(), new Gorilla()}; |
So you can see the roster has four hero animals, i.e. classes that must be defined elsewhere.
To specify a contract we would usually define an interface, but I’ve used [inheritance](https://thenewstack.io/how-to-use-inheritance-in-python/). Our contract is the abstract definition of our hero, which defines the skills and a home biome.

1234567 |
public abstract class HeroAnimal { public abstract bool canFly(); public abstract bool canSwim(); public abstract bool canClimb(); public abstract bool canCrawl(); public Biome Home { get; protected set;}} |
So each hero animal has possible skills that will help it break into an evil lair. A Lair is defined with an interface:
123 |
public interface Lair { bool CanHeroBreakIn(HeroAnimal hero); } |
And a Lair is just a place — like a castle — and we need to know which skills are needed to break in:
12345 |
public struct Castle : Lair { public bool CanHeroBreakIn(HeroAnimal hero) { return hero.canFly() || hero.canClimb(); } } |
So a castle can be broken into from the air by a flying hero, or by climbing the walls.
Animals live in a specific Biome:

123 |
public enum Biome { Forest, Ice, Plains, Swamp, Sea } |
We have some general classes we can use as templates, to define our hero animals, for example:
12345678 |
public abstract class Fish : HeroAnimal { public override bool canFly() => false; public override bool canSwim() => true; public override bool canClimb() => false; public override bool canCrawl() => false; public Fish() { Home = Biome.Sea; } } |
And finally, a concrete example that we can instantiate:
1 |
public class Shark : Fish { } |
A hero penguin is a bird, but not a usual one:
1234567 |
public class Penguin : Bird { public override bool canFly() => false; public override bool canSwim() => true; public Penguin() { Home = Biome.Ice; } } |
Once the mission is set, the system selects the team needed. This is just a simple list search and match. The system could be improved by mixing the list up before each run.
I’ve used the [C# online compiler at Programiz](https://www.programiz.com/online-compiler/6gfMhWkH9umce) to put all the code in one file, so you can run the code from there, or mess about with it. You can define and register new animal heroes, lairs or missions. You can also add biomes, but removing them might break existing heroes.

In fact, you have enough information to write the code yourself.

Here is the result of one run online:

1234567891011121314 |
Our Hero Animal roster:Penguin!Shark!Goat!Gorilla!Mission: Find Dr Evil's Forest Island CastleOur Hero team for mission:Shark through SeaGorilla through ForestGoat breaks into Castle lair=== Code Execution Successful === |
What we understand from this is that the hero animals can be defined without knowing anything about the mission. And conversely, the mission makes no reference to the available heroes. We can add or take hero animals to or from the roster freely.
What we need is simply a list of class instances that can be interrogated when required. This implies that the classes should have a similar interface, so they can respond to the same questions.

Obviously, more practical examples should come to mind, like making valid system configurations, where the list of available [components](https://thenewstack.io/the-risks-of-decomposing-software-components/) can grow or shrink. Or scheduling events and matching them to available and appropriate venues.

So while we should always respect what was said by the Gang of Four (the authors of the [classic book](https://en.wikipedia.org/wiki/Design_Patterns)) concerning software design, it is best to do so after working on solutions yourself.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)