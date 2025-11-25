[Natural](https://naturalnode.github.io/natural/) is a JavaScript library for Natural Language Processing (NLP), one of a number of [JavaScript libraries for machine learning](https://thenewstack.io/ditch-python-5-javascript-libraries-for-machine-learning/) gaining traction in the AI era. NLP, specifically, fills the gap between computer understanding and human language. It’s commonly used when sorting customer reviews, analyzing tweets, for search helpers like autocomplete, and in content tagging. Simple chatbots, like the ones that pop up to offer help with package tracking or changing an order, also use NLP. These chatbots tokenize (more on that later) the message, identify intent, and automatically reply with the solution (well… most of the time…).

By now, we are all familiar with NLP in one way or another (ChatGPT and Claude both use NLP). But not all NLP tools are created equal. Natural is a rule-based tool that provides basic NLP functionality; you can think of the Natural library as a tool for the simple building blocks of language processing, like splitting sentences into words, figuring out word roots and sorting text into categories. Natural is a good tool when you need something lightweight, easy to understand, and fast to build with.

The NLP models used by tools like ChatGPT and Claude use NLP — but not in the same way an application using the Natural library does. The likes of ChatGPT use advanced NLP which relies on massive neural networks that understand context, nuance and language patterns beyond rule-based tools; and they are not easy to understand, or to build with. So if you need something simple with a seamless build, Natural is a better option.

Let’s go over some of the basic Natural functionality. You will see for yourself how easy it can be to work with this basic NLP tool.

Before getting started, you should have a basic understanding of JavaScript and have `node.js` installed on your machine.

In your IDE, open a new file and create the project with the following code:

```
mkdir natural-tutorial
cd natural-tutorial
```

Then we’re ready to initialize a Node project and install Natural:

```
npm init -y
npm install natural
```

You can write all of this code on the same page. First, create a new page.

You can then run the code each time with this terminal command:

```
node index.js
```

## Tokenizing Text with the Natural Library

Computers can’t understand whole sentences — instead they read text as raw characters, and raw characters alone don’t have meaning. Tokenizing is the process of splitting sentences into words; it breaks a sentence into individual words or phrases. This gives the computer more manageable pieces to analyze, helping it recognize patterns, meanings and relationships.

Search engines use tokenizing to break the query into individual words to find the most relevant results.

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

Output:

```
[
  'Splitting', 'this', 'sentence',
  'is', 'like', 'translating',
  'from', 'human', 'to',
  'computer'
]
```

## Understanding Sentence Tokenization

Sentence tokenization helps the computer understand full sentences, rather than the words themselves. It does this by breaking a block of text into individual sentences, then reading the words and understanding each word in the context of the sentence. This helps the computer summarize text and extract information more accurately.

```
const nlpTools = require('natural');
const sentenceBreaker = new nlpTools.SentenceTokenizer();


const textBlob = "These words mean something as a group. This is a different group with new words. Here's one more!";
const sentenceSplits = sentenceBreaker.tokenize(textBlob);


console.log(sentenceSplits);
```

Output:

```
[
  'These words mean something as a group.',
  'This is a different group with new words.',
  "Here's one more!"
]
```

## How To Stem Words to Their Root Form

Stemming reduces the word to its root. This allows the computer to treat all similar words as the same. Stemming improves search and analysis. Words like “reading,” “reads,” and “read” all share the same root “ead.” With stemming, the computer treats all these words as similar. Without stemming, the computer would treat each word as completely different.

Natural uses the PorterStemmer to stem; it’s an algorithm built into the Natural library. It uses a set of rules to strip common word endings (like -ing, -s, and -ed) to reduce the word to its root. You don’t need to write any stemming logic.

```
const nlpTools = require('natural');
const rootFinder = nlpTools.PorterStemmer;


console.log(rootFinder.stem("reading")); 
console.log(rootFinder.stem("reads"));    
console.log(rootFinder.stem("read"));  
```

Output:

```
read
read
read
```

## Implementing Text Classification

Text classification automatically categorizes text. It does so by looking at words, patterns and context to assign its category. The Natural library does this with its built-in classifiers. The classifiers it uses most often are the Naive Bayes Classifier and the Logistic Regression Classifier. The Naive Bayes Classifier is a machine-learning model and the Logistic Regression Classifier is more of a statistical classifier. These classifiers analyze patterns and learn probability to classify new text.

Different from stemming, you have to train the classifier before categorizing new text. You can train the model by giving the classifier text and the category it belongs to. You don’t have to train the classifier on every possible word in a category. The classifier has built-in functionality to analyze the examples you provided, learn words associated with each category, and calculate probabilities. Once trained, you can give the classifier new text and it will predict the category.

Let’s use the example of categorizing email between spam and inbox messages.

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

Output:

```
spam
inbox
spam
inbox
```

## Measuring Word and String Similarity

We’ve all been personally affected by this one… autocorrect, spell check and autocomplete. To use these features, the computer measures how similar one word is to another. Word similarity, a.k.a. string similarity, is a way for the computer to compare two pieces of text and score how close they are.

Natural uses Levenshtein Distance or Jaro-Winkler Distance algorithms. These algorithms are rule-based and you don’t need to provide training data. They count the difference between letters or compare letter order — the smaller the difference, the higher the similarity score. This is how a computer suggests the correction or next words in a sequence depending on what function you’re using.

```
const nlpTools = require('natural');


const similarityScore = nlpTools.JaroWinklerDistance('sequnce', 'sequence');
console.log(similarityScore); 
```

Output:

```
0.9555555555555556
```

A quick note on the output:

* 1 means the words are identical
* 0 means completely different
* 0.9555555555555556 means these two words are nearly identical

## Performing Spellchecking in JavaScript

Tools like autocorrect also use spellchecking. Natural compares a word against its dictionary of known words (you need to provide the dictionary of known words). If the word in question isn’t found, spellchecking will identify and then suggest alternatives. The same algorithms that determine similarity between words also help with spell checking.

With the `typoChecker.getCorrections()` method, you need to provide the word and a number of possible matches to return. If you don’t provide a number, it will provide all possible matches.

```
const nlpTools = require('natural');
const wordStore = ['cat', 'dog', 'elephant', 'giraffe'];
const typoChecker = new nlpTools.Spellcheck(wordStore);


console.log(typoChecker.getCorrections('elephnt', 2));
console.log(typoChecker.getCorrections('grffe', 2)); 
```

Output:

```
[ 'elephant' ]
[ 'giraffe' ]
```

## Conclusion

This is but a brief intro to the Natural library. These are the building blocks you need to get started on building your first simple chat app or text-processing tool. If you found this tutorial easy to understand, you may be ready to start exploring more advanced libraries like [compromise](https://github.com/spencermountain/compromise) or [nlp.js](https://github.com/axa-group/nlp.js).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)