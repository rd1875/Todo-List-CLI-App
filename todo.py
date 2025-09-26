# Simple CLI Todo List App - Enhanced Version

import os

# The file to store the to-do list data
TODO_FILE = "todo.txt"

def read_tasks():
    """Reads tasks from the file, handling FileNotFoundError."""
    tasks = []
    if not os.path.exists(TODO_FILE):
        return tasks # Return empty list if file doesn't exist
        
    try:
        with open(TODO_FILE, "r") as file:
            # Read tasks and strip whitespace/newlines
            tasks = [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error reading file: {e}")
        
    return tasks

def write_tasks(tasks):
    """Writes the current list of tasks back to the file."""
    try:
        with open(TODO_FILE, "w") as file:
            for t in tasks:
                file.write(t + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

def list_tasks(tasks):
    """Prints all tasks with their index and status."""
    print("\n--- Your Tasks ---")
    if not tasks:
        print("🎉 Your todo list is empty! 🎉")
        print("------------------\n")
        return

    for i, task in enumerate(tasks, 1):
        # Check for status marker. Assuming [X] is done, and no marker is pending.
        status = "[X]" if task.startswith("[X]") else "[ ]"
        
        # Remove the status marker from the display text for cleaner look
        display_task = task[3:].strip() if task.startswith(("[X]", "[ ]")) else task
        
        print(f"{i}. {status} {display_task}")
    print("------------------\n")

def add_task(tasks, task_text, priority=None, deadline=None):
    """Adds a new task (pending) with optional details."""
    # New tasks start as pending [ ]
    entry = "[ ] " + task_text
    
    if priority:
        entry += f" [Priority: {priority.upper()}]"
    if deadline:
        entry += f" [Due: {deadline}]"
        
    tasks.append(entry)
    write_tasks(tasks)
    print(f"Task '{task_text}' added and saved!\n")

def mark_done(tasks, index_str):
    """Marks a task as done based on its 1-based index."""
    try:
        index = int(index_str) - 1
        if 0 <= index < len(tasks):
            task = tasks[index]
            
            # Check if task is not already done, then update the marker
            if not task.startswith("[X]"):
                # If it starts with [ ], replace it. Otherwise, prepend [X]
                if task.startswith("[ ]"):
                    tasks[index] = "[X]" + task[3:]
                else:
                    # For tasks saved without a status marker (old format)
                    tasks[index] = "[X] " + task
                    
                write_tasks(tasks)
                print(f"Task {index + 1} marked as DONE! ✅\n")
            else:
                print(f"Task {index + 1} is already done.\n")
        else:
            print("Invalid task number. Please check the list.\n")
    except ValueError:
        print("Invalid input. Please enter the task number.\n")

def delete_task(tasks, index_str):
    """Deletes a task based on its 1-based index."""
    try:
        index = int(index_str) - 1
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            write_tasks(tasks)
            print(f"Deleted task {index + 1}: '{deleted_task[3:].strip()}' 🗑️\n")
        else:
            print("Invalid task number. Please check the list.\n")
    except ValueError:
        print("Invalid input. Please enter the task number.\n")

def main():
    """The main application loop."""
    tasks = read_tasks()
    print("Welcome to the Enhanced CLI Todo List App!")
    
    while True:
        print("------------------------------------------------------------------")
        print("Options: list / add / done / delete / help / exit")
        choice = input("Enter choice: ").strip().lower()
        print("------------------------------------------------------------------")
        
        if choice == "list":
            list_tasks(tasks)
            
        elif choice == "add":
            task_text = input("Enter new task: ").strip()
            if not task_text:
                print("Task cannot be empty.\n")
                continue
                
            priority = input("Enter priority (e.g., HIGH, low, leave empty): ").strip() or None
            deadline = input("Enter deadline (e.g., 2025-12-31, leave empty): ").strip() or None
            add_task(tasks, task_text, priority, deadline)
            
        elif choice == "done":
            list_tasks(tasks)
            if tasks:
                task_num = input("Enter the number of the task to mark as DONE: ").strip()
                mark_done(tasks, task_num)
                
        elif choice == "delete":
            list_tasks(tasks)
            if tasks:
                task_num = input("Enter the number of the task to DELETE: ").strip()
                delete_task(tasks, task_num)

        elif choice == "help":
            print("\nAvailable Commands:")
            print("list: Show all tasks with their status.")
            print("add: Add a new task (will prompt for details).")
            print("done: Mark an existing task as completed.")
            print("delete: Permanently remove a task.")
            print("exit: Save changes and close the application.\n")
            
        elif choice == "exit":
            print("Tasks saved. Goodbye!")
            break
            
        else:
            print("Invalid choice. Enter 'help' to see available options.\n")

if __name__ == "__main__":
    main()