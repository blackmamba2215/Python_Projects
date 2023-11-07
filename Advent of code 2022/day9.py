from utilities import get_input_data
from copy import deepcopy

data = get_input_data()

rope = [[0,0] for _ in range(10)]

tail_positions = []

for line in data:
    line = line.strip()
    #print(line)
    #Pt1
    '''for positions in range(1, int(line.split(' ')[-1])+1):
        if line[0] == 'R':
            H[0]+=1
        elif line[0] == 'L':
            H[0]-=1
        elif line[0] == 'U':
            H[1]+=1
        else:
            H[1]-=1
        for index in range(2):
            if H[abs(index-1)]==T[abs(index-1)] and H[index]!=T[index]:
                if abs(H[index]-T[index])==2:
                    T[index] = T[index]+1 if H[index]>T[index] else T[index]-1
            elif H[abs(index-1)]==T[abs(index-1)] and H[index]==T[index]:
                pass
            else:
                if abs(H[index]-T[index])==2:
                    T[abs(index-1)]=H[abs(index-1)]
                    T[index] = T[index]+1 if H[index]>T[index] else T[index]-1
        copy_T = deepcopy(T)
        if copy_T not in tail_positions:
            tail_positions.append(copy_T)
        #print('H:{}; T:{}'.format(H,T))'''

    for positions in range(1, int(line.split(' ')[-1])+1):
        for knot_count, knot in enumerate(rope):
            if knot_count == 0:
                if line[0] == 'R':
                    knot[0]+=1
                elif line[0] == 'L':
                    knot[0]-=1
                elif line[0] == 'U':
                    knot[1]+=1
                else:
                    knot[1]-=1
            else:
                for index in range(2):
                    if rope[knot_count-1][abs(index-1)]==knot[abs(index-1)] and rope[knot_count-1][index]!=knot[index]:
                        if abs(rope[knot_count-1][index]-knot[index])==2:
                            knot[index] = knot[index]+1 if rope[knot_count-1][index]>knot[index] else knot[index]-1
                    elif rope[knot_count-1][abs(index-1)]==knot[abs(index-1)] and rope[knot_count-1][index]==knot[index]:
                        pass
                    else:
                        if abs(rope[knot_count-1][index]-knot[index])==2:
                            knot[abs(index-1)]=knot[abs(index-1)]+1 if rope[knot_count-1][abs(index-1)]>knot[abs(index-1)] else knot[abs(index-1)]-1
                            knot[index] = knot[index]+1 if rope[knot_count-1][index]>knot[index] else knot[index]-1

        #print(rope)
    
        x = deepcopy(rope[-1])
        if x not in tail_positions:
            tail_positions.append(x)

print()
print(tail_positions)
print(len(tail_positions))
            