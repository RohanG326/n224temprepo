class Fibonacci:
    def __init__(self):
        self.fiboSeq = [0, 1]
    def __call__(self, n):
        if n < len(self.fiboSeq):
            return self.fiboSeq[n]
        else:
            # Compute the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2) # two recursive calls to self (__call__(self, n))
            self.fiboSeq.append(fib_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.fiboSeq[n]


def fibclass():
    x = int(input("Compute the Fibonacci Number"))
    fibo_of = Fibonacci()
    print(fibo_of(x))

if __name__ == "__main__":
    fibclass()