BERLIN, GERMANY — [SAP SE](https://www.sap.com/index.html?utm_content=inline+mention), the German business software giant, is hosting its annual TechEd event in Berlin this week, and it won’t come to anyone’s surprise that the company is putting a heavy emphasis on AI in its announcements. AI, after all, was already a focus of the company’s [flagship Sapphire conference](https://thenewstack.io/sap-unveils-new-ai-tools-for-developers/) earlier this. What may come as a surprise, though, is that SAP today announced its first foundation model: SAP-RPT-1.

The company calls SAP-RPT-1, which will become generally available later this year, the “first enterprise relational foundation model” because it was natively designed to help its users work with relational and structured business data. It’ll be available as both a small and larger model on the SAP platform later this year (though SAP did not yet disclose the sizes of these models yet), but also as an open-weight model [on Hugging Face](https://huggingface.co/SAP/sap-rpt-1-oss).

“We saw a gap in the industry,” Bharat Sandhu, SAP’s Chief Marketing Officer for the SAP Business Technology Platform (BTP), told me when I asked him about why the company decided to build its own model. Traditionally, LLMs are primarily trained on vast troves of unstructured data. Because of this, Sandhu noted, they tend to excel at predicting text but have a hard time doing math.

[![](https://cdn.thenewstack.io/media/2025/11/27e30d5c-architecture.png)](https://cdn.thenewstack.io/media/2025/11/27e30d5c-architecture.png)

Architecture diagram for the ConTextTab model that is now SAP-RPT-1 (Credit: SAP).

RPT (pronounced “rapid”)  stands for “relational pre-trained transformer,” and its focus is very much on predicting the results of common business scenarios, not the next word in a sentence. That has long been the domain of various deep learning and machine learning algorithms, but relational foundation models are currently a very active [area of research](https://openreview.net/forum?id=HNKZJJ8xQV) and it’s worth noting that there are a few startups like [Kumo](https://kumorfm.ai/get-started) that are also working in this space.

SAP’s research team actually published an in-depth paper about its research around AI and tabular data earlier this year. At the time, the model was still called [ConTextTab](https://arxiv.org/pdf/2506.10707). Unlike most model builders, SAP disclosed that it used the [Tremendous TabLib Trawl](https://huggingface.co/datasets/mlfoundations/t4-full) (T4) dataset to train its open-weight model model. This 1.34TB data set from Approximate Labs contains about 3.1 million tables that range from sports data to emissions data about Lithuanian industrial installations.

For the commerical model, SAP enriched the model with data from a much broader set of sources, which will likely make it more performant than the open model..

[![](https://cdn.thenewstack.io/media/2025/11/31cc8d96-1762270606187.jpeg)](https://cdn.thenewstack.io/media/2025/11/31cc8d96-1762270606187.jpeg)

Image credit: SAP.

Since SAP’s model was pre-trained for this use case, SAP argues that this new model will allow its customers to bypass any additional training or fine-tuning if they want it to reason over their structured data. Using in-context learning, SAP-RPT-1 can perform classification and regression on tabular data with a simple API call.

“The issue with traditional machine learning is that you’ve got to train the model,” Sandhu said. “You have to have the data. You have to make sure it’s not overly biased in one way or the other. You’ve got to train it, so it takes time and expertise. So RPT-1 is basically a generic relational model and can do these generic kinds of predictions and forecasting and everything else on tabular data.”

For users who want to give the model a try, SAP is launching a free web-based experience as well, dubbed the [SAP-RPT Playground](https://rpt.cloud.sap/) (though the file type is limited to CSV files up to a maximum of 2,073 rows and 50 columns). The examples there focus on many of the standard use cases that SAP expects for the model, like predicting upcoming maintenance needs, payment risk and customer churn.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)