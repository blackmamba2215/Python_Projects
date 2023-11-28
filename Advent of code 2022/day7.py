from utilities import get_input_data

data = get_input_data()

'''class folder():
    def __init__ (self, name):
        self.name = name
        self.children = []
        self.size = 0
        self.parent = None
        self.item_added = False
    
    def add_content(self, value):
        self.size+=value
        
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def update_size_from_children(self):
        for child in self.children:
            self.size+=child.size
  
def get_folder_by_name(name, folder_list):
    for folder in folder_list:
        if folder.name == name:
            return folder
    
root_folder = folder('root')
folder_array = [root_folder]
list_of_all_folders = [root_folder]

for line in data:
    line = line.strip()
    if line.startswith('$'):
        command = line.split(' ')[1]
        if command == 'cd':
            if line.split(' ')[2] == '/':
                folder_array = [root_folder]
            elif line.split(' ')[2] == '..':
                folder_array.pop()
            else:
                folder_array.append(get_folder_by_name(line.split(' ')[2], list_of_all_folders))
    elif line.startswith('dir'):
        new_folder = folder(line.split(' ')[-1])
        list_of_all_folders.append(new_folder)
        folder_array[-1].add_child(new_folder)
    else:
        folder_array[-1].add_content(int(line.split(' ')[0]))
    
x = 2

def calculate_sum(folder):
    
    folder_sum = sum(calculate_sum(child) for child in folder.children)
    
    return folder.size + folder_sum

folder_cnt = 0
added_folders = []
for folder in list_of_all_folders:
    folder_size = calculate_sum(folder)
    print("Size of {}: {}".format(folder.name, folder_size))
    if calculate_sum(folder) <= 100000:
        if folder.name not in added_folders:
            added_folders.append(folder.name)
            folder_cnt+=calculate_sum(folder)
        else:
            print('Duplicated: {}'.format(folder.name))

print(folder_cnt)

'''
from collections import defaultdict
dict_sizes = defaultdict(int)
path = []
for line in data:
    content = line.strip().split(' ')
    if content[1] == 'cd':
        if content[2] == '..':
            path.pop()
        else:
            path.append(content[2])
    elif content[1] == 'ls':
        continue
    else:
        if content[0] != 'dir':
            for i in range(len(path)+1):
                dict_sizes['/'.join(path[:i])] += int(content[0])
                
size_counter = 0
for key in dict_sizes:
    if dict_sizes[key]<100000:
        size_counter += dict_sizes[key]

print(size_counter)

to_be_deleted = min([x for x in dict_sizes.values() if x > 30000000 - (70000000-dict_sizes['/'])])
print(to_be_deleted)
