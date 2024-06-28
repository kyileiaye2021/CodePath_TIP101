#unit 4
#session 1
# ver 3
# prob 1

# iterate until the number the exceed the limit
# the number can start from 0 to any number less than limit

# itearte from 1 to untili the num exceed the limit

def find_highest_exponent(base, limit):
  i = 1
  while base ** i < limit:
    i += 1
  return i-1

exp = find_highest_exponent(2, 100)
print(exp)

exp2 = find_highest_exponent(3, 5)
print(exp2)