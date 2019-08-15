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
    
    