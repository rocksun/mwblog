Among the myriad abilities that humans possess, which ones are uniquely human? Language has been a top candidate at least since Aristotle, who wrote that humanity was “the animal that has language.” Even as large language models such as ChatGPT superficially replicate ordinary speech, researchers want to know if there are specific aspects of human language that simply have no parallels in the communication systems of other animals or artificially intelligent devices.

In particular, researchers have been exploring the extent to which language models can reason about language itself. For some in the linguistic community, language models not only *don’t* have reasoning abilities, they *can’t*. This view was summed up by Noam Chomsky, a prominent linguist, and two co-authors in 2023, when they [wrote in *The New York Times* (opens a new tab)](https://www.nytimes.com/2023/03/08/opinion/noam-chomsky-chatgpt-ai.html) that “the correct explanations of language are complicated and cannot be learned just by marinating in big data.” AI models may be adept at using language, these researchers argued, but they’re not capable of analyzing language in a sophisticated way.

![Portrait of Gašper Begus](https://www.quantamagazine.org/wp-content/uploads/2025/10/Gasper-Begus-cr-Jami-Smith-V2.webp)

Gašper Beguš, a linguist at the University of California, Berkeley.

That view was challenged in a recent [paper (opens a new tab)](https://ieeexplore.ieee.org/document/11022724) by [Gašper Beguš (opens a new tab)](https://vcresearch.berkeley.edu/faculty/gasper-begus), a linguist at the University of California, Berkeley; [Maksymilian Dąbkowski (opens a new tab)](https://maksymilian-dabkowski.github.io/), who recently received his doctorate in linguistics at Berkeley; and [Ryan Rhodes (opens a new tab)](https://wavyphd.com/about) of Rutgers University. The researchers put a number of large language models, or LLMs, through a gamut of linguistic tests — including, in one case, having the LLM generalize the rules of a made-up language. While most of the LLMs failed to parse linguistic rules in the way that humans are able to, one had impressive abilities that greatly exceeded expectations. It was able to analyze language in much the same way a graduate student in linguistics would — diagramming sentences, resolving multiple ambiguous meanings, and making use of complicated linguistic features such as recursion. This finding, Beguš said, “challenges our understanding of what AI can do.”

This new work is both timely and “very important,” said [Tom McCoy (opens a new tab)](https://ling.yale.edu/profile/tom-mccoy), a computational linguist at Yale University who was not involved with the research. “As society becomes more dependent on this technology, it’s increasingly important to understand where it can succeed and where it can fail.” Linguistic analysis, he added, is the ideal test bed for evaluating the degree to which these language models can reason like humans.

## **Infinite Complexity**

One challenge of giving language models a rigorous linguistic test is making sure they don’t already know the answers. These systems are typically trained on huge amounts of written information — not just the bulk of the internet, in dozens if not hundreds of languages, but also things like linguistics textbooks. The models could, in theory, simply memorize and regurgitate the information that they’ve been fed during training.

To avoid this, Beguš and his colleagues created a linguistic test in four parts. Three of the four parts involved asking the model to analyze specially crafted sentences using tree diagrams, which were first introduced in Chomsky’s landmark 1957 book, *Syntactic Structures*. These diagrams break sentences down into noun phrases and verb phrases and then further subdivide them into nouns, verbs, adjectives, adverbs, prepositions, conjunctions and so forth.

One part of the test focused on recursion — the ability to embed phrases within phrases. “The sky is blue” is a simple English sentence. “Jane said that the sky is blue” embeds the original sentence in a slightly more complex one. Importantly, this process of recursion can go on forever: “Maria wondered if Sam knew that Omar heard that Jane said that the sky is blue” is also a grammatically correct, if awkward, recursive sentence.

Recursion in Nature

**R**ecursion is not only a key element in language, but also a feature of the natural world. On Victoria Island in northern Canada, for example, one can find an island in a lake that’s on an island. But that island is also in a lake on an island. The (unnamed) innermost island is the largest known “third order” island, and it has sometimes been jokingly referred to as Inception Island, after the 2010 film directed by Christopher Nolan in which characters travel to dream worlds inside dream worlds inside dreams.

![](https://www.quantamagazine.org/wp-content/uploads/2025/10/Metallinguistics_SideBar-crMarkBelan-Desktopv5-01.svg)

Recursion has been called one of the defining characteristics of human language by Chomsky and others — and indeed, perhaps a defining characteristic of the human mind. Linguists have argued that its limitless potential is what gives human languages their ability to generate an infinite number of possible sentences out of a finite vocabulary and a finite set of rules. So far, there’s no convincing evidence that other animals can use recursion in a sophisticated way.

Recursion can occur at the beginning or end of a sentence, but the form that is most challenging to master, called center embedding, takes place in the middle — for instance, going from “the cat died” to “the cat *the dog bit* died.”

Beguš’ test fed the language models 30 original sentences that featured tricky examples of recursion. For example: “The astronomy the ancients we revere studied was not separate from astrology.” Using a syntactic tree, one of the language models — OpenAI’s o1 — was able to determine that the sentence was structured like so:

> **The astronomy [the ancients [we revere] studied] was not separate from astrology.**

The model then went further and added another layer of recursion to the sentence:

> **The astronomy [the ancients [we revere [who lived in lands we cherish]] studied] was not separate from astrology.**

Beguš, among others, didn’t anticipate that this study would come across an AI model with a higher-level “metalinguistic” capacity – “the ability not just to use a language but to think about language,” as he put it.

That is one of the “attention-getting” aspects of their paper, said [David Mortensen (opens a new tab)](https://www.cs.cmu.edu/~dmortens/), a computational linguist at Carnegie Mellon University who was not involved with the work. There has been debate about whether language models are just predicting the next word (or linguistic token) in a sentence, which is qualitatively different from the deep understanding of language that humans have. “Some people in linguistics have said that LLMs are not really doing language,” he said.  “This looks like an invalidation of those claims.”

## **What Do You Mean?**

McCoy was surprised by o1’s performance in general, particularly by its ability to recognize ambiguity, which is “famously a difficult thing for computational models of language to capture,” he said. Humans “have a lot of commonsense knowledge that enables us to rule out the ambiguity. But it’s difficult for computers to have that level of commonsense knowledge.”

A sentence such as “Rowan fed his pet chicken” could be describing the chicken that Rowan keeps as a pet, or it could be describing the meal of chicken meat that he gave to his (presumably more traditional) animal companion. The o1 model correctly produced two different syntactic trees, one that corresponds to the first interpretation of the sentence and one that corresponds to the latter.

The researchers also carried out experiments related to phonology — the study of the pattern of sounds and of the way the smallest units of sound, called phonemes, are organized. To speak fluently, like a native speaker, people follow phonological rules that they might have picked up through practice without ever having been explicitly taught. In English, for example, adding an “s” to a word that ends in a “g” creates a “z” sound, as in “dogs.” But an “s” added to a word ending in “t” sounds more like a standard “s,” as in “cats.”

In the phonology task, the group made up 30 new mini-languages, as Beguš called them, to find out whether the LLMs could correctly infer the phonological rules without any prior knowledge. Each language consisted of 40 made-up words. Here are some example words from one of the languages:

> θalp  
> ʃebre  
> ði̤zṳ  
> ga̤rbo̤nda̤  
> ʒi̤zṳðe̤jo

They then asked the language models to analyze the phonological processes of each language. For this language, o1 correctly wrote that “a vowel becomes a breathy vowel when it is immediately preceded by a consonant that is both voiced and an obstruent” — a sound formed by restricting airflow, like the “t” in “top.”

The languages were newly invented, so there’s no way that o1 could have been exposed to them during its training. “I was not expecting the results to be as strong or as impressive as they were,” Mortensen said.

## **Uniquely Human or Not?**

How far can these language models go? Will they get better, without limit, simply by getting bigger — layering on more computing power, more complexity and more training data? Or are some of the characteristics of human language the result of an evolutionary process that is limited to our species?

The recent results show that these models can, in principle, do sophisticated linguistic analysis. But no model has yet come up with anything original, nor has it taught us something about language we didn’t know before.

If improvement is just a matter of increasing both computational power and the training data, then Beguš thinks that language models will eventually surpass us in language skills. Mortensen said that current models are somewhat limited. “They’re trained to do something very specific: given a history of tokens [or words], to predict the next token,” he said. “They have some trouble generalizing by virtue of the way they’re trained.”

But in view of recent progress, Mortensen said he doesn’t see why language models won’t eventually demonstrate an understanding of our language that’s better than our own. “It’s only a matter of time before we are able to build models that generalize better from less data in a way that is more creative.”

The new results show a steady “chipping away” at properties that had been regarded as the exclusive domain of human language, Beguš said. “It appears that we’re less unique than we previously thought we were.”