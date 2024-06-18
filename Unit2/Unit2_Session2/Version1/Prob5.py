#unit 2
#session 2
#ver1
#prob 5

def find_majority_element(elements):
  dictionary = {}

  for i in elements:
    if i not in dictionary:
      dictionary[i] = 1
    else:
      dictionary[i] += 1


  for key in dictionary:
    if dictionary[key] > (len(elements)/2):
      return key

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))