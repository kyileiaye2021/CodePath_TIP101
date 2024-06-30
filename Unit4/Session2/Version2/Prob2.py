#unit 4
#session 2
#ver2
#prob 2

# Assumption 
# if len of s is greater than len of t, return false

# Low Level Planning
# * return False if the size of the s is greater than that of t
# * create two pointers pointing to the first index of two str
# * iterate over the str until t pointer reaches to its end
#   * check if the char are the same, move both pointers forward by one
#   * move t char by one
# * return True if the len of s is equal to the curr index
# * otherwise False
def is_subsequence(s, t):
  if len(s) > len(t):
    return False
  s_index = 0
  t_index = 0
  while t_index < len(t):
    if s[s_index] == t[t_index]:
      s_index += 1
    
    t_index += 1

  return s_index == len(s)
    
s = "abc"
t = "ahbgdc"
print(is_subsequence(s, t))

a = "cba"
b = "ahbgdc"
print(is_subsequence(a, b))