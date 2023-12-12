from utility import get_input_data
import math

data = get_input_data()

points = 0

dict_cards = {x:0 for x in range(len(data))}

for cnt, line in enumerate (data):
    dict_cards[cnt] += 1
    winners = [x for x in line.split(':')[-1].split('|')[0].strip().split(' ') if x != '']
    choices = [x for x in line.split(':')[-1].split('|')[-1].strip().split(' ') if x != '']
    common_count = len(set(choices).intersection(set(winners)))
    #part 1
    #if common_count != 0:
    #    points += math.pow(2,common_count-1)
    #part 2
    for _ in range(dict_cards[cnt]):
        for x in range(1,common_count+1):
            dict_cards[cnt+x]+=1
    
    
#print(points)
print (sum(list(dict_cards.values())))