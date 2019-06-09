One time pad for cold storage of cryptocurrency wallet keys
================
No security method is guaranteed to be secure, or is it?

A so called "one-time pad" as an encryption cypher is mathematically proven to 
be secure. It's probably the best way to keep your cryptocurrency holding safe. 
This script applies principle to a crypto seed phrase.

There are too many horror stories about people using their access to their 
cryptocurrencies because they forgot or lost a piece of paper with their seed
phrase. Or, someone found it and transferred their crypto's...

The dilemma: security versus access
================

Are you nervous about writing down your wallet's seed phrase on a piece of paper?
But worried that if you don't, you might lose access?

Cold storage is an often used way to secure a cryptocurrency "wallet" and is
usually preferred over online storage and keeping private keys on a computer or
phone. However, you want to minimize the chance that you lose access to the private
key, but also minimize the chance that other will gain access.

The easy but risky way out
================
Very often, people split their seed phrase in x equal parts, however,
THIS IS VERY INSECURE. An attacker that obtains even one parts has 
significantly easier job of compromising your key and steal to your 
crypto assets/currencies. Imagine having to guess two numbers between one
and ten correctly. This is more than twice as hard than guessing a single 
number between one and ten. This principle applies to private keys as well.

Splitting the phrase also linearly increases the chances of losing one of 
the parts.

My solution
================

The alternative, downloading and running possibly hostile code or visiting 
a website to split the secret for you is aguably worse, as you trust its 
maker or a hacker that compromises the code 100% with your key.
Below is a better procedure with just a few lines of code, that you
can verify to have no backdoors.

This can also be an insurance policy for your loved ones to ensure your digital
assets aren't locked forever in cyptography.

The (only?) proven fundamentally secure cypher is a one time pad. 
This script creates a number to word lookup table for the person decyphering 
and a cyphering table to create the message for the recipient. The cypher 
should be destroyed after the creation of the message. The lookup table and
the message should be stored separate and safely, because combined they will
reveal your secret seed. When an attacker finds either the lookup table or
the message, your seed is not even 0.1% easier to crack.

More about one-time pad:
https://www.khanacademy.org/computing/computer-science/cryptography/crypt/p/perfect-secrecy-exploration

Okay, how does this work?
================

Step 1:
- Get word list and save it in the same folder as this script:
  wget https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt

Step 2: Create component 2 of 2.
- if you can, read the script and see for yourself if you trust it. I kept it
  short and "dumb".
- execute this python script to get a randomized list of numbers next to each word
- print out the unique number-to-word list to be stored separately as component 2
  by opening the generated file:
  component-I-decrypt.txt

Step 3: Create component 1 of 2.
- use component 2 to look up each of your seed words and write down the 
  corresponding numbers for each word (without writing the words!)

Step 4: Store both components in different secure places that you know 
of, ideally in tamper-evident storage.
- Create instructions for your older self or the recipients.
- Test the system before sealing them, ideally let someone trusted check if he/she
  can reproduce the entire seed.
- When using an envelope, these tips may be useful to secure the envelope:
  http://www.wikihow.com/Secure-an-Envelope
- Distribute the envelopes
- Remove the generated files "component-I-decrypt.txt" and "encryption-cypher.txt"

Optional steps:
- You can repeat the process, so that you have some redundancy so that for 
  instance a house can burn down without also losing access to your digital
  assets.
- Advanced users will note that you can also chain this process by using this 
  script multiple times to create 3 components or more, each of which doesn't
  reveal anything without knowing all of the components.
- Donate if you like:
    BTC: 1EQdz4HGkvLQw4SjsvhkGc2cbjec5BEtD6
    LTC: LanbojE8y5nUtiBWbQFLYC76aU7amWSDmw
    ETH: 0xFc6D36f2Dbf8E7462c2A7E972B6557dFE7257931
