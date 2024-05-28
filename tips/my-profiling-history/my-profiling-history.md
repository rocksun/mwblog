
<!--
title: 我的性能分析开端
cover: ./cover.png
-->

回顾我的职业生涯，中间件技术专家这个角色持续的时间最长，关于性能分析经历了许多，但故事要从我顿悟的那个案例开始。

## 某集团省公司新系统上线

该公司计划将核心业务升级到 WebService 架构。通过 WebService 将应用前后端分离。这里说的前端和后端都是运行在 WebLogic 的 Java Web 程序，只是前端负责生成 Web 页面，而后端则是负责执行业务逻辑。

可以想象，这样激进的架构不仅开发成本很高，也可能面临许多未知的风险。临近上线执行性能测试时，果然遇到了问题。新采购的小型机 CPU 已经拉满，但是几十个节点的集群才能达到几百的吞吐量。于是这个公司找到了我们提供支持，他们怀疑 WebLogic 需要调优。

> 可能很多年轻的朋友也不知道什么是 WebService，简单说就是一种分布式计算技术。和现在基于 JSON 的 API 很像，但报文封装用的是 SOAP，SOAP 是一种非常复杂的 XML。这个技术当年被许多大厂商推崇，但现在已经不太常见了，这里就不分析原因了，通过阅读本文你可能会对这个技术有一定的感受。

再讲讲我当时的情况。我是 Java 程序员出身，工作中接触到了 WebLogic，基本管理配置还是比较熟悉的。我也组织过大规模的性能测试，对于各类瓶颈有一定的认识。不过因为测试的对象都是成熟的系统，性能达标后就没有进一步优化，并没有在调优上做更多的工作。因此，这次支持对我来说可能也是一个挑战。

一般情况下，CPU 拉满是好现象，整个应用的瓶颈是 CPU 了，说明已经已经发挥了硬件的完全性能，可以暂时不考虑性能相关的其他因素。那么是什么占用了 CPU？当时的工具还不健全，也可能是我技能还不够完整，不过我觉得有一个思想是永远不会变的，**需要更清楚地看到问题**。

## 是应用占据了 CPU 吗？

确认这一点很容易，top、ps 命令都可以，很明显是 WebLogic 的 Java 程序占据的 CPU 最高。

## 哪些线程 CPU 高？

这里的操作系统是 AIX，我知道可以用 ps 命令查看线程的 CPU 占用率：

```
[/app/weblogic/bea/user_projects/domains/kfapp_domain]$ps -mp 172540 -o THREAD
    USER    PID   PPID      TID ST  CP PRI SC    WCHAN        F     TT BND COMMAND
weblogic 172540 119578        - A  1083  60 203        *   242001  pts/0   - /usr/java5_64/bin/java -Xms512m 
       -      -      -   377063 S    0  82  1 1190361d8   c10400      -   - -
       -      -      -   401657 S    2  83  1 f100070f10006240  8410400      -   - -
       -      -      -   405745 S    0  62  1 f100070f10006340  8410404      -   - -
       -      -      -   409615 R    8  60  1        -   400000      -   - -
       -      -      -   417831 S    1  82  1 f100070f10006640  8410400      -   - -
       -      -      -   434239 S    2  83  1 11cb85168   c10400      -   - -
       -      -      -   446625 S    0  82  1 f100070f10006d40  8410400      -   - -
       -      -      -   450639 S    0  82  1 f100070f10006e40  8410404      -   - -
       -      -      -   471155 S    0  82  1 f100070f10007340  8410404      -   - -
       -      -      -   475273 S    2  83  1 11cb85168   c10400      -   - -
       -      -      -   491667 R    7  60  1 11487ec88   c00000      -   - -
       -      -      -   508127 S    6  86  1 11cb85168   c10400      -   - -
       -      -      -   524491 S    0  66  1 f100070f10008040  8410400      -   - -
       -      -      -   528603 S   10  88  1 11cb85168   c10400      -   - -
       -      -      -   532703 S    0  82  1 1190361d8   c10400      -   - -
       -      -      -   545005 R   21  60  1 11487ec88   c00000      -   - -
```

