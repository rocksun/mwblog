When OpenAI unveiled Jalapeño, its first custom inference chip, in June, the company made some big promises. The chip, developed with Broadcom, was built from scratch for large language model inference, with OpenAI saying early testing showed substantially better performance per watt than existing accelerators. At the time, though, OpenAI didn’t release the detailed performance results to back that up.

On Tuesday, OpenAI published its first results from working Jalapeño silicon across GPT-OSS 120B, DeepSeek R1 and Kimi K2.5. The results show what OpenAI was aiming for with Jalapeño: higher throughput without the longer response times that can come with it.

> “Agents need to complete many steps in sequence, so delays can compound across an entire task.”

## Agents compound inference delays

An agent may call a model over and over as it works through a task, using tools and deciding what to do next based on the results, which means a delay that barely registers during a single inference can become much more noticeable when it happens repeatedly over the course of a longer task.

“Agents need to complete many steps in sequence, so delays can compound across an entire task,” OpenAI said.

Jalapeño was designed with those delays in mind. Different parts of running a large language model place different demands on the hardware, with the initial prompt requiring more compute and the response generation putting more pressure on memory bandwidth. Every time data has to move between cores and chips, that can add even more waiting.

Jalapeño takes a different approach, cutting down on that waiting without optimizing one part of the process at the expense of another.

“Agents need to complete many steps in sequence so that delays can compound across an entire task,” OpenAI said.

That helps explain some of the choices OpenAI made with Jalapeño. Running a large language model puts different demands on the hardware at different points: processing the initial prompt requires a lot of compute, while generating the response token by token relies more heavily on memory bandwidth. There’s also time lost whenever data has to move between cores and chips, leaving parts of the system waiting for what they need.

The idea is to reduce that waiting without optimizing one part of the process at the expense of another. Model state, including the KV cache used while generating a response, can be kept local, while Jalapeño’s networking allows more of the workload to stay within the same connected system. That means less time spent moving data around as the workload shifts between compute and memory.

## Jalapeño’s first public benchmarks

OpenAI put Jalapeño through InferenceX, SemiAnalysis’ public benchmark for AI inference, using GPT-OSS 120B, DeepSeek R1 670B, and Kimi K2.5 1T. Across the three models, Jalapeño handled 1.5 to 1.9 times more work per watt while cutting end-to-end latency by 1.7 to 3.6 times. On highly interactive workloads, OpenAI says it was 2.1 to 4.1 times faster than the systems it compared against.

The differences become particularly large when Jalapeño is compared at the previous best time-between-tokens operating point. OpenAI reported between 8.6 and 104.3 times more work per watt, depending on the model.

OpenAI based the power-efficiency comparisons on each accelerator’s published power rating. Jalapeño is rated at 700 watts, although the company says it never drew more than 550 watts during these tests. The bigger point is that OpenAI isn’t trying to improve throughput at the expense of response time, which is often the tradeoff with inference.

Batching more work can make infrastructure more efficient, but it can also mean making an individual user wait longer. OpenAI’s argument with Jalapeño is that an inference system increasingly needs to be good at both — particularly as the company [continues cutting the cost of API access](https://thenewstack.io/gpt-5-6-api-price-cuts/) while also needing to keep interactive workloads responsive.

> The bigger point is that OpenAI isn’t trying to improve throughput at the expense of response time, which is often the tradeoff with inference.

## AI-generated code runs faster

OpenAI used its own models throughout Jalapeño’s development, helping the hardware team move from initial design to tapeout in nine months by exploring implementations and shortening design, measurement, and verification cycles. The work didn’t stop once the chip was built.

The company says AI-generated implementations of selected GPT-OSS attention and mixture-of-experts blocks ran 1.5 to 1.8 times faster than versions written by its own experts. That doesn’t mean the entire model ran that much faster, but it does show what OpenAI is trying to do with Jalapeño: make the chip straightforward enough for AI, not just humans, to program and optimize.

Engineers describe work using local tensors, explicit communication and predictable synchronization, giving AI a way to help determine how that work should be mapped, placed and scheduled across the system. That could make it faster to adapt the chip as new models come along, although OpenAI says each new model family still requires its own kernels and optimizations.

## Custom silicon meets model roadmap

Using [Codex with GPT-Astra and earlier OpenAI models](https://thenewstack.io/codex-async-developer-messaging/), the hardware team brought three open-weight models that weren’t part of Jalapeño’s original production plan to high performance within two months. That fits with [OpenAI’s broader plans for Codex](https://thenewstack.io/openai-codex-cloud-evolution/), which the company has said is still early in its development, and shows how it could eventually play a role well beyond writing code.

OpenAI plans to start using Jalapeño in its own infrastructure by the end of the year, and it’s already working on the next two generations. The company will continue to use accelerators from Nvidia and other partners, but building its own chips gives OpenAI more control over how the hardware evolves alongside its models.

> OpenAI plans to start using Jalapeño in its own infrastructure by the end of the year, and it’s already working on the next two generations.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)