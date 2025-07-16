
import streamlit as st
import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

tasks = load_tasks()

st.title("📝 Persönliche To-do-Liste")

new_task = st.text_input("Neue Aufgabe hinzufügen:")
if st.button("Hinzufügen"):
    if new_task:
        tasks.append({"task": new_task, "done": False})
        save_tasks(tasks)
        st.rerun()

st.subheader("📋 Aufgaben")
for i, task in enumerate(tasks):
    col1, col2, col3 = st.columns([6, 1, 1])
    with col1:
        st.markdown(f"{'✅' if task['done'] else '🔲'} {task['task']}")
    with col2:
        if st.button("Erledigt", key=f"done_{i}"):
            tasks[i]["done"] = not tasks[i]["done"]
            save_tasks(tasks)
            st.rerun()
    with col3:
        if st.button("Löschen", key=f"delete_{i}"):
            tasks.pop(i)
            save_tasks(tasks)
            st.rerun()
