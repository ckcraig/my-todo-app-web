import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my web todo app.")

st.text_input(placeholder="Add new todo...", label="Enter New Todos here:",
              on_change=add_todo, key="new_todo")

for index, all_todos in enumerate(todos):
    checkbox = st.checkbox(all_todos, key=all_todos)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[all_todos]
        st.rerun()
