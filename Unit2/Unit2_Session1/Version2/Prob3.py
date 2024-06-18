#unit 2
#session 1
#ver 2
#problem 3

#should print the value associated with the key
#print none if the key doesn't exist
def get_description(info, keys):
  for key in keys:
    if key in info:
      print(info[key])

    else:
      print(None)


info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)