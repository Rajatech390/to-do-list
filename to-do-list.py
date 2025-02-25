# To-Do List Application using Python

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
            return
        print("Your To-Do List:")
        for idx, task in enumerate(self.tasks, 1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx}. {task['task']} [{status}]")
    
    def update_task(self, task_num, new_task=None, mark_completed=False):
        if task_num < 1 or task_num > len(self.tasks):
            print("Invalid task number.")
            return
        if new_task:
            self.tasks[task_num - 1]["task"] = new_task
            print(f"Task updated to: {new_task}")
        if mark_completed:
            self.tasks[task_num - 1]["completed"] = True
            print(f"Task marked as completed.")
    
    def delete_task(self, task_num):
        if task_num < 1 or task_num > len(self.tasks):
            print("Invalid task number.")
            return
        removed_task = self.tasks.pop(task_num - 1)
        print(f"Task '{removed_task['task']}' deleted.")

# Main function to interact with the user
def main():
    todo = TodoList()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            task = input("Enter a new task: ")
            todo.add_task(task)
        
        elif choice == '2':
            todo.view_tasks()
        
        elif choice == '3':
            todo.view_tasks()
            task_num = int(input("Enter the task number to update: "))
            new_task = input("Enter new task details (leave blank to skip): ")
            mark_completed = input("Mark as completed? (y/n): ").lower() == 'y'
            todo.update_task(task_num, new_task, mark_completed)
        
        elif choice == '4':
            todo.view_tasks()
            task_num = int(input("Enter the task number to delete: "))
            todo.delete_task(task_num)
        
        elif choice == '5':
            print("Exiting To-Do List Application. Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose between 1 and 5.")

# Run the application
if __name__ == "__main__":
    main()
