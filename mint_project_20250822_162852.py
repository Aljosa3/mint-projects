import tkinter as tk
from tkinter import messagebox
import json
import os

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("400x500")
        
        # Load tasks from file or create empty list
        self.tasks = self.load_tasks()
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Task input
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=10)
        
        self.task_entry = tk.Entry(self.task_frame, width=30)
        self.task_entry.pack(side=tk.LEFT, padx=5)
        
        self.add_button = tk.Button(self.task_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)
        
        # Task list
        self.task_listbox = tk.Listbox(self.root, width=45, height=15)
        self.task_listbox.pack(pady=10)
        
        # Buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)
        
        self.complete_button = tk.Button(self.button_frame, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack(side=tk.LEFT, padx=5)
        
        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)
        
        # Update task list
        self.update_task_list()
        
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
            
    def mark_complete(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]["completed"] = True
            self.save_tasks()
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")
            
    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.save_tasks()
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")
            
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓ " if task["completed"] else "  "
            self.task_listbox.insert(tk.END, f"{status}{task['task']}")
            
    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)
            
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()