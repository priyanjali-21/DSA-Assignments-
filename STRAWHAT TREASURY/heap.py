'''
Python Code to implement a heap with general comparison function
'''

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    def comp_of_crewmate_heap(crew1,crew2):
        if crew1.fake_load <= crew2.fake_load:
            return  True
        return False
    
    def comp_of_dual_heap(val1,val2):
        if val1[0].arrival_time + val1[1] < val2[0].arrival_time + val2[1]:
            return True
        elif val1[0].arrival_time + val1[1] == val2[0].arrival_time + val2[1]:
            return val1[0].id < val2[0].id
        else:
            return False
        
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        self.array = init_array
        self.comparison_function = comparison_function
        
        pass
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.array.append(value)
        self.upheap(len(self.array) -1)

        pass
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.array[0],self.array[len(self.array)-1] = self.array[len(self.array)-1],self.array[0]
        top_element = self.array.pop()
        self.downheap(0)
        return top_element
        pass
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        top_element = self.array[0]
        return top_element
        pass
    
    # You can add more functions if you want to
    
    def upheap(self,k):
        parent_index = (k-1)//2
        if k > 0 and self.comparison_function(self.array[k],self.array[parent_index]):
            self.array[k],self.array[parent_index] = self.array[parent_index],self.array[k] 
            self.upheap(parent_index)
    
    def downheap(self,k):
        if (2*k + 1 < len(self.array)):
            left_index = 2*k + 1
            small_child = left_index
            if (2*k + 2 < len(self.array)):
                right_index = 2*k + 2
                if self.comparison_function(self.array[right_index],self.array[left_index]):
                    small_child = right_index
            if self.comparison_function(self.array[small_child],self.array[k]):
                self.array[k],self.array[small_child] = self.array[small_child],self.array[k]
                self.downheap(small_child)
