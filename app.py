import streamlit as st

st.title("To-Do App")

tasks = []

def add_task():
    task = st.session_state["new_task"]
    tasks.append(task)
    st.session_state["new_task"] = ""

st.text_input("Enter a task", key="new_task")
st.button("Add Task", on_click=add_task)

st.write("## Tasks")
for task in tasks:
    st.write(f"- {task}")