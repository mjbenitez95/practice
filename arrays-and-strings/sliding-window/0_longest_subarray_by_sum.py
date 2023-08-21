TEST_CASES = [
    [[1,2,3,4,5,6], 4, 2],
    [[1,1,1,1,1,1], 4, 4],
    [[3,2,1,2,3,1], 5, 3],
    [[6,2,1,6,1,1,3,1], 6, 4],
    [[1,1,3,2,6,2,1,1,1,2,1], 8, 6],
]

def longest_subarray_by_sum(nums, sum):
    left = 0
    cur_sum = 0
    max_length = 0

    for right in range(0, len(nums)):
        cur_sum += nums[right]

        while cur_sum > sum:
            cur_sum -= nums[left]
            left += 1

        cur_length = right - left + 1
        max_length = max(max_length, cur_length)

    return max_length

if __name__ == "__main__":
    for case in TEST_CASES:
        print(longest_subarray_by_sum(case[0], case[1]) == case[2])

