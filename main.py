def reverse_prefix(word, ch):
  second = 0
  for i, ele in enumerate(word):
    if ele == ch:
      second = i
      break

  char_list = list(word)
  first = 0

  while first < second:
    temp = char_list[first]
    char_list[first] = char_list[second]
    char_list[second] = temp
    first += 1
    second -= 1
    
  return "".join(char_list)


word = "abcdefd"
rev_word = reverse_prefix(word, "d")
print(rev_word)

word2 = "helloworld"
rev_word2 = reverse_prefix(word2, "w")
print(rev_word2)

word3 = "xyzxyz"
rev_word3 = reverse_prefix(word3, "a")
print(rev_word3)
