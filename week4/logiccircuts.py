def logic():

  def AND (x,y):
      if x==1 and y==1:
        return True
      else: return False

  def OR (x,y):
    if x==1 or y==1:
       return True
    else: return False


  print(AND(0,0))
  print(AND(0,1))
  print(AND(1,0))
  print(AND(1,1))
  
  print(OR(0,0))
  print(OR(0,1))
  print(OR(1,0))
  print(OR(1,1))
if __name__ == "__main__":
    logic()
  