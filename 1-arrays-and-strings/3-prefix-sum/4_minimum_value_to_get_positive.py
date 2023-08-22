# Given an array of integers `nums``, you start with an initial positive value startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

TEST_CASES = [
    [[-3,2,-3,4,2], 5],
    [[1,2], 1],
    [[1,-2,-3], 5]
]

def minimum_value_to_get_positive(nums):
    prefix_sum = [nums[0]]
    has_negatives = nums[0] < 0

    for i in range(1, len(nums)):
        running_sum = nums[i] + prefix_sum[i - 1]
        if running_sum < 0:
            has_negatives = True
        prefix_sum.append(running_sum)

    if has_negatives == False:
        return 1

    return abs(min(prefix_sum)) + 1

if __name__ == "__main__":
    for case in TEST_CASES:
        print(minimum_value_to_get_positive(case[0]) == case[1])