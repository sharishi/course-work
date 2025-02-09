import re
import os


def read_items(filename='items.txt'):
    """
    Читает данные из указанного файла и возвращает словарь с блюдами и их ингредиентами.

    Параметры:
    filename (str): Имя файла, из которого будут читаться данные. По умолчанию 'items.txt'.

    Возвращает:
    dict: Словарь, где ключами являются названия блюд, а значениями - списки ингредиентов.
          Возвращает пустой словарь, если файл не существует или пустой.
    """

    # Проверяем, существует ли файл и имеет ли он размер больше 0
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        return {}  # Если файл не существует или пуст, возвращаем пустой словарь

    # Открываем файл для чтения
    with open(filename, 'r') as file:
        data = {}  # Инициализируем пустой словарь для хранения данных

        # Читаем каждую строку из файла
        for line in file:
            # Разделяем строку на название блюда и ингредиенты
            dish, ingredients = line.strip().split(':')
            # Заполняем словарь, убирая лишние пробелы и разделяя ингредиенты по запятой
            data[dish.strip()] = [i.strip() for i in ingredients.split(',')]

        return data  # Возвращаем заполненный словарь


# Function to write data to the file
def write_items(data, filename='items.txt'):
    """
    Записывает данные о блюдах и их ингредиентах в указанный файл.

    Параметры:
    data (dict): Словарь, где ключами являются названия блюд, а значениями - списки ингредиентов.
    filename (str): Имя файла, в который будут записываться данные. По умолчанию 'items.txt'.
    """

    # Открываем файл для записи (если файл существует, он будет перезаписан)
    with open(filename, 'w') as file:
        # Проходим по каждому блюду и его ингредиентам в словаре
        for dish, ingredients in data.items():
            # Записываем название блюда и его ингредиенты в файл в формате "блюдо: ингредиент1, ингредиент2, ..."
            file.write(f"{dish}: {', '.join(ingredients)}\n")


# Функция для валидации названия ингредиента
def validate_ingredient(ingredient):
    """
    Проверяет, является ли ингредиент допустимым.

    Параметры:
    ingredient (str): Ингредиент, который нужно проверить.

    Возвращает:
    bool: True, если ингредиент соответствует требованиям, иначе False.
    """

    # Используем регулярное выражение для проверки формата ингредиента
    # Ингредиент должен содержать от 3 до 15 букв (латинские буквы)
    return re.match(r'^[A-Za-z]{3,15}$', ingredient) is not None


# Функция для валидации количества ингредиентов
def validate_ingredient_count(count):
    """
    Проверяет, является ли количество ингредиентов допустимым.

    Параметры:
    count (str): Количество ингредиентов, которое нужно проверить.

    Возвращает:
    bool: True, если количество соответствует требованиям, иначе False.
    """

    # Используем регулярное выражение для проверки формата количества
    # Количество должно быть числом от 1 до 99 (одна или две цифры)
    return re.match(r'^\d{1,2}$', count) is not None


# Функция для поиска блюд по ингредиенту
def find_dishes_by_ingredient(data, ingredient):
    """
    Находит блюда, содержащие указанный ингредиент.

    Параметры:
    data (dict): Словарь, где ключами являются названия блюд, а значениями - списки ингредиентов.
    ingredient (str): Ингредиент, по которому нужно искать блюда.

    Возвращает:
    tuple: Кортеж, содержащий два элемента:
        - Список названий блюд, содержащих указанный ингредиент.
        - Список строк, представляющих ингредиенты для найденных блюд.
    """

    # Приводим ингредиент к нижнему регистру для корректного сравнения
    ingredient = ingredient.lower()
    found_dishes = []  # Список для хранения найденных блюд
    ingredient_combinations = []  # Список для хранения строк с ингредиентами

    # Проходим по каждому блюду и его ингредиентам в словаре
    for dish, ingredients in data.items():
        # Проверяем, содержится ли ингредиент в списке ингредиентов (в нижнем регистре)
        if ingredient in [i.lower() for i in ingredients]:
            found_dishes.append(dish)  # Добавляем блюдо в список найденных
            ingredient_combinations.append(', '.join(ingredients))  # Добавляем строку с ингредиентами

    return found_dishes, ingredient_combinations  # Возвращаем найденные блюда и их ингредиенты


