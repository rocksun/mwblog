# CoreGroup导致AppServer无法启动

## WebSphere的CoreGroup有什么用？

对于我们现在的大多数应用来说，WebSphere的HAManager CoreGroup没有任何用处。我们现在的大多数应用使用专门的硬件或软件将HTTP请求转发到WebSphere Application Server，这些负载均衡器可以通过Server的HTTP端口获取其状态，并不需要其他辅助手段。

所以你可能想到了，想不到也正常，WebSphere的CoreGroup是用来在WebSphere的各个进程之间同步信息用的，这里说的进程包括DMGR，NodeAgent和Application Server。同步的信息主要是各个进程的状态，以便实现某些服务的高可用，例如EJB消息队列服务。当然，我见过的应用，99.9%是没有使用这些服务的，所以我说CoreGroup没用。不过，即使没用，副作用还是可以有的。

## Server无法启动

一个两个受管节点和一个DMGR节点组成的环境。许多Application Server无法启动完成，然后日志中的报错都跟CoreGroup有关：


```
[12/19/18 10:43:16:810 GMT+08:00] 00000018 RoleViewLeade I   DCSV8030I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSNode02\nodeagent: Failed  to join or establish a view with member [HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr]. The reason is Not all candidates are connected ConnectedSetMissing=   [ ] ConnectedSetAdditional [ HQxPVL-PDMS-A01Cell01\PDMSNode01\PDMSServer012 ].
[12/19/18 10:43:19:056 GMT+08:00] 000003c0 NodeSyncTask  A   ADMS0003I: The configuration synchronization completed successfully.
[12/19/18 10:43:20:814 GMT+08:00] 00000018 RoleViewLeade I   DCSV8030I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSNode02\nodeagent: Failed  to join or establish a view with member [HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr]. The reason is Not all candidates are connected ConnectedSetMissing=   [ ] ConnectedSetAdditional [ HQxPVL-PDMS-A01Cell01\PDMSNode01\PDMSServer012 ].
[12/19/18 10:43:24:820 GMT+08:00] 00000018 RoleViewLeade I   DCSV8030I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSNode02\nodeagent: Failed  to join or establish a view with member [HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr]. The reason is Not all candidates are connected ConnectedSetMissing=   [ ] ConnectedSetAdditional [ HQxPVL-PDMS-A01Cell01\PDMSNode01\PDMSServer012 ].
```

这些错误会不断出现，看起来相当费解。

## 日志分析

不过仔细看下来，似乎分为以下几类。

### 已经加入DefaultCoreGroup的进程


已经加入的DMGR：

```
[12/19/18 10:48:40:814 GMT+08:00] 0000001f RoleMergeLead I   DCSV8054I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr: View change in process. 
[12/19/18 10:48:40:816 GMT+08:00] 0000001f RoleMergeLead I   DCSV8030I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr: Failed  to join or establish a view with member [HQxPVL-PDMS-A01Cell01\PDMSNode02\nodeagent]. The reason is Sender's reason: Not all candidates are connected. 
[12/19/18 10:48:40:817 GMT+08:00] 0000001f RoleMergeLead I   DCSV8030I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr: Failed  to join or establish a view with member [HQxPVL-PDMS-A01Cell01\PDMSNode01\PDMSServer012]. The reason is Sender's reason: Not all candidates are connected. 
[12/19/18 10:48:40:817 GMT+08:00] 0000001d VSyncAlgo1    I   DCSV2004I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr: View synchronization completed successfully. The View Identifier is (19817:0.HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr). The internal details are None.
[12/19/18 10:48:40:820 GMT+08:00] 0000001f CoreGroupMemb I   DCSV8050I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr: New view installed, identifier (19818:0.HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr), view size is 3 (AV=3, CD=5, CN=5, DF=9)
[12/19/18 10:48:40:822 GMT+08:00] 00000004 ViewReceiver  I   DCSV1033I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr: Confirmed all new view members in view identifier (19818:0.HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr). View channel type is View|Ptp.
```

已经加入的NodeAgent：

```
[12/19/18 10:46:28:630 GMT+08:00] 00000010 VSyncAlgo1    I   DCSV2004I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSNode01\nodeagent: View synchronization completed successfully. The View Identifier is (19784:0.HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr). The internal details are None.
[12/19/18 10:46:28:632 GMT+08:00] 00000018 CoreGroupMemb I   DCSV8050I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSNode01\nodeagent: New view installed, identifier (19785:0.HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr), view size is 3 (AV=3, CD=5, CN=5, DF=9)
[12/19/18 10:46:28:634 GMT+08:00] 00000004 ViewReceiver  I   DCSV1033I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSNode01\nodeagent: Confirmed all new view members in view identifier (19785:0.HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr). View channel type is View|Ptp.
```

