import csv
import sys

sys.setrecursionlimit(3000)

# Read the file line by line
with open('input/input_day_1.txt', 'r') as file:
    lines = file.readlines()

left_list = []
right_list = []
for line in lines:
    parts = line.strip().split()
    if len(parts) == 2:
        left_list.append(int(parts[0]))
        right_list.append(int(parts[1]))


def similarity(left_list, right_list):
    occurrence_dict = {}
    def occurrence(searched_list, item):
        if item not in occurrence_dict:
            occurrence_dict[item] = searched_list.count(item)

        return occurrence_dict[item] * item

    
    if not left_list or not right_list :
        return 0
    
    return similarity(left_list[1:], right_list) + occurrence(right_list, left_list[0])

print(similarity(left_list, right_list))
