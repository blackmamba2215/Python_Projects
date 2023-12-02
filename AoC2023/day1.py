from utility import get_input_data
from collections import deque
from re import search

data = get_input_data()

final_sum = 0
indexes = []

to_be_searched = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in data:
    line = line.strip()
    new_string = ''
    for i in range(len(line)):
        if line[i].isdigit():
            new_string += str(line[i])
            continue
        for element in to_be_searched:
            if line[i:].startswith(element):
                new_string += str(to_be_searched.index(element)+1)
    print(new_string)
    nr = ''.join(x for x in new_string if x.isdigit())
    print(nr)
    final_sum+=int(nr[0]+nr[-1])
print(final_sum)
