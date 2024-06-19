#unit 3
#session 1
#ver 1
#prob 4


def reverse_string(my_str):
  new_str = ""
  for letter in range(len(my_str)-1, -1, -1): #range(start, stop, step)
    new_str += my_str[letter]
  return new_str

my_str = "live"
print(reverse_string(my_str))