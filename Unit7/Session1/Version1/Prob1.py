def repeat_hello(n):
  if n > 0:
    print("Hello")
    repeat_hello(n - 1)

repeat_hello(5)
print() 
def repeat_hello_iterative(n):
  while n > 0:
    print('Hello')
    n -= 1

repeat_hello_iterative(5)