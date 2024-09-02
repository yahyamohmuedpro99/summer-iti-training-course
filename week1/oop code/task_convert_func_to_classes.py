def add_task(tasks, task):
    tasks.append(task)

def remove_task(tasks, task):
    tasks.remove(task)

def list_tasks(tasks):
    for task in tasks:
        print(task)

# Example usage
tasks = []
add_task(tasks, "Buy groceries")
add_task(tasks, "Read a book")
list_tasks(tasks)
remove_task(tasks, "Buy groceries")
list_tasks(tasks)

# add functionality that not exist e.g(edit,list_tasks_at_spcific_time,...)
