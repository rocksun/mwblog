# How To Use the Docker exec Command
![Featued image for: How To Use the Docker exec Command](https://cdn.thenewstack.io/media/2023/09/d9bb1569-dock-1365387_1280-1-1024x682.jpg)
## What Is the exec Command?
The docker exec command allows users to run commands within an already[ deployed container](https://thenewstack.io/introduction-to-containers/).

### Two ways to use the exec Command:
- Inside the container: Run
*docker exec -it ID /bin/bash*(where ID is the first four characters of the running container’s ID) to access the container’s shell. - Outside the container: Use
*docker exec ID*COMMAND (where ID is the first four characters of the running container’s ID and COMMAND is the command to be run within the container).
### Prerequisites:
- A running instance of Docker on Ubuntu Server 22.04 (or newer)
- The official Docker GPG key added and installed
### Steps To Get Started With the Docker exec Command:
[Install Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)on Ubuntu Server by adding the GPG key, creating the necessary repository, and installing dependencies.- Create a test container with docker run
*–name docker-nginx -p 8080:80 -d nginx*. - Access the running container’s shell using docker
*exec -it ID /bin/bash*(where ID is the ID of the container).
### Using the Docker exec Command Efficiently:
- Run commands inside or outside containers without accessing its shell.
- Use the && operator to chain commands together.
- By following these steps, users can effectively use the docker exec command to manage their running Docker containers.
For those who are just getting started on your journey with Docker containers, there is much to learn. Beyond pulling images and deploying basic containers, one of the first things you’ll want to understand is the exec command.

Essentially, the exec command allows you to run commands within an already deployed container. The exec command allows you to do this in two different ways…from inside or outside the container. I’m going to show you how to do both. In the end, you’ll be better prepared to interact with your running Docker containers.

## What You’ll Need
You’ll only need a running instance of the Docker runtime engine installed on a supported platform. I’ll demonstrate this on Ubuntu Server 22.04.

In case you don’t have Docker installed, let’s take care of that first. If you already have Docker installed, go ahead and jump to the next section.

## Install Docker
Before you can install Docker on Ubuntu Server, you must first add the official Docker GPG key with the command:

1 |
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg |
You’ll be prompted for your sudo password.
Once the GPG key is successfully added, create the necessary Docker repository with the following command:

Install a few dependencies with this command:

1 |
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y |
Update apt with:
1 |
sudo apt-get update |
Install Docker with the command:
1 |
sudo apt-get install docker-ce docker-ce-cli containerd.io -y |
Next, you must add your user to the docker group with the command:
1 |
sudo usermod -aG docker $USER |
Log out and log back in so the changes take effect.
Congrats, Docker is now ready to go.

## Deploy a Test Container
To use the exec command, we first must deploy a simple test container. For that, we’ll use the tried-and-true NGINX and deploy a container with the command:

1 |
docker run --name docker-nginx -p 8080:80 -d nginx |
After running the command, Docker should report back the ID of the container. If you miss that, you can always view it with:
1 |
docker ps |
You’ll only need the first four characters of the ID.
## Access the Running Container’s Shell
Now, we can access the running container’s shell, which will allow you to run command from inside the container. This is done with the exec command like so:

1 |
docker exec -it ID /bin/bash |
Where ID is the first four characters of the running container’s ID. You should then find yourself at the running container’s bash prompt. Let’s say you want to upgrade the software. You can do so with the commands:
12 |
apt-get updateapt-get upgrade -y |
After the upgrade completes, you can exit the shell with the command:
1 |
exit |
Let’s simplify the process.
## Run a Command From Outside the Container
Thanks to the exec command, you don’t have to first access the container’s shell before running a command. Instead, you can send the command inside the container. Let’s stick with our example of updating and upgrading the running NGINX container. Again, we’ll need the container ID for this command.

To update and upgrade the software for our NGINX container (without first accessing the container), the command would be:

1 |
docker exec ID apt-get update && apt-get upgrade |
Where ID is the first four characters of the container ID.
The use of the && operator is common in Linux and makes it possible to daisy chain commands together such that they run one after another.

You can use this method to run just about any command. For example, you could view the index.html file used by NGINX with the command:

1 |
docker exec ID cat /usr/share/nginx/html/index.html |
Where ID is the first four characters of the container ID.
Let’s copy a new index.html file into the running container and then use exec to view it. Create the new file on your host with:

1 |
nano index.html |
In that file, paste the following contents:
Save and close the file. Next, copy the file to the running NGINX container with the command:

1 |
docker cp index.html ID:/usr/share/nginx/html/ |
Where ID is the ID of the running container.
Now, we can view the contents of the file with:

1 |
docker exec ID cat /usr/share/nginx/html/index.html |
The output should simply be:
1 |
Hello, New Stack |
And that’s how you use the Docker exec command. With this tool, you can better (and more efficiently) manage your running Docker containers.
## Common Errors With the Docker exec Command
Here are some common errors that may occur when using the docker exec command:

**Insufficient permissions:**The user running the docker exec command may not have sufficient permissions to execute containers or access their resources.**Incorrect container ID:**If you use an incorrect container ID, it can result in a failed execution of the command inside the container.**Command not found:**If you run a command that is not installed or available within the container, it will fail with a “command not found” error.**Container is stopped or exited:**Running the docker exec command on a stopped or exited container will result in an error.**Timeout errors:**If the execution of a command takes too long within the container, Docker may timeout and return an error.**Resource constraints:**A container with insufficient resources (memory, CPU) can cause docker exec to fail.**File system limitations:**When running commands that write to files outside the container’s file system or modify sensitive data, limitations such as privileges and space can lead to errors or issues with Docker.**Network connectivity issues:**If the container is not properly connected to a network interface or has limited network access, docker exec may fail.
## FAQ
### Q: What is the purpose of the exec command?
A: The exec command allows you to run commands within an already deployed container, so you can interact with your running containers.

### Q: Can I use the exec command without creating a new container?
A: No, by default, the *docker exec* command requires a running container. If you want to execute a command outside of the existing container’s shell, you need to create an interactive session using *docker exec -it ID /bin/bash.*

### Q: What is the format for specifying a container ID in the Docker exec command?
A: The first four characters of the container ID (e.g., “1234”) can be used as part of the command.

### Q: Can I use the exec command to update dependencies within an existing container?
A: Yes, you can run commands like *apt-get update && apt-get upgrade* inside a running container using *docker exec*.

### Q: How do I view output from a Docker exec command?
A: The output of the executed command is displayed in your terminal. If you want to capture the output for further processing or logging, use redirection operators (e.g., >, >>) as needed.

### Q: Can I chain multiple commands together using the exec command?
A: Yes, by default, Docker executes each command sequentially. To execute a series of commands one after another without waiting for input from the shell, use the && operator between them (e.g., *apt-get update && apt-get upgrade -y*).

### Q: What happens if I run a failed command inside an existing container?
A: If you run a command that fails within an existing container, Docker exits and terminates your interactive session. To avoid this, use the -n option with *docker exec*, which prevents Docker from waiting for input (e.g., *docker exec -it ID /bin/bash -n apt-get update && *…).

### Q: Can I pipe data between containers using the exec command?
A: No, by default, Docker does not support piping or redirecting output/input within a container. To achieve this functionality, use tools like *docker run –rm -it <image> /bin/bash*, which creates an isolated environment with no persistent file system.

### Q: How do I exit the interactive session started by the exec command?
A: You can exit the interactive session using the *exit* command or by closing your terminal.

## Troubleshooting Tips:
- If Docker fails to detect a running container, check that it is indeed alive and active.
- Ensure that you have sufficient permissions to access and manage containers.
- Verify that the image used within the container is valid and exists in your local cache.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)