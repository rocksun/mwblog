# New Tools Help LLM Developers Choose Better Pre-Training Data
![Featued image for: New Tools Help LLM Developers Choose Better Pre-Training Data](https://cdn.thenewstack.io/media/2025/05/88a7dd8c-choose-data-2-1024x576.jpg)
When developing a new [large language model (LLM)](https://thenewstack.io/what-is-a-large-language-model/), choosing the right training data is critical. “What you train your model on will determine completely different abilities,” [Ian Magnusson](https://www.linkedin.com/in/ian-magnusson/), AI researcher at the University of Washington and the [Allen Institute for AI (Ai2)](https://allenai.org/), told The New Stack.

An AI’s training data affects efficiency, bias and accuracy. “Poorly selected datasets can amplify biases, dilute task performance and require massive downstream corrections,” [Sreekanth Gopi](https://www.linkedin.com/in/s-gopi/), founder at NeuroHeart, told The New Stack.

With countless massive datasets, or corpora, to choose from, how do you know which will yield the best results? Testing thoroughly takes significant computing power, which quickly becomes cost-prohibitive. “As models grow larger, so does the cost of training them,” Gopi added.

“Pre-training LLMs, even smaller models, is resource-intensive across time and compute,” [Randall Hunt](https://www.linkedin.com/in/ranman/), CTO of the cloud native services company Caylent, an [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) partner, told The New Stack. “Accurate predictions of the [return on investment] on additional pre-training data can save on wasted model training runs.”

To solve this, in April, Ai2 released [DataDecide](https://allenai.org/blog/datadecide) — a suite of models, benchmarks and recommendations to guide dataset selection. “DataDecide is the most extensive openly available sweep of data decisions over scales and random seeds to date,” wrote Magnusson on the Ai2 blog.

The study found developers don’t need large budgets to make informed training data choices. Small-scale experiments can be surprisingly accurate. “You can make predictions about what will be the best choice using surprisingly little compute,” Magnusson told us.

## Testing Training Data: Usually Ad Hoc
To date, pre-training data decisions have involved a lot of trial and error. Almost everyone will use the [Common Crawl dataset](https://commoncrawl.org/), a publicly available archive of webpages, said Caylent’s Hunt. “After that, people tend to diverge depending on what they’re hoping the model will do.”

Others agree that data selection has been left to the user to figure out. “Despite the scale of modern models, the data selection process remains surprisingly ad hoc,” said Gopi. Teams often use open datasets without empirical testing, relying on intuition and past experience.

[Keith Pijanowski](https://www.linkedin.com/in/keithpij/), AI solutions engineer at [MinIO](https://min.io/?utm_content=inline+mention), an object storage system, told The New Stack that early training involves data scrubbing, vector database preparation and security checks on every document. In enterprise settings, it often starts with organizing internal data.
The most rigorous way to test pre-training data is to train at full scale, benchmark and repeat — but that’s not practical, said Magnusson. Instead, it’s far more cost-effective to run small-scale experiments before full training begins.

“It allows us to produce analysis, characterizing the relationship between the amount of compute to make a prediction about what pre-training dataset to train on,” he said.

To evaluate model performance, AI researchers use benchmarks like MMLU, ARC, HellaSwag, and SocialIQA to test LLMs across various tasks, like reasoning, mathematics, symbolic interpretation, social intelligence and more. Datasets that perform well in small-scale benchmarks often do well at scale. “You fit the relationship from that to how it performs on downstream tasks,” said Magnusson.

## Key Finding: Reduced LLM Training Costs
Ai2 tested DataDecide across a wide range of datasets and model sizes, using 10 benchmarks to evaluate how well small models predict large-scale performance. The findings aren’t earth-shattering, but they present useful takeaways for AI developers and researchers.

For one, Ai2 found that small models (around 150 million parameters) can predict large-scale outcomes with surprising accuracy. Some benchmarks reached over 80% decision accuracy using just 0.01% of the compute compared to billion-parameter models.

Since small-model experiments use less compute than other methods, developers don’t need to run full-scale tests just to predict outcomes. “The promise of this work is lower compute costs during training,” said Pijanowski.

Ai2 found that scaling laws didn’t outperform the simpler method of ranking datasets by small-model results. Scaling laws, a more sophisticated and more costly testing method, aim to predict how accuracy improves with model size. For now, “just stick with ablating things at one scale,” advised Magnusson.

The findings should give LLM devs pause for thought, Hunt said: “There are scaling laws that have been derived from empirical studies between data volume, compute resources and performance. Ai2’s research points out that we may want to revisit some of those assumptions.”

Compute needs vary widely by benchmark. In some cases, accuracy plateaus early, requiring far less compute than expected. For example, ARC Easy, a test with multiple-choice, grade-school level science questions, needs minimal resources. In contrast, HellaSwag, focused on reasoning and sentence completion, is far more demanding.

Ai2’s findings especially matter most for smaller labs and startups, where every GPU hour counts. “One of the most expensive stages in language model development has always been pre-training experimentation,” said Gopi.

## Selecting Datasets To Fine-Tune AI Tasks
Ai2’s research could also support fine-tuned model development. At this stage, data selection becomes a strategic concern, said Gopi. “In practical terms, selecting better data from the start reduces the need for complex fine-tuning and resource-intensive fixes later.”

It’s often assumed that more training data leads to better performance, but that’s not always true. Every LLM has trade-offs, and more training data can even deliver diminishing returns. That’s one reason [finely tuned, task-specific models](https://thenewstack.io/the-rise-of-small-language-models/) are on the rise. [Gartner predicts](https://www.gartner.com/en/newsroom/press-releases/2025-04-09-gartner-predicts-by-2027-organizations-will-use-small-task-specific-ai-models-three-times-more-than-general-purpose-large-language-models) small, specialized models will outpace large ones three-to-one by 2027.

“If an organization has multiple corpora to use for training LLMs and they do not have enough compute to train a 1-billion or more parameter LLM on all their corpora, then this research could help them pick the corpora that will produce the best results,” said Pijanowski.

DataDecide can help developers determine which data best serves a given LLM use case — whether for code completion, math, reasoning or artistic generation. “This helps us isolate what kind of information is most helpful for developing the ability in a certain task,” said Magnusson.

As a bonus, knowing exactly where your data comes from helps with enterprise compliance. “Training from scratch gives you confidence to make statements that what you trained on is grounded in a guaranteeable reality,” said Magnusson. “DataDecide helps you get a full picture of the benchmarks — and the trade-offs.”

## Does This Help Solve “Garbage In, Garbage Out?”
Smarter data decisions seem relevant to the classic problem of “garbage in, garbage out.” LLMs are often trained on petabytes of unstructured, open-ended data, making it hard to detect errors, misinformation, bias, other people’s intellectual property or harmful content (aka, the garbage).

Pijanowski noted that the Ai2 research helps address upstream concerns. “It could be used to perform an initial filter on a corpus or to conduct a series of small experiments to determine whether a certain collection of documents is good enough for LLM fine-tuning.”

However, DataDecide serves only one part of a bigger whole, noted Hunt: “This, combined with other training techniques, could be a boon, but it isn’t a magic fix.”

Gopi echoed that sentiment. “DataDecide makes it easier to avoid obviously poor data choices, but it doesn’t close the loop on deeper data quality concerns,” he said. Linking datasets to predictive outcomes doesn’t automatically translate to ethical or long-term value.

“What DataDecide does well is surface comparative utility early, enabling a triage system for pre-training inputs,” he added. “The classic ‘garbage in’ problem becomes less random, but not fully resolved.”

Developers can use DataDecide to identify which data supports their specific goals earlier in the pipeline. “DataDecide helps you evaluate evaluations, to make new evaluations that are sensitive to these differences in data,” said Magnusson. In a sense, it helps reverse-engineer which inputs actually matter by testing outcomes first.

## Blind Spots Remain
Choosing the right datasets for your pre-training data is a decision that carries significant consequences for the ultimate efficiency and accuracy of your LLM-derived apps.

“Model behavior is shaped more by its training data than architecture alone,” said Gopi. Irrelevant or redundant data can lead to inefficiencies and affect model quality, making training data descriptions an important yet often overlooked area for AI development.

Eliminating weak datasets early prevents wasted compute and accelerates innovation. Until now, though, developers lacked a reliable way to measure the quality of their training data choices. DataDecide fills that gap, helping standardize a once-informal step in model development.

Still, data selection alone doesn’t solve deeper problems around data quality or model architecture. “Dataset selection tools are one useful tool out of many needed tools,” said Hunt. “For genuinely more powerful models, we’ll need more architectural techniques than what we have right now.”

Pijanowski isn’t fully convinced: Why not just use [retrieval-augmented generation (RAG)](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/)? “This allows all corpora to be used without running everything through an LLM.”

In enterprise settings, he sees a major challenge in segmenting data into distinct corpora that reflect different skillsets a model must learn.

There is also the risk of over-optimizing for measurable benchmarks, said Gopi, which test scores rather than real-world performance. These metrics don’t always reflect behavior in open-ended, multilingual or adversarial contexts. “Without qualitative reviews, bias checks or representational analysis,” he said, “such tools can only partially mitigate data-related risks.”

While no single tool can solve all of AI’s challenges, DataDecide lowers the barrier to making pre-training decisions with far-reaching impact. As Hunt told TNS, “This doesn’t dramatically change things, but it is an exciting set of findings.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)