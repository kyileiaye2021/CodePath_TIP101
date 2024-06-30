#unit 4
#session 2
#ver 1
#Prob 3

# Low Level Planning
# * Two pointer approach
# * create a char_lst cause s is not mutable
# * create two pointers
# * iterate over the list until left passess the right pointer
#     * check if the left var equal to the right var
#       * move left and right inwards
#     * check if the left var not equal right var and if one ele is not removed already
#       * remove the right var
#       * decrement the right one by 1
#     * otherwise, False

def valid_palindrome(s):
  char_lst = list(s)
  left = 0
  right = len(char_lst) - 1
  already_remove = False

  while left < right:
    if char_lst[left] == char_lst[right]:
      left += 1
      right -= 1

    elif char_lst[left] != char_lst[right] and not already_remove:
      char_lst.remove(char_lst[right])
      already_remove = True
      right -= 1

    else:
      return False
  return True

s = "aba"
s2 = "abca"
s3 = "abc"

print(valid_palindrome(s))
print(valid_palindrome(s2))
print(valid_palindrome(s3))