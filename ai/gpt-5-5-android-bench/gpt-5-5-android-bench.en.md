**Google wants software developers to use the best possible AI models when building Android applications;** consequently, the company debuted its [Android Bench](https://developer.android.com/bench) benchmarking portal in March. The service is intended to provide a continuously updated leaderboard to act as a reference point for developers and model creators.

The leaderboard was updated last week to include [open-weight models](https://thenewstack.io/ai-hardware-and-open-models-headed-in-the-linux-direction/) and add new columns for latency, [tokens](https://thenewstack.io/the-different-token-types-and-formats-explained/), and cost.

> “By establishing a clear, reliable baseline for what high-quality Android development looks like, we’re helping model creators identify gaps and accelerate improvements — which empowers developers to work more efficiently.”   
> —Matthew McCullough, Google.

## Model students

[Matthew McCullough](https://www.linkedin.com/in/matthewjmmccullough/), Google VP of product for the Android Developer division, [writes in a March blog post](https://android-developers.googleblog.com/2026/03/elevating-ai-assisted-androi.html#:~:text=We%20know%20you%20want%20AI,of%20LLMs%20for%20Android%20development.) that Google actively benchmarks top AI LLMs against tests designed to assess how these tools can build Android apps.

“Our goal is to provide model creators with a benchmark to evaluate LLM capabilities for Android development,” explains McCullough. “By establishing a clear, reliable baseline for what high-quality Android development looks like, we’re helping model creators identify gaps and accelerate improvements — which empowers developers to work more efficiently with a wider range of helpful models to choose for AI assistance — which ultimately will lead to higher-quality apps across the Android ecosystem.”

## GPT 5.5 is currently the best AI model for Android

This new service doesn’t appear to offer a historical record of where models have risen and fallen over time, but [*9to5Google*](https://9to5google.com/2026/05/21/best-ai-android-app-coding-development-google-list/) reports that the last Android Bench ranked Gemini 3.1 Pro alongside OpenAI’s GPT 5.4 as joint leaders.

As of the May 18 update, GPT 5.5 is currently the best AI model for Android app development.

Google provides an [openly accessible explanation of its operating methodology](https://developer.android.com/bench/methodology) for Android Bench to explain that, “The service evaluates the ability of LLMs to generate code that resolves the issue by presenting them with real-world issues and pull requests from open-source software projects. This approach aims to ensure that the tasks are representative of the challenges developers face daily.”

## Why did Google build Android Bench?

Google has said it built Android Bench because AI-assisted software engineering “has seen the emergence of several benchmarks” for measuring LLM capabilities. The company has further stated that Android developers “face specific challenges that aren’t covered by existing benchmarks”, so it created a ranking service that to focus on a comprehensive total assessment of high-quality Android development.

“We created a model-agnostic benchmark to accurately evaluate LLM performance on a variety of Android development tasks,” [stated Google](https://developer.android.com/bench/methodology). The company further defined the goals of Android Bench as a means of encouraging LLM improvements for Android development; empowering Android developers to be more productive with a range of “helpful models” for AI assistance; and leading to higher-quality applications across the Android ecosystem.

## Do software development benchmarks work?

Developers and model creators will naturally question whether Google’s action to set up this benchmarking is useful. Naysayers might naturally point to [Goodhart’s Law](https://en.wikipedia.org/wiki/Goodhart%27s_law#cite_note-Strathern1997-1), which states that, “When a measure becomes a target, it ceases to be a good measure.” Certainly, any reward system can attract actors who optimize their actions to achieve standardized goals.

Google may have second-guessed this pitfall by establishing Android Bench based upon real-world public code repositories.

“We created the benchmark by curating a task set against a range of common Android development areas. It is composed of real challenges of varying difficulty, sourced from public GitHub Android repositories,” writes Google’s McCullough.

This means scenarios tested against include resolving “breaking changes” across Android releases (when code that worked fine previously becomes corrupted as a result of Google updating Android to a new version), domain-specific tasks such as networking for wearable devices (where the specter of high latency and frequent disconnections is always a threat), and migrating to the latest version of Jetpack Compose (Android’s own declarative UI toolkit that uses Kotlin language functions), and more.

## What other Android benchmarks exist?

Other Android benchmarks include [Jetpack Microbenchmark](https://developer.android.com/topic/performance/benchmarking/microbenchmark-overview), a library that allows developers to benchmark their Android native code — whether written in Kotlin or Java — from within Android Studio. The sister Jetbank Macrobenchmark is provided to test large-scale user interactions, such as cold app startup time or the fluidity of user interface animations.

Also available in the Android benchmarking space is [Firebase Performance Monitoring,](https://firebase.google.com/products/performance) a production-level field benchmark that monitors an app’s network requests and screen rendering times; this is more of an application performance monitoring tool.

Within the Android developer community, [Android Vitals already](https://developer.android.com/topic/performance/vitals) provides a dashboard to track app quality metrics such as stability, performance, battery usage, and permission issues. Apptim is a generative AI mobile app profiling and testing tool, so again, performance benchmarking, but not quite the same as Android Bench. We could also mention Google’s own Android Performance Analyzer (APA). which only arrived on 19 May this year and serves as a profiling and performance analysis tool with workflow simplification support.

> “Open benchmarks like Android Bench are great, and we wish there were more of them. The caveat is data contamination. Public repositories leak into training, and we have seen models that cluster within a few points on public evals spread dramatically on private benchmarks built to mimic the same workload.” – Andrew Filev, CEO, Zencoder.

[Andrew Filev](https://www.linkedin.com/in/filev/), CEO and founder of code orchestration company [Zencoder](https://zencoder.ai/), tells *The New Stack* that he’s a fan of these systems, with caveats.

“Open benchmarks like Android Bench are great, and we wish there were more of them,” Filev enthuses. “In general terms, software development is too diverse for a single headline score to be universally meaningful — a Python benchmark tells you little about how a model handles Rust, embedded systems, or a mobile app. There’s also a real gap between building an open web app, an internal tool used by a few hundred people, and a multi-tenant product at a global scale, and models do not perform identically across those domains.”

Consequently, he says, domain-specific benchmarks push model developers to pay attention to the environments their users actually work in, so he thinks that “Google deserves credit here” and hopes other platforms follow.

“The caveat is data contamination. Public repositories leak into training, and we have seen models that cluster within a few points on public evals spread dramatically on private benchmarks built to mimic the same workload,” Filev says. “In our own research, a small change in how we framed test cases shifted the model spread from six percentage points to 26 and completely reordered the rankings. So public benchmarks help improve LLM performance across domains, and private evals help assess real-world performance on your workload.”

## How Android Bench scores are built

Each Android Bench model’s overall benchmark score is based on a Google-developed calculation comprising four core values.

The confidence interval (CI) range (%) is a measure of the expected performance range, reflecting the results’ statistical reliability (p-value, 0.05); the average latency score is the time taken to solve 100 tasks across 10 runs; the average total tokens score is a measure of token consumption for a full benchmark run across 10 runs; and the average cost is the cost per benchmark run at the time of testing, in US dollars.

The test harness for Android Bench is [publicly available on GitHub](https://github.com/android-bench/android-bench).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)