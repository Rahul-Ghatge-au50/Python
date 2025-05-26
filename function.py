def get_todos(filepath):
    """ Read the file and get the Todo List"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath):
    """ Write the file and save the Todo List"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)