task=[]

def add_task():
    task_num =int(input("how many tasks you wanna add ==>"))
    for i in range(task_num):
        name=input(f"what is the name of the task {i+1}==>")
        task.append(name)
    
def task_remover():
    task_num=int(input("how many tasks you wanna remove ==>"))
    for i in task:
        name=input(f"what is name of task==>")
        if i==name:
            task.remove(name)
while True :
    purpose =input(f"what is your pupose after looking at the list {task} \n do you wanna add/remove/check the tasks ? ==> ")
    if purpose=='check':    
        print("these are the task in the list\n " ,task)

    elif purpose=='add':
        add_task()
        print("now that list became like this now \n",task)

    elif purpose=='remove':
        task_remover()
        print("now that list became like this now \n",task)

    elif purpose=='no':
        print("okay goodbye")
        break