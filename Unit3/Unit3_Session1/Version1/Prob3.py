#unit 3
#session 1
#ver 1
#prob 3

#check the upper and lower cases
def is_pangram(my_str):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  for letter in alphabet:
    if letter not in my_str:
      return False
  return True


my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))