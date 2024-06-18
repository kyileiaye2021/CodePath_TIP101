#unit 2
#session 1
#ver 1
#problem 2

#2 lists as param
#the sizes of the two lists should be the same
#create a dict to store the key and values
#iterate over the keys list
#assign the key and value eles in the dict
#return dict
def create_dictionary(keys, values):
  dict = {}
  for i in range(len(keys)):
    dict[keys[i]] = values[i]

  return dict

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys,values))