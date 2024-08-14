#unit 10
#session 2
#ver 1
#prob 3

# Are the case sensitive?

'''Happy CAse'''
# input 
# s1 - "ABCABC", s2 - "ABC"
# output - "ABC"

# input 
# s1 - "ABABAB", s2 - "ABAB"
# output - "AB"

'''Edge CAse'''
# s1- "LEet", s2 - "Code"
# output - ""

# 1) Define a helper function `is_divisible(s, t)` that checks if string `t` divides string `s`.
# 2) Find the GCD of the lengths of `str1` and `str2`.
# 3) Use the GCD length to extract a candidate substring from `str1`.
# 4) Check if this candidate substring divides both `str1` and `str2`.
# 5) Return the candidate substring if it divides both strings; otherwise, return an empty string.

def gcd_of_stings(str1, str2):
  def is_divisible(s,t):
    if len(s) % len(t) != 0:
      return False

    repeat = len(s) // len(t)
    return t * repeat == s

  def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

  gcd_length = gcd(len(str1), len(str2))
  gcd_str = str1[:gcd_length]

  if is_divisible(str1, gcd_str) and is_divisible(str2, gcd_str):
    return gcd_str
  else:
    return ""

str1 = "ABCABC"
str2 = "ABC"
print(gcd_of_stings(str1, str2)) #ABC

str1 = "ABABAB"
str2 = "ABAB"
print(gcd_of_stings(str1, str2)) # AB

str1 = "LEET"
str2 = "CODE"
print(gcd_of_stings(str1, str2)) # ""
