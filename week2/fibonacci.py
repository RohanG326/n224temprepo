def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonaccifunction():
    x = int(input("How many terms do you want in fibonacci?"))
    if x <= 0:
        print("Not valid input")
    else:
        print("Sequence:")
        for i in range(x):
            print(fibonacci(i))

if __name__ == "__main__":
    fibonaccifunction()
