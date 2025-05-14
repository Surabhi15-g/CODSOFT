import sys
import tkinter as tk
from tkinter import messagebox, simpledialog

# To-Do List Data Structure
todo_list = []

# ---------------------------
# Command-Line Interface (CLI)
# ---------------------------
def cli_menu():
    while True:
        print("\n--- To-Do List CLI ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task_cli()
        elif choice == '3':
            update_task_cli()
        elif choice == '4':
            delete_task_cli()
        elif choice == '5':
            print("Exiting CLI.")
            break
        else:
            print("Invalid choice. Please try again.")

def view_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def add_task_cli():
    task = input("Enter new task: ").strip()
    if task:
        todo_list.append(task)
        print(f"Task '{task}' added.")
    else:
        print("Empty task cannot be added.")

def update_task_cli():
    view_tasks()
    if not todo_list:
        return
    try:
        index = int(input("Enter task number to update: "))
        if 1 <= index <= len(todo_list):
            new_task = input("Enter new task description: ").strip()
            if new_task:
                todo_list[index - 1] = new_task
                print("Task updated.")
            else:
                print("Empty task description. Update cancelled.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task_cli():
    view_tasks()
    if not todo_list:
        return
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(todo_list):
            removed = todo_list.pop(index - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# ---------------------------
# GUI Interface
# ---------------------------
class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List GUI")
        self.todo_list = []

        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        self.listbox = tk.Listbox(self.frame, width=50)
        self.listbox.pack()

        self.entry = tk.Entry(self.frame, width=50)
        self.entry.pack(pady=5)

        self.btn_frame = tk.Frame(self.frame)
        self.btn_frame.pack(pady=5)

        self.add_btn = tk.Button(self.btn_frame, text="Add Task", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.update_btn = tk.Button(self.btn_frame, text="Update Selected", command=self.update_task)
        self.update_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(self.btn_frame, text="Delete Selected", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        self.refresh_listbox()

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.todo_list:
            self.listbox.insert(tk.END, task)

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.todo_list.append(task)
            self.entry.delete(0, tk.END)
            self.refresh_listbox()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def update_task(self):
        selected_indices = self.listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Selection Error", "Please select a task to update.")
            return
        index = selected_indices[0]
        new_task = simpledialog.askstring("Update Task", "Enter new task description:")
        if new_task:
            self.todo_list[index] = new_task.strip()
            self.refresh_listbox()

    def delete_task(self):
        selected_indices = self.listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
            return
        index = selected_indices[0]
        removed_task = self.todo_list.pop(index)
        self.refresh_listbox()

# ---------------------------
# Main Application
# ---------------------------
def main():
    print("Welcome to the To-Do List Application!")
    print("Choose interface mode:")
    print("1. Command Line")
    print("2. GUI")
    mode = input("Enter choice (1 or 2): ")

    if mode == '1':
        cli_menu()
    elif mode == '2':
        root = tk.Tk()
        app = ToDoApp(root)
        root.mainloop()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()