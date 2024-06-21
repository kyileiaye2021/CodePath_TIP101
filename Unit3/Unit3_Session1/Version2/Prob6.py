#unit 3
#session 1
#ver 2
#prob 6

#create left and right pointer firstly initialized to 0
#iterate through the haystack str
  #check if the curr char in needle str
  #if it's,
      #move the right pointer to the right by 1
      #check the len(needle) == right - left:
        #return left pointer
  #if it's not,
      #move the right pointer to the right by 1
      #set the left pointer = right pointer
#return -1 if needle is not a substring of haystack

def find_the_needle(haystack, needle):
  left, right = 0, 0

  for char in haystack:
    if char in needle:
      right += 1
      if len(needle) == right - left:
        return left

    else:
      right += 1
      left = right

  return -1

haystack = "tobeornottobe"
needle = "be"
print(find_the_needle(haystack, needle))

haystack2 = "leetcode"
needle2 = "leeto"
print(find_the_needle(haystack2, needle2))
