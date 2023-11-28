from utilities import get_input_data

data = get_input_data()

commands = []
commands_flag = False

dict_order = {str(x):[] for x in range(1, int(len(data[0])/4)+1)}

for line in data:
    if line == '\n':
        commands_flag = True
        continue
    if commands_flag:
        line = line.strip()
        commands.append([line.split(' ')[1], line.split(' ')[3], line.split(' ')[5]])
    else:
        key_count = 0
        for count in range(0, len(line[:-2]), 4):
            if line[count] == '[':
                dict_order[str(key_count+1)].append(line[count+1])
            key_count+=1

print(dict_order)
print(commands)

for command in commands:
    int_stack = []
    for element in range(int(command[0])):
        #dict_order[command[2]].insert(0, dict_order[command[1]].pop(0)) pt 1
        int_stack.append(dict_order[command[1]].pop(0))
    dict_order[command[2]] = int_stack+dict_order[command[2]]

final_string = ''
        
for key in dict_order.keys():
    final_string+= dict_order[key][0]
    
print(final_string)
        