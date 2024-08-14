# unit 10
# session 2
# ver 3
# prob 3

'''Happy Case'''
# Input: n = 16
# Output: True

# Input: n = 5
# Output: False

'''Edge Case'''
# Input: n = 1
# Output: True

# iterative approach
# iterate until n becomes 1
#   n = divide n by 4
#   remainder = n % 4
# check if remainder is 0
#   return True
def is_power_of_four(n):

  while n % 4 == 0:
    n = n // 4

  return n == 1

n = 16
print(is_power_of_four(n)) # True

n = 5
print(is_power_of_four(n)) # False

n = 1
print(is_power_of_four(n)) # True