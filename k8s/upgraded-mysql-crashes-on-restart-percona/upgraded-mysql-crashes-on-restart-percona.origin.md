# Upgraded MySQL Crashes on Restart: Percona
![Featued image for: Upgraded MySQL Crashes on Restart: Percona](https://cdn.thenewstack.io/media/2024/07/2fe2e1bc-percona-mysql-1024x536.jpg)
We all love upgrading to a fresh version of our favorite software, but large-scale MySQL users may want to hold off on updating to the latest build of that database system (v9.0) until after a severe bug is squashed, lest they won’t be able to restart their databases at all.

An apparent bug in [MySQL](https://thenewstack.io/oracle-support-for-mysql-5-7-ends-soon-key-upgrades-in-8-0/) is severe enough that [Percona](https://www.percona.com/?utm_content=inline+mention) is advising users not to upgrade until [Oracle](https://developer.oracle.com/?utm_content=inline+mention), which manages the open source relational database system, fixes the issue.

The database performance company discovered that upgrading [MySQL](https://thenewstack.io/a-cheat-sheet-to-database-access-control-mysql/) to either versions 8.0.38, 8.4.1 or the recently released 9.0.0 will cause the database daemon to crash after restarting, at least in those cases where the database has 10,000 tables or more.

Once crashed, the server won’t restart, which could be very problematic for those organizations relying on the database for mission-critical operations.

“We have not yet identified the root cause or a workaround. As such, we suggest that all users do not adopt any of the MySQL versions mentioned until a fix is released,” wrote Percona High Availability Practice Manager [Marco Tusa](https://www.linkedin.com/in/marcotusa/?originalSubdomain=ca) in a [customer advisory](https://www.percona.com/blog/do-not-upgrade-to-any-version-of-mysql-after-8-0-37/).

A bug report (#[115517](https://bugs.mysql.com/bug.php?id=115517) Note: this page is now hidden) has been filed with [Oracle](https://thenewstack.io/oracle-introduces-new-app-analytics-platform-enhances-analytics-cloud/), which took the issue offline, presumably to investigate it further. Percona will conduct additional tests as well to further characterize the issue.

Percona has also opened a [Jira ticket](https://perconadev.atlassian.net/browse/PS-9306) to gather more data about the problem. There, the company posted instructions on how to (safely) reproduce the bug, first by using Docker to spin up an MySQL instance, and then firing up a ChatGPT-generated script to create 12,000 tables.

Percona’s own test was conducted on a local server running SSD disks. The company marked the issue as “critical” on Thursday.

## Could It Be an innoDB Issue?
A second Percona engineer suspected it might be related top an earlier bug that Percona encountered (#[115569](https://bugs.mysql.com/bug.php?id=115569)) in which a MySQL boot process will slow to a crawl if more than 8,000 tables are loaded, due to how the [innoDB](https://thenewstack.io/multi-version-concurrency-control-mvcc-design-decisions/) storage engine calls multiple threads for its check process.

The [Hacker News conversation](https://news.ycombinator.com/item?id=40938061) that ensued from this announcement pointed out that 10,000 tables is not that unusually large amount of tables to put in a database, and if there are limits to how many tables MySQL can handle, then those should be documented somewhere.

[MySQL](https://www.mysql.com/) is Oracle’s open source general use relational database system (apart from the company’s own flagship, eponymously-named, [commercial database system](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/cncpt/introduction-to-oracle-database.html)). Although open source, MySQL development and maintenance is managed by Oracle itself. The latest version of MySQL, 9.0 was [released earlier this month](https://linuxiac.com/mysql-rdbms-9-0-released).
The DB Engines site [estimates](https://db-engines.com/en/system/MySQL) that MySQL is the second most widely used database system worldwide, trailing only [Oracle RDBMS](https://db-engines.com/en/system/Oracle) in usage.

Percona’s business model is providing high-performance services and support for database systems such as [MySQL](https://www.percona.com/mysql), [MongoDB](https://www.percona.com/mongodb) and [Postgres](https://www.percona.com/postgresql). And such, the company’s engineers [tend to uncover issues](https://www.percona.com/blog/) in these systems early on, sometimes even before the maintainers themselves.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)