#Unit 2
#session 1
#ver 2
#prob 4

#create a var to keep track of the total current sum
#iterate over the dict 
#check the value is even or not
#if it's, accumulate the total var

def sum_even_values(dictionary):
  total = 0
  for key in dictionary:
    if dictionary[key] % 2 == 0:
      total += dictionary[key]
  return total

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))