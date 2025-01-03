import pandas as pd
import functools

@functools.cache
def fabric(towels: tuple, design: str) -> bool:
    """
    Determines if a design pattern can be created using a combination of towel patterns
    using dynamic programming with memoization.
    
    Time Complexity: O(N * M * K) where:
    - N = length of design string
    - M = number of towels
    - K = average length of towel patterns
    
    The functools.cache decorator provides memoization for the entire function calls,
    preventing redundant calculations for identical inputs.
    
    Args:
        towels (tuple): Available towel patterns (tuple for hashability)
        design (str): Target design pattern to create
        
    Returns:
        bool: True if design can be created using towels, False otherwise
    """
    # DP table: maps each prefix of the design to its validity
    is_valid = {}
    
    # Initialize DP table with all prefixes of design
    for i in range(len(design) + 1):
        is_valid[design[:i]] = False
    
    # Base case: empty string can always be made
    is_valid[""] = True

    # Bottom-up DP approach
    for subdesign in is_valid:  
        # Try each towel pattern
        for towel in towels:    
            # Check if current subdesign ends with this towel
            if subdesign.endswith(towel):
                # Get remaining pattern after removing towel
                previous_subdesign = subdesign.removesuffix(towel)
                
                # If remaining pattern is valid, current pattern is valid
                if is_valid[previous_subdesign]:
                    is_valid[subdesign] = True
                    break  # Found valid solution, no need to try other towels

    return is_valid[design]

def process_fabric_patterns(input_file: str) -> int:
    """
    Process fabric patterns from input file and count valid designs.
    
    Args:
        input_file (str): Path to input file
        
    Returns:
        int: Number of valid designs
    """
    # Read input file
    with open(input_file, 'r') as file:
        rawlines = file.readlines()
    
    # Parse towels and designs
    towels = rawlines[0].strip().split(", ")
    designs = [line.strip() for line in rawlines[2:]]

    # Count valid designs
    count = 0
    for design in designs:
        if fabric(tuple(towels), design):  # Convert list to tuple for @cache
            count += 1
    return count

# Process input and print result
input_file = 'input/input_day_19.txt'
result = process_fabric_patterns(input_file)
print("Count:", result)