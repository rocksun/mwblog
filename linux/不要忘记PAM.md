## 不要忘记PAM

一个客户要求升级sshd和vsftpd，结果都出现了一些奇怪的问题，而原因都与PAM有关。

### sshd

升级完sshd，发现用户通过ssh登录后的ulimit设置丢失，而如果用户是通过root su到该用户，则ulimit设置正常。经过排查，发现与PAM的设置有关。

编译安装新版的sshd时会修改sshd的配置文件和sshd的pam配置文件：

 * /etc/ssh/sshd_config
 * /etc/pam.d/sshd

安装过程中为了保证用户的正常登录，sshd_config的UsePAM设置变成了no（新装系统应该为yes）：

```bash

UsePAM no

```

设置为no时，用户通过ssh登录时并不会执行相关的PAM模块，对于ulimit来说就是pam_limits模块，在/etc/pam.d/sshd中对应：

```bash

session     required      pam_limits.so

```

所以为了这个解决这个问题，我们需要开启PAM，并保证PAM模块工作正常，所以修改sshd_config中的配置下如下：


```bash

UsePAM no

```

并将/etc/pam.d/sshd恢复到操作系统的默认配置：

```bash

#%PAM-1.0
auth       required     pam_sepermit.so
auth       include      password-auth
account    required     pam_nologin.so
account    include      password-auth
password   include      password-auth
# pam_selinux.so close should be the first session rule
session    required     pam_selinux.so close
session    required     pam_loginuid.so
# pam_selinux.so open should only be followed by sessions to be executed in the user context
session    required     pam_selinux.so open env_params
session    optional     pam_keyinit.so force revoke
session    include      password-auth

```

然后执行service restart sshd即可。

### vsftpd

升级完vsftpd，结果用户发现ftp根本无法登陆，开了ftp客户端的debug功能，看到这些信息：

```

Response: 220 vsFTPd 3.0.2+ (ext.1) ready...
Command: USER 9903286
Response: 331 Please specify the password.
Command: PASS ********************
Response: GThread-ERROR **: file gthread-posix.c: line 140 (g_thread_impl_init): error 'Operation not permitted' during 'pthread_getschedparam (pthread_self(), &policy, &sched)'
Error: Could not connect to server

```

查看vsftpd的日志，也没有更有用的信息。查看/var/log/messages，发现每次登录都会产生coredump，用gdb跟踪后发现跟认证模块有关，然后发现vsftpd的PAM配置文件/etc/pam.d/vsftpd在安装中已经被覆盖，新的配置有问题，所以恢复到升级前的配置，然后service restart vsftpd，ftp恢复正常。