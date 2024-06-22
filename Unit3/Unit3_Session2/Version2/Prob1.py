#unit 3
#session 2
#ver 2
#prob 1

#create an empty list
#iterate thru the s string
  #convert the char to int
  #put it in the list
#return the list


def string_to_integer_mapping(s):
  integer_lst = []
  for ele in s:
    integer_lst.append(int(ele))

  return integer_lst

s="12345"
print(string_to_integer_mapping(s))