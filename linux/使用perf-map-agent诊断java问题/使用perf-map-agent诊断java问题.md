## 使用perf-map-agent诊断java问题

Linux下可以通过perf统计分析CPU的占用情况，但是对于Java这类虚拟机语言，无法获知哪些Java方法占用了CPU。perf-map-agent实现了对于perf命令的扩展，将Java“内部”的信息提供给了perf，从而perf也能诊断Java本身的性能问题。

### 安装perf-map-agent

可以从github直接下载最新的软件[源代码压缩包](https://github.com/jvm-profiling-tools/perf-map-agent/archive/master.zip)，然后解压缩。这里要注意，因为perf-map-agent会su到进程的用户执行，所以要确保被监控的进程的用户能够访问解压缩的目录。否则，你可能会遇到以下报错：

```
Error: Could not find or load main class net.virtualvoid.perf.AttachOnce
```

如果你是用非root用户执行，需要确保用户有sudo权限。

解压缩后，创建perflinks目录，然后在perflinks中创建执行脚本：

```
[root@wls1 perftest]# mkdir perflinks
[root@wls1 perftest]# cd perf-map-agent-master
[root@wls1 perf-map-agent-master]# cmake .
-- JNI_INCLUDE_DIRS=/weblogic/jdk1.8.0_171/include;/weblogic/jdk1.8.0_171/include/linux;/weblogic/jdk1.8.0_171/include
-- JNI_LIBRARIES=/weblogic/jdk1.8.0_171/jre/lib/amd64/libjawt.so;/weblogic/jdk1.8.0_171/jre/lib/amd64/server/libjvm.so
-- JAVA_INCLUDE_PATH=/weblogic/jdk1.8.0_171/include
-- JAVA_INCLUDE_PATH2=/weblogic/jdk1.8.0_171/include/linux
-- Configuring done
-- Generating done
-- Build files have been written to: /root/perftest/perf-map-agent-master
[root@wls1 perf-map-agent-master]# make
[ 60%] Built target attach-main
[100%] Built target perfmap
[root@wls1 perf-map-agent-master]# bin/create-links-in  ../perflinks
[root@wls1 perf-map-agent-master]# 
```

然后进入到../perflinks目录就可以执行一些监控动作了。

### 基本操作

通过perf top查看带Java的运行状况：

```
[root@wls1 perflinks]# ./perf-java-top 4447
Samples: 242  of event 'cpu-clock', Event count (approx.): 28549271                                                                                                    
Overhead  Shared Object       Symbol             
  10.23%  [kernel]            [k] finish_task_switch
   3.64%  libjvm.so           [.] nmethod::cleanup_inline_caches
   2.34%  libpthread-2.17.so  [.] pthread_getspecific
   2.31%  [kernel]            [k] _raw_spin_unlock_irqrestore
   1.76%  libjvm.so           [.] PhaseIdealLoop::build_loop_tree
   1.76%  perf-4447.map       [.] I2C/C2I adapters
   ......
   1.17%  libjvm.so           [.] Type::cmp
   1.10%  perf-4447.map       [.] Lweblogic/application/ComponentInvocationContextManagerImpl;::setCurrentComponentInvocationContext
```

可以看到其中的 perf-4447.map 后面的Symbol即是相关的Java代码，这个直接执行perf命令时是看不到的。

然后可以产生perf报告：

```
[root@wls1 perflinks]# ./perf-java-report-stack 4447
Recording events for 15 seconds (adapt by setting PERF_RECORD_SECONDS)
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.131 MB /tmp/perf-4447.data (1 samples) ]
```

默认收集15秒的数据，并直接进入到perf report窗口：

```
Samples: 1  of event 'cpu-clock', Event count (approx.): 10101010
  Children      Self  Command  Shared Object       Symbol 
-  100.00%   100.00%  java     [kernel.kallsyms]   [k] system_call_after_swapgs
     start_thread
     java_start
     WatcherThread::run
     WatcherThread::sleep
     Monitor::wait
     Monitor::IWait
     pthread_cond_timedwait@@GLIBC_2.3.2
     system_call_after_swapgs
+  100.00%     0.00%  java     libpthread-2.17.so  [.] start_thread
+  100.00%     0.00%  java     libjvm.so           [.] java_start
+  100.00%     0.00%  java     libjvm.so           [.] WatcherThread::sleep
+  100.00%     0.00%  java     libjvm.so           [.] Monitor::wait
+  100.00%     0.00%  java     libpthread-2.17.so  [.] pthread_cond_timedwait@@GLIBC_2.3.2
```

如果想要继续查看该报告，可以运行：

```
perf report -i /tmp/perf-4447.data
```

### 生成火焰图

下载最新的[FlameGraph](https://github.com/brendangregg/FlameGraph/archive/master.zip)，解压缩，给所有的pl文件设置执行权限，然后设置环境变量：

```
[root@wls1 perftest]# cd FlameGraph-master
[root@wls1 FlameGraph-master]# chmod +x *.pl
[root@wls1 FlameGraph-master]# export FLAMEGRAPH_DIR=/root/perftest/FlameGraph-master

```

然后进入perflinks目录执行：

[root@wls1 perflinks]# ./perf-java-flames 4447
Recording events for 15 seconds (adapt by setting PERF_RECORD_SECONDS)
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.131 MB /tmp/perf-4447.data (1 samples) ]
Flame graph SVG written to PERF_FLAME_OUTPUT='/root/perftest/perflinks/flamegraph-4447.svg'.


可以看到，已经得到了一个svg火焰图，直接用浏览器打开。

最后一点，还需要给被检查的Java进程增加这个参数，这样可以得到更精确的调用信息：

```
-XX:+PreserveFramePointer
```

### 参考


 * 其他详细信息请参考：[perf-map-agent](https://github.com/jvm-profiling-tools/perf-map-agent)