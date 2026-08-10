class Task:
    def __init__(self, title, category, priority, command=None):
        self.title = title
        self.category = category
        self.priority = priority
        self.command = command

    def to_dict(self):
        return {
            "title": self.title,
            "category": self.category,
            "priority": self.priority,
            "command": self.command
        }
