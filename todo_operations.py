
todo_list=[] 

def add_task(task): #this function can be used to add tasks in the existing list of tasks

 todo_list.append(task)
 print(f"task'{task}' added successfully")

def view_task():
 if not todo_list:
    print("No tasks to display.")
 else:
   print(f"{todo_list}")
              
def delete_task():
 try:
        task = todo_list.pop(index - 1)
        print(f"Task '{task}' deleted successfully.")
    except IndexError:
        print("Invalid index. No task deleted.")
