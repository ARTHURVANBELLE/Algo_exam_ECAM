import pandas as pd
import functools

with open('input/input_day_19.txt', 'r') as file:
    rawlines = file.readlines()
    
towels = rawlines[0].strip().split(", ")
designs = [line.strip() for line in rawlines[2:]]

@functools.cache  # Top-level memorization for entire function calls
def fabric(towels: tuple, design: str) -> bool:
    # DP table: stores if each prefix of the design can be made with towels
    is_valid = {}
    
    # Initialize DP table with all prefixes of design
    for i in range(len(design) + 1):
        is_valid[design[:i]] = False
    
    # Base case: empty string can always be made (using no towels)
    is_valid[""] = True

    # Bottom-up DP: build solutions from smaller subproblems
    for subdesign in is_valid:  # For each prefix of the design
        for towel in towels:    # Try each available towel
            # Check if current subdesign ends with this towel
            if subdesign.endswith(towel):
                # Get the remaining pattern by removing this towel
                previous_subdesign = subdesign.removesuffix(towel)
                
                # If remaining pattern is valid, current pattern is valid
                # This is the optimal substructure property
                if is_valid[previous_subdesign]:
                    is_valid[subdesign] = True
                    break  # Found valid solution for this subdesign

    # Final state in DP table gives answer for full design
    return is_valid[design]

# Count valid designs
count = 0
for design in designs:
    if fabric(tuple(towels), design):  # Convert list to tuple for @cache
        count += 1
print("Count: ", count)


# The time complexity is O(N * M * K) where:
#
# N = length of design string
# M = number of towels
# K = average length of towel patterns