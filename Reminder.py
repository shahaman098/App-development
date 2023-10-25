import time
import os

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def main():
    tasks = []

    while True:
        clear_screen()

        print("Task Scheduler")
        print("--------------")

        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_description = input("Enter the task description: ")
            tasks.append(task_description)
        elif choice == "2":
            task_to_remove = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_to_remove < len(tasks):
                removed_task = tasks.pop(task_to_remove)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number.")
            input("Press Enter to continue...")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(2)

if __name__ == "__main__":
    main()
