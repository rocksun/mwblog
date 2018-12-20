## ChangeAwareClassLoader.loadClass死锁

SUN JDK 8, WebLogic 12.1.3，压力测试中出现所有线程锁住的现象，jstack得到thread dump，发现了死锁：

```


Found one Java-level deadlock:
=============================
"[STUCK] ExecuteThread: '999' for queue: 'weblogic.kernel.Default (self-tuning)'":
  waiting to lock monitor 0x00007f1ff56a07f8 (object 0x000000058e5e0668, a org.eclipse.rap.rwt.internal.util.SerializableLock),
  which is held by "[STUCK] ExecuteThread: '65' for queue: 'weblogic.kernel.Default (self-tuning)'"
"[STUCK] ExecuteThread: '65' for queue: 'weblogic.kernel.Default (self-tuning)'":
  waiting to lock monitor 0x00007f1fe8f53188 (object 0x00000005b5db7af8, a java.lang.Object),
  which is held by "[STUCK] ExecuteThread: '45' for queue: 'weblogic.kernel.Default (self-tuning)'"
"[STUCK] ExecuteThread: '45' for queue: 'weblogic.kernel.Default (self-tuning)'":
  waiting to lock monitor 0x00000000047e5908 (object 0x000000058377d2a0, a weblogic.utils.classloaders.ChangeAwareClassLoader),
  which is held by "[STUCK] ExecuteThread: '115' for queue: 'weblogic.kernel.Default (self-tuning)'"
"[STUCK] ExecuteThread: '115' for queue: 'weblogic.kernel.Default (self-tuning)'":
  waiting to lock monitor 0x000000000483c668 (object 0x00000005b5dc2108, a java.lang.Object),
  which is held by "[STUCK] ExecuteThread: '643' for queue: 'weblogic.kernel.Default (self-tuning)'"
"[STUCK] ExecuteThread: '643' for queue: 'weblogic.kernel.Default (self-tuning)'":
  waiting to lock monitor 0x00000000047e5908 (object 0x000000058377d2a0, a weblogic.utils.classloaders.ChangeAwareClassLoader),
  which is held by "[STUCK] ExecuteThread: '115' for queue: 'weblogic.kernel.Default (self-tuning)'"

......

"[STUCK] ExecuteThread: '115' for queue: 'weblogic.kernel.Default (self-tuning)'" #909 daemon prio=1 os_prio=0 tid=0x0000000004330800 nid=0x84b waiting for monitor entry [0x00007f1fdea64000]
   java.lang.Thread.State: BLOCKED (on object monitor)
	at weblogic.utils.classloaders.ChangeAwareClassLoader.loadClass(ChangeAwareClassLoader.java:68)
	- waiting to lock <0x00000005b5dc2108> (a java.lang.Object)
	at weblogic.utils.classloaders.ChangeAwareClassLoader.loadClass(ChangeAwareClassLoader.java:53)
	at java.lang.ClassLoader.defineClass1(Native Method)
	at java.lang.ClassLoader.defineClass(ClassLoader.java:763)
	at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:142)
	at weblogic.utils.classloaders.GenericClassLoader.defineClassInternal(GenericClassLoader.java:1113)
	at weblogic.utils.classloaders.GenericClassLoader.defineClass(GenericClassLoader.java:1046)
	at weblogic.utils.classloaders.GenericClassLoader.findLocalClass(GenericClassLoader.java:1038)
	at weblogic.utils.classloaders.GenericClassLoader.findClass(GenericClassLoader.java:990)
	at weblogic.utils.classloaders.ChangeAwareClassLoader.findClass(ChangeAwareClassLoader.java:104)
	at weblogic.utils.classloaders.ChangeAwareClassLoader.loadClass(ChangeAwareClassLoader.java:82)
	- locked <0x000000058377d2a0> (a weblogic.utils.classloaders.ChangeAwareClassLoader)
	- locked <0x00000005b5ed8aa0> (a java.lang.Object)
	at weblogic.utils.classloaders.ChangeAwareClassLoader.loadClass(ChangeAwareClassLoader.java:53)

```

找到了这个说明[Multithreaded Custom Class Loaders in Java SE 7](https://docs.oracle.com/javase/7/docs/technotes/guides/lang/cl-mt.html)，如果发生死锁，建议增加虚拟机参数：

```
-XX:+AlwaysLockClassLoader
```

这样在执行自定义Class Loader的findClass()或loadClass()方法前，会收回class loader锁，就不会引发死锁了。详细解释看上面的说明。
