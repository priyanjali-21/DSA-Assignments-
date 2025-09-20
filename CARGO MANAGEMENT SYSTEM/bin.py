from avl import *
from object import Object, Color

class Bin:
    def __init__(self):
        self.object_tree_inside_bin = AVLTree()  # We have object id's as our key
        pass

    def add_object(self, object_node):
        self.object_tree_inside_bin.insert_node(object_node)
        # Implement logic to add an object to this bin
        pass

    def remove_object(self, object_id):
        id_object_node = self.object_tree_inside_bin.key_search(self.object_tree_inside_bin.root,object_id)
        self.object_tree_inside_bin.delete_node(id_object_node)
        # Implement logic to remove an object by ID
        pass

