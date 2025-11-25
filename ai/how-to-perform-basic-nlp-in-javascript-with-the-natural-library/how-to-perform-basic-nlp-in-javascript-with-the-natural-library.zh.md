[Natural](https://naturalnode.github.io/natural/) 是一个用于自然语言处理（NLP）的 JavaScript 库，是人工智能时代越来越受欢迎的[用于机器学习的 JavaScript 库](https://thenewstack.io/ditch-python-5-javascript-libraries-for-machine-learning/)之一。具体来说，NLP 弥合了计算机理解与人类语言之间的鸿沟。它常用于分类客户评论、分析推文、提供诸如自动补全之类的搜索辅助功能以及内容标签。简单的聊天机器人，例如那些弹出以帮助包裹追踪或更改订单的机器人，也使用 NLP。这些聊天机器人对消息进行分词（稍后会详细介绍），识别意图，并自动回复解决方案（好吧……大多数时候如此……）。

到目前为止，我们都或多或少地熟悉 NLP（ChatGPT 和 Claude 都使用 NLP）。但并非所有 NLP 工具都是平等的。Natural 是一个基于规则的工具，提供基本的 NLP 功能；你可以将 Natural 库视为一个用于语言处理基本构建块的工具，例如将句子分成单词、找出词根并将文本分类。当你需要轻量级、易于理解且快速构建的东西时，Natural 是一个很好的工具。

ChatGPT 和 Claude 等工具使用的 NLP 模型也使用 NLP——但方式与使用 Natural 库的应用程序不同。像 ChatGPT 这样的工具使用高级 NLP，它依赖于大规模神经网络来理解超越基于规则的工具的上下文、细微差别和语言模式；它们不易于理解，也不易于构建。因此，如果你需要一个简单且构建无缝的工具，Natural 是一个更好的选择。

让我们来看看 Natural 的一些基本功能。你将亲身体验使用这个基本 NLP 工具是多么容易。

开始之前，你应该对 JavaScript 有基本的了解，并且你的机器上安装了 `node.js`。

在你的 IDE 中，打开一个新文件并使用以下代码创建项目：

```
mkdir natural-tutorial
cd natural-tutorial
```

然后我们就可以初始化一个 Node 项目并安装 Natural：

```
npm init -y
npm install natural
```

你可以将所有这些代码写在同一个页面上。首先，创建一个新页面。

然后你可以每次使用此终端命令运行代码：

```
node index.js
```

## 使用 Natural 库进行文本分词

计算机无法理解整个句子——相反，它们将文本作为原始字符读取，而原始字符本身没有意义。分词是将句子拆分成单词的过程；它将一个句子分解成单独的单词或短语。这为计算机提供了更容易分析的片段，帮助它识别模式、含义和关系。

搜索引擎使用分词将查询分解成单个单词，以找到最相关的结果。

```
const nlpTools = require('natural');


// create tokenizer
const splitter = new nlpTools.WordTokenizer();


// human words
const humanText = "Splitting this sentence is like translating from human to computer.";


// translate to computer understanding
const computerWords = splitter.tokenize(humanText);


console.log(computerWords);
```

输出：

```
[
  'Splitting', 'this', 'sentence',
  'is', 'like', 'translating',
  'from', 'human', 'to',
  'computer'
]
```

## 理解句子分词

句子分词帮助计算机理解完整的句子，而不是单个单词。它通过将文本块分解成单独的句子，然后阅读单词并理解句子上下文中的每个单词来实现这一点。这有助于计算机更准确地总结文本和提取信息。

```
const nlpTools = require('natural');
const sentenceBreaker = new nlpTools.SentenceTokenizer();


const textBlob = "These words mean something as a group. This is a different group with new words. Here's one more!";
const sentenceSplits = sentenceBreaker.tokenize(textBlob);


console.log(sentenceSplits);
```

输出：

```
[
  'These words mean something as a group.',
  'This is a different group with new words.',
  "Here's one more!"
]
```

## 如何将单词词干提取为词根形式

词干提取将单词还原为其词根。这使得计算机能够将所有相似的单词视为相同。词干提取改进了搜索和分析。“reading”、“reads”和“read”等词都共享相同的词根“read”。通过词干提取，计算机将所有这些词视为相似。如果没有词干提取，计算机将把每个词都视为完全不同。

Natural 使用 PorterStemmer 进行词干提取；它是一个内置于 Natural 库中的算法。它使用一组规则来去除常见的词尾（如 -ing、-s 和 -ed），以将单词还原为其词根。你无需编写任何词干提取逻辑。

```
const nlpTools = require('natural');
const rootFinder = nlpTools.PorterStemmer;


console.log(rootFinder.stem("reading")); 
console.log(rootFinder.stem("reads"));    
console.log(rootFinder.stem("read"));  
```

输出：

```
read
read
read
```

## 实现文本分类

文本分类自动对文本进行分类。它通过查看单词、模式和上下文来分配类别。Natural 库通过其内置分类器实现这一点。它最常使用的分类器是朴素贝叶斯分类器（Naive Bayes Classifier）和逻辑回归分类器（Logistic Regression Classifier）。朴素贝叶斯分类器是一个机器学习模型，而逻辑回归分类器更像是一个统计分类器。这些分类器分析模式并学习概率以对新文本进行分类。

与词干提取不同，你必须先训练分类器，然后才能对新文本进行分类。你可以通过向分类器提供文本及其所属类别来训练模型。你不需要对类别中的每个可能单词都训练分类器。分类器具有内置功能，可以分析你提供的示例，学习与每个类别相关的单词，并计算概率。训练完成后，你可以向分类器提供新文本，它将预测其类别。

让我们以将电子邮件分为垃圾邮件和收件箱邮件为例。

```
const natural = require('natural');
const classifier = new natural.BayesClassifier();


// train the classifier with labeled examples
classifier.addDocument('Win a free iPhone!', 'spam');
classifier.addDocument('Limited time offer! Click here!', 'spam');
classifier.addDocument('You're booked for Pilates at 7am', 'inbox');
classifier.addDocument('Meeting at 3pm today', 'inbox');
classifier.addDocument('Your package has been shipped', 'inbox');


// train the model
classifier.train();


// test 
console.log(classifier.classify('Congratulations! Claim your prize now!')); // spam
console.log(classifier.classify('Can we reschedule our meeting to 4pm?'));  // inbox
console.log(classifier.classify('Limited offer just for you'));             // spam
console.log(classifier.classify('Don’t forget to submit your report'));
```

输出：

```
spam
inbox
spam
inbox
```

## 衡量单词和字符串相似度

我们都曾亲身受到过这一点的影响……自动更正、拼写检查和自动补全。要使用这些功能，计算机需要衡量一个单词与另一个单词的相似程度。单词相似度，也称为字符串相似度，是计算机比较两段文本并评估它们相似程度的一种方式。

Natural 使用 Levenshtein 距离或 Jaro-Winkler 距离算法。这些算法是基于规则的，你不需要提供训练数据。它们计算字母之间的差异或比较字母顺序——差异越小，相似度得分越高。这就是计算机根据你使用的功能来建议更正或序列中下一个单词的方式。

```
const nlpTools = require('natural');


const similarityScore = nlpTools.JaroWinklerDistance('sequnce', 'sequence');
console.log(similarityScore); 
```

输出：

```
0.9555555555555556
```

关于输出的简要说明：

*   1 表示单词完全相同
*   0 表示完全不同
*   0.9555555555555556 表示这两个单词几乎相同

## 在 JavaScript 中执行拼写检查

自动更正等工具也使用拼写检查。Natural 将一个单词与其已知词典（你需要提供已知词典）进行比较。如果未找到该单词，拼写检查将识别并建议替代方案。确定单词相似度的相同算法也有助于拼写检查。

使用 `typoChecker.getCorrections()` 方法时，你需要提供单词和要返回的可能匹配项的数量。如果你不提供数量，它将提供所有可能的匹配项。

```
const nlpTools = require('natural');
const wordStore = ['cat', 'dog', 'elephant', 'giraffe'];
const typoChecker = new nlpTools.Spellcheck(wordStore);


console.log(typoChecker.getCorrections('elephnt', 2));
console.log(typoChecker.getCorrections('grffe', 2)); 
```

输出：

```
[ 'elephant' ]
[ 'giraffe' ]
```

## 结论

这只是 Natural 库的简要介绍。这些是构建你的第一个简单聊天应用或文本处理工具所需的基础构建块。如果你觉得本教程易于理解，你可能已准备好开始探索更高级的库，例如 [compromise](https://github.com/spencermountain/compromise) 或 [nlp.js](https://github.com/axa-group/nlp.js)。