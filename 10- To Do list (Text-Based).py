def save_tasks(tasks, completed):
    """Save tasks and their completion status to a text file."""
    with open("tasks.txt", "w") as f:
        for task, is_complete in zip(tasks, completed):
            status = "1" if is_complete else "0"
            f.write(f"{task},{status}\n")

def load_tasks():
    """Load tasks and their completion status from a text file."""
    tasks = []
    completed = []
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                task, status = line.strip().split(",")
                tasks.append(task)
                completed.append(status == "1")
    except FileNotFoundError:
        pass  # If the file doesn't exist, return empty lists
    return tasks, completed

def todo_list():
    """Main function to manage the to-do list."""
    tasks, completed = load_tasks()  # Load existing tasks
    print("Welcome to the To-Do List Application!")
    print("Available commands: add, remove, view, complete, quit")

    while True:
        command = input("> ").strip().lower()  # Get user input

        if command.startswith("add "):
            task = command[4:]  # Extract the task
            tasks.append(task)  # Add the task to the list
            completed.append(False)  # Mark it as incomplete
            print(f"Added task: '{task}'")

        elif command.startswith("remove "):
            try:
                task_number = int(command.split()[1]) - 1  # Get task index
                if 0 <= task_number < len(tasks):
                    removed_task = tasks.pop(task_number)  # Remove the task
                    completed.pop(task_number)  # Remove completion status
                    print(f"Removed task: '{removed_task}'")
                else:
                    print("Invalid task number.")
            except (IndexError, ValueError):
                print("Please provide a valid task number.")

        elif command == "view":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                for index, (task, is_complete) in enumerate(zip(tasks, completed), start=1):
                    status = "Complete" if is_complete else "Incomplete"
                    print(f"{index}. {task} [{status}]")

        elif command.startswith("complete "):
            try:
                task_number = int(command.split()[1]) - 1  # Get task index
                if 0 <= task_number < len(tasks):
                    completed[task_number] = True  # Mark task as complete
                    print(f"Marked task '{tasks[task_number]}' as complete.")
                else:
                    print("Invalid task number.")
            except (IndexError, ValueError):
                print("Please provide a valid task number.")

        elif command == "quit":
            save_tasks(tasks, completed)  # Save tasks before quitting
            print("Goodbye!")
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    todo_list()
