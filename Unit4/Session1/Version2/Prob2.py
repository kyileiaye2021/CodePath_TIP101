#unit 4
#session 1
#ver 2
#prob 2

# Assumptioin
# no upper case in the str
# whitespace?? yes

# * Two Pointer Approach
# * create ttwo pointers pointing to first index and last index
# * iterate over the str until left pointer passes right pointer
#    * check if left pointer var isn't equal to right pointer var
#      * return False
#    * move left pointer to right by 1
#    * move right pointer to left by 1
# * return True

def is_palindrome(s):
  l = 0
  r = len(s) - 1
  while l < r:
    if s[l] != s[r]:
      return False
    l += 1
    r -= 1

  return True 

s = "amanaplanacanalpanama"
s2 = "hello world"

print(is_palindrome(s))
print(is_palindrome(s2))