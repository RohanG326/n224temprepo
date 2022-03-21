from week1.swap import swapfunction
from week1.matrix import test_matrices
from week1.ship import ship
from week1.palindrome import palindromefunction
from week1.tree import tree
from week2.factorial import factfunction
from week2.fibonacci import fibonaccifunction

menu_options = {
    1: 'Palindrome',
    2: 'Factorial',
    3: 'Tree',
    4: 'Swap',
    5: 'Matrix',
    6: 'Ship',
    7: 'Fibonacci',
    8: 'Exit'
}

# Print menu options from dictionary key/value pair
def menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-8: '))
            if option == 1:
                palindromefunction()
            elif option == 2:
                factfunction()
            elif option == 3:
                tree()
            elif option == 4:
                swapfunction()
            elif option == 5:
                test_matrices()
            elif option == 6:
                ship()
            elif option == 7:
                fibonaccifunction()
            elif option == 8:
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    menu()
