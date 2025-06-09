import function
import FreeSimpleGUI as sg

"""Adding the todos"""
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter Todo", key="todo")
add_button = sg.Button("Add")


"""Listing the Todos"""
todo_list = sg.Listbox(values=function.get_todos('todos.txt'), key="todos", enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
comp_btn = sg.Button("Complete")
exit_btn = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [todo_list, edit_button, comp_btn],[exit_btn]],
                   font=('Helvetica', 16))


while True:
    event, values = window.read()
    print("event", event)
    print("values", values)
    match event:
        case "Add":
            todos_local = function.get_todos('todos.txt')
            new_todo = values['todo'] + "\n"
            todos_local.append(new_todo)
            function.write_todos(todos_local, 'todos.txt')
            window['todos'].update(values=todos_local)

        case "Edit":
            old_todo = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = function.get_todos('todos.txt')
            index = todos.index(old_todo)
            todos[index] = new_todo
            function.write_todos(todos, 'todos.txt')
            window['todos'].update(values=todos)
            window['todo'].update(value="")

        case 'Complete':
            comp_todo = values['todos'][0]
            todos = function.get_todos('todos.txt')
            todos.remove(comp_todo)
            function.write_todos(todos, 'todos.txt')
            window['todos'].update(values=todos)
            window['todo'].update(value="")

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break



window.close()

