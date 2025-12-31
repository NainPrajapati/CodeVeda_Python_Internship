# Level 2 - Task 1
# To-Do List Application (JSON based)
# Codveda Python Internship

import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task title: ")
    task_id = len(tasks) + 1
    tasks.append({
        "id": task_id,
        "title": title,
        "completed": False
    })
    save_tasks(tasks)
    print("✅ Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        status = "✔ Completed" if task["completed"] else "❌ Pending"
        print(f"{task['id']}. {task['title']} - {status}")


def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to mark as completed: "))
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                save_tasks(tasks)
                print("✅ Task marked as completed!")
                return
        print("❌ Task not found.")
    except ValueError:
        print("❌ Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to delete: "))
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks(tasks)
                print("🗑 Task deleted successfully!")
                return
        print("❌ Task not found.")
    except ValueError:
        print("❌ Please enter a valid number.")


def main():
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        tasks = load_tasks()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


main()
