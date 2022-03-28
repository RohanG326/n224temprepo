def timestable():
    adi = int(input("Enter number 10-99"))
    if 10 <= adi <= 99:
        y = int(adi / 10)
        z = adi % 10
        for i in range(9):
            a = y * i
            b = z * i
            bx = int(b / 10)
            monkey = adi * i
            print(f"{a}" + " || " + f"{b}" + " || " + f"({a} + {bx})" + " || " + f"{monkey}")
    else:
        print("invalid input")


if __name__ == "__main__":
    timestable()
