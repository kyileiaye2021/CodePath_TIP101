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