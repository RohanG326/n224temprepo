class Factorial:
    def __init__(self):
        self.fact = 1

    def __call__(self, n):
        for i in range(1, n + 1):
            self.fact = self.fact * i
        return self.fact


def factclass():
    x = int(input("Compute the factorial Number"))
    if x < 0:
        print("Sorry, factorial doesn't exist for negative numbers")
    else:
        fact_of = Factorial()
        print(fact_of(x))


if __name__ == "__main__":
    factclass()
