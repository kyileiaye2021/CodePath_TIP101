#unit 10
#session 1
#ver 2
#prob 1

'''Edge Cases'''
# input - [0,0,0,0], n = 3
# output - False

# input - [1,1,1,1], n = 1
# output = false

'''Happy Case'''
# input - [1,0,0,0,1], n = 1
# output - True

# input - [1,0,0,0,1], n = 2
# output - False

# Plan
# iterative approach
# iterate from index 1 to second to last element
#   check if the curr char is 0
#      check if the prev char and next char are also 0
#         decrement n by 1
#         replace the curr char val with 1
# if n is 0, return true
# otherwise, return false

def can_place_flowers(flowerbed, n):
  
  for i in range(1, len(flowerbed) - 1):
    if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
        n -= 1
        flowerbed[i] = 1

  return n == 0

flowerbed = [0,0,0,0]
n = 3
print(can_place_flowers(flowerbed, n)) # false

flowerbed = [1,1,1,1]
n = 3
print(can_place_flowers(flowerbed, n)) # false

flowerbed = [1,0,0,0,1]
n = 1
print(can_place_flowers(flowerbed, n)) # true

flowerbed = [1,0,0,0,1]
n = 2
print(can_place_flowers(flowerbed, n)) # false

    
  