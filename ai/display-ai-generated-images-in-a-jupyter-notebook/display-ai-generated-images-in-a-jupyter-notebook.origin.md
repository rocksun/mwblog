# Display AI-Generated Images in a Jupyter Notebook
![Featued image for: Display AI-Generated Images in a Jupyter Notebook](https://cdn.thenewstack.io/media/2024/11/20d1e8e3-reefs-1024x576.jpg)
AI and its associated technologies, such as [OpenAI](https://thenewstack.io/beyond-chatgpt-exploring-the-openai-platform/), can make many processes effortless. With the right tools, you can transform thoughts into creative ideas, by turning text into generated images and storing them in the cloud using [Cloudinary](https://cloudinary.com), a digital media management tool.

OpenAI’s high-intelligence image API makes displaying an [AI-generated image](https://thenewstack.io/the-power-and-ethical-dilemma-of-ai-image-generation-models/) possible. The API provides ways to generate original images from scratch, edit an existing image based on a text prompt and create variations of an image. The model, DALL-E, is a neural network trained to create images from text descriptions. (Fun fact: The name DALL-E originated from combining the names of artist Salvatore Dali and the character Eve from the movie “WALL-E.”)

From content creation to marketing, advertising and design, there are lots of commercial and personal use cases for working with generated images. By using the OpenAI API, developers can create helpful text-to-image applications for users with the image generation endpoint.

In this guide, I’ll provide a detailed walkthrough on how to build an efficient image-generation app that is dynamic based on user input and displays the image output in a Jupyter Notebook.

**What Is Jupyter Notebook?**
[Jupyter Notebook](https://jupyter.org/) is a top choice for [Python](https://www.python.org/) users working in fields like machine learning, data science and data visualization. It’s a web tool where you can [create and share files with live Python code](https://thenewstack.io/mit-created-compiler-speeds-up-python-code/), equations, visuals and text. These files, called notebooks, [mix Python code](https://thenewstack.io/python/) with rich text elements like paragraphs, pictures and tables.
**What You’ll Need:**
You need to do the following setup:

- Install
[Python](https://www.python.org/downloads/)on your machine [Sign up](https://cloudinary.com/users/register_free)for a free Cloudinary account- OpenAI API key.
[Register](https://platform.openai.com/signup)for an account [Install Jupyter](https://docs.jupyter.org/en/latest/install/notebook-classic.html#alternative-for-experienced-python-users-installing-jupyter-with-pip)using the Python package manager pip
## Setting Up the Project
For this project, create a folder called `openai_proj`
and install these libraries.

`pip3 install openai python-dotenv cloudinary ipython jupyter`
Next, store your secret key in the environment variable file.

## Setting Up Environment Variables
Create a new [file](https://thenewstack.io/what-is-the-docker-env-file-and-how-do-you-use-it/) in your project directory called `.env`
and add your OpenAI API key and Cloudinary secrets as follows:

To access your credential values, go to your [OpenAI](https://platform.openai.com/settings/profile?tab=api-keys) and [Cloudinary](https://www.youtube.com/watch?v=ok9mHOuvVSI) dashboard.

## Creating the App
In your project directory terminal, run this command: `jupyter notebook`
to start the development environment on [http://localhost:8888](http://localhost:8888/).

Once in the environment, create a new notebook called `dalle`
by clicking the **New** menu dropdown button.

## OpenAI API Initialization
This script will securely load the API key from the `.env`
file.

The purpose of the `os.getenv`
function is to read the `OPENAI_API_KEY`
secret key value and set it up for use in the application.

Next, let’s initialize an instance of the OpenAI client by importing the OpenAI class from the [openai](https://pypi.org/project/openai/) module.

The OpenAI API is not free. Check the [pricing page](https://openai.com/api/pricing/) to determine the cost if you intend to use it and build your product. If you are a new user, OpenAI gives you free credits to use within the first three months.

## Cloudinary Configuration
Cloudinary is a cloud-based tool that provides an image and video API for storing, transforming, optimizing and delivering all your media assets with easy-to-use APIs, widgets or a user interface.

Let’s import the Cloudinary libraries.

### Set the Configuration Parameters
The values set for the configuration will read from the `.env`
for your Cloudinary secrets.

## Generating Original Images Using DALL-E 3
When generating an image, we will allow the user to enter their desired prompt using the [Python](https://thenewstack.io/what-is-python/) `input`
function. If they do not enter a prompt, the provided prompt will display an image when the user presses the enter key on the blank input.

The imports in the code above will display the image visually using the URL from the stored Cloudinary AI-generated image instead of showing only the URL of the image. The `requests`
library makes an HTTP request.

Within the `generate_image`
function code block, it accepts a prompt that conditionally accepts user input. It uses the [image generation](https://platform.openai.com/docs/guides/images/generations) endpoint to create an original image given a text prompt in the variable `response`
.

The property `n = 1`
instructs the model to generate only one image at a time.

Learn more about the other two parameters the [cloudinary.uploader.upload](https://cloudinary.com/documentation/python_quickstart#2_upload_an_image) function accepts, which takes the `image_url`
from DALL-E’s generated image model.

Finally, we set the output image to a specified width in the `srcURL`
variable that produces the Cloudinary image URL.

![Generated output image from OpenAI API: An underwater scene with vibrant coral reefs.](https://cdn.thenewstack.io/media/2024/11/5135f029-image1-1024x564.jpg)
Generated output image from OpenAI API

![Uploaded AI-generated images in Cloudinary. A variety of images.](https://cdn.thenewstack.io/media/2024/11/80c98cac-image2-1024x512.jpg)
Uploaded AI-generated images in Cloudinary

For the complete source code for the project, use [this gist](https://gist.github.com/Terieyenike/a75491834479a8eac3ff7beb59f6bdc8) or [this notebook](https://colab.research.google.com/drive/14P1g24FGxPsNqbJOA2NZ_ux-uQ_SLiLZ#scrollTo=bGj_nt2J1Lu4&uniqifier=1) in Google Colab.

**Conclusion**
Feeling inspired already? The OpenAI API has many built-in features that allow you to expand this project.

There are many use cases, and this tutorial showcased one way to generate a custom and personalized image with words. Also, Cloudinary gave it a finishing touch so that you can relive the memory of creating something extraordinary and store the image in a secure location in the cloud.

Discover how you can source cloud and Kubernetes specialists to accelerate project delivery in Andela’s white paper “[How DevOps Skills Are Evolving to Deploy Kubernetes in the Cloud](https://www.andela.com/resources/how-devops-skills-are-evolving-to-deploy-kubernetes-in-the-cloud/?utm_medium=contentmarketing&utm_source=whitepaper&utm_campaign=brand-global-the-new-stack-nov-20&utm_content=teri-eyenike-jupyter-blog-writers-room).”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)