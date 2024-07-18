# The Critical Path to Superalignment as AI Invades the Enterprise
![Featued image for: The Critical Path to Superalignment as AI Invades the Enterprise](https://cdn.thenewstack.io/media/2024/07/a7f3c072-tree-3095703_1280-1024x682.jpg)
The concept of “superalignment,” once a niche topic confined to science fiction and academic computer science, entered everyday conversation after OpenAI disbanded its superalignment team.

Superalignment aims to ensure that future superhuman AI systems adhere to human ethics and objectives — an undeniably laudable ambition. However, much like prioritizing the improvement of automobile safety before designing seatbelts for intergalactic spacecraft, the [immediate concern](https://thenewstack.io/entrepreneurship-for-engineers-why-team-alignment-matters/) should be what we term “Enterprise Alignment”: [ensuring AI functions accurately](https://thenewstack.io/yes-orchestration-is-for-ai-too/) and safely, and can be audited and scaled in critical business environments.

Let’s [get chatbots to function](https://thenewstack.io/building-smarter-chatbots-with-advanced-language-models/) without saying noncompliant or inaccurate things before worrying about curtailing SkyNet.

**The Challenge of Enterprise Alignment**
The Snorkel team has worked on weak-to-strong generalization (the technical foundation of superalignment) at the Stanford AI lab since 2015. Our experience with [enterprise AI teams](https://thenewstack.io/enterprise-ai-requires-a-lean-mean-data-machine/) today shows that enterprises need help aligning current, non-superhuman production-quality generative AI systems with organizational standards, ethics and objectives.

[Labeled data](https://thenewstack.io/the-new-face-of-data-quality-anomalo-and-automated-monitoring/), specifically preference data, where humans rank LLM responses as acceptable or not (or give other similar forms of feedback), is key to enterprise alignment.
We see leading banks, tech companies and other enterprises collecting data on user responses to their AI models and manually labeling whether each response is acceptable. This laborious “thumbs up, thumbs down” approach is highly tedious, challenging and inefficient at the enterprise scale.

These manual processes lead to bottlenecks and delays, making it difficult for enterprises to adapt to rapidly changing policies and regulations. For example, during the COVID-19 pandemic, policy exceptions and changes were frequent, requiring constant updates to AI model training data. Enterprises found it challenging to adjust their models to reflect these changes quickly manually.

Efforts from large technology companies and LLM providers, using approaches such as Reinforcement Learning from Human Feedback (RLHF), have relied heavily on large volumes of manually annotated data. This process, often involving outsourced gig workers, is prohibitively costly and inefficient for most enterprise settings. Practical enterprise alignment — for example, the alignment of custom LLMs to custom, domain-specific objectives and policies — is effectively blocked on the data.

One large tech company we collaborated with found its manual labeling process unsustainable as its user base grew. By adopting programmatic data development, it was able to scale its operations without a proportional increase in manual labeling efforts. This improved its AI’s performance and allowed it to respond to policy changes swiftly and effectively.

I’ve talked with many senior IT leaders, and their experiences suggest that enterprises just beginning their AI alignment journey should avoid trying to label everything manually. Even if you outsource that work, you’ll create technical debt through static datasets that can’t evolve. Programmatic data development future-proofs your alignment capabilities**.**

**Programmatic Data Development: The Key to Enterprise Alignment**
In recent research, the team at Snorkel has shown that it can rapidly apply programmatic data development to align LLMs to custom, domain-specific policies and objectives. We validated this approach on three enterprise-specific tasks, showing substantial improvements with under five hours of programmatic data development each:

**Financial services:**We aligned a compliance-aware GenAI application to financial advisers’ professional and ethical standards, improving the proper response rate to noncompliant requests by 20.7 accuracy points over an off-the-shelf solution — the result: an enterprise-aligned, 99% compliant financial adviser chatbot.**Insurance**: We aligned a claim coverage AI assistant to an automotive insurance policy, improving the rejection of invalid claims by 12.3 accuracy points to 98% with virtually no impact on valid claims. We also provided clear explanations for why a claim was rejected based on the applicable policy.**Health care**: We aligned a chatbot to the specific policies of the health-care provider to achieve a near 20-point lift for assessing policy adherence in interactions with users.
These successes underscore the potential of a programmatic approach, which empowers subject matter experts to encode organizational policies into preference datasets efficiently. The key to this approach is a structured, programmatic workflow that efficiently enables subject matter experts to encode domain — and enterprise-specific policies into datasets.

Imagine the analogy of transitioning from manual coding in binary to using high-level programming languages. Initially, every single step had to be meticulously coded, but with higher-level abstractions, complex functions can be implemented more efficiently and with fewer errors. Similarly, programmatic data development allows for higher-level, more abstract ways of encoding and updating AI models, making the process faster and more reliable.

**Accelerating Time-to-Value for Enterprise AI**
Beyond improving alignment accuracy, programmatic data development techniques enable AI teams to unlock value far more rapidly than traditional approaches. Empowering subject matter experts to encode their domain knowledge directly vastly reduces the need for repeated feedback loops between developers and SMEs.

“In our previous manual annotation process, it would often take months just to get an initial model trained due to all the back and forth,” recalled one AI program manager at a major manufacturing company. “With programmatic data development, our compliance lead could basically ‘write’ the policy rules directly into the training data in an afternoon. We went from model conception to production in less than a week.”

**The Road to Enterprise Superalignment**
The ultimate goal extends beyond immediate enterprise alignment to enterprise superalignment — ensuring future, more powerful AI systems align with organizational standards. This journey starts with practical, incremental steps. By addressing current challenges in enterprise settings, we pave the way for broader super alignment objectives.

Programmatic approaches provide the speed and repeatability necessary for today’s dynamic business landscapes and allow for rapid adjustments as enterprise policies evolve. This adaptability ensures that AI systems remain aligned with organizational changes without requiring extensive rework.

While developing advanced safety systems for hypothetical flying saucers is admirable, the real-world necessity lies in enhancing AI alignment in current enterprise settings. There is optimism about AI’s transformative potential and a commitment to bridging the gap between theoretical advancements and practical, production-ready AI solutions.

There is a pathway to accelerate data science and machine learning initiatives for organizations looking to leverage generative AI and achieve high-quality LLMs. By exploring programmatic data development techniques, enterprises can drive value and efficiency in their AI endeavors.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)