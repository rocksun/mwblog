# Monitor Your System Health From Python’s Command Line
![Featued image for: Monitor Your System Health From Python’s Command Line](https://cdn.thenewstack.io/media/2025/06/ca124f6f-ahmed-nvkeryvt3ck-unsplash-1-1024x683.jpg)
[Python](https://thenewstack.io/python/)’s `psutil`
library is a powerful tool for getting real-time insight into your system’s performance. You can use it in custom scripts, applications or directly from the [command line](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/).
Using `psutil`
in the [command line interface (CLI)](https://thenewstack.io/guis-cli-apis-learn-basic-terms-of-infrastructure-as-code/) gives you speed, simplicity and flexibility. It’s especially useful for developers, system administrators and DevOps engineers who live in the terminal. It’s also a great entry point for beginners learning the CLI and exploring their system’s resource usage.

You might choose `psutil`
in the CLI over other methods when:

- You need diagnostics on the fly, like during a sudden CPU spike or unexpected memory usage.
- You want to integrate system checks into shell scripts or cron jobs (for example, to detect zombie processes).
- You prefer minimal setups instead of complex monitoring stacks.
There are more reasons to use `psutil`
in the CLI, and many apply to other CLI-based scripts as well:

- No GUI, less overhead. CLI scripts are lightweight, fast and work across platforms including Windows, macOS and Linux.
- Tailor scripts to exactly what you care about — CPU usage, memory pressure, disk I/O or running processes — and output them however you like: plain text, logs or JSON.
- Automation ready. CLI-based
`psutil`
scripts plug easily into cron,`systemd`
timers, CI/CD pipelines or remote monitoring setups over SSH.
## Using `psutil`
in the CLI
First, make sure `psutil`
is installed.

Before you can use the terminal to check system health metrics, you need to run Python interactively.

Type `python3`
in the terminal to get started:

### Checking CPU Usage
Is your laptop fan running unexpectedly? It might be time to check CPU usage. High CPU activity generates heat, which triggers the fan. This could mean a background process is stuck in a loop, or worse, malware is running silently and consuming your resources.

Other signs include general sluggishness or system unresponsiveness, sudden temperature spikes or noticing zombie and defunct processes.

The code below uses `psutil`
’s `cpu_percent()`
function. The `interval=1`
means it measures CPU usage over one second to give a more accurate reading. The function returns the percentage of CPU in use, and the print statement shows it as a readable string:

This will show you the percentage of CPU you’re currently using.

### Checking Memory Usage
Just like with the CPU, if your system feels slow or apps freeze or close unexpectedly, it could be time to check memory usage. High memory warnings are a clear sign to look into it.

In the code below, `psutil.virtual_memory()`
fetches your memory stats, including total, used and available RAM. The print statements convert the values from bytes to gigabytes for easier reading:

### After You Detect High Memory Usage
You can run this anytime, but it’s especially helpful after spotting high memory consumption. It shows which processes are using the most RAM.

The code goes through all running processes, filters out those not using memory, and prints a list of the ones that are, sorted by the highest memory use at the top:

### Save Disk Usage Report to a Log
This is useful when you want to track slow-growing storage issues, understand when usage spikes happen, feed monitoring and alerting systems or just collect disk data automatically with minimal impact.

The code first gets the current date and time. Then `psutil.disk_usage('/')`
pulls disk stats for the root partition (you can change `/'`
to any path). It formats the time in ISO standard, then opens a file called disk_report.log in append mode so existing data stays intact:

You can also schedule this as a cron job to run regularly:

## Conclusion
Using `psutil`
in the CLI offers a fast, flexible way to monitor your system’s health. It’s a practical step toward staying on top of system performance with minimal setup and maximum control.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)