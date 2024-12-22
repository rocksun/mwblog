# Open Source Innovation Comes to Time-Series Data Compression
![Featued image for: Open Source Innovation Comes to Time-Series Data Compression](https://cdn.thenewstack.io/media/2024/12/5d9932fc-compressed-1024x576.jpg)
Time-series data collection inherently generates [massive storage requirements](https://thenewstack.io/storage/) that can overwhelm organizations. From IoT systems enabling predictive maintenance to weather tracking systems and personal fitness apps, these monitoring solutions accumulate vast amounts of real-time information — often collecting multiple data points per second, with storage costs mounting exponentially.

While traditional data compression provides some relief from these [storage demands](https://thenewstack.io/cloud-native/the-most-popular-cloud-native-storage-solutions/), the industry has long needed a more effective solution. Recognizing this challenge, NetApp Instaclustr collaborated with the University of Canberra through the [OpenSI initiative](https://opensi.net/) to develop the [Advanced Time Series Compressor](https://github.com/instaclustr/atsc) (ATSC) — an open source innovation that fundamentally reimagines high-volume time-series data compression.

Here’s what to know and how to use it.

**Loss for the Win**
The current landscape of time-series compression is dominated by lossless solutions like LZ4, DoubleDelta and ZSTD — tools designed to preserve data with perfect fidelity. ATSC embraces an often-overlooked reality: Most time-series data already incorporates some degree of loss, whether through inherent limitations in data collection, deliberate under-sampling or routine data management processes like rollover and averaging.

With this insight, ATSC implements a sophisticated lossy compression approach. Rather than storing complete data sets, it generates mathematical functions that closely approximate the original data patterns, storing only the essential parameters of these functions. This approach is paired with granular configurability — users can precisely tune their desired level of accuracy, balancing storage efficiency with data fidelity based on their specific use cases. The result is decompressed data that, while not identical to the original, maintains the accuracy necessary for practical analysis and decision-making.

Consider a real-world example of temperature monitoring data. The figure below compares traditional lossless storage with ATSC’s approach, demonstrating how ATSC captures the essential temperature patterns and gradual changes typical of system metrics. While the ATSC version uses significantly less storage space, it maintains the key characteristics needed for meaningful analysis — the peaks, valleys and overall trends remain clearly visible and analytically valuable.

![Lossless vs. ATSC temperature data](https://cdn.thenewstack.io/media/2024/12/42db9105-image1.png)
Lossless vs. ATSC temperature data

## ATSC’s Architecture
At its core, ATSC employs a sophisticated suite of mathematical approaches to compress time-series data: [fast Fourier transforms](https://en.wikipedia.org/wiki/Fast_Fourier_transform) (FFT) for periodic patterns, constant functions for stable readings, Catmull-Rom interpolation for smooth transitions, and inverse distance weighted interpolation for irregular data points. The system intelligently selects the optimal method through rapid statistical analysis of each data segment. Whenever the choice isn’t immediately clear, ATSC benchmarks multiple approaches before selecting the most effective compression method.

A key innovation in ATSC’s design is its default data segmentation strategy. Rather than processing entire data sets as single units, ATSC breaks data into manageable segments. This approach yields multiple advantages:

- Enhanced computational efficiency through
[parallel processing of smaller data blocks](https://thenewstack.io/heterogeneous-processing-requires-data-parallelization-tools-sycl-and-dpc-are-a-good-start/). - More precise function fitting by adapting to local data characteristics.
- Reduced memory overhead during both compression and decompression.
- Selective data access, allowing users to decompress specific time ranges without processing entire files.
This architecture consistently achieves remarkable results, with compressed data typically showing less than 1% deviation from original values. For applications requiring even higher precision, ATSC offers configurable accuracy thresholds to match specific use-case requirements.

![Lossless vs. ATSC polynomial fitting vs. ATSC Fast-Fourier Transform fitting](https://cdn.thenewstack.io/media/2024/12/29bda24c-image3.png)
Lossless vs. ATSC polynomial fitting vs. ATSC fast Fourier transform fitting

## Breakthrough Compression Performance
ATSC achieves compression ratios that fundamentally change the economics of time-series data storage. In rigorous testing, compression ratios ranged from 46:1 to 880:1, often with negligible loss of analytical value. To put these results in perspective: When compared to industry-standard solutions, ATSC demonstrated compression efficiency approximately 10 times greater than LZ4 and 30 times greater than Prometheus.

![The better-fitting purple function uses twice the data storage of the loose-fitting red function.](https://cdn.thenewstack.io/media/2024/12/5ef8efb6-image2.png)
The better-fitting purple function uses twice the data storage of the loose-fitting red function.

These performance metrics translate directly to operational benefits: Data that previously required terabytes of storage can now be maintained in gigabytes, while preserving the fidelity needed for analysis. This compression efficiency makes it practical to retain longer historical data sets and implement higher-frequency data collection — options that were previously cost-prohibitive with traditional compression methods.

## Practical Applications and Use Cases
ATSC’s unique compression capabilities make it particularly valuable in scenarios where storage efficiency can be balanced against precise data reproduction. Here are three key applications where ATSC delivers exceptional value:

**Long-Term Data Archival**
For organizations managing historical metrics, ATSC transforms the economics of data retention. When moving time-series data into long-term storage, ATSC’s compression enables organizations to maintain comprehensive historical records while dramatically reducing storage costs. The minimal information loss is negligible for most analytical purposes, making it an ideal solution for archival requirements.

**High-Frequency Data Collection**
ATSC resolves a common monitoring dilemma: the trade-off between sampling frequency and storage costs. Organizations previously limited to 30-second sampling intervals due to storage constraints can now increase their sampling rates substantially while actually reducing storage requirements. This enables more precise event detection and system monitoring without the traditionally associated storage burden.

**Operational Metrics and Visualization**
For system monitoring applications — tracking CPU usage, memory utilization and similar metrics — ATSC’s approach is particularly effective. These metrics typically display gradual changes and patterns that ATSC’s mathematical functions can model efficiently. When [visualizing such data](https://thenewstack.io/explore-and-visualize-data-the-apache-superset-way/) for human analysis, the slight variations in precision are imperceptible, while the storage savings are substantial.

The flexibility of ATSC’s compression approach allows organizations to optimize their data storage strategy for each specific use case, finding the ideal balance between precision and efficiency.

![Original data (yellow) vs. ATSC data (green) with 88x compression.](https://cdn.thenewstack.io/media/2024/12/6ac776f5-image4.png)
Original data (yellow) vs. ATSC data (green) with 88x compression.

## Getting Started With ATSC Is Easy
ATSC is available as an [open source project](https://github.com/instaclustr/atsc) on GitHub, ready for organizations to evaluate and implement. The project is actively expanding its ecosystem, with new integrations under development for popular databases including [ClickHouse](https://clickhouse.com/) and [Apache Cassandra](https://cassandra.apache.org/_/index.html). These integrations will streamline ATSC adoption, making its powerful compression capabilities more accessible to a broader range of applications.

For organizations managing large-scale time-series data, ATSC represents a significant opportunity to optimize storage costs while maintaining analytical capabilities. Its [open source nature ensures transparency](https://thenewstack.io/open-source-is-at-a-crossroads/) and allows for community contributions, while its configurable compression settings enable precise control over the balance between storage efficiency and data fidelity.

As data volumes continue to grow exponentially, ATSC offers a pragmatic, forward-thinking approach to time-series data compression that aligns with both technical requirements and business objectives.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)