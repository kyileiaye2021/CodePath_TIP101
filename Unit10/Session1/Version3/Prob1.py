#unit 10
#session 1
#ver 3
#Prob 1

# Questions
# is it possible that n = 0?

# Happy Case
# in - n = 2
# out - 2

# in - n = 3
# out - 3

# in - n = 4
# * 1,1,1,1
# * 1,1,2
# * 1, 2, 1
# * 2, 1, 1
# * 2, 2
# out - 5

# in - 5
# * 1,1,1,1,1
# * 1,2,2
# * 2, 1, 2
# * 2,2, 1
# * 1,1, 1, 2
# * 1, 2, 1, 1
# * 1,1,2,1
# * 2, 1,1, 1
# out - 8

'''Edge cases'''
# in - n = 0
# out - 1

# in - n = 1
# out - 1

# Dynamic programming 
# check if the stair is 0 or 1
#  return 1
# create a var to store the last curr ways
# create two vars to store prev1 and prev2 ways
# iterate until i = 0 reaches to n steps
#   curr ways = prev1 + prev2
#   temp = prev2
#   prev2 = curr ways
#   prev1 = temp
# return last curr ways

def climb_stairs(n):
  if n < 2:
    return 1

  prev1, prev2 = 1,1

  for _ in range(n-1):
    curr_ways = prev1 + prev2
    temp = prev2
    prev2 = curr_ways
    prev1 = temp

  return prev2

n = 2
print(climb_stairs(n)) # 2

n = 3
print(climb_stairs(n)) # 3

n = 4
print(climb_stairs(n)) # 5

n = 1
print(climb_stairs(n)) # 1

n = 0
print(climb_stairs(n)) # 1


