Nothing matches the dread of checking a perfectly green observability dashboard with sub-100ms latency, right before an enterprise client emails you a screenshot of your AI lying to their users.

Exactly six months ago, my team delivered a Retrieval-Augmented Reality model for a fintech customer. Our task was to create a system capable of ingesting thousands of highly unstructured PDFs containing financial reports, extracting critical data from them, computing embeddings, and storing everything in a vector database to fuel the internal Q&A chatbot.

The system worked flawlessly at first.

Then the chatbot began answering queries about the firm’s 2022 performance while citing data from 2018. The bot also attributed revenue earned by the client’s competitors to its subsidiaries. What made this really scary was the fact that the system [retrieved information from the vector](https://thenewstack.io/writer-coms-graph-based-rag-alternative-to-vector-retrieval/) database correctly.

And it wasn’t the RAG pipeline’s fault. We poisoned our database with garbage due to a faulty autonomous ingestion engine.

Here’s a post-mortem of building a completely reliable system that produces nothing but garbage.

## What went wrong: the ingestion hallucination

Our ingestion workflow followed a standard AI pipeline. Once a PDF was placed in our S3 bucket, the ingestion process would trigger an extraction agent to run. The extraction agent (with the help of a widely used frontier-LLM) was tasked with extracting text chunks from the document and returning the corresponding metadata:  `document_type`, `fiscal_year`, `company_entity`, and a `summary` in JSON form.

These metadata values were subsequently appended to the text chunks and then sent to the vector store for embedding.

Our mistake was treating a probabilistic extraction process as deterministic. This meant that when the LLM failed to recognize an illegible fiscal year in a poorly scanned PDF, it didn’t throw an exception. Rather, it did what LLMs tend to do; they made guesses. In this case, the guess about the fiscal year was “2024.”

> “Our mistake was treating a probabilistic extraction process as deterministic.”

Since we were embedding the hallucination along with the extracted text, it became clear that we had created high-speed [searches for documents](https://thenewstack.io/build-rag-document-search/) that didn’t exist.

## Why it was surprising: the failure of “LLM-as-a-judge”

The AI echo chamber loves the concept of “LLM-as-a-judge.” The prevailing wisdom says that if you don’t trust an LLM’s output, you simply put another LLM in front of it to double-check the work.

We had implemented exactly this. Before the data was added to the vector database, a secondary “Validator Agent” evaluated the extracted JSON against the raw text.

So why did the hallucinations slip through? Because we vastly underestimated **LLM Sycophancy.**

When we reviewed the logs, we saw the Validator Agent consistently agreeing with the Extractor Agent. If the Extractor output `{"fiscal_year": 2024}`, the Validator would scan the text, fail to find a year, and, instead of rejecting the payload, would internally rationalize: “*Well, the first model must have seen something I missed*.”

It turns out that using a probabilistic model to police another probabilistic model doesn’t give you a firewall; it gives you a confirmation bias loop.

## What didn’t work: the “prompt engineering” trap

Our first reaction was that we could solve this engineering problem through prompt engineering.

> “It turns out that using a probabilistic model to police another probabilistic model doesn’t give you a firewall; it gives you a confirmation bias loop.”

We made several hotfixes on the system prompt of the Validator agent:

* *“DO NOT HALLUCINATE”*
* *“If you are not sure 100% certain of the metadata, output NULL”*
* *“You are a strict financial auditor. Guessing results in high penalties.”*

Not surprisingly, our attempt ended in utter failure. The LLM became overly defensive. Instead of extracting valid entries, it began rejecting perfectly good data. And with the reasoning steps included, our API expenses went up by 40%.

To expect that a mathematical matrix would follow a strict schema was lazy thinking on our part.

## What finally worked: code over prompts

It became clear that we needed to remove all decision-making authority from the validation process. Data pipelines depend on fixed data contracts rather than probabilities.

We replaced the Validator LLM with a deterministic Python component based on Pydantic and the relational database we were already using. We forced the LLM to split out what it thought was the most likely answer, but we treated its output as user input from an HTML form.

1. **Strict pydantic grounding**. A naive Pydantic check just makes sure a year is between 2000 and the current year. But that doesn’t [stop an LLM from hallucinating](https://thenewstack.io/3-ways-to-stop-llm-hallucinations/) “2024” for a 2018 document. To fix this, we required the `fiscal_year` to physically exist in the raw text using a regex grounding check.

```

import re
from pydantic import BaseModel, Field, model_validator
from typing import Optional
from datetime import datetime


class ExtractedMetadata(BaseModel):
    raw_text: str = Field(exclude=True) # Keep out of final DB payload
    company_entity: str
    fiscal_year: Optional[int]
    
  model_validator(mode='after')
def ground_year_in_text(self) -> "ExtractedMetadata":
if self.fiscal_year is not None:
# Step 1: Bounds Check (Catch impossible years)
current_year = datetime.now().year
if not (2000 <= self.fiscal_year <= current_year):
raise ValueError(f"Year {self.fiscal_year} is out of bounds.")

# Step 2: Grounding Check (Catch plausible hallucinations)
# Find all 4-digit numbers in the raw text that look like recent years
years_in_text = [int(y) for y in re.findall(r'\b(20\d{2})\b', self.raw_text)]

if self.fiscal_year not in years_in_text:
raise ValueError(
f"Hallucination detected: {self.fiscal_year} does not exist in source text."
)
return self

```

2. **Deterministic cross-referencing. Regarding the** **company\_entity** **field, we decided that the LLM should no longer be fully trusted for** its spelling. We took the LLM’s suggestion for what it was and did a fuzzy string match against our hardcoded SQL database of our client’s real entities.

The tricky engineering thing was that we needed to avoid spamming our Dead Letter Queue (DLQ) with actual competitor analysis. In other words, if the document in question was analyzing “Acme Corp” (our client’s competitor), we certainly did not want the fuzzy string matcher to incorrectly interpret that as “Alpha Corp” and throw it into the DLQ. So, how did we do this? We got the LLM to add an `is_competitor` boolean flag. And then if it was a client entity, it needed to match at least 95% against the SQL DB; otherwise, it would get tossed into the DLQ.

3. **Quarantine by default.** The pipeline architecture was redesigned so that nothing from the extraction queue is placed into the vector database. Everything was moved to an intermediate PostgreSQL table. However, only those messages that meet the requirements of Pydantic grounding were embedded.

## What I’d do differently

If I were architecting this from scratch today, my fundamental philosophy would be different: **Never use an LLM for a task that a simple `IF` statement, regex rule, or standard database constraint can solve.**

The industry is suffering from a severe “golden hammer” syndrome with Generative AI. We are delegating critical data integrity checks to systems designed to be creative storytellers

**The ultimate takeaway**: Probabilistic systems require deterministic boundaries.

We redesigned the pipeline architecture. No extraction data went directly into the vector database. All data had to be temporarily staged in a PostgreSQL table. Embedding occurred only for payloads that had successfully met the Pydantic grounding constraints and DB validation checks.

> “The ultimate takeaway: Probabilistic systems require deterministic boundaries.”

You can allow the LLM  to extract, analyze, and summarise information. However, whenever data needs to be written to storage as ground truth, it must pass a more stringent, traditionally engineered barrier. Replacing our “Validator Agent” with the new Pydantic grounding and SQL check cut out data poisoning immediately, reduced our API expenses by 50%, and made us create an AI product our enterprise client could trust.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.