## WebLogic12.1.3的几个新bug

### 找不到ExecutionContext类

配置了WTC，每次执行tpcall日志都会有如下的报错：

```
java.lang.ClassNotFoundException: oracle.dms.context.ExecutionContext
at com.oracle.classloader.PolicyClassLoader.loadClass(PolicyClassLoader.java:267)
at com.oracle.classloader.weblogic.LaunchClassLoader.loadClass(LaunchClassLoader.java:62)
at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
at java.lang.Class.forName0(Native Method)
at java.lang.Class.forName(Class.java:264)
at weblogic.wtc.jatmi.DmsReflect.<init>(DmsReflect.java:28)
at weblogic.wtc.jatmi.DmsReflect.getInstance(DmsReflect.java:58)
at weblogic.wtc.jatmi.dsession._tpacall_internal(dsession.java:3151)
at weblogic.wtc.jatmi.dsession.tpacall(dsession.java:3444)
at weblogic.wtc.jatmi.dsession.tpcall(dsession.java:3991)
at weblogic.wtc.gwt.TuxedoConnection.tpcall(TuxedoConnection.java:1410)

```

可以查到这个bug[2187481_1](https://support.oracle.com/knowledge/Middleware/2187481_1.html)，对业务执行没有影响，发生的原因是tpcall的代码调用了DMS (Oracle Dynamic Monitoring Service)，但是WebLogic根本就没有配置DMS。解决办法就是安装JRF（Java Required Files，包含了DMS）；或者简单一点，也就是打补丁（24617915），然后增加以下WebLogic启动参数关闭对于DMS相关代码的调用：

```
-Dweblogic.wtc.disableECID=true

```

经过实际测试，最新的补丁集已经包含了这个问题的修正，直接添加启动参数即可。


### 找不到setPDBChangeEventListener方法

执行数据库相关的故障转移测试，发现日志中有以下错误：

```
java.lang.NoSuchMethodException: oracle.jdbc.internal.OracleConnection.setPDBChangeEventListener(oracle.jdbc.internal.PDBChangeEventListener)
at java.lang.Class.getMethod(Class.java:1786)
at weblogic.jdbc.common.internal.ConnectionEnvPDB.<init>(ConnectionEnvPDB.java:35)
at weblogic.jdbc.common.internal.ConnectionEnv.setConnection(ConnectionEnv.java:1060)
at weblogic.jdbc.common.internal.ConnectionEnvFactory.createResource(ConnectionEnvFactory.java:278)
at weblogic.common.resourcepool.ResourcePoolImpl.makeResources(ResourcePoolImpl.java:1331)
at weblogic.common.resourcepool.ResourcePoolImpl.makeResources(ResourcePoolImpl.java:1248)
at weblogic.common.resourcepool.ResourcePoolImpl.start(ResourcePoolImpl.java:240)
at weblogic.jdbc.common.internal.ConnectionPool.doStart(ConnectionPool.java:1626)

```

这个查一下，果然又是一个bug[2171926_1](https://support.oracle.com/knowledge/Middleware/2171926_1.html)，也是对业务并没有影响。发生的原因是JDBC驱动没有setPDBChangeEventListener这个方法，我晕！解决方法就是换驱动，或者打补丁（20741228）。WLS 12.1.3包含的是较早版本的JDBC 12.1.0.2，没有这个方法。经过实地查看，打过补丁的WebLogic已经更新了JDBC驱动：

```

[weblogic@wls1 orahome1]$ java -jar ./oracle_common/modules/oracle.jdbc/ojdbc8.jar
Oracle 12.2.0.1.0 JDBC 4.2 compiled with javac 1.8.0_91 on Tue_Dec_13_06:08:31_PST_2016

```

然后看了一下驱动中的类，OracleConnection类已经包含了setPDBChangeEventListener方法，所以也不需要单独打补丁了。