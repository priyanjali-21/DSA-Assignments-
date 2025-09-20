class Node:
    def __init__(self, key): # Key can be bin_id,bin_capacity or object_id , depending on the tree
        self.key = key
        self.item = None
        self.left = None
        self.right = None
        self.height = 1
        self.extra_key = None
        pass
