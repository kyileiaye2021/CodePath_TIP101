
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
