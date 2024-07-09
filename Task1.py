class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}\n"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"Task {index}:")
                print(task)

    def complete_task(self, task_index):
        try:
            self.tasks[task_index - 1].completed = True
            print("Task marked as completed.")
        except IndexError:
            print("Invalid task index. Please try again.")

    def delete_task(self, task_index):
        try:
            del self.tasks[task_index - 1]
            print("Task deleted successfully.")
        except IndexError:
            print("Invalid task index. Please try again.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)

        elif choice == "2":
            todo_list.list_tasks()

        elif choice == "3":
            task_index = int(input("Enter task index to mark as completed: "))
            todo_list.complete_task(task_index)

        elif choice == "4":
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()