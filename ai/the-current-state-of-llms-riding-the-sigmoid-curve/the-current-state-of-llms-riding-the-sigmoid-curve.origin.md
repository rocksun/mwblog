# The Current State of LLMs: Riding the Sigmoid Curve
![Featued image for: The Current State of LLMs: Riding the Sigmoid Curve](https://cdn.thenewstack.io/media/2024/08/e0b6a2da-graph-1024x574.png)
You might have noticed a shift in the air if you’ve been following the AI space lately. The unbridled optimism of a year ago has given way to a more somber, realistic outlook. As someone who spends most weekends knee-deep in AI code and has contributed to projects like [LangChain](https://python.langchain.com/v0.2/docs/integrations/toolkits/cassandra_database/) and [LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/), I’ve had a front-row seat to this transformation.

Recently, I attended two AI conferences — the AI Quality Conference and [AI Engineer World’s Fair](https://thenewstack.io/mozilla-llamafile-builders-projects-shine-at-ai-engineers-worlds-fair/) — and the change in sentiment was palpable. It felt like a significant milestone in the [AI journey](https://thenewstack.io/ai/), and I want to share my thoughts on where we are and where we’re headed.

## The Sigmoid Curve: A New Perspective on AI Growth
Remember when we thought AI growth was on an exponential curve, ready to leave us all in the dust? Well, reality had other plans. The AI community is now embracing a different model: [the sigmoid curve](https://news.ycombinator.com/item?id=40683845). This S-shaped curve suggests that after an initial period of rapid growth, progress starts to level off as we hit natural limitations.

Why the shift in perspective? It comes down to the constraints we’re facing in [large language model](https://www.datastax.com/guides/what-is-a-large-language-model?utm_medium=byline&utm_source=hackernoon&utm_campaign=LLM&utm_content=sigmoid) development.

## The Triple Threat: Data, Energy and Economics
First up is data availability. As massive as the internet is, there’s still a finite amount of high-quality data. Sure, companies like OpenAI are scrambling to make deals for more data to feed GPT-5, but what happens when we need 10x more for GPT-6? Synthetic data will help make up some of the gaps, but this is a hard reality to solve.

Then there’s the energy and infrastructure costs. [Training these behemoth models](https://thenewstack.io/nvidia-shaves-up-to-30-off-large-language-model-training-times/) requires an eye-watering amount of computational power. We’re talking racks upon racks of GPUs chugging away, generating enough heat to warm a small town. It’s not just expensive; it’s reaching the point of diminishing returns. In some cases, resource availability limits what’s even possible. The [new xAI data center](https://www.bloomberg.com/news/features/2024-07-25/in-memphis-elon-musk-s-xai-supercomputer-stirs-hope-and-concern) in Memphis, Tennessee, needs a staggering 1 million gallons of water a day and 150 megawatts of power. [Researchers](https://venturebeat.com/ai/new-transformer-architecture-could-enable-powerful-llms-without-gpus/) and [startups](https://www.theregister.com/2024/06/26/etched_asic_ai/) are looking to eliminate the GPU requirement, but it is still early days.

Last, there’s the economic viability question. Right now, large frontier models are being subsidized by deep-pocketed cloud providers. But as the true cost of LLMs becomes apparent, we might see a shift in the way these [models are developed and deployed](https://thenewstack.io/arrikto-ml-model-deployments-on-kubernetes-can-get-better/). Training a frontier model is a [billion-dollar club](https://www.washingtonpost.com/technology/2024/04/25/microsoft-google-ai-investment-profit-facebook-meta/) and requires Nvidia CEO Jensen Huang’s personal cell number.

## The AI Trust Crisis
As if these constraints weren’t enough, we’re also facing what’s called the “[AI trust crisis](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/#slide.032.jpeg).” This was a hot topic at the AI engineering conference. The problem? By design, LLMs tend to get … creative. This is great for writing the next great American novel but not for automating critical business processes. The disconnect is magical thinking about AI and a lack of understanding of the implementation. LLMs are a probabilistic model; they get lost in some cases.

I’ve seen this firsthand with some of our customers: trying to replace analytic processes by feeding large volumes of data into an LLM, or worse, trying to replace an entire job category by letting the LLM do the work unmonitored. Of course, neither of those ideas ended well, leaving the originators upset and with a negative opinion about the capabilities of new AI. Even the insiders realized that the transformer architecture [isn’t enough](https://www.sequoiacap.com/article/new-ideas-for-agi/), and we’re settling in at [GPT4](https://thenewstack.io/openais-gpt-4-can-analyze-visual-images-pass-bar-exam/)-level performance across all models. We’re one or two more breakthroughs away from trusted automation or everyone’s favorite buzzword, AGI (artificial general intelligence).

## Entering the Trough: Evidence From the Gartner Hype Cycle
If you’re wondering where we are in this AI roller coaster, look no further than the Gartner Hype Cycle. This trusty tool gives us a visual representation of technology maturity and adoption. I can’t embed the graph for the Gartner AI Hype Cycle due to licensing reasons, but I can link you to the [presentation](https://www.linkedin.com/video/live/urn:li:ugcPost:7222239254624530432/) that the Gartner folks did with plenty of graphics. It’s worth a few minutes of watching to see how your favorite new technologies stack up.

According to what Gartner is saying in the Hype Cycle for AI, foundation models and generative AI are headed into the “Trough of Disillusionment.” Don’t let the name fool you — this isn’t a bad thing. It’s a necessary step in the maturation of any technology. The early adopters get everyone excited, and power users find many of the early benefits. Late adopters start comparing more mature technology and find the sharp edges, declaring it “all hype” (I’m looking at you, enterprises). Eventually, there are things like support contracts, architecture diagrams and a host of products that make it all much more reliable and safe. Ahh, the dawn of enlightenment.

## The Sigmoid’s Silver Lining
Now, before you start thinking it’s all doom and gloom, let me assure you that this sigmoid curve and the “Trough of Disillusionment” have some serious benefits. If you are ready to trust the process, here are some things to feel good about.

**Time for adaptation**— As the pace of change slows down, organizations have a chance to catch their breath and figure out how to use these tools effectively. No more constant scrambling to keep up with the latest model that renders last week’s work obsolete. This is what keeps you from getting stuck in an endless POC and finally shipping something.**Improved risk management**— By clearly understanding AI’s capabilities and limitations, companies can make more informed decisions about where and how to implement these technologies. What even a little AI can do to your product and end-user productivity is amazing.**Strategic planning opportunities**— As the fog of hype clears, the path forward becomes easier to see. Companies can start planning their AI strategies with a more realistic view of future capabilities. Not too long ago, there was some crazy speculation about firing entire software engineering teams or all of marketing. AI will do it all, right? Now, it’s clearer that AI is a new skill set in those professions that increases productivity and adds new capabilities. Plan accordingly.
## The Current State of Play: From ‘Wow’ to ‘How’
So where does this leave us? If we look at the Gartner Hype Cycle, we see that while foundation models and GenAI are heading into the trough, other AI technologies are at different stages. Knowledge graphs, for instance, are finally pulling out of the trough, likely boosted by their usefulness in AI applications.

The key takeaway? AI isn’t going away, but it’s entering a phase of more measured, realistic progress. We’re moving from the “wow” phase to the “how” phase: How do we actually implement these technologies in a way that adds real value? My advice after absorbing our current state: Relax and get comfortable with what we have today. If you’re building a chatbot, you should be increasing your user’s productivity in some way. Otherwise, you’re just conducting more AI research.

## Looking Ahead
What can we expect as we ride this sigmoid curve? I believe we’re in for a period of consolidation and refinement. The gap between models is shrinking, with many leveling off at around GPT-4-level quality. This is great news for power users, who can now build on a more stable foundation.

We’re also likely to see a shift toward more focused, efficient models. The era of “bigger is always better” is coming to an end, replaced by a more nuanced approach that balances capability with efficiency.

While we may not be racing toward AGI at breakneck speed, we’re entering a phase that could be even more exciting. It’s a time of practical innovation, where the real-world impact of AI will start to become clear. So buckle up, fellow AI enthusiasts. The ride might be smoother than expected, but it’s far from over.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)