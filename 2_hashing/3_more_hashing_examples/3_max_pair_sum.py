# Given an array of integers nums, find the maximum value of nums[i] + nums[j], 
# where nums[i] and nums[j] have the same digit sum (the sum of their 
# individual digits). Return -1 if there is no pair of numbers with the same digit sum.

TEST_CASES = [
    [[14,25,76,31,12,54,41], 55],
    [[14,25,76,31,12,54,11], -1],
    [[14,25,76,32], 46],
]

def max_pair_sum(nums):
    ans = -1
    digit_sums = {}

    for num in nums:
        digits = list(str(num))
        key = sum(map(lambda x: int(x), digits))

        if key not in digit_sums:
            digit_sums[key] = []

        digit_sums[key].append(num)

    for digit_sum, nums in digit_sums.items():
        if len(nums) < 2:
            continue

        sorted_nums = sorted(nums)
        ans = max(ans, sorted_nums[-2] + sorted_nums[-1])

    return ans

if __name__=="__main__":
    for case in TEST_CASES:
        print(max_pair_sum(case[0]) == case[1])

