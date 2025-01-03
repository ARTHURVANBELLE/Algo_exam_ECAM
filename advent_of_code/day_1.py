import sys

sys.setrecursionlimit(3000)

def similarity(left_list, right_list):
    """
    Calculates the similarity score between two lists by finding occurrences of elements
    from the left list in the right list and multiplying them by their values.
    
    The algorithm uses memoization to optimize counting occurrences of elements.
    
    Time Complexity: O(n^2) where n is the length of the input lists
    - The recursive calls create O(n) stack frames
    - For each recursive call, we potentially need to count occurrences in right_list O(n)
    - Memoization helps by storing counts, but first-time calculations still need full traversal
    
    Args:
        left_list (List[int]): First list of integers
        right_list (List[int]): Second list of integers to search in
        
    Returns:
        int: Sum of (value × occurrence count) for each element in left_list
    """
    occurrence_dict = {}
    
    def occurrence(searched_list, item):
        """
        Counts occurrences of an item in the searched_list, using memoization (like in cache)
        to avoid recounting for previously seen items.
        
        Args:
            searched_list (List[int]): List to search in
            item (int): Item to count
            
        Returns:
            int: Number of occurrences multiplied by the item value
        """
        if item not in occurrence_dict:
            occurrence_dict[item] = searched_list.count(item)
        return occurrence_dict[item] * item
    
    if not left_list or not right_list:
        return 0
    
    return similarity(left_list[1:], right_list) + occurrence(right_list, left_list[0])

# Read input file and create two lists from space-separated values
with open('input/input_day_1.txt', 'r') as file:
    lines = file.readlines()

left_list = []
right_list = []
for line in lines:
    parts = line.strip().split()
    if len(parts) == 2:
        left_list.append(int(parts[0]))
        right_list.append(int(parts[1]))

# Calculate and print the similarity score
print(similarity(left_list, right_list))