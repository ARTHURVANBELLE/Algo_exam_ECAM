def safety_check_2(lines: list[list[int]]) -> int:
    """
    Analyzes a list of number sequences to find which sequences can become valid after removing
    exactly one number. A valid sequence must be either strictly increasing or decreasing
    with differences between consecutive numbers in the range [1,3].
    
    Time Complexity: O(n * m^2) where:
    - n is the number of lines/sequences
    - m is the length of each sequence
    The complexity comes from:
    - Iterating through each line O(n)
    - For each line, trying each possible deletion O(m)
    - For each deletion, checking if sequence is valid O(m)
    
    Args:
        lines (list[list[int]]): List of sequences to check, each sequence is a list of integers
        
    Returns:
        int: Count of sequences that can become valid after removing exactly one number
    """
    count = 0

    for line in lines:
        # Try removing each number once
        for i in range(len(line)):
            # Create new sequence without the number at position i
            temp_line = line[:i] + line[i+1:]
            
            # Check if sequence is valid increasing (differences between 1-3)
            increasing = all((temp_line[i] - temp_line[i - 1]) in {1, 2, 3} 
                           for i in range(1, len(temp_line)))
            
            # Check if sequence is valid decreasing (differences between 1-3)
            decreasing = all((temp_line[i - 1] - temp_line[i]) in {1, 2, 3} 
                           for i in range(1, len(temp_line)))
            
            # If either condition is met, count this sequence and move to next
            if increasing or decreasing:
                count += 1
                break  # Found a valid deletion, no need to check others

    return count

# Read and parse input file
with open('input/input_day_2.txt', 'r') as file:
    rawlines = file.readlines()

# Convert input strings to lists of integers
lines = [[int(num) for num in line.strip().split()] for line in rawlines]

# Calculate and print result
print(safety_check_2(lines))