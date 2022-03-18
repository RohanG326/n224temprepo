def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factfunction():
    try:
        num = int(input("Enter a number for factorial: "))
        if num >= 0:
            print("The factorial of", num, "is", factorial(num))
        else:
            print("Sorry, factorial does not exist for negative numbers")
    except ValueError:
        print('Invalid input. Please enter an integer input.')

if __name__ == "__main__":
    factfunction()
