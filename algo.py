# You can modify this file to implement your own algorithm

from constants import *

"""
You can use the following values from constants.py to check for the type of cell in the grid:
I = 1 -> Wall 
o = 2 -> Pellet (Small Dot)
e = 3 -> Empty
"""



def get_next_coordinate(grid, location):

    """
    Calculate the next coordinate for 6ix-pac to move to.
    Check if the next coordinate is a valid move.

    Parameters:
    - grid (list of lists): A 2D array representing the game board.
    - location (list): The current location of the 6ix-pac in the form (x, y).

    Returns:
    - list or tuple: 
        - If the next coordinate is valid, return the next coordinate in the form (x, y) or [x,y].
        - If the next coordinate is invalid, return None.
    """
    #define function to check if move is valid
    def is_valid_move(x,y): 
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] in [2, 3]
    
    #define function to get neighbouring moves
    def get_neighbors(x, y):
        neighbors = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y):
                    neighbors.append((new_x, new_y))
        
        return neighbors

    #define function to find nearest pellet
    def bfs(start, target):
        queue = [(start, [])]
        visited = set()
        while queue:
            (x, y), path = queue.pop(0)
            if (x, y) == target:
                return path
            if (x, y) not in visited:
                visited.add((x, y))
                for neighbor in get_neighbors(x, y):
                    queue.append((neighbor, path + [neighbor]))     
        

    # Find the position of all pellets on the grid
    
    pellets = [(x, y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 2]
    
    # If there are no pellets left, return None (Pac-Man has collected them all)
    if not pellets:
        return None

    # Find the closest pellet to Pac-Man's current location
    
    closest_pellet = min(pellets, key=lambda pellet: len(bfs(location, pellet)))
    
    # Find the next move to reach the closest pellet
    path = bfs(location, closest_pellet)
    
    # The next direction is the first move in the path
    if len(path) > 0:
        next_x, next_y = path[0]
        location = [next_x - location[0], next_y - location[1]]
        return path
    else:
        
        location = [14, 7]
        return location
    