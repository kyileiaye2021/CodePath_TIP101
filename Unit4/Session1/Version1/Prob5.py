#unit 4
#session 1
#ver 1
#prob 5

# Questions
# Can there be upper cases and lower cases in the words? #Yes
# Can the str in the lists be case sentitive? #Yes
# Can the string list be empty or null? #No return empty str
# Can there be more than one string that is panlindrome? Yes but we will return the first one

# Assumption
# There can be more than one element in the list that is panlindrome 
# The list can also be empty list
# The list can also contain no panlindrom string

# High Level Planning
# * Reversed String Appraoch
#    * iterate over the list. in each iteration, reverse the word. iterate over the current word and compare each curr 
#      corresponds to curr char in reverse list.
# * Two Pointer Approach
#    * iterate over the list. in each iteration, create l and r pointers pointing to index 0 and last index
#    * compare the two and return accordingly

# Low Level Planning
# * Two pointer approach
# * create a new str to store the panlindrome str
# * Iterate over the list
#    * In each iteratioin, 
#        * create l to 0 and r pointers to last index of the lst
#        * iterate over each curr string until l passes the r
#            * check if l var is not equal to r var
#                * stop the inner loop
#            * concatenate the cur char to the new str
# return the new created string

def first_palindrome(words):

  res = ""
  for word in words:
    l = 0
    r = len(word) - 1
    is_palindrome = True
    while l < r:
      if word[l] != word[r]:
        is_palindrome = False
      l += 1
      r -= 1

    if is_palindrome:
      return word
  return res

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)

