#unit 3
#session 1
#ver 3
#prob 6

#create a map {"Roman ele": "numerical val"}
#integer_numerical_val = 0
#iterate over the string s
 #check the curr char val < next char val
  #subtract the curr char val from integer_numerical_val
#else: add the curr char val to integer_numerical_val
#return integer_numerical_val

def roman_to_int(s):
  roman_int_map = {'I':1,
                   'V':5,
                   'X':10,
                   'L':50,
                   'C':100,
                   'D':500,
                   'M':1000
                  }
  integer_numerical_val = 0

  for i in range(len(s)):
    if i + 1 < len(s) and roman_int_map[s[i]] < roman_int_map[s[i+1]]:
      integer_numerical_val -= roman_int_map[s[i]]
    else:
      integer_numerical_val += roman_int_map[s[i]]

  return integer_numerical_val


s = "XL"
print(roman_to_int(s))

s2 = "LVIII"
print(roman_to_int(s2))

s3 = "MCMXCIV"
print(roman_to_int(s3))



