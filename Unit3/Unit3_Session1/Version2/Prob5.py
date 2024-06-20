#unit 5
#session 1
#ver 2
#prob 5

#create a frequency map
#iterate over the str
  #fill the frequency map
#create a new_str
#iterate thru the frequency map
  #add the key and value to new_str
#if the len of new_str > orig str
  #return the new_str
#return the orig str

def compress_string(my_str):
  frequency_map = {}
  for char in my_str:
    if char in frequency_map:
      frequency_map[char] += 1
    else:
      frequency_map[char] = 1
      
  new_str = ""
  for key in frequency_map:
    new_str += key + str(frequency_map[key])

  if len(new_str) < len(my_str):
    return new_str

  return my_str

my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
print(compressed_Str)

my_str2 = "abcde"
compressed_Str2 = compress_string(my_str2)
print(compressed_Str2)