# AI Is Coming to the Edge, but It Will Look Different
![Featued image for: AI Is Coming to the Edge, but It Will Look Different](https://cdn.thenewstack.io/media/2025/03/03da3105-ai-edge-1024x576.jpg)
The first working AI programs were developed some 70 years ago, but it wasn’t until cloud-based tools like ChatGPT hit the market that AI truly began to capture the imagination of both the business community and the public at large.

In 2024, McKinsey reported that [72% of enterprises](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) had already adopted AI. By early 2025, the analyst firm found that over the next three years, [92% of companies](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-at-work) are planning to increase their AI investments, many of them seeking a piece of the estimated $4.4 trillion in productivity growth AI is expected to bring. These data points show how ubiquitous AI has become — but challenges persist, from the risk of [data breaches](https://thenewstack.io/llm-integration-pitfalls-protecting-sensitive-data-in-the-ai-age/), concerns related to vendor lock-in, and limited control over the infrastructure, to issues with the speed at which data is transferred.

Edge AI achieves many of the same goals with a radically different approach: processing data closer to the source instead of using distant cloud servers.

But how does processing data closer to where it’s generated change the way AI operates, and which industries stand to benefit the most from this approach? What role will [small language models](https://thenewstack.io/the-rise-of-small-language-models/) (SLMs) play at the edge? In this article, I’ll look at the key advantages and potential drawbacks of deploying AI at the edge, along with an expert analysis of emerging trends that could shape its future adoption.

**Key Advantages of Deploying AI at the Edge**
When data processing is moved closer to the source through [edge computing](https://thenewstack.io/edge-computing/what-is-edge-computing/), it results in four key advantages: improved connectivity, reduced latency, more efficient data processing, and better security.

**1. Better Connectivity**
Connectivity is seldom an issue when AI is deployed at the edge, precisely because data processing is handled closer to the source, reducing reliance on internet bandwidth and the need for constant communication with the cloud.

**2. Reduced Latency**
Since edge AI processes data closer to the source, response times are significantly shorter, which is crucial when quick decision-making might substantially affect efficiency and safety.

**3. More Efficient Data Processing**
For organizations that handle large volumes of data, edge AI is the superior solution in many cases, as it reduces the need to transfer data to and from the cloud.

By processing data closer to its origin, organizations can filter information and send refined insights to central systems instead of overwhelming them with irrelevant data. This type of data collection and processing reduces bottlenecks, network congestion, and bandwidth costs while improving performance and efficiency.

**4. Improved Privacy and Compliance **
Capital One suffered a massive[ cloud-related breach](https://cert.europa.eu/publications/threat-intelligence/threat-memo-190802-1/pdf) in 2019, exposing the sensitive information of more than 100 million individuals. The bank relied on [Amazon Web Services (AWS)](https://aws.amazon.com/?utm_content=inline+mention) for cloud storage and computing, which the attacker exploited to gain access to clients’ financial and personal data.

Edge AI offers a security advantage in certain environments by operating in air-gapped or disconnected modes. In such configurations, where systems are not connected to external networks, the risk of cyberattacks and malware is reduced substantially. This approach is especially valuable in sectors like energy and manufacturing.

**How Businesses Can Leverage the Benefits of Edge AI Technology**
Edge management and orchestration platforms can help businesses take full advantage of edge AI, making it easier to support edge AI deployment and achieve operational goals more efficiently. To explore how this works, I spoke with [Padraig Stapleton](https://www.linkedin.com/in/padraigstapleton/), senior vice president of product and engineering at ZEDEDA.

![Inference at the edge vs in the cloud.](https://cdn.thenewstack.io/media/2025/03/78eb43f1-inference-edge-vs-cloud.jpeg)
Inference at the edge vs. in the cloud.

As a cloud native Software as a Service (SaaS)-based edge management and orchestration platform, ZEDEDA serves companies that operate in remote areas, such as those in the oil and gas industry that work in Scandinavia, across North America, the Middle East, and Latin America. It uses ZEDEDA’s edge computing platform to run apps on edge devices.

“Those apps include your traditional business apps, but also machine learning apps that are ingesting data directly from the edge, whether that’s at an oil drilling site or a solar farm. They’re processing the data on site and coming up with recommendations far faster than what it would take to transport and process that data in a data center,” said Stapleton.

Stapleton said security is the first topic ZEDEDA addresses in conversations with prospective clients. “In a lot of cases, our clients are dealing with very sensitive customer data, and they’re not willing to have it transported over the internet back to a cloud. So for them, the inference and all the AI has to be done at the edge,” he said.

Reduced latency is another major factor in choosing edge computing, as Stapleton explained: “You need to be able to look at the data and make a decision in pretty much real time, which you cannot do if you have to send it back to the cloud, get it processed and get the response back.”

**Drawbacks to Deploying AI at the Edge**
Of course, there are some drawbacks to deploying AI at the edge. They are primarily related to limited computational power and resource constraints, which can impact the efficiency of processing and make it challenging to handle resource-intensive tasks.

“If you have an AI model in the cloud, you typically have better access, better control, and a better ability to update the model. You likely have a larger data set available to you than at the edge, and you have more tools to retrain, update, and test the efficiency and accuracy of the model,” Stapleton noted.

Deploying AI at the edge can be a manual and time-consuming process, especially compared to the more centralized nature of [cloud computing](https://thenewstack.io/how-to-choose-the-right-cloud-cpu-for-your-workload/). Ideally, edge AI deployment would be as simple as pushing a button. One way to get the best of both worlds is to develop a model in the cloud and deploy it at the edge, but this isn’t always easy to achieve.

Platforms like ZEDEDA may aid organizations in getting to that point, but the inherent limitations of deploying AI at the edge — from limited hardware resources to scalability issues and data management challenges — cannot be ignored. Rather, they need to be embraced and dealt with.

Generally, the choice between edge AI and traditional cloud AI depends on specific use cases and requirements. What works for some organizations and industries may not be ideal for others.

**Emerging Trends: What AI Will Look Like at the Edge**
By 2028, [50% of AI workloads](https://www.techopedia.com/50-percent-ai-data-computing-on-edge) are predicted to happen at the edge, up from only 5% in 2023. Meanwhile, the[ hyperscale edge computing market](https://www.thebusinessresearchcompany.com/report/hyperscale-edge-computing-global-market-report#:~:text=It%20will%20grow%20to%20%2419.49,autonomous%20vehicles%20and%20smart%20cities.) is poised to grow at a compound annual growth rate of 34.2% and is projected to reach $19.49 billion by 2029.

There have also been [major advancements](https://www.microchipusa.com/industry-news/semiconductor-industry/the-intersection-of-ai-and-semiconductors-advancements-implications-and-future-opportunities/) in hardware development. Companies like [NVIDIA are creating specialized chips](https://thenewstack.io/after-deepseek-nvidia-puts-its-focus-on-inference-at-gtc/), such as the Jetson series, to deliver immense computing power to smaller, more energy-efficient edge devices. Neuromorphic chips (designed to mimic neural networks in the human brain) are emerging as well, alongside silicon photonics technologies and field-programmable gate arrays (FPGAs).

This proactive approach helps enforce safety protocols, allowing businesses to address potential risks in real-time.

According to Stapleton, there is a booming interest in edge AI in many industries, especially in oil, gas, and manufacturing. It’s primarily driven by the ongoing digitization and automation of manufacturing processes, where companies are looking to use edge AI to replace manual tasks and processes previously handled in the cloud.

“Think about stuff going through a manufacturing process. You have an app that’s basically checking whether that widget is of the right size, the right color, the right shape, the right density. And you want to be able to make that decision on the spot and detect whether it’s valid or not,” Stapleton said.

Some of ZEDEDA’s customers use edge AI and computer vision to validate workplace safety, with AI systems that monitor whether employees are, for example, wearing protective equipment. If an employee is found not wearing the necessary gear, the system can detect this and trigger an immediate response. This proactive approach helps enforce safety protocols, allowing businesses to address potential risks in real time.

**The Two Ecosystems Shaping the Future of Edge AI**
Looking ahead, there are two potential ecosystems that will shape the future of computer vision and AI at the edge.

The first is a hybrid model where edge systems remain connected to the cloud, allowing organizations to leverage cloud resources to train AI models, update them, and then deploy them at the edge. This offers flexibility, as the business app tends to remain static, while the model running and processing the data is updated frequently.

*“*Our clients want to evolve from this monolith, where they had the app and the model all tightly coupled, to one where they get loosely coupled and have a lot more flexibility in how they actually update the model going forward,*“* Stapleton noted.
The second type of emerging ecosystem is more vertical-centric. Companies in energy and critical systems, for instance, are reluctant to open up their network to the internet due to concerns about security and data privacy. This ecosystem revolves around air-gapped solutions, which enable training and deployment on premises within a secure environment.

*“*In this case, what we’re creating is a complete ecosystem where you can train models within the on-prem solution, deploy those models, monitor their outputs, and then feed everything back into a loop,*“* he explained.
Both of these models make sense because they cater to industry-specific needs. The hybrid model suits organizations that are comfortable leveraging the cloud for training and model updates and want to maintain a degree of flexibility. The on-premises, [air-gapped model](https://thenewstack.io/the-ultimate-guide-to-software-distribution/) is potentially a better option for industries with more pronounced security and data privacy concerns.

**The Role SLMs Will Play in Edge Computing**
SLMs are likely to play a role at the edge, especially in operational technology, as well as in the manufacturing, oil and gas, and automotive and transportation industries. These models, often derived from [large language models (LLMs)](https://thenewstack.io/llm/), will probably be used across different verticals, largely with a focus on providing knowledge and expertise at the edge not readily available today.

For now, the approach to AI in these industries is somewhat conservative, with machine learning deterministic models being used for computer vision and predictive maintenance. That may change in the near future, however, as more organizations explore workforce augmentation.

*“*Some industries will struggle with an aging workforce or the need to deploy equipment in locations that aren’t necessarily the most hospitable for people to work in,” Stapleton said.
“I see these models helping to augment their workforce, reducing the need for as much human intervention or participation in challenging locations. Technologies like SLMs trained for specific vertical use cases will allow them to do more, as the knowledge will be built into the models to assist staff, even in remote environments. I believe this is another trend we’ll see growing in the next few years,*”* he continued.

The best way … to leverage edge AI technology is to take a step back, identify practical use cases, focus on specific, manageable projects, and extrapolate knowledge from there.

Stapleton posited that new, disruptive technologies emerge roughly every 10 years. In the 2000s, it was the internet; in the 2010s, the cloud; and now, in the 2020s, AI seems to be the driving force behind the reorganizations taking place across various industries.

The problem is that it’s not always easy to distill reality from hype. The best way forward for organizations looking to leverage edge AI technology is to take a step back, identify practical use cases, focus on specific, manageable projects, and extrapolate knowledge from there. That is pretty much what ZEDEDA did with models like the Llama 3.1 8B model, which it integrated into its own in-house knowledge-sharing application, according to Stapleton.

“By doing that, we were able to create the first app based on LLMs that we’re using within the company. We’re going to use that as a model to start building other use cases, either for how we do our business internally or for things we can make available to our clients as part of our ecosystem. So, it’s very much a case of starting small, with a small team and a specific use case, and then building upon that knowledge to grow the use of these technologies within your organization,*“* he said.

**Solve Real-World Problems at the Edge**
Edge AI represents a transformative shift in how businesses approach data processing, offering distinct advantages over traditional cloud-based AI, such as reduced latency, improved security, and more efficient use of bandwidth.

Still, challenges remain, particularly when it comes to resource constraints and the complexity of managing AI at the edge. Companies like ZEDEDA can support businesses through these challenges, providing edge management solutions that can help facilitate the deployment and orchestration of edge AI.

ZEDEDA aims to eliminate manual processes, reduce deployment time, protect device health through real-time monitoring, simplify maintenance and large-scale deployments, and help manage distributed systems through a centralized platform.

Dedicated to bringing the cloud experience to the edge, ZEDEDA strives to accelerate [computer vision](https://zededa.com/solutions/enabling-computer-vision-at-the-edge/) deployments with a scalable and versatile platform that simplifies management while leveraging a zero-trust security model to provide robust protection against potential threats.

To learn more about ZEDEDA’s solutions, [request a demo](https://zededa.com/request-a-demo/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)