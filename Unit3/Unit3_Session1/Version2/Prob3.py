#unit 3
#session 1
#ver 2
#prob 3

#create a vowel_str
#create a var to store total count
#make every char of the orig str to lower cases
#iterate over the orig str
  #check the curr char is vowel or not
    #increment total count by 1
#return total count

def vowel_count(s):
  vowel_str = 'aeiou'
  total_count = 0
  s = s.lower()
  
  for char in s:
    if char in vowel_str:
      total_count += 1

  return total_count

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)
