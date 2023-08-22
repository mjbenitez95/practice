# Given an integer array nums, find the number of ways 
# to split the array into two parts so that the first 
# section has a sum greater than or equal to the sum of 
# the second section. The second section should have at 
# least one number.

TEST_CASES = [
    [[1, 2, 3, 4, 5], 1],
    [[5, 4, 3, 2, 1], 3],
    [[0, 0, 1, 0], 1],
    [[0, 0, 0, 1], 0],
    [[20, -10, -10, -5], 3],
]

def num_ways_to_split(nums):
    n = len(nums)

    prefix_sum = [nums[0]]
    for i in range(1, n):
        prefix_sum.append(nums[i] + prefix_sum[i-1])

    ans = 0
    for i in range(n - 1):
        if prefix_sum[i] >= (prefix_sum[n - 1] - prefix_sum[i]):
            ans += 1

    return ans

# use integers to track sums,
# improving space complexity from O(n)
# to O(1).
def num_ways_to_split_two(nums):
    total = 0
    ans = 0

    for i in range(len(nums)):
        total += nums[i]

    left = 0
    for i in range(len(nums) - 1):
        left += nums[i]
        right = total - left
        if left >= right:
            ans += 1

    return ans

if __name__ == "__main__":
    for case in TEST_CASES:
        print(num_ways_to_split(case[0]) == case[1], num_ways_to_split_two(case[0]) == case[1])