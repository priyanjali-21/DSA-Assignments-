'''
    This file contains the class definition for the StrawHat class.
'''
from crewmate import *
from heap import *
from treasure import *

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        # Write your code here
        self.global_time = 0

        self.crewmates_array = [CrewMate() for i in range(m)]
        self.crewmates_heap = Heap(Heap.comp_of_crewmate_heap,self.crewmates_array)

        self.all_treasures_array = []
        pass
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        self.global_time = treasure.arrival_time

        self.all_treasures_array.append(treasure)
        
        selected_crewmate = self.crewmates_heap.extract()

        selected_crewmate.fake_load += (treasure.size + treasure.arrival_time)
        selected_crewmate.treasure_array.append(treasure)
        selected_crewmate.timed_array.append(treasure.arrival_time)

        self.crewmates_heap.insert(selected_crewmate)

        pass
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        for crew in self.crewmates_array:

            # If this crewmate has no treasure, we will shift to next crewmate
            if(len(crew.treasure_array) == 0):
                continue
            
            treasure_array = crew.treasure_array #Get the Treasure array of crewMate

            timed_array = crew.timed_array #Get the times of insertion of different treasures
            
            dual_treasure_heap = Heap(Heap.comp_of_dual_heap,[])
            
            for i in range(len(timed_array)):

                treasure = treasure_array[i] 

                if len(dual_treasure_heap.array) == 0:

                    dual_treasure_heap.insert([treasure,treasure.size])
                
                else:
                    selected_treasure_tuple_of_that_crewmate = dual_treasure_heap.top()
                    selected_treasure_tuple_of_that_crewmate[1] -= (treasure.arrival_time - crew.timed_array[i-1])
               
                    if selected_treasure_tuple_of_that_crewmate[1] > 0:
                        dual_treasure_heap.insert([treasure,treasure.size])
                    
                    elif selected_treasure_tuple_of_that_crewmate[1] == 0:
                        selected_treasure_tuple_of_that_crewmate[0].completion_time = treasure.arrival_time
                        dual_treasure_heap.extract()

                        dual_treasure_heap.insert([treasure,treasure.size])
                    
                    else:
                        # Remaining Size before Processing
                        selected_treasure_tuple_of_that_crewmate[1] += (treasure.arrival_time - crew.timed_array[i-1])

                        current_time = crew.timed_array[i-1]
                        remaining_time  = treasure.arrival_time - crew.timed_array[i-1]
                        current_time += selected_treasure_tuple_of_that_crewmate[1]
                        remaining_time -= selected_treasure_tuple_of_that_crewmate[1] 

                        selected_treasure_tuple_of_that_crewmate[0].completion_time = current_time
                        selected_treasure_tuple_of_that_crewmate[1] = 0 
                        
                        dual_treasure_heap.extract()
                        
                        while (len(dual_treasure_heap.array) != 0 and remaining_time>0):
                            newly_selected_treasure = dual_treasure_heap.top()

                            if(newly_selected_treasure[1] > remaining_time):
                                current_time = treasure.arrival_time
                                newly_selected_treasure[1] -= remaining_time
                                remaining_time = 0
                            
                            elif(newly_selected_treasure[1] == remaining_time):
                                current_time = treasure.arrival_time
                                newly_selected_treasure[1] -= remaining_time
                                remaining_time = 0
                                newly_selected_treasure[0].completion_time = current_time
                                dual_treasure_heap.extract()

                            else:
                                current_time += newly_selected_treasure[1]
                                remaining_time -= newly_selected_treasure[1]
                                newly_selected_treasure[1] = 0
                                newly_selected_treasure[0].completion_time = current_time
                                dual_treasure_heap.extract()

                        dual_treasure_heap.insert([treasure,treasure.size])

            current_time = timed_array[-1]

            while(len(dual_treasure_heap.array) != 0):
                newly_selected_treasure = dual_treasure_heap.extract()
                current_time += newly_selected_treasure[1]
                newly_selected_treasure[0].completion_time = current_time

            self.all_treasures_array = sorted(self.all_treasures_array,key = self.get_id)

        return self.all_treasures_array                                                                                                                                 
             
    def get_id(self,obj):
            return obj.id
    