import os

def get_input_data():
    '''
    returns a list of lines content from the input file
    '''
    project_root = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(project_root, 'input.txt'), 'r') as file:
        lines = file.readlines()

    content = [line.strip() for line in lines]
        
    return content