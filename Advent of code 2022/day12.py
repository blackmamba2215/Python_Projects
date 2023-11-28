from utilities import get_input_data
from collections import deque

data = get_input_data()

table = []

for line_cnt, line in enumerate(data):
    line = list(line.strip())
    for col_cnt, letter in enumerate(line):
        if letter == 'E':
            line[col_cnt] = 'z'
            start_coord = [line_cnt, col_cnt]
    table.append(line)

queue = deque()
queue.append((0, start_coord[0], start_coord[1]))
checked = {(start_coord[0], start_coord[1])}

while queue:
    dist, row, col = queue.popleft()
    print(row, col, table[row][col], dist)
    for r,c in [[row+1,col], [row-1,col], [row, col+1], [row, col-1]]:
        if r<0 or c<0 or r>=len(table) or c>=len(table[0]):
            continue
        if (r,c) in checked:
            continue
        
        if ord(table[row][col])-ord(table[r][c]) > 1:
            continue
        
        if table[r][c] == 'a':
            print(dist+1)
            exit(0)
        
        checked.add((r,c))
        queue.append((dist+1, r, c))
        
        
