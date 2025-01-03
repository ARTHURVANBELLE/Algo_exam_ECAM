import pandas as pd

def separate(rawtxt: str) -> tuple[dict[int, list[int]], list[list[int]]]:
    """
    Returns:
        tuple: (couples dict mapping end to list of starts, list of updates)
    """
    lines = pd.Series([line for line in rawtxt.split("\n") if line])
    split_index = lines.str.contains(",").idxmax() if lines.str.contains(",").any() else len(lines)
    
    # Create couples dict {end: [start, start, ...]}
    couples = {int(line.split("|")[1]): [] for line in lines[:split_index]}
    for line in lines[:split_index]:
        couples[int(line.split("|")[1])].append(int(line.split("|")[0]))
        
    # Parse updates into list of integer lists
    updates = [list(map(int, line.split(","))) for line in lines[split_index:]]
    
    return couples, updates

def update(couples: dict[int, list[int]], updates: list[list[int]]) -> int:
    """
    Processes updates based on couples relationships using divide-and-conquer approach.
    
    Time Complexity: O(m * n * log n) where:
    - m is number of updates
    - n is max length of any update
    The complexity comes from:
    - Processing each update O(m)
    - Validating each update using divide and conquer O(n * log n)
    - Set intersection operations O(n)
    
    Args:
        couples (dict): Dictionary mapping end values to list of start values
        updates (list): List of updates to process
        
    Returns:
        int: Sum of middle elements from valid updates
    """
    total = 0
                    
    def get_middle_update(update_list: list[int]) -> int:
        """Returns middle element of list or 0 if list has length ≤ 1"""
        if len(update_list) > 1:
            return update_list[len(update_list) // 2]
        return 0
                    
    def invalid_update(update: list[int]) -> list[int]:
        """Checks if update violates couples relationships"""
        for i in range(len(update)):
            end = update[i+1:]
            if update[i] in couples.keys():
                if len(set(couples[update[i]]) & set(end)) > 0:
                    return update
        return []
    
    def validate_update(update: list[int]) -> list[int]:
        """
        Validates and reorders update using divide-and-conquer approach
        to maintain couples relationships
        """
        # Base case
        if len(update) < 2:
            return update
        
        # Divide
        n = len(update)
        start = validate_update(update[:n // 2])
        end = validate_update(update[n // 2:])
        
        # Conquer
        output = []
        while start and end:
            if start[0] in couples.keys():
                # Place start[0] if end[0] isn't required to be before it
                output += [start.pop(0) if (end[0] not in couples[start[0]]) else end.pop(0)]
            else:
                # If start[0] isn't in couples, it can be placed anywhere
                output.insert(0, start.pop(0))
                
        return output + start + end
    
    # Process each update
    for update in updates:
        if len(invalid_update(update)) > 1:
            total += get_middle_update(validate_update(update))
        
    return total

# Read and process input
with open('input/input_day_5.txt', 'r') as file:
    rawtxt = file.read()

couples, updates = separate(rawtxt)
print(update(couples, updates))