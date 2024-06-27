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