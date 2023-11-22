from utilities import get_input_data

data = get_input_data()

cycle_count = 0
value_count = 1
final_values = 0

sprite = '###'+'.'*38
print('OldSpr:{}'.format(sprite))
CRT = []
actual_CRT = ''
for line in data:
    line = line.strip()
    #pt1
    '''cycle_count += 1
    if cycle_count in [20,60,100,140,180,220]:
        print('cycle:{}; value:{}'.format(cycle_count, value_count))
        final_values+= cycle_count*value_count  
    if line.split(' ')[0] == 'addx':
        cycle_count += 1
        if cycle_count in [20,60,100,140,180,220]:
            print('cycle:{}; value:{}'.format(cycle_count, value_count))
            final_values+= cycle_count*value_count
        value_count += int(line.split(' ')[-1])'''
    #pt2
    
    if len(actual_CRT) >= 40:
        CRT.append(actual_CRT)
        actual_CRT = ''
    cycle_count = (cycle_count+1)%40
    actual_CRT = actual_CRT+'#' if sprite[(cycle_count-1)%40] == '#' else actual_CRT+' '
    if len(actual_CRT) >= 40:
        CRT.append(actual_CRT)
        actual_CRT = ''
    if line.split(' ')[0] == 'addx':
        cycle_count = (cycle_count+1)%40
        actual_CRT = actual_CRT+'#' if sprite[(cycle_count-1)%40] == '#' else actual_CRT+' '
        if len(actual_CRT) >= 40:
            CRT.append(actual_CRT)
            actual_CRT = ''
        value_count += int(line.split(' ')[-1])
        sprite = '.'*(value_count%40-1)+'###'+'.'*(38-value_count%40)
    print('CRT:   {}'.format(actual_CRT))
    print('Sprite:{}'.format(sprite))
       

for line in CRT:
    print(line)