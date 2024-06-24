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