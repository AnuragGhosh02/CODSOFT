tasks = []
def add_task(new_task):
    tasks.append(new_task)
    print(f"Added task: {new_task}")
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Removed task: {task}")
    else:
        print(f"{task} not found!")
def view_task(tasks_list):
    print("To-do lists: ")
    for i, task in enumerate(tasks_list):
        print(f"{i+1}. {task}")
while True:
    print("\nWhat do you want to do?\n1: Add a task\n2: Remove a task\n3: View all tasks\n4: Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        new_task = input("Enter a new task: ")
        add_task(new_task)
    elif choice == "2":
        task_to_remove = input("Enter the task you want to remove: ")
        remove_task(task_to_remove)
    elif choice == "3":
        view_task(tasks)
    elif choice == "4":
        print("Exiting!")
        break
    else:
        print("Invalid choice!")
