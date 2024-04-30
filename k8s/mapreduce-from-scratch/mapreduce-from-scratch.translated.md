# 从头开始构建 MapReduce

### 逐步构建分布式计算框架

在过去的几周里，我一直在从头开始构建 MapReduce。

这将是一篇很长的文章：我们将了解分布式计算的必要性，重新发现为什么 MapReduce 是对许多问题进行建模的自然方式，构建我们自己的版本，了解各个部分如何组合在一起，并用它解决一个实际问题！

## 激励问题

假设我们想计算海量数据集中的词频。我们尝试在单台机器上处理它，但发现需要一个月以上的时间。我们能做什么？

第一个想法应该是获得一台更快的机器，但它可能不存在或太昂贵。相反，让我们看看如何将问题分布到 N 台商品机器上。我们希望有一种简单的方法来使用简单的查询查找任何单词的频率，即 grep over a file。

让我们首先将数据集拆分为 N 个分区，并使用不同的机器计算每个子集的词频。这已经给了我们 Nx 的加速，减去了一些固定的开销。为了合并结果，我们可以添加一台最终机器，它获取这 N 个部分结果文件并对相应单词的频率求和。

这与 MapReduce 背后的核心思想相差不远。上述过程有两个主要步骤：首先，我们

* 将单词映射到输入数据子集中的频率，然后减少中间结果以获得最终答案。

请注意，这是非常通用的，想象一下我们有一个大型照片数据集，我们希望对其进行分类：我们可以将图像分类任务作为映射操作，然后在归约阶段将具有相同类别的图像分组。

另一个观察结果是，映射部分通常是两个部分中更昂贵的阶段，因此，通常映射器比归约器多。

希望已经让你相信 MapReduce 是一个合理的想法，让我们看看 MapReduce 论文如何解决词频问题。

感谢阅读 Michal 的 Substack！免费订阅以接收新帖子并支持我的工作。

## 使用 MapReduce

下面，我从 [论文](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf)中复制粘贴了 WordCounter MapReduce 程序。让我们看看它是如何工作的。稍后，当我们实现我们的版本时，我们的目标是保持使用语义相同。

```cpp
#include "mapreduce/mapreduce.h"

// 用户的映射函数
class WordCounter : public Mapper
{
public:
virtual void Map(const MapInput &input)
{
const string &text = input.value();
const int n = text.size();
for (int i = 0; i < n;)
{
// 跳过前导空白
while ((i < n) && isspace(text[i]))
i++;
// 查找单词结尾
int start = i;
while ((i < n) && !isspace(text[i]))
i++;
if (start < i)
Emit(text.substr(start, i - start), "1");
}
}
};
REGISTER_MAPPER(WordCounter);

// 用户的归约函数
class Adder : public Reducer
{
virtual void Reduce(ReduceInput *input)
{
// 遍历具有
// 相同键的所有条目并添加值
int64 value = 0;
while (!input->done())
{
value += StringToInt(input->value());
input->NextValue();
}
// 为 input->key() 发射和
Emit(IntToString(value));
}
};
REGISTER_REDUCER(Adder);

int main(int argc, char **argv)
{
ParseCommandLineFlags(argc, argv);
MapReduceSpecification spec;
// 将输入文件列表存储到 "spec" 中
for (int i = 1; i < argc; i++)
{
MapReduceInput *input = spec.add_input();
input->set_format("text");
input->set_filepattern(argv[i]);
input->set_mapper_class("WordCounter");
}
MapReduceOutput *out = spec.output();
out->set_filebase("/gfs/test/freq");
out->set_num_tasks(100);
out->set_format("text");
out->set_reducer_class("Adder");
// 调整参数：最多使用 2000
// 台机器和每个任务 100 MB 内存
spec.set_machines(2000);
spec.set_map_megabytes(100);
spec.set_reduce_megabytes(100);
// 现在运行它
MapReduceResult result;
if (!MapReduce(spec, &result))
abort();
// 完成：'result' 结构包含有关计数器、花费时间、
// 使用的机器数量等的信息。
return 0;
}
```

用户程序有 3 部分：映射函数、归约函数和配置。大部分繁重的工作由导入的
mapreduce 库处理。

