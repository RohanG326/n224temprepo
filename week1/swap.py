#sets 2 variables a and b as age one and age 2. One is enterd it will swap the ages to b,a
def swap(age1, age2):
    a = age1
    b = age2
    if a <= b:
        return a, b
    else:
        return b, a
def swapfunction():
    input1 = input("first age")
    input2 = input("second age")
    a, b = swap(input1, input2)
    print(a, b)

if __name__ == "__main__":
    swapfunction()

