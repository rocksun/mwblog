Microsoft flagged a phishing campaign last week that exploits a gap in how machines read text. Attackers are slipping invisible Unicode tag characters into email bodies; they don’t render on screen but change the underlying string that software processes.

The company says attackers are already using the technique at scale to bypass spam filters and ML-based classifiers, and the same approach could cause problems for AI systems that regularly ingest text from external sources.

## Tag characters split keywords

Security researchers have documented a nearly identical technique targeting LLMs, commonly called “ASCII Smuggling,” which uses Unicode tag characters in the U+E0000 to U+E007F range — code points that exist in the character stream but aren’t displayed by most interfaces.

That gives you two versions of the same text: what a person reads and what software receives.

For example:

```
Human view:     funding  
Under the hood: fun⟨U+E0020⟩ding
```

In the [campaign tracked by Microsoft Defender for Office 365](https://www.microsoft.com/en-us/security/blog/), attackers weren’t using tag characters to smuggle hidden instructions into an AI model. They placed them inside high-signal words associated with financial phishing, such as “funding,” “loan,” and “credit,” so that filters scanning for those terms would no longer find an exact match.

A hunting signature for ASCII Smuggling fired on roughly 21,000 messages the day before the campaign started and the next day, it fired on more than 1.3 million. Then, just two days later, the count passed 2.3 million. The whole time, [recipients saw ordinary-looking offers](https://thenewstack.io/npm-supply-chain-worm-attack/) for business loans and credit lines.

> Just two days later, the count passed 2.3 million.

## Tokenizers parse them differently

NLP systems break text into tokens before processing it, and slipping an unexpected Unicode character into a word can change how those tokens are formed. [Researchers have already shown](https://thenewstack.io/encrypted-prompt-injection-grok/) that encoding techniques can hide adversarial content from AI systems, although Microsoft’s campaign uses the trick for a different purpose.

> NLP systems break text into tokens before processing it, and slipping an unexpected Unicode character into a word can change how those tokens are formed.

Exactly what happens depends on the tokenizer. Some may ignore the tag character while others split the surrounding text differently, so developers have to test the models they’re actually using rather than assume they’ll all behave the same way.

Running the text through standard Unicode normalization won’t necessarily remove the tags, either. NFC and NFD can clean up different representations of the same character, but they weren’t designed to strip Unicode tag characters, which means those tags can still make it through to the next step.

## Agents lack email’s defenses

Email providers have other ways to spot a suspicious message beyond the words it contains, but an AI pipeline may be working with far less information.

That then becomes a problem when agents are pulling in outside text and using it to decide what to do next because those invisible characters buried in the text can change how it gets processed along the way, while also making a hidden prompt injection much harder for someone looking at the original to catch.

## Normalize before the model

For applications that have no reason to accept characters in the `U+E0000` to `U+E007F` range, the simplest approach is to remove them before the text reaches the model, although that gets trickier when an application has a legitimate reason to keep them.

In those cases, developers can compare the original text with a version that has the tags removed and look for anything that changed, while also testing the tokenizer their application actually uses to see how it handles the same characters. Whatever gets cleaned should stay that way [through the rest of the pipeline](https://thenewstack.io/go-language-ai-agents/), rather than checking one version of the text and then sending the untouched original to the LLM.

## The subdivision flag edge case

Stripping every Unicode tag character isn’t always safe because some serve a legitimate purpose. The subdivision flag emojis for England, Scotland and Wales rely on invisible tag-character sequences to render, and Microsoft’s initial hunting signature was broad enough to trip on those flags before the team carved out an explicit exception.

> Stripping every Unicode tag character isn’t always safe because some serve a legitimate purpose.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)