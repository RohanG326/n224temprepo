import random

def flip():
  flip = random.randint(0,1)
  if flip == 0:
    print ("Head")
  else:
    print ("Tails")

if __name__ == "__main__":
    flip()