# 📋 To-Do List CLI App (Enhanced Version)

A robust, file-based command-line interface (CLI) application built with **Python** for managing your daily tasks. Keep track of what you need to do, when it's due, and its priority—all from the comfort of your terminal!

---

## ✨ Features

This version includes everything you need to manage your workflow efficiently:

| Icon | Feature | Description |
| :---: | :--- | :--- |
| **🔎** | **View Tasks** | Displays all tasks with their index and current status (`[X]` for done, `[ ]` for pending). |
| **✍️** | **Add Tasks** | Quickly adds new items, prompting for optional **Priority** and **Deadline**. |
| **✔️** | **Mark Done** | Changes a pending task to completed status. |
| **🗑️** | **Delete Tasks** | Permanently removes an item from the list by its index. |
| **🗃️** | **Persistence** | Saves all your tasks automatically to a local **`todo.txt`** file. |
| **ℹ️** | **Help Command** | Provides a quick reference guide for all available commands within the app. |

---

## 🚀 Getting Started

### Prerequisites

You only need **Python 3** installed on your system.

### How to Run

1.  **Save the Code:** Save the provided Python code into a file named `todo.py`.
2.  **Open Terminal:** Navigate to the directory where you saved `todo.py`.
3.  **Execute:** Run the application using the command:

```bash
python todo.py
```
*(The app will automatically create a `todo.txt` file if one doesn't exist.)*

---

## 📚 How to Use

Once the application is running, you'll be greeted with the main prompt. Enter one of the available options:

### Command Reference

| Command | Action | Example Input |
| :--- | :--- | :--- |
| **`list`** | Shows all tasks with their status and index number. | `Enter choice: list` |
| **`add`** | Prompts you to enter a new task, priority, and deadline. | `Enter choice: add` |
| **`done`** | Marks a task as complete. You'll be prompted for the task's index number. | `Enter choice: done` |
| **`delete`** | Permanently removes a task. You'll be prompted for the task's index number. | `Enter choice: delete` |
| **`help`** | Displays a list of all available commands. | `Enter choice: help` |
| **`exit`** | Saves all changes and closes the application. | `Enter choice: exit` |

Export to Sheets

---

### Example Workflow

1.  **Start the app:**
    ```bash
    $ python todo.py
    Welcome to the Enhanced CLI Todo List App!
    ```

2.  **Add a new task (using the `add` command):**
    ```
    Enter choice: add
    Enter new task: Review project requirements
    Enter priority (e.g., HIGH, low, leave empty): HIGH
    Enter deadline (e.g., 2025-12-31, leave empty): 2025-10-01
    Task 'Review project requirements' added and saved!
    ```

3.  **View the list:**
    ```
    Enter choice: list

    --- Your Tasks ---
    1. [ ] Review project requirements [Priority: HIGH] [Due: 2025-10-01]
    ------------------
    ```

4.  **Mark the task as done (using the `done` command and index 1):**
    ```
    Enter choice: done
    Enter the number of the task to mark as DONE: 1
    Task 1 marked as DONE! ✅
    ```

---

## 💾 Data Storage

Your tasks are stored locally in a plain text file called **`todo.txt`** in the same directory as the `todo.py` script. This makes it easy to back up or check your tasks outside the application if needed.