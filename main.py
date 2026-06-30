import tkinter as tk
from tkinter import messagebox

# ---------------------- Functions ----------------------

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass


def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")


def add_task():
    task = task_entry.get()

    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task.")


def clear_tasks():
    answer = messagebox.askyesno("Confirm", "Delete all tasks?")
    if answer:
        task_listbox.delete(0, tk.END)
        save_tasks()


# ---------------------- GUI ----------------------

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text="TO-DO LIST",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

task_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=25
)
task_entry.pack(pady=10)

add_btn = tk.Button(
    root,
    text="Add Task",
    width=20,
    command=add_task
)
add_btn.pack(pady=5)

task_listbox = tk.Listbox(
    root,
    width=40,
    height=12,
    font=("Arial", 12)
)
task_listbox.pack(pady=10)

delete_btn = tk.Button(
    root,
    text="Delete Selected",
    width=20,
    command=delete_task
)
delete_btn.pack(pady=5)

clear_btn = tk.Button(
    root,
    text="Clear All",
    width=20,
    command=clear_tasks
)
clear_btn.pack(pady=5)

load_tasks()

root.mainloop()