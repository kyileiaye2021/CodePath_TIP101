#unit 7
#session1
#ver 2
#prob 4

'''
Time complexity: 
if n == 1: func called 1 time
if n == 2, func called 1 time
if n == 3, func called 1 time
if n == 4, func called 1 time
...
if n == 16, func called 2 times
...
if n== 64, func called 3 times
The n is reduced by the factor of 4 so time complexity log(n)

Space complexity:
Up to n = 15, the stack of the recursion is 1
Up to n = 63, the stack of the recursion is 2
Up to n = 255, the stack of the recursion is 3
The recursion depth is proportional to the num of times n can be divided by 4
so space complexity is log(n)
'''
# n can be 1 and greater than 1 ()
# n cannot be 0 or -1

# each time we have to divide it by 4 and check if the num is divisible
# base case would be 1 (stop when n = 1)

def is_power_of_four(n):
  if n == 1: #base case
    return True
  if n <= 0 or (n % 4) != 0: # if the number is not divisible by 4 at first place, it will return false
    return False
  return is_power_of_four(n // 4)

print(is_power_of_four(5))

