#unit 10
#session 1
#ver 3
#prob 5

# CAn the list have duplicates?

'''Happy CAse'''
# input - [1,2,3,4], target = 3
# output - [1,2]

'''Edge Case'''
# input - [], target = 2
# output - []

# input - [1,2], target = 4
# output - []

# Two pointer 
# create two pointers pointing to first index and last index
# iterate until first passes last
#   check the sum of first and last ele are the same as target
#      return [first index, last index]
#   check if the sum is greater than the target
#      decrement the high pointer by 1
#   otherwise, increment the low pointer by 1

def two_sum(numbers, target):
  low = 0
  high = len(numbers) - 1

  while low < high:
    num_sum = numbers[low] + numbers[high]
    if num_sum == target:
      return [low, high]

    elif num_sum > target:
        high -= 1
    else:
        low += 1

  return []

input = [2, 7, 11, 15]
target = 9
print(two_sum(input, target)) #[0, 1]

input = [1, 2, 3, 4, 4, 9]
target = 8
print(two_sum(input, target)) #[3,4]

input = [1, 2]
target = 4
print(two_sum(input, target)) # []

input = []
target = 4
print(two_sum(input, target)) # []