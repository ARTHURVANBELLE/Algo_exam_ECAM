
import numpy as np

def shortest_path_bfs_2(filepath):
    # Read the file and parse coordinates
    with open(filepath, 'r') as file:
        rawlines = file.readlines()

    # Convert each line to a list of coordinates
    coordinates = [[int(num) for num in line.strip().split(',')] for line in rawlines]

    # Determine grid size and corrupted length
    size = 71
    corrupted_length = 1024
    if len(coordinates) == 25:  # Test input
        size = 7
        corrupted_length = 12

    # Initialize the grid with zeros
    grid = np.zeros((size, size), dtype=int)

    # Mark corrupted positions as 1
    for x, y in coordinates[:corrupted_length]:
        grid[y, x] = 1

    # BFS to find the shortest path
    start = (0, 0)
    end = (size - 1, size - 1)

    if grid[start[1], start[0]] == 1 or grid[end[1], end[0]] == 1:
        return -1  # Start or end point is blocked

    queue = [(start, 0)]  # (current_position, path_length)
    seen = set()

    while queue:
        pos, length = queue.pop(0)
        if pos == end:  # Reached the destination
            return length
        if pos in seen:  # Skip already visited positions
            continue
        seen.add(pos)

        x, y = pos
        # Explore neighbors
        for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and grid[ny, nx] == 0:
                queue.append(((nx, ny), length + 1))

    return -1  # No path found



filepath = 'input/input_day_18.txt'
result = shortest_path_bfs_2(filepath)
print("Shortest Path Length:", result)
