from datetime import datetime
import time
import random
import string
import uuid
import importlib

from utility.math_utility import math_menu
from utility.file_operations import file_menu

def main():
    while True:
        print("================================")
        print("Welcome to Multi-Utility Toolkit")
        print("================================")
        print("Choose an Option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate UUID")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("Enter Your Choice: ")
        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            generate_uuid()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_module()
        elif choice == "7":
            print("Thank You for using multi-utility tookit!")
            break
        else:
            print("Invalid Choice")


def show_current_datetime():
    print("Current Date and Time:")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def date_difference():
    print("Date Difference")
    d1 = input("Enter the first date (YYYY-MM-DD): ")
    d2 = input("Enter the second date (YYYY-MM-DD): ")
    date1 = datetime.strptime(d1, "%Y-%m-%d")
    date2 = datetime.strptime(d2, "%Y-%m-%d")
    diff = (date2 - date1).days
    print("Difference:", diff, "days")

def format_date():
    date_str = input("Enter date (YYYY-MM-DD): ")
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    print("Formatted Date:")
    print(date_obj.strftime("%d-%m-%Y"))

def stopwatch():
    print("Stopwatch")
    input("Press Enter to Start...")
    start = time.perf_counter()
    input("Press Enter to Stop...")
    end = time.perf_counter()
    print("Elapsed Time:", round(end - start, 2), "seconds")

def countdown_timer():
    sec = int(input("Enter countdown seconds: "))
    for i in range(sec, 0, -1):
        print(i)
        time.sleep(1)
    print("Time's Up!")

def datetime_menu():
    while True:
        print("==========================")
        print("Datetime and Time Operations")
        print("==========================")
        print("1. Display Current Date and Time")
        print("2. Calculate Difference Between Two Dates/times")
        print("3. Format Date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to main menu")

        choice = input("Enter Your choice: ")
        if choice == "1":
            show_current_datetime()
        elif choice == "2":
            date_difference()
        elif choice == "3":
            format_date()
        elif choice == "4":
            stopwatch()
        elif choice == "5":
            countdown_timer()
        elif choice == "6":
            break
        else:
            print("Invalid Choice")


def random_number():
    print("Random Number:", random.randint(1, 100))
def random_list():
    print("Random List:",
          random.sample(range(1, 100), 5))
def random_password():
    length = int(input("Enter Password Length: "))
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    password = ""
    for i in range(length):
        password += random.choice(chars)
    print("Generated Password:", password)
def random_otp():
    otp = random.randint(100000, 999999)
    print("Generated OTP:", otp)

def random_menu():
    while True:
        print("==========================")
        print("Random Data Generation")
        print("==========================")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back")

        choice = input("Enter choice: ")
        if choice == "1":
            random_number()
        elif choice == "2":
            random_list()
        elif choice == "3":
            random_password()
        elif choice == "4":
            random_otp()
        elif choice == "5":
            break
        else:
            print("Invalid Choice")


def generate_uuid():
    unique_id = uuid.uuid4()
    print("Generated UUID:")
    print(unique_id)


def explore_module():
    module_name = input("Enter Module Name: ")
    try:
        module = importlib.import_module(module_name)
        print("\nAvailable Attributes:")
        print(dir(module))
    except:
        print("Module Not Found")


if __name__ == "__main__":
    main()