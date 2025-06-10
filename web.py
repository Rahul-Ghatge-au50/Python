import streamlit as st
import function
import time

# st.markdown("<h1 style='text-align: center; color: grey;'>Big headline</h1>", unsafe_allow_html=True)
# st.markdown("<h2 style='text-align: center; color: black;'>Smaller headline in black </h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

timeer = time.strftime("%b %d, %Y %H:%M:%S")

with col1:
    st.title("My Todo App")

with col2:
    st.subheader(timeer)

todos = function.get_todos('todos.txt')


user_input = st.text_input(label="Enter a todo", placeholder="Add a new todo...")

for todo in todos:
    st.checkbox(todo)

if user_input:
    todos_local = function.get_todos('todos.txt')
    new_todo = f"{user_input}\n"
    print("new_todo", new_todo)
    todos_local.append(new_todo)
    function.write_todos(todos_local, 'todos.txt')
