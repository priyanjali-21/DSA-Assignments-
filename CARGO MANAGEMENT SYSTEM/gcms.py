from bin import Bin
from avl import *
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.gcms_tree_for_bin_capacity = AVLTree()
        self.gcms_tree_for_bin_id = AVLTree()
        self.gcms_tree_for_object_id = AVLTree()
        pass 

    def add_bin(self, bin_id, bin_capacity):
        # gcms_tree_for_bin_capacity
        bin_capacity_node = self.gcms_tree_for_bin_capacity.key_search(self.gcms_tree_for_bin_capacity.root,bin_capacity)

        if bin_capacity_node == None:
            insert_bin_cap_node = Node(bin_capacity)
            insert_bin_cap_node.item = AVLTree()
            insert_id_node_in_capacity_node_1 = Node(bin_id)
            insert_bin_cap_node.item.insert_node(insert_id_node_in_capacity_node_1)
            self.gcms_tree_for_bin_capacity.insert_node(insert_bin_cap_node)
        else:
            insert_id_node_in_capacity_node_2 = Node(bin_id)
            bin_capacity_node.item.insert_node(insert_id_node_in_capacity_node_2)

        # gcms_tree_for_bin_id
        bin_id_node = Node(bin_id)
        bin_id_node.item = Bin()
        bin_id_node.extra_key = bin_capacity
        self.gcms_tree_for_bin_id.insert_node(bin_id_node)
        
        pass

    def  add_object(self, object_id, object_size, color):
        color1 = color.name
        bin_cap_node = None
        bin_id_node = None
        bin_cap_root = self.gcms_tree_for_bin_capacity.root
        bin_id_root = self.gcms_tree_for_bin_id.root

        if color1 == "BLUE" or color1 == "YELLOW":
            bin_cap_node = self.gcms_tree_for_bin_capacity.blue_or_yellow_cap_search(bin_cap_root,object_size)
        else:
            bin_cap_node = self.gcms_tree_for_bin_capacity.green_or_red_cap_search(bin_cap_root,object_size)
        
        if bin_cap_node == None:
            raise NoBinFoundException
        
        else: 
            if color1 == "BLUE":
                bin_id_node = self.gcms_tree_for_bin_capacity.blue_search(bin_cap_root,object_size)
            elif color1 == "YELLOW":
                bin_id_node = self.gcms_tree_for_bin_capacity.yellow_search(bin_cap_root,object_size)
            elif color1 == "RED":
                bin_id_node = self.gcms_tree_for_bin_capacity.red_search(bin_cap_root,object_size)
            elif color1 == "GREEN":
                bin_id_node = self.gcms_tree_for_bin_capacity.green_search(bin_cap_root,object_size)
            
            if bin_id_node == None:
                raise NoBinFoundException
            else:
                # gcms_tree_for_bin_id
                object_node_for_bin_id_tree = Node(object_id)
                object_node_for_bin_id_tree.item = Object(object_id,object_size,color,bin_id_node.key)
                bin_id_node_to_add_obj = self.gcms_tree_for_bin_id.key_search(bin_id_root,bin_id_node.key)
                bin_id_node_to_add_obj.item.add_object(object_node_for_bin_id_tree)
                bin_id_node_to_add_obj.extra_key -= object_size 

                # gcms_tree_for_bin_capacity
                extra_key_of_bin_id = bin_id_node.key
                # extra_key_of_bin_cap = bin_cap_node.key
                bin_cap_node.item.delete_node(bin_id_node)
                if bin_cap_node.item.root == None:
                    self.gcms_tree_for_bin_capacity.delete_node(Node(bin_cap_node.key))
                
                bin_capacity_node = self.gcms_tree_for_bin_capacity.key_search(self.gcms_tree_for_bin_capacity.root,bin_id_node_to_add_obj.extra_key)

                if bin_capacity_node == None:
                    insert_new_bin_cap_node = Node(bin_id_node_to_add_obj.extra_key)
                    insert_new_bin_cap_node.item = AVLTree()
                    insert_id_node_in_new_capacity_node_1 = Node(extra_key_of_bin_id)
                    insert_new_bin_cap_node.item.insert_node(insert_id_node_in_new_capacity_node_1)
                    self.gcms_tree_for_bin_capacity.insert_node(insert_new_bin_cap_node)
                else:
                    insert_id_node_in_capacity_node_2 = Node(extra_key_of_bin_id)
                    bin_capacity_node.item.insert_node(insert_id_node_in_capacity_node_2)

                # gcms_tree_for_object_id
                object_node_for_object_tree = Node(object_id)
                object_node_for_object_tree.item = Object(object_id,object_size,color,bin_id_node.key)
                self.gcms_tree_for_object_id.insert_node(object_node_for_object_tree)

    def delete_object(self, object_id):
        object_node = self.gcms_tree_for_object_id.key_search(self.gcms_tree_for_object_id.root,object_id)
        if object_node == None:
            return None
        bin_id_for_given_object = object_node.item.bin_id
        object_size_for_given_object = object_node.item.size

        # gcms_tree_for_id
        bin_id_node_to_delete_object = self.gcms_tree_for_bin_id.key_search(self.gcms_tree_for_bin_id.root,bin_id_for_given_object)
        bin_id_node_to_delete_object.item.remove_object(object_id)
        initial_bin_size = bin_id_node_to_delete_object.extra_key
        bin_id_node_to_delete_object.extra_key += object_size_for_given_object

        # gcms_tree_for_bin_capacity
        bin_cap_node = self.gcms_tree_for_bin_capacity.key_search(self.gcms_tree_for_bin_capacity.root,initial_bin_size)
        bin_cap_node.item.delete_node(Node(bin_id_for_given_object))

        if bin_cap_node.item.root == None:
            self.gcms_tree_for_bin_capacity.delete_node(Node(bin_cap_node.key))
                
        bin_capacity_node = self.gcms_tree_for_bin_capacity.key_search(self.gcms_tree_for_bin_capacity.root,bin_id_node_to_delete_object.extra_key)

        if bin_capacity_node == None:
            insert_new_bin_cap_node = Node(bin_id_node_to_delete_object.extra_key)
            insert_new_bin_cap_node.item = AVLTree()
            insert_id_node_in_new_capacity_node_1 = Node(bin_id_for_given_object)
            insert_new_bin_cap_node.item.insert_node(insert_id_node_in_new_capacity_node_1)
            self.gcms_tree_for_bin_capacity.insert_node(insert_new_bin_cap_node)
        else:
            insert_id_node_in_capacity_node_2 = Node(bin_id_for_given_object)
            bin_capacity_node.item.insert_node(insert_id_node_in_capacity_node_2)

        # gcms_tree_for_object_id
        self.gcms_tree_for_object_id.delete_node(object_node)

        # Implement logic to remove an object from its bin
        pass

    def bin_info(self, bin_id):
        obj_list = []
        def Inorder_bin_info(node):
            if node is None:
                return
            Inorder_bin_info(node.left)
            obj_list.append(node.key)
            Inorder_bin_info(node.right)
        
        bin_id_node = self.gcms_tree_for_bin_id.key_search(self.gcms_tree_for_bin_id.root,bin_id)
        object_node = bin_id_node.item.object_tree_inside_bin.root
        Inorder_bin_info(object_node)
        return (bin_id_node.extra_key,obj_list)
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        pass

    def object_info(self, object_id):
        node_of_object_id = self.gcms_tree_for_object_id.key_search(self.gcms_tree_for_object_id.root,object_id)
        if node_of_object_id == None:
            return None
        bin_id = node_of_object_id.item.bin_id
        return bin_id
        # returns the bin_id in which the object is stored
        pass

