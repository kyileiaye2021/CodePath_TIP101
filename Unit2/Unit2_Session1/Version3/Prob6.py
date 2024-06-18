#unit 2
#session 1
#ver 3
#prob 6

#create a list
#iterate over the dict
#check if the key is odd or not
#check if the value is even
#assign in the list
#return the list

def odd_keys_even_values(dictionary):
  lst = []
  for dict in dictionary:
    if dict % 2 != 0 and dictionary[dict] % 2 == 0:
        lst.append(dict)
  return lst

dictionary = {1: 2, 2: 6, 3: 5, 4: 4, 5: 8}
final_list = odd_keys_even_values(dictionary)
print(final_list)