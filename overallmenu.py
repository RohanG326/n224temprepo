from main import aboutme
from week1.swap import swapfunction
from week1.matrix import test_matrices
from week1.ship import ship
from week1.tree import tree
from week2.factorial import factfunction
from week2.fibonacci import fibonaccifunction
from week2.infodb import infoDB
from week3.challenge import timestable
from week3.factclass import factclass
from week3.fibclass import fibclass
from week3.palindrome import palindromefunction
from week4.coinflip import flip
from week4.logiccircuts import logic



main_menu = [
    ["About Me", aboutme],
    ["InfoDB", infoDB],
    ["Swap", swapfunction],
    ["Coin Flip", flip],
    ["Logic Gate", logic],



]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu1 = [
    ["Ship", ship],
    ["Tree", tree],
    ["Matrix", test_matrices],

]

sub_menu2 = [
    ["Palindrome Class", palindromefunction],
    ["Factorial Class", factclass],
    ["Factorial Imperative", factfunction],
    ["Fibonacci Class", fibclass],
    ["Fibonacci Imperative", fibonaccifunction],

]


# Menu banner is typically defined by menu owner
border = u"\033[1;32;40m"
submenu1 = u"\033[1;32;40m"
submenu2 = u"\033[1;32;40m"

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Designs", submenu1])
    menu_list.append(["Patterns", submenu2])
    buildMenu(title, menu_list)




  
# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()




  
def submenu1():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu1)

def submenu2():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu2)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
