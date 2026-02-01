import streamlit as st
import functions

todos = functions.get_todos('todos.txt')

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos, "todos.txt")

# BTS = Behind the scenes.

# While creating elements, order is important.
st.title('My Todo App') # BTS, it is a '<span>' inside '<h1>' tag.
st.subheader('This is my todo app.') # BTS, it is a '<span>' inside '<h3>' tag.
st.write('This app is to increase the productivity.') # BTS, it is a '<p>' tag.

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos,"todos.txt")
        del st.session_state[todo] # In Python, 'del' is used to remove a property from a dictionary.
        st.rerun() # This will programmatically rerun the script. When we tick/untick a checkbox, that event will run the script and remove it from the list of 'todos' and from session state dictionary. Now, the extra 'st.rerun()' is to render the unchecked checkboxes.

st.text_input(label = "Enter a todo", placeholder="Add new todo...", on_change= add_todo, key='new_todo')

print('Hello')

# st.session_state # Live session state