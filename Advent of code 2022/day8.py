from utilities import get_input_data

data = get_input_data()
matrix = []
for line in data:
    matrix.append(list(line.strip()))
    
#visible_trees = 0
routes = []

for line_cnt, line in enumerate (matrix):
    for col_cnt, tree in enumerate (line):
        tree = int(tree)
        
        '''#if tree != 0:
        if line_cnt == 0 or line_cnt == len(matrix)-1:
            visible_trees += 1
        elif col_cnt == 0 or col_cnt == len(line)-1:
            visible_trees += 1
        else:
            left_max = int(max(line[:col_cnt]))
            right_max = int(max(line[col_cnt+1:]))
            top_max = int(max([x[col_cnt] for x in matrix[:line_cnt]]))
            bottom_max = int(max([x[col_cnt] for x in matrix[line_cnt+1:]]))


            if tree > min([left_max, right_max, top_max, bottom_max]):
                visible_trees+=1'''

        if line_cnt not in [0, len(matrix)-1] and col_cnt not in [0, len(line)-1]:
            
            tree_score = 1
            left = line[:col_cnt][::-1]
            right = line[col_cnt+1:]
            top = [x[col_cnt] for x in matrix[:line_cnt]][::-1]
            bottom = [x[col_cnt] for x in matrix[line_cnt+1:]]
            
            for side in [left, right, top, bottom]:
                side_counter = 0
                for element in side:
                    if int(element) < tree:
                        side_counter+=1
                    elif int(element) >= tree:
                        side_counter+=1
                        break
                tree_score*=side_counter
                
            routes.append(tree_score)
        
print(max(routes))
