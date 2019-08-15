import hashlib
import datetime

class Block(): 
    def __init__(self, index, timestamp, data, prev_hash): 
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hashing()
    
    def hashing(self): 
        key = hashlib.sha256()
        key.update(str(self.index)).encode('utf-8')
        key.update(str(self.timestamp)).encode('utf-8')
        key.update(str(self.data)).encode('utf-8')
        key.update(str(self.prev_hash)).encode('utf-8')

        return key.hexdigest()

class Chain(): 
    def __init__(self): 
        self.Blocks = [self.make_genesis_block()]
    
    def make_genesis_block(self): 
        return Block(0, datetime.datetime.utcnow(), "Genesis", "arbitrary")

    def add_block(self, data): 
        index = len(self.Blocks)
        date = datetime.datetime.utcnow()
        prev_hash = self.Blocks[-1].hash

        self.Blocks.append(Block(index, date, data, prev_hash))  
    
    def verify(self): 
        secure = True

        for i in range(1, len(self.Blocks)): 
            # Verifying if Block is at correct Index
            if self.Blocks[i].index != i: secure = False
            # Verifying if previous block's Hash is stored correctly
            if self.Blocks[i-1].hash != self.Blocks[i].prev_hash: secure = False
            # Verifying Block Hash with Hashing function
            if self.Blocks[i].hash != self.Blocks[i].hashing(): secure = False
            # Checking for Backdating in Timestamps
            if self.Blocks[i-1].timestamp >= self.Blocks[i].timestamp: secure = False
        
        return secure
