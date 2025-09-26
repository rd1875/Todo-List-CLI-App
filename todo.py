# Simple CLI Todo List App with Deadline

TODO_FILE = "todo.txt"

def read_tasks():
    with open(TODO_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def list_tasks(tasks):
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def add_task(tasks, task, deadline):
    tasks.append(f"{task} [Due: {deadline}]")
    with open(TODO_FILE, "w") as file:
        for t in tasks:
            file.write(t + "\n")
    print(f"Task '{task}' with deadline '{deadline}' added!\n")

def main():
    tasks = read_tasks()
    while True:
        print("Options: list / add / exit")
        choice = input("Enter choice: ").strip().lower()
        if choice == "list":
            list_tasks(tasks)
        elif choice == "add":
            task = input("Enter new task: ").strip()
            deadline = input("Enter deadline (YYYY-MM-DD): ").strip()
            add_task(tasks, task, deadline)
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
