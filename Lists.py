tasks = []

#to add tasks
def Add_Task(): 
   number = int(input("How many tasks to add: "))

   for i in range(number):
    task = input(f"Enter Task {i+1}: ")
    tasks.append(task)
   return
   

#to remove tasks
def Remove_Task():
  delete=int(input("Which number of task do you wish to remove: "))
  tasks.pop(delete-1)
  return   
  
  
#to view the current tasks
def View_Tasks():
 if(len(tasks)==0):
   print("No Tasks Found")
 else: 
  for i in range(len(tasks)):
   print(f"Your tasks are: {i+1}.{tasks[i]}")
 return 


#Display Menu
while True:
  print("1.Add Task")
  print("2.Remove Task")
  print("3.View Task")
  print("4.Exit")

  choice = int(input("Enter Choice =  "))

  match choice:

   case 1:
    Add_Task()
  
   case 2:
    Remove_Task()

   case 3:
    View_Tasks()

   case 4:
    break