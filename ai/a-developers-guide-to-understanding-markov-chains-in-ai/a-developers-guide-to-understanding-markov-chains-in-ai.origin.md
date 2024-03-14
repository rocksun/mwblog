# A Developer’s Guide to Understanding Markov Chains in AI
![Featued image for: A Developer’s Guide to Understanding Markov Chains in AI](https://cdn.thenewstack.io/media/2024/03/e02889d6-fre-sonneveld-k8ihtzoikq4-unsplash-1024x683.jpg)
Muscling in on the theoretical mathematics used in
[Artificial Intelligence](https://thenewstack.io/3-vectors-of-artificial-intelligence-and-machine-learning/) (AI) can help you transition towards the skills that AI developers use. Or at least, it can help you appreciate what is going on behind the scenes.
There is quite a lot of mathematics (and the terminology derived from it) in AI — though most of it is conceptual, not algebraic. Nevertheless, we don’t want to dig deeply into it, rather just peer around the edges so we become a little less blind-sided by technical white papers.
Andrei Andreevich
**Markov** was a Russian mathematician (and strong chess player) whose work on processes and probability preceded modern computing, but have been gratefully exploited since.
Any process can be simplified into
**states** and **transitions**, and while these are naturally good for computers, it is actually how humans explain narratives too. We don’t try to explain things in real-time, we just jump to the events that matter. For instance, if we take the narrative “John walked to the shops, he entered the baker, bought some bread, entered a deli and bought a sandwich, said hi to a friend, left the shops and returned home,” this makes sense to us. But there is no time information whatsoever, just an ordered **series of events**.
We can summarise John’s state at any time as one of these:
- Traveling (to and from shops)
- Shopping (buying some bread, or a sandwich)
- Chatting (with friends)
And we can summarise the transitions as:
- From home to shops and back.
- From one shop to another.
- From shopping to chatting and back to shopping.
We’ve kind of created zones where John is transitioning to and from. To John, these are all normal daily things. If a nosy neighbor observed a number of John’s similar journeys, they would look random, even though they are only made from a small set of options. John’s journeys might be described as a
**stochastic** process.
Let’s leave John back at home for a moment. Here is a Wikipedia definition of a Markov chain: “A Markov chain or Markov process is
**a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event**.”
In other words, what happens next only depends on what happens before. Now if we consider John’s journeys from that nosy neighbour’s perspective, it would seem that whatever he did next was only really dependent on what he was doing at the time. For instance, he would only bump into a friend and have a chat if he was already near the shops.
![](https://cdn.thenewstack.io/media/2024/03/e186b34b-untitled.png)
John’s journey
Note that there are different chances of the options occurring from each state, but if we add up each possibility from each state it adds up to 100%. Note that John can go from shop to shop, so the transition points to the state it just left. And the same for chatting. When the neighbor looks, John only seems to go from home to the shops, so that transition is the only option available — hence 100%.
If I produce a series of random numbers between 1 and 100, and allot each option appropriately, then we can “walk with John” so to speak. So I asked
[Claude 3](https://www.anthropic.com/news/claude-3-family) to help:
So here is the walk, starting from home.
|Random number
|John’s journey event
|42
|John goes to the shops
|87
|John goes from one shop to another
|16
|John returns home
|64
|John goes to the shops
|29
|John goes from one shop to another
And one last thing; mathematicians like to convert this type of model into a
**matrix.** The percentage chance is always seen as a decimal between 0 and 1.
|traveling
|shopping
|chatting
|traveling
|0
|1
|0
|shopping
|0.2
|0.75
|0.05
|chatting
|0
|0.85
|0.15
- The
**transition matrix**is always a square matrix or n-by-n matrix, where the size is determined by the number of possible states.
- The row represents the current state, the column represents the next state.
- The total probability for each current state (i.e. a row) is 1.
So when is a Markov chain useful for solving problems? Basically, when you want to model something that’s in discrete states, but you don’t understand how it works.
You may well think, “But John knows what he is doing, doesn’t he?” But we are observing John (from the nosy neighbor perhaps) and from an observer’s point of view, John’s actions do seem random. The mathematics isn’t seeking to understand anything, it is just a platform from which to make predictions.
Some of these basics we have seen in
[state machines](https://thenewstack.io/state-machines-for-devs-from-blockchain-to-aws-to-tv-sets/), though these are normally modeling internal software states, not real-life systems.
## How Markov Chains Are Used in AI
Markov chains are used as the design for predictive text. As more words are typed in and gained by the model, a new set of statistics is attached to an updated Markov chain.
Note that the letters in the alphabet do not change even as extra words are added. Just the probability weightings alter, and some new transitions appear. When doing my bad
[Shakespeare generator](https://thenewstack.io/beware-chatgpt-a-language-model-in-the-shape-of-shakespeare/), I covered a little of this. We used a **corpus of** Shakespeare’s sonnets, and then tried to calculate some weights.
When we are using predictive text in the English language, it is more likely that we look at the current two letters, and work with those. We obtain a more refined model by allowing the probability of choosing each successive letter to depend on the preceding letter or letters. Hence we use “tokens” not single letters.
So a Markov model of order
*2* predicts that each letter occurs with a fixed probability, but that probability can depend on the previous two consecutive letters ( **). You may also have come across the term k-gram** **ngram**. For example, if our corpus includes 100 occurrences of “th”, with 60 occurrences of “the”, 25 occurrences of “thi”, 10 occurrences of “tha”, and 5 occurrences of “tho”, the model predicts that the next letter following the 2-gram “th” is “e” with probability 0.6, “i” with probability 0.25, “a” with probability 0.1, and “o” with probability 0.05. ![](https://cdn.thenewstack.io/media/2024/03/59f6aebb-untitled-2-750x1024.png)
the, this, tha or tho
In the case of sentence completion in the Google Search bar, the corpus is the world’s search terms. But this corpus is so large, that incorrect spellings can be spotted too — making the system a little different overall.
![](https://cdn.thenewstack.io/media/2024/03/cc366506-untitled-3-1024x289.png)
You complete me.
If you have done a reasonable amount of development, you will feel comfortable with much of this, as linked chains of information pop up in different guises from time to time. By getting back to the mathematics, you should find that future AI developments have less of a mysterious past.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)