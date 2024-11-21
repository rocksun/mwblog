# 在Jupyter Notebook中显示AI生成的图像

![Featued image for: Display AI-Generated Images in a Jupyter Notebook](https://cdn.thenewstack.io/media/2024/11/20d1e8e3-reefs-1024x576.jpg)

AI及其相关技术，例如[OpenAI](https://thenewstack.io/beyond-chatgpt-exploring-the-openai-platform/)，可以使许多流程变得轻松。使用合适的工具，您可以将想法转化为创意，通过将文本转换为生成的图像并使用数字媒体管理工具[Cloudinary](https://cloudinary.com)将其存储在云中。

OpenAI的高智能图像API使得显示[AI生成的图像](https://thenewstack.io/the-power-and-ethical-dilemma-of-ai-image-generation-models/)成为可能。该API提供从头开始生成原始图像、根据文本提示编辑现有图像以及创建图像变体的方法。该模型DALL-E是一个经过训练可以根据文本描述创建图像的神经网络。（有趣的事实：DALL-E这个名字来源于艺术家萨尔瓦多·达利和电影《机器人瓦力》中伊娃的名字组合。）

从内容创作到营销、广告和设计，使用生成的图像有很多商业和个人用例。通过使用OpenAI API，开发人员可以使用图像生成端点为用户创建有用的文本到图像应用程序。

在本指南中，我将详细介绍如何构建一个基于用户输入的动态高效图像生成应用程序，并在Jupyter Notebook中显示图像输出。

**什么是Jupyter Notebook？**

[Jupyter Notebook](https://jupyter.org/)是从事机器学习、数据科学和数据可视化等领域的[Python](https://www.python.org/)用户的首选工具。它是一个Web工具，您可以在其中[创建和共享包含实时Python代码](https://thenewstack.io/mit-created-compiler-speeds-up-python-code/)、方程式、视觉效果和文本的文件。这些文件称为notebook，[将Python代码](https://thenewstack.io/python/)与丰富的文本元素（如段落、图片和表格）混合在一起。

**您需要什么：**

您需要进行以下设置：

- 在您的机器上安装[Python](https://www.python.org/downloads/)
- 注册[Cloudinary](https://cloudinary.com/users/register_free)免费帐户
- OpenAI API密钥。
- 注册[OpenAI](https://platform.openai.com/signup)帐户
- 使用Python包管理器pip安装[Jupyter](https://docs.jupyter.org/en/latest/install/notebook-classic.html#alternative-for-experienced-python-users-installing-jupyter-with-pip)


## 项目设置

对于这个项目，创建一个名为`openai_proj`的文件夹，并安装这些库：

```bash
pip3 install openai python-dotenv cloudinary ipython jupyter
```

接下来，将您的密钥存储在环境变量文件中。

## 设置环境变量

在您的项目目录中创建一个名为`.env`的新[文件](https://thenewstack.io/what-is-the-docker-env-file-and-how-do-you-use-it/)，并添加您的OpenAI API密钥和Cloudinary密钥，如下所示：

要访问您的凭据值，请访问您的[OpenAI](https://platform.openai.com/settings/profile?tab=api-keys)和[Cloudinary](https://www.youtube.com/watch?v=ok9mHOuvVSI)仪表板。

## 创建应用程序

在您的项目目录终端中，运行此命令：`jupyter notebook`，以在[http://localhost:8888](http://localhost:8888/)上启动开发环境。

进入环境后，通过单击**新建**菜单下拉按钮创建一个名为`dalle`的新notebook。

## OpenAI API 初始化

此脚本将安全地从`.env`文件中加载API密钥。

`os.getenv`函数的目的是读取`OPENAI_API_KEY`密钥值并将其设置为可在应用程序中使用。

接下来，让我们通过从[openai](https://pypi.org/project/openai/)模块导入OpenAI类来初始化OpenAI客户端的实例。

OpenAI API不是免费的。如果您打算使用它并构建您的产品，请查看[价格页面](https://openai.com/api/pricing/)以确定成本。如果您是新用户，OpenAI会在前三个月为您提供免费积分。

## Cloudinary 配置

Cloudinary是一个基于云的工具，它提供图像和视频API，用于存储、转换、优化和交付所有媒体资产，并提供易于使用的API、小部件或用户界面。

让我们导入Cloudinary库。

### 设置配置参数

为配置设置的值将从您的Cloudinary密钥的`.env`中读取。

## 使用DALL-E 3生成原始图像

生成图像时，我们将允许用户使用[Python](https://thenewstack.io/what-is-python/)的`input`函数输入他们想要的提示。如果他们没有输入提示，则当用户在空白输入上按下回车键时，提供的提示将显示图像。
以上代码中的导入语句将使用存储的Cloudinary AI生成的图像的URL以可视方式显示图像，而不是仅显示图像的URL。`requests`库发出HTTP请求。

在`generate_image`函数代码块中，它接受一个条件性地接受用户输入的提示。它使用[图像生成](https://platform.openai.com/docs/guides/images/generations)端点根据变量`response`中的文本提示创建原始图像。

属性`n = 1`指示模型一次只生成一张图像。

了解更多关于[cloudinary.uploader.upload](https://cloudinary.com/documentation/python_quickstart#2_upload_an_image)函数接受的其他两个参数的信息，该函数接收来自DALL-E生成的图像模型的`image_url`。

最后，我们将输出图像设置为`srcURL`变量中指定的宽度，该函数生成Cloudinary图像URL。

![来自OpenAI API的生成的输出图像：一个充满活力的珊瑚礁水下场景](https://cdn.thenewstack.io/media/2024/11/5135f029-image1-1024x564.jpg)
来自OpenAI API的生成的输出图像

![Cloudinary中上传的AI生成的图像。各种各样的图像](https://cdn.thenewstack.io/media/2024/11/80c98cac-image2-1024x512.jpg)
Cloudinary中上传的AI生成的图像

项目的完整源代码，请使用[这个gist](https://gist.github.com/Terieyenike/a75491834479a8eac3ff7beb59f6bdc8)或Google Colab中的[这个notebook](https://colab.research.google.com/drive/14P1g24FGxPsNqbJOA2NZ_ux-uQ_SLiLZ#scrollTo=bGj_nt2J1Lu4&uniqifier=1)。

**结论**
已经有灵感了吗？OpenAI API拥有许多内置功能，允许您扩展此项目。

有很多用例，本教程展示了一种使用文字生成自定义个性化图像的方法。此外，Cloudinary为其增添了最终润色，以便您可以重温创作非凡事物的记忆，并将图像安全地存储在云中的位置。

在Andela的白皮书“[如何在云中部署Kubernetes的DevOps技能正在发展](https://www.andela.com/resources/how-devops-skills-are-evolving-to-deploy-kubernetes-in-the-cloud/?utm_medium=contentmarketing&utm_source=whitepaper&utm_campaign=brand-global-the-new-stack-nov-20&utm_content=teri-eyenike-jupyter-blog-writers-room)”中，了解如何寻找云和Kubernetes专家来加快项目交付。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)