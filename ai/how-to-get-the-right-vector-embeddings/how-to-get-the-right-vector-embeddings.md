<!--
# 如何获得正确的向量嵌入
https://cdn.thenewstack.io/media/2023/09/e2f3db99-poly-3295856_1280-1024x680.png
Feature Image by Денис Марчук from Pixabay. 
-->

向量嵌入是一个非常强大且常用的自然语言处理技术。本文将为您全面地介绍向量嵌入，以及如何使用流行的开源模型生成它们。

译自 [How to Get the Right Vector Embeddings](https://thenewstack.io/how-to-get-the-right-vector-embeddings/) 。

向量嵌入在处理[语义相似性](https://zilliz.com/blog/vector-similarity-search)时非常关键。然而，向量只是一系列数字；向量嵌入是表示输入数据的一系列数字。使用向量嵌入，我们可以对[非结构化数据](https://zilliz.com/blog/introduction-to-unstructured-data)进行结构化，或通过将任何类型的数据转换为一系列数字来处理它。这种方法允许我们对输入数据执行数学运算，而不是依赖定性比较。

向量嵌入对许多任务特别是[语义搜索](https://zilliz.com/glossary/semantic-search)具有重大影响。然而，在使用向量嵌入之前获得适当的向量嵌入至关重要。例如，如果您使用图像模型对文本进行向量化，反之亦然，您可能会得到较差的结果。

在本文中，我们将学习什么是向量嵌入，如何使用不同的模型为您的应用程序生成正确的向量嵌入，以及如何通过 [Milvus](https://milvus.io/) 和 [Zilliz Cloud](https://zilliz.com/?utm_content=inline-mention) 等向量数据库来最大限度地利用向量嵌入。

## 向量嵌入是如何创建的？

![](https://cdn.thenewstack.io/media/2023/09/1717dbb9-milvus.png)

既然我们了解了向量嵌入的重要性，让我们来了解它们是如何工作的。向量嵌入是深度学习模型(也称为嵌入模型或深度神经网络)中输入数据的内部表示。那么，我们如何提取这些信息呢？

我们通过删除最后一层并获取倒数第二层的输出来获得向量。神经网络的最后一层通常会输出模型的预测，所以我们获取倒数第二层的输出。向量嵌入是输入到神经网络预测层的数据。

向量嵌入的维数等于模型中倒数第二层的大小，因此与向量的大小或长度是可交换的。常见的向量维数包括 384(由 Sentence Transformers Mini-LM 生成)、768(由 Sentence Transformers MPNet 生成)、1，536(由 OpenAI 生成)和 2，048(由 ResNet-50 生成)。

## 向量嵌入的含义是什么？

有人曾问我向量嵌入中每个维度的含义。简短的回答是没有意义。向量嵌入中的单个维度本身没有任何意义，因为它太抽象而难以确定其含义。然而，当我们将所有维度组合在一起时，它们可以提供输入数据的语义含义。

向量的维度是不同属性的高级抽象表示。所表示的属性取决于训练数据和模型本身。文本和图像模型会生成不同的嵌入，因为它们用于从根本上不同的数据类型进行训练。即使是不同的文本模型也会生成不同的嵌入。有时它们在大小上有所不同；有时，它们在所表示的属性上有所不同。例如，在法律数据上训练的模型会学到不同于在医疗保健数据上训练的模型的东西。我在[比较向量嵌入](https://zilliz.com/blog/comparing-different-vector-embeddings)的文章中探讨了这个话题。

## 生成正确的向量嵌入

如何获得适当的向量嵌入？首先需要确定您希望嵌入的数据类型。本节将介绍五种不同类型数据的嵌入方法：图像、文本、音频、视频和多模态数据。这里介绍的所有模型都是开源的，来自 Hugging Face 或 PyTorch。

### 图像嵌入

AlexNet 问世后，图像识别在 2012 年获得了巨大发展。从那时起，计算机视觉领域取得了许多进步。最引人注目的图像识别模型是基于之前 ResNet-34 架构的 50 层深度残差网络（deep residual network） ResNet-50。

残差神经网络(ResNet)使用快捷连接解决了深度卷积神经网络中的梯度消失问题。这些连接允许来自较早层的输出直接进入较晚层，而无需通过所有中间层，从而避免了梯度消失问题。与之前表现最好的卷积神经网络 VGGNet(视觉几何组) 相比，这种设计使得 ResNet 的复杂度更低。

我推荐两个 ResNet-50 实现作为示例：[Hugging Face 上的 ResNet 50](https://huggingface.co/microsoft/resnet-50) 和 [PyTorch Hub 上的 ResNet 50](https://pytorch.org/vision/main/models/generated/torchvision.models.resnet50.html)。虽然网络是相同的，但获得嵌入的过程有所不同。

下面的代码示例演示了如何使用 PyTorch 获得向量嵌入。首先，我们从 PyTorch Hub 加载模型。接下来，我们删除最后一层并调用 `.eval()` 指示模型表现得像运行推理一样。然后，`embed` 函数生成向量嵌入。

```python
# 从PyTorch Hub加载删除最后一层的嵌入模型
model = torch.hub.load('pytorch/vision:v0.10.0'， 'resnet50'， pretrained=True)
model = torch.nn.Sequential(*(list(model.children())[:-1]))
model.eval()

def embed(data):
  with torch.no_grad():
    output = model(torch.stack(data[0])).squeeze()
  return output
```

HuggingFace 使用了略有不同的设置。下面的代码演示了如何从 Hugging Face 获取向量嵌入。首先，我们需要从 transformers 库中获取一个特征提取器和模型。我们将使用特征提取器来获取模型的输入，并使用模型来获取输出并提取最后的隐藏状态。

```python
# 直接加载模型
from transformers import AutoFeatureExtractor， AutoModelForImageClassification

extractor = AutoFeatureExtractor.from_pretrained("microsoft/resnet-50")
model = AutoModelForImageClassification.from_pretrained("microsoft/resnet-50")

from PIL import Image

image = Image.open("<image path>")
# image = Resize(size=(256， 256))(image) 

inputs = extractor(images=image， return_tensors="pt")
# print(inputs)

outputs = model(**inputs)
vector_embeddings = outputs[1][-1].squeeze()
```

## 文本嵌入

自 AI 发明以来，工程师和研究人员一直在实验自然语言和 AI。一些最早的实验包括：

- ELIZA，第一个 AI 治疗师聊天机器人。
- John Searle 的中国房间，一个检查汉英翻译是否需要对语言的理解的思想实验。
- 英语和俄语之间的基于规则的翻译。

自然语言上的 AI 操作已经从其基于规则的嵌入发生了显著的变化。从基本的神经网络开始，我们通过 RNN 添加了递归关系来跟踪时间中的步骤。从那里，我们使用 transformers 来解决序列变换问题。

transformers 由编码器组成，它将输入编码为表示状态的矩阵，注意力矩阵和解码器。 解码器对状态和注意力矩阵进行解码以预测正确的下一个标记以完成输出序列。 GPT-3 是迄今为止最流行的语言模型，由严格的解码器组成。它们对输入进行编码并预测正确的下一个 token。

除了 OpenAI 的嵌入之外，这里还有来自 Hugging Face 的 sentence-transformers 库的两个模型可以使用：

- [MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2): 384维模型
- [MPNet-Base-V2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2): 768维模型

您可以以相同的方式访问这两个模型的嵌入。

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("<model-name>")
vector_embeddings = model.encode("<input>")
```

## 多模态嵌入

与图像或文本模型相比，多模态模型不太成熟。它们通常将图像与文本关联起来。

最有用的开源示例是 [CLIP VIT](https://huggingface.co/openai/clip-vit-large-patch14)，这是一个图像到文本的模型。您可以以与图像模型相同的方式访问 CLIP VIT 的嵌入，如下面的代码所示。

```python
# 直接加载模型
from transformers import AutoProcessor， AutoModelForZeroShotImageClassification

processor = AutoProcessor.from_pretrained("openai/clip-vit-large-patch14")
model = AutoModelForZeroShotImageClassification.from_pretrained("openai/clip-vit-large-patch14")
from PIL import Image

image = Image.open("<image path>")
# image = Resize(size=(256， 256))(image) 

inputs = extractor(images=image， return_tensors="pt")
# print(inputs)

outputs = model(**inputs)
vector_embeddings = outputs[1][-1].squeeze()
```

## 音频嵌入

与文本或图像相比，音频的 AI 获得的关注较少。最常见的音频用例是语音转文本，用于呼叫中心、医疗技术和辅助功能等行业。开源语音转文本的一个流行模型是 OpenAI 的 Whisper。下面的代码显示了如何从语音转文本模型获得向量嵌入。

```python
import torch

from transformers import AutoFeatureExtractor， WhisperModel

from datasets import load_dataset

model = WhisperModel.from_pretrained("openai/whisper-base")

feature_extractor = AutoFeatureExtractor.from_pretrained("openai/whisper-base")

ds = load_dataset("hf-internal-testing/librispeech_asr_dummy"， "clean"， split="validation")

inputs = feature_extractor(ds[0]["audio"]["array"]， return_tensors="pt")

input_features = inputs.input_features

decoder_input_ids = torch.tensor([[1， 1]]) * model.config.decoder_start_token_id

vector_embedding = model(input_features， decoder_input_ids=decoder_input_ids).last_hidden_state
```

## 视频嵌入

与音频或图像嵌入相比，视频嵌入更为复杂。在处理视频时，由于它们包括同步的音频和图像，因此需要采用多模态方法。 一种流行的视频模型是 DeepMind 的[多模态 perceiver](https://huggingface.co/deepmind/multimodal-perceiver)。 这个 [notebook 教程](https://github.com/NielsRogge/Transformers-Tutorials/blob/master/Perceiver/Perceiver_for_Multimodal_Autoencoding.ipynb)展示了如何使用该模型对视频进行分类。

要获取输入的嵌入，请改用 notebook 中显示的代码的 `outputs[1][-1].squeeze()`，而不是删除 outputs。 我在 `autoencode` 函数中突出显示了这段代码。

```python
def autoencode_video(images， audio):

  # 只需整个视频输入一次
  inputs = {'image': torch.from_numpy(np.moveaxis(images， -1， 2)).float().to(device)， 
            'audio': torch.from_numpy(audio).to(device)，
            'label': torch.zeros((images.shape[0]， 700)).to(device)}
            
  nchunks = 128
  reconstruction = {}
  for chunk_idx in tqdm(range(nchunks)):
      image_chunk_size = np.prod(images.shape[1:-1]) // nchunks
      audio_chunk_size = audio.shape[1] // SAMPLES_PER_PATCH // nchunks
      subsampling = {
          'image': torch.arange(
              image_chunk_size * chunk_idx， image_chunk_size * (chunk_idx + 1))，
          'audio': torch.arange(
              audio_chunk_size * chunk_idx， audio_chunk_size * (chunk_idx + 1))，
          'label': None，
      }

      # 前向传播
      with torch.no_grad():
          outputs = model(inputs=inputs， subsampled_output_points=subsampling)

      output = {k:v.cpu() for k，v in outputs.logits.items()}
      reconstruction['label'] = output['label']
      if 'image' not in reconstruction:
          reconstruction['image'] = output['image']
          reconstruction['audio'] = output['audio']
      else:
          reconstruction['image'] = torch.cat(
              [reconstruction['image']， output['image']]， dim=1)
          reconstruction['audio'] = torch.cat(
              [reconstruction['audio']， output['audio']]， dim=1)
              
  vector_embeddings = outputs[1][-1].squeeze()

  # 最后，将图像和音频模态reshape回原始形状
  reconstruction['image'] = torch.reshape(reconstruction['image']， images.shape)
  reconstruction['audio'] = torch.reshape(reconstruction['audio']， audio.shape)

  return reconstruction
  
return None
```

## 使用向量数据库存储、索引和搜索向量嵌入

既然我们了解了向量嵌入是什么，以及如何使用各种强大的嵌入模型生成它们，那么接下来的问题是如何存储和利用它们。向量数据库就是答案。

诸如 [Milvus](https://zilliz.com/what-is-milvus) 和 [Zilliz Cloud](https://zilliz.com/cloud) 之类的向量数据库专门用于通过向量嵌入在大规模非结构化数据集上存储、索引和搜索。它们也是各种 AI 技术栈中最关键的基础设施之一。

向量数据库通常使用[近似最近邻(ANN)](https://zilliz.com/glossary/anns)算法来计算查询向量与数据库中存储的向量之间的空间距离。两个向量的位置越近，相关性就越大。然后，该算法找到前 k 个最近邻并将其传送给用户。

向量数据库广泛用于如语言[模型检索增强生成(RAG)](https://zilliz.com/use-cases/llm-retrieval-augmented-generation)、问答系统、推荐系统、语义搜索以及图像、视频和音频相似性搜索等场景中。

要进一步了解向量嵌入、非结构化数据和向量数据库，可以从[向量数据库 101 系列](https://zilliz.com/blog?tag=39&page=1)开始。

## 总结

向量是使用非结构化数据的强大工具。使用向量，我们可以根据语义相似性在数学上比较不同的非结构化数据。为任何应用程序构建向量搜索引擎，选择正确的向量嵌入模型至关重要。

在本文中，我们了解到向量嵌入是神经网络中输入数据的内部表示。因此，它们在很大程度上取决于网络架构和用于训练模型的数据。不同的数据类型(如图像、文本和音频)需要特定的模型。幸运的是，有许多开源的预训练模型可供使用。在本文中，我们介绍了最常见的数据类型：图像、文本、多模态、音频和视频的五种模型。另外，如果您想最大限度地利用向量嵌入，则向量数据库是最流行的工具。
