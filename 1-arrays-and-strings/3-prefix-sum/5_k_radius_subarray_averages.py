# You are given a 0-indexed array nums of n integers, and an integer k.

# The k-radius average for a subarray of nums centered at some index i 
# with the radius k is the average of all elements in nums between the 
# indices i - k and i + k (inclusive). If there are less than k elements 
# before or after the index i, then the k-radius average is -1.

# Build and return an array avgs of length n where avgs[i] is the k-radius
# average for the subarray centered at index i.

# The average of x elements is the sum of the x elements divided by x, 
# using integer division. The integer division truncates toward zero, which
# means losing its fractional part.

import math

TEST_CASES = [
    [[7, 4, 3, 9, 1, 8, 5, 2, 6], 3, [-1, -1, -1, 5, 4, 4, -1, -1, -1]],
    [[100000], 0, [100000]],
    [[8], 100000, [-1]]
]

def k_radius_subarray_averages(nums, k):
    prefix_sum = [nums[0]]
    # O(n space)
    ans = [-1] * len(nums)

    # O(n) space and time
    for i in range(1, len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[i - 1])

    # O(n) time
    for i in range(len(nums)):
        if i < k or i + k >= len(nums):
            continue
        
        ans[i] = math.floor((prefix_sum[i + k] - prefix_sum[i - k] + nums[i - k]) / (2 * k + 1))
    
    return ans

def k_radius_subarray_averages_optimized(nums, k):
        # if radius is 0, average is just the element
        if k == 0:
            return nums

        n = len(nums)
        subarray_length = (2 * k) + 1
        prefix_sum = [0] * (n + 1)
        ans = [-1] * n

        if subarray_length > n:
            # no k-radius subarrays exist
            return ans

        # generate prefix_sums 
        # 'prefix[i + 1]' will be sum of all elements of 'nums' from index '0' to 'i'.

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # iterate only on the k-radius subarrays
        for i in range(k, n - k):
            subarray_sum = prefix_sum[i + k + 1] - prefix_sum[i - k]
            ans[i] = math.floor(subarray_sum / subarray_length)
        
        return ans

def k_radius_subarray_sliding_window(nums, k):
    n = len(nums)
    ans = [-1] * n
    window_size = (2 * k) + 1

    # if looking at only 1 element, avg is just that element
    if window_size == 1:
        return nums

    # if no k-radius subarrays exist, all values are -1
    if window_size > n:
        return ans

    # build first window
    cur_sum = sum(nums[:window_size])
    ans[k] = cur_sum // window_size

    # window will iterate at the right edge
    # but answer will be updated at the middle
    # start here --------v
    # [7, 4, 3, 9, 1, 8, 5, 2, 6]
    for i in range(window_size, n):
        cur_sum = cur_sum - nums[i - window_size] + nums[i]
        ans[i - k] = cur_sum // window_size

    return ans

if __name__ == "__main__":
    for case in TEST_CASES:
        print(
            k_radius_subarray_averages(case[0], case[1]) == case[2], 
            k_radius_subarray_averages_optimized(case[0], case[1]) == case[2],
            k_radius_subarray_sliding_window(case[0], case[1]) == case[2]
        )