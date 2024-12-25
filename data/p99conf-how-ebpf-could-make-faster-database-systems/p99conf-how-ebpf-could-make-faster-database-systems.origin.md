# P99Conf: How eBPF Could Make Faster Database Systems
![Featued image for: P99Conf: How eBPF Could Make Faster Database Systems](https://cdn.thenewstack.io/media/2024/10/0a44ad98-p99conf-1024x719.png)
One day in the future, database systems may soon get a speed boost thanks to the emerging [eBPF technology](https://thenewstack.io/ebpf/).

Although [eBPF](https://ebpf.io/) was originally created for in-kernel packet filtering, researchers are finding other potential uses for the technology, which provides a sandboxed execution environment for event-driven programs that run directly within the kernel itself.

One use could be for rerouting database operations around the operating system, which has long been a bottleneck for databases.

“Over the last 50 years, operating systems have been making the lives of database engineers absolutely miserable because the operating system is making certain design choices and imposing its will upon any user space application like a database system,” explained [Andy Pavlo,](https://www.cs.cmu.edu/~pavlo/) associate professor at Carnegie Mellon University, [speaking](https://www.p99conf.io/session/the-next-chapter-in-the-sordid-love-hate-relationship-between-dbs-and-oses/) at [ScyllaDB](https://www.scylladb.com/?utm_content=inline+mention)‘s [P99 CONF](https://www.p99conf.io/) held earlier this week.

In his talk, Pavlo introduced BPF-DB, an in-memory key-value data store that can be planted within the OS kernel itself via eBPF, thereby routing around the restrictions and limitations of an OS’s user space, or the space in memory where a program is typically run.

“Because we don’t have to copy things into user space, it is much faster,” Pavlo said.

The research team behind the project plans to release the bits as open source in the new year, to go along with a paper that is being published.

## Databases vs. Operating Systems
In its role of managing the resources of the computer, an OS must make decisions about how to allocate resources across multiple competing applications. Not every app can always get the memory and processing it wants.

This has always been a sore point among database designers, who feel the database is the most important application that an OS is running (and sometimes rightfully so).

“The OS only wants to crush the database’s spirit and impose [its] iron will on them.”

—Andy Pavlo
“The bottom line is that operating system services in many existing systems are either too slow or inappropriate,” [PostgreSQL](https://thenewstack.io/postgresql-17-gets-incremental-backup-sql-queries-for-json/) founder [Michael Stonebraker](https://thenewstack.io/dr-michael-stonebraker-a-short-history-of-database-systems/) wrote in 1991.

Pavlo pointed out that OS people aren’t too fond of the database people either, noting chief [Linux](https://thenewstack.io/Linux/page/2/) kernel maintainer [Linus Torvalds](https://thenewstack.io/linus-torvalds-on-security-ai-open-source-and-trust/) once quipped that database people “seldom have any shred of taste,” grumbling over the work he had to do on the ASYNC I/O kernel API which was seemingly only used by database designers for non-blocking data writes.

Database systems are rife with workarounds, such as memory management, to deal with OS limitations.

“Pick your favorite system, there is probably something like this in there,” Pavlo said.

So, naturally, research to build faster database systems has gone in the direction of interacting with the kernel as little as possible by minimizing the number of system calls as possible and other techniques.

One early approach has been in kernel-bypass techniques, in which many of the functions typically handled by the kernel are handled in the database system itself, usually by libraries such as Intel’s [DPDK](https://www.dpdk.org/) and [SPDK](https://spdk.io/).

This approach has had its limitations though, Pavlo said. This approach requires a lot of duplicative work, and debugging can be a pain ([SycllaDB](https://www.scylladb.com/) offers DPDK as an option).

## User Bypass
The research team’s BPF-DB takes the opposite approach, where you put a database system within the OS itself.

Instead of copying the data into user space so it can be processed by the database system logic, the database logic within the kernel itself processes the data, eliminating a lot of copying of data.

“Instead of pulling DBMS data to user-space, push DBMS logic to kernel-space,” Pavlo said.

eBPF provides the secret sauce to making this happen.

It allows the user to write event-driven programs, using eBPF libraries, that execute in the kernel space itself, and can be called from within the application via trace points or interrupts.

In this approach, the most frequent database operations can then be executed by the kernel itself.


Instead of database users making individual connections into the database system itself, they can be routed to a in-kernel proxy, which bundles and database changes to the database.

“These alleviates much of the pressure from the database system,” he said. “Because we don’t have to pay that cost to get things up to user space, we are able to achieve much better performance.”

Pavlo said some operations still must be completed in user space, such as password authentication.

Building this sort of eBPF program wasn’t possible five years ago, Pavlo said, but the eBPF Application Binary Interface (ABI) has grown much richer since then.

## Introducing BPF-DB
BPF-DB is a fully-transactional data store, that can be used as a frontend-for-backend database, such as Redis (“Think of it as [RocksDB](https://thenewstack.io/instagram-supercharges-cassandra-pluggable-rocksdb-storage-engine/) for eBPF,” Pavlo said). It comes with a set of database operators (BEGIN, SET, GET, COMMIT) accessible by API, and the data is captured in kernel-resident hash tables. Data is then pushed into user space so it can be committed to long-term storage.


In early tests, the research team found BPF-DB doubled the throughput (operations-per-second) of Redis, and equaling that the high-performance Redis clone [Dragonfly](https://www.dragonflydb.io/), while also offering full transactional capability. Latency was lower than Redis and Dragonfly as well.

“We really think eBPF is the final thing we need to break off the shackles of problematic design choices of operating systems, and to start injecting more sophistication into the kernel to do the things we want it to do,” Pavlo said.










[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)