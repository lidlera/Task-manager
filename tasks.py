from storage import load_tasks, save_tasks

def add_task(title):
    """
    Добавляет новую задачу.
    Adds a new task.

    :param title: Task title
    :type title: str
    """
    tasks = load_tasks()
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added.")

def list_tasks():
    """
    Выводит все задачи с их статусом.
    Displays all tasks with their status.
    """
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. [{status}] {task['title']}")

def complete_task(task_id):
    """
    Отмечает задачу как выполненную по её ID.

    :param task_id: Индекс задачи в списке
    :type task_id: int

    Marks a task as completed by its ID.

    :param task_id: Index of the task in the list
    :type task_id: int
    """
    tasks = load_tasks()
    try:
        tasks[task_id]["completed"] = True
        save_tasks(tasks)
        print("Task completed.")
    except IndexError:
        print("Task with this ID not found.")

def delete_task(task_id):
    """
    Удаляет задачу по её ID.

    :param task_id: Индекс задачи в списке
    :type task_id: int
    
    Deletes a task by its ID.

    :param task_id: Index of the task in the list
    :type task_id: int
    """
    tasks = load_tasks()
    try:
        tasks.pop(task_id)
        save_tasks(tasks)
        print("Task deleted.")
    except IndexError:
        print("Task with this ID not found.")
