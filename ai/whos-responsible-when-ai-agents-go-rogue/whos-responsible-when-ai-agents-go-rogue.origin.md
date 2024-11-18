# Who’s Responsible When AI Agents Go Rogue?
![Featued image for: Who’s Responsible When AI Agents Go Rogue?](https://cdn.thenewstack.io/media/2024/11/ad6f6fc8-alessio-ferretti-upwjvq8cjry-unsplash-1024x604.jpg)
[Alessio Ferretti](https://unsplash.com/@ilferrets?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/a-strange-looking-object-with-eyes-and-a-nose-upwjVq8cJRY?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
Whether you’re in the tech world or enjoying dinner with your family, there’s no escape from AI these days. Many of us have been through several cycles of AI’s evolution, and every new growth stage evokes many questions about how we got here and where we are headed. Years ago, when building the ML products at ARM, we faced many of these questions as well, and it was pretty clear how innovation and independence of AI are deeply interwoven concepts.

Fast forward to today in the Age of AI, and while we haven’t been taken over by Skynet just yet, there is a growing concern across people, businesses, and societies about the new attack surface that has recently opened up with the latest phase of widespread Gen AI adoption. Whether you’re worried about [deep-fake driven social engineering attacks](https://thenewstack.io/why-ai-cant-protect-you-from-ai-generated-attacks/), [AI-powered phishing attacks](https://hbr.org/2024/05/ai-will-increase-the-quantity-and-quality-of-phishing-scams), or [prompt injection attacks](https://thenewstack.io/top-9-api-security-vulnerabilities-how-to-defend-against-them/), there are real reasons to be concerned about the new risks lurking in AI application stacks; after all, AI doesn’t live in a vacuum — it is integrated into the heart of the application stack at every layer, processing vast amounts of data, including highly sensitive data, and exchanging that data with all sorts of third parties, whether it’s AI APIs like OpenAI or homegrown models from Hugging Face.

Despite AI’s faults, there’s no denying its massive promise regarding productivity and innovation. Although imperfect, AI agents are about to become much more prevalent. According to a [Capgemini survey](https://www.capgemini.com/insights/research-library/generative-ai-in-organizations-2024/), 82% of tech executives “intend to integrate AI-based agents across their organizations within the next three years — up from 10% with functioning agents at the current time.”

As AI agents become more widespread, the potential for danger grows across important industries that use them. In light of this, C-suite executives face a critical question: Who’s responsible when AI goes rogue?

**AI Accountability: A Shifting Landscape**
The proliferation of AI is shaking up the organizational structure of modern enterprises. A [Pearl Meyer report](https://pearlmeyer.com/press-releases/pearl-meyer-survey-shows-companies-are-taking-steps-to-introduce-ai-in-the-workforce) revealed that 30% of companies have opted to bake AI-related responsibilities into existing executive roles. Meanwhile, “32% are taking a decentralized approach to AI oversight and expect AI efforts to be led by various leaders across multiple functions.”

In most organizations today, CISOs, CIOs, and CTOs bear the brunt of responsibility for AI’s behavior and security. This can create tension between the different leadership roles since CISOs don’t have control over AI systems, yet they’re tasked with maintaining security.

Since AI is a shared responsibility, organizations must adopt strategies and tools that clearly define accountability while bridging the gap between the different areas of leadership.

**Bringing Transparency to the ‘Black Box’ of AI**
Transparency is a significant first step towards accountability. As an engineer, I’m innately joyous when deconstructing how systems work. Bridging the worlds of Operating Systems and encryption, I’ve learned how transparency and trust are established between these complex software systems.

But it is not a trivial ask for those in the AI development trenches. Traditional software engineering leans towards deterministic systems that rely on predefined rules that can be written and audited. In contrast, modern probabilistic Gen AI systems make (often unpredictable) predictions based on their complex and multidimensional calculations of likelihoods. Probabilistic systems, by their very nature, are not transparent.

So, if an AI agent goes rogue and can’t explain its decisions, determining what went wrong can be challenging (if not impossible). So, how do the leaders in charge of AI systems get as much transparency and control as possible in this imperfect world?

AI is only as good as the data that fuels it — “garbage in, garbage out,” as the adage goes — so keeping clear records of which training [data is feeding the model](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/) is key. Scrubbing and redacting as often as possible to protect private information that may be intentionally or unintentionally swept up into its modeling is also key.

When AI is deployed via AI APIs, teams must have a complete picture of how their data and application behavior interact with the external entity (such as Open AI). They need to understand what [data is expected to flow through the model](https://thenewstack.io/nosql-data-modeling-mistakes-that-ruin-performance/) (and what data isn’t) and have real-time access to how their live AI agents are operating so that unexpected behavior can be caught and blocked instantly before they have a chance to steal data or take down the entire system.

**Enhancing Human Oversight With Technology**
Some believe that humans need to interact with AI to keep it accountable, but how do we keep human oversight from becoming a roadblock to innovation?

Designing AI to interact with [human experts to enhance their capacity instead of replacing](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/) them is a good starting point. Then, teams must use technology to proactively limit access to AI agents to reduce or eliminate the consequences of rogue mayhem.

Just like we enforce zero trust in a cybersecurity context so that access controls and privileges are assigned to specific individuals based on a secure “[least privilege](https://www.cisa.gov/zero-trust-maturity-model)” model, so too should “least privilege” logic be applied to AI agents. That way, the AI agent is assigned tasks can be contained, and the attack surface will be reduced. At the same time, human oversight at key junctures offers crucial transparency and control to the teams and leaders who are ultimately responsible for their actions.

The AI revolution is well underway, yet we’re still just at the beginning. Organizations must establish who is responsible for AI’s behavior, whether that means bridging the gap between CISOs, CIOs, and CTOs or hiring an entirely AI-focused executive. By establishing accountability, increasing transparency, and using technology to enhance human oversight, companies will be well-positioned to reap the benefits of AI and drive innovation safely and securely.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)