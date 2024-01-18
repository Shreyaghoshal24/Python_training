import sys
from operation import add, subtract, multiply, divide


def main():
    if len(sys.argv) > 1:
        choice = " ".join(sys.argv[1:])
    else:
        choice = input(
            "Enter your values like <number1> <operator> <number2> /exit: ")

    while True:
        values = choice.split()
        if values[0].lower() == 'exit':
            print("Exiting the program, bye!")
            break
            # return choice == 'y'

        if len(values) != 3:
            print(
                "Invalid input. Please enter values like <number1> <operator> <number2>.")
            break

        # if 'exit' in sys.argv:
        #     print("Exiting the program.")
        #     sys.exit()

        num1 = float(values[0])
        operator = values[1]
        num2 = float(values[2])

        if operator == 'add':
            result = add(num1, num2)
        elif operator == 'sub':
            result = subtract(num1, num2)
        elif operator == 'mult':
            result = multiply(num1, num2)
        elif operator == 'div':
            result = divide(num1, num2)
        else:
            print("Invalid operator. Please use add, sub, mult, div")
            break  # If the operator is invalid, exit the loop

        print(result)

        # Ask the user whether to continue or exit
        choice = input(
            "Do you want to continue? Enter your values like <number1> <operator> <number2> /exit: ")

        if choice.lower() == '/exit':
            print("Exiting the program, bye!")
            break


if __name__ == "__main__":
    main()
