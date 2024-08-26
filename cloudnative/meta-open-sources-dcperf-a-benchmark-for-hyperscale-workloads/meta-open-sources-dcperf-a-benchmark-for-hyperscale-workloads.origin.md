# Meta Open Sources DCPerf, a Benchmark for Hyperscale Workloads
![Featued image for: Meta Open Sources DCPerf, a Benchmark for Hyperscale Workloads](https://cdn.thenewstack.io/media/2024/08/d66decf8-andreas-weilguny-jbsy1gkgfma-unsplash-1024x768.jpg)
Stymied by the limits of the standard data center benchmarks, social media giant [Meta](https://about.meta.com/?utm_content=inline+mention), formerly Facebook, developed its own set of performance tests, called DCPerf, to measure the performance requirements of its [hyperscale applications](https://thenewstack.io/how-meta-patches-linux-at-hyperscale/), those heavily used applications requiring hundreds or even thousands of servers to run.

The company has now released this benchmarking suite (on [GitHub](https://github.com/facebookresearch/DCPerf)) under an [MIT open source license](https://opensource.org/license/mit), hoping it will be picked up by academia, the hardware industry and other Internet companies.

“As an open source benchmark suite, DCPerf has the potential to become an industry standard method to capture important workload characteristics of compute workloads that run in hyperscale data center deployments,” wrote Meta engineers [Abhishek Dhanotia](https://engineering.fb.com/author/abhishek-dhanotia/), [Wei Su](https://engineering.fb.com/author/wei-su/), [Carlos Torres](https://engineering.fb.com/author/carlos-torres/), [Shobhit Kanaujia](https://engineering.fb.com/author/shobhit-kanaujia/), [Maxim Naumov](https://engineering.fb.com/author/maxim-naumov/), in a [blog post](https://engineering.fb.com/2024/08/05/data-center-engineering/dcperf-open-source-benchmark-suite-for-hyperscale-compute-applications/) published Aug. 5.

Hyperscale computing is a different beast compared to traditional enterprise computing, or even supercomputer-based [high performance computing](https://thenewstack.io/top500-chinas-supercomputing-silence-aggravates-tech-cold-war-with-u-s/) (HPC). And it requires its own set of tests, the Meta engineers argued, given that data center-driven hyperscale computing takes up the largest market share of server deployments worldwide.

So it makes sense that hyperscale needs its own set of evaluation methodologies.

DCPerf was designed to match different kinds of hyperscale workloads, with each of the five benchmarks modeled on a large Meta application currently in use.

![A table of the different DCPerf tests andthe apps they were built from.](https://cdn.thenewstack.io/media/2024/08/ace51ceb-meta-dcperf.png)
Different DCPerf benchmarks are based on different Meta workloads, each with a different mix of technologies. (Source: Meta)

The benchmarks support both [ARM](https://www.arm.com/campaigns/multi-arch-cloud-infrastructure?utm_content=inline+mention) and [Intel](https://www.intel.com/content/www/us/en/now/data-centric/overview.html?utm_content=inline+mention) platforms and can support multi-tenancy for those cases where an application runs across multiple data centers. The testing software can run on either [CentOS Stream 8/9](https://thenewstack.io/red-hat-deprecates-linux-centos-in-favor-of-a-streaming-edition/) or [Ubuntu 22.04 Linux](https://thenewstack.io/how-to-install-ubuntu-pro-on-your-servers/).

## But What About SPEC?
To date, the industry standard for data center benchmarks has come from the [Standard Performance Evaluation Corporation](https://www.spec.org/) ([SPEC](https://thenewstack.io/nvidia-h200-gpus-crush-mlperfs-llm-inferencing-benchmark/)). Meta itself uses [SPEC’s CPU benchmark](https://www.spec.org/benchmarks.html#cpu) suite for processor evaluation.

DCPerf extends SPEC CPU, allowing the company to pinpoint optimal configuration choices, as well as make more accurate performance projections. It can even identify performance bugs in hardware and system software.

“DCPerf provides a much richer set of application software diversity and helps get better coverage signals on platform performance versus existing benchmarks such as SPEC CPU,” the engineers wrote. “Due to these benefits, we have also started using DCPerf to assist with our decision making process on which platforms to deploy in our data centers.”

In the blog post, the engineers showed how DCPerf provided more nuanced results in how well system-on-a-chip microarchitectures supported Meta’s applications.

![Chart comparing the accuracy of SpecCPU and DCPerf.](https://cdn.thenewstack.io/media/2024/08/3bf78adb-meta-dcperf-compare.png)
Here are two estimates of the average core frequency (1.94) consumed by production applications; SpecCPU 2006 estimated the number at 2.10, while DCPerf pegged the number at 1.92. For a giant operation like Meta’s, more accurate predictions mean better estimates of how much hardware to buy. (Source: Meta)

Meta has worked with the CPU vendors over the past two years to externally validate the spec.

## Google Has a Benchmark, Too
Meta is not the only hyperscaler with its own internal testing suite.

[Google](https://cloud.google.com/?utm_content=inline+mention) has [Fleetbench](https://github.com/google/fleetbench), which is a set of seven “microbenchmarks” designed to help CPU and system software builders better understand hyperscale workloads at Google.
“Traditional benchmarks often fall short in capturing the nuances of” hyperscale workloads, wrote Google researchers [in a paper](https://ieeexplore.ieee.org/document/10590038) detailing Fleetbench. “Creating a public benchmark suite that is representative of the workloads used by actual warehouse-scale computers is challenging, as they typically run proprietary, non-public software that operates on confidential data.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)