
class textColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ToDoList:

    def __init__(self):
        self.list = []


    def AppendToList(self):
        action = input("\nWhat do you plan to do? ")

        if(len(self.list) < 5):
            self.list.append(action);

            print(textColors.OKGREEN + "\nAdded successfully." + textColors.ENDC)
            self.NumberOfTasks()

            if(len(self.list) < 4):
                print(textColors.OKBLUE + "\nYou have less than 4 tasks to do on your list, you have more time to put in more effort :D" + textColors.ENDC)
        else:
            print(textColors.FAIL + "\nWhat a hardworking person! You don't have more time to do other activities." + textColors.ENDC)

    
    def NumberOfTasks(self):
        print(textColors.OKCYAN + "You have {} task(s) in your to-do list.".format(len(self.list)) + textColors.ENDC)


    def RemoveFirstTask(self):
        if (len(self.list) == 0):
            print(textColors.FAIL + "There is nothing to do today, do something !" + textColors.ENDC)
        else:
            del self.list[0]
            print(textColors.OKGREEN + "\nFirst task has removed successfully." + textColors.ENDC)
            self.NumberOfTasks()


    def RemoveSpecificTask(self):
        self.PrintList()

        if(len(self.list) > 0):
            selectedTask = input("\nWhich task do you want to remove? ")

            if not selectedTask.isnumeric():
                print(textColors.FAIL + "Please choose correct task" + textColors.ENDC)
                
            else:
                try:
                  del self.list[int(selectedTask)-1]
                  print(textColors.OKGREEN + "\nTask number {} has removed successfully.".format(selectedTask) + textColors.ENDC)
                  self.NumberOfTasks()
                except IndexError:
                    print(textColors.FAIL + "Task number {} doesn't exist in your to-do list !".format(selectedTask) + textColors.ENDC)


    def ClearList(self):
        self.list = []


    def PrintList(self):
        if (len(self.list) == 0):
            print(textColors.FAIL + "There is nothing to do today, do something !" + textColors.ENDC)
        else:
            print(textColors.OKCYAN + "\n-------------------------------------------" + textColors.ENDC)
            for i in range(len(self.list)):
                print(textColors.OKCYAN + str(i+1) + "] " + self.list[i] + textColors.ENDC)
            print(textColors.OKCYAN + "-------------------------------------------" + textColors.ENDC)


    def ShowMenu(self):
        print(textColors.WARNING + 
              "\n-------------------------------------------\n"
              "(1) Add new task\n"
              "(2) Number of available tasks\n"
              "(3) Remove first task\n"
              "(4) Remove specific task\n"
              "(5) Print tasks list\n"
              "(6) Clear list\n"
              "(7) Show action menu\n"
              "-------------------------------------------"
               + textColors.ENDC)



if __name__ == '__main__':

    todo_List = ToDoList()
    print(textColors.BOLD + textColors.HEADER + "\nTo-Do List" + textColors.ENDC)

    todo_List.ShowMenu()

    while True:
        action = input("\nChoose the option you want (Enter 7 to show menu): ")

        if not action.isnumeric():
            print(textColors.FAIL + "I don't know how to do that!" + textColors.ENDC)
            continue

        elif action == "1":
            todo_List.AppendToList()

        elif action == "2":
            todo_List.NumberOfTasks()

        elif action == "3":
            todo_List.RemoveFirstTask()

        elif action == "4":
            todo_List.RemoveSpecificTask()

        elif action == "5":
            todo_List.PrintList()
        
        elif action == "6":
            todo_List.ClearList()

        elif action == "7":
            todo_List.ShowMenu()

        else:
            print(textColors.FAIL + "Your chosen option is not in the list !" + textColors.ENDC)


#Written by (Mehdi Daustany) at the request of the University of the Netherlands
#https://github.com/daustany/todo-list.git