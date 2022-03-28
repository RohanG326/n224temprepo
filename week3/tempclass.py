class Conversion:
    def __init__(self):
        self.temp = 0

    def __call__(self, n):
        fah = (n * 1.8) + 32
        print(fah)


def tempclass():
    x = int(input("Convert Celsius to Fahrenheit"))
    fahrenheit = Conversion()
    print(fahrenheit(x))



def tester():
    testvals = [0, 10, 20, 30]
    for i in range(len(testvals)):
        fahrenheit = Conversion()
        print(fahrenheit(i))

if __name__ == "__main__":
    tester()
