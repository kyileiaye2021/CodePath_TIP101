# first and second fibo num are 0 and 1
# write a recursion func that will allow us to get nth fibo num in seq
# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8

def fibonacci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))
# Example Input: 6
# Expected Output: 8
# Explanation: The 6th Fibonacci number is 8. The 5th Fibonacci number is 5 and the 4th Fibonacci
# number is 3. 5 + 3 = 8.