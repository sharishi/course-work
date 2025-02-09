def add_tolist(mylist, item):
    if item in mylist:
        user_input = input("This item is already in the list. Do you want to add it again?(Yes/No): ")
        if user_input.lower() == "no":
            return
    print(f"You just added {item} to the list")
    mylist.append(item)


def delete_fromlist(mylist, item):
    if item not in mylist:
        print("We don't have this item in our list. Please try again")
        return
    while item in mylist:
        mylist.remove(item)
    print(f"You just removed {item} from the list")


def print_list(my_list):
    print("Your list:")
    for i in my_list:
        print(i)


def show_menu():
    print("Menu:")
    print("1. Display the list of current products: ")
    print("2. Add item to list: ")
    print("3. Remove an item from the list:")
    print("4. Exit:")


def shop_list(mylist = []):
    while True:
        try:
            show_menu()
            user_input = int(input("Enter the option number: "))

            match user_input:
                case 1:
                    print_list(mylist)
                case 2:
                    item_input = str(input("Enter the item you want to add: "))
                    add_tolist(mylist, item_input)
                    print_list(mylist)
                case 3:
                    item_remove = str(input("Enter the item you want to remove: "))
                    delete_fromlist(mylist, item_remove)
                    print_list(mylist)
                case 4:
                    print("We'll be happy to see you again!")
                    break
                case _:
                    print("You entered the wrong option number. Please try again =)")
        except ValueError:
            print("Error: Incorrect number format! Please enter a number.")


mylist = ['turmeric', 'coffee', 'tea', 'croissant']
shop_list(mylist)
