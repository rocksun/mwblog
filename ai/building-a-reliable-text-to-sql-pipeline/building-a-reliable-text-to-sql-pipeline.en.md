[![](https://substackcdn.com/image/fetch/$s_!4CFP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F860b74d5-342f-4490-b42b-0d20b853ddfc_788x680.jpeg)](https://substackcdn.com/image/fetch/$s_!4CFP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F860b74d5-342f-4490-b42b-0d20b853ddfc_788x680.jpeg)

Image by Author

Many of our clients are asking for text-to-SQL solutions these days, and it’s become a key part of nearly every project we’ve worked on in the last quarter. While it’s easy to get a language model to generate SQL queries, building a reliable system for enterprise use is a different story. For business-critical applications, we need a high level of accuracy — ideally, over 95% on the first try.

In this blog post, I’ll show you how to build a robust text-to-SQL pipeline from the ground up. And if you’re short on time, I’ll also introduce you to some open-source tools like Vanna.AI that can help speed things up.

This blog is divided into two parts:

1. **Building a text-to-SQL agentic system (with retry & self-correction built-in)**
2. **Enhancing accuracy & reliability for text to SQL.**

This is part one about how to build a text-to-SQL agent, please follow and stay tuned for the next part!

***Note**: There is some confusion around what exactly an agent is. From my developer point of view agent is LLM program with memory and access to external tools. The word agent in this post is interchangeable with “LLM program”.*

> Looking for expert(s) to build custom AI solutions for you?
>
> [Reach out for help](https://tally.so/r/3x9bgo)

**[How to make more reliable reports using AI - A Technical Guide](https://www.firebird-technologies.com/p/how-to-make-more-reliable-reports)***[Technical guide, sharing my experience of working with AI](https://www.firebird-technologies.com/p/how-to-make-more-reliable-reports)*[www.firebird-technologies.com](https://www.firebird-technologies.com/p/how-to-make-more-reliable-reports)

[![](https://substackcdn.com/image/fetch/$s_!bpvR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff80761a8-a3e5-406d-9ce7-10118a4eb5ba_900x709.png)](https://substackcdn.com/image/fetch/$s_!bpvR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff80761a8-a3e5-406d-9ce7-10118a4eb5ba_900x709.png)

Image by Author — The query flow of the system

The text-to-SQL system has three parts:

1. **SQL Agent**: This is a program that takes information from the database and a user’s question, then creates an SQL query.
2. **Error Reasoning Agent**: This program looks at the user’s query and the error it caused, then tries to explain why the query didn’t work.
3. **Error-Fix Agent**: This program uses the explanation from the Error Reasoning Agent and the wrong query to create a corrected version of the SQL query.

There are many ways to build this system, and depending on the specific use case, you may need to design your own process. Here’s why this approach was chosen:

* **Simplicity**: Too much complexity can increase the chances of making mistakes in generating code. Adding more parts to the system can lead to more errors.
* **Safety**: Some might argue the system could work with just two parts — one for generating the SQL and another for fixing errors. While that could work, it’s more prone to failure, especially if the user asks a non-SQL or unrelated question (like trying to “trick” the system). Having a reasoning agent make it “safe”.

**[Building Production-Ready AI Agents & LLM programs with DSPy: Tips and Code Snippets](https://www.firebird-technologies.com/p/building-production-ready-ai-agents)***[A technical guide on how you can use DSPy in production for AI agents & large language model programs](https://www.firebird-technologies.com/p/building-production-ready-ai-agents)*[www.firebird-technologies.com](https://www.firebird-technologies.com/p/building-production-ready-ai-agents)

Feeding the right information to an LLM is key for generating accurate queries. Here’s what you should provide:

1. **Table, Column, and Value Info**: Include table names, column details, and stats like numerical ranges, number of categories, and top values.
2. **Metadata**: Share details about what data each table holds, what each column means, and common errors you might run into.
3. **Queries**: Provide a collection of example queries and their SQL outputs, showing how questions are usually asked and queries written in your organization.

For large enterprise databases, this info can take up a lot of space in the model’s memory. So, focus on passing only what’s directly relevant to the user’s question. You could use a RAG pipeline to pull the most relevant data.

Example of how you can provide dataset information to the LLM.

```
db_info = """### Database Structure:

**Tables:**
1. **salesperson**
   - `salesperson_id` (INT)
   - `name` (TEXT)
   - `region` (TEXT)
   
   **Sample Data**:
   | salesperson_id | name        | region |
   |----------------|-------------|--------|
   | 1              | John Doe    | North  |
   | 2              | Jane Smith  | South  |

2. **timber_sales**
   - `sales_id` (INT)
   - `salesperson_id` (INT, FK to `salesperson`)
   - `volume` (REAL)
   - `sale_date` (DATE)

   **Sample Data**:
   | sales_id | salesperson_id | volume | sale_date  |
   |----------|----------------|--------|------------|
   | 1        | 1              | 120    | 2021-01-01 |
   | 2        | 1              | 150    | 2021-02-01 |
   | 3        | 2              | 180    | 2021-01-01 |

### Key Points:
- **Relationships**: One-to-many between `salesperson` and `timber_sales` via `salesperson_id`.
- **Indexes**: Likely primary keys on `salesperson_id` and `sales_id`.

### Example Query:
- **Total timber sold by each salesperson**:
   ```sql
   SELECT s.name, SUM(t.volume) AS total_sales_volume
   FROM salesperson s
   JOIN timber_sales t ON s.salesperson_id = t.salesperson_id
   GROUP BY s.salesperson_id;
   ```
   
   """
```

For this blog, I choose DSPy but you can use any other framework or the API directly.

Below is the prompt used for the SQL program.

```
class sql_program(dspy.Signature):
    """
You are a text-to-SQL agent designed to generate SQL queries based on user input. You have access to the following database information:

Table, Column, and Value Info
You know the table names, column details (e.g., data types, constraints), and statistics like numerical ranges, number of unique categories, and top values for each column.

Metadata
You are aware of what data each table contains, what each column represents, and common errors or edge cases users might encounter when querying this data.

Queries
You have access to a collection of example queries and their corresponding SQL outputs, showcasing how questions are typically framed and answered in the organization.

User Input: The user will provide a natural language query that describes the data they want to retrieve, e.g., “Show me the top 5 customers who spent the most in the last quarter.”

Your Task:

Analyze the user's query.
Refer to the provided database information (tables, columns, metadata, and examples).
Generate the most accurate SQL query to retrieve the requested data.
Make sure to follow these guidelines:

Ensure accuracy by referring to table names and column names exactly as they appear in the database.
ONLY ANSWER WITH SQL
    
    
    """
    user_query = dspy.InputField(desc="User input query describing what kind of SQL user needs")
    dataset_information = dspy.InputField(desc="The information around columns, relevent tables & metadata that helps answer the user query")
    generated_sql = dspy.OutputField(desc="The SQL query, remember to only include SQL")
```

> Looking for text-to-action AI system? Want me & my team to develop for you?
>
> [Reach out for help](https://tally.so/r/3x9bgo)

You can use a prompt similar to this

```
class error_reasoning_program(dspy.Signature):
    """

**Task:** Given a SQL error message, an incorrect SQL, user query, and database information, generate a series of concise instructions for another agent on how to resolve the issue. 
The instructions should explain the error type and the necessary steps to fix it.



**Input:**
1. **SQL Error Message:** The error generated when the query is executed.
2. **Incorrect Query:** The SQL query that caused the error.
3. **Database Information:** Schema details (tables, columns, data types, etc.).

---

**Output:**  
Provide a **series of concise instructions** that include:

1. **Error Diagnosis:** Briefly describe the issue (e.g., "Column not found in the table").
2. **Analysis:** Identify the root cause (e.g., "The column `age` does not exist in the `users` table").
3. **Solution:** Specify the necessary fix (e.g., "Correct the column name to `dob`").
4. **Verification:** Suggest how to test the fix (e.g., "Rerun the query with the corrected column name").

---

### **Common Error Types & Instruction Patterns:**

1. **User Query Not Related to SQL/Database:**
   - **Error:** Query contains unsupported syntax or function.
   - **Solution:**: Output a query like SELECT "NOT ASKING FOR SQL";.
   
2. **Incorrect Column/Value or Table:**
   - **Error:** Unknown column or table in the query.
   - **Solution:** Correct column/table name or suggest schema verification.
   
3. **Incorrect Datatype Conversion:**
   - **Error:** Mismatch in data types (e.g., string vs integer).
   - **Solution:** Ensure correct data types or use type conversion functions (e.g., `CAST()`).

Think about the error deeply and give a step by step solutions to try

    """
    error_message = dspy.InputField(desc="The SQL engine error message")
    incorrect_sql = dspy.InputField(desc="The failed SQL")
    information = dspy.InputField(desc="user query or question and database information ")
    error_fix_reasoning = dspy.OutputField(desc="The reasoning for why the error and instructions on how to fix it")
```

Example prompt:

```
class error_fix_agent(dspy.Signature):
    """

**Task:** Given a series of instructions from the Error Reasoning Agent, generate a corrected SQL query to resolve the issue described. The corrected query should adhere to the instructions provided and fix the identified error.

---

**Input:**
1. **Instructions from Error Reasoning Agent:** A series of steps outlining the error diagnosis, analysis, and suggested solution.
   - Example Instructions:
     - Error Diagnosis: "Column 'age' is missing in the 'users' table."
     - Solution: "Correct the column name to 'birthdate'."
     - Verification: "Rerun the query with the updated column name."

---

**Output:**
Generate the **corrected SQL query** based on the instructions.

---

### **Example Input:**
- **Instructions:**
  - **Error Diagnosis:** "The column 'age' is missing from the 'users' table."
  - **Analysis:** "Verify the schema for the correct column name."
  - **Solution:** "Correct the query to use an existing column (e.g., 'birthdate')."
  - **Verification:** "Rerun the query with the updated column name."

---

### **Example Output:**

**Corrected SQL Query:**
```sql
SELECT name, birthdate FROM users;
```

---

### **Guidelines for Generating Corrected SQL:**
- **Understand the Error Reasoning:** Use the instructions to determine which part of the query needs to be corrected (e.g., column names, table names, datatypes).
- **Apply the Fix:** Modify the query to address the identified issue (e.g., replace an incorrect column name with the correct one).
- **Check Syntax:** Ensure the corrected SQL query adheres to proper syntax and structure for the given database system.

    """
    instruction = dspy.InputField(desc="The instructions from the agent on how to fix the SQL query")
    generated_sql = dspy.OutputField(desc="The correct and fixed query")
```

Now a system which completes the entire flow and builds the text-to-SQL system.

```
def clean_llm_response(text):
    
    splits = text.split('```')
    # print(splits)
    if len(splits)==1:
        return splits[0].replace('sql','').replace("\n",'')
    else:

        return splits[1].replace('sql','').replace("\n",'')

class agent_system(dspy.Module):
    def __init__(self, max_retry=2):
# initializes the all the values and agents
        self.max_retry = max_retry
        self.sql_agent = dspy.Predict(sql_agent)
        self.error_reasoning_agent = dspy.Predict(error_reasoning_agent)
        self.error_fix_agent = dspy.ChainOfThought(error_fix_agent)
    
# In a DSPy module, the forward function is called when you 'invoke' the program
    def forward(self,query,relevant_context, db_engine):

        df = pd.DataFrame()
# What to return in the end, you can customize
        return_dict = {'response':[], 'sql':[],'error_reason':[], 'df':[]}
        response = self.sql_agent(user_query = query, dataset_information = relevant_context)

        return_dict['response'].append(response)
        
        information = {'user_query':query, 'relevant_context':relevant_context}
        i = 0
# This loop iterates until, max_retry exhausted or query executes
        while i < self.max_retry:
            print("Try "+str(i))
            sql = clean_llm_response(response.generated_sql)
            print(sql)
            try:
                
                return_dict['sql'].append(sql)
# Replace this with whatever db SDK you're using
# This is only for duckDB
                df = db_engine.execute(sql).df()
                return_dict['df'].append(df)
                display(df.head())
                if df.empty:
                    raise Exception("Empty Dataframe")
                else:
                    i=self.max_retry+1

            except Exception as e:
                print("This is the exception"+str(e)[:100])


                error_reason = self.error_reasoning_agent(error_message= str(e)[:-200], incorrect_sql = sql, information = str(information))
# Checks if user asked a SQL based question 
                if 'NOT ASKING FOR SQL' not in error_reason.error_fix_reasoning:

                    return_dict['error_reason'].append(error_reason.error_fix_reasoning)
                    response = self.error_fix_agent(instruction=error_reason.error_fix_reasoning)
                    return_dict['response'].append(response)
                else:
                    i=self.max_retry+1

            i+=1
        return return_dict


```

For this blog, I used the open-source Text-to-SQL dataset provided by [gretelai](https://huggingface.co/datasets/gretelai/synthetic_text_to_sql). However, you can replace this with database information about your DB and query like this

```

# Create a system object
sql_system = agent_system()


# This is how you can call the system, this uses a DuckDB engine, change based on your db SDK
responses = sql_system(query='What is the total volume of timber sold by each of salesperson, sorted by name?',relevant_context=db_info,db_engine=conn)

```

[![](https://substackcdn.com/image/fetch/$s_!g_iZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9547556-e4f5-4fd4-85ef-7eb9579934d2_1350x186.png)](https://substackcdn.com/image/fetch/$s_!g_iZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9547556-e4f5-4fd4-85ef-7eb9579934d2_1350x186.png)

Image by Author — Example output, it took two tries to answer the question. The error is fixed automatically by the system!

> **Did you like how the solution was designed and how the information was presented? If so, would you want an expert like that on your team?**
>
> [Reach out for help](https://tally.so/r/3x9bgo)

And that’s a wrap on part one of the blog! Make sure to subscribe to FirebirdTech so you’ll be the first to know when part two is out!