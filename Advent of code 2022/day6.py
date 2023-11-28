from utilities import get_input_data

data = get_input_data()[0]

for counter in range(len(data)):
    if len(set(list(data[counter:counter+14]))) == len(data[counter:counter+14]):
        #print (counter+4) pt1
        print (counter+14) #pt2
        break