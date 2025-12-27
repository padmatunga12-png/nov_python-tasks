from ast import main


class todolist:
    def __init__(self):
        self.tasks = []
    def add_task(self,task):
        self.task.append({"task": task, "completed": False})
        print("task added successfully!")
    def remove_task(self,task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                print("task removed successfully!")
                return
            print("task not found in the list")
    def mark_completed(self,task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                print("task marked as completed!")
                return
            print("task not found in the list")
    def display_tasks(self):
        if self.tasks:
            print("tasks:")
            for i, t in enumerate(self.tasks,start=1):
                status = "completed" if t["completed"] else "not completed"
                print(f"{i}. {t['task']} - {status}")
            else:
                print("no tasks in the list")
                def main():
                    todo_list = todolist()
                    while True:
                        print("\nTODO LIST MENU:")
                        print("1. add a task")
                        print("2.remove a task")
                        print("3.mark a task as completed")
                        print("4. display tasks")
                        print("5.exit")
                    choice = input("enter your choice(1/2/3/4/5): ")
                    if choice == '1':
                        task = input("enter task to add:")
                        todo_list.add_task(task)
                    elif choice == '2':
                        task = input("enter task to remove:")
                        todo_list.remove_task(task)
                    elif choice == '3':    
                        task = input("enter task to mark as completed:")
                        todo_list.mark_completed(task)
                    elif choice == '4':
                        todo_list.display_tasks()
                    elif choice == '5':
                        print("exiting...")
                        break    
                    else:
                       print("invalid choice. please enter a valid option.")
main()
                                                     
    