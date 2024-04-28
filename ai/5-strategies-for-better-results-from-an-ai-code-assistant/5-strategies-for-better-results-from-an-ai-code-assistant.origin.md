# 5 Strategies for Better Results from an AI Code Assistant
![Featued image for: 5 Strategies for Better Results from an AI Code Assistant](https://cdn.thenewstack.io/media/2024/04/474ac28b-rizelscarlett-2-1024x768.jpg)
Copilots, like all GenAI, are non-deterministic; meaning they vary in outcome. But while using AI code assistants, developers can use prompt engineering to refine and guide the AI for better outcomes, according to
[Rizel Scarlett](https://www.linkedin.com/in/rizel-bobb-semple/) — who is a developer advocate, including recently for [GitHub Copilot](https://thenewstack.io/github-copilot-and-open-source-a-love-story-that-wont-end-well/).
Scarlett is now a staff developer advocate at
[TBD](https://www.tbd.website/), a business unit operating within Block that’s building open source platforms and protocols for exchanging money internationally. She shared five strategies for improving a copilot’s results at this week’s [InfoBip Shift conference](https://shift.infobip.com/) in Miami.
First, she set up a scenario: Imagine, she asked the audience, a developer named Dawson who suffers a bit from imposter syndrome. Fortunately for Dawson, she has a friend who can help — a developer and time traveler named Phil, from Disney’s
[Phil of The Future](https://www.imdb.com/title/tt0340281/), except he’s all grown up.
Dawson has a problem: She has to create an identity verification program, but she doesn’t know how and she’s unsure how to really leverage Copilot to help her, Scarlett said. Phil is from the 22nd century when
[AI assistants](https://thenewstack.io/meet-the-star-member-of-the-it-team-the-ai-assistant/) are the norm. He helps her jumpstart her efforts with five strategies for prompting Copilot.
## Strategy 1: Provide High-Level Concepts
The first step is to provide the GPT with high-level context. In her scenario, Phil demonstrates by building a Markdown editor. Since Copilot has no idea of the context, he has to provide it and he does this with a large prompt comment with step-by-step instructions. For instance, he tells the copilot, “Make sure we have support for bold, italics and bullet points” and “Can you use reactions in the React markdown package.” The prompt enables Copilot to create a functional but unsettled markdown editor.
## Strategy 2: Provide Details
Follow up by providing the Copilot with specific details, Scarlett advised.
“If he writes a column that says get data from [an]
[API](https://thenewstack.io/api-design-is-pretty-bad-heres-how-to-fix-it/), then GitHub Copilot may or may not know what he’s really trying to do, and it may not get the best result. It doesn’t know which API he wants to get the [data](https://thenewstack.io/sir-tim-berners-lees-solid-protocol-puts-data-back-in-the-control-of-the-end-user/) from or what it should return,” Scarlett said. “Instead, you can write a more specific comment that says use the JSON placeholder API, pass in user IDs, and return the users as a JSON object. That way we can get more optimal results.”
## Strategy 3: Provide Examples
There are three terms to understand when it comes to giving AI examples, Scarlett said:
- Zero-shot learning, in which the model is expected to correctly make predictions for tasks on which they have never been explicitly trained. A human example would be trying to defeat a video game without playing it, but using strategies the gamer learned from previous video games.
- One-shot learning, which provides a single example to the AI. The corollary is being expected to competently play any character and defeat any opponent after playing one match in the game.
- Few-shot learning, where the model is provided with a small set of examples. This would be like doing two to five missions in the new game and then being expected to fully navigate the game.
## Strategy 4: Keep A Few Tabs Open
This one may seem a bit surprising, but keeping open a tab or two open in the editor allows GitHub Copilot to gain context from the tabs. Too many open tabs can lower the quality of the Copilot suggestions, she cautioned.
## Strategy 5: Use Copilot Chat
Our heroine Dawson loves the advice and results, but she actually would like to get code feedback. Copilots come with a chat function, which can be used for tasks such as fixing bugs, formatting dates, refactoring code, testing code and
[generating](https://thenewstack.io/make-your-dev-life-easier-by-generating-tests-with-codiumai/) tests, Scarlett said. It can be asked to identify any bugs and then asked to provide a solution with a brief explanation, she said. She then demoed asking GitHub Copilot to generate a [test using the open source JavaScript testing framework](https://thenewstack.io/jest-metas-javascript-testing-framework-joins-openjs/), Jest. ( [Microsoft’s Copilot](https://thenewstack.io/microsoft-one-ups-google-with-copilot-stack-for-developers/) also offers a chat interface.)
By using Copilots, developers can do more than increase productivity, Scarlett added. Copilots can also improve psychological safety, especially in new
[developers or others who might have imposter syndrome](https://thenewstack.io/shameless-developers-how-to-manage-imposter-syndrome-within-your-team/), she said.
“Unfortunately, the reality is psychological safety is not always common at work, especially in second history, and especially for minorities,” she said. “Beginner devs can gain reassurance from a Copilot because it can act as a peer, providing us with ideas when using a new tool for the first time.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)