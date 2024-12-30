import pandas as pd

with open('input/input_day_6.txt', 'r') as file:
    rawlines = file.readlines()

room = [[char for char in line.strip()] for line in rawlines]

# position = [row, column]
def check_next_position(direction: int, new_position: list, position: list, count: int):
    if (new_position[0] > (len(room) - 1) or 
        new_position[1] > (len(room[0]) - 1) or 
        new_position[0] < 0 or 
        new_position[1] < 0):  # Out of bounds
        return -1, position, count
    elif room[new_position[0]][new_position[1]] == "#":  # Wall detected
        direction += 1  # Turn clockwise
        if direction > 3:
            direction = 0
        return direction, position, count
    else:
        if room[position[0]][position[1]] != "X":  # Mark visited if not already
            count += 1
        room[position[0]][position[1]] = "X"  # Mark current position as visited
        return direction, new_position, count

def guard_walk(direction: int, position: list):
    count = 1  # Start counting from the first position
    while True:
        # Determine the new position based on the direction
        if direction == 0:  # Go right
            new_position = [position[0], position[1] + 1]
        elif direction == 1:  # Go down
            new_position = [position[0] + 1, position[1]]
        elif direction == 2:  # Go left
            new_position = [position[0], position[1] - 1]
        elif direction == 3:  # Go up
            new_position = [position[0] - 1, position[1]]

        # Check the next position
        direction, new_position, count = check_next_position(direction, new_position, position, count)

        # If the guard has reached a stopping condition, exit the loop
        if direction == -1:
            print(f"Finished walking. Total count: {count}")
            return count

        # Update the position for the next iteration
        position = new_position

def find_guard(room: list):
    for i in range(len(room)):
        for j in range(len(room[0])):
            if room[i][j] not in [".", "#", "X"]:  # Find guard symbol
                if room[i][j] == "v":
                    return [i, j], 1
                if room[i][j] == "^":
                    return [i, j], 3
                if room[i][j] == "<":
                    return [i, j], 2
                if room[i][j] == ">":
                    return [i, j], 0
    return None

# Find the guard's initial position and direction
position, direction = find_guard(room)
guard_walk(direction, position)