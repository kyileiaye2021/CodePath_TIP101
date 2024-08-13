#unit 10
# session 1
#ver 3
# Prob 2

# What if the list is empty or there is only one num in the list?
# is the list sorted?

# Happy cases:
# Input: nums = [1, 2, 2, 4]
# Expected Output: [2, 3]

# Edge cases
# input: nums = []
# expected output: []

# input: nums = [1]
# expected output: []

# 1) Calculate the expected sum of numbers from `1` to `n` using the formula `n * (n + 1) // 2`.
# 2) Calculate the expected sum of squares of numbers from `1` to `n` using the formula `n * (n + 1) * (2 * n + 1) // 6`.
# 3) Calculate the actual sum of the given numbers.
# 4) Calculate the actual sum of squares of the given numbers.
# 5) Find the difference between the expected and actual sums (`sum_diff`).
# 6) Find the difference between the expected and actual sum of squares (`sum_squares_diff`).
# 7) Use these differences to solve for the missing and duplicate numbers:
#     a) `missing_plus_duplicate = sum_squares_diff // sum_diff`
#     b) `missing = (sum_diff + missing_plus_duplicate) // 2`
#     c) `duplicate = missing_plus_duplicate - missing`
# 8) Return the duplicate and missing numbers as a list.

def find_error_nums(nums):
  n = len(nums)
  expected_sum = n * (n + 1) // 2
  expected_squared_sum = n * (n + 1) * (2 * n + 1) // 6

  actual_sum = sum(nums)
  actual_squared_sum = sum(x * x for x in nums)

  sum_diff = abs(expected_sum - actual_sum)
  squared_sum_diff = abs(expected_squared_sum - actual_squared_sum)

  missiing_plus_duplicates = squared_sum_diff // sum_diff
  missing = (missiing_plus_duplicates + sum_diff) // 2
  duplicates = missiing_plus_duplicates - missing

  return [duplicates, missing]

nums = [1,2,2,4]
print(find_error_nums(nums)) #[2,3]

nums = [1,1]
print(find_error_nums(nums)) # [1,2]

nums = [2,2]
print(find_error_nums(nums)) #[1,2]

