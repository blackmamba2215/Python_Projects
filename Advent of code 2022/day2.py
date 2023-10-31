from utilities import get_input_data

input_Data = get_input_data()

score = 0

for line in input_Data:
    
    opponent = line.strip().split(' ')[0]
    mine = line.strip().split(' ')[1]
    '''
    pt1
    if ord(mine) - ord(opponent) - 23 == 0:
        score += 3
    
    if mine == 'X':
        score += 1
        if opponent == 'C':
            score += 6
    elif mine == 'Y':
        score += 2
        if opponent == 'A':
            score += 6
    else:
        score += 3
        if opponent == 'B':
            score += 6
    '''        
    dWins = {
        'A':'C',
        'B':'A',
        'C':'B'
    }
        
    if mine == 'X':
        score += ord(dWins[opponent])-ord('A')+1
    elif mine == 'Y':
        score += 3+ord(opponent)-ord('A')+1
    else:
        score += 6 + ord(list(dWins.keys())[list(dWins.values()).index(opponent)])-ord('A')+1

    
print(score)
    
    
    
    