import json
import subprocess
from models import Task

class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, title, category, priority, command=None):
        task = Task(title, category, priority, command).to_dict()
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Task '{title}' added with priority {priority}.")

    def view_tasks(self):
        if not self.tasks:
            print("📂 No tasks found.")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task['title']} | Category: {task['category']} | Priority: {task['priority']} | Command: {task['command']}")

    def run_task(self, index):
        try:
            task = self.tasks[index]
            if task["command"]:
                print(f"▶ Running: {task['command']}")
                try:
                    subprocess.run(task["command"], shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"❌ Error running command: {e}")
            else:
                print("ℹ No command assigned to this task.")
        except IndexError:
            print("❌ Invalid task index.")

    def delete_task(self, index):
        try:
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"🗑 Task '{removed['title']}' deleted.")
        except IndexError:
            print("❌ Invalid task index.")

    def search_task(self, keyword):
        results = [task for task in self.tasks if keyword.lower() in task['title'].lower()]
        if results:
            print("🔍 Search Results:")
            for task in results:
                print(f"- {task['title']} | Category: {task['category']} | Priority: {task['priority']}")
        else:
            print("❌ No tasks found with that keyword.")
