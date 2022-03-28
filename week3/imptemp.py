def celsius():
    x = int(input("What temperature of Celsius do you want to convert to Fahrenheit?"))
    cel = (x * 1.8) + 32
    print(f"The temperature is {cel} degrees Fahrenheit")
    return cel


def fahrenheit():
    x = int(input("What temperature of Fahrenheit do you want to convert to Celsius?"))
    fah = (x - 32) * 5 / 9
    print(f"The temperature is {fah} degrees Celsius")


def tempconversion():
    while True:
        try:
            option = int(input('Fahrenheit(1) or Celsius(2)'))
            if option == 1:
                fahrenheit()
            elif option == 2:
                celsius()
            else:
                print('Invalid option. Please enter a number between 1 and 3.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')


if __name__ == "__main__":
    print(tempconversion())
