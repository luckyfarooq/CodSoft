import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete")

def mark_completed():
    try:
        index = task_listbox.curselection()[0]
        task = task_listbox.get(index)
        task_listbox.delete(index)
        task_listbox.insert(index, task + " - Completed")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed")

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=0, padx=5, pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5)

task_listbox = tk.Listbox(root, width=50)
task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=2, column=0, padx=5, pady=5)

complete_button = tk.Button(root, text="Mark Completed", command=mark_completed)
complete_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()