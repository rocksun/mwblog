# The bug that led to SimKube 2.0
Some of you might have noticed (on my [newly-designed website](https://simkube.dev/)!) that SimKube is now at version 2.0—and actually, it has been for a few months at this point[1](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-1-157665317). I had made a [comment on lobste.rs](https://lobste.rs/s/usawel/debugging_memory_corruption_who_wrote_2#c_6huyba) a month or so ago that I wish more people talked about their debugging process, and SimKube 2.0 came about as the result of a sortof embarrassing bug, so I thought in this post I’d “be the change” and talk about the debugging process I went through for SimKube.

P.S. You can also find the “full” SimKube code [on GitHub](https://github.com/acrlabs/simkube), along with the [diff of changes](https://github.com/acrlabs/simkube/commit/7678afca8ecf43d944977cebc8c9861835ed5048) that we’re talking about today.

## But first, a message from our sponsors about versioning
If you’ve spent any time on the Internet, you’ll know that version numbering schemes are a hotly-debated topic; [SemVer](https://semver.org/) is the scheme that probably “most” people are familiar with, but there’s also [CalVer](https://calver.org/), used by such projects as Ubuntu, there’s “have a single number and make it go up sometimes” (aka, the Google Chrome versioning scheme), there’s the “use your Git SHA as a version number” crowd, and then there’s whatever the heck Google Cloud Platform is doing[2](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-2-157665317):

```
> gcloud version
Google Cloud SDK 511.0.0
alpha 2025.02.18
beta 2025.02.18
bq 2.1.13
bundled-python3-unix 3.12.8
core 2025.02.18
gcloud-crc32c 1.0.0
gke-gcloud-auth-plugin 0.5.9
gsutil 5.33
```
Part of the problem is that version numbers are used for a bunch of different audiences to communicate different things. Marketing folks want a version number that corresponds to a big new feature set or product release, whereas technical folks want a version number that communicates information about how much work they’re going to have to do to upgrade (i.e., did you make any breaking changes, did you fix some bugs, did you introduce new bugs, etc)[3](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-3-157665317).

Anyways I’m not here to start a flamewar about versioning schemes, I just want to put into context what SimKube 2.0 actually means. The SimKube project follows a “best-effort” semver scheme, which just means that “when the big number goes up, there was a breaking change that I knew about when I released it, and if one of the smaller numbers goes up, there might still be a breaking change, I just didn’t know about it at the time.” In other words—SimKube 2.0 is incompatible with SimKube 1.x, but it’s all still the same project. There wasn’t some big rewrite or whatever that happened[4](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-4-157665317). And, now that we’re over the “2.0” hump, future breaking changes will (hopefully) seem like less of a big deal. I guess we’ll see how that plays out in practice, but for now, let’s talk about the bug that inspired all this.

## Why aren’t these objects getting created?
OK so a quick recap: SimKube is split into multiple components; `sk-tracer`
collects “traces” of events that happen in a Kubernetes cluster, and `sk-driver`
replays the events from those traces in a simulated environment. I first found out about the bug in question when a user reported that not all of the events from their trace were getting replayed in their simulation. I went through all the standard debugging steps:

I tried it on my own setup and it seemed to work fine

[5](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-5-157665317).I got the logs from the user’s cluster, and went “Huh? This doesn’t make any sense and also there isn’t enough information to actually see what’s going on.”

[6](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-6-157665317)Set up a Zoom call with the user to watch it break, and I observed that it did, in fact, break. Still couldn’t figure out what was going on, even with the live debugging session.

Finally narrowed this down to “something weird happening on Google Cloud”, so while I was at KubeCon last year, I spun up ACRL’s first Google Cloud environment to try to reproduce it

[7](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-7-157665317).
I was, at this point, actually able to reproduce the issue, and it was at this point that I realized that Google Cloud had nothing at all to do with the problem, and that I could reproduce the problem locally just fine as well—I just hadn’t *realized* that I was reproducing it locally[8](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-8-157665317).

So what was the problem we were actually seeing? Well, the high-level version was that the user was reporting that not all the objects from their trace were getting created in their simulation environment. Specifically, the user was trying to track both Kubernetes Deployments and ServiceAccounts, and because I had some degree of foresight when I created the trace file format, I could see from their generated trace file that this wasn’t user error:

```
{
"trackedObjects": {
"v1.ServiceAccount": {
"podSpecTemplatePath": null
},
"apps/v1.Deployment": {
"podSpecTemplatePath": "/spec/template"
}
}
}
```
I could also see that the trace file did not store any actual ServiceAccount resources, which meant that the bug was in `sk-tracer`
somewhere. Looking at the user’s `sk-tracer`
logs, I saw a pattern like this at the very beginning of its initialization:

```
2024-11-12T16:59:08.711589Z INFO sk-store/src/trace_store.rs:171: microservices-demo/adservice - ObjectApplied @ 1731430748
2024-11-12T16:59:08.711867Z INFO sk-store/src/trace_store.rs:171: microservices-demo/cartservice - ObjectApplied @ 1731430748
2024-11-12T16:59:08.712140Z INFO sk-store/src/trace_store.rs:171: microservices-demo/checkoutservice - ObjectApplied @ 1731430748
...
2024-11-12T16:59:08.715746Z INFO sk-store/src/trace_store.rs:171: microservices-demo/frontend-external - ObjectDeleted @ 1731430748
2024-11-12T16:59:08.715841Z INFO sk-store/src/trace_store.rs:171: gmp-system/alertmanager - ObjectDeleted @ 1731430748
2024-11-12T16:59:08.715912Z INFO sk-store/src/trace_store.rs:171: default/kubernetes - ObjectDeleted @ 1731430748
```
These logs are recording the set of events that `sk-tracer`
is observing: as expected, we see a bunch of objects getting created in the first part of the logs, and then later (unexpectedly) a bunch of objects getting deleted.

As an aside, this is why I thought I was unable to reproduce the problem way back in step 1—in my environment, which I created from scratch every time, I did not see all of the `ObjectDeleted`
log lines. I *did* see some log lines that looked sorta like this:

```
2024-11-12T16:59:08.715912Z INFO sk-store/src/trace_store.rs:171: - ObjectDeleted @ 1731430748
```
As you can see, *some* objects were getting deleted, but there’s no name so I couldn’t tell which ones. I thought this was weird, but the events were sortof spurious (unlike the logs I got from the user) and I thought it was an unrelated bug.

But anyways, now that I knew that the problem was occurring in my own environment, and I knew *roughly* where to look, my next thought was to fire up a debugger and step through the code. Why was it deciding to delete some objects from the trace right when `sk-tracer`
started up? If I could just set a breakpoint and poke around, maybe I could figure out what was going on. Unfortunately for me, the state of debugging in Rust is, and I’m putting this as charitably as possible, *abysmal*. There are two different debugging backends for rust code, based off [gdb](https://sourceware.org/gdb/) and [lldb](https://lldb.llvm.org/). They both work slightly differently, but neither one of them work *well*. In short, these debuggers were written for and designed to work with C and C++ code, and have almost no understanding of Rust. Simple things like “how can you inspect the contents of this `Option`
?” require you to go manually dereference a bunch of addresses (sure do love typing `/x *(int*)0x12345678`
all the time), and perhaps even worse, they have zero understanding of [traits](https://doc.rust-lang.org/book/ch10-02-traits.html), which means you’re *severely* limited in the types of operations you can perform on an object[9](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-9-157665317).

So instead, I was back to print-line-based debugging. Well, based on the context of the user’s issue, one thing was clear: my log lines needed to print the *type* of the object that was getting deleted, not just the name. So I made [quick fix](https://github.com/acrlabs/simkube/commit/951eb7ecfd1c20eca9b5ea3ce63ec5bca306f91d) to update that, and now I got log lines that look like this:

```
2024-11-12T16:59:08.711589Z INFO sk-store/src/trace_store.rs:171: ObjectApplied @ 1739899948: apps/v1.Deployment microservices-demo/adservice
```
Once I got these log lines in place it became… slightly more clear what was happening: namely, all of the objects of one type were getting created, and then all of the objects of another type were getting created, and all of the objects of the first type were getting deleted. Now we’re getting somewhere! The problem is in this block of code (slightly simplified for clarity):

```
let mut apis = vec![];
for gvk in tracked_objects.keys() {
let stream = build_stream_for_tracked_obj(apiset, gvk).await?;
apis.push(stream);
}
let obj_stream = select_all(apis);
while let Some(res) = obj_stream.next().await {
let ts = clock.now_ts();
match res {
Ok(evt) => handle_obj_event(evt, ts),
Err(err) => {
skerr!(err, "watcher received error on stream");
},
}
}
```
Because `sk-tracer`
can be configured to watch arbitrary Kubernetes resource types, we’re using the dynamic API for this code; for each resource type (Deployments, ServiceAccounts, etc) that the user configures, we create a separate watcher stream that receives “events” for the [GVK](https://book.kubebuilder.io/cronjob-tutorial/gvks.html) corresponding to that object. And what’s an event? Well, it’s a set of Kubernetes objects that have been applied or deleted from the cluster; these are passed in from the [kube-rs runtime](https://github.com/kube-rs/kube)[10](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-10-157665317). The event itself doesn’t come with a timestamp[11](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-11-157665317), so instead we collect the timestamp we *receive* the event, and pass that (timestamp, event) pair off to `handle_obj_event`
. What does that function do?

```
fn handle_obj_event(&mut self, evt: Event<DynamicObject>, ts: i64) {
let mut store = self.store.lock().unwrap();
match evt {
Event::Applied(obj) => store.create_or_update_obj(&obj, ts),
Event::Deleted(obj) => store.delete_obj(&obj, ts),
Event::Restarted(objs) => store.update_all_objs(&objs, ts);
}
}
```
Seems pretty straightforward: if an object is created or modified, we get an `Applied`
event; if it’s deleted, we get a `Deleted`
event. And… what’s this `Restarted`
event? Well, it’s possible that the thing that watches for changes in the cluster gets restarted (or that `sk-tracer`
*itself* gets restarted), and in this case, we receive a list of all the objects that are currently in the cluster. But what happened if something got deleted in the intervening period? We have no way of knowing about it, so what SimKube does is keep track of all the objects we’ve ever seen, and then mark as “deleted” the ones that we didn’t get in the most recent update. This is one piece of the puzzle.

The second piece requires understanding how these streams are processed: we’re creating one stream for each object type, and then using `select_all`
to asynchronously handle updates *on a per object-type basis*. Which means that, when `sk-tracer`
first starts up, we *first* get an event that updates *all* of the ServiceAccount objects (for example), and *then* we get an event that updates *all* of the Deployment objects. BUT, crucially, none of the ServiceAccount objects are present in that second event, which means the tracking/delete logic kicks in and deletes all the ServiceAccounts that were just recorded. D’oh!

Getting to this point just required a bunch of staring at the code and trying to reason through things in my head until the lightbulb went on—asynchronous processing can have some surprising behaviour!

## So why a new major version?
Ok, so now we understand what the problem is, how do we fix it? The solution is to just make `sk-tracer`
track the object *type* (that it, its GVK) in addition to the name of the object; that way, when it gets a `Restarted`
event it can only apply the reconcile logic to objects *of that type*, not everything it’s ever seen.

Making this change required storing the object’s GVK in the trace alongside the object’s name. Now, I *could* have made it possible to do this while still supporting old versions of the trace file format, but in the time since I first developed the trace format, I realized that it wasn’t very extensible in a lot of ways, so I elected to use this bug as an opportunity to improve the extensibility of the format. And since I have very few users right now, I’m not actually that worried about breaking backwards compatibility at this point, so I elected to just do the thing[12](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-12-157665317). And, since I was releasing a new major version anyways, I took the opportunity to update all of my dependencies and make a couple other small breaking changes as well.

So anyways, this was my SimKube debugging story! No idea if anyone else found it interesting or not, but I always enjoy reading about how people solve problems, so hopefully you do too! Next time I’m going to talk about some of the new features that I’m really excited about in the new version.

As always, thanks for reading,

~drmorr

P.S. My goal has always been to get the paid-subscriber early drafts of posts out on Fridays at 1pm Pacific, but as I have more client work happening I haven’t been making that goal. I’m still trying to get things published early for my paid subscribers, but it might be at 10:00 at night sometimes :blobsweat:

Articles should still go out for everyone else on Monday at 11am Pacific.

[1](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-anchor-1-157665317)
I actually released v2.0 just after KubeCon, and was considering making a snarky announcement pillorying all the companies releasing new versions of their product at KubeCon, but… just never got around to it.

[2](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-anchor-2-157665317)
Seriously, Google, are you OK???

[3](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-anchor-3-157665317)
Note that I’m grossly oversimplifying here, there’s lots of other reasons why you want version numbers, and most people want multiple different things out of their version information.

[4](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-anchor-4-157665317)
Though I did consider trolling all the “rewrite-it-in-Rust” folks by announcing that I’d rewritten it in Golang.

[5](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-anchor-5-157665317)
Foreshadowing: it did not, in fact, “work fine”.

[6](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-anchor-6-157665317)
There is an incredibly fine art to writing log messages (and setting log levels) that aren’t overly verbose, but still communicate useful debugging information. I still don’t know how to do it very well.

[7](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-anchor-7-157665317)
If you know *anything at all* about how SimKube works, alarm bells should be going off at this point. SimKube doesn’t care what cloud provider it’s running on, or if it’s running on a cloud provider at all. This is like saying “Oh, my C++ program segfaulted, must be a bug in GCC.”

[8](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-anchor-8-157665317)
And just to be really clear, it took several weeks of back-and-forth to get to this point; these sorts of retrospectives can be misleading, because the sequence of steps “seems like” it didn’t take much time and the problem “should have been” obvious. But even for dumb mistakes like this one, understanding them can take *a lot of time*.

[9](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-anchor-9-157665317)
For example, if you want to see what the contents of a particular element of a `Vec`
object is in rust, you can either do this with square brackets (e.g., `v[5]`
) or by calling the `.get()`
method on the vector. The `.get()`
method returns an `Option`
in case you tried to get an out-of-bounds index, which means that even after calling `v.get()`
in your debugger, you’d have to play pointer games to actually see the contents, but in this case it doesn’t matter. Both `.get()`
and `[]`
are implemented as traits on `Vec`
, which means if you try to use them inside your debugger it just *DOES NOT WORK*. The debugger doesn’t know how to look up function calls for traits, so it just completely shits the bed. You’re out of luck, unless you want to go poking around the `Vec`
internals yourself. This kind of problem crops up all the time, because most things in Rust use traits, and it means that debugging your code is more-or-less impossible in this environment.

[10](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-anchor-10-157665317)
Also for anyone following along, this interface has changed in more recent versions of `kube-rs`
; the whole SimKube 2.0 release was significantly more work because I updated the version of `kube-rs`
I was using and had to rewrite a bunch of code to handle this change

[11](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-anchor-11-157665317)
Presumably because of the difficulties of handling time across a bunch of distributed nodes.

[12](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-anchor-12-157665317)
It also isn’t *that* hard to convert an individual trace file to the new format, so if you are one of my mysterious users and you run into a format issue, let me know and I can help you convert it!