<!--
title: Argo CD与GitOps：让你的Kubernetes应用“自愈”新生
cover: https://cdn.thenewstack.io/media/2025/12/070a0120-band-aids.jpg
summary: GitOps 结合 Argo CD 实现了 Kubernetes 应用程序的自动化部署和自我修复。它通过将集群状态与 Git 仓库同步，确保应用程序始终符合预期，并在出现漂移时自动修复。
-->

GitOps 结合 Argo CD 实现了 Kubernetes 应用程序的自动化部署和自我修复。它通过将集群状态与 Git 仓库同步，确保应用程序始终符合预期，并在出现漂移时自动修复。

> 译自：[Make Your Kubernetes Apps Self-Heal With Argo CD and GitOps](https://thenewstack.io/make-your-kubernetes-apps-self-heal-with-argo-cd-and-gitops/)
> 
> 作者：Vinod Pal

Kubernetes 生产环境应用程序传统上需要人工操作和时间。

GitOps 结合 [Argo CD 解决了这个问题](https://thenewstack.io/why-argo-cd-is-the-lifeline-of-gitops/)。它使你的集群与 Git 同步，你的存储库定义了所需的状态。 [Argo CD](https://thenewstack.io/survey-argocd-leaves-flux-and-other-gitops-platforms-behind/) 确保集群始终与它匹配，当出现问题时，它会自动修复。通过 GitOps，你的应用程序变得自我修复，并始终与 Git 保持同步。

## **什么是 GitOps 和自我修复？**

[GitOps](https://thenewstack.io/gitops-in-the-real-world-barriers-and-best-practices/) 意味着你的 Git 存储库是所有事物的唯一真实来源。当[现实与 Git 不符时](https://thenewstack.io/i-need-to-talk-to-you-about-kubernetes-gitops/)，系统会自动修复。

你的应用程序配置存储在 Git 中，对应用程序或 Git 源代码的任何更改都将自动修复。这是 GitOps 的最佳和最简单的机会，可以加速传统的部署过程。

### 恢复传统部署

当你遵循传统部署过程时，在许多情况下事情可能会出现意想不到的转折：

* 有人可能手动更改生产设置，导致你的生产停滞。
* 服务器上的技术失误可能会暂停生产，然后你必须手动重启。
* 你的应用程序配置发生变化，你必须跟踪所有更改。

GitOps 有效且简单地处理所有这些可能性。

### GitOps 自我修复解决方案

通过 GitOps，你可以将应用程序的当前状态维护在 Git 存储库中。Argo CD 等 GitOps 技术可确保 Git 中定义的内容与实际的应用程序部署匹配。

如果服务器出现技术问题，GitOps 将自动解决它们并将你的应用程序恢复到定义的状态。这就是 GitOps 中的自我修复。

最重要的是，你还可以保留 Git 中所有更改的审计追踪。

## **第 0 步：先决条件**

* 系统上已安装 Docker。
* 我首选：带有 Ubuntu 的 WSL2。随意使用你自己的 Linux 设置。
* GitHub 账户。
* Docker Hub 账户。
* 我首选：React 项目（你可以使用任何项目）。
* Kubernetes 知识（可选）。

## **第 1 步：安装并启动 Minikube**

首先，设置一个 Kubernetes 集群。本教程中，我们将使用 Minikube。它轻量级，非常适合学习。

（如果你已经有本地运行的集群，可以跳过此步骤。）

### **安装 Minikube**

运行以下命令安装 Minikube：

```
# Download and install minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
# Install kubectl if you don't have it
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
# Note: Some Linux distributions need this for Minikube
sudo apt install conntrack
```

### **启动 Minikube 集群**

运行以下命令之前，请确保 Docker 正在运行。

```
# Start minikube with Docker driver
minikube start --driver=docker

# Verify everything is working
kubectl version --client
kubectl get nodes

# You should see:
# NAME       STATUS   ROLES           AGE
# minikube   Ready    control-plane   1m

# Enable ingress addon (useful for later)
minikube addons enable ingress
```

## 第 2 步：创建你的 React 应用程序

```
# Create the app
cd ~/projects
npx create-react-app my-selfhealing-app
cd my-selfhealing-app
```

### **更新应用程序以进行演示**

替换 `src/app.js`：

```
import './App.css';
import { useState, useEffect } from 'react';

function App() {
  const [count, setCount] = useState(0);
  const [timestamp, setTimestamp] = useState('');

  useEffect(() =&gt; {
    setTimestamp(new Date().toLocaleString());
  }, []);

  return (
    &lt;div className="App"&gt;
      &lt;header className="App-header"&gt;
        &lt;h1&gt;🛡️ Self-Healing React App&lt;/h1&gt;
        &lt;p&gt;This app automatically fixes itself using GitOps!&lt;/p&gt;
        
        &lt;div style={{ 
          background: 'rgba(255,255,255,0.1)', 
          padding: '20px', 
          borderRadius: '10px',
          margin: '20px 0' 
        }}&gt;
          &lt;button 
            on​Click={() =&gt; setCount(count + 1)}
            style={{
              padding: '10px 20px',
              fontSize: '16px',
              backgroundColor: '#61dafb',
              border: 'none',
              borderRadius: '5px',
              cursor: 'pointer'
            }}
          &gt;
            Clicked {count} times
          &lt;/button&gt;
        &lt;/div&gt;

        &lt;div style={{ fontSize: '14px', opacity: 0.8 }}&gt;
          &lt;p&gt;🔄 Auto-sync enabled&lt;/p&gt;
          &lt;p&gt;🛠️ Self-healing active&lt;/p&gt;
          &lt;p&gt;📅 Deployed: {timestamp}&lt;/p&gt;
          &lt;p&gt;🏷️ Version: 1.0.0&lt;/p&gt;
        &lt;/div&gt;
      &lt;/header&gt;
    &lt;/div&gt;
  );
}


export default App;
```

注意：这段代码应该可以正常工作。你也可以使用 Vite 或任何其他框架，因为 CRA 已经弃用。

### **创建 Dockerfile**

Dockerfile 用于编写 Docker 代码库。

创建 `Dockerfile`：

确保将此文件放在项目根目录中。将以下代码粘贴到其中。

```
FROM node:18-alpine as builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

在这里，我们首先安装 node，然后创建构建，然后遵循在端口 80 上运行应用程序的说明。

### **推送到 GitHub**

所有代码准备好后，将其推送到 GitHub。

```
git init
git add .
git commit -m "Initial self-healing app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/my-selfhealing-app.git
git push -u origin main
```

## **第 3 步：构建并推送 Docker 镜像**

现在代码已准备好，创建一个 Docker 镜像并将其推送到 Docker Hub。

如果你没有 Docker Hub 账户，可以从 [Docker Hub](https://hub.docker.com/) 页面注册并创建一个。

另外，请确保 Docker 在本地运行。如果你没有在本地安装 Docker，可以安装 [Docker Desktop](https://www.docker.com/products/docker-desktop/)。

```
# Build the image
docker build -t YOUR_DOCKERHUB_USERNAME/selfhealing-app:v1.0.0 .

# Push to DockerHub
docker login
docker push YOUR_DOCKERHUB_USERNAME/selfhealing-app:v1.0.0
```

## **第 4 步：创建 GitOps 配置仓库**

要开始使用 GitOps，请创建一个新的 Git 存储库。这很重要，因为源代码和 GitOps 可能有单独的存储库。

```
# Build the image
docker build -t YOUR_DOCKERHUB_USERNAME/selfhealing-app:v1.0.0 .

# Push to DockerHub
docker login
docker push YOUR_DOCKERHUB_USERNAME/selfhealing-app:v1.0.0
```

### **创建 Kubernetes 清单**

首先，创建一个名为“app”的新文件夹。在此文件夹中，创建与 Kubernetes 相关的文件。

创建 `app/deployment.yaml`：

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: selfhealing-app
  namespace: default
spec:
  replicas: 2  # We are having 2 replicas of our app
  selector:
    matchLabels:
      app: selfhealing-app
  template:
    metadata:
      labels:
        app: selfhealing-app
    spec:
      containers:
      - name: react-app
        image: YOUR_DOCKERHUB_USERNAME/selfhealing-app:v1.0.0  # Update this!
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "64Mi"
            cpu: "50m"
          limits:
            memory: "128Mi"
            cpu: "100m"
```

这是一个带有基本信息的常规 Kubernetes 部署文件。请务必用你的 Docker 镜像更新 `image`。

接下来，为 Kubernetes 服务创建另一个文件。

创建 `app/service.yaml`：

```
apiVersion: v1
kind: Service
metadata:
  name: selfhealing-app-service
  namespace: default
spec:
  selector:
    app: selfhealing-app
  ports:
  - port: 80
    targetPort: 80
  type: LoadBalancer
```

### **提交 GitOps 配置**

所有文件创建完成后，将更改推送到 GitHub。

```
git add .
git commit -m "Add GitOps configuration for self-healing app"
git push origin main
```

## **第 5 步：安装 Argo CD**

接下来，安装使自我修复成为可能的工具。

```
# Create Argo CD namespace
kubectl create namespace Argo CD

# Install Argo CD
kubectl apply -n Argo CD -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Wait for it to be ready (takes 2-3 minutes)
echo "Installing Argo CD... this takes a few minutes"
kubectl wait --for=condition=available --timeout=300s deployment/Argo CD-server -n Argo CD
```

### **访问 Argo CD**

```
# Get the admin password
echo "Argo CD Password:"
kubectl -n Argo CD get secret Argo CD-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d && echo
# It will give output something like this. Keep the password handy. Username is admin.
# Argo CD Password:
#Gvy5q5gb3kADdS3w

# Start port forwarding (keep this running)
kubectl port-forward svc/Argo CD-server -n Argo CD 8080:443 > /dev/null 2>&1 &

echo "Argo CD UI: https://localhost:8080"
```

现在 Argo CD 将在端口 8080 上运行。在浏览器中打开此 URL：<https://localhost:8080>。

你会看到这样的登录屏幕：

[![AgroCD login screen](https://cdn.thenewstack.io/media/2025/12/681d53eb-image7-1024x479.png)](https://cdn.thenewstack.io/media/2025/12/681d53eb-image7-1024x479.png)

*AgroCD 登录屏幕。*

你可以使用用户名“admin”和你刚刚通过上述命令生成的密码。登录完成后，是时候在 Argo CD 中创建应用程序了。

## 第 6 步：创建自我修复应用程序

告诉 Argo CD 管理你的应用程序并启用自我修复。

### **创建 Argo CD 应用程序**

创建 `selfhealing-application.yaml`：

```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: selfhealing-app
  namespace: Argo CD
spec:
  project: default
  source:
    repoURL: https://github.com/YOUR_USERNAME/my-GitOps-config  # Update this!
    targetRevision: HEAD
    path: app
  destination:
    server: https://kubernetes.default.svc
    namespace: default
  syncPolicy:
    automated:
      prune: true      # Remove extra resources
      selfHeal: true   # THE MAGIC: Auto-fix when things drift
```

应用它：

```
# Update the repoURL first, then:
kubectl apply -f selfhealing-application.yaml

# This will give the result below
# application.argoproj.io/selfhealing-app configured
```

完成后，你应该会在 Argo CD 控制面板中看到你的应用程序。

[![Argo CD UI showing that it  is running locally](https://cdn.thenewstack.io/media/2025/12/524f4f6a-image2.png)](https://cdn.thenewstack.io/media/2025/12/524f4f6a-image2.png)

*Argo CD UI 显示它正在本地运行。*

## **第 7 步：访问你的自我修复应用程序**

```
# Check pods are running
kubectl get pods -l app=selfhealing-app
```

它应该显示如下：

[![Output showing that pods are running](https://cdn.thenewstack.io/media/2025/12/4a9ca882-image1-1024x96.png)](https://cdn.thenewstack.io/media/2025/12/4a9ca882-image1-1024x96.png)

显示 Pod 正在运行的输出。

```
# Access your app using port-forward
kubectl port-forward svc/selfhealing-app-service 3000:80 > /dev/null 2>&1 &
```

访问

`http://localhost:3000`

查看你的应用程序运行情况。

[![Initial app with first version](https://cdn.thenewstack.io/media/2025/12/6a37ca07-image6-1024x660.png)](https://cdn.thenewstack.io/media/2025/12/6a37ca07-image6-1024x660.png)

*带有第一个版本的初始应用程序。*

## **第 8 步：测试自我修复**

是时候测试更改并查看自我修复过程的实际运行情况了。

### **删除 Pod**

从简单地删除一个 Pod 开始。

```
# See your pods
kubectl get pods -l app=selfhealing-app

#You should see 2 pods
#NAME                               READY   STATUS    RESTARTS      AGE
#selfhealing-app-58cb69c845-ndssn   1/1     Running   1 (47m ago)   43h
#selfhealing-app-58cb69c845-swsf6   1/1     Running   1 (47m ago)   43h

# Delete one pod
kubectl delete pod -l app=selfhealing-app

# Watch it get recreated immediately
kubectl get pods -l app=selfhealing-app
#Now, even after deleting your pods, you will still see 2 pods.
```

这是基本的 Kubernetes 行为，但现在让我们看看 Argo CD 的自我修复……

### **删除整个部署**

现在，更进一步，删除所有内容。

```
# The ultimate test - delete everything!
kubectl delete deployment selfhealing-app
kubectl delete service selfhealing-app-service

# Watch Argo CD recreate everything automatically
kubectl get all -l app=selfhealing-app -w
```

[![Argo CD app status, showing sync time and other details](https://cdn.thenewstack.io/media/2025/12/14466621-image3.png)](https://cdn.thenewstack.io/media/2025/12/14466621-image3.png)

*Argo CD 应用程序状态，显示同步时间和其他详细信息。*

Argo CD 控制面板将显示同步时间为“几秒前”。这表明它已经同步并再次创建了应用程序。换句话说，Argo CD 确保现实始终与 Git 匹配。

## **第 9 步：进行实际更新（GitOps 方式）**

现在，进行合法更改以查看 GitOps 如何处理更新。

### **更新你的应用程序**

编辑 `src/App.js` 并更改：

```
<p>🏷️ Version: 2.0.0 - Updated via GitOps!</p>
```

此更新反映了应用程序的新版本。一个简单的更改。

### **构建并推送新版本**

现在，创建新的 Docker 构建并将其推送到 Docker Hub。另外，将源代码推送到 GitHub。

```
cd ~/projects/my-selfhealing-app

# Build and push new version
docker build -t YOUR_DOCKERHUB_USERNAME/selfhealing-app:v2.0.0 .
docker push YOUR_DOCKERHUB_USERNAME/selfhealing-app:v2.0.0

# Commit app changes
git add .
git commit -m "Update to version 2.0.0"
git push origin main
```

### **更新 GitOps 配置**

接下来，打开 GitOps 存储库并使用更新的 `app/deployment.yaml` 文件，更新 `app/deployment.yaml` 文件中新 Docker 镜像的 `image` 路径。

```
image: YOUR_DOCKERHUB_USERNAME/selfhealing-app:v2.0.0
```

接下来，将更改推送到 GitOps 仓库。

```
# Commit the configuration change
git add .
git commit -m "Deploy version 2.0.0"
git push origin main
```

### **观察自动部署**

几分钟内，Argo CD 将：

1. 注意到 Git 存储库已更改。
2. 拉取新配置。
3. 更新正在运行的应用程序。
4. 在用户界面中显示“已同步”状态。

默认情况下，Argo CD 每三分钟检查一次更改。你可以调整此设置以使其检查更快（接近实时）或更慢（不那么频繁）。

访问 `http://localhost:3000` 查看你更新后的应用程序。

检查之前务必进行端口转发。

```
kubectl port-forward svc/selfhealing-app-service 3000:80 > /dev/null 2>&1 &
```

现在，你将看到更新后的用户界面。

[![Final app showing self-healed state with new version](https://cdn.thenewstack.io/media/2025/12/8c5a29df-image4-1024x855.png)](https://cdn.thenewstack.io/media/2025/12/8c5a29df-image4-1024x855.png)

*显示具有新版本的自我修复状态的最终应用程序。*

此屏幕表示你已完成 GitOps 设置。现在，你的应用程序将自动部署并在需要时自我修复。

## **理解自我修复的魔力**

以下是使自我修复成为可能的工作流程：

1. Argo CD 持续监控 Git 存储库。它还监控你的 Kubernetes 集群。
2. 它持续比较 Git 中定义的配置和实际的 Kubernetes 结构。
3. 如果发现差异，它会向 Kubernetes 发出信号，使其根据 Git 中的定义进行调整。

这就是自我修复过程。

[![Image showing GitOps workflow](https://cdn.thenewstack.io/media/2025/12/64bbc127-image5.png)](https://cdn.thenewstack.io/media/2025/12/64bbc127-image5.png)

*显示 GitOps 工作流程的图片。*

## **GitOps 是未来（也是现在）**

每次你推送到 Git，你的应用程序都会更新。当生产停止时，你的应用程序会自我修复。这不仅仅是部署自动化。这是一种自我修复的基础设施。它会自行处理，同时为你腾出时间来处理其他事情。这就是 GitOps 的力量。