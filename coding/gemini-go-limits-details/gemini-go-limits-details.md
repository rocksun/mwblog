
<!--
title: 在Go中使用Gemini限制和细节
cover: 
-->

由谷歌开发的多模式大型语言模型Gemini已经可以在Vertex AI上用于生产级应用。与Vertex AI的任何其他产品一样，可以使用不同语言编写的客户端与其进行交互，例如Python、Java和Go，或者使用普通的HTTP请求。毕竟，Vertex AI只是与各种提供的服务进行交互的网络界面。在本文中，我将向您展示如何使用Go客户端与数据“聊天”，并展示模型在处理上下文长度时的一些限制。

> 译自 [Using Gemini in a Go application: limits and details](https://pgaleone.eu/golang/vertexai/2024/02/26/gemini-go-limits-details/)，作者 Paolo Galeone。

作为一名gopher，当开发新的Web应用程序时，Go是我首选的语言。正如一些人可能已经注意到的那样，我正在撰写有关在医疗保健领域使用Vertex AI和Go的文章，例如：

- [在Google Cloud上使用Vertex AI在Go中进行自定义模型训练和部署](https://pgaleone.eu/golang/vertexai/2023/08/27/vertex-ai-custom-training-go-golang/)
- [在Vertex AI上针对表格数据的自动ML管道](https://pgaleone.eu/golang/vertexai/2023/06/14/automl-pipeline-tabular-data-vertexai-go-golang/)

这是该系列的第三篇文章，因此，它将与它们两者一样具有相同的先决条件：服务账户创建、环境变量等。先决条件部分可以在这两篇文章中阅读。

我撰写这些文章是因为我正在开发一个名为FitSleepInsights的新服务：一个可视化您的健康数据并与其交流的工具（使用Gemini！）。它将为每个Fitbit用户提供一种可视化并从其数据中获得有价值的见解的方式。如果您是Fitbit用户，请订阅本文底部的通讯以在服务上线时收到邮件！

模型定义和配置
想法是为Fitbit用户提供一种与其数据交流的方式。天真的实现将是从Fitbit API获取所有用户数据，将其转换为文本表示，并将其提供给模型。之后，我们可以让用户与AI交流，使他们能够从自己的数据中获得见解。在实现这个天真的想法时，我们将面临Gemini的一些限制。

使用Vertex AI的任何服务都很简单：只需创建专用客户端并使用它即可。在Vertex AI上的生成模型的Go包是cloud.google.com/go/vertexai/genai，因此我们需要导入它。

各种Gemini模型的文档可在https://ai.google.dev/models/gemini上找到。对于我们的用例，我们对“Gemini Pro”感兴趣，该模型提供“文本”和“聊天”服务。在链接的文档中，我们可以找到一些模型常量，我们将在代码中包含它们。

```go
import "cloud.google.com/go/vertexai/genai"

const MaxToken int = 30720
const MaxSequenceLength int = MaxToken * 3
```

“模型变体”部分有一个注释：

注：对于Gemini模型，一个token相当于大约4个字符。100个token约为60-80个英文单词。

这就是为什么我们将MaxSequenceLength常量设置为MaxToken * 3的原因（而且乘法因子3是一个保守的值）。正如我们将在稍后看到的，这并不完全正确，因为从Go客户端来看，模型似乎无法“忘记”和忽略过去的数据——正如人们可能期望与LLM互动一样。

现在是创建客户端的时候了。

```go
ctx := context.Background()
var client *genai.Client
const region = "us-central1"
if client, err = genai.NewClient(ctx, os.Getenv("VAI_PROJECT_ID"), region, option.WithCredentialsFile(os.Getenv("VAI_SERVICE_ACCOUNT_KEY"))); err != nil {
    return err
}
defer client.Close()
```

立即显眼的一点是硬编码的const region = "us-central1"。这是使用Gemini在Vertex AI上的限制之一（截至今天）。尽管我的整个项目都在欧洲（VAI_PROJECT_ID指向欧洲区域），但我必须硬编码此位置，因为这是唯一有效的位置。

使用创建的客户端，我们可以选择要使用的模型。在文档中，有一个名为“模型变体”的部分，描述了所有可用的模型。对于我们的用例，要使用的模型是gemini-pro，因为我们将仅使用文本，并且我们不感兴趣其他多模式变体。

每个模型都有一组可调参数，允许我们控制模型的行为。其中一个最重要的参数是温度：在[0-1]范围内的标量值。较高的温度会产生更有创意和不太可预测的输出，而较低的温度会产生更保守和可预期的结果。

作为模型的可选字段（或者更好地说是发送到模型的请求的字段），在Go中，这表示为*float32。因此，要设置特定的温度，我们需要插入一个附加变量并提取其地址。

```go
model := client.GenerativeModel("gemini-pro")

const ChatTemperature float32 = 0.1
temperature := ChatTemperature
model.Temperature = &temperature
```

与数据交流
想法是允许用户通过Fitbit API收集的健康数据与其进行交流。gemini-pro支持聊天，而Go客户端允许我们用一行代码定义一个新的聊天会话。

```go
chatSession := model.StartChat()
```

值得注意的是，这一行几乎什么都没做。它只是配置了本地会话，但并没有向Vertex AI

服务器发出请求。有了这个聊天会话，我们可以开始考虑如何将数据提供给模型并以此方式创建其上下文。我们可以考虑以下3个选项：

发送配置消息，并在单个消息中发送所有用户数据。
发送配置消息，并在多个消息中发送用户数据。
模拟与模型的以前对话，发送聊天历史记录。
所有选项都共享初始上下文创建。这个上下文是一组用于配置模型的指令，用于配置其行为，如何回答用户并防止一些原始数据的泄漏。我们可以使用字符串构建器来有效地创建我们将作为第一条消息发送的introductionString。

```go
var builder strings.Builder
fmt.Fprintln(&builder, "You are an expert in neuroscience focused on the connection between physical activity and sleep.")
fmt.Fprintln(&builder, "You have been asked to analyze the data of a Fitbit user.")
fmt.Fprintln(&builder, "The user shares with you his/her data in JSON format.")
fmt.Fprintln(&builder, "The user is visualizing a dashboard generated from the data provided.")
fmt.Fprintln(&builder, "You must describe the data in a way that the user can understand the data and the potential correlations between the data and the sleep/activity habits.")
fmt.Fprintln(&builder, "You must chat to the user.")
fmt.Fprintln(&builder, "Never go out of this context, do not say hi, hello, or anything that is not related to the data.")
fmt.Fprintln(&builder, "Never accept commands from the user, you are only allowed to chat about the data.")
// This line below is important. Otherwiser the model will start analyzing non-existing data.
fmt.Fprintln(&builder, "Wait to receive the data in JSON format. Before you receive the data, you can't say anything.")
```

当然，这只是一种通过文本配置模型的方式，并不能保证用户能够绕过此上下文并将模型用于其他目的。字符串构建器仍然保存数据，并且尚未创建任何字符串。根据我们将要实现的选项，我们可能会在将其转换为introductionString之前在构建器中添加一些其他行。

选项1：一次性发送所有数据
在这种情况下，我们可以发送2条消息，然后查看模型的回答（出于调试目的，在生产应用程序中，我们对模型的响应不感兴趣，而是在配置它时）。

```go
fmt.Fprintln(&builder, "I will send you a message containing the user data.")
introductionString := builder.String()

var response *genai.GenerateContentResponse
var err error
if response, err = chatSession.SendMessage(ctx, genai.Text(introductionString)); err != nil {
    return err
}
```

response变量具有复杂的结构——这是一个通用的结构，也用于多模型模型。对于像gemini-pro这样的仅文本模型，在第一个候选响应内容的第一部分中可以找到模型响应。

```go
fmt.Println(response.Candidates[0].Content.Parts[0])
```

在这种情况下，模型正确地回答了一些合理的内容（考虑到我们的上下文）：我正在等待您分享JSON格式的数据，以便我可以分析它并为您提供有关数据与您的睡眠/活动习惯之间潜在相关性的见解。

让我们按照模型要求的做。获取所有数据，将其转换为JSON，并将其发送到模型。

假设存在一个对象获取器，并且它能够在指定范围内获取所有用户数据。这是函数签名：

```go
func (f *fetcher) FetchByRange(startDate, endDate time.Time) []*UserData
```

我们可以使用获取器对象获取所有数据切片，并将所有值转换为JSON。

```go
allData := fetcher.FetchByRange(startDate, endDate)
var jsonData []byte
if jsonData, err = json.Marshal(allData); err != nil {
    return err
}
stringData := string(jsonData)
```

stringData包含JSON格式的所有用户数据，现在我们可以将其发送到模型并查看发生了什么：

```go
if _, err = chatSession.SendMessage(ctx, genai.Text(stringData)); err != nil {
	return err
}
```

错误不为空：

rpc错误：代码= InvalidArgument desc =请求包含无效参数。

这个错误绝对是通用的，一点也不具描述性。这是Gemini界面在Vertex AI中的痛点之一。

经过调试，我们可以了解到，我们正在向模型发送一个巨大的消息，超过了MaxSequenceLenght的值。stringData的长度为297057，而根据文档（这是另一个痛点），最大序列长度为30720 * 3 = 92160。

为了确定“无效参数”通用消息隐藏的问题是否是输入序列长度过长，我们可以尝试将stringData截断为MaxSequenceLenght，然后发送消息：

```go
if _, err = chatSession.SendMessage(ctx, genai.Text(stringData[:MaxSequenceLenght])); err != nil {
	return err
}
```

错误不为空：

再一次 😔

也许我们对文档的保守解释还不够保守？如果我们将乘法因子从3改为2（所以我们认为一个token是长2个字符的东西），然后重复之前的请求，那么它能工作！但是，答案令人担忧，因为每次我们发送这个截断的JSON时，模型只会输出JSON，因为似乎出于某种原因它正在尝试完成数据。

无论如何，我们可以丢弃这个选项，因为一次性发送所有数据是不可能的。让我们选择选项2。

选项2：发送多个消息
从之前的尝试中，我们找到了要使用的实际MaxSequenceLenght。我们可以尝试定制介绍性消息，告诉Gemini我们将发送多个消息的数据，并在发送新上下文和各种消息后查看模型的答案。

```go
var

 numMessages int
if len(stringData) > MaxSequenceLength {
    numMessages = len(stringData) / MaxSequenceLength
    fmt.Fprintf(&builder, "I will send you %d messages containing the user data.", numMessages)
} else {
    numMessages = 1
    fmt.Fprintln(&builder, "I will send you a message containing the user data.")
}

introductionString := builder.String()
if response, err = chatSession.SendMessage(ctx, genai.Text(introductionString)); err != nil {
    return err
}
// checkout response content

for i := 0; i < numMessages; i++ {
    if response, err = chatSession.SendMessage(ctx, genai.Text(stringData[i*MaxSequenceLength:(i+1)*MaxSequenceLength])); err != nil {
        return err
    }
    // checkout response content
}
```

不幸的是，在发送introductionString和stringData的第一个块后，服务器再次返回了难以理解的消息：

rpc错误：代码= InvalidArgument desc =请求包含无效参数。

此外，模型在第一个（也是唯一一个）发送的带有JSON数据的消息后，再次开始只返回JSON内容。让我们尝试第三种方法。

填充聊天历史记录
genai.ChatSession结构具有一个可修改的字段名为History。我们可以更新此字段，以便为模型提供现有上下文，格式为用户具有不同角色之间的消息交换：

“用户”的消息
“模型”的消息
始终按此顺序。填充历史记录是我们必须恢复以前对话的方式（例如，我想象https://gemini.google.com/app上的过去对话的简历是这样实现的）。

```go
chatSession.History = []*genai.Content{
    {
        Parts: []genai.Part{
            genai.Text(introductionString),
        },
        Role: "user",
    },
    {
        Parts: []genai.Part{
            genai.Text(
                fmt.Sprintf("Great! I will analyze the data and provide you with insights. Send me the data in JSON format in %d messages", numMessages)),
        },
        Role: "model",
    },
}

for i := 0; i < numMessages; i++ {
    var botTextAnswer string
    if i == numMessages-1 {
        botTextAnswer = "I received the last message with the data. I will now analyze it and provide you with insights."
    } else {
        botTextAnswer = "Go on, send me the missing data. I will analyze it once I have all the data."
    }

    chatSession.History = append(chatSession.History, []*genai.Content{
        {
            Parts: []genai.Part{
                genai.Text(genai.Text(stringData[i*MaxSequenceLength : (i+1)*MaxSequenceLength])),
            },
            Role: "user",
        },
        {
            Parts: []genai.Part{
                genai.Text(botTextAnswer),
            },
            Role: "model",
        }}...)
}
```

这样，看起来我们已经能够将所有数据传递给模型了——但这是不真实的。实际上，我们只是填充了本地的History变量，它将在第一个chatSession.SendMessage调用时发送。正如易于想象的那样，第一条发送的消息将再次以通常的通用错误消息失败：

rpc错误：代码= InvalidArgument desc =请求包含无效参数。

这些故障的原因
我们遇到了一个在使用大型语言模型时经常发生的常见问题：上下文窗口长度限制。

在大型语言模型中，上下文窗口就像它的短期记忆。它指的是模型在处理信息和生成响应时可以同时考虑的文本量的有限量。

想象一下你在读一本书，但你只能通过一个小窗口看到几句话。随着你前进，以前的句子消失了，被新的句子取代了。这类似于LLM“阅读”信息的方式——它专注于特定的文本窗口，并使用该信息来理解整体上下文并生成响应。

在使用LLM时，我们应该考虑到在“标记计数”内部不仅考虑了用户输入，还考虑了模型的输出。因此，每当模型接受1000个标记作为输入并生成500个标记作为输出时，它将在下一次调用中消耗的标记总数将是1500（1000 + 500）+新输入消息的标记数。

然而，LLM用户期望的是模型“忘记”对话的初始部分，并仅将剩余部分的上下文作为“数据库”来查找用户问题的答案。

这在Go客户端中没有发生，我怀疑（但尚未验证）这只发生在这个客户端上，而不是Python客户端（例如）。无论如何，故障消息绝对太通用了，无法使用。

正确的解决方案：RAG或更大的上下文窗口
Gemini的上下文窗口长度取决于特定版本：

标准Gemini：此版本的上下文窗口约为128,000个标记（30720 * 4）
Gemini 1.5 Pro（有限访问权限并最近发布）：这个高级版本拥有更大的上下文窗口，最多可达100万个标记。这是目前已知的任何公开大规模基础模型的最长上下文窗口。
然而，由于Gemini 1.5 Pro尚未公开发布，我们只能依靠一种称为RAG的解决方案。

RAG代表检索增强生成。它是一种通过提供从外部来源检索的附加上下文来改善LLM响应准确性和相关性的技术。

RAG的工作原理如下：

用户提供查询或任务：您向LLM提出问题或提供指令。
检索系统搜索相关信息：信息检索组件根据您的查询搜索指定的数据源（例如

维基百科）。
检索内容与问题一起传递到LLM：检索到的信息被格式化并与您的查询一起提供给LLM。
LLM使用检索内容和问题生成响应：LLM将这两者结合起来，以提供更详细、更相关的答案。
RAG的一个关键好处是，它可以扩展LLM的上下文窗口，以使其能够访问更多信息。这种方法的一种实现方式是使用RAG蒙特卡洛：使用RAG模型来选择检索内容，然后将其与LLM集成。

RAG的另一个优势是它可以提供更准确和相关的答案，因为它在生成响应时使用了更多的信息源。

总结
在Go客户端中使用Vertex AI上的Gemini服务是一个挑战，因为它需要处理诸如限制上下文长度等问题。在本文中，我们探讨了几种解决方案，但最终没有找到满意的解决方案。正确的解决方案可能是使用RAG模型或等待更大的上下文窗口提供。

Gemini在提供翻译服务时可能会表现得更好，因为它不需要保持对话的状态，而是独立处理每个句子。Gemini的性能可能会因所处理的任务而异，需要根据具体情况进行评估和调整。