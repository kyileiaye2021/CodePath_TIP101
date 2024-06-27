#checking prime number 
#divide the number by the num from the range of 2 to the num before that number
def is_prime(n):
  if n <= 1:
    return False

  i = 2
  while i < n:
    if n % i == 0:
      return False
    i += 1
    
  return True


print(is_prime(5))
print(is_prime(12))
print(is_prime(2))