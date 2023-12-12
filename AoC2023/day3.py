from utility import get_input_data

data = get_input_data()

parsed_data = []

final_sum = 0
gear_dict = {}
gear_data = ()

for line_idx, line in enumerate(data):
    if line_idx == 5:
        x = 2
    is_Good = False
    current_number = 0
    for elem_idx, elem in enumerate(line):
        if elem == '8':
            x = 2
        if elem.isdigit():
            current_number = 10*current_number+int(elem)
            for l in [-1,0,1]:
                if line_idx+l<0 or line_idx+l>=len(data):
                    continue
                for c in [-1,0,1]:
                    if elem_idx+c<0 or elem_idx+c>=len(line):
                        continue
                    if not data[line_idx+l][elem_idx+c].isdigit() and data[line_idx+l][elem_idx+c] != '.':
                        is_Good = True
                    if data[line_idx+l][elem_idx+c] == '*':
                        gear_data = (line_idx+l, elem_idx+c)
        else:
            if current_number != 0:
                if gear_data != ():
                    if gear_data not in gear_dict:
                        gear_dict[gear_data] = [current_number]
                    else:
                        gear_dict[gear_data].append(current_number)        
                    gear_data = ()   
                print(current_number, is_Good)
                if is_Good:
                    #print(current_number)
                    final_sum+= current_number
                is_Good = False
                current_number = 0 
    if current_number != 0:
        if gear_data != ():
            if gear_data not in gear_dict:
                gear_dict[gear_data] = [current_number]
            else:
                gear_dict[gear_data].append(current_number)        
            gear_data = ()   
        if is_Good:
            print(current_number)
            final_sum+= current_number
        is_Good = False
        current_number = 0        

total_gear = 0

for key in gear_dict.keys():
    if len(gear_dict[key]) == 2:
        total_gear += gear_dict[key][0]*gear_dict[key][1]
        
print(final_sum)
print(total_gear)