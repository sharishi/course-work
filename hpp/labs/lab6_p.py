import re


def input_data():
    pattern_name = r"^[A-Za-z]{1,10}(-[A-Za-z]{1,10}){0,5}$"
    pattern_kids = r"^(1[0-9]|\d)$"

    surname = input("Enter the employee's surname (Latin letters only): ")
    if not re.match(pattern_name, surname):
        print("Error: the surname must contain only Latin letters or a hyphen.")
        return
    name = input("Enter the employee's name (Latin letters only): ")

    if not re.match(pattern_name, name):
        print("Error: the name must contain only Latin letters or hyphens.")
        return
    children_count = input("Enter the number of children under 18 years of age (1-2 digits): ")
    if not re.match(pattern_kids, children_count):
        print("Error: the number of children should be a number between 0 and 20.")
        return

    with open("data.txt", "a") as file:
        file.write(f"{surname}\t{name}\t{children_count}\n")
    print("The data has been successfully saved.")


def view_data():
    try:
        with open("data.txt", "r") as file:
            total_kids = 0
            print("Staff list:")
            for line in file:
                line = line.strip()
                if line:
                    surname, name, children_count = line.split("\t")
                    print(f"Employee: {surname} {name}, number of children: {children_count}")
                    total_kids += int(children_count)
            print(f"Total number of children of all employees: {total_kids}")
    except FileNotFoundError:
        print("Data file not found.")


def show_menu():
    while True:
        print("\nMenu:")
        print("1. Enter data")
        print("2. View data")
        print("3. Get out")
        user_input = input("Select an option (1, 2, 3): ")

        match user_input:
            case '1':
                input_data()
            case '2':
                view_data()
            case '3':
                print("Exiting the program.")
                break
            case _:
                print("Wrong choice, try again.")


# Запуск программы
show_menu()
