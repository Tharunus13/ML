import tkinter as tk
from tkinter import messagebox


class ToDoList:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.root.title("To-Do List")

        # Create and pack the UI elements
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.add_task_entry = tk.Entry(root, width=40)
        self.add_task_entry.pack(pady=5)

        self.add_task_button = tk.Button(root, text="Add Task", width=20, command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.mark_done_button = tk.Button(root, text="Mark as Done", width=20, command=self.mark_done)
        self.mark_done_button.pack(pady=5)

        self.delete_task_button = tk.Button(root, text="Delete Task", width=20, command=self.delete_task)
        self.delete_task_button.pack(pady=5)

    def update_task_list(self):
        """Updates the Listbox with the current tasks."""
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            status = "Done" if task["done"] else "Pending"
            self.task_listbox.insert(tk.END, f"{idx + 1}. {task['task']} - {status}")

    def add_task(self):
        task = self.add_task_entry.get()
        if task.strip():
            self.tasks.append({"task": task, "done": False})
            self.add_task_entry.delete(0, tk.END)
            self.update_task_list()
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def mark_done(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            task["done"] = True
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.tasks.pop(selected_task_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")


if __name__ == "__main__":
    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()

