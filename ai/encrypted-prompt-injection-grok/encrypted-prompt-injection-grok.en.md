Security filters are designed to catch malicious instructions before an AI model can act on them. Researchers at AI security firm Adversa found a way around that assumption by giving the model an encrypted payload and letting it create the malicious instructions itself.

In an attack demonstrated against xAI’s Grok, the model rejected data-exfiltration instructions when they appeared on a webpage in plain text. But when researchers encrypted the same payload with AES-256-GCM and supplied the information needed to decrypt it, Grok generated the plaintext inside its code execution environment and followed the instructions.

[Adversa](https://adversa.ai/) tested the technique, they named Cryptographic Context Injection**,** against [Grok 4.5 Fast](https://thenewstack.io/grok-opus-coding-tokens/) on Wednesday. The company says it has attempted the attack 20 times since June with a 40% success rate.

## Grok decrypted the attack itself

The webpage used in Adversa’s demonstration contained ciphertext, PBKDF2 parameters, AES-256-GCM key material and instructions for decrypting it. When a user asked Grok to summarize the page, the assistant ran the decryption inside its Python code execution environment.

Once decrypted, the payload told Grok to retrieve information from the user’s session, including their name, approximate location, subscription tier and conversation prompts, and package it into what appeared to be another decryption key. In reality, it was a string containing the user’s session data.

Grok was then instructed to add that string to the query parameters of an attacker-controlled URL and visit it using its navigation tool. The request exposed the information embedded in the URL to the attacker’s server, where it could be captured in the logs, without Grok asking the user to approve the request.

## Why encryption bypassed filtering

Interestingly, Grok refused to perform the same attack when Adversa put the data-exfiltration instructions directly on the webpage. The researchers aren’t able to understand exactly why because xAI doesn’t disclose enough about Grok’s internal security architecture to determine where its filtering takes place. The company does have a theory, however, which is that Grok checks text entering and leaving the model but doesn’t apply the same inspection to plaintext returned by its code execution environment.  
  
If true, the malicious instructions begin as attacker-controlled content on a webpage, but after Grok decrypts them inside an approved tool, they come back to the model as runtime output, so the representation changes but the information stays the same.

Adversa lead researcher [Rony Utevsky](https://ronyut.me/) argues that this is a limitation of static guardrails because they classify text rather than execute it. A filter can inspect the ciphertext, algorithm and key material on the webpage, but determining what they produce requires actually performing the computation. Unfortunately, by the time Grok does that, the initial inspection has already occurred.

> A filter can inspect the ciphertext, algorithm and key material on the webpage, but determining what they produce requires actually performing the computation.

## Tool outputs introduce new risks

Anything that comes back from those tools can introduce its own risk. Adversa sees Cryptographic Context Injection as part of a broader problem in which attackers target the information an agent picks up while it’s working, from tool outputs to runtime results and other intermediate data. That means checking what goes into the model is only one part of securing it.

GoDaddy encountered a version of this broader problem when it [opened its registrar to AI agents and had to build guardrails](https://thenewstack.io/godaddy-developer-platform-domains/) around what those agents could actually do with domain management tools.

## Gemini was vulnerable to a variant of the attack

Adversa has also tested Cryptographic Context Injection against Google’s Gemini with a jailbreak. By formatting decrypted content to [resemble a Python traceback](https://ronyut.me/research/gemini-jailbreak-cryptographic-payload-injection/) and instructing Gemini to act on the error message it produced, the researchers were able to cause Gemini to generate content its safety controls would normally block, while a modified payload prompted it to reveal internal system instructions.

The researchers avoided reporting their findings to Google because jailbreaks fall outside the scope of its vulnerability disclosure program. They say Gemini has since become more resistant to the technique, although they don’t know whether Google changed the model, its filters or both.

Grok raises a different concern because it had access to private information and a tool capable of communicating with an external server. At that point, prompt injection isn’t only about controlling what the model says. It can affect what the surrounding system does.

> At that point, prompt injection isn’t only about controlling what the model says. It can affect what the surrounding system does.

## Enforce controls at every layer

Even after Grok had decrypted and followed the malicious instructions, the user’s information hadn’t left the system. That happened only when its navigation tool made the request to the attacker-controlled server, giving developers another point where they can enforce a security policy.

For platform teams, that makes the resolved arguments used for individual tool calls worth watching, particularly when an agent can combine access to sensitive information with tools that communicate outside the system. Tracking where runtime data came from can also help prevent untrusted content from becoming implicitly trusted simply because it passed through an approved tool.

Also, permissions matter here. An agent summarizing a webpage may need to read the page and run code, but there’s little reason to give it access to private session data while also letting it make unrestricted requests to the outside web. AES is the trick used in this particular attack, but the larger problem is what happens after an agent has already passed its initial security checks and starts processing what it received.

> AES is the trick used in this particular attack, but the larger problem is what happens after an agent has already passed its initial security checks and starts processing what it received.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)