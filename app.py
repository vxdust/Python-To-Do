Tasks = []


def ViewTaskList():
    print("ViewTaskList Started")
    if len(Tasks) > 0:
        print(Tasks)
        userInput = input("Go Back?\n")
        if userInput in ["Yes", "YES", "y", "Y", "yes"]:
             Start()
        else:
             print("Goodbye!")
             exit()
    else:
        print("Your Current List is Empty")
        userInput = input("Go Back?\n")
        if userInput in ["Yes", "YES", "y", "Y", "yes"]:
            print("if worked")
            Start()
        else:
            print("else worked")
            exit()

def AddTask():
    print("AddTask Started")
    userInput = input("What Task Would You Like to Add?\n")
    Tasks.append(userInput)
    print("Task Added Successfully")
    print("Would You Like to Add More Tasks?")
    userInput = input("")
    if userInput in ["Yes", "YES", "y", "Y", "yes"]:
        AddTask()
    else:
        Start()


def RemoveTask():
    print("RemoveTask Started")
    if len(Tasks) > 0:
                print(Tasks)
                userInput = input("Which Task Would you Like to Remove?\n")
                if userInput in Tasks:
                        print("Removing " + userInput)
                        Tasks.remove(userInput)
                        print("Removed Successfully")
                        Start()  
                else:
                        print("That's not in the list")
                        userInput = input("Go Back? ")
                        if userInput in ["Yes", "YES", "y", "Y", "yes"]:
                             Start()
                        else:
                             print("Goodbye, Have a Great Day!")


def Start():
    
    print("Hi! " + "What would you like to do?")
    print("1: " + "View Task List")
    print("2: " + "Add New Task")
    print("3: " + "Remove Task")
    print("4: " + "Exit Program")
    userInput = input()
    if userInput == "1":
        ViewTaskList()
    elif userInput == "2":
        AddTask()
    elif userInput == "3":
        RemoveTask()
    elif userInput == "4":
        exit()
    else:
        print("Invalid Response " + "Please Select Between 1-4")
        Start()

Start()