def update_ingredients(data, dish_name):
    """
    Обновляет список ингредиентов для указанного блюда.

    Параметры:
    data (dict): Словарь, где ключами являются названия блюд, а значениями - списки ингредиентов.
    dish_name (str): Название блюда, для которого нужно обновить ингредиенты.
    """

    # Проверяем, существует ли указанное блюдо в данных
    if dish_name not in data:
        print(f"Dish '{dish_name}' not found.")
        return

    # Отображаем текущие ингредиенты для указанного блюда
    print(f"Current ingredients for the dish '{dish_name}': {', '.join(data[dish_name])}")

    # Начинаем бесконечный цикл для обновления ингредиентов
    while True:
        print("\nWhat would you like to do?")
        print("1. Add ingredients.")
        print("2. Remove ingredients.")
        print("3. Replace all ingredients.")
        print("4. Exit.")
        choice = input("Choose an option (1, 2, 3, 4): ")

        # Добавление ингредиентов
        if choice == '1':
            count = input("How many ingredients do you want to add? (1-99): ")
            if not validate_ingredient_count(count):
                print("Error: The number of ingredients must be a number between 1 and 99.")
                continue

            new_ingredients = []
            for _ in range(int(count)):
                ingredient = input("Enter a new ingredient: ").strip()
                if not validate_ingredient(ingredient):
                    print("Error: Ingredient must only contain letters and be between 3 and 15 characters.")
                    break
                new_ingredients.append(ingredient.lower())  # Добавляем новый ингредиент в нижнем регистре

            data[dish_name].extend(new_ingredients)  # Добавляем новые ингредиенты к существующим
            print(f"Ingredients added: {', '.join(new_ingredients)}.")
            write_items(data)  # Сохраняем изменения в файл

        # Удаление ингредиентов
        elif choice == '2':
            to_remove = input("Enter the ingredients to remove, separated by commas: ").strip().split(',')
            to_remove = [i.strip().lower() for i in to_remove]  # Приводим ингредиенты к нижнему регистру
            initial_len = len(data[dish_name])  # Сохраняем начальную длину списка ингредиентов

            # Удаляем указанные ингредиенты
            data[dish_name] = [i for i in data[dish_name] if i not in to_remove]

            # Проверяем, были ли удалены ингредиенты
            if initial_len == len(data[dish_name]):
                print("None of the entered ingredients were found in the list.")
            else:
                print(f"Ingredients removed: {', '.join(to_remove)}.")
            write_items(data)  # Сохраняем изменения в файл

        # Замена всех ингредиентов
        elif choice == '3':
            count = input("Enter the new number of ingredients (1-99): ")
            if not validate_ingredient_count(count):
                print("Error: The number of ingredients must be a number between 1 and 99.")
                continue

            new_ingredients = []
            for _ in range(int(count)):
                ingredient = input("Enter a new ingredient: ").strip()
                if not validate_ingredient(ingredient):
                    print("Error: Ingredient must only contain letters and be between 3 and 15 characters.")
                    break
                new_ingredients.append(ingredient.lower())  # Добавляем новый ингредиент в нижнем регистре

            data[dish_name] = new_ingredients  # Заменяем список ингредиентов новым
            print(f"Ingredient list has been replaced. New ingredients: {', '.join(new_ingredients)}.")
            write_items(data)  # Сохраняем изменения в файл

        # Выход из цикла
        elif choice == '4':
            print("Ingredient modification completed.")
            break

        else:
            print("Invalid choice. Please try again.")  # Обработка недопустимого выбора

