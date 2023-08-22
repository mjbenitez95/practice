TEST_CASES = [
    [[1, 12, -5, -6, 50, 3], 4, 12.75],
    [[5], 1, 5],
]

def maximum_average_subarray(nums, k):
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

    return ans/k

if __name__ == "__main__":
    for case in TEST_CASES:
        print(maximum_average_subarray(case[0], case[1]) == case[2])

