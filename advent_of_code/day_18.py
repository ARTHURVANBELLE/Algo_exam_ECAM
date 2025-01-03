import numpy as np

def shortest_path_bfs(filepath: str) -> int:
    """
    Finds the shortest path through a grid from top-left to bottom-right corner,
    avoiding corrupted positions using Breadth-First Search.
    
    Time Complexity: O(V + E) where:
    - V is number of cells in grid (size^2)
    - E is number of possible moves between cells (≤ 4V)
    The BFS explores each reachable cell exactly once.
    
    Args:
        filepath (str): Path to input file containing corrupted coordinates
        
    Returns:
        int: Length of shortest path, or -1 if no path exists
    """
    # Read and parse input file
    with open(filepath, 'r') as file:
        rawlines = file.readlines()
    coordinates = [[int(num) for num in line.strip().split(',')] for line in rawlines]

    # Set grid parameters based on input size
    size = 71  # Default grid size
    corrupted_length = 1024  # Default number of corrupted positions
    if len(coordinates) == 25:  # Test input detection
        size = 7
        corrupted_length = 12

    # Initialize grid and mark corrupted positions
    grid = np.zeros((size, size), dtype=int)
    for x, y in coordinates[:corrupted_length]:
        grid[y, x] = 1

    # Define start and end positions
    start = (0, 0)
    end = (size - 1, size - 1)

    # Check if start or end is blocked
    if grid[start[1], start[0]] == 1 or grid[end[1], end[0]] == 1:
        return -1

    # Initialize BFS
    queue = [(start, 0)]  # (position, path_length)
    seen = set()  # Track visited positions

    # Possible movement directions (up, left, down, right)
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    # BFS implementation
    while queue:
        pos, length = queue.pop(0)
        
        # Check if reached destination
        if pos == end:
            return length
            
        # Skip if position already visited
        if pos in seen:
            continue
            
        seen.add(pos)
        x, y = pos

        # Explore all valid neighboring positions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < size and 0 <= ny < size and 
                grid[ny, nx] == 0 and 
                (nx, ny) not in seen):
                queue.append(((nx, ny), length + 1))

    return -1  # No valid path found

# Read input and find shortest path
filepath = 'input/input_day_18.txt'
result = shortest_path_bfs(filepath)
print("Shortest Path Length:", result)