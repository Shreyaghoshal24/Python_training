import sys
from operation import add, subtract, multiply, divide

def checkOperation(num1, operator, num2):
    if operator == 'add':
        return add(num1, num2)
    elif operator == 'sub':
        return subtract(num1, num2)
    elif operator == 'mult':
        return multiply(num1, num2)
    elif operator == 'div':
        return divide(num1, num2)
    else:
        return "Invalid operator. Please use add, sub, mult, div"

def main():
    if len(sys.argv) > 1:
        choice = " ".join(sys.argv[1:])
    else:
        choice = input("Enter your values like <number1> <operator> <number2> /exit: ")

    while True:
        values = choice.split()
        if values[0].lower() == 'exit':
            print("Exiting the program, bye!")
            break

        if len(values) != 3:
            print("Invalid input. Please enter values like <number1> <operator> <number2>.")
            break

        num1 = float(values[0])
        operator = values[1]
        num2 = float(values[2])

        result = checkOperation(num1, operator, num2)
        print(result)

        choice = input("Do you want to continue? Enter your values like <number1> <operator> <number2> /exit: ")

        if choice.lower() == '/exit':
            print("Exiting the program, bye!")
            break

if __name__ == "__main__":
    main()
