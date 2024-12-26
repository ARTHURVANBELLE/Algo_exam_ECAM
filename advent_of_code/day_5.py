import pandas as pd

with open('input/input_day_5.txt', 'r') as file:
    rawtxt = file.read()

def separate(rawtxt):
    lines = pd.Series([line for line in rawtxt.split("\n") if line])
    split_index = lines.str.contains(",").idxmax() if lines.str.contains(",").any() else len(lines)
    
    couples = {int(line.split("|")[1]): [] for line in lines[:split_index]}
    for line in lines[:split_index]:
        couples[int(line.split("|")[1])].append(int(line.split("|")[0]))
        
    updates = [list(map(int, line.split(","))) for line in lines[split_index:]]
    
    return couples, updates

couples, updates = separate(rawtxt)

def update(couples, updates):
    total = 0
                    
    def get_middle_update(update_list):
        return update_list[len(update_list) // 2]
                    
    def valid_update(update):
        for i in range(len(update)):
            end = update[i+1:]
            if update[i] in couples.keys():
                if len(list(set(couples[update[i]]) & set(end))) > 0:
                    return 0
            
        return get_middle_update(update)
    
    for update in updates:
        total += valid_update(update)
    
    return total
        
print (update(couples, updates))

