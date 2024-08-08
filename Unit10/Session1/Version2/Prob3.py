#unit 10
#session 1
#ver 2
#prob 3

# Valid Word Abbreviation
# Happy cases
# word = "s ubstitutio n", abbrev = s10n", return True
# word = "su bst i t u ti on", abbrev = "su3i1u2on", return True

# Edge cases
# word = "s ubsti tutio n", abbrev = "s55n", return False (adjacen substitutue)
# word = "substitution" abbrev = s010n, return False (leading zeros)

# Plan 
# Two pointer
# create a pointer | one pointing to the word | another pointing to the abbrev
# iterate until word and abbr reaches to its end
#   check if the abbr pointer points to digit
#     check if the abbr pointer points to is 0
#        return False
#     num = 0
#     while abbr pointer is less than the length of abbr and the current abbr pointer val is digit
#        num * 10 + abbr pointer val
#    increment the word pointer by num val
#   check if the curr word pointer val and abbr pointer val are not the same
#     return False
#   increment both pointers by 1
# if word and abbr pointers are not the same as their lengths, return False
# otherwise, return true

def valid_word_abbreviation(word, abbr):
  word_ptr = 0
  abbr_ptr = 0

  while word_ptr < len(word) and abbr_ptr < len(abbr):
    if abbr[abbr_ptr].isdigit():

      if abbr[abbr_ptr] == '0':
        return False

      num = 0
      while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
        num = num * 10 + int(abbr[abbr_ptr])
        abbr_ptr += 1

      word_ptr += num

    else:

      if word[word_ptr] != abbr[abbr_ptr]:
        return False

      word_ptr += 1
      abbr_ptr += 1

  return word_ptr == len(word) and abbr_ptr == len(abbr)


word = "substitution"
abbrev = "s10n"
print(valid_word_abbreviation(word, abbrev)) # true

word = "substitution"
abbrev = "su3i1u2on"
print(valid_word_abbreviation(word, abbrev)) # true

word = "s ubsti tutio n"
abbrev = "s55n"
print(valid_word_abbreviation(word, abbrev)) # false

word = "substitution"
abbrev = "s010n"
print(valid_word_abbreviation(word, abbrev)) # false
