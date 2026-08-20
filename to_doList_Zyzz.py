
options = [1,2,3,4]
tasks = []

def add_task(task):
    tasks.append(task)
    print('Task added succesfully! Here are your current tasks:')
    for t in enumerate(tasks, 1):
        print(t)
        

def view_task():
    if tasks == []:
        print('You have zero tasks ')
    else:    
        print(f'Here are your current tasks: {tasks}')
    

def remove_task(removal):
    try:       
        tasks.pop(int(removal) - 1)
        print('Task removed succesfully')
    except IndexError:
        print('input correct value ')
    


while True:
    print('\n Hello sir, welcome to the your task manager')
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input('What would you like to do (1/4): ')

    if choice == '1':
        task = input('Name the task: ')
        add_task(task)

    elif choice == '2':
        view_task()

    elif choice =='3':
        print(f'These your current tasks: ')
        for t in enumerate(tasks, 1):
            print(t)
        removal = input('what number task would you like to remove?: ')
        remove_task(removal)
    
    elif choice == '4':
        break

    else:
        print('Wrong input, please retry.')



       


