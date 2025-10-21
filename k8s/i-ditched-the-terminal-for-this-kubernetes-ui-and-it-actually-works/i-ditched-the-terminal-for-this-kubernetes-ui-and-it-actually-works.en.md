## Why I picked Headlamp over kubectl and Lens

Let’s be honest: most of us live in the terminal. `kubectl get pods` is basically muscle memory at this point. And sure, for some things, nothing beats the CLI. But when you’re juggling multiple clusters, inspecting RBAC, checking logs, editing YAMLs, and explaining what the hell is going on to someone on Zoom—you start wishing for a UI that doesn’t suck.

That’s where **Headlamp** slots in better than I expected.

## kubectl: power but pain

* Great for scripts and quick commands
* Terrible for multi-cluster workflows
* Doesn’t give you visibility unless you already know what you’re looking for
* You’re just one typo away from nuking prod

## Lens: powerful but bloated

* Lens is solid, no doubt
* But it’s **Electron-heavy**, slow to start, and a bit too “IDE-feeling” for my taste
* Multi-cluster? Yes but you have to manage contexts manually and pray your kubeconfig is clean
* Some features are locked behind their cloud login now yeah, no thanks

## Headlamp: just enough UI, none of the BS

* Starts instantly, runs in browser or desktop
* Reads your kubeconfig, supports **multiple clusters without context switching hacks**
* Doesn’t try to be VSCode-for-Kubernetes
* Feels like a UI built *by* devs, not for marketing screenshots

It doesn’t replace `kubectl`and it’s not trying to. Instead, Headlamp gives you an easier way to navigate clusters when precision matters and time is short. Especially if you’re in a team and can’t assume everyone’s a CLI wizard.

I still script with `kubectl`, but for exploration, debugging, and real-time ops? Headlamp just... works.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*wdEy1IMRigr68UZXcT7B4w.png)

## Features that made me stay

Headlamp didn’t just win me over with a clean UI. It stuck because it solved actual pain points without trying to do too much. Here are the standout features that made me keep it installed across all my machines (and clusters).

## Multi-cluster support (done right)

Most tools say they support multi-cluster. What they *really* mean is: “You can switch kubeconfig contexts manually and hope it works.”

Headlamp actually means it.

You can load **multiple clusters** into the UI at the same time. It pulls from your kubeconfig, and each cluster shows up in a sidebar for easy toggling. You can view workloads across clusters without having to reauth or juggle env variables. It even color-codes them simple, but kind of a lifesaver.

## Get Devlink Tips’s stories in your inbox

Join Medium for free to get updates from this writer.

**Image idea:** A screenshot of Headlamp’s multi-cluster sidebar showing two or more clusters, ideally with different namespaces selected.

## RBAC-aware UI

You know that moment when a junior engineer asks, “Why can’t I see the pods?” and you realize their role doesn’t have permission — but there’s no way for them to know?

Headlamp **respects Kubernetes RBAC**, so if a user logs in with restricted permissions, the UI shows only what they’re allowed to see. No weird errors, no forbidden screens. It’s subtle, but it keeps things sane in real-world teams.

## Plugins that actually feel native

Unlike other dashboards that bolt on plugins as a marketing checkbox, Headlamp has a **real plugin architecture** using React and TypeScript.

Want to add a custom visualization for your CRDs? Go for it. Need to surface metrics from Prometheus or something custom in your stack? You can extend the UI without patching core code.

I built a basic plugin to surface logs from a sidecar container with some extra parsing and it felt like writing a mini React app, not hacking some brittle YAML.

[**Plugin docs here**](https://github.com/headlamp-k8s/headlamp/blob/main/docs/extensions.md)

## Live resource watching

You don’t need to hit “refresh” every 5 seconds like it’s 2004. Headlamp supports **real-time updates** on deployments, pods, events, logs — you name it. Watching a rollout or a crashing pod in real time is actually… enjoyable?

Also, the YAML editor supports inline editing, and changes are validated before you apply. Way less nerve-wracking than doing a live `kubectl edit` on something fragile.

**Image idea:** Live resource page showing a pod crashlooping or restarting, with real-time updates.

## Terminal built-in

If you *really* want to drop into a terminal, Headlamp includes one. You can open a shell into your pods directly from the interface no separate tabs, no typing out long pod names. It’s not as powerful as `k9s`, but for quick inspection or copy-pasting commands from docs, it’s super handy.

This is where the tool quietly flexes. It’s not trying to out-feature Lens or replace the terminal it’s focused, extendable, and fast.