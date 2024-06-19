#unit 2
#session 1
#ver 1
#prob 2

#string is immutable
#create a new str
#splitting the char into a list
#replace the first char of the list with the last char of the str
#replace the last char of the list with the first char of the str
#iterate over the list and concatenate the curr ele of the list into the new str
#return the str



def swap_ends(my_str):
  swap_str = ""
  my_str_list = list(my_str)
  my_str_list[0] = my_str[-1]
  my_str_list[-1] = my_str[0]
  for i in my_str_list:
    swap_str += i
  return swap_str



my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)

