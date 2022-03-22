from week1.swap import swapfunction
from week1.matrix import test_matrices
from week1.ship import ship
from week1.palindrome import palindromefunction
from week1.tree import tree
from week2.factorial import factfunction
from week2.fibonacci import fibonaccifunction
from week2.infodb import infoDB
from main import aboutme

main_menu = [
    ["About Me", aboutme],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Swap", swapfunction],
    ["Palindrome", palindromefunction],
    ["Ship", ship],
    ["Tree", tree],
    ["Matrix", test_matrices]
]

week_2_sub_menu = [
    ["Factorial", factfunction],
    ["Fibonacci", fibonaccifunction],
    ["InfoDB", infoDB],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Week 1", submenu])
    menu_list.append(["Week 2", week2_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)

def week2_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, week_2_sub_menu)

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
