# Given an integer array nums and an integer k, find the number 
# of subarrays whose sum is equal to k.

from collections import defaultdict

TEST_CASES = [
    [[1, 2, 1, 2, 1], 3, 4],
    [[7, 8, -4, 4, 5], 15, 2],
    [[1, 4, 3, 2, 1, -5, 4, 3, 1], 1, 4],
]

def subarray_sum_equals_k(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1

    return ans

if __name__ == "__main__":
    for case in TEST_CASES:
        print(subarray_sum_equals_k(case[0], case[1]) == case[2])