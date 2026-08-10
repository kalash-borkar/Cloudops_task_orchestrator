🌩️ CloudOps Task Orchestrator
📌 About
A Python-based CLI application to create, manage, search, and run tasks.
Each task can have a title, category, priority, and optional system command.
The project is modular, making it easy to extend into DevOps workflows (Docker, CI/CD, Cloud deployment).

❓ Problem Statement
Managing tasks manually is inefficient:

📝 Commands and priorities are often forgotten

📂 No central storage for tasks

⏳ Running commands one by one wastes time

⚙️ Automation is hard without structure

✅ Solution
CloudOps Task Orchestrator solves these problems by:

💾 Storing tasks in a JSON file for persistence

🏷️ Adding metadata (category, priority) for better organization

⚡ Running system commands directly via Python subprocess

🔍 Searching tasks quickly by keyword

🛡️ Handling errors gracefully to keep automation stable

This makes it ideal for automation and future DevOps pipeline integration.

🚀 Features
➕ Add new tasks with category & priority

📋 View all tasks

⚡ Run system commands directly from tasks

❌ Delete tasks

🔍 Search tasks by keyword

💾 Save tasks in JSON file

🛡️ Error handling for invalid inputs & failed commands

📂 Project Structure
Code
cloudops_task_orchestrator/
│
├── 🎯 main.py          → Entry point (menu system)
├── ⚙️ task_manager.py  → Handles task logic (add, view, run, delete, search)
├── 🧩 models.py        → Defines Task class (object → dict)
├── 🛠 utils.py         → Helper functions (banner, validation)
└── 📄 tasks.json       → Stores tasks persistently
▶ How to Run
Clone the repository:

bash
git clone https://github.com/kalash-borkar/Cloudops_task_orchestrator.git
Navigate into the folder:

bash
cd Cloudops_task_orchestrator
Run the program:

bash
python main.py
