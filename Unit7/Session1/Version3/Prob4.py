#unit 7
#session 1
#ver 3
#prob 4

#count the num of 7 in the non neg integer n
# n = 75, return 1
# n = 55, return 0
# n = 0, return 0
# n = -3, return None

# n = 75
# n = 75/10= 7 
# n = 7/ 10 = 0 (stop)

# n = 55
# n = 55 // 10 = 5
# n = 5 / 10 = 0
def count_sevens(n):
  #base case
  if n < 0:
    return None
  if n == 0:
    return 0
  if n % 10 == 7: #if 7 is found in the n
    return 1 + count_sevens(n // 10)
  return count_sevens(n/10)

print(count_sevens(727))
# Example Input: 727
# Expected Output: 2
# Explanation: 2 digits with value 7 in the number 727