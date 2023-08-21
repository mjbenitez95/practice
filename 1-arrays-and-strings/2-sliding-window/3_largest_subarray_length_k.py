TEST_CASES = [
    [[3, -1, 4, 12, -8, 5, 6], 4, 18],
    [[2, -4, 3, 6, -1, 7, 1], 3, 12],
    [[1, -1, 0, 2, 1, -1, 4], 2, 3],
]

def largest_subarray_length_k(nums, k):
    subarray_sum = 0

    # build first window
    for right in range(k):
        subarray_sum += nums[right]
    
    ans = subarray_sum

    # iterate the rest of the array
    for right in range(k, len(nums)):
        subarray_sum += nums[right]
        subarray_sum -= nums[right - k]
        ans = max(ans, subarray_sum)

    return ans

if __name__ == "__main__":
    for case in TEST_CASES:
        print(largest_subarray_length_k(case[0], case[1]) == case[2])

