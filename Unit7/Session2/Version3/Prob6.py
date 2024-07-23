#unit 7
#session 2
#ver 3
#prob 6

# A nice string

def is_nice(s):
  lower_count = {}
  upper_count = {}

  for char in s:
    if 'a' <= char <= 'z':
      if char in lower_count:
        lower_count[char] += 1
      else:
        lower_count[char] = 1

    elif 'A'<= char <= 'Z':
      if char in upper_count:
        upper_count[char] += 1
      else:
        upper_count[char] = 1

  for key in lower_count:
    if key.upper() not in upper_count:
      return False

  for key in upper_count:
    if key.lower() not in lower_count:
      return False
  return True

def longest_nice(s):
  if len(s) < 2:
    return "" #no substring

  if is_nice(s): #if the string or substring is nice, return the str
    return s

  mid = len(s) // 2
  left = longest_nice(s[:mid])
  right = longest_nice(s[mid:])

  if len(left) >= len(right):
    return left
  else:
    return right

def longest_nice_substring(s):
  if len(s) < 2:
    return "" #no substring
  return longest_nice(s)

s = "YazaAay"
print(longest_nice_substring(s))