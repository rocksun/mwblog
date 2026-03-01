It was a normal day working from home. I was sitting at my desk, typing away, when I heard my son's little voice *"Daddy...what are you doing?"* I looked at him and said *"I'm in the middle of a change."* He stared at me, clearly not understanding a word. *"I'm making computers trust each other so they can talk safely."* Silence. Staring intensifies...

I'm starting to wonder how the heck do I explain Kubernetes Ingress TLS Certificates to a 4-year-old? Buckle up.

*"Imagine you're going to an aquarium, there are fish, sharks and turtles waiting for you. Before you can go inside, you need a special wristband. One day, that wrist band is going to get old and the door man that checks them will say 'Sorry, you* can't *come in...this wristband is too old.' Wristbands don't last forever. You will need to get a new wristband so you can go inside."*

Kubernetes is big and complicated, and I can’t cover it all here, but I can teach you how to give your Ingress a TLS certificate so your apps are trusted and secure.

## Break it down

* Kubernetes - The platform that runs your apps / the aquarium
* Secret - A safe place to store important things your apps need / the staff’s box of wristbands
* Ingress - The gateway that lets external traffic reach your apps / the main lobby
* TLS - The system that encrypts traffic and ensures its secure / the door man
* Certificates - Digital keys that proves identity / the wristband

### Step 1 - Get yourself a fresh wristband, err...I mean certificate.

Before anyone can enter the aquarium, you'll need a new wristband. That means a new TLS certificate. I usually take the full PEM file so you have the full certificate chain and separate out the key.

### Step 2 - Add the Certificate in Kubernetes

Now it's time to notify the aquarium staff that there will be new wristbands. In Kubernetes, this means creating a Secret to store your certificate and key. Think of it as a box where all the new wristbands are stored until the doorman needs to know what color they are for the day.

```
apiVersion: v1
kind: Secret
metadata:
  name: aquarium-tls
  namespace: aquarium
type: kubernetes.io/tls
data:
  tls.crt: <new-aquarium-certificate>
  tls.key: <new-aquarium-key>
```

### Step 3 - Apply the Certificate to the Ingress

Finally, we get to tell the doorman to check for the new colored wristbands. In Kubernetes, this is pointing the Ingress to the Secret we created. Once it knows about the new certificate, all visitors can enter the aquarium!

```
spec:
  tls:
  - hosts:
    - aquarium.com
    secretName: aquarium-tls
```

Without a trusted wristband, visitors were turned away, browsers shouted warnings, and the fish looked sad and lonely. But once we gave out fresh wristbands, the doors opened, visitors roamed happily through the aquarium, and everyone enjoyed a safe and secure visit.

## Want some advice?

1. Check your certificates before they expire and setup monitoring to notify you when the time comes.
2. Automation helps. Use cert-manager to issue and renew certificates automatically.
3. Secrets matter. Double-check names, namespaces, and encoding.
4. Test everything. Make sure the Ingress points to the right Secret and apps or service show as trusted.
5. TLS isn’t optional. Don't be lazy and apply it to everything!