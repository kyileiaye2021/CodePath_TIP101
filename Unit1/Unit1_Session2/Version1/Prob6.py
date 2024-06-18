#Unit 1
#Session 2
#Ver 1
#Problem 6

#create a func with a list and an integer as params
#create a count var initialized to 0 
#use for loop and update the count var in each iteration if the current ele is less than the threshold
#return that count num (int)

def count_less_than(numbers, threshold):
  count_num = 0
  for ele in numbers:
    if ele < threshold:
      count_num += 1

  return count_num

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)