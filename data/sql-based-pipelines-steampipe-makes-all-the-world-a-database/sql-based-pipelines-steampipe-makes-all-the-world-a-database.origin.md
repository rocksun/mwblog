# SQL-Based Pipelines: Steampipe Makes All the World a Database
![Featued image for: SQL-Based Pipelines: Steampipe Makes All the World a Database](https://cdn.thenewstack.io/media/2024/06/9de8c55f-api-hero-image.png)
Many companies have their own API for programmatic access — numerous enterprise SaaS applications, hyper-scaler cloud services, and developer services like GitHub. But all of these APIs work differently, and they require imperative code in languages like Python, Java or C#. Wouldn’t it be cool if all those services could be made to look like relational databases, enabling inspection of them using declarative SQL, along with reporting and visualization of their content with popular business intelligence (BI) tools?
Plain old SQL could become a domain-specific language for numerous platforms across the internet.
With this approach, plain old SQL could become a domain-specific language for numerous platforms across the Internet. Cross-referencing different aspects of platforms could be achieved with joins, honing in on specific application items could be implemented using a WHERE clause, and a SELECT column list would allow you to bring back just the specific attributes of those items that you were interested in.
## Plumbing Internet Services with SQL-Based Pipelines
In fact, there’s a great open source option for doing that. It’s called
[Steampipe](https://steampipe.io/) and it works really well, with an ecosystem of [over a hundred service-specific plug-ins](https://hub.steampipe.io/#search) for platforms like Airtable, GitHub, Jira, LinkedIn, and Kubernetes; database services including MongoDB Atlas and Snowflake (for administrative data, rather than data in the databases); and querying data from file-based sources like CSV files and Google Sheets.
Now there’s an even easier way to work with Steampipe, by installing extensions to either Postgres or SQLite.
Getting all of this to work is as simple as installing Steampipe into a Linux environment (including
[Windows Subsystem for Linux](https://learn.microsoft.com/windows/wsl/about)), then pulling down the plug-ins for the services you’re interested in and running SQL queries interactively. Simple documentation makes it easy to understand the table schemas supported by each plug-in, putting details of various online services just a SQL query away.
And now there’s an even easier way to work with Steampipe, by installing Steampipe plug-in-specific extensions to either
[Postgres](https://www.postgresql.org/) or [SQLite](https://www.sqlite.org/index.html). This allows you to query the corresponding services right from within these two well-known databases, instead of needing the separate SQL interface implemented by the conventional version of Steampipe. This makes possible not just federated joins between the data from various services, but also between these services and your *own* data.
The possibilities are vast and arise not just at the SQL prompt, but from any BI tool that can talk to Postgres (essentially, all of them). Meanwhile, the SQLite implementation makes it possible to query this data in a range of minimalist Linux environments.
## Practical Applications
The set of use cases that apply here is huge. For example, imagine getting a list of customers, with their IDs, that you’re tracking in Salesforce, then joining that into customer and sales records in an on-premises line-of-business database.
A funny thing happens when you turn information into tabular data: not only does it become query-able by developers and business intelligence tools, but it becomes usable in other domains.
Then imagine getting statistics on code check-ins for specific developers in a particular GitHub repo, and storing those aggregate figures in your HR system and/or reporting on them in a dashboard that you built in a tool like Tableau or Power BI.
Here’s another: searching Slack conversations for mentions of an internal application and cross-referencing that with open tickets in Zendesk for the same application.
## Near-Instant SQL Gratification
Want some techie specificity? We can do that real fast. Installing the standalone Steampipe variant is as easy as running a
**curl** command at the command line. Afterwards, use the **steampipe plugin install** command to install a plugin of your choice and take care of any necessary authentication and connection details. From there, just type **steampipe query** to get an interactive prompt for entering SQL queries.
If you find that all pretty simple (and you should) take note that working with Steampipe in SQLite or Postgres is even easier, since you will likely already have those databases installed.
I spoke with
[Jon Udell](https://www.linkedin.com/in/jon-udell-45915), an evangelist for [Turbot](https://turbot.com/), the company behind Steampipe *(Editor: he’s also a contributor to The New Stack, including writing articles about SQL)*. Udell took me step-by-step through the product’s capabilities, and how to install and use it, to the point where I had it running on my own machine. If you’re interested in the details, read on as we explore a specific example, copied directly from the steps I successfully executed on my own computer, with Udell’s support.
## Do It Yourself
To work with Steampipe with SQLite or Postgres, all you need to do is install a plug-in-specific extension and configure the connection particulars. Then you can start querying immediately, right from your existing database environment. For example, to perform discovery from SQLite on assets in a Microsoft Azure cloud account, simply follow these steps:
1. From the Linux shell, execute the following command to install a plug-in-specific SQLite extension:
|
1
|
sudo /bin/sh -c "$(curl -fsSL https://steampipe.io/install/sqlite.sh)"
(The above may look arcane, but you can simply copy it from above or from
[here](https://steampipe.io/downloads?install=sqlite), and paste it.)
2. When prompted for the plugin name, simply type “azure” and tap Enter, then tap Enter twice more to accept default values for version and the install location.
3. Enter the following Azure CLI command to authenticate:
|
1
|
az login
Next, enter your credentials into the resulting browser window.
4. Now, start up SQLite and, from its prompt, load the plug-in’s extension with the command:
|
1
|
.load <install folder>/steampipe_sqlite_azure.so
(where <install folder> is the folder you were in during step 1.)
5. Now set your azure subscription with
|
1
|
SELECT steampipe_configure_azure('subscription_id="<subscription id>"');
Replace <subscription id> with the actual subscription ID in your Azure tenant that you’d like to explore.
6. That’s it! You’re now ready to interrogate all kinds of Azure assets. For example, to list all the Azure blobs in a particular Azure Storage account (essentially providing a huge recursive directory listing), use the following SQL query:
|
1
2
3
4
5
|
SELECT name, container_name, storage_account_name, region, type, is_snapshot
FROM azure_storage_blob
WHERE resource_group=<resource group>
AND storage_account_name=<storage account name>
AND region=<azure region>;
Make sure, of course, to replace <resource group>, <storage account name> and <azure region> with the appropriate strings for your own environment (and don’t forget the quotes, if you’re hard-coding those values.)
## Even Easier from Here
That’s all there is to it. Plus, steps 1 and 2 will never have to be repeated and steps 3, 4 and 5 won’t need to be run again until you’re in a new SQLite session. That means you’re free to execute a range of subsequent SQL queries to get a rich set of additional information about your Azure environment.
Want to install another plug-in extension? Just repeat the above procedure but enter a different plug-in name, then start up SQLite, load the appropriate
**steampipe_sqlite_xxx.so** extension, configure it with the appropriate **steampipe_configure_xxx** function and start querying. Each steampipe plug-in has simple documentation, listing all query-able tables, and providing a slew of sample queries that you can copy, paste, edit and run.
## Mashup Nirvana
A funny thing happens when you turn information into tabular data: not only does it become query-able by developers and business intelligence tools, but it becomes usable in other domains, including spreadsheets, no-code/low-code platforms, workflow systems, and even machine learning and AI platforms. Imagine building a predictive model about developer productivity based on observed check-ins to public GitHub repos or discussions in company Slack channels.
Once you make things look like rows and columns, all kinds of possibilities emerge. Steampipe has established a growing ecosystem that enables those scenarios elegantly and robustly.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)