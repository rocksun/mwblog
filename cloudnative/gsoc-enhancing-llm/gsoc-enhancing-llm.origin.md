# Enhancing an Existing LLM Model with Domain-specific Jenkins Knowledge
[August 25, 2024](/blog/authors/nouralmulhem/)
Nour Ziad Almulhem
![Nour Ziad Almulhem](/images/avatars/nouralmulhem.jpg)
[Tweet](https://twitter.com/intent/tweet?text=Enhancing+an+Existing+LLM+Model+with+Domain-specific+Jenkins+Knowledge&url=https%3A%2F%2Fwww.jenkins.io%2Fblog%2F2024%2F08%2F25%2Fgsoc-enhancing-llm%2F)
Table of Contents
About the Project
JenAI is a pioneering chatbot that is trained specifically to answer users’s queries about Jenkins technologyÂ which enhance the accessibility and usability of software.

We aim to provide faster and more reliable assistance to our users. The model is integrated with a friendly UI to ensure a better user experience.

The project outcomes are:

-
Collected datasets from different sources, like

[Jenkins blogs](https://www.jenkins.io/blog/),[community questions](https://community.jenkins.io/c/using-jenkins/7). and other external sources -
Preprocessing this dataset to make sure it is clean and not confusing the model

-
Fine-tuning llama2 on this data and provide a new open-source fine-tuned modelÂ

-
Creating a user interface with a small server to interact with the model

-
Providing documentation of all the work done and a user guide to use our chatbot locally on your machine

Why JenAI:
-
Jenkins currently does not have AI-driven assistive technology to help Jenkins new users.

-
This project combines Jenkins knowledge with ai to assist all users with the knowledge that usually Jenkins expert has, providing a complete solution.

-
We empower users to interact with this knowledge through a smooth UI instead of looking for your answer here and there.

Milestones
This project included several stages that we have gone through:

Stage #1: data collection
Different sources were used to collect Jenkins knowledge, like [jenkinsÂ documents and blogs](https://www.jenkins.io/blog/), [discource community questions](https://community.jenkins.io/c/using-jenkins/7), and many external sources like [stack overflow](https://stackoverflow.com/), [ask ubuntu](https://askubuntu.com/), and [stack exchange](https://stackexchange.com/)

Stage #2: data preprocessing and refinement
This stage consisted of 3 parts:Â

-
The first one is utilizing another large language model to help us generate question-answer pairs out of Jenkins Documentations.Â

-
The second one is using stack exchange queries to get datasets of questions and correct solutions asked on stack overflow and many other platforms. We could define a score threshold for those questions and answers to ensure the reliability of the dataset we are collecting. The dataset generated includes HTML tags like paragraph code and many un-useful blocks or urls, so further processing was done to remove all useless information.Â

-
The last part of this is utilizing the community questions available on Discourse, where we could use

[discource apis](https://docs.discourse.org/)to prune Jenkins posts and retrieve ones with approved solutions, then we could do another request to retrieve those posts and their answers.
All those parts are automated, and the notebooks for creating the datasets are provided on our repository. In doing so, weÂ managed to collect around 4100 pairs; a bunch of which were used to fine-tune our model on.

Stage #3: JenAI as a system
This stage was about creating software with a friendly user interface as part of this project to interact with the model. We used ReactJs, Typescript, and MUI components to help us create the interface.

We also used Flask to create a small server with only one endpoint so far to interact with the model through Rest API and ensure smooth communication.

Stage #4: Fine-tuning
The core of our project, the effort of fine-tuning, was iterative and resumed until we made sure of its performance. A lot of research is conducted here to ensure the optimal parameters and the best approach to fine-tuning the model and obtaining accurate results.

We were using Colab and Kaggle free resources to fine-tune our model as they provide a T4 GPU with around 16 gigabytes of VRAM, which is pretty enough to load and fine-tune our model.

Details of fine-tuning, the approach, and parameters are provided in our [Final Documentation](https://github.com/nouralmulhem/Enhancing-LLM-with-Jenkins-Knowledge/blob/main/JenAi%20Final%20Document.pdf):

Stage #5: Convert the model to GGML format and quantization
In order to achieve our objective, we need users to be able to run the model on their local machines using only CPUs instead of hosting it. To achieve this, we used llama.cpp to convert the model to GGML binary format (using `convert_hf_to_gguf.py`
) that can be loaded and run on CPU.

Part of the appeal of the GGML library is being able to quantize this binary model into smaller models that can be run even faster. There is a tool called quantize in the Llama.cpp repo that can be used to convert the model to different quantization levels. We used the quantize tool to shrink our model to `q8_0`

Next Steps
This idea can be enhanced more, and many approaches are provided to achieve the same goal:

-
Using retrieval-augmented generation (RAG) that combines the strengths of databases or traditional information retrieval systems with the capabilities of large language models

-
Llama3 that has been pre-trained on over 15 trillion tokens, with a dataset used in training 7 times larger than the one used for training Llama2, which can make it outperform Llama2 when fine-tuning on Jenkins knowledge.

Acknowledgments
I want to take this chance and extend my gratitude to:Â

-
Google Summer of Code for organizing this and their mentors who provided help throughout the program.

-
Jenkins and GSoC org admins for having me contribute to this challenging problem and thank you for your flexibility along the way.

-
My team mentors

[Kris Stern](https://www.jenkins.io/blog/authors/krisstern/)(as a lead mentor),[Bruno Verachten](https://www.jenkins.io/blog/authors/gounthar/),[Harsh Pratap Singh](https://www.jenkins.io/blog/authors/harsh-ps-2003/), and[Shivay Lamba](https://www.jenkins.io/blog/authors/shivaylamba/)for their continuous support and guidance throughout the project, answering my questions and pointing out some great ideas so we are not left with something incomplete. They were a great reason for making this a success.