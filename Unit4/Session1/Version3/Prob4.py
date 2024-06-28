#unit 4
#session 1
#ver 3
#prob 4

# Assumption 
# the string cannot be empty or null
# The string can have both upper and lowercase letters
# The string has non letter char

# High level planning
# * Reverse list approach
#    * reverse the str and return
# * Two pointer approach
#    * compare two pointer var and swap if they both are letters

# Low level planning
# * create a list of char
# * create l and r
# * iterate thru the list until l passes r
#    * check if the l is letter
#        * check if the r is letter
#            * swap the two letter
#        * move the r to the left by 1
#    * move the l to right by 1

def reverse_only_letters(s):
  letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  char_lst = list(s)
  l, r = 0, len(char_lst) - 1
  
  while l < r:
    if char_lst[l] in letters:
      if char_lst[r] in letters:
        temp = char_lst[l]
        char_lst[l] = char_lst[r]
        char_lst[r] = temp
      r -= 1
    l += 1
  return "".join(char_lst)

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)