from utility import get_input_data

data = get_input_data()

dict_data = {}

for line in data:
    line = line.strip()
    id = line.split(':')[0].split(' ')[-1]
    dict_data[id] = {'red':[], 'blue':[], 'green':[]}
    rounds = line.split(':')[1].split(';')
    for round in rounds:
        round = round.replace(',','').strip()
        round_items = round.split(' ')
        for color in dict_data[id].keys():
            if color in round_items:
                dict_data[id][color].append(int(round_items [round_items.index(color)-1]))
            else:
                dict_data[id][color].append(0)

output = 0
'''
pt1
for key in dict_data.keys():
    if max(dict_data[key]['red'])<=12 and max(dict_data[key]['green'])<=13 and max(dict_data[key]['blue'])<=14:
        output +=  int(key)
'''

for key in dict_data.keys():
    game_score = max(dict_data[key]['red'])*max(dict_data[key]['green'])*max(dict_data[key]['blue'])
    output += game_score

print (output)