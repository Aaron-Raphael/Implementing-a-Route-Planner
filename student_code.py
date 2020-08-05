import math
from helpers import show_map


def shortest_path(M,start,goal):
    print("shortest path called")
    
    cost_path = { 0 : ([start] , 0) } # { f_value(float : (path(list) , g_value till last node(float) ) }
    
    goal_cost_path = {} #{ f_value : path(list)
        
    while len(cost_path) > 0:  
        
        min_cost_node = min(cost_path)
        
        c_cost_path =(min_cost_node , cost_path.pop(min_cost_node)) # (cost, (path, g_val))
        
        c_path = (c_cost_path[1][0])
        c_node = (c_cost_path[1][0])[-1]
        g_val = (c_cost_path[1][1])
        
        o_g_val = g_val
        
        # check if goal is the start
        if c_node == goal:
            print('Already in goal')
            eff_path = [c_node]
            
            print('efficient_path: ', eff_path)
            show_map(M, start = start, goal = goal, path = eff_path)
            return eff_path
            
            break        

        # Iterate over all available nodes for the current node
        for a_node in M.roads[c_node]:
            
            # check the node is not int previous node
            if a_node not in c_path:

                # Check if the node is the goal node
                if a_node == goal:
                    
                    up_a_path = c_path+ [a_node]
                    
                    
                    up_g_val = o_g_val + get_distance(M.intersections[c_node] , M.intersections[a_node])
                    
                    up_a_cost = up_g_val
                    
                    goal_cost_path[up_a_cost] = (up_a_path , up_g_val)

                # if the node is not the goal node
                if a_node != goal:
                    
                    up_a_path = c_path+ [a_node]

                    up_g_val = o_g_val + get_distance(M.intersections[c_node] , M.intersections[a_node])
                    up_h_val = get_distance(M.intersections[a_node] , M.intersections[goal])

                    up_a_cost = up_g_val + up_h_val
                    
                    # check if there are any available paths to the goal
                    if len(goal_cost_path) == 0:
                        cost_path[up_a_cost] = (up_a_path , up_g_val)
                    
                    # If paths to the goal exists 
                    if len(goal_cost_path)>0:
                        # Proceed only if the f_value is less than the f_value of the goal path
                        if up_a_cost < o_g_val:
                            cost_path[up_a_cost] = (up_a_path , up_g_val)

        
    # Efficient path is the one with minimum f_value
    eff_path = (goal_cost_path[min(goal_cost_path)][0])   
    
    print('efficient_path: ', eff_path)
    show_map(M, start = start, goal = goal, path = eff_path)
  
    return eff_path
                  
                 
def get_distance(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))