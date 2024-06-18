#create a func with an integer positive parameters
#the func returns the total sum (int type) of the numbers from 1 to the integer argument
#initialize a var to store the total sum before the loop to 0
# update it in the loop by adding the current element of the loop
#range(1,stop) to get the range of 1 to stop

def sum_positive_range(stop):
  total = 0
  for i in range(1, stop + 1):
    total += i
  return total

print(sum_positive_range(6))
