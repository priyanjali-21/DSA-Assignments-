from maze import *
from exception import *
from stack import *

class PacMan:
    def __init__(self, grid : Maze) -> None:
        self.navigator_maze = grid.grid_representation

    def find_path(self, start, end):
        # start and end are 2 element list
        start = list(start)
        end = list(end)
        path = Stack()
        self.priority_order = []
        
        
        grid1 = Maze(len(self.navigator_maze),len(self.navigator_maze[0]))
        for i in range(0,len(self.navigator_maze)):
            for j in range(0,len(self.navigator_maze[0])):
                if self.navigator_maze[i][j] == 1:
                    grid1.add_ghost(i,j)
                
        def is_possible(x : int, y:int) -> bool:
            grid = grid1.grid_representation
            if(x < 0 or x >= len(grid)):
                return False
            elif(y < 0 or y >= len(grid[0])):
                return False
            elif(grid[x][y] == 1):
                 return False
            return True

        if  grid1.is_ghost(start[0],start[1]) or grid1.is_ghost(end[0],end[1]):
            raise PathNotFoundException
        
        path.add_at_last(tuple(start))
        
        while start!=end:
            if (start[0]-end[0]) >= 0 and (start[1] - end[1]) >= 0:
                self.priority_order.append("UL-RD")
                #Up
                if is_possible(start[0] - 1,start[1]):
                    grid1.add_ghost(start[0],start[1])
                    path.add_at_last((start[0] - 1,start[1]))
                    start = [start[0] - 1,start[1]]
                #Left    
                elif is_possible(start[0],start[1]-1):
                    grid1.add_ghost(start[0],start[1])
                    path.add_at_last((start[0],start[1]-1))
                    start = [start[0],start[1]-1]
                #Right
                elif is_possible(start[0],start[1]+1):
                    grid1.add_ghost(start[0],start[1])
                    path.add_at_last((start[0],start[1]+1))
                    start = [start[0],start[1]+1]
                #Down
                elif is_possible(start[0]+1,start[1]):
                    grid1.add_ghost(start[0],start[1])
                    path.add_at_last((start[0]+1,start[1]))
                    start = [start[0]+1,start[1]]
                else:
                    grid1.add_ghost(start[0],start[1])
                    path.remove_at_last()
                    if path.length() != 0 :
                        grid1.remove_ghost(path.top()[0],path.top()[1])
                        start = path.top()
                    else:
                        raise PathNotFoundException
            
            elif (start[0]-end[0]) <= 0 and (start[1] - end[1]) >= 0:
                self.priority_order.append("LD-UR")
                #Left    
                if is_possible(start[0],start[1]-1):
                    grid1.add_ghost(start[0],start[1])
                    path.add_at_last((start[0],start[1]-1))
                    start = [start[0],start[1]-1]
                #Down
                elif is_possible(start[0]+1,start[1]):
                    grid1.add_ghost(start[0],start[1])
                    path.add_at_last((start[0]+1,start[1]))
                    start = [start[0]+1,start[1]]
                #Up
                elif is_possible(start[0] - 1,start[1]):
                    grid1.add_ghost(start[0],start[1])
                    path.add_at_last((start[0] - 1,start[1]))
                    start = [start[0] - 1,start[1]]
                #Right
                elif is_possible(start[0],start[1]+1):
                    grid1.add_ghost(start[0],start[1])
                    path.add_at_last((start[0],start[1]+1))
                    start = [start[0],start[1]+1]
                else:
                    grid1.add_ghost(start[0],start[1])
                    path.remove_at_last()
                    if path.length() != 0 :
                        grid1.remove_ghost(path.top()[0],path.top()[1])
                        start = path.top()
                    else:
                        raise PathNotFoundException
        
            elif (start[0]-end[0]) >= 0 and (start[1] - end[1]) <= 0:
                self.priority_order.append("UR-LD")
                #Up
                if is_possible(start[0] - 1,start[1]):
                    grid1.add_ghost(start[0],start[1])
                    path.add_at_last((start[0] - 1,start[1]))
                    start = [start[0] - 1,start[1]]
                #Right
                elif is_possible(start[0],start[1]+1):
                    grid1.add_ghost(start[0],start[1])
                    path.add_at_last((start[0],start[1]+1))
                    start = [start[0],start[1]+1]
                #Left    
                elif is_possible(start[0],start[1]-1):
                    grid1.add_ghost(start[0],start[1])
                    path.add_at_last((start[0],start[1]-1))
                    start = [start[0],start[1]-1]
                #Down
                elif is_possible(start[0]+1,start[1]):
                    grid1.add_ghost(start[0],start[1])
                    path.add_at_last((start[0]+1,start[1]))
                    start = [start[0]+1,start[1]]
                else:
                    grid1.add_ghost(start[0],start[1])
                    path.remove_at_last()
                    if path.length() != 0 :
                        grid1.remove_ghost(path.top()[0],path.top()[1])
                        start = path.top()
                    else:
                        raise PathNotFoundException
            
            elif (start[0]-end[0]) <= 0 and (start[1] - end[1]) <= 0:
                self.priority_order.append("RD-UL")
                #Right
                if is_possible(start[0],start[1]+1):
                    grid1.add_ghost(start[0],start[1])
                    path.add_at_last((start[0],start[1]+1))
                    start = [start[0],start[1]+1]
                #Down
                elif is_possible(start[0]+1,start[1]):
                    grid1.add_ghost(start[0],start[1])
                    path.add_at_last((start[0]+1,start[1]))
                    start = [start[0]+1,start[1]]
                #Up
                elif is_possible(start[0] - 1,start[1]):
                    grid1.add_ghost(start[0],start[1])
                    path.add_at_last((start[0] - 1,start[1]))
                    start = [start[0] - 1,start[1]]
                #Left    
                elif is_possible(start[0],start[1]-1):
                    grid1.add_ghost(start[0],start[1])
                    path.add_at_last((start[0],start[1]-1))
                    start = [start[0],start[1]-1]
                else:
                    grid1.add_ghost(start[0],start[1])
                    path.remove_at_last()
                    if path.length() != 0 :
                        grid1.remove_ghost(path.top()[0],path.top()[1])
                        start = path.top()
                    else:
                        raise PathNotFoundException
        return path.obj
