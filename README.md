# Minimal Blockchain

I recently completed IBM's online course titled "Blockchain Essentials", but in order to fully grasp the concept I built this simple Blockchain.
I like learning by doing. It forces me to deal with the subject matter at a code level, which gets it sticking.

In my implementation of a Blockchain, Each block has the following features - Index, Timestamp, data, previous hash and the current Hash.
I used the sha256 Hashfunction to generate the hash of each block using all of its features encoded in 'uft-8'. The chain is implemented 
using python's built in List data structure.

Moreover, I created a verify method which verifies the integrity of Blockchain by: 
- Verifying Block Indexes
- Comparing Hash in the current block with the previous hash stored in the next block
- Verifying Block Hash with the value from the sha256 Hash function
- Checking for Backdating