映射函数将输入文本拆分为单词并发出键值对。例如，
*“the quick brown fox jumps over the lazy dog”* 映射到以下键值对：[“the”:1, “quick”:1, “brown”:1, “fox”:1, “jumps”: 1, “over”:1, “the”:1, “lazy”:1, “dog”:1]。请注意，对 (“the”: 1) 发射了两次。

归约函数按键操作。例如，给定输入 [“the”:1, “the”:1”, “the”:1]，它将发出 (“the”:3)。

配置处理输入输出、格式以及可用于 MapReduce 作业的资源数量。

在不到 100 行代码中，我们可以通过利用 1000 台机器来解决单词计数问题！这非常简洁，展示了 MapReduce 作为一种抽象的强大功能。

## 收集需求
## Requirements

Inspired by the paper, let's outline the requirements for our implementation:

- User imports our MapReduce library, implements Map and Reduce functions, and provides configuration.
- When the user executes the binary, it gets copied to multiple machines, executing in either Mapper or Reducer mode.
- These machines must have access to the input data.
- The output of the mappers must be available to the reducers.
- The user can access the final results.

## Infrastructure

As I started digging into it, these requirements posed two major unknowns:

- How to distribute the binary to other machines and make the input data available to them.
- How to collect the results from the mappers and make them available to the reducers.

After some research, I decided to host my input data on a network storage server - I went with NFS. We can mount the network directory on each machine, allowing the machines to read and write to it. It won't be as efficient or scalable as Google File System or HDFS, but it should suffice for our purposes.

To distribute the binary to multiple machines, execute it, and monitor its state, we could potentially copy the binary via SCP, SSH into the machine, execute the binary, and then wait for it to finish. We could even implement health pings and progress reporting.

However, after playing around with this for a while, I realized that this sounds a lot like cluster orchestration, and decided to leverage Kubernetes to make my life easier. We can build the binary as a docker image, and have Kubernetes execute it as a [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/). Integrating NFS with Kubernetes is quite easy, thanks to Persistent Volumes and Persistent Volume Claims. Don't worry, you don't need to understand these concepts, but I mention them for completeness.

