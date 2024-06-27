#unit 4
#session 1
#ver2
#prob 1

# Assumption 
# n is a positive integer
# n cannot be 0

# * Iterative Approach
# * create a var sum
# * create an index 1
# * iterate from 1 to n-1
  # * in each iteraton, check if n is divisible by current index
    # * add curr index to the sum
# * compare sum with n
  # * return trure if it's equal
# return False

def is_perfect_number(n):
  sum = 0
  for i in range(1, n):
    if n % i == 0:
      sum += i
  if n == sum:
    return True
    
  return False
  
print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9))
