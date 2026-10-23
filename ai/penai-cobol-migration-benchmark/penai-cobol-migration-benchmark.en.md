**This week, OpenAI put COBOL in the spotlight.** It [announced](https://openai.com/index/low-resource-programming-languages/) benchmark results suggesting its latest models are getting much better at migrating COBOL programs and building software in languages with less code and documentation for models to learn from.

On OpenAI’s own COBOL migration test, GPT-6.1 Sol reached 86.6% accuracy at low reasoning effort, up from GPT-5.6 Sol’s 5.4%, while costing 39% less. At higher reasoning effort, the newer model reached 97.9%.

But the evidence behind the two evaluations is uneven.

OpenAI has *not* published the details of its evaluation of COBOL (“Common Business-Oriented Language”; the programming language that AI coding tools may help maintain or migrate). It *has* released the MultiLangBench setup and test suite on [GitHub](https://github.com/openai/MultiLangBench). That benchmark tests whether models can build a SQLite-compatible database engine from scratch across 20 programming languages.

OpenAI’s announcement calls the results “substantial improvements across both evaluations, delivering much higher accuracy at lower cost.”

Those results could matter to teams maintaining and modernizing legacy software. But without public COBOL test cases, developers cannot independently inspect that evaluation.

## **Is there finally some hope for modernizing COBOL?**

Per OpenAI, its new COBOL migration evaluation “tests whether a model can migrate existing programs to another language while preserving their behavior.” Specifically, it’s testing migrations from COBOL to C++, Java, Kotlin, Python, and Rust.

To succeed, each migration must pass a series of hidden tests that require “byte-for-byte parity on observable outputs.” And with markedly greater accuracy than its predecessor, GPT-6.1 Sol is, indeed, showing substantial progress.

![](https://cdn.thenewstack.io/media/2026/10/a7ebc9bc-cobol-migration-performance.png)

Source: OpenAI

The measured gains are striking, though OpenAI is not the first company to bring AI to COBOL modernization.

Even though COBOL underpins much of the world’s financial transactions and business records — [IBM](https://www.ibm.com/think/topics/cobol) reports COBOL underpins over 40% of all online banking systems, supports 80% of in-person credit card transactions, and handles 95% of all ATM transactions — it remains a difficult target for AI coding tools.

Compared with Python and JavaScript, models have less COBOL code and documentation to learn from. Experienced COBOL developers can also be hard to find, and documentation often lags behind the systems they maintain.

## **AI coding gains across 20 languages**

Alongside its COBOL migration tests, OpenAI developed a second evaluation to measure models’ ability to build software from scratch, MultiLangBench. This benchmark “tests whether a model can build a SQLite-compatible database engine across 20 different programming languages.”

First, the program gets a database and SQL query. Then, it produces a modified database. The reference SQLite implementation serves as the ground truth to check if the resulting database contains the expected data.

![](https://cdn.thenewstack.io/media/2026/10/6d2a35c9-average-test-pass-rate-multilangbench.png)

Source: OpenAI

On average, GPT-6 Astra — [OpenAI’s flagship model](https://thenewstack.io/openai-gpt6-astra-benchmarks/) — achieved an 87.4% test pass rate across 20 programming languages, a hefty jump from GPT-5.6 Sol’s modest 26.8%. It scored above 83% on 19 out of 20 languages and made improvements on all of them.

[GPT-6 Luna](https://thenewstack.io/openai-gpt-6-sol-luna-release/), predictably, didn’t do as well as Astra, with the lower-cost option only achieving an average pass rate of 40.3%. That said, it did manage to outperform GPT-5.6 Sol on every language tested, with an approximate 78% lower estimated API cost.

## **All right, then. Keep your secrets.**

OpenAI reports promising results from its COBOL migration evaluation and MultiLangBench, but benchmarks don’t tell the whole story. As of Thursday, [Real-SWE 1.1](https://realswe.withspecific.com/), which uses private codebases, lists Claude Opus 5.5 in first place at 56.8% resolution. An [earlier Real-SWE run](https://thenewstack.io/real-swe-coding-benchmark/) covered by *The New Stack* had a different leader and lower scores.

Plus, developers still can’t inspect OpenAI’s COBOL migration benchmark. The announcement credits feedback from developers and enterprise customers for guiding the work, but without the underlying tests and dataset, outsiders can’t independently check the results.

OpenAI acknowledges a key limitation, noting that “applying it to production software still requires expert review and testing against the system’s business rules and dependencies.”

OpenAI is entering a field others have been working on for some time. Anthropic outlined how Claude Code could assist COBOL modernization on [February 23](https://claude.com/blog/how-ai-helps-break-cost-barrier-cobol-modernization). As *The New Stack* reported, AWS introduced [AI agents](https://thenewstack.io/aws-launches-new-ai-agents-to-simplify-legacy-migrations/) for mainframe migrations in 2024.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)