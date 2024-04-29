# Generate PowerPoints using Llama-3 — A first step in automating slide decks
## Automating Presentations using LLMs and Python-pptx
In the corporate world slides are everywhere, it is often used as a way to communicate idea and achievements. I have personally worked for big multinational corporations for the past 4 years, and making slides is something most people do every week.
That would not be a huge issue if slides were an effective use of time. There are plenty of people who will detract from this but in my opinion, slides consume too much time in most companies. An employee could have used that time actually executing on projects and building stuff.
*Looking for someone to solve your problem related to Large Language Models & data science? Click here:* [https://form.jotform.com/240744327173051](https://form.jotform.com/240744327173051)
## RAG pipeline
Python has a library called Python-pptx which allows users to programmatically create PowerPoint presentations. Prompting large language models to use this library and generate executable code, would be the first step.
In this pipeline we would be taking a corpus of information, which in this case is a book on CFA exam. The end goal for this exercise is to load the page, extract the text and use an LLM to generate code that creates a slide for the page.
from llama_index.core import SimpleDirectoryReader
#you can use any PDF/text document for this excercise
reader = SimpleDirectoryReader(input_files =['CFA_Fundamentals_2nd_Edition.pdf'])
docs = reader.load_data()
In order for better retrieval, it is advised that you perform some pre-processing on your documents. Chunk-size, removing unnecessary information and spacing, would enable better retrieval.
Llama-Index has a variety of LLM integrations to choose from, for this project I decided to go with open-source Model llama-3 70 via Groq. You can get a free API from Groq website.
from llama_index.llms.groq import Groq
# Initiating the LLM instance, Groq takes in two parameters, model and api_key
llm = Groq(model="llama3-70b-8192", api_key="<insert_your_api-key")
Next step is to feed the documents into a vector-store, which will create a retriever.
from llama_index.core import VectorStoreIndex
# Creates an Index for the documents
index = VectorStoreIndex.from_documents(docs)
For the first output, we want the LLM to use our query and give a structured output as a Header, and three bullet-points. The Pydantic library allows you to create the output layer which is fed into the query engine.
from typing import List, Field
from pydantic import BaseModel, Field
# Creating a Pydantic object for structured output
class Extract(BaseModel):
title: str = Field(description="Title for the information retrieved")
bullet_points: List[str] = Field(description="Three bullet-points for the information")
## First LLM call
Building the prompt
from llama_index.core import PromptTemplate
# The prompt
template = (
"We have provided context information below. \n"
"---------------------\n"
"{context_str}"
"\n---------------------\n"
"Given this information, please generate a header, and 3 bullet points for the {query_str}\n"
"Also fetch sub_titles and numbers to describe the information"
)
qa_template = PromptTemplate(template)
# Building the Query Engine, passing in the Prompt and Pydantic model
query_engine = index.as_query_engine(similarity_top_k=3,llm=llm,text_qa_template=prompt,response_mode='tree_summarize', output_cls=Extract)
# Query and response
response=query_engine.query("BlackSholes Option Pricing Formula")
## Second LLM Call
Now pass the output of the LLM into another LLM call which would output the python-pptx code.
# response.header
from llama_index.core import PromptTemplate
from llama_index.core.program import LLMTextCompletionProgram
#Another Pydantic model to extract output
class Python_code(BaseModel):
comments: str = Field(description='Comments about the code')
code:List[str] = Field(description='Python-pptx code')
template = (
"We have provided information below. \n"
"---------------------\n"
"{title}"
"{bullet_points}"
"\n---------------------\n"
"Given this information, please generate python-pptx code for a single slide with this title & bullet points\n"
"Separate the bullet points into separate texts"
"Do not set font size"
)
#This Program would allow to feed the prompt with headers and bullet-points
program = LLMTextCompletionProgram.from_defaults(
output_cls=Python_code,
prompt_template_str=template,
verbose=True,
llm=llm
)
#Feeding the response of the previous LLM call
output =program(title=response.title, bullet_points=response.bullet_points)
exec(output.code)
Next step is to improve the output of the RAG application using few-shot examples and additional functionality like charts/shapes. If you like the project, please follow for updates.