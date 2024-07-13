Podman machine’s primary virtualization driver is referred to as a “provider”. In April 2024, I added support for the krun as a provider for MacOS. We made little mention of the addition, because we also needed to tidy up items like regression testing, testing environments, and details around support. But as we near completion of these items, we are ready to let krun support escape from the zoo.

One of the key reasons we added support for krun was its ability to provide pass-through support of the GPUs on Macs to the Podman machine. This feature makes containerized AI workloads on MacOS realistic and broadens the experience for developers alike significantly.

The basic steps to using libkrun with Podman machine are:

- Install the proper software (Podman and libkrun components)
- Configure Podman to use the libkrun provider.
- Create and start a Podman machine.
**Considerations**
If you want to try krun and podman machine, I recommend you execute podman machine reset prior. It is NOT required, and it is destructive in nature because it will remove all your existing Podman machines as well as any machine images you have downloaded (and cached).

**Install Software**
As of this writing, there are two primary means of installing Podman and the required libkrun components: via [brew](https://brew.sh/) or via the Podman installer and other downloads.

**With Brew**
(If you do not have brew, skip to the next section below)

This section assumes you have already installed homebrew. If you have already installed brew and podman (via brew), then you can simply jump to the step where the krun components are added. I personally prefer to download the software and install it myself, but the same Podman user experience can be had by both.

#### Install Podman
To install Podman on your Mac, issue the following command from a terminal prompt:

```
% brew install podman
==> Downloading https://formulae.brew.sh/api/formula.jws.json
#################################################################################################...
[ omitted for brevity ]
==> Running `brew cleanup podman`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
```
#### Install krunkit
To use libkrun, you are required to install krunkit. In versions of Podman 5.2 or greater, it will be bundled into the Podman Mac Installer. But for now, it would be sufficient to install it like so:

```
brentbaude@Mac-mini ~ % brew tap slp/krun
==> Tapping slp/krun
Cloning into '/opt/homebrew/Library/Taps/slp/homebrew-krun'...
remote: Enumerating objects: 291, done.
remote: Counting objects: 100% (28/28), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 291 (delta 22), reused 17 (delta 17), pack-reused 263
Receiving objects: 100% (291/291), 169.33 MiB | 3.79 MiB/s, done.
Resolving deltas: 100% (113/113), done.
Tapped 4 formulae (20 files, 195MB).
bbrentbaude@Mac-mini ~ % brew install krunkit
==> Downloading https://formulae.brew.sh/api/formula.jws.json
==> Downloading https://formulae.brew.sh/api/cask.jws.json
==> Fetching dependencies for slp/krunkit/krunkit: dtc, libepoxy, molten-vk, slp/krunkit/virglrenderer and slp/krunkit/libkrun-efi
[ omitted for brevity ]
==> Installing slp/krunkit/krunkit
==> Pouring krunkit-0.1.1.arm64_sonoma.bottle.tar.gz
🍺 /opt/homebrew/Cellar/krunkit/0.1.1: 7 files, 1.2MB
==> Running `brew cleanup krunkit`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
```
**Without Brew**
If you cannot or choose not to use brew. I frankly prefer this approach as you get binaries produced by the communities themselves.

#### Podman
Download the [latest version](https://github.com/containers/podman/releases) of the Podman Installer for MacOS and follow the installation instructions.

#### Krunkit
**Note**: This step will no longer be needed for Podman 5.2 and later releases. The krunkit binary will be included in the Podman installer and as also signed.
You can get the latest version of krunkit from its [GitHub releases](https://github.com/containers/krunkit/releases). Download the latest version and unpack the tarball to your filesystem.

`brentbaude@Mac-mini ~ % sudo tar xzf ~/Downloads/krunkit-podman-unsigned-0.1.1.tgz -C /opt/podman`
The krunkit binary is unsigned by its upstream community and will not execute unless you [explicitly allow it](https://support.apple.com/guide/mac-help/open-a-mac-app-from-an-unidentified-developer-mh40616/mac). This can be done using the following command:

`brentbaude@Mac-mini ~ % sudo xattr -dr com.apple.quarantine /opt/podman/bin/krunkit`
## 3. **Change Podman machine provider**
The default Podman machine provider on MacOS is called vfkit. To switch to an alternate provider like libkrun, you simply need to define the preferred provider in a configuration file. For Podman, this file (which does not exist by default) is $HOME/.config/containers/containers.conf. You may also need to create the `$HOME/.config/containers` directory depending on your previous use of Podman. It is a YAML based configuration file. In its simplest form, the following will suffice:.

```
brentbaude@Mac-mini ~ % mkdir ~/.config/containers/
brentbaude@Mac-mini ~ % cat ~/.config/containers/containers.conf
[machine]
provider="libkrun"
```
You can verify the provider with the podman info command:
```
brentbaude@Mac-mini ~ % podman info
OS: darwin/arm64
provider: libkrun
version: 5.1.2
```
**4. Create and start a Podman machine**
With the prerequisite software installed and having verified the correct provider is being used, we can create and start a Podman machine with one command:.

```
brentbaude@Mac-mini ~ % podman machine init --now
Looking up Podman Machine image at quay.io/podman/machine-os:5.1 to create VM
Extracting compressed file: podman-machine-default-arm64: done
Machine init complete
Starting machine "podman-machine-default"
This machine is currently configured in rootless mode. If your containers
require root permissions (e.g. ports < 1024), or if you run into compatibility
issues with non-podman clients, you can switch using the following command:
podman machine set --rootful
API forwarding listening on: /var/folders/ml/3yfmdg5n4qn0zq05f7sl34z40000gn/T/podman/podman-machine-default-api.sock
The system helper service is not installed; the default Docker API socket
address can't be used by podman. If you would like to install it, run the following commands:
sudo /opt/homebrew/Cellar/podman/5.1.1/bin/podman-mac-helper install
podman machine stop; podman machine start
You can still connect Docker API clients by setting DOCKER_HOST using the
following command in your terminal session:
export DOCKER_HOST='unix:///var/folders/ml/3yfmdg5n4qn0zq05f7sl34z40000gn/T/podman/podman-machine-default-api.sock'
Machine "podman-machine-default" started successfully
```
Now that the machine is running, you can verify the VM TYPE is libkrun using podman machine ls:

```
brentbaude@Mac-mini ~ % podman machine ls
NAME VM TYPE CREATED LAST UP CPUS MEMORY DISK SIZE
podman-machine-default* libkrun 29 seconds ago Currently running 4 2GiB 100GiB
```
**Ensure GPU is present**
You can check for the presence of the GPU by looking at the devices in the Podman machine itself. The presence of a render device isd representative of the GPU being present.

```
brentbaude@Mac-mini ~ % podman machine ssh ls -l /dev/dri
total 0
drwxr-xr-x. 2 root root 80 Jul 11 06:33 by-path
crw-rw----. 1 root video 226, 0 Jul 11 06:33 card0
crw-rw-rw-. 1 root render 226, 128 Jul 11 06:33 renderD128
```
Note: When running a container that needs access to the GPU, you will need to pass the `--device /dev/dri`
reference to the podman run command.

## Leave a ReplyCancel reply