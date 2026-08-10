from task_manager import TaskManager
from utils import print_banner, validate_choice

def main():
    print_banner()
    manager = TaskManager("tasks.json")

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Run Task Command")
        print("4. Delete Task")
        print("5. Search Task by Keyword")
        print("6. Exit")

        choice = input("Enter choice: ")
        if not validate_choice(choice):
            print("❌ Invalid input. Please enter a number between 1-6.")
            continue

        choice = int(choice)

        if choice == 1:
            title = input("Task Title: ")
            category = input("Category (Work/Personal/DevOps): ")
            priority = input("Priority (High/Medium/Low): ")
            command = input("System Command (optional): ")
            manager.add_task(title, category, priority, command)

        elif choice == 2:
            manager.view_tasks()

        elif choice == 3:
            idx = int(input("Enter task index to run: "))
            manager.run_task(idx)

        elif choice == 4:
            idx = int(input("Enter task index to delete: "))
            manager.delete_task(idx)

        elif choice == 5:
            keyword = input("Enter keyword to search: ")
            manager.search_task(keyword)

        elif choice == 6:
            print("👋 Exiting... Goodbye!")
            break

if __name__ == "__main__":
    main()
