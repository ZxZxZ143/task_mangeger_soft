import json

FILE_NAME = "tasks.json"

tasks = []


class Task:
    def __init__(self, task_id, title, description, status="Pending"):
        self.id = task_id
        self.title = title
        self.description = description
        self.status = status


def save_tasks():
    data = []
    for task in tasks:
        data.append(task.__dict__)

    with open(FILE_NAME, "w") as f:
        json.dump(data, f)


def generate_id():
    if len(tasks) == 0:
        return 1
    return tasks[-1].id + 1


def add_task():
    title = input("Enter title: ")
    description = input("Enter description: ")

    task = Task(generate_id(), title, description, "Pending")
    tasks.append(task)

    save_tasks()
    print("Task added")


def list_tasks():
    if len(tasks) == 0:
        print("No tasks")
        return

    for task in tasks:
        print(task.id, task.title, "-", task.status)


def mark_complete():
    list_tasks()

    try:
        task_id = int(input("Enter task id: "))
    except:
        print("Invalid input")
        return

    for task in tasks:
        if task.id == task_id:
            task.status = "Completed"
            save_tasks()
            print("Task completed")
            return

    print("Task not found")


def delete_task():
    list_tasks()

    try:
        task_id = int(input("Enter id to delete: "))
    except:
        print("Invalid input")
        return

    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            del tasks[i]
            save_tasks()
            print("Task deleted")
            return

    print("Task not found")


def menu():
    while True:
        print("\nTask Manager")
        print("1 Add task")
        print("2 List tasks")
        print("3 Complete task")
        print("4 Delete task")
        print("0 Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


menu()