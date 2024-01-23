import sys
from operation import add, subtract, multiply, divide  

def checkOperation(num1, operator, num2):
    operationsDictionary = {
        'addition': add,
        'subtraction': subtract,  
        'multiplication': multiply,  
        'division': divide
    }
    
    operationPerform = operationsDictionary.get(operator)
    if operationPerform is not None:
        result = operationPerform(num1, num2)
        return result
    else:
        print("Invalid operation. Please choose from addition, subtraction, multiplication, or division.")
        return None

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
