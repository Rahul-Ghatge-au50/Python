import function
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter Todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 16))


while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos_local = function.get_todos('todos.txt')
            new_todo = values['todo'] + "\n"
            todos_local.append(new_todo)
            function.write_todos(todos_local, 'todos.txt')

        case sg.WIN_CLOSED:
            break



window.close()

