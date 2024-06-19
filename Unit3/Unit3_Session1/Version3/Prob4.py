#unit 3
#session 1
#ver 3
#prob 4

#iterate over the str 2
  #check the curr char not in str1
    #return the curr char

def find_difference(s1, s2):
  for char in s2:
    if char not in s1:
      return char
      
s1 = "abcd"
s2 = "baedc"
print(find_difference(s1, s2))