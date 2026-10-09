**OpenSSH 10.6, released Tuesday, makes compression less effective and rejects some usernames** that previously worked, and the maintainers knew both changes would break things when they shipped them.

One change disables the LZ77 dictionary coder used for SSH compression after researchers found that sharing compression state across multiple channels could expose plaintext. The other blocks `$` and `\` in command-line usernames to prevent them from being interpreted by the shell through directives such as ProxyCommand and Match exec.

The [release](https://www.openssh.org/txt/release-10.6) comes as OpenSSH sees more security research conducted with AI models, while [those models get better at finding exploitable flaws](https://thenewstack.io/claude-exploits-openai-forum/). Other researchers later found some of those bugs independently. OpenSSH warned that adversaries who don’t report what they find “are likely to be able to discover these bugs too,” and for now, the project plans to release fixes more often rather than wait for its usual release schedule.

> OpenSSH warned that adversaries who don’t report what they find “are likely to be able to discover these bugs too,” and for now, the project plans to release fixes more often rather than wait for its usual release schedule.

## Compression context leaks plaintext

SSH can carry several things over one encrypted connection, including an interactive shell, port forwarding, or a dynamic SOCKS proxy. When compression is enabled, those channels share the same compression state, although [OpenSSH leaves compression off by default](https://man.openbsd.org/ssh_config), so the attack only works when someone has turned it on.

Ruhr University Bochum security researchers [Fabian Bäumer](https://www.linkedin.com/in/fabian-baumer/) and [Marcus Brinkmann](https://www.linkedin.com/in/marcus-brinkmann-57b39a1/) demonstrated the problem in their paper, [“Crossing the Streams: SSH Plaintext Recovery via a Common Compression Context in Multiplexed Channels.”](https://arxiv.org/abs/2609.07709) An attacker who can feed chosen plaintext into one channel and watch the resulting encrypted traffic can use the compression to recover secrets moving through another channel in the same session.

> An attacker who can feed chosen plaintext into one channel and watch the resulting encrypted traffic can use the compression to recover secrets moving through another channel in the same session.

The leak comes from LZ77’s memory. Instead of encoding the same sequence of bytes again, it can point back to a matching sequence it has already seen. OpenSSH shared that history across channels, so data controlled by an attacker could change how a secret elsewhere in the session was compressed. When a guess matched part of that secret, the resulting traffic could get slightly shorter, giving the attacker another piece of information.

That puts the attack in the same family as CRIME and BREACH against HTTP over TLS, although pulling it off here requires a fairly specific setup. The attacker-controlled traffic and the secret have to share the same multiplexed SSH session. In their lowest-noise tests, Bäumer and Brinkmann recovered an eight-character secret from a 26-character alphabet in a median of 276 guesses across 100 trials. In their noisier browser-based scenario, that jumped to about 27,600.

The two researchers built the proof-of-concept implementations for all three attack scenarios with Claude Code, and they weren’t the only ones using AI tooling against OpenSSH, since the 10.6 release also credits [Chris Rohlf](https://www.linkedin.com/in/chrisrohlf/), working with Claude and Anthropic Research, with finding two other bugs fixed in the release.

## Huffman stays, LZ77 goes

OpenSSH went with the straightforward fix and removed the shared dictionary entirely. Deflate uses LZ77 to find repeated chunks of previously seen data, then Huffman coding to represent frequently used values with fewer bits. OpenSSH 10.6 disables the LZ77 part in both `ssh` and `sshd`, while keeping Huffman coding.

Compression still works, just not as well. OpenSSH warns that the `Compression` option will be less effective and recommends handling compression at the application layer instead, where it says it will usually perform better without being vulnerable to this attack.

Most interactive SSH sessions probably won’t notice the difference, although automated jobs moving large amounts of compressible data over constrained connections could. Those workloads may need to move compression out of SSH and into the application after upgrading.

> Most interactive SSH sessions probably won’t notice the difference, although automated jobs moving large amounts of compressible data over constrained connections could.

The username change is aimed at commands built from outside input. An internal tool, CI job or agent might run something like `ssh "$INPUT_USER@host"`, and that username can later end up inside `ProxyCommand`, `Match exec` or another command passed to the shell, where characters such as `$` and `\` can suddenly become shell syntax instead of just part of the username.

This isn’t the first time the project has tightened this path. [Version 10.3](https://www.openssh.org/txt/release-10.3) fixed a related bug where command-line usernames were checked for shell metacharacters too late, after they could already be expanded through `ssh_config`.

With 10.6, `$` and `\` are rejected in usernames passed on the command line, but the restriction doesn’t apply when the username is set with the `User` directive in an SSH configuration file. Legitimate accounts containing either character can still work that way, although scripts and agent tooling that pass those usernames directly will have to change.

## Post-quantum keys, deprecated scp

There are a few other changes in OpenSSH 10.6 that could trip up automated workflows. The hybrid post-quantum `ssh-mldsa44-ed25519` signature algorithm loses its experimental `@openssh.com` suffix, which means keys created with the earlier implementation need to be regenerated or removed. The release also begins phasing out `scp -R` for remote-to-remote copies; it still works in 10.6, but now produces a warning and will eventually be ignored.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)