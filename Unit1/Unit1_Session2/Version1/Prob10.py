#unit 1
#session 2
#ver 1
#problem 10

#create a func with an integer
#if the current ele is divisibel by 3, print fizz
##if the current ele is divisibel by 5, print buzz

def fizzbuzz(n):
  for ele in range(1, n+1):
    if ele % 3 == 0:
      print("Fizz")

    elif ele % 5 == 0:
      print("Buzz")

    else:
      print(ele)

fizzbuzz(13)