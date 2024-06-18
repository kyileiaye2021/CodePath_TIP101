#create a func that adds the sum of numbers from 1 to 10
#return the sum of total numbers from range of 1 to 10 inclusively
#create a total_sum int type var with initialization of 0 before the loop
#during the loop, add current elements to the total_sum to have the sum of all elements within the range

#range(start, stop) | iteration from start to stop -1

def sum_ten():
  total = 0
  for i in range(1, 11):
    total += i
  return total

total_sum = sum_ten()
print(total_sum)




