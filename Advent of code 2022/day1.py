from utilities import get_input_data

input_data = get_input_data()

elfs_counter = []

sum_cnt = 0

for x in input_data:
    if x == '\n':
        elfs_counter.append(sum_cnt)
        sum_cnt = 0
    else:
        sum_cnt+=int(x.strip())

if x != '\n':
    elfs_counter.append(sum_cnt)

elfs_counter.sort()
#print(max(elfs_counter)) # pt1
print(sum(elfs_counter[-3:]))   #pt2