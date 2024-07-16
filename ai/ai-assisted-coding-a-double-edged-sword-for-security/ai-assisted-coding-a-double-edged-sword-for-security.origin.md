# AI-Assisted Coding: A Double-Edged Sword for Security
![Featued image for: AI-Assisted Coding: A Double-Edged Sword for Security](https://cdn.thenewstack.io/media/2024/07/9aa57160-bruce-pic-1-1024x768.png)
PARIS — Developers on a wide scale are using and creating AI models and [large language models (LLMs)](https://thenewstack.io/llm/), as these facilities offer both the creation of code and the development of applications for LLMs. The popularity of LLMs has exploded, but despite the enthusiasm, the security issues resulting from this rapid advancement remain unsolved, not fully understood, and ultimately overlooked.

Some observers, especially in the security business, argue that we are moving far too fast before security is properly implemented and managed. This mirrors the mistake made with cloud native technologies like [Kubernetes](https://thenewstack.io/llm/), where security concerns were not fully addressed before widespread adoption. It’s challenging to stop someone from using a cutting-edge technology before all security issues are resolved.

“The problem is the volume of code — using tools like [Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) and GPT to write code means you’re writing much more code than before, which is great for productivity but doesn’t speed up the security process. We’re essentially clogging up the pipes with all this new code,” [Dan Lorenc,](https://www.linkedin.com/in/danlorenc) co-founder and CEO of [Chainguard,](https://www.chainguard.dev/) said during his keynote at the recent Linux Foundation [ AI_dev](https://aidevsummit.co/) conference. “Security was already struggling to keep up with developers, and now the amount of code being written has increased tenfold… No security team is prepared to handle 100 times the amount of code.”

The trials and tribulations for security teams to review and monitor security through observability are well-known. But as they look for bugs and vulnerabilities and test new features, “this approach won’t work with 100 times the amount of code and 100 times the number of features, and 10 times the number of developers,” Lorenc told me a few days ahead of the conference.

More developers are deploying AI workloads and don’t really know how to do that securely yet says

[@chainguard_dev]’s[@lorenc_dan]at the[#AIDev]conference.[@CloudNativeFdn][@linuxfoundation][@thenewstack][pic.twitter.com/XMqfYKZfgn]— BC Gain (@bcamerongain)

[June 19, 2024]
AI-assisted development has engendered an explosion in the open source code available and pull requests on [GitHub,](https://thenewstack.io/githubs-2fa-push-boosts-adoption-among-developers/) for example. As Lorenc noted, GitHub repositories for AI are getting hundreds of thousands of stars over a weekend in many cases, and many are writing AI code, even without backgrounds in it. “It’s great to see new people are writing and consuming code, which is wonderful, but we can’t forget about securing all the layers underneath — nothing changes. But you have to prepare for the new generations of people who don’t know about all those little problems,” Lorenc said. “You have to make it so they don’t need to know about security — telling every developer that they must know about security has never worked.”

During his talk, Lorenc made the comparison between [AI-generated code](https://thenewstack.io/ai-code-generation-6-faqs-for-developers/) and models and thermodynamics, which I remember fellow students in college claiming the professor said was 99% chaos.

Not unlike the inability of predicting the speed and position of electrons, I would say. The AI security conundrum is comparable to fluid dynamics in engineering, says

[@chainguard_dev]’s[@lorenc_dan]at the[#AIDev]conference.[@CloudNativeFdn][@linuxfoundation][@thenewstack][pic.twitter.com/bZHAXZ0TAO]— BC Gain (@bcamerongain)

[June 19, 2024]
Lorenc compared the present dilemma to fluid dynamics — a very difficult subject I heard tell, when I was in college. Instead of the more predictable laminar flow, AI security is like measuring and predicting turbulent flow patterns that manifest in chaotic environments. As developers use AI tools to write more and more code, they’re not using those same techniques to help review that code, leading to the present situation of there being too much water “flowing through the pipe than we can handle,” Lorenc said during his keynote.

“The transitional state here, when something first begins to transition from that one model to another, this is actually the toughest to reason about. This is the toughest type of system to model. In fluid dynamics, that transition doesn’t really happen at a set time, either,” Lorenc said. “There are some constants and ratios you can plug in to try to predict and guess which state of that you’re in, but a lot of engineering work goes into ensuring you know which regime you’re operating in, whether it’s laminar or turbulent. When you’re here in the middle, you don’t really know what to do.”

Already attackers have begun to use LLMs to generate new vulnerabilities or permutations on existing vulnerabilities to bypass signature detection,” Lorenc said. “We have to get out of that transitional state in order to fully understand and be able to work together as an industry again,” Lorenc said. “When that transition completes, though, and you get back over to the turbulent one, it makes folks feel really uncomfortable because scientists and physicists can’t actually explain how this works.”

![](https://cdn.thenewstack.io/media/2024/07/db459e4e-img_4850-2.jpg)
Jossef Kadouri and Tzachi Zornshtain, who are both head of software supply chain at Checkmarx, describe supply-chain threats from AI during their talk “Dark Side of AI: The Hidden Supply Chain Risks in Open.”

The developer can make diligent efforts to vet AI-generated code, but more work needs to be done in order for vulnerability detection and remediation to become effective. During their talk “Dark Side of AI: The Hidden Supply Chain Risks in Open,” [Jossef Kadouri](https://www.linkedin.com/in/jossef/) and [Tzachi Zornshtain,](https://www.linkedin.com/in/tzachi-zornstain/) who are both head of software supply chain for [Checkmarx](https://checkmarx.com/), described specific threat vectors.

When using ML models with weights — parameters that are honed to improve neural-computing results in specific LLMs — it is very difficult to determine whether code is malicious or not. “I’m not saying the developer used to check the code that they were downloading — most of them weren’t doing that, but at least they had the option,” Zornshtain said. “When you’re getting an [ML model](https://thenewstack.io/training-a-ml-model-to-forecast-kubernetes-node-anomalies/), is it good or is it bad? It’s actually a bit more problematic for us to apply some of the changes there.”

Who among us, when writing a program or generating code, has not at least asked [ChatGPT](https://thenewstack.io/how-to-learn-unfamiliar-software-tools-with-chatgpt/) for its opinion or used a tool like GitHub Copilot? However, inputs into ChatGPT or other LLMs do not always result in the same output, due to the neural network configuration of machine learning and other aspects of these AI models involving hallucinations. When taking open source LLMs to build a service, an attacker can upload a malicious LLM model there and “trick you to use it,” Zornshtain said. Bad actors can inject malicious code vulnerabilities into LLMs and, through social engineering, manipulate the output of specific LLMs, just to name two risks, he said.

Meanwhile, developers using open source packages or models should be responsible for the quality and safety of the LLM models they use, Zornshtain said. “That being said, as an industry providing those solutions, do we have the right controls in place? Not necessarily,” Zornshtain said. “We know where the safety concerns lie, but are those checks being performed today? Based on what we are seeing, the answer isn’t necessarily what we want.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)