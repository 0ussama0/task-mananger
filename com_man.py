


task = [] #list to store tasks
def add () :#add new task
  while True : #make it run for easy adding multi tasks 
    print("-"*30)
    print("inter Q to quite") #note for a quite
    print("-"*30)
    tasks = input ("plz, input the task : ") #take task name
    tasks=tasks.capitalize() #for formating
    if tasks == "Q": #make quite for user to en adding
        break
    else: #now take the input ex (q) to store it as task
         info = {"task":tasks,"category":False } #take the task and mark it as not done
         task.append(info) #add it to the list
    print("-"*30)
def view () : #view what taks in the mananger
    i=0
    
    print("-"*30)
    while i < len(task):  #here we inform what is done and what is not
       if task[i].get("category")==True:k="(done)"
       else : k="(not done)"
       print (i+1,"-",task[i].get("task"),k)
       i+=1
    print("-"*30)
def mark (): #make user to mark what he done
    view() #view tasks to know what he did 

    v=input("plz input the task number : ") #take task num
    v=int(v) #make it int to use it as indix
    #check for it and mark it
    if task[v-1]["category"]== False : 
        task[v-1]["category"]=True
        print (task[v-1]["task"],"has been marked as done")
    else:
           print ("the task is alredy mark as done before")
    print("-"*30)
while True : #make loop for the program
#print the options and take actions

    x=input ("""1: add task 
2: view tasks
3: mark task as done 
4: quite
plz inter ur choise : """)
    if x == "1": add()
    elif x == "2": view()
    elif x == "3": mark()
    elif x == "4": break
    else:print("plz inter choise from below ")