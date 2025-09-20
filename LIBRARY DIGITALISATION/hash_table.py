class HashTable:
    def __init__(self, collision_type, params):
        self.ct = collision_type
        self.num_elements = 0
        
        if collision_type in ["Chain", "Linear"]:
            self.z = params[0]
            self.table_size = params[1]
            self.table = [None] * self.table_size
        else:  # Double hashing
            self.z = params[0]
            self.z2 = params[1]
            self.c2 = params[2]
            self.table_size = params[3]
            self.table = [None] * self.table_size
    
    def h1(self, key):
        """Polynomial accumulation hash function"""
        h = 0
        for ch in key[::-1]:
            if 'a' <= ch <= 'z':
                value = ord(ch) - ord('a')
            else:  # 'A' to 'Z'
                value = ord(ch) - ord('A') + 26
            h = (h * self.z + value) 
        return h% self.table_size
    
    def h2(self, key):
        """Second hash function for Double hashing"""
        h = 0
        for ch in key[::-1]:
            if 'a' <= ch <= 'z':
                value = ord(ch) - ord('a')
            else:  # 'A' to 'Z'
                value = ord(ch) - ord('A') + 26
            h = (h * self.z2 + value) 
        return self.c2 - (h % self.c2)
    
    def get_slot(self, key):
        initial_slot = self.h1(key)
        
        if self.ct == "Chain":
            return initial_slot
            
        slot = initial_slot
        if self.ct == "Linear":
            while self.table[slot] is not None:
                k, _ = self.table[slot]
                if k == key:
                    return slot
                slot = (slot + 1) % self.table_size
        else:  # Double hashing
            step = self.h2(key)
            while self.table[slot] is not None:
                k, _ = self.table[slot]
                if k == key:
                    return slot
                slot = (slot + step) % self.table_size
                
        return slot
    
    def insert(self, x):
        if isinstance(x,tuple):
            key, value = x
        else:
            key, value = x, 0
            
        slot = self.get_slot(key)
        
        if self.ct == "Chain":
            if self.table[slot] is None:
                self.table[slot] = []
            for i, entry in enumerate(self.table[slot]):
                if entry[0] == key:
                    self.table[slot][i] = (key, value)
                    return
            self.table[slot].append((key, value))
            self.num_elements += 1
        else:
            if self.table[slot] is None:
                self.table[slot] = (key, value)
                self.num_elements += 1
    
    def find(self, key):
        slot = self.h1(key)
        
        if self.ct == "Chain":
            if self.table[slot] is not None:
                for k, v in self.table[slot]:
                    if k == key:
                        return v
        else:
            if self.ct == "Linear":
                while self.table[slot] is not None:
                    k, v = self.table[slot]
                    if k == key:
                        return v
                    slot = (slot + 1) % self.table_size
            else:  # Double hashing
                step = self.h2(key)
                while self.table[slot] is not None:
                    k, v = self.table[slot]
                    if k == key:
                        return v
                    slot = (slot + step) % self.table_size
                    
        return None
    
    def get_load(self):
        return self.num_elements / self.table_size
    
    def __str__(self):
        result = []
        for key_slot in self.table:
            if key_slot is None:
                result.append("<EMPTY>")
            elif self.ct == "Chain" and len(key_slot) > 0:
                result.append(" ; ".join(str(key[0]) for key in key_slot))
            else:
                result.append(str(key_slot[0]) if key_slot else "<EMPTY>")
        return " | ".join(result)

class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
    
    def insert(self, key):
        super().insert(key)
    
    def find(self, key):
        return (super().find(key) == 0)
        
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
    
    def insert(self, x):
        super().insert(x)
    
    def find(self, key):
        return super().find(key)