已经加入的ApplicationServer：

```
[12/19/18 10:54:09:315 GMT+08:00] 0000000b VSyncAlgo1    I   DCSV2004I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSNode01\PDMSServer011: View synchronization completed successfully. The View Identifier is (19899:0.HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr). The internal details are None.
[12/19/18 10:54:09:317 GMT+08:00] 0000000d CoreGroupMemb I   DCSV8050I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSNode01\PDMSServer011: New view installed, identifier (19900:0.HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr), view size is 3 (AV=3, CD=5, CN=5, DF=9)
[12/19/18 10:54:09:318 GMT+08:00] 00000005 ViewReceiver  I   DCSV1033I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSNode01\PDMSServer011: Confirmed all new view members in view identifier (19900:0.HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr). View channel type is View|Ptp.
```

可以看到共同点是“View synchronization completed successfully”，是的，我知道你同步成功了，但是你不用反复的提示我吧。事实上，在正常的WebSphere环境中，并不会反复打印这些信息，这些信息的反复出现也意味问题的存在。另外，AV=3 提示我们，只有上面三个进程正常加入了DefaultCoreGroup。

### 无法加入DefaultCoreGroup的进程

一些其他的进程的报错似乎指向了凶手：

```
[12/19/18 10:43:16:810 GMT+08:00] 00000018 RoleViewLeade I   DCSV8030I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSNode02\nodeagent: Failed  to join or establish a view with member [HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr]. The reason is Not all candidates are connected ConnectedSetMissing=   [ ] ConnectedSetAdditional [ HQxPVL-PDMS-A01Cell01\PDMSNode01\PDMSServer012 ].

[12/18/18 19:07:24:984 GMT+08:00] 0000000d RoleViewLeade I   DCSV8030I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSNode02\PDMSServer021: Failed  to join or establish a view with member [HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr]. The reason is Not all candidates are connected ConnectedSetMissing=   [ ] ConnectedSetAdditional [ HQxPVL-PDMS-A01Cell01\PDMSNode01\PDMSServer012 ].

[12/18/18 19:22:02:750 GMT+08:00] 0000000e RoleViewLeade I   DCSV8030I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSNode02\PDMSServer022: Failed  to join or establish a view with member [HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr]. The reason is Not all candidates are connected ConnectedSetMissing=   [ ] ConnectedSetAdditional [ HQxPVL-PDMS-A01Cell01\PDMSNode01\PDMSServer012 ].

[12/18/18 18:09:07:738 GMT+08:00] 0000000d RoleViewLeade I   DCSV8030I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSNode02\PDMSServer023: Failed  to join or establish a view with member [HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr]. The reason is Not all candidates are connected ConnectedSetMissing=   [ ] ConnectedSetAdditional [ HQxPVL-PDMS-A01Cell01\PDMSNode01\PDMSServer012 ].

```

这几个进程都声称自己通过 dmgr 尝试加入到 DefaultCoreGroup ，但是似乎无法连接 ConnectedSetAdditional 的 PDMSServer012 ， 也就是 dmgr 声称已经连接到的进程，所以无法加入到 DefaultCoreGroup。然后看 PDMSServer012 的日志：


```
[12/19/18 10:56:13:591 GMT+08:00] 0000000d RoleViewLeade I   DCSV8030I: DCS Stack DefaultCoreGroup at Member HQxPVL-PDMS-A01Cell01\PDMSNode01\PDMSServer012: Failed  to join or establish a view with member [HQxPVL-PDMS-A01Cell01\PDMSDmgr01\dmgr]. The reason is Not all candidates are connected ConnectedSetMissing=   [ ] ConnectedSetAdditional [ HQxPVL-PDMS-A01Cell01\PDMSNode02\nodeagent ]. 
```

嗯，了解，你说你连不上 PDMSNode02 的 nodeagent ，而人家在前面说了连不上你，你俩互相连不上。

## 解决方案

既然 PDMSNode02 的 nodeagent 和 PDMSServer012 互相指责，所以他俩某种意义上进入了死锁状态， 也幸好是这俩有矛盾，给了我们不影响业务的情况下恢复的机会。停止这两个进程，然后重启 PDMSNode02 上的其他 Application Server 以及 PDMSServer012。这次重启成功了。

并不是很清楚何种操作造成了这样的后果，但是为了避免最可怕的情况，可以在配置上做一些改进。可以新创建一个CoreGroup，把不同的进程加入到不同的CoreGroup，这样，即使一个CoreGroup出现问题，也不会影响另一个CoreGroup。


## 参考资料

这一个很详细的[说明](http://www-01.ibm.com/support/docview.wss?uid=swg21245012)，解释了各种情况，如果你要深入研究可以一看。

