# ML and LLM Adoption Challenged Most Often by Observability
![Featued image for: ML and LLM Adoption Challenged Most Often by Observability](https://cdn.thenewstack.io/media/2025/03/5fad52d3-olivie-strauss-xuuuktvxv7a-unsplashb-1024x576.jpg)
Observability and monitoring is the most cited challenge when moving ML models into production. [The Institute for Ethical AI & Machine Learning](https://ethical.institute/index.html) conducted a [survey on the state of production ML](https://docs.google.com/forms/u/2/d/e/1FAIpQLSfY7kqfD1YJOW1KwsYr1VYzjn_ONdUVQ71xkgsz2rsulHrJ6Q/viewanalytics) in the fourth quarter of 2024. The other key takeaway is that custom-built tools dominate user roadmaps, since few vendor tools have gained significant traction.

Overall, 44% of the 170 practitioners surveyed were machine learning engineers with about the same amount identifying as a data scientist or a MLOps engineer. Many of the respondents are subscribers to [Alejandro Saucedo’s](https://www.linkedin.com/in/axsaucedo/overlay/about-this-profile/) [The ML Engineer newsletter](https://www.linkedin.com/newsletters/6882216044568571904/).

Only 7% say that ML security is one of their top three challenges and only 17% say the same about governance and domain risks. That finding is significantly different from what we’ve seen in other studies, where security and AI governance are cited as among the biggest obstacles to increased adoption. We believe the practitioners view ML security as pertaining just to the ability of a model to be hacked, while other IT decision-makers worry more about general access to corporate and personal data.

It seems like every enterprise is at least experimenting with generative AI and AI agents that rely on [large language models](https://thenewstack.io/llm/) (LLMs). At the same time, the adoption of predictive analytics and computer vision continues to grow. As these applications scale up, developers require data engineers, SREs and others to handle Day 1 and [Day 2 challenges](https://thenewstack.io/cloud-native-day-2-operations-why-this-begins-on-day-0/). Rising to the challenge, [MLOps](https://thenewstack.io/what-is-mlops/) became a real discipline, followed by LLMOps and [GenAIOps](https://thenewstack.io/microsoft-sees-devs-embracing-a-paradigm-shift-to-genaiops/).

Regardless of the terminology used, [LLM observability and monitoring](https://thenewstack.io/what-is-llm-observability-and-monitoring/) is something that has to be addressed.

## Custom-Built vs. Vendor Tools
The survey asked about nine different parts the technology stack needed to utilize AI and machine learning. Here are some noteworthy findings:

- A managed model or LLM API service is used by 65% of the survey use. Among those that use this type of service,
[OpenAI](https://thenewstack.io/openais-realtime-api-takes-a-bow/)(38%),[AzureAI](https://azure.microsoft.com/en-us/solutions/ai/)(20%) and[Amazon Bedrock](https://thenewstack.io/amazons-bedrock-can-now-check-ai-for-hallucinations/)(12%) were used most often. [MLflow](https://mlflow.org/)is the leader for. Among those that have adopted these tools, 48% use MLflow most often. Custom built tools (16%) and Weights & Biases (12%) were the next most used tools in this category. Note that CoreWeave, which itself just had an IPO, recently announced its acquisition of Weights & Biases.*model registry and/or experiment tracking*- Among users of
, 40% use*ETL / workflow orchestrators*[Airflow](https://thenewstack.io/how-apache-airflow-better-manages-machine-learning-pipelines/)most often. Custom-built tools (17%) and[Argo Workflows](https://argoproj.github.io/workflows/)(11%) were the next most used tools in this category. - Among users of
, 46% use FastAPI/Flask Wrapper most often. Data scientists were more likely to use this tool (70%). Custom-built tools (16%) and*real-time model serving*[AWS SageMaker](https://thenewstack.io/address-common-machine-learning-challenges-with-managed-mlflow/)(12%) were the next most used tools in this category.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)