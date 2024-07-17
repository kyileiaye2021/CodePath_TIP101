#unit 7
#session 1
#ver 1
#prob 4

# Time complexity : O(logn) in each iteration call, the num is reduced by the factor of 2
# Space complexity: O(logn) the depth of the stack is proportional to the num of times n can be divided by 2
# n = 64 / 2
# n = 32 / 2
# n = 16 / 2
# n = 8 / 2
# n = 4 / 2
# n = 2 / 2
# n = 1 (stop) (remainder = 0) 
# n can never be 0 or neg num

def is_power_of_two(n):
  if n == 1: 
    return True
  if n < 0:
    return False
  if n % 2 == 0:
    return is_power_of_two(n // 2)
  else:
    return False

print(is_power_of_two(64))
print(is_power_of_two(5))