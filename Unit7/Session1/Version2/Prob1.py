#unit 7
#session 1
#ver 2
#prob 1

def countdown(n):
  if n > 0:
    print(n)
    countdown(n - 1)

countdown(5)

def countdownIterative(n):
  while n > 0:
    print(n)
    n -= 1

countdownIterative(5)