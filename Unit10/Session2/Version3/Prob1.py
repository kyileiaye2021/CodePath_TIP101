#unit 10
#session 2
#ver 3
#prob 1

# Problem 1: Count of Matches in Tournament

'''Happy Case'''
# Input - 7
# Output - 6

# Input - 14
# Output - 13

'''Edge Cases'''
# Input - 0
# Output - 0

# Input - 1
# Output - 0

# create a var to store total num of matches to 0
# while n is not 1
  # if it is even
  #   match = n /2
  #   n = match
  # if it is odd
  #   match = (n - 1) / 2
  #   n = match + 1
  # update the total num of matches
# return total num of matches

# time complexity - O(logn)
# space complexity - O(1)

def number_of_matches(n):
  total_matches = 0

  while n > 1:
    if n % 2 == 0:
      match = n // 2
      n = match

    else:
      match = (n - 1) // 2
      n = match + 1

    total_matches += match

  return total_matches

n = 7
print(number_of_matches(n)) #6

n = 14
print(number_of_matches(n)) # 13

n = 0
print(number_of_matches(n)) # 0

n = 1
print(number_of_matches(n)) # 0