import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.heading_label = tk.Label(self.root, text="TO-DO LIST", font=("Helvetica", 16, "bold"))
        self.heading_label.pack(pady=10)

        self.tasks = []
        self.task_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.listbox = tk.Listbox(self.root, font=("Helvetica", 12), selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.edit_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack()

        self.track_button = tk.Button(self.root, text="Track Task", command=self.track_task)
        self.track_button.pack()

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append((task, False))
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def edit_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task_to_edit = self.tasks[index][0]
            new_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=task_to_edit)
            if new_task:
                self.tasks[index] = (new_task, self.tasks[index][1])
                self.listbox.delete(index)
                self.listbox.insert(index, new_task)

    def track_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task, tracked = self.tasks[index]
            self.tasks[index] = (task, not tracked)
            self.listbox.itemconfig(index, {'bg': 'lightgreen' if not tracked else 'white'})

    def delete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            deleted_task = self.tasks.pop(index)[0]
            self.listbox.delete(index)
            messagebox.showinfo("Task Deleted", f"Task '{deleted_task}' deleted.")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
