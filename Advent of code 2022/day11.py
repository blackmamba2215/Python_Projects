from utilities import get_input_data
import math

data = get_input_data()

class Monkey():
    def __init__(self, items, operation, test, if_true, if_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0
        
    def Calculate(self, level):
        
        old = int(level)
        return eval(self.operation)
        
    def process_monkey(self, level):
        #level = self.items.pop(0)
        level = self.Calculate(level)
        if level % self.test == 0:
            index = self.if_true
        else:
            index = self.if_false
        level = math.gcd(level, self.test)
        return level, index
        
        
monkey_array = []

for line in data:
    line = line.strip()
    if line.startswith('Monkey'):
        items = None
        operation = None
        div_number = None
        if_true = None
        if_false = None
    elif line.startswith('Starting'):
        items = line.replace(' ', '').split(':')[-1].split(',')
    elif line.startswith('Operation:'):
        operation = line.split('=')[-1].strip()
    elif line.startswith('Test'):
        div_number = int(line.split(' ')[-1])
    elif line.startswith('If true:'):
        if_true = int(line.split(' ')[-1])
    elif line.startswith('If false:'):
        if_false = int(line.split(' ')[-1])
        monkey_array.append(Monkey(items, operation, div_number, if_true, if_false))
        
for round_count in range(10000):
    print('Round: {}'.format(round_count))
    for counter, monkey in enumerate (monkey_array):
        for item in monkey.items:
            monkey.inspected+=1
            level, index = monkey.process_monkey(item)
            monkey_array[index].items.append(level)
        print ("Monkey {}: {}".format(counter, monkey.inspected))
        monkey.items = []
         
sorted_monkeys = sorted(monkey_array, key = lambda x: x.inspected)

print (sorted_monkeys[-2].inspected*sorted_monkeys[-1].inspected)