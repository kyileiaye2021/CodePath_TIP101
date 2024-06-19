#unit 3
#session 1
#ver 3
#prob 3

#create a str
#use the for loop to iterate over the string
  #if the curr char in string
    #return the index
#return None

def first_repeated_char(s):
  unique_str = ""
  for i in range(len(s)):
    if s[i] in unique_str:
      return i
    unique_str += s[i]

  return None

s = "hello world"
s2 = "aAbBCC"
s3 = "abcdefg"

print(first_repeated_char(s))
print(first_repeated_char(s2))
print(first_repeated_char(s3))