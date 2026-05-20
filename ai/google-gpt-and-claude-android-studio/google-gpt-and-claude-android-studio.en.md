Google is using its annual I/O developers conference to announce quite a few new AI-centric tools for building Android apps. These include the ability to build native apps in its AI Studio prototyping environment, but Android Studio, Google’s dedicated IDE for building these apps, is also getting a number of updates. In addition, the Android CLI is now available as a 1.0 release and can be used from Google’s Antigravity app.

> “This flexibility offers developers greater control over performance, privacy, and cost,” Google says in its announcement.

## Choose your own model

What shows off Google’s current approach to how developers want to build their apps best, though, is maybe the fact that they can now choose either Gemini, GPT from OpenAI, or Claude from Anthropic for building inside of Android Studio. For those who want to use a local model, Gemma 4 is now also available, and in the latest canary build of Android Studio, developers can download it directly from the IDE without the need to run it with the help of an external server.

“This flexibility offers developers greater control over performance, privacy, and cost,” Google says in its announcement.

Earlier this year, the company launched [Android Bench](https://developer.android.com/bench), its benchmark and leaderboard for testing how well a given model handles building Android development tasks. Currently, GPT 5.5 leads the pack there, with GPT 5.4 and Google’s own Gemini 3.1 Pro Preview sharing second place (Opus 4.7 comes in fourth). The best models can currently resolve just under 75% of test cases in the benchmark.

Google, of course, would love to have you use its own Gemini models, and to sweeten the deal, Google AI Pro and Ultra subscribers will get “dedicated capacity and higher rate limits for Gemini in Android Studio,” the company says.

## Android CLI

The [Android CLI](https://developer.android.com/tools/agents/android-cli) has been around for a few weeks now, and at I/O, Google pronounced it’s now a 1.0 release and stable. Like so many other recent CLI tools, the point here isn’t so much to give developers access to Android development features from the command-line, but to give AI agents access to them. This is about agent-first workflows that give agents the ability to use Google’s official tools, skills, and knowledge base for Android development.

Any agent could use the CLI, too, which is part of how Google is positioning so many of its recent announcements in this age of “[zero developer loyalty](https://thenewstack.io/google-doesnt-care/).” This means that Claude Code, Codex, or Google’s own Antigravity can use the CLI.

With this latest version of the CLI tool, Google is introducing the *`android studio`* command, which lets “the agent of your choice to leverage the deep, contextual capabilities of Android Studio to understand better and perform actions on an open Android project,” Google explains.

As Google also notes, having the agent run side-by-side with Android Studio will allow it to better work with the codebase, and when it comes to moving from the agent harness to Android Studio, the transition will be much easier.

 “By leveraging the new `android studio` commands, developers can now grant their preferred agents the ability to perform semantic symbol resolution, analyze files for warnings, and even render Jetpack Compose previews,” Google says.

Agent Skills, by the way, are now available in Android Studio to help ground models with specialized knowledge for a given project, and built-in skills for Android development and for using Google’s Firebase platform now come with Android Studio.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)