import json
import os

FILE_NAME = "data/data.json"

def load_tasks():
    """
    Загружает список задач из JSON файла.
    Loads the list of tasks from the JSON file.

    :return: Список задач
    :rtype: list
    """
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)

def save_tasks(tasks):
    """
    Сохраняет список задач в JSON файл.
    Saves the list of tasks to the JSON file.

    :param tasks: Список задач
    :type tasks: list
    """
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)
