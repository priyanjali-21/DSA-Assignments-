from node import Node

def comp_1(node_1, node_2): 
    if node_1.key > node_2.key:
        return True
    return False

class AVLTree:
    def __init__(self, compare_function = comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, root, node):
        if not root:
            return node
        elif self.comparator(root,node):
            root.left = self.insert(root.left, node)
        else:
            root.right = self.insert(root.right, node)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and self.comparator(root.left,node):
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.comparator(node,root.right):
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.comparator(node,root.left):
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.comparator(root.right,node):
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, node):
        if not root:
            return root

        if self.comparator(root,node):
            root.left = self.delete(root.left, node)
        elif self.comparator(node,root):
            root.right = self.delete(root.right, node)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.item = temp.item
            root.key = temp.key

            root.right = self.delete(root.right, temp)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current
    
    def max_value_node(self,root):
        current = root
        while current.right:
            current = current.right
        return current

    def key_search(self, root, key_value): # Binary search for key
        if not root or root.key == key_value:
            return root
        if root.key < key_value:
            return self.key_search(root.right, key_value)
        return self.key_search(root.left, key_value)
    
    def node_search(self, root, node): # Binary Search for Node
        if not root or (not self.comparator(root,node) and not self.comparator(node,root)):
            return root
        if self.comparator(node,root):
            return self.node_search(root.right, node)
        return self.node_search(root.left, node)
    
    # <-----COLOUR SEARCHES----->
    # smallest remaining capacity that is still sufficient to hold the item
    def blue_or_yellow_cap_search(self,root,size):
        val = None
        while root:
            if root.key < size:
                root = root.right
            else:
                val = root
                root = root.left
        if val == None:
            return None
        else:
            return val
    # least id
    def blue_search(self,root, size):
        val = None
        while root:
            if root.key < size:
                root = root.right
            else:
                val = root
                root = root.left
        if val == None:
            return None
        else:
            root1 = val.item.root
            while root1.left:
                root1 = root1.left
            return root1
    # greatest id
    def yellow_search(self,root, size):
        val = None
        while root:
            if root.key < size:
                root = root.right
            else:
                val = root
                root = root.left
        if val == None:
            return None
        else:
            root1 = val.item.root
            while root1.right:
                root1 = root1.right
            return root1
    
    # bin with the largest remaining capacity
    def green_or_red_cap_search(self,root,size):
        val = root
        while val.right:
            val = val.right
        if val.key < size:
            return None
        else:
            return val
    # greatest id
    def green_search(self,root,size):
        val = root
        while val.right:
            val = val.right
        if val.key < size:
            return None
        else:
            root1 = val.item.root
            while root1.right:
                root1 = root1.right
            return root1
            
    # least id
    def red_search(self,root,size):
        val = root
        while val.right:
            val = val.right
        if val.key < size:
            return None
        else:
            root1 = val.item.root
            while root1.left:
                root1 = root1.left
            return root1

    def insert_node(self, node):
        self.root = self.insert(self.root, node)
    def delete_node(self, node):
        self.root = self.delete(self.root, node)
