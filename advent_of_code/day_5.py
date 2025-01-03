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
    Validates updates against couples relationships and sums middle elements
    of valid updates.
    
    Time Complexity: O(m * n^2) where:
    - m is number of updates
    - n is max length of any update
    The complexity comes from:
    - Processing each update O(m)
    - For each element, checking all following elements O(n^2)
    - Set intersection operations O(n)
    
    Args:
        couples (dict): Dictionary mapping end values to list of start values
        updates (list): List of updates to process
        
    Returns:
        int: Sum of middle elements from valid updates
    """
    total = 0
                    
    def get_middle_update(update_list: list[int]) -> int:
        """Returns middle element of an update list"""
        return update_list[len(update_list) // 2]
                    
    def valid_update(update: list[int]) -> int:
        """
        Checks if update is valid according to couples relationships.
        Returns middle element if valid, 0 if invalid.
        """
        for i in range(len(update)):
            end = update[i+1:]
            if update[i] in couples.keys():
                # Check if any required start elements appear after current element
                if len(list(set(couples[update[i]]) & set(end))) > 0:
                    return 0
            
        return get_middle_update(update)
    
    # Process each update
    for update in updates:
        total += valid_update(update)
    
    return total

# Read and process input
with open('input/input_day_5.txt', 'r') as file:
    rawtxt = file.read()

couples, updates = separate(rawtxt)
print(update(couples, updates))