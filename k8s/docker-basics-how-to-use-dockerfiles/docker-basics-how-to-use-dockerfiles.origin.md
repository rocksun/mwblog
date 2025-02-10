# Docker Basics: How to Use Dockerfiles
![Featued image for: Docker Basics: How to Use Dockerfiles](https://cdn.thenewstack.io/media/2019/06/76845160-child-1864718_640.jpg)
[Esi Grünhagen](https://pixabay.com/users/FeeLoona-694250/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1864718)from
[Pixabay](https://pixabay.com/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1864718).
## Understanding Dockerfiles: Construction and Application
A Dockerfile is a script that automates the creation of Docker images, essential for building containers. Key sections include specifying a base image (FROM), executing commands (RUN), copying files (COPY), exposing ports, and setting environment variables. Utilizing Dockerfiles enhances efficiency, reusability, and standardization in image creation.

To construct a Dockerfile, create a directory and define specific keywords like FROM, RUN, and MAINTAINER. For example, a basic Dockerfile for updating an Ubuntu image involves commands for updating packages and installing build-essential.

After creating the Dockerfile, build the image using the command *docker build -t “NAME:Dockerfile,”* (where NAME is the name you want to use). This process enables the management of multiple variations of containers efficiently, simplifying deployment from a single image.

## Overview
A Dockerfile is a text file that contains instructions for building and configuring an image in Docker. It’s used to automate the process of creating a container from scratch, using various layers to build up the final image. Dockerfiles typically contain the following sections:

**From**: This line specifies the base image that your new image will be built on top of.**Run or Command**: These lines run commands during the build process, such as installing dependencies or setting environment variables.**Copy**: This instruction copies files from the current directory into the container at a specific location.**Exposed port**: This line specifies which ports will be exposed when the image is created and run in containers.**Environment variables**: These lines set environment variables for your application to use.
Using Dockerfiles has several benefits, including efficient image creation, reusability, portability, standardization, a faster build process, and better testing.

In this article, you’ll learn the basics of a Dockerfile, how to construct a Dockerfile, how to build a Docker image from a Dockerfile, and how to deploy containers using a Dockerfile.

By using a [Docker](https://www.docker.com/?utm_content=inline+mention) image, it is not only possible to deploy one container after another, it’s quite easy. Once you’ve pulled the image from a registry (such as [Docker Hub](https://hub.docker.com/)), each container can then be deployed with a single [ docker command](https://thenewstack.io/how-to-use-the-docker-exec-command/). But what happens when you find yourself having to deploy numerous containers (each for a different purpose) from the same image? All of a sudden, the

[management of those containers](https://thenewstack.io/deploy-portainer-for-easier-container-management/)can get a bit cumbersome.
Say, for example, you pull down the latest [Ubuntu image](https://thenewstack.io/an-introduction-to-ubuntus-uncomplicated-firewall/) for development. Before you can develop with that container, there are a number of modifications you want to make to the image (such as upgrading [software and adding the necessary development packages for the job](https://thenewstack.io/surprise-software-testing-is-every-developers-job-now/) at hand).

For this, you could manually edit each image as needed (creating a new image for each necessary variation on the theme), or you could construct a Dockerfile for each variation. Once you have your Dockerfile basics constructed, you can quickly [build the same image](https://thenewstack.io/3-best-practices-for-image-building-and-scanning/) over and over, without having to take the time to do it manually. Carefully crafted Dockerfiles can save you considerable time and effort.

I want to walk you through the process of how to use Dockerfile. I will demonstrate by using the latest Ubuntu image, updating and upgrading that image, and then installing the build-essential package. This will be a fairly basic Dockerfile, but one you can easily build upon.

**Dockerfile Basics**
Before we construct our Dockerfile, you need to understand what makes up the file. This will be a text file, named Dockerfile, that includes specific keywords that dictate how to build a specific image. The specific keywords you can use in a file are:

**ADD**copies the files from a source on the host into the container’s filesystem at the set destination.**CMD**can be used for executing a specific command within the container.**ENTRYPOINT**sets a default application to be used every time a container is created with the image.**ENV**sets environment variables.**EXPOSE**associates a specific port to enable networking between the container and the outside world.**FROM**defines the base image used to start the build process.**MAINTAINER**defines the full name and email address of the image creator.**RUN**is the central executing directive for Dockerfiles, also known as the run Dockerfile command.**USER**sets the UID (or username) which is to run the container.**VOLUME**is used to enable access from the container to a directory on the host machine.**WORKDIR**sets the path where the command, defined with CMD, is to be executed.**LABEL**allows you to add a label to your docker image.
Not all keywords are required for a Dockerfile to function. Case in point, our example will only make use of FROM, MAINTAINER, and RUN.

**Constructing the Dockerfile**
Before we create the basic Dockerfile, we need to make a new directory from which to work. We’ll create the **dockerbuild **directory with the command:

1 |
mkdir ~/dockerbuild |
Change into that newly created directory with the command:
1 |
cd ~/dockerbuild |
Now, we’ll craft our Dockerfile. Create the new file with the command:
1 |
nano Dockerfile |
Within that file, paste the following to run a Dockerfile:
123456789 |
FROM ubuntu:latestMAINTAINER NAME EMAILRUN apt-get -y updateRUN apt-get -y upgradeRUN apt-get install -y build-essential |
NAME is your full name, and EMAIL is your email address.
Save and close that file.

**Building Your Docker Image**
With the basic Dockerfile complete, you can now build the image from that file. Issue the command (from within the *~/dockerbuild* directory):

1 |
docker build -t "NAME:Dockerfile" . |
Where NAME is the name of the new image to be created, it’s important to note that NAME must be all lower case, otherwise, the build will fail.
For example, say you want to create images for web development, app development, and security development. You could issue the following commands:

12345 |
docker build -t "appdev:Dockerfile" .docker build -t "webdev:Dockerfile" .docker build -t "secdev:Dockerfile" . |
This will begin the process of downloading the ubuntu:latest image and building the image according to the Dockerfile (**Figure 1**):
![](https://cdn.thenewstack.io/media/2024/02/847f61a1-dockerfiles-1.jpg)
Figure 1: The image has been built.

Once the build(s) are complete, issue the command:

1 |
docker images |
You should see all of the newly build images, now available for use (**Figure 2**):
![](https://cdn.thenewstack.io/media/2024/02/e8247536-dockerfile-02.jpg)
Figure 2: Newly created images ready to be deployed.

**How to Run Dockerfile for Rocky Linux**
Let’s say you want to create an image using [Rocky Linux](https://thenewstack.io/start-developing-with-rocky-linux-as-a-docker-container/) that updates the pulled Rocky Linux image and installs a web server. For this, we’d first create a new directory with the command:

1 |
mkdir ~/rockylinux |
Change into that directory with the command:
1 |
cd ~/rockylinux |
Create the new Dockerfile with the command:
1 |
nano Dockerfile |
Paste the following contents into that file for the Dockerfile run command:
123456789 |
FROM rockylinux:9MAINTAINER NAME EMAILRUN dnf makecacheRUN dnf upgrade -yRUN dnf install -y httpd |
Where NAME is your name and EMAIL is your email address.
Save and close the file. Build the image with the command:

1 |
docker build -t “webdev_rockylinux:Dockerfile” . |
Depending on how much upgrading is necessary, this particular build will take a bit longer than the Ubuntu image. Once the build completes, issue the command *docker images* to see that your newly built (CentOS-based) image is ready (**Figure 3**):
![](https://cdn.thenewstack.io/media/2024/02/65fe0164-dockerfile-3.jpg)
Figure 3: The Rocky Linux image is available for deployment.

**Docker Image Building Made Easy**
And that’s all there is to building Docker images with Dockerfiles. This is a much more efficient and standard method for creating new images than is committing changes to a pulled image. Once you are proficient in how to use Dockerfiles, there’s no limit to the types of images you can create.

*(Editor’s note: This post has been updated. It originally ran June 19, 2019).*
**FAQ: Using Dockerfiles**
**1. What is a Dockerfile?**
A Dockerfile is a text file that contains a series of instructions on how to build a Docker image. It defines the environment and the application that will run inside a container.

**2. What are the basic commands used in a Dockerfile?**
Here are some essential commands you might encounter:

**FROM**: Specifies the base image to use for the new image.**RUN**: Executes commands in a new layer on top of the current image and commits the results.**COPY**: Copies files or directories from the host filesystem into the image.**CMD**: Provides defaults for an executing container, such as the command to run.**ENTRYPOINT**: Configures a container to run as an executable.
**3. How do I build an image from a Dockerfile?**
To build an image, navigate to the directory containing your Dockerfile and run the following command in your terminal:

*docker build -t your-image-name .*
**4. What is the difference between CMD and ENTRYPOINT?**
- CMD: Sets default commands and/or parameters for the container. It can be overridden when running the container.
- ENTRYPOINT: Configures the container to run as an executable. It is not overridden by command line arguments.
**5. How can I optimize my Dockerfile?**
To optimize your Dockerfile, consider the following tips:

- Minimize the number of layers: Combine commands where possible using
*&&*. - Order your commands wisely: Place commands that change less frequently at the top to take advantage of caching.
- Use
*.dockerignore*: Exclude files and directories that are not needed in the image to reduce size.
**6. What is a multi-stage build?**
A multi-stage build allows you to use multiple *FROM* statements in your Dockerfile, which is useful for separating the build environment from the runtime environment to help significantly reduce the final image size.

**7. How do I run a container from my image?**
### Once your image is built, you can run a container using:
*docker run -d IMAGE*
Where IMAGE is the name of the image to be used.

**8. Where can I find more information about Dockerfiles?**
For more detailed information, you can refer to the [official Docker documentation](https://docs.docker.com/reference/dockerfile/), which provides extensive resources on Dockerfiles and their usage.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)