import json
import os

from task import Task

TASKS_FILE = "tasks.json"


def load_tasks() -> list["Task"]:
    """Load tasks from JSON file or return empty list if file not exists."""
    from task import Task  # import here

    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [
        Task(item["id"], item["title"], item["description"], item["status"])
        for item in data
    ]


def save_tasks(tasks: list["Task"]) -> None:
    """Save list of tasks to JSON file."""
    data = [task.__dict__ for task in tasks]
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
