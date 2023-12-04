from utility import get_input_data

data = get_input_data()

parsed_data = []

final_sum = 0

for line_idx, line in enumerate(data):
    is_Good = False
    current_number = 0
    for elem_idx, elem in enumerate(line):
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
        else:
            if current_number != 0:
                print(current_number, is_Good)
                if is_Good:
                    #print(current_number)
                    final_sum+= current_number
                is_Good = False
                current_number = 0 
    if current_number != 0:
        if is_Good:
            print(current_number)
            final_sum+= current_number
        is_Good = False
        current_number = 0        

print(final_sum)