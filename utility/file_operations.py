def create_file():
    filename = input("Enter File Name: ")
    file = open(filename, "w")
    file.close()
    print("File Created Successfully")


def write_file():
    filename = input("Enter File Name: ")
    data = input("Enter Data: ")

    file = open(filename, "w")
    file.write(data)
    file.close()

    print("Data Written Successfully")


def read_file():
    filename = input("Enter File Name: ")

    try:
        file = open(filename, "r")
        print("\nFile Content:")
        print(file.read())
        file.close()

    except FileNotFoundError:
        print("File Not Found")


def append_file():
    filename = input("Enter File Name: ")
    data = input("Enter Data: ")

    file = open(filename, "a")
    file.write("\n" + data)
    file.close()

    print("Data Appended Successfully")
def file_menu():
    while True:
        print("\n==========================")
        print("File Operations")
        print("==========================")
        print("1. Create a new File")
        print("2. Write to a File")
        print("3. Read from a File")
        print("4. Append to a File")
        print("5. Back to main menu")
        choice = input("Enter choice: ")
        if choice == "1":
            create_file()
        elif choice == "2":
            write_file()
        elif choice == "3":
            read_file()
        elif choice == "4":
            append_file()
        elif choice == "5":
            break
        else:
            print("Invalid Choice")
