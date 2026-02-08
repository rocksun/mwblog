It was Monday morning when our analytics team started noticing something wrong. Customer transaction volumes had apparently skyrocketed over the weekend, up 4,700% according to the dashboards. Impossible numbers were everywhere. Our fraud detection system was flagging thousands of suspicious patterns. The executive team was already asking questions.

I pulled up the logs with a sinking feeling. Sure enough, our production [data pipeline](https://thenewstack.io/part-1-the-evolution-of-data-pipeline-architecture/) had processed Saturday’s data not once, not twice, but 47 times between Saturday afternoon and Monday morning.

## **The Investigation**

The first clue was in the Airflow DAG (directed acyclic graph) history. Every few hours over the weekend, a task had failed, triggered a retry and then succeeded. Normal behavior, except that each “successful” retry processed the same date’s data again and again.

I started digging through our PySpark job logs. The execution timestamps told the story: Saturday at 2 p.m., Saturday at 5 p.m., Saturday at 8 p.m., Sunday morning, Sunday afternoon. Each run showed the same execution date in the logs but was reprocessing Saturday’s transactions. The pipeline was supposed to be idempotent. We’d spent weeks building retry logic specifically to handle transient failures gracefully. Yet here we were with 47 copies of the same data sitting in our [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) warehouse.

## **The Root Cause**

Our retry logic had a subtle but critical bug. Here’s what was supposed to happen:

1. Task fails (network timeout, temporary error, etc.)
2. Airflow triggers retry.
3. Task re-runs with the same execution date.
4. Data gets reprocessed, deduplication logic handles it.

What was actually happening:

1. Task fails processing Saturday’s data.
2. Our “smart” fallback logic kicked in: “If the current date fails, process the last successful date instead.”
3. Task succeeded — processing Saturday’s data again.
4. Next scheduled run: “Process Sunday’s data, but if that fails, fall back to Saturday…”
5. Sunday processing failed (different issue).
6. Fallback processed Saturday again.
7. Repeat 47 times.

The fallback logic seemed reasonable when we wrote it. “Always deliver something” felt safer than “fail completely.” We didn’t realize we’d created a loop where temporary failures would cause us to repeatedly process stale data.

## **The Debugging Process**

Finding the bug took longer than it should have because the pipeline showed “success” in Airflow. Every task is completed with a green checkmark. The data was landing in Snowflake. From a workflow perspective, everything looked fine.

The breakthrough came when I compared execution dates in our logs with the actual data dates in the processed files. They didn’t match. Tasks marked “execution\_date=2024-11-10” were processing data from “data date=2024-11-09”.

Once I saw that discrepancy, the fallback logic became obvious. I found the code:

```
try: 
data = load_data(execution_date) 
except DataNotAvailableError: 
logger.warning(f"Data for {execution_date} not available, using previous date") 
data = load_data(previous_successful_date)
```

This seemed defensive. But it violated a critical principle: The execution date and the data date must always match.

## **TheFix**

The solution had three parts:

1. **Remove the fallback logic entirely.** If data isn’t available for the execution date, the task should fail. Period.

No clever workarounds.

2. **Make idempotency explicit.** We added a merge operation in Snowflake using the execution date as part of the deduplication key:

```
MERGE INTO target_table t 
USING source_data s 
ON t.transaction_id = s.transaction_id 
AND t.execution_date = s.execution_date 
WHEN MATCHED THEN UPDATE ... 
WHEN NOT MATCHED THEN INSERT ...
```

3. **Add execution date validation.** Every stage of the pipeline now validates that it’s processing the correct date:

```
def validate_execution_date(data, expected_date): 
actual_date = data['date'].max() 
if actual_date != expected_date: 
raise ExecutionDateMismatchError( 
f"Expected {expected_date}, got {actual_date}"
```

## **The Recovery**

Cleaning up 47 copies of the same data wasn’t trivial. We couldn’t just delete everything and reprocess. We had 46 duplicate copies mixed with legitimate data from Sunday and Monday.

We ended up writing a cleanup script that identified duplicates by transaction ID and execution date, keeping only the first occurrence of each transaction for Saturday. It took six hours to run and required careful validation afterward.

## **What I Learned**

* **Idempotency requires discipline.** It’s not enough to say “our pipeline is idempotent.” Every retry, every fallback, every “clever” error handling needs to maintain the guarantee: same input → same output.
* **Test with weekend data.** Our tests all ran with consecutive weekdays. Saturday and Sunday have different data patterns, lower volumes, different transaction types, different timing. If we’d tested with weekend data, we would have caught this immediately.
* **Fail loudly on data mismatches.** The execution date and data date should always match. When they don’t, something is deeply wrong. Failing fast would have prevented 46 unnecessary retries.
* **Monitor successful runs too.** We had alerts for failures, but we weren’t monitoring whether successful runs were processing the correct data. We’ve since added data quality checks that validate the date range of processed data.
* **Beware of** **“****defensive****”** **code.** The fallback logic seemed reasonable: always deliver something rather than nothing. But in data pipelines, delivering the wrong data is often worse than delivering nothing at all.

## **The Aftermath**

Three months later, our pipeline has better monitoring, clearer error messages, and ironically, simpler retry logic. We removed the “clever” fallbacks. Tasks either succeed with the correct data or fail explicitly.

The incident cost us a weekend of manual cleanup and some uncomfortable conversations with stakeholders about data quality. But it taught the entire team a valuable lesson about the difference between “working” code and reliable production systems.

If your retry logic includes phrases like “fall back to” or “use previous data instead,” take a closer look. You might be one failed task away from your own 47x incident.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/01/48f919ce-cropped-ab56d8b4-pradeep-kalluri-600x600.jpeg)

Pradeep Kalluri is a data engineer at NatWest Bank in London, building production data pipelines for banking operations. He previously worked at Accenture delivering enterprise data platforms. He's passionate about data quality, pipeline reliability and open source contributions with merged...

Read more from Pradeep Kalluri](https://thenewstack.io/author/pradeep-kalluri/)