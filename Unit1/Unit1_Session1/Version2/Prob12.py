#unit 1
#session 1 veer 2
#Problem 12

#create a func with a positive int and returns its factorial
#create a variable to store the total factorial
#use a for loop with range func to count down back from the para to 1
#update total factorial var

def factorial(n):
  res = n
  for i in range(n-1,0, -1):
    res = res * i

  return res

print(factorial(3))