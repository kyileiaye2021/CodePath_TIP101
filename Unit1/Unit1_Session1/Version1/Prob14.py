#create a func with two parameters (start and stop)
#returns an integer type total of the numbers within that range
#start and stop vars are both inclusive in the range
def sum_range(start, stop):
  total = 0
  for i in range(start, stop + 1):
    total += i
  return total

sum = sum_range(3,9)
print("sum =", sum)