从 CP 字段可以看到，并没有某个或某些线程的占用的 CPU 较高，难道就是应用本身慢吗？

> 作为 Java 应用中间件产品专家，对于产品的了解固然重要，但另一个很重要的难点是如何证明不是中间件的问题。应用运行在中间件上，还可能要与其他外围系统交互，很多问题并不是中间件产品的问题，但是如何证明呢？

## 进一步分析

我知道，我还有个 Java 工程师最常用的工具：线程堆栈。因为这里用的是 AIX，其 JDK 为 IBM JDK 。通过 `kill -3 [pid]` 我们就可以在 WebLogic 根目录得到一个  javacore 开头的文件，也就是线程堆栈文件，线程堆栈就是 Java 进程的线程快照。

我用 `kill -3` 得到了几个快照，但结论并不是那么一目了然，大多数工作线程都处于类似下面的状态：

```java
at java/util/zip/ZipFile.getEntry(Native Method) 
at java/util/zip/ZipFile.getEntry(ZipFile.java:292(Compiled Code)) 
at weblogic/utils/classloaders/ClasspathClassFinder.getZipSource(ClasspathClassFinder.java:360(Compiled Code)) 
at weblogic/utils/classloaders/ClasspathClassFinder.getSourcesInternal(ClasspathClassFinder.java:296(Compiled Code)) 
at weblogic/utils/classloaders/ClasspathClassFinder.getSource(ClasspathClassFinder.java:272(Compiled Code)) 
at weblogic/utils/classloaders/JarClassFinder.getSource(JarClassFinder.java:46(Compiled Code)) 
at weblogic/utils/classloaders/MultiClassFinder.getSource(MultiClassFinder.java:64(Compiled Code)) 
at weblogic/utils/classloaders/MultiClassFinder.getSource(MultiClassFinder.java:64(Compiled Code)) 
at weblogic/utils/classloaders/MultiClassFinder.getSource(MultiClassFinder.java:64(Compiled Code)) 
at weblogic/utils/classloaders/CodeGenClassFinder.getSource(CodeGenClassFinder.java:33(Compiled Code)) 
at weblogic/utils/classloaders/MultiClassFinder.getSource(MultiClassFinder.java:64(Compiled Code)) 
at weblogic/utils/classloaders/CodeGenClassFinder.getSource(CodeGenClassFinder.java:33(Compiled Code)) 
at weblogic/utils/classloaders/GenericClassLoader.findResource(GenericClassLoader.java:212(Compiled Code)) 
at weblogic/utils/classloaders/GenericClassLoader.getResourceInternal(GenericClassLoader.java:143(Compiled Code)) 
at weblogic/utils/classloaders/GenericClassLoader.getResource(GenericClassLoader.java:169(Compiled Code)) 
at java/lang/ClassLoader.getResourceAsStream(ClassLoader.java:482(Compiled Code)) 
at weblogic/apache/xerces/util/SecuritySupport12$4.run(SecuritySupport12.java:119(Compiled Code)) 
at java/security/AccessController.doPrivileged(AccessController.java(Compiled Code)) 
at weblogic/apache/xerces/util/SecuritySupport12.getResourceAsStream(SecuritySupport12.java(Compiled Code)) 
at weblogic/apache/xerces/util/ObjectFactory.findJarServiceProvider(ObjectFactory.java:299(Compiled Code)) 
at weblogic/apache/xerces/util/ObjectFactory.createObject(ObjectFactory.java:191(Compiled Code)) 
at weblogic/apache/xerces/util/ObjectFactory.createObject(ObjectFactory.java:121(Compiled Code)) 
at weblogic/apache/xerces/parsers/DOMParser. (DOMParser.java:157(Compiled Code)) 
at weblogic/apache/xerces/parsers/DOMParser. (DOMParser.java:140(Compiled Code)) 
at weblogic/apache/xerces/jaxp/DocumentBuilderImpl. (DocumentBuilderImpl.java:103(Compiled Code)) 
at weblogic/apache/xerces/jaxp/DocumentBuilderFactoryImpl.setAttribute(DocumentBuilderFactoryImpl.java:126(Compiled Code)) 
at weblogic/xml/jaxp/WebLogicDocumentBuilderFactory. (WebLogicDocumentBuilderFactory.java:49(Compiled Code)) 
at weblogic/xml/jaxp/RegistryDocumentBuilder.getDefaultDocumentBuilderFactory(RegistryDocumentBuilder.java:283(Compiled Code)) 
at weblogic/xml/jaxp/RegistryDocumentBuilder.getDocumentBuilder(RegistryDocumentBuilder.java:222(Compiled Code)) 
at weblogic/xml/jaxp/RegistryDocumentBuilder.parse(RegistryDocumentBuilder.java:147(Compiled Code)) 
at org/apache/axis/utils/XMLUtils.newDocument(XMLUtils.java:322(Compiled Code)) 
at org/apache/axis/utils/XMLUtils.newDocument(XMLUtils.java:335(Compiled Code)) 
at org/apache/axis/configuration/FileProvider.configureEngine(FileProvider.java:209(Compiled Code)) 
at org/apache/axis/AxisEngine.init(AxisEngine.java:187(Compiled Code)) 
at org/apache/axis/AxisEngine. (AxisEngine.java:172(Compiled Code)) 
at org/apache/axis/client/Service.getAxisClient(Service.java:143(Compiled Code)) 
at org/apache/axis/client/Service. (Service.java:152(Compiled Code)) 
at com/xxx/esb/action/webservice/ZJESBserviceServiceLocator. (ZJESBserviceServiceLocator.java:10(Compiled Code)) 
at com/yyy/integration/eai/xxxFacadeESB.getxxxESBStub(xxxFacadeESB.java:33(Compiled Code)) 
at com/yyy/integration/eai/xxxFacadeESB.doBussiness(xxxFacadeESB.java:177(Compiled Code)) 
at com/yyy/integration/eai/xxxESBServiceBean.doBussiness(xxxESBServiceBean.java:29(Compiled Code)) 
at com/yyy/integration/ejb/BusinessServiceBean.searchBusiNumLinkOrderNum(BusinessServiceBean.java:2122(Compiled Code)) 

...
```

