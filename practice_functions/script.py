# Function to calculate the square of a number
def square(number):
    return number ** 2

# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function to find the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Function to print a list in reverse order
def reverse_list(input_list):
    return input_list[::-1]

# Function to find the maximum element in a list
def find_max(input_list):
    return max(input_list)

# Function to create a dictionary from two lists
def create_dictionary(keys, values):
    return dict(zip(keys, values))

# Main part of the script for testing
if __name__ == "__main__":
    # Test square function
    print("Square of 5:", square(5))

    # Test even/odd function
    print("Is 7 even or odd?", check_even_odd(7))

    # Test factorial function
    print("Factorial of 4:", factorial(4))

    # Test reverse list function
    my_list = [1, 2, 3, 4, 5]
    print("Reversed list:", reverse_list(my_list))

    # Test find max function
    another_list = [10, 5, 8, 15, 2]
    print("Maximum element in the list:", find_max(another_list))

    # Test create dictionary function
    keys_list = ['name', 'age', 'city']
    values_list = ['John', 25, 'New York']
    print("Created Dictionary:", create_dictionary(keys_list, values_list))
