import hashlib

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
        self.blocks = [self.make_genesis_block()]
    
    def make_genesis_block(self): 
        return Block(0, datetime.datetime.utcnow(), "Genesis", "arbitrary")

    def add_block(self, data): 
        index = len(self.blocks)
        date = datetime.datetime.utcnow()
        prev_hash = self.blocks[-1].hash

        self.blocks.append(Block(index, date, data, prev_hash))  
    
    