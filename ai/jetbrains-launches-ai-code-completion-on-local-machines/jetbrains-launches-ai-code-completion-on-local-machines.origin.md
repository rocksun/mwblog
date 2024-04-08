# JetBrains Launches AI Code Completion on Local Machines
![Featued image for: JetBrains Launches AI Code Completion on Local Machines](https://cdn.thenewstack.io/media/2024/04/1bc544ba-despaired-2261021_1920-1024x683.jpg)
[JetBrains](https://www.jetbrains.com/) is offering full line code completion in its IDE, courtesy of an AI model that runs on local machines so that code doesn’t have to be sent off-premise.
It’s designed to appeal to industries with strict data privacy regulations, such as healthcare and finance, or wherever organizations might be hesitant to send code out the door, the company noted.
“How does our product work? You run a not-so-big, yet smart language model on your local computer and everything happens locally,” explained
[Daniel Savenkov](https://www.linkedin.com/in/daniel-savenkov-098b41149/?originalSubdomain=rs), a senior machine learning engineer at JetBrains. “It’s really important because not everyone is ready to share their code to cloud.”
## Model Runs on Internal Machines
The fact that JetBrains code completion runs locally makes it different from other code competition tools, including
[GitHub’s Copilot](https://thenewstack.io/hey-github-tries-a-voice-interface-for-copilot/), which relies on external calls to the cloud-based large language model underlying it. While there are user agreements in place with Copilot that prohibit using the code for anything other than code completion, in some industries that’s simply not enough due to security concerns, Savenkov said.
The JetBrains code completion model is still a
[large language model](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/), but with 100 million parameters. By comparison, industry-standard models are 100 times larger, Savenkov added. The smaller model is one reason the code completion model handles full line code completion rather than large blocks of code. It’s really hard to work with large blocks of generated code, Savenkov said. Since some suggestions may not be good, the coder has to review all the code created by the AI model.
There is some debate in the industry over which length of code completion works best, Savenkov said. Some code completion products can produce huge chunks of code, but also may hallucinate things like API calls. JetBrains settled on one line of code completion as a “pretty fair trade-off” that
[developers can easily work](https://thenewstack.io/using-ai-to-help-developers-work-with-regular-expressions/) with, he added.
The fact that it’s run locally also minimizes latency issues.
“It’s a much simpler task than the task to generate 10 lines of code or a block or entire method or entire class,” he said. “Because of that, we have an opportunity to go with smaller models and to get really meaningful and useful results. So that was roughly the way we arrived here, where we have [a] local, not so big, model generating a
[single line](https://thenewstack.io/preflight-defends-against-supply-chain-attacks-with-single-line-of-code/) of code.”
## Smaller LLM Offers Comparable Quality
The quality is similar, even though the LLM is smaller, he claimed.
“We do not have a dramatic drop of quality in our use case, as compared to really big cloud-based models. Of course, if we start to try to generate blocks of code, the difference will be much bigger, but keeping a single line, the difference is not so big,” Savenkov told The New Stack.
The model also leverages information from the IDE to filter out hallucinations such as calls to APIs that don’t exist. This also helps ensure that the code suggestions do not contain syntax errors such as non-existent variables or methods, he noted.
Also, since the language model is trained on certain languages and frameworks, rather than generally trained, it can be a smaller size, added
[Mikhail Kostyukov](https://www.linkedin.com/in/mikhailkin/?originalSubdomain=nl), the company’s ML product manager.
JetBrains piloted the code completion feature in PyCharm, its Python IDE. As of today, it is available for Java, Kotlin, JavaScript, TypeScript, CSS, PHP, Go, and Ruby within the corresponding JetBrains IDEs out of the box: IntelliJ IDEA, WebStorm, PhpStorm, GoLand, and RubyMine.
In the coming months, the company will extend the functionality to C#, Rust, and C++ in all JetBrains IDEs that support these languages, including Rider, RustRover, CLion Nova, and more.
In addition to its code completion offering,
[JetBrains offers an AI Assistant](https://thenewstack.io/jetbrains-launches-new-ai-assistant-powered-by-multiple-llms/) as an add-on subscription service that can autocomplete entire blocks of code. The AI Assistant also offers improved test generation and cloud code completion, custom prompts for commit messages, the ability to create files from AI chat, and updated in-editor code generation, the company said.
It’s available in IntelliJ IDEA, PyCharm, PhpStorm, ReSharper, and other JetBrains IDEs; as well as in Fleet, as a supplemental feature.
This 2024.1 update also introduced other new features to JetBrain’s IDEs, including an overhauled terminal feature with enhancements that streamline command-line tasks. The terminal now enables navigation within blocks, nesting each command separately, a command completion feature, and easy access to the command history, the company noted in a press release. Among the improvements to particular IDEs are:
- IntelliJ IDEA will provide support for the features in the newly released Java 22. It also incorporates the new Kotlin K2 mode based on the K2 Kotlin compiler for enhanced code analysis.
- RubyMine can execute VCS commands in the context of the current product’s local SDK.
- PyCharm 2024.1 brings new features to
[integrated Jupyter notebooks](https://thenewstack.io/integrate-jupyter-notebooks-with-github/), along with simplified version control with new visual diff, widgets rendering, and the ability to explain pandas and Polars DataFrames with AI Assistant. Also, all documentation on the Hugging Face models is directly accessible in PyCharm.
- PhpStorm adds support for Symfony’s AssetMapper. The press release noted that developers can now quickly install missing modules and packages via importmap.php and utilize full autocompletion for their classes and methods. They also can generate
[Pest tests](https://pestphp.com/)for PHP classes and methods and create new Pest tests right from the Intention actions menu. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)