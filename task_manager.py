from task import Task
from file_manager import save_tasks


def generate_id(tasks: list[Task]) -> int:
    """Generate next available task ID."""
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1  # лучше max, чем tasks[-1]


def find_task_by_id(tasks: list[Task], task_id: int) -> Task | None:
    """Find task by ID or return None."""
    for task in tasks:
        if task.id == task_id:
            return task
    return None


def add_task(tasks: list[Task]) -> None:
    """Add new task from user input."""
    title = input("Enter title: ").strip()
    if not title:
        print("Title cannot be empty!")
        return
    description = input("Enter description: ").strip()
    task = Task(generate_id(tasks), title, description)
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully")


def list_tasks(tasks: list[Task]) -> None:
    """Print all tasks."""
    if not tasks:
        print("No tasks yet.")
        return
    print("\nTasks:")
    for task in tasks:
        print(f"{task.id}. {task.title} ({task.description}) - {task.status}")


def mark_complete(tasks: list[Task]) -> None:
    """Mark task as completed."""
    list_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to complete: "))
    except ValueError:
        print("Invalid ID - must be a number.")
        return
    task = find_task_by_id(tasks, task_id)
    if task is None:
        print("Task not found.")
        return
    if task.status == "Completed":
        print("Task already completed.")
        return
    task.status = "Completed"
    save_tasks(tasks)
    print("Task marked as completed")


def delete_task(tasks: list[Task]) -> None:
    """Delete task by ID."""
    list_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid ID - must be a number.")
        return
    task = find_task_by_id(tasks, task_id)
    if task is None:
        print("Task not found.")
        return
    tasks.remove(task)
    save_tasks(tasks)
    print("Task deleted successfully")
