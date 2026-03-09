tasks = []


class Task:
    def __init__(self, task_id, title, description, status="Pending"):
        self.id = task_id
        self.title = title
        self.description = description
        self.status = status


def generate_id():
    if len(tasks) == 0:
        return 1
    return tasks[-1].id + 1


def add_task():
    title = input("Enter title: ")
    description = input("Enter description: ")

    task = Task(generate_id(), title, description, "Pending")
    tasks.append(task)

    print("Task added")


def menu():
    while True:
        print("\nTask Manager")
        print("1 Add task")
        print("2 List tasks")
        print("0 Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            print("List tasks not implemented yet")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


menu()