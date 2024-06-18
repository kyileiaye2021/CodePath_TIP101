#Unit 1
#Problem Set VErsion 2
#Problem 2
#CAlculate difference

#create a func with two int type para
#return the difference which is int type
#always subtract the smaller number from the larger num

def difference(a, b):
  if a >= b:
    return a - b
  else:
    return b - a


print("diff =",difference(3, 8))