Since I'm developing for educational purposes, I'm using [minikube](https://minikube.sigs.k8s.io/docs/start/) to spin up a local virtual cluster on my laptop. I'm running my NFS server as a docker container outside of the cluster, and connecting it to the cluster via a docker network. The beauty of this setup is that it can be easily migrated to multiple physical or virtual machines.

With the infrastructure sorted out, let's dive into writing our MapReduce framework!

## Using My MapReduce

First, we'll explore how to use my MapReduce implementation to solve the word count problem. Then, we'll dig into the implementation to see how the different components work together.

As promised, I tried to keep the usage semantics similar to the original paper. Let's compare the MapReduce program using my Go implementation with the C++ example we saw earlier!

```go
// main.go
import (
    ...
    "github.com/MichalPitr/map_reduce/pkg/config"
    "github.com/MichalPitr/map_reduce/pkg/interfaces"
    "github.com/MichalPitr/map_reduce/pkg/mapreduce"
)

type WordCounter struct {
    wordRegex *regexp.Regexp
}

func (wc *WordCounter) Map(input interfaces.MapInput, emit func(key, value string)) {
    text := input.Value()
    text = strings.ToLower(text)
    words := wc.wordRegex.FindAllString(text, -1)
    for _, word := range words {
        emit(word, "1")
    }
}

type Adder struct{}

func (a *Adder) Reduce(input interfaces.ReducerInput, emit func(value string)) {
    val := 0
    for !input.Done() {
        num, err := strconv.Atoi(input.Value())
        if err != nil {
            log.Printf("Failed converting input to integer, skipping: %q", input.Value())
            input.NextValue()
            continue
        }
        val += num
        input.NextValue()
    }
    emit(strconv.Itoa(val))
}

func main() {
    cfg := config.SetupJobConfig()
    log.Printf("cfg: %+v", cfg)
    cfg.NumReducers = 2
    cfg.NumMappers = 4
    cfg.Mapper = &WordCounter{wordRegex: regexp.MustCompile(`\b\w+\b`)}
    cfg.Reducer = &Adder{}
    mapreduce.Execute(cfg)
}
```

Let's take a moment to understand how my solution works under the hood. We can refer to a handy diagram from the paper to illustrate this.

The user's program executes in three modes on different machines: Master, Mapper, and Reducer. At a high level, the master handles the overall job orchestration, the mappers perform the expensive map operation on the input files, and the reducers combine the intermediate results from the mappers. In my solution, the mode is determined by a CLI flag, e.g. `--mode=master` for master mode.

## Master

The Master mode splits the input files into subsets, prepares the NFS directory, launches mapper jobs with the assigned files, and waits for them to finish. It then repeats the process for the reducers. The main function is quite straightforward, I can list it here:

```go
// /pkg/master/master.go
func Run(cfg *config.Config) {
    clientset := createKubernetesClient()
    numNodes := getNumberOfNodes(clientset)
    mustValidateConfig(cfg, numNodes)
    jobId := fmt.Sprintf("job-%s", time.Now().Format("2006-01-02-15-04-05"))
    log.Printf("Running master: %s", jobId)
    mustCreateJobDir(cfg.NfsPath, jobId)
    fileRanges := partitionInputFiles(cfg.InputDir, cfg.NumMappers)
    t0 := time.Now()
    launchMappers(cfg, clientset, jobId, fileRanges)
    waitForJobsToComplete(clientset, jobId, "mapper")
    log.Printf("Mappers took %v to finish", time.Since(t0))
    t1 := time.Now()
    ...
}
```
## launchReducers

```go
launchReducers(cfg, clientset, jobId)
waitForJobsToComplete(clientset, jobId, "reducer")
log.Printf("Reducers took %v to finish", time.Since(t1))
log.Printf("Total runtime: %v", time.Since(t0))
}
```

### Let's dive into the `launchMappers` function.

It creates a Kubernetes job for each mapper. The job specification defines:

- The Docker image containing our binary.
- The CLI arguments required by the mapper: mapper mode, input/output directories, and files to process.
- How to mount the NFS storage.
- Etc... Docker image? We never created one! I'll show this in more detail when we finally run our solution, but Kubernetes revolves around containers, so we dockerize our binary so that the Kubernetes pod can download it.

After `launchMappers` creates the mapper jobs, Kubernetes assigns the jobs to nodes in the cluster, starts the containers, and monitors their status.

Now that we have mappers running, it's time to understand how they work!

## Mappers

In mapper mode, the binary scans the input file line by line, passing the line to the user's map function. The map processes the text and emits key-value pairs using the injected `emit` function.

In my implementation, the `emit` function is very simple - it stores the key-value pairs in a map of dynamic lists. A more complete implementation would do some buffering and then flush the buffer to disk.

When the mapper finishes processing all the input, it saves the sorted key-value pairs to an intermediate file in the NFS storage, from which the reducers will later read to do the final processing. Let's zoom in here and see how this mapping from intermediate files to reducers works.

We want to partition the intermediate files by key so that all the same keys are processed by one reducer. For example, let's say that `"brown"` and `"the"` appear in the intermediate files of mapper 1 and mapper 2. We want to make sure that each is eventually processed by the same reducer. Let's see an example.

To do this, when we save the intermediate results from the mappers, we partition the keys by the number of reducers R using the formula:

```
key % R
```

For example, using the FNV hash and R = 2, we get:

```
(math note: this says "1 equals FNV("brown") mod 2".)
```

Based on this, we assign `"brown"` to the 2nd intermediate file, which will be processed by reducer 2. Notice that in the example above, all the `"the"`s end up in the blue file, and all the `"brown"`s end up in the red file!

This concludes our discussion of mappers - next, let's see how reducers work.

## Reducers

As mentioned earlier, the reducer's job is to read key-value pairs from its assigned intermediate files and process them using the user-defined reduce function.

We can be sure of two things: the keys in the intermediate files are sorted by key, and if key `A` is present in one of the intermediate files, we are guaranteed that key `A` is not present in any of the files assigned to other reducers.

I tried to implement my reducer more cleverly, and avoid loading all the intermediate files into memory. This led to an interesting algorithmic problem:

Suppose we are trying to process 3 intermediate files, one key-value pair at a time, without loading everything into memory.

We can use a min-heap to merge the key-value pairs dynamically! We load the first key-value pair from each file into the heap. Whenever we pop from the heap, we read the next line from the corresponding file and push it onto the heap. This gives us a memory-efficient way to read a stream of key-value pairs! You can find the implementation [here](https://github.com/MichalPitr/map_reduce/blob/main/pkg/reducer/stream_merger.go).

After processing all the intermediate files, the reducer saves the results to the NFS storage.

For example, the example above would produce: `["abby": 1, "alice": 3, "bob": 2, "car":2, "dog":1, …]`.

The MapReduce paper describes some other optimizations that I skipped in my implementation. The astute reader may have already thought of some - for example, can't we do some optional reduction on the mappers?

Congratulations, you now have a fairly comprehensive understanding of MapReduce! The hardest part is over! Let's put it all together and use our MapReduce to count word frequencies in the [100 most popular books on Project Gutenberg](https://www.gutenberg.org/browse/scores/top#authors-last30)!

## MapReduce in Practice

I downloaded the 100 most popular books on Project Gutenberg to `/mnt/nfs/input/`, using this [script](https://github.com/MichalPitr/map_reduce/blob/main/utils/create-dataset.py). The book files are labeled `book-0` to `book-99`. I also created a 4-node minikube cluster with access to my NFS storage.

```
michal@michal-ThinkPad-T490s:/mnt/nfs$ kubectl get nodes
NAME STATUS ROLES AGE VERSION
multi-node Ready control-plane 27d v1.28.3
multi-node-m02 Ready <none> 7d2h v1.28.3
multi-node-m04 Ready <none> 7d1h v1.28.3
multi-node-m05 Ready <none> 7d1h v1.28.3
```

I'll reuse the word frequency Go main file that I showed earlier. We'll have to use this
[Dockerfile](https://github.com/MichalPitr/map_reduce/blob/main/Dockerfile) 并将其推送到我的注册表。映射器和归约器节点将拉取此镜像来运行我们的工作负载。

```
docker build -t michalpitr/mapreduce:latest .
docker push michalpitr/mapreduce:latest
```

现在我们只需要在本地运行 master！

```
go build .
./map_reduce --mode=master --image=michalpitr/mapreduce:latest --input-dir /mnt/input/ --nfs-path /mnt/nfs/
```

让我们检查执行日志。

```
michal@michal-ThinkPad-T490s:~/code/map_reduce$ ./map_reduce --mode=ma
ster --image=michalpitr/mapreduce:latest --input-dir /mnt/nfs/input/ -
-nfs-path /mnt/nfs/
2024/04/28 17:13:53 正在运行 master 作业-2024-04-28-17-13-53
2024/04/28 17:13:53 正在为 book-0-30 创建映射器-0
2024/04/28 17:13:53 正在为 book-31-53 创建映射器-1
2024/04/28 17:13:53 正在为 book-54-76 创建映射器-2
2024/04/28 17:13:53 正在为 book-77-99 创建映射器-3
2024/04/28 17:13:53 正在等待作业完成。
2024/04/28 17:14:03 正在等待作业完成。
2024/04/28 17:14:13 正在等待作业完成。
2024/04/28 17:14:23 所有作业已完成。
2024/04/28 17:14:23 映射器花费 30.1843218 秒完成
2024/04/28 17:14:23 正在创建归约器-0
2024/04/28 17:14:23 正在创建归约器-1
2024/04/28 17:14:23 正在等待作业完成。
2024/04/28 17:14:33 所有作业已完成。
2024/04/28 17:14:33 归约器花费 10.106014703 秒完成
2024/04/28 17:14:33 总运行时间：40.290376921 秒
```

整个作业花费了 40 秒。我们在此处并未期望出现任何疯狂的情况，毕竟，我是在一台动力不足的笔记本电脑上运行此作业，而不是一个
*真正的* 集群。

让我们简单了解一下。master 创建了 4 个映射器，每个映射器都分配了一个书籍范围。

使用
kubectl，我们可以看到集群正在创建 4 个容器。这是集群拉取我们之前推送的镜像的时候！

```
michal@michal-ThinkPad-T490s:/mnt/nfs$ kubectl get pods
名称 就绪状态 状态 重启次数 年龄
mapper-0-zgz24 0/1 正在创建容器 0 11 秒
mapper-1-m824k 0/1 正在创建容器 0 11 秒
mapper-2-ctqqt 0/1 正在创建容器 0 11 秒
mapper-3-l2ddh 0/1 正在创建容器 0 11 秒
```

这些容器启动并完成运行所需的时间并不长。

```
michal@michal-ThinkPad-T490s:/mnt/nfs$ kubectl get pods
名称 就绪状态 状态 重启次数 年龄
mapper-0-zgz24 1/1 正在运行 0 18 秒
mapper-1-m824k 0/1 已完成 0 18 秒
mapper-2-ctqqt 0/1 已完成 0 18 秒
mapper-3-l2ddh 0/1 已完成 0 18 秒
```

master 定期轮询 Kubernetes API 服务器以获取这些作业的状态。一旦所有作业都完成，它就会启动归约器。

在进入归约器之前，让我们看看其中一个映射器生成的中间文件：

```
michal@michal-ThinkPad-T490s:/mnt/nfs/job-2024-04-28-17-13-53/mapper-3$ ls
分区-0 分区-1
```

检查分区-1 的末尾，显示了陀思妥耶夫斯基的《地下室手记》中一个角色的键值对。到目前为止，一切都好！

```
michal@michal-ThinkPad-T490s:/mnt/nfs/job-2024-04-28-17-13-53/mapper-3$ tail 分区-1
zverkov,1
zverkov,1
zverkov,1
zverkov,1
zverkov,1
…
```

接下来，master 启动归约器，

```
michal@michal-ThinkPad-T490s:/mnt/nfs$ kubectl get pods
名称 就绪状态 状态 重启次数 年龄
…
reducer-0-4xt58 0/1 正在创建容器 0 2 秒
reducer-1-xvhfk 0/1 正在创建容器 0 2 秒
```

它们很快完成。

```
michal@michal-ThinkPad-T490s:/mnt/nfs$ kubectl get pods
名称 就绪状态 状态 重启次数 年龄
…
reducer-0-4xt58 0/1 已完成 0 7 秒
reducer-1-xvhfk 0/1 已完成 0 7 秒
```

就是这样 - 我们刚刚使用我们自己的 MapReduce 框架计算了单词频率！让我们看看我们可以从结果中学到什么！

我可以在作业文件夹的根目录中看到输出文件：

```
michal@michal-ThinkPad-T490s:/mnt/nfs/job-2024-04-28-17-13-53$ ls
… reducer-0 reducer-1
```

让我们使用 grep 来查找一些单词的频率。

```
michal@michal-ThinkPad-T490s:/mnt/nfs/job-2024-04-28-17-13-53$ grep -w zverkov reducer-0 reducer-1
reducer-1:zverkov,112
michal@michal-ThinkPad-T490s:/mnt/nfs/job-2024-04-28-17-13-53$ grep -w the reducer-0 reducer-1
reducer-1:the,822175
michal@michal-ThinkPad-T490s:/mnt/nfs/job-2024-04-28-17-13-53$ grep -w mapreduce reducer-0 reducer-1
michal@michal-ThinkPad-T490s:/mnt/nfs/job-2024-04-28-17-13-53$
michal@michal-ThinkPad-T490s:/mnt/nfs/job-2024-04-28-17-13-53$ grep -w map reducer-0 reducer-1
reducer-1:map,188
michal@michal-ThinkPad-T490s:/mnt/nfs/job-2024-04-28-17-13-53$ grep -w reduce reducer-0 reducer-1
reducer-0:reduce,123
```

遗憾的是，在古腾堡计划最流行的 100 本书中没有提到 MapReduce……也许有一天？

最后一点，请注意这些输出文件如何按键对结果空间进行分区。当我们查找一个单词时，它只存在于一个文件中！这几乎就像我们做对了什么！

如果您已经读到这里，您不妨查看
[GitHub 仓库](https://github.com/MichalPitr/map_reduce)。您已经熟悉
[SQLite 存储格式内部](https://michalpitr.substack.com/p/how-does-sqlite-store-data)

研究和撰写这些文章需要大量时间和精力。为确保您不会错过下一篇文章，请考虑订阅或关注我。