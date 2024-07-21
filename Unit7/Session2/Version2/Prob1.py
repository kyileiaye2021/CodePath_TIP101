#unit 7
#session 2
#ver 2
#prob 1

# is it possible that the sub is not in s? #possible
# can either of s be null or empty? #no
# can the size of s and sub be the same? #yes

# hash map approach
# * create a dict for s and dict for sub, then compare and operate on those dicts

# sliding window approach
# * slice the string when we iterate the s and compare the slic with sub

# Happy case
# abcdeabcde, abc -> 2

# Edge case
# abcde, fg -> 0
# abc, abcd -> 0
# none, ab -> 0

'''
High level plan
base case: if the length of the sub is greater than s, return 0
recursive case: check the curr seg of the str is equal to sub

low level plan
# find the len of the sub
base case:
# check if the len of current main str is less than sub
#  return 0

recursive case:
# check if the curr sub string from current s position to len of the sub is the same as sub:
#    call func with the arg of the str starting from the next sub len of the curr position (to avoid the overlap)
# otherwise 
#    move the s curr to next char in the str
'''
def count_substring(s, sub):
  sub_len = len(sub)

  #base case
  if sub_len > len(s): #the size of curr s str is greater than the size of sub
    return 0

  #recursive case
  if s[0:sub_len] == sub: # the curr slice of the str is equal to the sub (O(m))
    return 1 + count_substring(s[sub_len:], sub) # ignore the checked slice to avoid overlap
  else:
    return count_substring(s[1:], sub) # move to next char in the str O(n)

print(count_substring('abcdeabcde','abc')) #2
print(count_substring('abcde', 'fg')) #0
print(count_substring('abc','abcde')) #0

#Time complexity is O(n * m), check every char in every func if the sub is not in s 
# in slicing the curr position, it takes O(m)
#Space complexity is O(n), the func is called the size of the whole lst in worse case 