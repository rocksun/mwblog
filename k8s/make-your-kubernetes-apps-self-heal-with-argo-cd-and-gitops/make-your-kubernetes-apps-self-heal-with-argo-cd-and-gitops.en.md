Kubernetes applications in production traditionally require manual work and time.

GitOps with [Argo CD solves this](https://thenewstack.io/why-argo-cd-is-the-lifeline-of-gitops/). It keeps your cluster in sync with git, where your repository defines the desired state. [Argo CD](https://thenewstack.io/survey-argocd-leaves-flux-and-other-gitops-platforms-behind/) makes sure the cluster always matches it, and when something falters, it fixes itself automatically. With GitOps, your applications become self-healing and always stay in sync with git.

## **What Is GitOps and Self-Healing?**

[GitOps](https://thenewstack.io/gitops-in-the-real-world-barriers-and-best-practices/) means your git repository is the single source of truth for everything. When [reality doesn’t match git](https://thenewstack.io/i-need-to-talk-to-you-about-kubernetes-gitops/), the system automatically fixes itself.

Your app’s configurations are stored in git, and any changes to either your app or the git source code will automatically be fixed. This is GitOps at its finest and most simple opportunity to accelerate the traditional deployment process.

### Rejuvenating Traditional Deployment

When you follow the traditional deployment process, there are many scenarios where things might take an unexpected turn:

* Someone can manually change the production settings, and your production might halt.
* A technical misstep on the server can pause production, then you have to manually restart it.
* Your app configuration changes, and you have to keep track of what was changed.

GitOps handles all these possibilities effectively and with simplicity.

### GitOps Self-Healing Solution

With GitOps, you can maintain the current state of your application in a git repository. GitOps tech like Argo CD ensures that whatever is defined in your git matches the actual app deployment.

If there are technical hiccups on the server, GitOps will automatically resolve them and restore your app to the defined state. This is known as self-healing in GitOps.

On top of that, you also keep an audit trail of all the changes made in git.

## **Step 0: Prerequisites**

* Docker is installed on your system.
* My go-to: WSL2 with Ubuntu. Feel free to use your own Linux setup.
* GitHub account.
* Docker Hub account.
* My go-to: React project (You can use any project).
* Knowledge of Kubernetes (optional).

## **Step 1: Install and Start Minikube**

First, set up a Kubernetes cluster. For this tutorial, we will use Minikube. It’s lightweight and ideal for learning.

(You can skip this step if you already have a cluster running locally.)

### **Install Minikube**

Run the commands below to install Minikube:

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

### **Start Minikube Cluster**

Before running the command below, make sure Docker is running.

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

## Step 2: Create Your React App

```
# Create the app
cd ~/projects
npx create-react-app my-selfhealing-app
cd my-selfhealing-app
```

### **Update the App for Demo**

Replace `src/app.js`:

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

Note: This code should work fine. You can also use Vite or any other framework, since CRA is deprecated.

### **Create Dockerfile**

A Dockerfile is used to write the Docker codebase.

Create `Dockerfile`:

Make sure to put this file in the root of the project. Paste the code below into it.

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

Here, we are first installing the node, then creating a build, then following instructions on running the application on port 80.

### **Push to GitHub**

Once all your code is ready, push it to GitHub.

```
git init
git add .
git commit -m "Initial self-healing app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/my-selfhealing-app.git
git push -u origin main
```

## **Step 3: Build and Push Docker Image**

Now that the code is ready, create a Docker image and push it to Docker Hub.

If you don’t have a Docker Hub account, you can sign up and create one from the [Docker Hub](https://hub.docker.com/) page.

Also, make sure Docker is running locally. If you don’t have Docker installed locally, you can install [Docker Desktop](https://www.docker.com/products/docker-desktop/).

```
# Build the image
docker build -t YOUR_DOCKERHUB_USERNAME/selfhealing-app:v1.0.0 .

# Push to DockerHub
docker login
docker push YOUR_DOCKERHUB_USERNAME/selfhealing-app:v1.0.0
```

## **Step 4: Create GitOps Configuration Repository**

To get started with GitOps, create a new git repository. This is important because it’s possible to have separate repositories for source code and GitOps.

```
# Build the image
docker build -t YOUR_DOCKERHUB_USERNAME/selfhealing-app:v1.0.0 .

# Push to DockerHub
docker login
docker push YOUR_DOCKERHUB_USERNAME/selfhealing-app:v1.0.0
```

### **Create Kubernetes Manifests**

First, create a new folder called “app.” Inside this folder, create Kubernetes-related files.

Create `app/deployment.yaml`:

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

This is a regular Kubernetes deployment file with basic details. Make sure to update the image with your Docker image.

Next, create another file for the Kubernetes service.

Create `app/service.yaml`:

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

### **Commit GitOps Configuration**

Once all the files are created, push the changes to GitHub.

```
git add .
git commit -m "Add GitOps configuration for self-healing app"
git push origin main
```

## **Step 5: Install Argo CD**

Next, install the tool that makes self-healing possible.

```
# Create Argo CD namespace
kubectl create namespace Argo CD

# Install Argo CD
kubectl apply -n Argo CD -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Wait for it to be ready (takes 2-3 minutes)
echo "Installing Argo CD... this takes a few minutes"
kubectl wait --for=condition=available --timeout=300s deployment/Argo CD-server -n Argo CD
```

### **Access Argo CD**

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

Now Argo CD will run on port 8080. Open this URL in your browser: <https://localhost:8080>.

You would see a login screen like this:

[![AgroCD login screen](https://cdn.thenewstack.io/media/2025/12/681d53eb-image7-1024x479.png)](https://cdn.thenewstack.io/media/2025/12/681d53eb-image7-1024x479.png)

AgroCD login screen.

You can use the username “admin” and the password that you have just generated using the above command. Once the login is done, it’s time to create an application inside Argo CD.

## Step 6: Create Self-Healing Application

Tell Argo CD to manage your app and enable self-healing.

### **Create Argo CD Application**

Create `selfhealing-application.yaml`:

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

Apply it:

```
# Update the repoURL first, then:
kubectl apply -f selfhealing-application.yaml

# This will give the result below
# application.argoproj.io/selfhealing-app configured
```

Once this is done, you should see your application in your Argo CD dashboard.

[![Argo CD UI showing that it  is running locally](https://cdn.thenewstack.io/media/2025/12/524f4f6a-image2.png)](https://cdn.thenewstack.io/media/2025/12/524f4f6a-image2.png)

Argo CD UI showing that it is running locally.

## **Step 7: Access Your Self-Healing App**

```
# Check pods are running
kubectl get pods -l app=selfhealing-app
```

It should show something like this:

[![Output showing that pods are running](https://cdn.thenewstack.io/media/2025/12/4a9ca882-image1-1024x96.png)](https://cdn.thenewstack.io/media/2025/12/4a9ca882-image1-1024x96.png)

Output showing that pods are running.

```
# Access your app using port-forward
kubectl port-forward svc/selfhealing-app-service 3000:80 > /dev/null 2>&1 &
```

Visit

`http://localhost:3000`

to see your app running.

[![Initial app with first version](https://cdn.thenewstack.io/media/2025/12/6a37ca07-image6-1024x660.png)](https://cdn.thenewstack.io/media/2025/12/6a37ca07-image6-1024x660.png)

Initial app with first version.

## **Step 8: Test Self-Healing**

It’s time to test the changes and see the self-healing process in action.

### **Deleting a Pod**

Start by simply deleting a pod.

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

This is basic Kubernetes behavior, but now let’s see Argo CD’s self-healing …

### **Delete the Entire Deployment**

Now, go one step further by deleting everything.

```
# The ultimate test - delete everything!
kubectl delete deployment selfhealing-app
kubectl delete service selfhealing-app-service

# Watch Argo CD recreate everything automatically
kubectl get all -l app=selfhealing-app -w
```

[![Argo CD app status, showing sync time and other details](https://cdn.thenewstack.io/media/2025/12/14466621-image3.png)](https://cdn.thenewstack.io/media/2025/12/14466621-image3.png)

Argo CD app status, showing sync time and other details.

The Argo CD dashboard will show sync time as “a few seconds ago.” This shows that it has already synced and created the application again. In other words, Argo CD ensures reality always matches git.

## **Step 9: Making Real Updates (The GitOps Way)**

Now, make a legitimate change to see how GitOps handles updates.

### **Update Your App**

Edit `src/App.js` and change:

```
<p>🏷️ Version: 2.0.0 - Updated via GitOps!</p>
```

This update reflects a new version of the app. A simple change.

### **Build and Push New Version**

Now, create a new Docker build and push it to the Docker Hub. Also, push the source code to GitHub.

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

### **Update GitOps Configuration**

Next, open the GitOps repository and use the update app/deployment.yaml file, updating the image path in the app/deployment.yaml file for the new Docker image.

```
image: YOUR_DOCKERHUB_USERNAME/selfhealing-app:v2.0.0
```

Next, push changes to the GitOps repo.

```
# Commit the configuration change
git add .
git commit -m "Deploy version 2.0.0"
git push origin main
```

### **Watch Automatic Deployment**

Within minutes, Argo CD will:

1. Notice the git repository changed.
2. Pull the new configuration.
3. Update the running application.
4. Show “Synced” status in the UI.

By default, Argo CD checks for changes every three minutes. You can adjust this to make it check faster (near real time) or slower (less frequent).

Visit `http://localhost:3000` to see your updated app.

Make sure to do port forwarding before checking.

```
kubectl port-forward svc/selfhealing-app-service 3000:80 > /dev/null 2>&1 &
```

Now, you will see the updated UI.

[![Final app showing self-healed state with new version](https://cdn.thenewstack.io/media/2025/12/8c5a29df-image4-1024x855.png)](https://cdn.thenewstack.io/media/2025/12/8c5a29df-image4-1024x855.png)

Final app showing self-healed state with new version.

This screen means you have completed the GitOps setup. Now your apps will automatically be deployed and heal themselves whenever needed.

## **Understanding the Self-Healing Magic**

Here’s the workflow that makes self-healing possible:

1. Argo CD keeps watching the git repository. It also watches your Kubernetes cluster.
2. It continuously compares the configuration defined in git and the actual Kubernetes structure.
3. If it finds a difference, it signals Kubernetes to adjust as defined in git.

This is the self-healing process.

[![Image showing GitOps workflow](https://cdn.thenewstack.io/media/2025/12/64bbc127-image5.png)](https://cdn.thenewstack.io/media/2025/12/64bbc127-image5.png)

Image showing GitOps workflow.

## **GitOps Is the Future (And Present)**

Every time you push to git, your app updates. When production stops, your app heals itself. This is more than deployment automation. It is a self-healing infrastructure. It takes care of itself while giving you back time to work on other things. That’s the power of GitOps.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/10/6698ac9e-cropped-4739937e-vinod-pal.jpg)

Vinod Pal is a full-stack developer and a member of the Andela network, a private global talent marketplace. With an eight-year track record of building end-to-end products, he specializes in .NET, NodeJs, React and Angular. He has developed microservices using...](https://thenewstack.io/author/vinod-pal/)