大量线程处于这样的状态。堆栈最后是 JDK 和 WebLogic 的方法，是否意味着 JDK 或 WebLogic 本身有性能问题？一个有经验的工程师其实会反问，如果基础的类库有问题，大概率早就有人报告了，所以还是看看自己哪里有问题。

> 这个思考过程其实也告诉我们，应该等某个产品的大版本成熟后再选用，这样应该可以避开那些严重的软件 Bug 。

此时此刻，如果我跟这个客户和开发商说是他们应用的问题，估计不会得到太正面的回应，毕竟证据不明显，而开发商和客户的技术水平可能更加无法理解这些现象。

那时的我的知识水平也比较有限，所以只能从现有的数据中寻找线索，于是我做了一个后来看来非常正确的动作，我将所有的线程堆栈做了一个统计，形成以下表格:

| **正在执行的方法** | **线程数量** | **百分比** |
|-|-|-|
| java/util/zip/ZipFile.getEntry(Native Method) | 33 | 16% |
| java/util/zip/ZipFile.getEntry(ZipFile.java:290(Compiled Code)) | 24 | 12% |
| com/yyy/util/UUID.(UUID.java:81(Compiled Code)) | 24 | 12% |

而且这些堆栈都指向了同一个方法：

```java
at org/apache/axis/client/Service.getAxisClient(Service.java:143(Compiled Code)) 
```

突然之间，我做开发时的一个记忆闪现了出来：对于 EJB 操作，因为 EJB Stub 的创建非常耗时，应该在客户端进行缓存。这个 Axis 的客户端，是否也有类似的问题？

## 解决问题

与应用开发人员一起找到了这段代码对应的应用代码，发现果然是每一次请求都会新建一个 Axis 客户端。于是修改代码，将 Axis 客户端存放到了 ThreadLocal 上，又重新进行了测试。效果相当的惊人，吞吐量轻松提高了 10 倍以上。

## 什么是 Profiling 工具？

