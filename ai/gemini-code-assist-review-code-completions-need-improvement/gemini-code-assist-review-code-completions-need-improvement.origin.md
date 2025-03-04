# Gemini Code Assist Review: Code Completions Need Improvement
![Featued image for: Gemini Code Assist Review: Code Completions Need Improvement](https://cdn.thenewstack.io/media/2025/03/69600efb-joshua-aragon-eab4ml7c7fe-unsplashb-1024x576.jpg)
It was never going to be long before Google got into the game of code assistance with [Gemini](https://codeassist.google/). The headline is the number of completions being [offered for free on their platform](https://thenewstack.io/google-ai-coding-tool-now-free-with-90x-copilots-output/) — 90x what GitHub Copilot offers — and behind that, the understanding that scale is something Google does well. So this is the same play as Gmail giving every user a much larger chunk of space than competitors, back when it launched in 2004.

Gemini Code Assist claims it supports 20+ languages, which again is a strong offering at scale. But as Google doesn’t offer its own IDE, they are likely to be dependent in many cases on Microsoft’s Visual Studio Code (VS Code). I’m beginning to wonder if alternatives like JetBrains are getting a massive boost for this reason. However, the default seems to be VS Code:

You may have seen how I moved code assistants from Copilot to [Augment](https://thenewstack.io/augment-code-an-ai-coding-tool-for-real-development-work/), and I will do the same thing now — but shifting from Augment to Gemini Code Assist, in order to check it out.

I opened VS Code on my MacBook M4 and immediately searched for the extension, freshly available on that day:

Loading the extension appeared to take some time, although there is no progress meter on VS Code. Of course, the servers will have been hammered on day one for a new version.

There was a welcome page, but nothing about setup. As I hadn’t even signed into Google, it was highly unlikely to actually be ready. The left side bar had the Gemini icon, and selecting it did fill the sidebar with a request to log in. But this just underlines what I’ve said previously: the customer journey with extension loading code assistants is weak within VS Code.

I was thrown into a web page to sign in, and navigated back to my IDE to now see the following:

While the sidebar was controlled by Gemini, I still didn’t know who was controlling the code completions. The bottom toolbar seemed to suggest it may be cohabiting with Augment:

(My Copilot menu had moved to the top, even though the copilot extension itself said it needed restarting.)

I disabled the Augment extension to allow Gemini to take sole control. But this is a mess that needs to be fixed by Microsoft.

Meanwhile, Google needs to place a warning on its extension just like Augment did.

As before, I’ll make real changes to my project and see how the code completion behaves. My game project uses random numbers, but I need to take them from a list so that I can generate them in place, or use a pre-rolled set of numbers for testing. As the call order that a number might be taken can change during development, I need to make sure each call takes a fixed index on the list, and in addition check that I don’t accidentally take the same number twice. However, this would be hard to manage within loops, so I return a block of numbers.

I found that Gemini made some poor completions. It tended to jump before understanding context, e.g.:

123456789 |
...private RN[] randomNumbers = new RN[MAXRN]; ... for(short i; i < MAXRN; i++) { float rnd = UnityEngine.Random.value; short converted = (short)(rnd * 100); randomNumbers[i] = new RN(converted, false); TagDebug.Log($"We set number {i} to {rnd}"); //Line suggested by Gemini } |
In the example above, Gemini suggested a log line that prints out the index and value, but misses out the conversion to ‘converted’ that my list directly uses. I often found that as I was updating my solution and deleting older code, Gemini would suggest putting the deleted lines back in. It makes me wonder how much Gemini has been tested during agile development, where refactoring is so important.
(At some stage Augment turned itself back on, and uninstalling the extension made no difference. Only after quitting and opening back up did Augment fully disappear. Now, I’m very aware that my situation reviewing different assistants makes me much more open to clashing assistants, but I’m afraid that while the review should be about Gemini, I was unimpressed with VS Code’s complete inability to control clashing extensions.)

Gemini sensibly stresses “Smart Actions” using **command-i**, which sits between code completion and trying to write bulk code for you:

I first asked Gemini to “Explain this” on the selected method, which is where a block of random numbers is requested. It took about 10 seconds (which is quite long) to produce an output:

*“The RequestNewIndexedBlock method is designed to provide a way for different parts of your game to request and ‘reserve’ a specific block of pre-generated or randomly-generated numbers from the RandomNumber system. It acts as a manager for distributing these blocks.”*
This is a very good summary. The key here is that it recognized the reservation pattern with that term “reserve,” which is not based on any cues I left in code. It also understood that “different parts of your game” point, and that the numbers may be pre-generated. It also presented a detailed “code breakdown” that was perhaps a little too detailed, if anything.

While the method and the whole class work, you can see that I should be using a`ushort`
(unsigned short) for `storeindex`
, as a negative index is not sensible. So I tried the second smart action “fix” to see if it proposed this:

Telling us to be cautious with generated code at this stage is a bit like telling Alice that following rabbits down holes into Wonderland might have unpredictable results!

As is the norm, it created a temporary diff file. The result suggested a superfluous check on the block, which while technically correct relied on assumptions about the internals of another class. If anything, it did make me reduce the access to the `RNBlock`
, so that was indirectly good. Inexplicably, because the temporary file was not part of the project, Copilot tried to make suggestions! My previous remarks about how VS Code handles extensions covers this.

Finally, I let it try the final smart action “Generate unit tests” for this method. I have a separate assembly in the project with tests and a mocking library (Moq), though I’ve written none for this class — and I wasn’t sure Gemini could see these. Glancing at the code, you can see that there are two cases to test as I throw exceptions for them.

It did a good job of creating a setup and teardown, for both a pre-rolled and a generated random set. For the main happy path, the test was sensible enough:

1234567891011121314 |
[Test] public void RequestNewIndexedBlock_ValidIndex_ReturnsBlockAndMarksAsTaken() { // Arrange RandomNumber rng = RandomNumber.GetActiveRandomNumber(); short validIndex = 5; // Act RandomNumber.RNBlock block = rng.RequestNewIndexedBlock(validIndex); // Assert Assert.IsNotNull(block); Assert.AreEqual(validIndex, block.storeindex); Assert.IsTrue(block.taken); } |
## Conclusion
I’ve made my concerns about VS Code’s inability to handle multiple extensions vying for the same LLM functionality perfectly clear, but Gemini Code Assist has to do better in helping the user to disable previous extensions.

The only thing that concerns me regarding Gemini Code Assist is the speed of code completion, which at times was slightly tardy. While code is being refactored, no [code assistant](https://thenewstack.io/top-dev-tools-and-web-developer-trends-of-2024/) can ever be certain which parts of the code are no longer part of the new solution. But I generally felt that Gemini didn’t quite keep up with me — despite the fact that the code explanations were precise.

The quality of the code completions was generally ok — although in my recent tests both Copilot and Augment gave me superior results. But your mileage may vary, and I don’t doubt that scaling out enough processing time may be an issue here. Also if there’s one thing we know, it’s that LLM output only improves over time.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)