[Podman 5.0 is out](https://github.com/containers/podman/releases/tag/v5.0.0), and with this also comes several breaking changes, but there is no reason to fear them; unless you are using podman machine, chances are you will not even notice them.
# Podman Machine
The biggest breaking change is a major refactor for the podman machine config files. There is no migration from the old to the new format. On MacOS, support for the qemu provider has also been removed in favor of the more performant Apple hypervisor. For more details on the machine changes, see
[this post](https://blog.podman.io/2024/03/migration-of-podman-4-to-podman-5-machines/) from Brent Baude.
# CNI removal
With Podman 4.0, we introduced our new networking backend, netavark, to configure container networking, and since then, we defaulted to netavark over CNI. However, users that updated from 3.X and older were not migrated to netavark and thus they kept using CNI. With 5.0 we will only support netavark going forward due to the increased support burden of trying to work with two tools. CNI support is still guarded behind a build tag (
cni) and will be enabled on distributions where we still need it, such as RHEL 9 and FreeBSD, but do not expect any help from upstream maintainers in case of issues with the CNI integration.
Users can check what backend they use with the
podman info --format {{.Host.NetworkBackend}} command, it will either print netavark or cni. If it is netavark, you do not need to worry about anything. Everything will keep working like it did before. For cni, manual intervention may be required. If you do not care about your containers you can run podman system reset which deletes everything. Otherwise check with
podman network ls if you have any custom network defined. If not, then the update should not cause many issues, although a reboot is highly recommended to prevent any old temporary network interfaces/firewall rules from interfering with netavark. In case you do have custom networks, they all will be lost on the upgrade, so a manual migration will be needed.
Assuming the networks were only created via
podman network create, then one way to migrate is to save all your old cni configs in the new netavark format by using this one liner:
for name in $(podman network ls -q); do podman network inspect --format "{{json .}}" "$name" > "$name.json"; done
This command must be executed while still using Podman 4.*. It will create a bunch of .json files in your current directory, once you updated to Podman 5.0 you simply move the files to the network cofig dir. The default as root would be
/etc/containers/networks/ and as rootless
~/.local/share/containers/storage/networks/. Then confirm that
podman network ls shows the networks. Alternatively you could just recreate the networks with the
podman network create command.
# Cgroups v1 deprecation
The support for systems with cgroups v1 is deprecated and will be removed in a future release. Please migrate to cgroups v2. Most distributions have already done so we do not expect many users to be affected by this. On cgroups v1 systems a warning will be printed for each podman command. To turn off the warning set the
PODMAN_IGNORE_CGROUPSV1_WARNING environment variable.
# Pasta default for rootless networking
The default rootless networking tool has been switched from
[slirp4netns](https://github.com/rootless-containers/slirp4netns) to [pasta](https://passt.top/passt/about/#pasta-pack-a-subtle-tap-abstraction). It should offer better performance and more features. As such you need to make sure you have pasta installed (part of the passt package) if you use rootless containers with networking. While I do not think it is necessarily a breaking change for many, it could be to some users. Rootless containers created with the default network option on 4.X will continue use slirp4netns as networking tool even after the upgrade as the network mode is set when the container was created so if you want to keep your older containers working you need to make sure slirp4netns is still installed after the upgrade in this case.
Pasta by default performs no Network Address Translation (NAT) and copies the ip addresses from your main interface into the container namespace. For that, pasta will pick your interface with a default route. If pasta cannot find an interface with the default route, it will select an interface if there is only one interface with a valid route. If you do not have a default route and several interfaces have defined routes, pasta will be unable to figure out the correct interface and it will fail to start. In this case the user would need to specify the interface to use with the -i option to pasta, because Podman launches pasta, the user cannot do this directly. A default set of pasta options can be set in containers.conf, the pasta_options key accepts an array of options (they correspond to the pasta cli options, see the pasta(1) man page).
[network]
pasta_options = ["-i", "eth0"]
By default it will not be possible to connect to the host via the eth0 (or whatever your main interface is called) ip as the exact same ip is used in the container and thus is not routed to the outside. This can cause problems for users of the host.containers.internal name entry as we rely on the host ip being reachable. For Podman 5.0.0 it is likely that this entry will contain a invalid ip but we are working on a fix for Podman 5.0.1. However, the underlying problem will stay if you only have a single host ip (excluding localhost), as there would be no way to route to that if the container always uses the same ip. One workaround for that is to tell pasta to use a different address in the container. In this case set something like this in containers.conf:
pasta_options = ["-a", "10.0.2.0", "-n", "24", "-g", "10.0.2.2", "--dns-forward", "10.0.2.3"]
Also, the default rootless networking tool can be selected in containers.conf under the [network] section with default_rootless_network_cmd, which can be set to pasta or slirp4netns. So, if you run into bugs, you can always revert to slirp4netns.
[network]
default_rootless_network_cmd = "slirp4netns"
# Podman Inspect
Some fields in the podman inspect JSON output have been changed to better match the Docker output. The Config.Entrypoint field was changed to an array from a string because it can hold multiple args. Previously, those would be space-separated, which was not good for parsing. The Config.StopSignal field is now a string and not an integer. As such, it no longer returns the signal number but rather the signal name. This is better for us humans to read and better for cross-platform compatibility because the signal numbers can differ between platforms. Lastly, the State.Health field will no longer be displayed if the container has no healthcheck defined. The same change applies to the libpod REST API. The difference between the two versions looks something like this:
23,27d22
< "Health": {
< "Status": "",
< "FailingStreak": 0,
< "Log": null
< },
145c140,142
< "Entrypoint": "sh",
---
> "Entrypoint": [
> "sh"
> ],
149c146
< "StopSignal": 15,
---
> "StopSignal": "SIGTERM",
# Podman Pod Inspect
The podman pod inspect command now always outputs an array instead of a single object. This was done to improve the consistency with other inspect commands that do the same. If you parse the
podman pod inspect JSON, you have to update it to use the first array element.
# Container Stats API
The libpod stats API was changed to return network stats per interface. The single NetInput and NetOutput fields that contain the sum of all the interfaces were removed, and instead a Network field was added that contains a map/object with the interface name as key, and the per interface statistics as value.
"Network":{"eth0":{"RxBytes":3740,"RxDropped":0,"RxErrors":0,"RxPackets":42,"TxBytes":3036,"TxDropped":0,"TxErrors":0,"TxPackets":34}}
This gives much more information to the user.
# Podman command line flags
The parsing for a number of Podman CLI options which accept arrays has been changed to no longer accept string-delineated lists.
These options are:
--annotationfor
podman manifest annotateand
podman manifest add
--configmap,
--log-optand
--annotationfor
podman kube play
--pubkeysfilefor
podman image trust set
--encryption-keyand
--decryption-keyfor
podman create,
podman run,
podman pushand
podman pull
--env-filefor
podman exec
--bkio-weight-device,
--device-read-bps,
--device-write-bps,
--device-read-iops,
--device-write-iops,
--device,
--label-file,
--chrootdirs,
--log-optand
--env-filefor
podman createand
podman run
--hooks-dirand
--moduleas global
podmanoptions.
The reason for this change was to allow commas in their values rather the interpreting this as a separator. So for example, if my annotation did contain a comma setting
--annotation key=val,withcomma, it would have resulted in an error as it tried to parse
withcomma as a second annotation. So unless you relied on the comma as a separator, this change should not affect you. Otherwise you need to give the option multiple times for each of your value, i.e.
--annotation key1=val1 --annotation key2=val2.
## Leave a ReplyCancel reply