import functions as func


def main():
    data = func.read_items()

    # Предоставим пользователю список блюд
    if len(data) == 0:
        print("The file is empty or does not exist. Dishes are missing.")
    else:
        print("List of dishes:")
        for idx, dish in enumerate(data, 1):
            print(f"{idx}. {dish}")

    while True:
        try:
            print("\nHi! What do you want to do?")
            print("1. Find dishes by ingredient.")
            print("2. Add or change a dish.")
            print("3. Exit.")
            choice = int(input("Select an action (1, 2, 3): "))

            match choice:
                case 1:
                    # Найти блюда по ингредиенту
                    ingredient = input("Enter the name of the ingredient (3 to 15 letters): ")
                    if not func.validate_ingredient(ingredient):
                        print(
                            "Error: the ingredient must contain only letters and be between 3 and 15 characters long.")
                        continue
                    found_dishes, ingredient_combinations = func.find_dishes_by_ingredient(data, ingredient)
                    if len(found_dishes) == 0:
                        print(f"Ingredient '{ingredient}' not found in any of the dishes.")
                    else:
                        print(f"This ingredient was found in {len(found_dishes)} dishes: {', '.join(found_dishes)}")
                        print("Ingredient combinations:")
                    for dish, combo in zip(found_dishes, ingredient_combinations):
                        print(f"{dish}: {combo}")
                case 2:
                    # Добавить или изменить блюдо
                    dish_name = input("Enter the name of the dish: ").strip()
                    if dish_name not in data:
                        print(f"Dish '{dish_name}' not found on the list. It will be added.")
                    else:
                        u_input = input(
                            f"Dish '{dish_name}' is already in the list. Do you want to change it?.(yes/no)").lower()
                        if u_input == "yes":
                            func.update_ingredients(data, dish_name)
                            continue
                        elif u_input == "no":
                            continue
                        else:
                            print("Wrong choice. Try again.")

                    count = input("Enter the number of ingredients (1-99): ")
                    if not func.validate_ingredient_count(count):
                        print("Error: the number of ingredients should be a number between 1 and 99.")
                        continue

                    ingredients = []
                    for _ in range(int(count)):
                        ingredient = input("Enter only one ingredient from the list: ").strip()
                        if not func.validate_ingredient(ingredient):
                            print(
                                "Error: the ingredient must contain only letters and be between 3 and 15 characters long.")
                            break
                        ingredients.append(ingredient.lower())
                    else:
                        data[dish_name] = ingredients
                        print(f"Dish '{dish_name}' and its ingredients are preserved.")

                case 3:
                    # exit
                    func.write_items(data)
                    print("Goodbye!")
                    break

                case _:
                    print("Wrong choice. Try again.")
        except ValueError:
            print("Error: Incorrect number format! Please enter a number.")


main()

