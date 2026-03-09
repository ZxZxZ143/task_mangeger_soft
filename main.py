tasks = []


def menu():
    while True:
        print("\nTask Manager")
        print("1 Add task")
        print("2 List tasks")
        print("0 Exit")

        choice = input("Choose: ")

        if choice == "1":
            print("Add task not implemented yet")
        elif choice == "2":
            print("List tasks not implemented yet")
        elif choice == "0":
            break
        else:
            print("Invalid choice")


menu()