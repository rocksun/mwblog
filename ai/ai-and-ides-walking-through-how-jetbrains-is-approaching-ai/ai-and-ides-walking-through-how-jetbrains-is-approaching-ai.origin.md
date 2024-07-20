# AI and IDEs: Walking Through How JetBrains Is Approaching AI
![Featued image for: AI and IDEs: Walking Through How JetBrains Is Approaching AI](https://cdn.thenewstack.io/media/2024/07/7e18e438-getty-images-0oviynbjwes-unsplash-1024x683.jpg)
Colleagues using Java have always rated [IntelliJ](https://www.jetbrains.com/idea/), and more recently Rider for C#. So when I was given the opportunity to try [JetBrains AI](https://www.jetbrains.com/ai/), which is an AI service that refers to itself as “AI Assistant,”** **I was intrigued. Apparently “It is powered by OpenAI and Google as the primary third-party providers”. I’m not sure trying to match different LLM abilities to certain tasks is a good idea when they are changing so regularly, but not depending on one vendor does make sense.

Now when it comes to using LLMs, professional developers all have slightly varying needs — none of which is “write my code for me.” But the two modes that stand out are code completion and “explain this code,” which is useful for consultants facing an unfamiliar codebase. [Generating unit tests](https://thenewstack.io/make-your-dev-life-easier-by-generating-tests-with-codiumai/) is also potentially a fit, even though not taking responsibility for your own unit tests breaks the Agile canon somewhat. I don’t personally rate having examples within the IDE when I could just browse for them — but I know some people do. For instance, most developers have discovered that *Time* and *Date* functions can become quite unintuitive; sometimes complex systems can’t be made simpler. Examples of these are very useful.

While this post is a review of the AI Assistant, this will be the first time I’ve had a JetBrains IDE on my Mac, so I have to go through the administration for the first time. I have a “license key” for their AI service, which I will try to graft onto the community edition or equivalent. Whereas ReSharper seems to sit on Visual Studio, Rider is a separate IDE — so I chose that, in order to look at C#. I was hoping the AI service would attach to it; this wasn’t made entirely clear.

I ended up installing a trial version of Rider. Full marks for starting off by importing settings.

In the next section, my question is answered immediately. Hurrah.

This gives me a great deal more trust that customer paths have been considered. It might seem obvious to do this at the start, but I’ve seen enough products that don’t give their own services enough attention. JetBrains emailed me back to get an account once I registered, and I was given a free license for the purposes of testing.

It should be noted that LLM services are very much treated as an add-on, which makes “AI” feel like an add-on. I don’t think this is the fault of the IDE makers at the moment — eventually, this type of offering will exist a bit further back in the OS stack. Right now, we have to wait for the big companies to battle over LLM dominance, which pushes individual users into an explicit consumer position.

## Code Explanations
I’ve opened some code from a game project, and we’ll ask for an explanation:

12345678910111213 |
...static private List<Archetype> archetypes = new List<Archetype>(); ... public static List<Archetype> FetchArchetypes() { if (!archetypes.Any()) { ArchetypeTemplates tt = BackEnd.DataLoader<ArchetypeTemplates>.LoadGameData("Archetypes.json"); foreach (ArchetypeTemplate t in tt.Archetypes) { archetypes.Add(new Archetype(t)); } } return archetypes; } |
An `Archetype`
is just an arbitrary structure from the game. Initially, I read this in as an array from a JSON file, and recreated the structure locally in the list. If the list has already been created, I just pass the list.
So what does the AI think this is doing? It returns a very comprehensive answer, with these two highlights:

*“At the end, the method returns the Archetypes List which contains Archetype instances created based on the templates from the JSON file. The Archetype class seems to represent a specific archetype in a game and this method is used to populate the list of all archetypes based on the data in the JSON file.”**”In this particular method, it’s worth noting that data loading and object instantiation are only performed when the Archetypes List is empty. This means once the Archetypes have been fetched once, subsequent calls to this method will return the same List without any additional processing. This is a common pattern for instances where loading or object creation is a taxing process and the resulting data doesn’t change over the lifecycle of the application.”*
So there are several good things here. It has worked out that the Archetype in question is probably for a game. That’s important — understanding the intention as well as the utility is important when quickly trying to grok code. It has recognized that I’ve used late instantiation, why I’ve used that, and that it is a bonafide **pattern. **It also understands that reading the JSON file is done elsewhere, but we depend on the input.

I then asked for **suggested refactoring,** also directly from the context menu:

It suggested separating the loading action into a separate method, to simplify the code. I think almost every developer would agree to that improvement. It could have also have complained about the lack of error detection.

If you want a simple contrast, doing [coding creation with JSON persistence using Meta’s Llama 3](https://thenewstack.io/coding-test-for-llama-3-implementing-json-persistence/) wasn’t entirely successful. Mind you, three months is an age in LLM progress.

## Code Completion
Let’s try some code completion. I’ll try a similar example to that which I tried for [Copilot using the C# FlagsAtribute.](https://thenewstack.io/the-changing-role-of-human-developers-in-an-ai-and-llm-world/) From that post: “The FlagsAttribute in C# is used when you want to efficiently store a flag set — that is, a set of boolean values manipulated with bitwise arithmetic.”

Here is a simple example:

123456789 |
[Flags] public enum Pets { None = 0, Dog = 1, Cat = 2, Bird = 4, Rabbit = 8, Other = 16 } |
As long as the flag values go up in binary powers, you can build up a binary flag set. Check that article for a bit more explanation.
I deleted my actual code and asked the assistant to regenerate it with just the signature. I got the purple squiggle and it gave me the option to generate. First, the method to check whether a flag was in the current set. It gave this function body:

1234 |
public bool CheckFullGameFlags(FullGameFlags flag) { return (InGameFullFlags & flag) != 0; } |
Here is what I had originally:
1 |
public bool CheckGameFlag(FullGameFlags flag) => (InGameFullFlags.HasFlag(flag)); |
While it missed the existing C# method `HasFlag,`
it correctly worked out that I wanted to compare the incoming flag with the set. It found the local set `InGameFullFlags`
from the code above.
I then gave it the complimentary signature for SetFullGameFlag. Again, there is enough in the naming conventions for a cue that I want to add the new flag:

I clicked on the squiggle again and used “Implement with AI” and it generated the code below. Again, it came with a full explanation.

1234 |
void SetFullGameFlag(FullGameFlags flag) { InGameFullFlags = InGameFullFlags | flag; } |
This is the same (bar the expression body token ⇒) as what I had:
1 |
public void SetGameFlag(FullGameFlags flag) => InGameFullFlags |= flag; |
And finally the same for the ClearGameFlag. This just does the bitwise opposite of the set. Again it got this precisely correct.
I would have been happy for the result to be written directly into the editor, or as a code completion, but by writing the assistance in the side panel it came with a good deal of explanation.

## Conclusion
All in all I think the AI Assistant performed admirably; for many developers, AI may already be just an expectation for an IDE. Treating AI Assistant as a registration signup is still a minor nuisance, but that will change eventually. I got the whole IDE and AI Assistant up and running pretty quickly, and it ran appreciably quickly.

To some degree, the “Hey! Look! We have AI” is a current business necessity for IDEs as the environment expands and while agreed expectations are still forming. By next year, much of this will exist as part of the IDE experience, just as Cut and Paste does today.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)