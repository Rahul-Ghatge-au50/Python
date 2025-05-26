
# list are mutable so dont need to assign a variable to list

# todos = []

from function import get_todos, write_todos
import time

todayDate = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", todayDate)

while True:
    user_action = input("Type show ,edit,remove ,add or clear : ")
    user_action = user_action.strip()  # strip() method - change the string and remove the extra space

    # if 'add' in user_action:
    if user_action.startswith('show'):
        # use for error handling
        todos = get_todos('todos.txt')

        # new_todos = [item.strip('\n') for item in todos]  LIST COMPREHENSION

        for index, i in enumerate(todos):  # without enumerate we cant use index keyword in for loop for the numbers
            i = i.strip('\n')
            i = i.title()  # It makes the first word capital
            print(f"{index + 1}-{i}")  # f-strings for modification of the output
    elif user_action.startswith('add') or user_action.startswith('new'):
        user_input = user_action[4:] + "\n"

        # read() readlines() write() writelines() file functions
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()

        todos.append(user_input)

        write_todos(todos, 'todos.txt')

        print('Added Successfully')

    elif user_action.startswith('edit'):
        try:
            num = int(user_action[5:])
            num = num - 1
            new_todo = input('Enter the new Todo : ')

            todos = get_todos('todos.txt')

            todos[num] = new_todo + "\n"

            write_todos(todos, 'todos.txt')
        except ValueError:
            print("Entered Wrong Command")
            continue

    elif user_action.startswith('remove'):
        try:
            # remove and pop method to remove a item from the list
            num = int(input('Enter the number which you want to remove'))
            num = num - 1

            todos = get_todos('todos.txt')

            todos.pop(num)  # In pop method you can directly send the index

            write_todos(todos, 'todos.txt')
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('Entered Wrong Command')
print('Bye')

# It is possible to have three variable when not using enumarate function
buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    print(first, second, third)
