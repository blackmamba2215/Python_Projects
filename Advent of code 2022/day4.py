from utilities import get_input_data

input_data = get_input_data()

counter = 0

for line in input_data:
    line = line.strip()
    splitted_line = line.split(',')
    
    elf_1 = list(range(int(splitted_line[0].split('-')[0]), int(splitted_line[0].split('-')[1])+1))
    elf_2 = list(range(int(splitted_line[1].split('-')[0]), int(splitted_line[1].split('-')[1])+1))
    
    #if set(elf_1).issubset(set(elf_2)) or set(elf_2).issubset(set(elf_1)): pt1
    
    if set(elf_1).intersection(set(elf_2))!=set(''):
        counter += 1
        
print(counter)