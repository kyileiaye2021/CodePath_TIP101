#unit 2
#session 1
#ver 1
#problem 3

#iterate over the dict
#create a boolean var to keep track of the target key existing in the dict or not
#check the target key is in the dict
#if it's, print key and value
#if it's not, print pair not exist

def print_pair(dictionary, target_key):
  is_exist = False
  for key in dictionary:
    if key == target_key:
      print("Key:",key)
      print("Value:",dictionary[key])
      is_exist = True

  if not is_exist:
    print("The pair does not exist!")


dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")
