# Open Source Library Taipy Turns AI Algorithms, Data into Web Apps
![Featued image for: Open Source Library Taipy Turns AI Algorithms, Data into Web Apps](https://cdn.thenewstack.io/media/2024/03/9ed80d32-python-1024x684.jpg)
A free open source Python library allows developers to turn data and AI algorithms into production-ready web applications. Called
[Taipy](https://github.com/Avaiga/taipy), the library is designed to support data science and machine learning engineers in building full-stack apps.
The
[startup](https://www.taipy.io/) was founded by [Vincent Gosselin](https://www.linkedin.com/in/vincent-gosselin-5011559/?originalSubdomain=fr) and [Albert Antoine](https://www.linkedin.com/in/albert-antoine-7a5a673/), both of whom are veterans of the technology world. Gosselin, who is CEO, spent eight years in IBM’s Data Science and Advanced Analytics, along with heading advanced analytics at DecisionBrain. Antoine, the executive director of Taipy, was the CEO at data analytics firm Avaiga.com and worked in business development at Dataiku, a data science platform.
”The problem they wanted to address when creating Taipy is the failure rate of projects in the data space,” explained
[Rym Michaut](https://www.linkedin.com/in/rymguerbi/recent-activity/all/), a data scientist and Taipy’s global community manager, in a written response to The New Stack. “Most of these projects are written in Python. That’s why we moved on from Java to Python.”
## Taipy’s Three Components
Developers do not need any prior knowledge of HTML,
[JavaScript](https://thenewstack.io/2024-predictions-by-javascript-frontend-framework-maintainers/), or [CSS](https://thenewstack.io/tailwind-css-for-developers-style-without-using-css-code/) to use Taipy, but do need a basic understanding of Python.
The tool is composed of three components, starting with Taipy frontend for building out a Graphical User Interface using simple Markdown language to create interactive pages with graphical elements, according to the
[Taipy FAQ](https://www.taipy.io/company/faq).
“Devs have a lot of control over look and feel,” Michaut said. “We provide a default CSS style to all our apps and UI components, but these can be modified through Python or CSS code. Our main strength in terms of look and feel is the layout: We provide an easy syntax to customize the design of your app, and we also have a
[VS Code](https://thenewstack.io/how-to-use-vs-code-as-your-python-ide/) extension that allows you to preview your page’s design without running Python code.”
She acknowledged that while the library is customizable, the “default layout and look might be less impressive than other, less customizable libraries,” she said. To give developers an idea of a real-world application to build with Taipy, she shared a
[financial forecasting dashboard mockup](https://pl-dashboard.taipy.cloud/group_contributions) completed for a company. ![App mockup made with Taipy.](https://cdn.thenewstack.io/media/2024/03/382f65c3-taipy-mockup.png)
App
[mockup](https://pl-dashboard.taipy.cloud/group_contributions) made with Taipy, courtesy Taipy.
In the coming months, Taipy plans to release a new low-code offering that will allow users to edit frontends without coding using drag-and-drop UI components from a web interface.
Taipy backend is for building and managing data flows, including pipelines that can call upon your code. It can schedule tasks, cache repetitive operations, and parallelize tasks “to optimize performance and streamline management of pipelines and scenarios,” the FAQ stated. “The primary aim of Taipy backend is to translate standard Python code and enhance pipeline and scenario performance and management,” it added.
The third component, Taipy Rest, provides a way to access scenarios, pipelines, and data accessors through a Rest API.
“Taipy also focuses on working in full-scale production applications: As we run the minimum necessary tasks on a user interaction using what we call the callbacks, front end and back end run on different threads so the user can still interact with the app even if a model is running in the background,” Michaut explained.
Taipy can connect by default to pickle, CSV, Excel, JSON, Mongo, SQL and Parquet.
“Of course, if you can connect to a data source using Python, it will also work within Taipy using a few lines of code,” she added.
There’s also documentation for connecting to
[AWS](https://thenewstack.io/bringing-the-aws-serverless-strategy-to-azure/) and [DataBricks](https://thenewstack.io/databricks-sees-and-raises-snowflake-with-gen-ai-llmops-more/).
## Integration with Existing Data Science, ML Libraries
The New Stack asked Michaut if Taipy can handle large datasets and complex machine learning models efficiently and how easily it can integrate with existing data science and
[machine learning libraries](https://thenewstack.io/ai-ml-best-practices-during-a-gold-rush/), such as [scikit-learn](https://scikit-learn.org/stable/), [TensorFlow](https://thenewstack.io/tutorial-deploying-tensorflow-models-with-amazon-sagemaker-serverless-inference/) or [PyTorch](https://thenewstack.io/pytorch-takes-ai-ml-back-to-its-research-open-source-roots/).
“Yes, Taipy can handle large datasets and
[ML algorithms](https://thenewstack.io/ml-engineer-teaches-graph-algorithms-with-dungeons-dragons/) efficiently by integrating other libraries,” she responded. “Since our library mainly focuses on the frontend, we do not interfere with anything that can be written with [Python code](https://thenewstack.io/what-is-python/). Taipy calls the different libraries you need to run your ML algo inside a web page and interacts with it directly. You can, for example, change model parameters from a Taipy interface, run the model using a button and visualize results within a Taipy webpage.”
It also provides features that allow the user to visualize and interact with large datasets in real-time. One such feature is the decimator, which reduces the number of points on a chart that least modify the curves, she explained. “We also have features to run ML models in parallel or on distribute clusters,” she added.
## The Goal: Ease of Use Plus Scalability
We also asked how Taipy compares to other, similar frameworks, such as
[Streamlit](https://streamlit.io/), [Dash](https://dash.plotly.com/) or [Flask](https://flask.palletsprojects.com/en/3.0.x/). Taipy’s goal is to hit a sweet spot of ease of use and scalability that these solutions don’t, Michaut said.
“We found that the Python graphical package scene is split between two poles: On the one side, tools like Streamlit are easy to use but do not scale to production applications. They often fail when confronted with multiple pages/users or large datasets/computations,” she stated. “On the other hand, tools like Dash are scalable but have a steep learning curve. We saw a gap in the market and we seized it.”
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)