from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        old_table = self.table
        old_size = self.table_size
        
        try:
            # Get new size and update table size
            self.table_size = get_next_size()
        except IndexError:
            # If no more primes available, just double the current size
            self.table_size = old_size * 2
            
        self.num_elements = 0  # Reset count as insert will recount
        
        # Create new empty table based on collision type
        self.table = [None] * self.table_size
            
        # Rehash existing elements
        for slot in old_table:
            if self.ct == "Chain":
                if slot is not None:
                    for key_value in slot:
                        self.insert(key_value)
            else:
                if slot is not None:
                    self.insert(slot)
         
    
    def insert(self, x):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(x)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        old_table = self.table
        old_size = self.table_size
        
        try:
            # Get new size and update table size
            self.table_size = get_next_size()
        except IndexError:
            # If no more primes available, just double the current size
            self.table_size = old_size * 2
            
        self.num_elements = 0  # Reset count as insert will recount
        
        # Create new empty table based on collision type
        self.table = [None] * self.table_size
            
        # Rehash existing elements
        for slot in old_table:
            if self.ct == "Chain":
                if slot is not None:
                    for key_value in slot:
                        self.insert(key_value)
            else:
                if slot is not None:
                    self.insert(slot)
    
    def insert(self, x):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(x)
        
        if self.get_load() >= 0.5:
            self.rehash()
            