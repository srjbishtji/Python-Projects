tasks = []
username = input("enter your name : ")


def show_menu():
    print("\n1. Add a Task ")
    print("2. View Tasks")
    print("3. Delete a Task")
    print("4. Update a Task")
    print("5. Clear Tasks")
    print("6. Search Tasks")
    print("7. Exit")


def add_task(task):
    tasks.append(task)
    return f'Task "{task}" added successfully.'
    

def show_tasks():
    if not tasks:
        return "No Task Available"
    result = ""
    for index,task in enumerate(tasks):
        result += f"{index+1}. {task}\n"
    return result.strip()


def delete_task():
    if tasks:
        try:
            index = int(input("enter the index of the task : "))
            if 1 <= index <= len(tasks):
                tasks.pop(index-1)
                return "Task deleted successfully"
            else:
                    return "Put the number according to the Tasks Index"
        except ValueError:
            return "Invalid input. Please enter a valid number."
    else:
        return "No tasks to delete"


def update_task():
    if tasks:
        print("Task Lists:\n")
        print(show_tasks())
        try:
            indexs = int(input("Enter the index of task to update: "))
            if 1 <= indexs <= len(tasks):
                updated_task = input("Enter the new task: ")
                tasks[indexs - 1] = updated_task
                return f"Task {indexs} updated successfully."
            else:
                return "Invalid task index."
        except ValueError:
            return "Please enter a valid number."
    else:
        return "No tasks available to update."


def clear_task():
    tasks.clear()
    return "Tasks are cleared"


def search_task():
    if not tasks:
        print("No tasks available")
        return
    keyword = input("Enter the keyword to search the task: ").lower()
    found_tasks = []
    for index, task in enumerate(tasks):
        if keyword in task.lower():
            found_tasks.append((index, task))
    if found_tasks:
        print("Matching Tasks:")
        for index, task in found_tasks:
            print(f"{index + 1}. {task}")
    else:
        print("No matching tasks found.")


def save_tasks_to_file():
    with open(f"{username}_tasks.txt", "w") as file:
        if not tasks:
            file.write("No Task Available\n")
        else:
            for index, task in enumerate(tasks):
                file.write(f"{index + 1}. {task}\n")


while True:
    show_menu()
    try:
        choice = int(input("enter your choice from the Menu : "))
        if choice not in range(1, 8):
            print("Choose a valid option")
            continue  
        if choice == 1:
            task = input("enter the task : ")
            print(add_task(task))
            save_tasks_to_file()
        elif choice == 2:
            print(show_tasks())
        elif choice == 3:
            print(delete_task())
            save_tasks_to_file()
        elif choice == 4:
            print(update_task())
            save_tasks_to_file()
        elif choice == 5:
            print(clear_task())
            save_tasks_to_file()
        elif choice == 6:
            search_task()
        elif choice == 7:
            print("Exiting the program.")
            break

    except ValueError:
        print("Invalid Input")




# functionality :
# 1. Add a feature to mark tasks as completed. (change your tasks = [] to tasks = {})