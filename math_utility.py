import math

def factorial_calculation():
    n = int(input("Enter number: "))
    print("Factorial =", math.factorial(n))
def compound_interest():
    p = float(input("Enter Principal Amount: "))
    r = float(input("Enter rate of intrest (in %): "))
    t = float(input("Enter Time (In Years): "))
    amount = p * ((1 + r / 100) ** t)
    print("Compound Interest:", round(amount, 2))

def trigonometry():
    angle = float(input("Enter Angle in Degrees: "))
    rdn = math.radians(angle)
    print("Sin =", round(math.sin(rdn), 4))
    print("Cos =", round(math.cos(rdn), 4))
    print("Tan =", round(math.tan(rdn), 4))

def area_shapes():
    print("\n1. Circle")
    print("2. Rectangle")
    choice = input("Enter choice: ")
    if choice == "1":
        radius = float(input("Enter Radius: "))
        area = math.pi * radius * radius
        print("Area of circle =", round(area, 2))
    elif choice == "2":
        length = float(input("Enter Length: "))
        width = float(input("Enter Width: "))
        print("Area of rectangle =", length * width)
    else:
        print("Invalid Choice")

def math_menu():
    while True:
        print("==========================")
        print("Mathematical Operations")
        print("==========================")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back")

        choice = input("Enter Your choice: ")
        if choice == "1":
            factorial_calculation()
        elif choice == "2":
            compound_interest()
        elif choice == "3":
            trigonometry()
        elif choice == "4":
            area_shapes()
        elif choice == "5":
            break
        else:
            print("Invalid Choice")