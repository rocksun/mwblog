Member-only story

Your container might be running… but completely unresponsive.
Kubernetes probes help you detect that and take action.
In this post, I’ll show you **how to use liveness, readiness, and startup probes** the right way with **real YAML, diagram, and use cases**.

# What Are Probes in Kubernetes?
Probes are how Kubernetes checks if your containers are **alive** and **ready** to serve traffic.

They help Kubernetes:

- Know if a container needs to be
**restarted**(if it’s unhealthy). - Know if a container is
**ready to receive traffic**.
# Three Types of Probes
# 1. Liveness Probe
Checks if the container is **alive** (i.e., not stuck, unresponsive).

- If the probe fails, Kubernetes
**restarts the container**. - Useful for apps that might get into a
**deadlock**or stuck state.
# 2. Readiness Probe
Checks if the container is **ready to accept traffic**.

- If it fails,
**traffic is not sent**to the container. - Very useful when your app takes time to initialize or depend on something external.
# 3. Startup Probe
Used to delay **liveness + readiness** checks until the app has **fully started**.

- Prevents false failures when app takes longer to start.
- Once successful, other probes kick in.
# Probe Mechanisms (How They Work)
# a. Exec Probes
- Runs a
**command inside the container**. - If exit code =
`0`
, success; else failure.
**Example**:
`livenessProbe:`
exec:
command:
- cat
- /tmp/healthy
initialDelaySeconds: 5
periodSeconds: 5
# b. HTTP Probes
- Makes an
**HTTP GET**request to a specific path/port. - If it returns
`2xx`
or`3xx`
status code → success.