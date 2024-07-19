#unit 7
#session 1
#ver 3
#prob 3


# n will be non-neg nums
# n = 0, return 0
# n = 100, return 1
# n = -1, return none

# divide the digit by 10
# add the remainder to next func call

# n = 523
# n / 10 = 52 (remainder = 3)
# n / 10 = 5 (remainder = 2)
# n / 10 = 0 (remainder = 5) [stop here]

'''
Time complexity: O(logn) the size of the input is reduced by the factor of 10
Space complexity O(logn) the depth of the recursion equal to the num of times that n can be divided by 10'''
def sum_digits(n):
  if n < 0:
    return None
  if n == 0:
    return 0
  remainder = n % 10
  return remainder + sum_digits(n // 10)

print(sum_digits(523)) #10
print(sum_digits(0)) #0
print(sum_digits(-1)) #none
