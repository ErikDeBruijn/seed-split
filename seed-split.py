# ==== The dilemma: security versus access ====
# Nervous writing down your valuable seed phrase on a piece of paper?
# But worried that if you don't, you might lose access?
#
# ==== The easy (risky) way out ====
# Very commonly, people split their seed phrase in x equal parts, however,
# THIS IS VERY INSECURE. An attacker that obtains even one split has 
# significantly easier job of compromising your key and steal to your 
# crypto assets/currencies. E.g. when splitting a 12 word seed in 4 pieces
# and just one is found, it makes it more than 8 billion times easier to crack.
# For this scheme, unless all components are found, it's no easier to crack.
# 
# ==== The solution ====
# The alternative, downloading and running possibly hostile code or visiting 
# a website to split the secret for you is aguably worse, as you trust its 
# maker or a hacker that compromises the code 100% with your key.
# Below is a better procedure with just a few lines of code, that you
# can verify to have no backdoors.
# 
# This can also be an insurance policy for your loved ones to ensure your digital
# assets aren't locked forever in cyptography.
#
# The (only?) proven fundamentally secure cypher is a one time pad. 
# This script creates a number to word lookup table for the person decyphering 
# and a cyphering table to create the message for the recipient. The cypher 
# should be destroyed after the creation of the message. The lookup table and
# the message should be stored separate and safely, because combined they will
# reveal your secret seed. When an attacker finds either the lookup table or
# the message, your seed is not even 0.1% easier to crack.
# 
# More about one-time pad:
# https://www.khanacademy.org/computing/computer-science/cryptography/crypt/p/perfect-secrecy-exploration
# 
# ==== Okay, how does this work? ====
# Step 1:
# - Get word list and save it in the same folder as this script:
#   wget https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt
# 
# Step 2: Create component 2 of 2.
# - if you can, read the script and see for yourself if you trust it. I kept it
#   short and "dumb".
# - execute this python script to get a randomized list of numbers next to each word
# - print out the unique number-to-word list to be stored separately as component 2
#   by opening the generated file:
#   component-I-decrypt.txt
# 
# Step 3: Create component 1 of 2.
# - use component 2 to look up each of your seed words and write down the 
#   corresponding numbers for each word (without writing the words!)
# 
# Step 4: Store both components in different secure places that you know 
# of, ideally in tamper-evident storage.
# - Create instructions for your older self or the recipients.
# - Test the system before sealing them, ideally let someone trusted check if he/she
#   can reproduce the entire seed.
# - When using an envelope, these tips may be useful to secure the envelope:
#   http://www.wikihow.com/Secure-an-Envelope
# - Distribute the envelopes
# - Remove the generated files "component-I-decrypt.txt" and "encryption-cypher.txt"

# Optional steps:
# - You can repeat the process, so that you have some redundancy so that for 
#   instance a house can burn down without also losing access to your digital
#   assets.
# - Advanced users will note that you can also chain this process by using this 
#   script multiple times to create 3 components or more, each of which doesn't
#   reveal anything without knowing all of the components.
# - Donate if you like:
#     BTC: 1EQdz4HGkvLQw4SjsvhkGc2cbjec5BEtD6
#     LTC: LanbojE8y5nUtiBWbQFLYC76aU7amWSDmw
#     ETH: 0xFc6D36f2Dbf8E7462c2A7E972B6557dFE7257931
#
# http://pythonfiddle.com/basic-one-time-pad/

import random

f_name, word_count, i, cols, s = ["encryption-cypher.txt", 2048, 0, 6, ""]
nrs = random.sample(range(0, word_count), word_count)
words = []
nr_words = {}
f = open(f_name, 'w')
print "Generating %s ..." % f_name
print >> f, "==== Encryption sheet to make component 1 of 2 (DESTROY after use) ===="
with open ("english.txt", "r") as myfile:
	for line in myfile:
		words.append(line.strip())
for word in words:
	s = "%s %-9s=%-05d" % (s, word, nrs[i])
	nr_words[nrs[i]] = word
	i = i + 1
	if(i%cols==0):
		print  >> f, s
		s = ""
print >> f, "==== END OF %d CODES ==== " % i
f.close()

f_name, i, cols, s = ["component-II-decrypt.txt", 0, 6, ""]
f = open(f_name, 'w')
print "Generating %s ..." % f_name

print >> f, "==== DO NOT DISCARD - STORE SAFELY - component 2 of 2 (decryption cypher) ===="
for nr, word in nr_words.items():
	s = "%s %-04d=%-9s" % (s, nr, word)
	i = i + 1
	if(i%cols==0):
		print  >> f, s
		s = ""
print >> f, "==== END OF %d CODES ==== " % i

print "Done."

