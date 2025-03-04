# Boost Your CI/CD Pipeline: Automate Docker With GitHub Actions
![Featued image for: Boost Your CI/CD Pipeline: Automate Docker With GitHub Actions](https://cdn.thenewstack.io/media/2025/02/c974d68e-rose-galloway-green-mzpnzk3prtu-unsplash-1024x602.jpg)
In this guide, we will get deeper into automating Docker workflows with GitHub Actions — just clear steps that get you up and running. Automation is necessary with the rise of cloud-native development and the growing complexity of CI/CD pipelines. [GitHub Actions provides a seamless way to integrate Docker](https://thenewstack.io/dockerize-a-rust-application-with-aws-ecr-and-github-actions/) into your workflows, reducing manual effort and improving deployment speed.

Let’s get started!

## How To Set Up GitHub Actions for Docker
Let’s get straight into [setting up GitHub Actions](https://thenewstack.io/8-github-actions-for-setting-up-your-ci-cd-pipelines/). The first thing you need to do is create a workflow file. It’s a simple YAML file placed in .github/workflows/your repo.

Step 1: Create the Workflow File

- Go to your repo.
- Create a folder called
`.github`
if it doesn’t already exist. - Inside that, create a folder called
`workflows`
. - Create a file called
`docker.yml`
(or anything you like) in`.github/workflows/`
.
Here’s the basic structure of your docker.yml file:

12345678910111213141516171819202122232425 |
name: Docker Workflowon: push: branches: - mainjobs: build: runs-on: ubuntu-latest steps: - name: Check out code uses: actions/checkout@v2 - name: Set up Docker Buildx uses: docker/setup-buildx-action@v1 - name: Build Docker Image run: docker build -t myapp:${{ github.sha }} . - name: Push Docker Image run: | echo ${{ secrets.DOCKER_PASSWORD }} | docker login --username ${{ secrets.DOCKER_USERNAME }} --password-stdin docker push myapp:${{ github.sha }} |
The above YAML file automates the build. Further, it pushes your Docker image whenever changes are moved to the `main`
branch.
## Self-Hosted vs. GitHub-Hosted Runners
There are two options available for executing your workflow:

The GitHub-hosted runners are the default option. The setup is relatively maintenance-free and handy from your side.

With self-hosted runners, the user has complete control over the workflow execution machines. While this method provides increased flexibility, it requires ongoing maintenance.

GitHub-hosted runners will be the preferred solution for most users. Since they work best for Docker builds.

## Automating Docker Image Builds
Let’s say you’ve pushed some new code. Now, you want to automate building your Docker image. Here’s how you can do that.

### Step 2: Build the Docker Image Automatically
You’ll use the `docker build`
command in the [GitHub Actions workflow](https://thenewstack.io/the-missing-part-of-github-actions-workflows-monitoring/) file to build your Docker image automatically.

For example, inside your `docker.yml`
file:

12 |
- name: Build Docker image run: docker build -t myapp:${{ github.sha }} . |
The mentioned command will [create a Docker image](https://thenewstack.io/tutorial-create-a-docker-image-from-a-running-container/) and tag it with the commit `SHA (${{ github.sha }})`
. It makes sure each image is uniquely tagged with the commit ID.
### Step 3: Tagging Docker Images Dynamically
You’ll probably want to tag your images in a meaningful way. For example, by branch name and maybe with a version tag. You can do this with GitHub Actions variables:

12 |
- name: Build and tag Docker image run: docker build -t myapp:${{ github.sha }} -t myapp:${{ github.ref }} . |
In this example:
`${{ github.sha }}`
tags the image with a unique commit hash.`${{ github.ref }}`
tags it with the branch name (e.g., refs/heads/main).
It makes your images easy to track and identify.

## Pushing to Docker Hub or GHCR
Now that you’ve built the image, the next step is to push it to a container registry, such as [Docker Hub or GitHub Container](https://thenewstack.io/bypass-docker-hub-rate-limits-with-this-stateless-image-cache/) Registry (GHCR).

### Step 4: Set Up Secure Authentication
First, you’ll need to authenticate Docker to push the image. Since you don’t want to expose your credentials directly in the YAML file, GitHub Secrets is your friend here.

Go to your GitHub repo’s Settings > Secrets and add two secrets:

`DOCKER_USERNAME`
`DOCKER_PASSWORD`
Then, in your workflow file, you’ll use these secrets to log in to your Docker:

123 |
- name: Log in to Docker Hub run: | echo ${{ secrets.DOCKER_PASSWORD }} | docker login --username ${{ secrets.DOCKER_USERNAME }} --password-stdin |
### Step 5: Push the Image to Docker Hub or GHCR
Finally, after logging in, push your Docker image:

12 |
- name: Push Docker image to Docker Hub run: docker push myapp:${{ github.sha }} |
The YAML code pushes your image to Docker Hub. Moreover, you can swap this out for GHCR if that’s your choice.
## Multi-Arch Builds With QEMU and Buildx
Your existing workflow must support several machine architectures, such as ARM and x86. It allows prop-up [hardware operations ranging from Raspberry](https://thenewstack.io/the-new-2gb-raspberry-pi-5-another-option-for-linux-sysadmins/) Pi (ARM-based) devices to cloud-based servers (x86-based). At this phase, the combination of QEMU+Buildx [inside GitHub Actions](https://thenewstack.io/how-to-use-databases-inside-github-actions/) is handy.

### Step 6: Set Up Multi-Arch Builds
First, you must set up QEMU and Buildx in your workflow file.

Here’s what that looks like:

123456789 |
- name: Set up QEMU uses: docker/setup-qemu-action@v2- name: Set up Buildx uses: docker/setup-buildx-action@v1- name: Build multi-arch Docker image run: | docker buildx build --platform linux/amd64,linux/arm64 -t myapp:${{ github.sha }} . |
This will build images for both amd64 (standard desktop/server architecture) and arm64 (used by Raspberry Pi and some cloud servers).
## Security Improvements: Scanning Images for Vulnerabilities
[Security is always top](https://thenewstack.io/what-we-can-learn-from-the-top-cloud-security-breaches/) of mind. You don’t want to push images that have vulnerabilities.
### Step 7: Scan Docker Images for Vulnerabilities
You can integrate security tools like Trivy, and Snyk into your GitHub Actions to [scan your images during the build](https://thenewstack.io/3-best-practices-for-image-building-and-scanning/) process. Here’s an example using Trivy:

1234 |
- name: Scan Docker image for vulnerabilities run: | trivy image myapp:${{ github.sha }} if [ $? -ne 0 ]; then exit 1; fi |
If Trivy detects vulnerabilities, the build will fail. This ensures only secure images get pushed.
## Automating Deployments
You’ve built your Docker image and must now push it to the registry. Now, it’s time to deploy it.

### Step 8: Deploy to Kubernetes
Using GitHub Actions, you can easily [deploy your Docker image to a Kubernetes cluster](https://thenewstack.io/deploy-mongodb-in-a-container-access-it-outside-the-cluster/). Here’s is how;

123456 |
- name: Deploy to Kubernetes uses: appleboy/kubernetes-action@v0.1.0 with: kubeconfig: ${{ secrets.KUBECONFIG }} context: ${{ secrets.K8S_CONTEXT }} command: kubectl set image deployment/myapp myapp=myapp:${{ github.sha }} |
The action updates the Kubernetes deployment with the latest image tagged with `${{ github.sha }}`
.
## Summary
Automating your Docker workflows with [GitHub Actions can dramatically improve your development pipeline](https://thenewstack.io/make-a-scalable-ci-cd-pipeline-for-kubernetes-with-github-and-argo-cd/), reliability, and security. So you now have an automated pipeline with no manual intervention that builds Docker images, gets them pushed to a registry, scans them for known vulnerabilities, and deploys them to your environment.

The best part? You can do it all directly from GitHub with just a few lines of YAML with just a few lines of YAML. So, whether you’re pushing code, testing images, or deploying to prod, GitHub Actions has you covered.

So, are you ready to take the plunge? Begin automating your Docker workflows now! For a complete working demo, look at the GitHub repository.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)