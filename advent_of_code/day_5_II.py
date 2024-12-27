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

    # couples dict = {int: [int, int, ...], ...} = {end: [start, start, ...], ...}

def update(couples, updates):
    total = 0
                    
    def get_middle_update(update_list):
        if len(update_list) > 1:
            return update_list[len(update_list) // 2]
        else:
            return 0
                    
    def invalid_update(update):
        for i in range(len(update)):
            end = update[i+1:]
            if update[i] in couples.keys():                             
                if len(set(couples[update[i]]) & set(end)) > 0:  #if the intersection of the two lists is not empty (start element in end list of the update)
                    return update       
        return []
    
    def validate_update(update): 
        # Simple cases
        if len(update) < 2:
            return update
        
        # Divide
        n = len(update)
        start = validate_update(update[:n // 2])
        end = validate_update(update[n // 2:])
        
        # Conquer
        output = []
        while start and end:
            
            #if the first start element is referenced key (to be after in the update)
            if (start[0] in couples.keys()):
                # check if end[0] is not a value that must be placed before start[0]
                output += [start.pop(0) if (end[0] not in couples[start[0]]) else end.pop(0)] 
            # if the first start element is not a referenced key in couples,it means that it can placed before any other element    
            else:
                output.insert(0, start.pop(0))
                
        return output + start + end
    
    for update in updates:
        if len(invalid_update(update)) > 1:
            total += get_middle_update(validate_update(update))
        
    return total

couples, updates = separate(rawtxt)      
print (update(couples, updates))