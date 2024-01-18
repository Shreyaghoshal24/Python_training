from operation import add, subtract, multiply, divide

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Oops! That doesn't look like a number. Please enter a numeric value.")

def get_operation_choice():
    while True:
        print("Alright, let's do some math:")
        print("Add, Subtract, Multiply, Divide")

        choice = input("Choose an operation (add/sub/mult/div): ").lower()

        if choice in ('add', 'sub', 'mult', 'div'):
            return choice
        else:
            print("Oops! That's not a valid choice. Please enter one of: add, sub, mult, div.")

def ask_to_continue():
    choice = input("Do you want to continue? (y/n): ").lower()
    return choice == 'y'

def main():
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")

    while True:
        choice = get_operation_choice()

        if choice == 'add':
            result = add(a, b)
        elif choice == 'sub':
            result = subtract(a, b)
        elif choice == 'mult':
            result = multiply(a, b)
        elif choice == 'div':
            result = divide(a, b)
        else:
            continue

        print(f"The result is: {result}")

        if not ask_to_continue():
            break

if __name__ == "__main__":
    main()
