
from file_manager import load_tasks
from task_manager import add_task, list_tasks, mark_complete, delete_task

tasks = load_tasks()


def menu() -> None:
    """Main application loop with menu."""
    while True:
        print("\n=== Task Manager ===")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("0. Exit")
        choice = input("Choose option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()
