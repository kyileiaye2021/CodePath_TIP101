  #unit 3
  #session 1
  #ver 3
  #prob 2

#create a new str
#iterate over the s string starting from n index to the end
  #add each curr char to the new str
#itearate over the s string from the start to n-1 index
  #add curr char to the new str
#return the string

def rotate_left(s, n):
  res_str = ""
  for char in s[n : len(s)]:
    res_str += char
  for char in s[0:n]:
    res_str += char
  return res_str

s = "rotation"
print(rotate_left(s, 2))