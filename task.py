class Task:
    def __init__(
        self, task_id: int, title: str, description: str, status: str = "Pending"
    ):
        """Represents a single task with id, title, description and status."""
        self.id = task_id
        self.title = title
        self.description = description
        self.status = status
