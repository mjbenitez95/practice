# Given an integer array nums, find the number of ways 
# to split the array into two parts so that the first 
# section has a sum greater than or equal to the sum of 
# the second section. The second section should have at 
# least one number.

TEST_CASES = [
    [[1, 2, 3, 4, 5], 1],
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

if __name__ == "__main__":
    for case in TEST_CASES:
        print(num_ways_to_split(case[0]) == case[1])