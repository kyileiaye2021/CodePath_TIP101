#unit 7
#session 1
#ver 1
#prob 2

def factorial(n):
  #Base case
  if n == 0:
    return 1
  #Recursive case
  if n > 0 :
    return n*factorial(n-1)

print(factorial(5))