#unit 7
#session 1
#ver 3
#prob 2

#empty string should have size 0
def string_length(s):
  #base case
  if len(s) == 0 or not s:
    return 0

  #recursive case
  return 1 + string_length(s[1:])

print(string_length('abc'))
# Example Input: 'abc'

# Expected Output: 3