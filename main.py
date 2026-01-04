from tasks import add_task, list_tasks, complete_task, delete_task

def show_menu():
    """
    Отображает главное меню приложения.
    Displays the main menu of the application.
    """
    print("\nTask Manager")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Выполнить задачу")
    print("4. Удалить задачу")
    print("0. Выход")

def main():
    """
    Основной цикл приложения.
    Обрабатывает ввод пользователя и вызывает функции работы с задачами.
    Main application loop.
    Handles user input and calls task functions.
    """
    while True:
        show_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Название задачи: ")
            add_task(title)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_id = int(input("ID задачи: "))
            complete_task(task_id)
        elif choice == "4":
            task_id = int(input("ID задачи: "))
            delete_task(task_id)
        elif choice == "0":
            print("Выход из приложения.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
