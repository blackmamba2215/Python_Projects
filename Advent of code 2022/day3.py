from utilities import get_input_data

input_Data = get_input_data()

score = 0

#pt1
'''
for line in input_Data:
    line = line.strip()
    common = list(set(line[:int(len(line)/2)]).intersection(set(line[int(len(line)/2):])))[0]
    score+=ord(common)-ord('a')+1 if not common.isupper() else ord(common)-ord('A')+27
'''
    
#pt2

for line_cnt in range(0, len(input_Data)-2, 3):
    common_int = set(input_Data[line_cnt].strip()).intersection(set(input_Data[line_cnt+1].strip()))
    common = list(common_int.intersection(set(input_Data[line_cnt+2].strip())))[0]
    score+=ord(common)-ord('a')+1 if not common.isupper() else ord(common)-ord('A')+27
    
print(score)