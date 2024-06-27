def is_perfect_number(n):
  sum = 0
  for i in range(1, n):
    if n % i == 0:
      sum += i
  if n == sum:
    return True

  return False

print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9))