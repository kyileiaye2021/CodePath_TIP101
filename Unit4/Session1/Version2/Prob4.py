#unit 4
#session 1
#ver 2
#prob 4


# Assumption
# every char in the str is lowercase
# empty str is possible
# str cannot be null

# High Level Planning
# * Two pointer technique
#   * create two pointers. iterate over the list and compare two pointer var. 
#   * if both pointers are the same, go to the next item
#   * if not, check which one is smaller lexicographically
#   * assign the larger char with the smaller char

# Low level planning
# * create a list of char from the str
# * create two pointers
# * iterate over the lst until l passes r
#    * check if l and r var are not the same
#      * check if r var > l var lexi
#        * assign r var with l var
#      * assign l var with r var
#    * shift l to right by 1 and r to left by 1
# * return the joined list

def make_palindrome(s):
  char_lst = list(s)
  left = 0
  right = len(char_lst) - 1
  while left < right:
    if char_lst[left] != char_lst[right]:
      if char_lst[right] > char_lst[left]:
        char_lst[right] = char_lst[left]
      else:
        char_lst[left] = char_lst[right]
    left += 1
    right -= 1

  return "".join(char_lst)

s = "egcfe"
s_pal = make_palindrome(s)
print(s_pal)
# s_pal == "efcfe"
# The min number of operations to make s a palindrome is 1 by changing `f` to `g`
# another palindrome possible is "egcge", but it is not lexicographically smaller

s1 = "abcd"
s_pal1 = make_palindrome(s1)
print(s_pal1)
# s_pal == "abba"
# The min number of operations to make s a palindrome is 2 by changing `c` to `b` and `d` to `a`
# a palindrome cannot be created in 1 operation

s2 = "seven"
s_pal2 = make_palindrome(s2)
print(s_pal2)
# s_pal == "neven"
# The min number of operations to make s a palindrome is 1 by changing `s` to `n`
# to get a palindrome that is lexographically smaller, it would take more operations