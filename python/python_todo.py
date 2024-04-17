tasks = []

def showTasks():
    with open("todo_list.txt", "r") as task_file:
        lines = task_file.readlines()
        title = "Todo list :"
        separator = "-" * len(title) 
        print(separator)
        print(title)
        print(separator)
        for i, line in enumerate(lines, start=1):
            if line.strip():
                print(f"{i}. {line.strip()}")
        print(separator, "\n")

showTasks()
    

def askForChoice():
    return input("What do you want to do now?\n 1. See the todo list\n 2. Add a new task\n 3. Delete a task\n 4. Modify a task\n 5. Exit\n\nSubmit: ")


def addTask():
   task_description = input("enter a new task: ")
   with open("todo_list.txt", "a") as task_file:
       task_file.write(f"{task_description}\n")



def deleteTask():
    with open("todo_list.txt", "r+") as tasks:
        lines = tasks.readlines()
        tasks.seek(0)
        title = "Todo list :"
        separator = "-" * len(title)
        print("\n", separator, "\n", title, "\n", separator) 

        new_lines = []
        for line in lines:
            if line.strip():  
                new_lines.append(line.strip())

        for i, line in enumerate(new_lines, start=1):
            print(f"{i}. {line}")

        print("\n")
        delete_num = input("Choose number of task to delete: ")
        

        if delete_num.isdigit():
            delete_index = int(delete_num) - 1
            if 0 <= delete_index < len(new_lines):
                del new_lines[delete_index]
                tasks.truncate(0)
                tasks.seek(0)
                for line in new_lines:
                    tasks.write(line + "\n")
            else:
                print("Invalid task number.")
        else:
            print("Invalid input. Please enter a valid task number.")
           
def modifyTask():
    with open("todo_list.txt", "r+") as tasks:
        lines = tasks.readlines()
        tasks.seek(0)
        title = "Todo list :"
        separator = "-" * len(title)
        print("\n", separator, "\n", title, "\n", separator) 

        new_lines = []
        for line in lines:
            if line.strip():  
                new_lines.append(line.strip())

        for i, line in enumerate(new_lines, start=1):
            print(f"{i}. {line}")

        print("\n")
        modify_num = input("Choose the number of the task to modify: ")

        if modify_num.isdigit():
            modify_index = int(modify_num) - 1
            if 0 <= modify_index < len(new_lines):
                new_description = input("Enter the new task description: ")
                new_lines[modify_index] = new_description
                tasks.truncate(0)
                tasks.seek(0)
                for line in new_lines:
                    tasks.write(line + "\n")
            else:
                print("Invalid task number.")
        else:
            print("Invalid input. Please enter a valid task number.")
      
while True:
    choice = askForChoice()
    
    if choice == "1":
        showTasks()
    elif choice == "2":
        addTask()
    elif choice == "3":
        deleteTask()
    elif choice == "4":
        modifyTask()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")



    