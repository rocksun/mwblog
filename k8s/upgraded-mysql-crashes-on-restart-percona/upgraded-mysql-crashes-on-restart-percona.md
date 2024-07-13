
<!--
title: 升级后的 MySQL 在重启时崩溃：Percona
cover: https://cdn.thenewstack.io/media/2024/07/2fe2e1bc-percona-mysql.jpg
-->

Percona 发现将 MySQL 升级到 8.0.38、8.4.1 或最近发布的 9.0.0 版本会导致数据库守护进程在重启后崩溃，至少在数据库拥有 10,000 个或更多表的情况下是如此。

> 译自 [Upgraded MySQL Crashes on Restart: Percona](https://thenewstack.io/upgraded-mysql-crashes-on-restart-percona/)，作者 Joab Jackson。


# Upgraded MySQL Crashes on Restart: Percona

![Featued image for: Upgraded MySQL Crashes on Restart: Percona](https://cdn.thenewstack.io/media/2024/07/2fe2e1bc-percona-mysql-1024x536.jpg)

We all love upgrading to new versions of our favorite software, but large-scale MySQL users might want to hold off on upgrading to the latest version of the database system (v9.0) until a critical bug is fixed, or they won't be able to restart their database.

A glaring bug in [MySQL](https://thenewstack.io/oracle-support-for-mysql-5-7-ends-soon-key-upgrades-in-8-0/) is so severe that [Percona](https://www.percona.com/?utm_content=inline+mention) is advising users to hold off on upgrading until [Oracle](https://developer.oracle.com/?utm_content=inline+mention) (which manages the open-source relational database system) fixes the issue.

The database performance company found that upgrading [MySQL](https://thenewstack.io/a-cheat-sheet-to-database-access-control-mysql/) to versions 8.0.38, 8.4.1, or the recently released 9.0.0 will cause the database daemon to crash after restarting, at least if the database has 10,000 or more tables.

Once crashed, the server will be unable to restart, which could be a major headache for organizations that rely on the database for mission-critical operations.

“We have not yet identified the root cause or a workaround. Therefore, we recommend all users to refrain from adopting any of the mentioned MySQL versions until a fix is released,” Marco Tusa, Percona’s High Availability Practice Manager, wrote in a [customer advisory](https://www.percona.com/blog/do-not-upgrade-to-any-version-of-mysql-after-8-0-37/).

A bug report (#[115517](https://bugs.mysql.com/bug.php?id=115517) Note: This page is now hidden) has been submitted to [Oracle](https://thenewstack.io/oracle-introduces-new-app-analytics-platform-enhances-analytics-cloud/), which has taken the issue offline, presumably for further investigation. Percona will also be conducting additional testing to further describe the issue.

Percona has also opened a [Jira ticket](https://perconadev.atlassian.net/browse/PS-9306) to gather more data on the issue. There, the company has published instructions on how to (safely) reproduce the bug, starting with a MySQL instance launched using Docker, followed by a ChatGPT-generated script to create 12,000 tables.

Percona’s own testing was conducted on a local server running SSD disks. The company flagged the issue as “critical” on Thursday.

## Could it be an innoDB issue?

A second Percona engineer suspects this could be related to an earlier bug (#[115569](https://bugs.mysql.com/bug.php?id=115569)) that Percona encountered, where the MySQL startup process would become very slow if more than 8,000 tables were loaded, due to the [innoDB](https://thenewstack.io/multi-version-concurrency-control-mvcc-design-decisions/) storage engine calling multiple threads for its checking process.

A [Hacker News discussion](https://news.ycombinator.com/item?id=40938061) points out that it’s not uncommon to have 10,000 tables in a database, and if there are limits on the number of tables MySQL can handle, then those limits should be documented somewhere.

[MySQL](https://www.mysql.com/) is Oracle’s open-source general-purpose relational database system (aside from the company’s own flagship, the eponymous [commercial database system](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/cncpt/introduction-to-oracle-database.html)). While open-source, MySQL’s development and maintenance are managed by Oracle itself. The latest version of MySQL, 9.0, was [released earlier this month](https://linuxiac.com/mysql-rdbms-9-0-released).

The DB Engines website [estimates](https://db-engines.com/en/system/MySQL) that MySQL is the second most widely used database system globally, behind only [Oracle RDBMS](https://db-engines.com/en/system/Oracle).

Percona’s business model is to provide high-performance services and support for database systems like [MySQL](https://www.percona.com/mysql), [MongoDB](https://www.percona.com/mongodb), and [Postgres](https://www.percona.com/postgresql). As such, the company’s engineers [tend to find issues in these systems early](https://www.percona.com/blog/), sometimes even before the maintainers themselves discover them.

[
YOUTUBE.COM/THENEWSTACK
Technology is moving fast, don’t miss a beat. Subscribe to our YouTube
channel to watch all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)