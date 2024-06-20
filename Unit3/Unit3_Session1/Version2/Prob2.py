#UNIT 3
#session 1
#ver 2
#prob 1

#create a new str
#iterate through the orig str
  #if curr index != n 
    #put it in the new str
#return the new str

def remove_char(s, n):
  new_str = ""
  for i in range(len(s)):
    if i != n:
      new_str += s[i]
  return new_str

s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)
