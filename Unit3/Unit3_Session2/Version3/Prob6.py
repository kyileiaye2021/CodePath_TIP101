#unit 3
#session 2
#version 3
#prob 6

#some edge cases
# [], n = 1, False
# [0,0], n = 1, True
# [0,0,0,0], n = 2, True
# [1,1,1,1], n = 1, False
# [0,1,1,0], n = 1, False
# [1,0,0,0,1], n = 1, True

# High Level Plan
# iterate over the list
# if the curr ele is the 0, check before and after the current ele

#Low Level Plan
# create a counter to store the num of possibilities of flowers to plant
# iterate over the flowerbed lst
     # if the curr ele is 0 
        # check prev ele and next ele is 0
            # update counter (increment by 1)
#if n <= counter:
    #return True
#return False

def can_place_flowers(flowerbed, n):
  if len(flowerbed) == 0 or not flowerbed:
    return False

  counter = 0
  for i in range(len(flowerbed)): 

    if flowerbed[i] == 0:

      if i == 0: 
        if flowerbed[i + 1] == 0:
          counter += 1
      elif i == len(flowerbed) - 1:
        if flowerbed[i-1] == 0:
          counter += 1
      else:
        if flowerbed[i-1] == 0 and flowerbed[i + 1] == 0:
          counter += 1

    else:
      continue

  if n <= counter:
    return True
  return False

flowerbed = [1,0,0,0,1]
approved = can_place_flowers(flowerbed, 1)
approved2 = can_place_flowers(flowerbed, 2)
print(approved) #True
print(approved2) #False

flowerbed3 = []
approved3 = can_place_flowers(flowerbed3, 1)
print(approved3) #False

flowerbed4 = [0,0]
approved4 = can_place_flowers(flowerbed4, 1)
print(approved4) #True

flowerbed5 = [0,1,1,0]
approved5 = can_place_flowers(flowerbed5, 1)
print(approved5) #False



