from swap import swap
from matrix import test_matrices
from ship import ship
from palindrome import palindromefunction
from tree import tree

# Menu options as a dictionary
menu_options = {
    1: 'Palindrome',
    2: 'Tree',
    3: 'Listy',
    4: 'Swap',
    5: 'Matrix',
    6: 'Ship',
    7: 'Exit'
}

# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

# menu option 2
def numby():
    print('You chose \' 2 - Numby\'')

# menu option 3
def listy():
    print('You chose \'3 - Listy\'')

# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-6: '))
            if option == 1:
                palindromefunction()
            elif option == 2:
                tree()
            elif option == 3:
                listy()
            elif option == 4:
                input1 = input("first age")
                input2 = input("second age")
                a, b = swap(input1, input2)
                print(a, b)
            # Exit menu
            elif option == 5:
                test_matrices()
            elif option == 6:
                ship()
            elif option == 7:
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    print_menu2()
