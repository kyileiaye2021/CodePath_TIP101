#Unit 7
#session 1
#ver 3
#prob 1

#time complexity: O(n)
#space complexity: O(n) recursion depth being equal to the amount of s
def insert_stars(s):
    # If the string is empty or has only one character, return it as is
    if len(s) <= 1:
        return s
    # Otherwise, insert '*' between the first character and the rest, then recurse
    else:
        return s[0] + '*' + insert_stars(s[1:])

print(insert_stars('abc'))

#Time complexity : O(n)
#Space complexity: O(n)
def insert_stars_iterative(s):
  res = ''
  if len(s) <= 1:
    return s
  for i in range(len(s)):
    if i != len(s) - 1:
      res += s[i] + "*"
    else:
      res += s[i]

  return res
print(insert_stars_iterative('abc'))
