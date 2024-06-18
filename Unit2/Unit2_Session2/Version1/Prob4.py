#iterate over the list
#check if the curr item is in the dict
def count_occurrences(nums):
  dictionary = {}
  for i in nums:
    if i not in dictionary:
      dictionary[i] = 1

    else:
      dictionary[i] += 1
  return dictionary

nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))


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