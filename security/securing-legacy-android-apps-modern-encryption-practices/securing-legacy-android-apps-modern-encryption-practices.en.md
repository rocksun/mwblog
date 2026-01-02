As software engineers rise up the ranks from junior levels to managerial roles in [mobile development](https://thenewstack.io/intertwined-worlds-platform-and-mobile-app-engineering/), [good code practices](https://thenewstack.io/why-quality-code-matters-and-how-to-achieve-it/) become more apparent and not just an afterthought. One of the litmus tests of seniority is the ability to adapt to modern security practices.

It is worth noting that as the mobile ecosystem moves fast, attacks on user data also evolve at the same pace. Therefore, it is the engineer’s responsibility to modernize the remnants of legacy implementations, even if they still appear to work. That’s because they expose users to security threats and render applications susceptible to attacks.

Some of the security debt often hidden beneath old code include, but are not limited to:

* Use of [MD5](https://www.okta.com/identity-101/md5/#:~:text=The%20message%2Ddigest%20algorithm%20MD5,matched%20with%20a%20public%20key.) or [SHA-1](https://www.nist.gov/news-events/news/2022/12/nist-retires-sha-1-cryptographic-algorithm) for hashing passwords or verifying data integrity.
* Reliance on [DES](https://www.geeksforgeeks.org/computer-networks/data-encryption-standard-des-set-1/) or [AES/ECB](https://www.npmjs.com/package/aes-ecb) for encryption (both prone to predictable patterns).
* Hardcoded API keys or symmetric keys stored in SharedPreferences instead of the Android Keystore System.
* Outdated authentication flows, such as Basic Auth or custom token handling.
* Use of deprecated and [ESAPI-banned API](https://www.appmarq.com/public/tqi,1039044,Avoid-usage-of-BannedAPI-when-using-ESAPI-library), such as `android.webkit.WebView.setJavaScriptEnabled(true)` and `Math.Random.*`
* Non-compliance with the most recent OWASP Top 10 lists.

A typical security scan of a mobile application by AppSec tools, such as Checkmarx, will more often reveal the above practices, all of which were once common but are now considered dangerous.

Let’s explore shared legacy cryptographic algorithms and their modern equivalents.

## The Dangers of Weak Hash Algorithms (MD5 and SHA-1)

MD5 and SHA-1 are cryptographic hash functions known for their vulnerabilities, including susceptibility to collision attacks. A cryptographic hash function takes any input, which can be a message, file or password, producing a short and unique fingerprint of that data. A collision attack occurs when two distinct inputs produce the same hash, leading to identity spoofing, [tampering with signed data and other security breaches](https://thenewstack.io/how-iam-missteps-cause-data-breaches/) by attackers through reverse-engineering or hash manipulation.

These algorithms have been broken publicly for years. MD5, collisions can be generated in milliseconds on consumer hardware. A key vulnerability: SHA-1 was officially deprecated after [Google’s SHAtteredattack in 2017](https://thehackernews.com/2017/02/sha1-collision-attack.html#:~:text=The%20Google%2Dled%20attack%20on%20SHA1%2C%20dubbed%20SHAttered%2C,attackers%20to%20break%20communications%20encoded%20with%20SHA1.). Over time, cryptanalysis has shown that SHA-1 is no longer secure enough for use in sensitive applications.

Additionally, continuous use of these algorithms for password storage, signature generation or integrity checks can lead to non-compliance with regulatory bodies such as EU data privacy laws GDPR, the global payment card industry security standard PCI-DSS and others.

## Alternatives for Data Integrity and Password Hashing

Therefore, to secure your legacy application, consider replacing the above vulnerable algorithms with the following:

For data integrity, instead of using an MD5 checksum, consider a more secure cryptographic hash function, such as [SHA-256](https://www.movable-type.co.uk/scripts/sha256.html) or [SHA-3](https://csrc.nist.gov/projects/hash-functions/sha-3-project). They offer stronger resistance to collision and pre-image attacks. Using SHA-256 or SHA-3 also guarantees determinism by ensuring the same input always gives the same hash, while ensuring that even a tiny input change results in a significant change in output. This avalanche effect helps to detect even the slightest one-bit tampering or corruption.

When it comes to password storage and hashing, consider an algorithm that not only provides data integrity but also ensures confidentiality. This is where MD5 and SHA-1 fail. These cryptographic hash functions are designed for integrity and speed, but never for secure password storage. Additionally, the hashes are always stored by adding salt, making them prone to rainbow table attacks.

To overcome this, consider using security-focused algorithms such as [bcrypt](https://auth0.com/blog/hashing-in-action-understanding-bcrypt/), [Argon2](https://argon2.online/) or [PBKDF2](https://hexdocs.pm/pbkdf2_elixir/Pbkdf2.html). These are not just hash algorithms but key derivation functions (KDFs), which are engineered to resist brute-force and GPU attacks.

Password-Based Key Derivation Function 2 (PBKDF2) is one of the most widely used KDFs and is approved by the National Institute of Standards and Technology (NIST). PBKDF2 strengthens the security of hashed passwords by adding a salt to the pre-hashed password, ensuring that the same password produces a different hash. This approach defeats the rainbow table attacks. PBKDF2 also applies many iterations of the hashing process, known as stretching. Stretching implies multiple applications of the hash function (thousands or even millions of times) to the password and salt combination. This approach slows the hash computation, thereby reducing the feasibility of brute-force attacks.

PBKDF2 is limited in the number of salts it can generate, so it is the engineer’s responsibility to generate and store salts separately. It is this limitation that makes bcrypt a preference for many. With built-in and automatic salt handling, bcrypt is considered more secure due to resistance to GPU cracking.

It is older, CPU-intensive and simpler to implement. This makes it a reasonable choice for less demanding applications or legacy applications, but it is not the sharpest tool available. For this, Argon2 is the double-edged “Honjo Masamune” sword.

Argon2 is a modern, secure KDF designed to protect passwords by being memory-hard, which means it requires more memory resources. This makes brute-force attacks using fast hardware, such as GPUs, much less efficient and more costly. It is also highly configurable, enabling fine-tuning of security parameters such as memory usage, iterations and parallelism — making it resistant to evolving cracking techniques.

It is worth mentioning that KDFs should be implemented on the backend server for password storage, as hashing on the client-side (Android) is insecure against server compromise.

## Vulnerabilities of DES and AES/ECB Encryption

Other than the above, if your application uses symmetric encryption as an alternative, replace AES/ECB or DES with [AES/GCM](https://medium.com/@pravallikayakkala123/understanding-aes-encryption-and-aes-gcm-mode-an-in-depth-exploration-using-java-e03be85a3faa). Symmetric encryption is one of the two fundamental pillars of modern cryptography, alongside public-key (asymmetric) encryption. In symmetric encryption, the same key is used for both encryption and decryption. It is also widely used in modern mobile development, ranging from file encryption and token storage to secure preferences.

The Advanced Encryption Standard (AES) replaced the deprecated Data Encryption Standard (DES), a 56-bit symmetric cipher from the 1970s. DES has a very small keyspace, making it easy to brute-force.

AES/ECB (Electronic Codebook) has a fundamental weakness of pattern exposure. By design, AES/ECB divides plaintext into fixed-size blocks and encrypts each block independently with the same key. As simple as it is, it is considered insecure because the same plaintext blocks produce the same ciphertext blocks, hence leaking patterns.

## Modern Symmetric and Asymmetric Encryption Alternatives

The modern and secure alternatives include:

[AES/CBC](https://www.cincopa.com/learn/what-is-cipher-block-chaining-cbc-mode-in-aes#:~:text=Mode%20in%20AES?-,Cipher%20Block%20Chaining%20(CBC)%20is%20a%20block%20cipher%20mode%20of,if%20plaintext%20contains%20repetitive%20patterns.) (Cipher Block Chaining), where each plaintext block is [XORed](https://www.youtube.com/watch?v=h7Cgx-pn9bw) with the previous ciphertext block before being encrypted, causing a chaining effect. The first block must also have a unique initialization vector (IV).

[AES-GCM](https://datatracker.ietf.org/doc/html/rfc5288#:~:text=Abstract%20This%20memo%20describes%20the,Hellman%2Dbased%20key%20exchange%20mechanisms.) (Galois/Counter Mode) is the modern, integrity-centered and recommended mode of symmetric encryption on Android and in most secure systems today. It operates by incrementing a counter and XORing the result with the plaintext. GCM is an [Authenticated Encryption with Associated Data (AEAD)](https://developers.google.com/tink/aead) mode, meaning it provides both confidentiality and integrity in a single efficient step.

It is crucial to make sure that the symmetric keys are not hard-coded or stored in insecure locations such as SharedPreferences. Instead, use Android Keystore System which stores keys in an isolated and non-exportable way and using the Cipher class with the correct transformation string (such as `AES/GCM/NoPadding`).

Asymmetric encryption (public-key encryption), on the other hand, is too slow to be used for [bulk data on mobile applications](https://thenewstack.io/how-time-plays-a-crucial-role-in-aggregating-mobile-data/). It is primarily used to supplement symmetric encryption in a hybrid approach to secure the exchange of AES symmetric keys and to support digital signatures for authentication and data integrity. [RSA (Rivest-Shamir-Adleman)](https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/) relies on the difficulty of factoring large prime numbers. It uses a public key for encryption and a private key for decryption.

For public-key encryption, consider [RSA/OAEP (Optimal Asymmetric Encryption Padding](https://www.cs.rit.edu/~spr/COURSES/CRYPTO/oaep.pdf)) or [ECC (Elliptic Curve Cryptography)](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/) instead of RSA/ECB/PKCS1, which lack modern cryptographic guarantees. The padding scheme (PKCS1) used in RSA/ECB/PKCS1 is the leading cause of the vulnerability, as it is obsolete, lacks modern security proofs and is susceptible to chosen-ciphertext attacks. OAEP padding eliminates these vulnerabilities by adding randomness and using hash functions.

For signing or certificate purposes, consider transitioning to stronger algorithms, such as RSA with SHA-256 or [ECDSA (Elliptic Curve Digital Signature Algorithm)](https://www.cs.miami.edu/home/burt/learning/Csc609.142/ecdsa-cert.pdf). When it comes to Android security and other resource-limited environments, ECDSA is highly favoured because it can produce smaller and faster-processing keys, which is important for TLS/SSL communication.

Additionally, to secure the certificates and build trust during the communication between applications and the server over TLS/SSL, consider certificate pinning. It adds a layer of security by ensuring that the application only trusts specific, preset certificates or public keys, which is a crucial defence against man-in-the-middle (MITM) attacks.

## **Conclusion**

Migrating to modern cryptography should be a canary process that involves a clear audit of legacy algorithm use, risk classification, compatible migration and, finally, intensive testing and verification. All these processes should also involve clear documentation of the project blueprint for future development.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/11/2a15df1a-cropped-eee864b7-stephen-henry1.jpg)

Stephen Henry is a mobile engineer and a technologist at Andela. Stephen is highly experienced in mobile application development, with a specialized focus on iOS and Android platforms. He is skilled in various programming languages including Swift, Kotlin and Java,...

Read more from Stephen Henry](https://thenewstack.io/author/stephen-henry/)