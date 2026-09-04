**Growing datasets and public benchmarks** are making it harder to tell whether a model is being tested on something it hasn’t seen before.

On Thursday, Google DeepMind showed off what the company calls the first [double-blind evaluation](https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/) of a proprietary frontier-class AI model. The setup keeps Gemini’s model weights hidden from the evaluators while the test questions are hidden from Google.

The pilot tested Gemini 2.5 Flash Lite against private benchmarks from MLCommons and the Singapore AI Safety Institute, but rather than using the results to tout a new Gemini score, Google is focusing on how the tests were run, with neither side having access to the other’s data.

## Benchmark leakage inflates scores

Google’s technical report cites earlier research that found signs of benchmark leakage in about half of the 31 models tested, and another study published this year that found contamination can inflate scores, particularly for larger models. This dynamic has already [raised questions about where certain post-training coding gains actually come from](https://thenewstack.io/glm-5-3-post-training-coding/).

Keeping benchmarks private would seem like the obvious answer, except closed models make that difficult. With a closed model, evaluators usually have to run their questions through the provider’s API, which means the company can see a test that was supposed to stay private, whereas running it independently would require the provider to hand over its model weights. Google’s setup is meant to give both sides another option.

> Keeping benchmarks private would seem like the obvious answer, except closed models make that difficult.

## How the enclave works

The pilot is using Google Cloud Confidential Space together with an NVIDIA H100 Confidential GPU and Intel TDX host memory encryption.

Google DeepMind provides Gemini with its weights and inference code, while the evaluator offers its benchmark prompts and evaluation code; these are then transmitted over encrypted connections into the enclave, where the evaluation takes place without either party gaining access to the other’s protected assets.

The model weights are stored in hardware-encrypted GPU memory, and the evaluation prompts are kept in encrypted host memory as well. After the test is complete, the evaluator is given the permitted results, and the temporary environment can then be destroyed.

Before either side sends over its private data, remote attestation verifies that the enclave is running the software they agreed on.

## Code controls beyond encryption

The enclave protects what’s stored in memory, but the code running inside it can still create problems. If an application has unrestricted network access, for example, it could send sensitive information somewhere else.

OpenMined’s PySyft handles that part of the process by allowing Google and the evaluator to approve the code in advance and to block sensitive parts of the evaluation from making external connections.

That process takes some work, although compute doesn’t appear to be the problem. The paper puts the overhead at less than 5% and instead points to legal agreements and code reviews between organizations as some of the bigger hurdles to running these evaluations.

The researchers eventually want to make attestation much less hands-on, comparing the goal to the HTTPS lock icon in a browser, where the security checks happen without the user having to deal with the underlying hashes and keys.

Google still has a hand in verification because, although the Confidential Space guest OS is open source and its build process has been externally validated, individual builds rely on private signing keys and can’t be independently reproduced. At the same time, Google’s own services are used to sign and verify the attestation report.

> The paper puts the overhead at less than 5% and points instead to the legal agreements and code reviews between organizations as some of the bigger hurdles to running these evaluations.

## Scaling past one GPU

So while the system reduces how much the two sides need to trust each other, it doesn’t remove trust entirely from the equation. Some of it simply moves elsewhere, including to the hardware itself. There is still some trust involved in the hardware itself, including the assumption that the cloud provider and the hardware maker aren’t working together to circumvent the protections.

Then there’s the benchmark itself. MLCommons points out that it still needs to be carefully managed, no matter how well the questions are protected.

The pilot ran Gemini 2.5 Flash Lite on a single H100 80GB Confidential GPU. Still, the researchers are already looking at clusters of H100 and B200 GPUs connected via encrypted links to eventually evaluate models that are too large to fit on a single GPU.

If this approach catches on, developers could have another way to [look beyond the benchmark score](https://thenewstack.io/gemini-3-7-flash-agents/), with some proof that the company behind the model didn’t see the test before the results came out.

> If this approach catches on, a benchmark score could offer some proof that the company behind the model didn’t get to see the test first.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)