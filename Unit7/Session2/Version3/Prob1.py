#unit 7
#session 2
#ver 3
#prob 1

# can s be empty or null? # (stop)
# can char not be in s? # return s

# s = "xaxbxc", char = 'x' -> abc
# s = "", char = 'x' -> ""

# high level plan
# base case: stop when s is empty (return "")
# recursive case: 
# check the curr char is equal to char
#   return the next positon 
# otherwise
#   return the curr char + next position


def remove_char(s, char):
  if len(s) == 0:
    return ""

  if s[0] == char:
    return remove_char(s[1:], char)

  else:
    return s[0] + remove_char(s[1:], char)


s = "xaxbxc"
char = "x"
print(remove_char(s, char))

s2 = ""
char2 = "x"
print(remove_char(s2, char2))


