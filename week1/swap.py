def swap(age1, age2):
    a = age1
    b = age2
    if a <= b:
        return a, b
    else:
        return b, a

if __name__ == "__main__":
    input1 = input("first age")
    input2 = input("second age")
    a, b = swap(input1, input2)
    print(a, b)

