tasks=[]
def add_tasks():
    global tasks
    description = input("enter your description : ")
    due_date = input("enter your due date : ")
    status=False
    task={"description":description,"due_date": due_date,"status":status}
    tasks.append(task)
    print("Task added successfully...!1")

def task_displaying():
    if len(tasks) >= 1:
      status = "completed"

      for task in tasks:
        if task['status']:
            status="completed"
        else:
            status="pending"
        print(f"{tasks.index(task)+1}. {task['description']}, the due date is {task['due_date']}, {status}")
    else:
        print("There is no tasks to display")

def task_completion():
    if len(tasks)>=1:
       task_displaying()
       choice=int(input("Enter your task number which you want to mark as completed : "))-1
       # updated_status=input("Type 'c' if task is completed else type 'p'")
       print("Status updated successfully")
       tasks[choice]['status']=True
    else:
        print("There is no tasks to update status")


def updating_tasks():
    if len(tasks) >= 1:
      task_displaying()
      choice=int(input("enter the task number which you want to update the details : "))-1
      new_description=input("whats your new description ?")
      new_due_date=input("Enter the date ")
      tasks[choice]['description']=new_description
      tasks[choice]['due_date']=new_due_date
    else:
        print("There is no tasks to update")

def removing_tasks():
    if len(tasks) >= 1:
      task_displaying()
      choice = int(input("enter the task number which you want to remove : ")) - 1
      del tasks[choice]
      print("Task removed successfully")
    else:
        print("There is no tasks in your todo list")


print("welome to todo list")
adding_tasks_todolist=True
while adding_tasks_todolist:

   print("""
    1.Add task
    2.Display the tasks
    3.update status of the task
    4.Update task details
    5.Remove task
    6.Exit(This will delete your to do list tasks)
    """)

   option=int(input("choose which you want to do from the list"))
   if option==1:
      add_tasks()
   elif option==2:
      task_displaying()
   elif option==3:
     task_completion()
   elif option==4:
       updating_tasks()
   elif option==5:
       removing_tasks()
   elif option==6:
       adding_tasks_todolist=False
   else :
      op=input("invalid choice, choose a valid option")
      option=int(op)


