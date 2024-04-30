I made the multimodal multitool mobile application
[CrayEye](https://www.crayeye.com) in a language & framework with which I'm unfamiliar by relying on modern large language models to write not just snippets but the entirety of the code. While I later on made minimal tweaks by hand (e.g. changing element colors or swapping their positions), LLMs did all the early & heavy lifting.
For the purpose of this exercise, I used the latest state-of-the-art models available to me via web UI:
- OpenAI's
[GPT-4](https://cdn.openai.com/papers/GPTV_System_Card.pdf)
- Anthropic's
[Claude 3 Opus](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf)
- Google's
[Gemini Advanced](https://support.google.com/gemini/answer/14517446?hl=en&co=GENIE.Platform%3DAndroid)
Ever since the early pre-release demos of
[GPT-4V](https://openai.com/research/gpt-4v-system-card), imaginations have run wild with what sorts of magical new things we'll be able to build with it. The implications of the technology for vision based user experience can't be understated - what once took a dedicated team of specialists a substantial amount of time and resources can now be done with even greater proficiency and detail with a trivial call to a multimodal LLM. I wanted to explore what they were capable of without spinning up
create-react-app or
create-next-app frontends for every idea and truly explore what
[Ethan Mollick](https://www.oneusefulthing.org/) calls the [jagged frontier](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged) (i.e. the line between what this tech is and isn't capable of which can shift rapidly even among seemingly adjacent or comparable domains and tasks).
My requirements were largely:
- Quick interface for capturing input
- Ability to use all cameras with minimal friction
- Configurable prompts that could be edited and shared
- Incorporation of on-board sensor data (e.g. location) into prompts
I decided to create an app. It had been a while since I'd created a native app and I'd been wanting to kick the tires on the landscape again, and this use case of a multimodal multitool offered the perfect opportunity.
Since my last run at making native apps,
[Flutter](https://flutter.dev/) had grown in popularity, so I decided to give it a go even though I hadn't worked with [Dart](https://dart.dev/) before. My unfamiliarity with the language was actually going to be useful here, because another thing I wanted to get my feet wet with was testing today's LLMs' capabilities for holistic development.
I kicked things off by following
[Flutter documentation](https://flutter.dev/learn) to set up the [Flutter dev tools for iOS](https://docs.flutter.dev/get-started/install/macos/mobile-ios?tab=download) and firing off a
flutter create.
At this point, the boilerplate app's core logic was contained entirely in
lib/main.dart - this made it particularly easy to start working with immediately. I began prompting to add simple functionality - a camera preview, a remote HTTP request to analyze the image via GPT, and the app's functionality (and lines of code) quickly began growing. My prompts leaned heavily on requesting:
"the complete modified files after these changes with no truncation"
This was critical because I wanted to both reduce the friction of shuttling responses between the LLM and disk as well as ensure it was fully explicitly accounting for areas of change in context with the rest of the code as it generated its responses. My evidence is purely anecdotal, but it generally seemed to produce higher quality results with fewer regression issues than letting it pass along patch updates to partial sections of files.
Shortly after my
[initial commit (76841ef)](https://github.com/alexdredmon/crayeye/commit/76841ef2a105817d7062baf5055147bd8842a27c) of a minimally functional POC, I had the LLM perform a [modular refactor (6247975)](https://github.com/alexdredmon/crayeye/commit/624797532388cd24e46041f97914378fcc15bcf2) to split things into separate files. This was helpful both from a best practices and workflow performance standpoint, given that I had to wait less for it to output smaller chunks of more modularly split files.
Now that things were in separate modules, I needed to distinguish the different files/modules from each other as I passed the codebase along to the LLM. At this point, I added comments to the beginning of each file containing its name and an
// eof comment at the end. My prompt looked something like this:
You are a software development team. Ask for the codebase if not provided, and base all your changes around this codebase. When provided with the codebase, reply only with "I'm in" unless a new feature has been requested.
The user will ask for features - respond first with the files that need to be changed followed by a brief summary of the changes. Only output files that require changes to implement the current feature. When you output the files, begin with the filename of the file being updated and then output the entire un-truncated file after modifications. Do not remove any comments. Ensure that the first line of each file is "// FILENAME" where "FILENAME" is the file's name, and that the last line of each file is "// eof" - and most importantly, make sure to surround each file with triple backticks "```" so that they will be entirely formatted as code.
Here's my codebase:
By saving the prompt in the lib directory prefixed by an
_ (specifically
lib/_autodev_prompt.txt) to ensure it floated to the top of sorted lists of files, I could easily
cat lib/* | pbcopy and have my prompt alongside my entire codebase, delimited by filename identifiers, ready to paste in my LLM of choice. In the running were:
- OpenAI's
[GPT-4](https://cdn.openai.com/papers/GPTV_System_Card.pdf)
- Anthropic's
[Claude Opus](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf)
- Google's
[Gemini Advanced](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/#gemini-15)
I found that the various providers excelled at different things. Anthropic's Claude was perfectly suited to the copy-pasta workflow, automatically collapsing a large paste into an attachment style inteface. ChatGPT and Gemnini neither collapsed nor auto-formatted the code input, leading to a bit messier of a UX out the gate:
Gemini rendered pretty much exactly the same, although it also ultimately ran into a character count constraint at ~31,000 characters. This was pretty limiting once the app was off the ground.
Gemini also seemed consistently keen to dive into suggesting changes before any features had been requested, although with some adjustment to the prompt this could be somewhat avoided.
Claude generally seemed to do the best with the prompt I had at producing complete changes without introducing regression issues, as well as properly responding "I'm in" at the start rather than diving into un-requested changes. The larger the code base grew, the less this seemed to be the case - I ultimately wound up adding another reminder at the end of my prompt in later requests:
I frequently began hitting the Claude message throttle, which would reset every ~8hrs - this became my primary bottleneck as the features acculuated and codebase grew. Claude 3 Opus showed itself to be hands-down the champ at consistently producing complete untruncated files and changes with few to no bugs or regressions.
Eventually, the codebase grew large enough that even Claude Opus would start to suggest changes before any features were described, just as Gemini had done. It seemed the context window or at least the size of the prompt was the cause here, as it consistently happened over a certain line/character count.
In
[autodev prompt tweaks (5539cfb)](https://github.com/alexdredmon/crayeye/commit/5539cfb428770785779f3ba78599ed5972cb1e93), I finally broke the prompt out into two parts - sandwiching the codebase with a [before](https://github.com/alexdredmon/crayeye/blob/5539cfb428770785779f3ba78599ed5972cb1e93/flutter/lib/_autodev_prompt.txt) and [after](https://github.com/alexdredmon/crayeye/blob/5539cfb428770785779f3ba78599ed5972cb1e93/flutter/lib/z_autodev_prompt_end.txt) prompt. This seemed to resolve the issues with suggesting changes before features were requested, as well as ensuring more consistent adherence to the "complete files after these changes with no truncations" rule.
With the sandwich prompt in place, it was off to the races again - iterating quickly was again a breeze and feature requests readily turned into code.
The MVP, which allowed me to add/edit prompts with location data interpolated in, came out quite usable and useful:
It supported interpolating the user's location values using the tokens
{location.lat},
{location.long}, and
{location.orienation} to represent their current latitude, longitude, and north/south/east/west orientation at the time of executing the prompt.
I initially assumed I migh need to use an API call like I do for
[WhatsMyHood](https://whatsmyhood.com/) to interpret the user's neighborhood from their latitude/longitude, but it turned out just providing the raw values to the LLM was sufficient - it was able to work out which neighborhood you were in just as well as Google Maps' API.
There were areas for improvement, such as improving the cramped "Add/Edit Prompt" dialog, but I could easily manage and share my prompts and test them in the field - and even save my favorite responses.
I was ready to share my app. I prepared to test on Android and submit to the Google Play Store and Apple App Store. That's when I first encountered my first serious setback - after setting up the
[Android dev tools](https://docs.flutter.dev/get-started/install/macos/mobile-android?tab=download) I fired up
flutter emulators and tried to run my app on an Android emulator. It was a no go - it turned out several packages I was using weren't compatible with my target Android SDK version, and after several attempts of getting an LLM to properly address I finally landed on a solution involving
[dropping a dependency (f18c8b2)](https://github.com/alexdredmon/crayeye/commit/f18c8b2e276f12b21f7e586f46d7581e34ceb1ed) (and in doing so, support for the
{location.orientation} interpolation values in prompts).
- I was able to quickly make a feature-complete cross-platform MVP with minimal effort/input thanks to the force multiplier of modern LLMs - the initial MVP took ~10hrs of human work/input.
- For my purposes, Claude Opus 3 did far and away the best job of consistently producing functional code without regressions
- Gemini was limited to building an app beyond ~31k characters (including all prompts)
- ChatGPT had the largest tendency to introduce regression errors or ignore instructions to output complete untruncated files
- Business limitations outpaced technical ones (i.e. Anthropic message throttle, initial App Store rejection)
- The workflow utilized could obviously lend to further automation, particularly using autonous agents (e.g. Autogen) to write and test changes with a human in the loop purely for requirements input and validation of acceptance criteria.
- Code search and ability to map / use code maps or documentation would be ideal for larger projects
- While the MVP took ~10hrs of hands-on input/work, this was spread across a number of days/weekends given the message cap for Claude 3 Opus. By using the API rather than the web UI or otherwise circumventing message caps, the timeline to delivery could have been accelerated.
Large language models as they're used for code generation can be conceptualized similarly to the latest higher level language for development - just as the existence of Python has not supplanted all development in C, LLMs don't necessarily obviate 100% of lower level language development - even if it undeniably accelerates the ability to execute on said lower level development.
They do however take a big bite - a strikingly large and growing percentage of use cases can be handled exclusively by a modern foundational LLM
*today* and that number is only going to go up.
find me on: