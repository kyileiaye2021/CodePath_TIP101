#unit 4
#session 2
#ver 1
#prob 6

# Sliding Window Technique
# create a boolean var to keep track of dupllicates
# iterate over the lst 
#   slide the window
#   check the eles in the window are equal
#   return False if there are not duplicates
# return True

def check_duplicate(window):
  return len(window) == len(set(window))

def contains_nearby_duplicate(lst, k):
  is_duplicated = True

  for i in range(len(lst)-k):
    window = lst[i:i+k+1]
    is_duplicated = check_duplicate(window)
    if not is_duplicated:
      return False

  return is_duplicated

lst = [1, 2, 3, 1, 2, 3]
lst2 = [1, 0, 1, 1]
print(contains_nearby_duplicate(lst, 2))
print(contains_nearby_duplicate(lst2, 1))
