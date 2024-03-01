<!--
title: 网关API实践（2）-FSM网关中的黑名单和白名单访问控制
cover: https://miro.medium.com/v2/resize:fit:720/format:webp/0*ymRzv1VvxhBr1vc5.png
-->

注意力机制推动深度学习在自然语言处理中的进一步发展

> 译自 [Gateway API Practices (Part Two) — Blacklist and Whitelist Access Control in FSM Gateway](https://blog.flomesh.io/gateway-api-practices-part-two-blacklist-and-whitelist-access-control-in-fsm-gateway-253309a4fc35)，作者 Addo Zhang 。


域级访问控制:基于域名的网络流量管理策略。它涉及为匹配特定域名条件的流量实施访问规则,如允许或阻止与某些域的通信。

路由维护级访问控制:基于路由(请求头、方法、路径、参数)的管理策略,其中访问控制策略应用于路由以管理访问特定路由的流量。

接下来,我们将演示如何使用黑名单和白名单访问控制。

演示

先决条件

Kubernetes集群 

kubectl工具

环境准备

安装FSM网关

有关FSM网关安装,请参阅安装文档。这里,我们选择CLI方法进行安装。

下载FSM CLI,当前版本为*v1.2.0。

system=$(uname -s | tr '[:upper:]' '[:lower:]') 
arch=$(uname -m | sed -E 's/x86_/amd/' | sed -E 's/aarch/arm/')
release=v1.2.0
curl -L https://github.com/flomesh-io/fsm/releases/download/$release/fsm-$release-$system-$arch.tar.gz | tar -vxzf -
./$system-$arch/fsm version
sudo cp ./$system-$arch/fsm /usr/local/bin/fsm

在FSM安装过程中启用FSM网关,默认情况下该网关未启用。

fsm install \
--set=fsm.fsmGateway.enabled=true

确认安装了网关类控制器:flomesh.io/gateway-controller。

kubectl get gatewayclass
NAME                   CONTROLLER                     ACCEPTED   AGE
fsm-gateway-cls        flomesh.io/gateway-controller   True        12h

部署示例应用程序

<transl

更新策略后,发送请求进行测试。访问路径/headers的结果与以前相同。

curl -I http://$GATEWAY_IP:8000/headers -H 'host:foo.example.com' -H 'x-forwarded-for:112.94.5.242'
HTTP/1.1 200 OK
server: gunicorn/19.9.0
date: Fri, 29 Dec 2023 02:39:02 GMT  
content-type: application/json
content-length: 139
access-control-allow-origin: *
access-control-allow-credentials: true
connection: keep-alive

curl -I http://$GATEWAY_IP:8000/headers -H 'host:foo.example.com' -H 'x-forwarded-for: 10.42.0.1'
HTTP/1.1 403 Forbidden
content-length: 9
connection: keep-alive

然而,如果访问路径/get,则没有限制。

curl -I http://$GATEWAY_IP:8000/get -H 'host:foo.example.com' -H 'x-forwarded-for: 10.42.0.1'  
HTTP/1.1 200 OK
server: gunicorn/19.9.0
date: Fri, 29 Dec 2023 02:40:18 GMT
content-type: application/json  
content-length: 230
access-control-allow-origin: *
access-control-allow-credentials: true
connection: keep-alive

Kubernetes

网关  

网关API

