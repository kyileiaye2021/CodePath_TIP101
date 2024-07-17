#unit 7
#session1
#ver 2
#prob 4

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

