import re

with open('input/input_day_3.txt', 'r') as file:
    rawtxt = file.read()

def compute_mul(multxt):

    if len(multxt.split(",")) == 2:
        val1 = multxt.split(",")[0].strip(')')
        val2 = multxt.split(",")[1].strip(')')

        if val1.isnumeric() and val2.isnumeric():
            return int(val1) * int(val2)

    return 0
        

def uncorrupt(rawtxt):
    total = 0
    enable = True

    if not rawtxt:
        return 0

    for i in range(len(rawtxt)):
        if rawtxt[i:i + 4]== "do()":
            enable = True
        elif rawtxt[i:i + 7]== "don't()":
            enable = False
        
        if (rawtxt[i:i + 4]== "mul(") and enable:

            for j in range(i + 5, i + 12):
                if rawtxt[j] == ")":
                    total += compute_mul(rawtxt[i+4:j])
                    
                if not(rawtxt[j].isnumeric() or rawtxt[j] == "(" or rawtxt[j] == ","):
                    break
    return total

print(uncorrupt(rawtxt))