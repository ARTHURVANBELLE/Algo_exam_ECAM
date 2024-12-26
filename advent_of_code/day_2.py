#this function test every possibility of deletion in the report (max 1 deletion)

def safety_check_2(lines: list[list[int]]) -> int:
    count = 0


    for line in lines:

        for i in range(len(line)):

            temp_line = line[:i] + line[i+1:]

            increasing = all((temp_line[i] - temp_line[i - 1]) in {1, 2, 3} for i in range(1, len(temp_line)))
            decreasing = all((temp_line[i - 1] - temp_line[i]) in {1, 2, 3} for i in range(1, len(temp_line)))

            if increasing or decreasing:
                count += 1
                break  # don't check any further for this line

    return count


with open('input/input_day_2.txt', 'r') as file:
    rawlines = file.readlines()

lines = [[int(num) for num in line.strip().split()] for line in rawlines]

# Call the function and print the result
print(safety_check_2(lines))