Apple may not be [a fan of vibe coding](https://www.theinformation.com/articles/apple-cracks-vibe-coding-apps), but Google is leaning in. On Tuesday, Google [announced](https://android-developers.googleblog.com/2026/05/build-android-apps-google-ai-studio.html) that anyone can now use [Google AI Studio](https://aistudio.google.com/apps?features=build_android_app) to build native, Kotlin-based Android apps with just a few prompts. To test the result, users can install the app on their device and share it with others for testing, or bring it into Android Studio to refine the details and get it ready for wider distribution.

As Google notes in its announcement, AI has made it almost trivial to build web-based applications (though running those in production is another issue). Mobile development, however, has taken something of a back seat as everybody runs their MVPs in the browser on *localhost:3001.* And while Google already supported Gemini in Android Studio for vibe coding mobile apps (and, starting today, supports virtually any popular LLM, too), getting started there was surely a hurdle for many non-developers.

> “Now, you get the best of both worlds: the ease of a prompt-based interface paired with the power of the Android SDK, all in your browser, no installation required.”

“Now, you get the best of both worlds: the ease of a prompt-based interface paired with the power of the Android SDK, all in your browser, no installation required,” writes Google.

The company notes that building Android apps in AI Studio, Google’s web-based tool for testing new models and prototyping applications, uses the same technology that powers building apps with Gemini in Android Studio. The apps will be built in Kotlin and use Google’s Jetpack Compose, which is the current standard for building Android apps.

> What this really enables…is the ability to use all the features on a mobile device, including the built-in sensors, GPS, Bluetooth, and NFC.

What this really enables, though, is the ability to use all the features on a mobile device, including the built-in sensors, GPS, Bluetooth, and NFC. Google’s example shows how this could work on a Pixel Watch (those are Android devices, too, after all) for building an avionics panel that mimics what you’d find in a small airplane with data from the GPS, gyroscope and other sensors — though while Google’s prompt asks for an airspeed indicator, that’s not something the watch can ever know (groundspeed will do for this, though).

Google, of course, also notes that you can integrate Gemini into the apps to bring AI capabilities to them.

AI Studio now comes with a built-in Android emulator for previewing the app, but the real test is how well it runs on an actual device. For this, users only need to plug their Android phone into the machine running AI Studio, and the integrated Android Debug Bridge will take over.

To continue building the app in Android Studio, Google will allow developers to download the code as a zip file.

What’s especially interesting here is that Google is also building a direct connection to its Google Play Console, so users can upload the apps directly to Google Play for testing and sharing. One caveat is that you need a [Google Play developer account](https://play.google.com/console/u/0/signup), which comes with a one-time $25 registration fee. “AI Studio will automatically create your app record, package the bundle, and upload it to an internal testing track in Google Play Developer Console.”

Soon, you will also be able to share this app from AI Studio directly with friends and family.

Also on the roadmap are integrations with Firebase, Google’s backend platform for adding databases, authentication, and more to mobile apps.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)