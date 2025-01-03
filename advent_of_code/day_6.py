import pandas as pd

def check_next_position(direction: int, new_position: list, position: list, count: int) -> tuple[int, list, int]:
    """
    Checks if the next position is valid and updates the direction and count accordingly.
    
    Time Complexity: O(1) - constant time operations
        
    Returns:
        tuple: (new_direction, next_position, updated_count)
    """
    if (new_position[0] > (len(room) - 1) or 
        new_position[1] > (len(room[0]) - 1) or 
        new_position[0] < 0 or 
        new_position[1] < 0):  # Out of bounds
        return -1, position, count
    elif room[new_position[0]][new_position[1]] == "#":  # Wall detected
        direction = (direction + 1) % 4  # Turn clockwise
        return direction, position, count
    else:
        if room[position[0]][position[1]] != "X":  # Mark visited if not already
            count += 1
        room[position[0]][position[1]] = "X"  # Mark current position as visited
        return direction, new_position, count

def guard_walk(direction: int, position: list) -> int:
    """
    Simulates guard walking through maze following right-hand wall rule.
    
    Time Complexity: O(m*n) where:
    - m is maze height
    - n is maze width
    Each cell can only be visited once.
    
    Args:
        direction (int): Initial direction (0=right, 1=down, 2=left, 3=up)
        position (list): Starting position [row, col]
        
    Returns:
        int: Total number of cells visited
    """
    count = 1  # Start counting from the first position
    
    while True:
        # Calculate new position based on direction
        new_position = [
            position[0] + (direction == 1) - (direction == 3),  # row adjustment
            position[1] + (direction == 0) - (direction == 2)   # column adjustment
        ]

        # Check the next position
        direction, new_position, count = check_next_position(direction, new_position, position, count)

        # Exit if out of bounds
        if direction == -1:
            print(f"Finished walking. Total count: {count}")
            return count

        position = new_position

def find_guard(room: list) -> tuple[list, int]:
    """
    Locates guard in maze and determines initial direction.
    
    Time Complexity: O(m*n) where m is maze height, n is maze width
    
    Args:
        room (list): 2D maze representation
        
    Returns:
        tuple: ([row, col], direction) or None if guard not found
    """
    direction_map = {
        'v': 1,  # down
        '^': 3,  # up
        '<': 2,  # left
        '>': 0   # right
    }
    
    for i in range(len(room)):
        for j in range(len(room[0])):
            if room[i][j] in direction_map:
                return [i, j], direction_map[room[i][j]]
    return None

# Read input file
with open('input/input_day_6.txt', 'r') as file:
    rawlines = file.readlines()

# Initialize maze
room = [[char for char in line.strip()] for line in rawlines]

# Find guard and start walking
position, direction = find_guard(room)
guard_walk(direction, position)