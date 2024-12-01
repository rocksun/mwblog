# How to Use the JQ Command to Speed Developer Workflows
![Featued image for: How to Use the JQ Command to Speed Developer Workflows](https://cdn.thenewstack.io/media/2024/11/73d841f1-jq-playground-lead-1024x576.png)
Working with JSON objects can be a complex everyday task for both developers and platform engineers. Developers often need to automate workflows that incorporate JSON data, such as processing API responses, generating configuration files or analyzing logs. Meanwhile, platform engineers use JSON to create automated workflows, self-service actions and more within their platforms and portals.

While the [simplicity of JSON](https://thenewstack.io/an-introduction-to-json/) attracted engineers at the outset, [processing JSON data](https://thenewstack.io/working-with-json-data-in-python/) introduced some complexity. The difficulty in working with JSON files, particularly with larger data sets, is that it is hard to locate and manipulate the information you need. To deal with this, engineers copy and paste parts of the JSON file to calculate totals or write complex scripts for simple tasks, but this is a time-consuming process that is prone to errors that subsequently impact developer workflows.

, a command-line JSON processing tool, was introduced as a response to this. It empowers developers to easily manipulate data, whether that’s extracting information from a server’s response or the number of available replicas for a deployment. [jq](https://www.getport.io/glossary/what-is-jq)`jq`
embeds these tasks in shell scripts or pipelines, which are not compatible with JSON directly.
Thus, `jq`
provides a consistent way to handle JSON without leaving the command line. And since `jq`
was launched, interactive `jq`
playgrounds that let you experiment with JQ commands and filters in real time have launched, providing immediate feedback to help you learn, test and debug complex JSON transformations.

## JQ Use Cases
There are multiple ways to use JQ to speed up developer workflows. For the purposes of this article, I’ll be talking specifically about building developer workflows in an [internal developer portal](https://thenewstack.io/improve-developer-onboarding-with-an-internal-developer-portal).

### 1. Filtering and Extracting Data From JSON API Responses
If you frequently work with APIs that return large JSON payloads, `jq`
helps you filter and extract only the relevant pieces of information, making it easier to work with and analyze the data. This can be helpful especially when building workflows in an internal developer portal, as you can locate exact fields and data points more quickly with `jq`
than you could with a simple JSON file.

For example, say you’ve integrated GitHub into an internal developer portal to make the backlog more actionable. You want to surface the GitHub issue with the most comments to the top of your backlog list and use the title of each GitHub issue to organize them.

You can do this using the [GitHub API](https://docs.github.com/en/rest?apiVersion=2022-11-28). Pass the API request in with this `jq`
command:

In return, the API output should be:

### 2. Transforming JSON Structures into Input for Other Tools
In many cases, you’ll need to reformat your JSON data structure to match the structure required by another tool or service. `jq`
speeds up this process by allowing you to create new JSON objects, manipulate arrays and convert data formats quickly.

Continuing with the above example, you can clean up the `issue`
object from GitHub to include only the fields you deem important into your Slack message automation.

Here is the input:

The `jq`
command to transform this JSON payload should look like:

Finally, the output includes only the fields you want to share in a Slack message:

Now your portal will assist in prioritizing your backlog by sending Slack messages that alert sprint planners to GitHub issues with comments to prioritize them.

### 3. Automating Configurations and Environment Variables
`jq`
can be used in shell scripts to read, modify and write JSON configuration files. It’s particularly useful in CI/CD pipelines where you need to adjust JSON configuration dynamically.
Here is an example `jq`
command:

You can also modify your configuration like:

### 4. Validating and Pretty-Printing JSON
If you need to quickly check whether a JSON file is properly formatted, or if you know you need to make it more readable and don’t want to do it manually, you can use `jq`
to validate and format JSON with a single command. This is especially helpful when debugging issues with malformed JSON or just reviewing data.

## Get Up to Speed Using a JQ Playground
`jq`
playgrounds are online environments where you can test and experiment with `jq`
commands and filters. A playground allows you to experiment with `jq`
commands in real time, helping you quickly see how different filters, pipes and operators behave. This hands-on, trial-and-error approach helps you learn the syntax and functionality of `jq`
more effectively than just reading documentation.
By providing a visual environment, playgrounds allow you to build and test `jq`
queries in smaller, more manageable pieces before combining them into a larger script. You can also use comments and white space to break down complicated queries, making it easier to understand how different parts of your `jq`
code work together.

Playground environments are also helpful for recall and retention because you are able to immediately see the results of your `jq`
queries in practice, making it easier to identify and fix errors. Since you can iteratively test small changes, this step-by-step feedback helps you debug complex transformations without the overhead of saving files, running commands and waiting for output.

Playground environments make it easier to explore deeply nested or irregular JSON data. You can try different paths and transformations on the fly, immediately see the output and adjust your approach as needed. This makes it much easier to understand and navigate complex JSON without needing to write and rerun scripts repeatedly on the command line.

## Using a JQ Playground
Here is an example of using a JQ playground

If you want to experiment with JQ commands and filters, use [this JQ playground](https://jq.getport.io/). And if you want to discuss other ways of speeding up developer workflows, join [the Port Community](https://port-community.slack.com/ssb/redirect).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)