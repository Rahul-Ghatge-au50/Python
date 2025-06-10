import function
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme("Black")

"""Adding the todos"""
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter Todo", key="todo")
add_button = sg.Button("Add", mouseover_colors="LightBlue2", tooltip="Add", key="Add")

clock = sg.Text("", key="clock")



"""Listing the Todos"""
todo_list = sg.Listbox(values=function.get_todos('todos.txt'), key="todos", enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
comp_btn = sg.Button("Complete")
exit_btn = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock], [label], [input_box, add_button], [todo_list, edit_button, comp_btn], [exit_btn]],
                   font=('Helvetica', 16))


while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos_local = function.get_todos('todos.txt')
            new_todo = values['todo'] + "\n"
            todos_local.append(new_todo)
            function.write_todos(todos_local, 'todos.txt')
            window['todos'].update(values=todos_local)

        case "Edit":
            try:
                old_todo = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = function.get_todos('todos.txt')
                index = todos.index(old_todo)
                todos[index] = new_todo
                function.write_todos(todos, 'todos.txt')
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first")

        case 'Complete':
            try:
                comp_todo = values['todos'][0]
                todos = function.get_todos('todos.txt')
                todos.remove(comp_todo)
                function.write_todos(todos, 'todos.txt')
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first")
        case "todos":
            window['todo'].update(value=values['todos'][0])

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break



window.close()