这次问题处理，帮客户解决了大问题，对我个人也有着重大的意义，从此我对这个行业有了比较充分的信心。

不久之后我进了 IBM，主要是做 WebLogic 和 WebSphere Application Server （WAS）的支持。WAS 有着更加健全的诊断体系，例如 [WAS 的 MustGather 网站](https://www.ibm.com/support/pages/mustgather-read-first-websphere-application-server-and-liberty)详细说明了不同的故障应该收集的信息，以及处理方法。这让我有机会更系统地学习软件的问题诊断。

因为当时 AIX 的市场占有率很高，所以接触到的工具也是 AIX 的。通过学习和实践，我发现了 tprof 这个工具，例如通过执行命令 `tprof -kesj -x sleep 60`，我们可以得到以下报告：

```
...
Shared Object                                                             %  
=============                                                          ======
/usr/java6_64/jre/lib/ppc64/default/libj9prt24.so                       38.23
/usr/java6_64/jre/lib/ppc64/default/libjclscar_24.so                    26.27

...
 Total % For All Processes (/usr/java6_64/jre/lib/ppc64/default/libj9prt24.so) = 38.23

Subroutine                                            %   Source              
==========                                         ====== ======              
rt_time_TEXT                                        27.92 rt_time.s           
.j9time_current_time_millis                         10.32 aix/j9time.c        

Profile: /usr/java6_64/jre/lib/ppc64/default/libjclscar_24.so

  Total % For All Processes (/usr/java6_64/jre/lib/ppc64/default/libjclscar_24.so) = 26.27

Subroutine                                            %   Source              
==========                                         ====== ======              
.JIT_java_lang_System_currentTimeMillis             20.38 jlsys.s             
._ptrgl                                              5.89 ptrgl_64.s 
...

```

这个报告是 60 秒的时间里 CPU 被程序占用的一个统计报告。可以看到 38.23 的 CPU 时间在执行动态链接库 `libj9prt24.so` 的程序，具体来说 27.92% 是在执行 `rt_time_TEXT` 这个方法。

> 这是取自另一个故障的数据，应用中大量的获取系统时间的操作严重的影响了系统的运行效率。

如果我早点知道 `tprof` ，我可能可以更好地完成本文所说的那次问题诊断，其实我已经自发的用 tprof 的思想执行了 profiling。

tprof 命令执行时，每隔一定的时钟周期， 便会记录正在执行的指令，然后将所有的记录进行统计分析，形成报告。报告中出现较多的指令，通常也是占用 CPU 最多的指令，从而我们可以判断哪些方法，哪些组件可能存在性能问题。

现在大家都知道火焰图，这正是 profiling 工具收集数据的一种图形化展示方式：

![](https://user-images.githubusercontent.com/662636/149874240-438e017e-3c99-457f-963b-9d91d2a586ec.png)

## 其他工具

随着 Linux 的占有率越来越高，我们更多的使用 perf 命令实现 profiling。许多新兴的编程语言，也内置了更好的工具，例如 go 语言的 [pprof](https://github.com/google/pprof)。随着云原生的发展，还有 eBPF 的出现，又有人提出了 [continuous profiling](https://www.cncf.io/blog/2022/05/31/what-is-continuous-profiling/) 这个概念。例如 [Pyroscope](https://github.com/grafana/pyroscope) ，通过这样的工具，我们可以随时随地实现 profiling 。

## 后记

职业生涯早期的这个关键之战对我意义重大。在那短短的一周里，我解决了两个关键问题，让项目能够顺利上线，赢得了合作伙伴的信任。更重要的是，这次支持也给了我信心，促使我完善自己的知识体系，让我能够更自信从容地应对未来的挑战。

不过，自此我也发现，这个行业有太多不专业的人。许多时候，即使你解决了问题，可能也无法得到感谢。例如这个客户的领导其实完全不懂技术，她并不能判断谁对谁错，谁的贡献更大，但是却有一股子不知道来自何处的傲慢。多年之后又遇到了这位领导，态度依旧，实在是不想跟这种人合作了。以后有机会跟大家聊聊工作生涯中遇到的奇葩事情奇葩人，顺便聊聊技术。