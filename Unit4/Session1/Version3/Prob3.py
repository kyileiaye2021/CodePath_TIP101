#unit 4
#session1
#ver 3
#prob 3

def two_sum(nums, target):
  prev_map = {}  # Value to index mapping

  for i in range(len(nums)):
      diff = target - nums[i]
      if diff in prev_map:
          return [prev_map[diff], i]
      prev_map[nums[i]] = i

# Time complexity - O(n)
# Space complexity - O(n)
