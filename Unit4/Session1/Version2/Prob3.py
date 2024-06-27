#unit 4
#session 1
#ver 2
#prob 3

#Evaluate Palindrome
def is_palindrome(s):
  # create a new list
  reverse = s[::-1] # time complexity - O(n) | space complexity - O(n)
  # compare two string 
  return reverse == s
#Two pointer technique is better than reverse list technique
