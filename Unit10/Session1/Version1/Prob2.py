
#unit 1
#session 1
#ver 1
#Problem 2: Best Time to Buy & Sell Stock

# create two pointers (l, r = 0, 1)
#Iterate through the list
#   if r val is greater than l val
#     calculate the profit and get the max val
#   else:
#     move l to r
#   increment r by 1

def max_profit(prices):
  maximum_profit = 0
  l, r = 0, 1

  while r < len(prices):
    if prices[r] < prices[l]:
      l = r

    else:
      profit = prices[r] - prices[l]
      maximum_profit = max(maximum_profit, profit)

    r += 1

  return maximum_profit


prices = [7,1,5,3,6,4]
print(max_profit(prices))

prices = [7,6,4,3,1]
print(max_profit(prices))

# Time complexity - O(n)
# Space complexity - O(1) 