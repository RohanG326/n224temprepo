#imported library
import random

#chooses between 0 and 1. if it is 0 its heads but if its anything else so 0 it is tails
def flip():
  flip = random.randint(0,1)
  if flip == 0:
    print ("Head")
  else:
    print ("Tails")

if __name__ == "__main__":
    flip()