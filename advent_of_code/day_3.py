def compute_mul(multxt: str) -> int:
    """
    Computes multiplication of two comma-separated numbers from a string.
    
    Args:
        multxt (str): String containing two numbers separated by comma
        
    Returns:
        int: Product of the two numbers if valid format, 0 otherwise
    """
    if len(multxt.split(",")) == 2:
        val1 = multxt.split(",")[0].strip(')')
        val2 = multxt.split(",")[1].strip(')')

        if val1.isnumeric() and val2.isnumeric():
            return int(val1) * int(val2)

    return 0

def uncorrupt(rawtxt: str) -> int:
    """
    Process a text string containing special commands and multiplication operations.
    Calculates sum of all valid multiplication results when enabled.
    
    Time Complexity: O(n*m) where:
    - n is the length of the input text
    - m is the max length of multiplication operation (bounded by 12 in this case)
    
    Args:
        rawtxt (str): Input text containing commands and operations
        
    Returns:
        int: Sum of all valid multiplication results
    """
    total = 0
    enable = True

    if not rawtxt:
        return 0

    for i in range(len(rawtxt)):
        # Check for enable/disable commands
        if rawtxt[i:i + 4] == "do()":
            enable = True
        elif rawtxt[i:i + 7] == "don't()":
            enable = False
        
        # Process multiplication when enabled
        if (rawtxt[i:i + 4] == "mul(") and enable:
            # Look ahead max 12 characters for closing parenthesis
            for j in range(i + 5, i + 12):
                if rawtxt[j] == ")":
                    total += compute_mul(rawtxt[i+4:j])
                    
                # Break if invalid character encountered
                if not(rawtxt[j].isnumeric() or rawtxt[j] == "(" or rawtxt[j] == ","):
                    break
    return total

# Read input file
with open('input/input_day_3.txt', 'r') as file:
    rawtxt = file.read()

# Calculate and print result
print(uncorrupt(rawtxt))